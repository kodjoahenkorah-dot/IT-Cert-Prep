"""CompTIA Security+ SY0-701 practice questions — Domain 5 (Security Program
Management and Oversight), file C.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 5 in
``_topic_labels.json``. Scenarios are brand-new relative to d5a.py and
d5b.py.
"""

QUESTIONS = [
    {
        "id": "nd5c-001",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A law firm's document management system is valued at $650,000 (asset value, AV). Incident response "
            "data from a similar prior ransomware event indicates that a successful attack typically encrypts and "
            "renders unusable 25% of the system's value (exposure factor, EF) before containment. What is the "
            "single loss expectancy (SLE) for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$162,500",
                "correct": True,
                "rationale": "Correct. SLE = AV x EF = $650,000 x 0.25 = $162,500.",
            },
            {
                "id": "b",
                "text": "$487,500",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the complement of the exposure factor (75%) instead of the stated "
                    "25% EF ($650,000 x 0.75), which is not what the scenario describes."
                ),
            },
            {
                "id": "c",
                "text": "$650,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the asset value with the exposure factor ignored entirely. SLE must scale "
                    "AV by the proportion of value actually expected to be lost."
                ),
            },
            {
                "id": "d",
                "text": "$2,600,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from dividing AV by EF ($650,000 / 0.25) rather than multiplying. "
                    "Dividing produces a figure larger than the asset itself, which cannot be a valid SLE."
                ),
            },
        ],
        "explanation": (
            "SLE = Asset Value (AV) x Exposure Factor (EF). Here, $650,000 x 0.25 = $162,500. EF must be "
            "multiplied against AV, not subtracted from 1 and applied, divided into AV, or ignored."
        ),
    },
    {
        "id": "nd5c-002",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A single loss expectancy (SLE) of $95,000 has been calculated for a business email compromise (BEC) "
            "wire-fraud scenario. Fraud analytics show this type of incident has occurred twice in the past 5 "
            "years at this organization. What is the annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$38,000",
                "correct": True,
                "rationale": (
                    "Correct. ARO = 2 events / 5 years = 0.4. ALE = SLE x ARO = $95,000 x 0.4 = $38,000."
                ),
            },
            {
                "id": "b",
                "text": "$237,500",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing SLE by ARO ($95,000 / 0.4) instead of multiplying, "
                    "which inflates the figure well beyond the single-loss amount."
                ),
            },
            {
                "id": "c",
                "text": "$95,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats ALE as identical to SLE, ignoring the annualized rate of occurrence "
                    "(the fact that this occurs twice, not once, per 5-year window)."
                ),
            },
            {
                "id": "d",
                "text": "$19,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading the frequency as once every 5 years (ARO = 1/5 = "
                    "0.2) instead of correctly accounting for both occurrences (ARO = 2/5 = 0.4)."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO. 'Twice in 5 years' converts to ARO = 2/5 = 0.4. $95,000 x 0.4 = $38,000."
        ),
    },
    {
        "id": "nd5c-003",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "Before mitigation, the ALE for phishing-driven business email compromise at a professional services "
            "firm is $180,000/year. A proposed initiative (advanced email security plus enforced DMARC, annual "
            "cost of safeguard, ACS, of $65,000) would reduce the ALE to $40,000/year. Using cost-benefit analysis "
            "of the control, what should the organization conclude?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The safeguard produces a net benefit of $75,000/year ($140,000 ALE reduction minus the "
                    "$65,000 ACS), so it is cost-justified."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Value of the control = (ALE_before - ALE_after) - ACS = ($180,000 - $40,000) - "
                    "$65,000 = $140,000 - $65,000 = $75,000. A positive figure means the safeguard is worth its "
                    "cost."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The safeguard produces a net benefit of $140,000/year, because the full ALE reduction "
                    "determines value regardless of the safeguard's cost."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores the $65,000 ACS entirely. Cost-benefit analysis requires subtracting "
                    "the cost of the safeguard from the ALE reduction it produces."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The safeguard produces a net benefit of $115,000/year, calculated as ALE_before minus ACS "
                    "($180,000 - $65,000)."
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
                    "The safeguard produces a net benefit of only $10,000/year, because the $65,000 ACS must be "
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
            "Value of a control = (ALE_before - ALE_after) - ACS = ($180,000 - $40,000) - $65,000 = $75,000/year "
            "net benefit, making the safeguard cost-justified."
        ),
    },
    {
        "id": "nd5c-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A logistics company's data warehouse is valued at $1,200,000 (AV). Security engineers estimate that a "
            "successful attack would destroy 15% of the warehouse's value (EF), and threat intelligence indicates "
            "this type of attack is expected to succeed 3 times per 10 years against comparable organizations. "
            "What is the annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$54,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $1,200,000 x 0.15 = $180,000. ARO = 3 events / 10 years = 0.3. "
                    "ALE = SLE x ARO = $180,000 x 0.3 = $54,000."
                ),
            },
            {
                "id": "b",
                "text": "$180,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the SLE ($1,200,000 x 0.15) with the ARO ignored entirely (effectively "
                    "treated as if ARO = 1, i.e., the event happens every year)."
                ),
            },
            {
                "id": "c",
                "text": "$360,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies ARO directly to the full asset value ($1,200,000 x 0.3) without "
                    "first applying the exposure factor, skipping the SLE step entirely."
                ),
            },
            {
                "id": "d",
                "text": "$5,400",
                "correct": False,
                "rationale": (
                    "Incorrect. This misreads '3 times per 10 years' as an ARO of 0.03 (3%) rather than the "
                    "correct 0.3 (3/10), understating the true frequency by a factor of 10."
                ),
            },
        ],
        "explanation": (
            "SLE = AV x EF = $1,200,000 x 0.15 = $180,000. ARO = 3/10 = 0.3. ALE = SLE x ARO = $180,000 x 0.3 = "
            "$54,000. Both the exposure factor and the annualized rate of occurrence must be applied, in order."
        ),
    },
    {
        "id": "nd5c-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA determines that a payroll system can tolerate a maximum of 8 hours of total downtime before "
            "causing unacceptable harm (maximum tolerable downtime, MTD). The technical recovery process — "
            "restoring the system from backups and bringing infrastructure back online — is expected to take 5 "
            "hours (recovery time objective, RTO). What is the maximum acceptable work recovery time (WRT) — the "
            "time needed after systems are technically restored to validate data integrity and resume full "
            "business operations — before the MTD is exceeded?"
        ),
        "options": [
            {
                "id": "a",
                "text": "3 hours",
                "correct": True,
                "rationale": (
                    "Correct. MTD = RTO + WRT, so WRT = MTD - RTO = 8 hours - 5 hours = 3 hours. This is the "
                    "remaining time budget after technical restoration for validation and business resumption."
                ),
            },
            {
                "id": "b",
                "text": "8 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This uses the full MTD without subtracting the RTO already consumed by technical "
                    "recovery, leaving no time budget for the RTO portion at all."
                ),
            },
            {
                "id": "c",
                "text": "13 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This adds RTO to MTD (8 + 5) instead of subtracting RTO from MTD, producing a "
                    "figure that exceeds the organization's stated maximum tolerable downtime entirely."
                ),
            },
            {
                "id": "d",
                "text": "5 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This restates the RTO value itself rather than calculating the remaining WRT "
                    "budget after the RTO portion of recovery has already elapsed."
                ),
            },
        ],
        "explanation": (
            "MTD (maximum tolerable downtime) = RTO (technical recovery time) + WRT (work recovery time to "
            "validate and resume operations). WRT = MTD - RTO = 8 - 5 = 3 hours."
        ),
    },
    {
        "id": "nd5c-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A critical network switch cluster experienced 6 separate outages over the past year, totaling 18 "
            "hours of cumulative downtime. What is the mean time to repair (MTTR) for this cluster?"
        ),
        "options": [
            {
                "id": "a",
                "text": "3 hours per incident",
                "correct": True,
                "rationale": (
                    "Correct. MTTR = total downtime / number of incidents = 18 hours / 6 incidents = 3 hours per "
                    "incident, the average repair time per outage."
                ),
            },
            {
                "id": "b",
                "text": "0.33 hours per incident",
                "correct": False,
                "rationale": (
                    "Incorrect. This inverts the formula (6 incidents / 18 hours) instead of dividing total "
                    "downtime by the number of incidents."
                ),
            },
            {
                "id": "c",
                "text": "18 hours per incident",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the total cumulative downtime across all 6 incidents, not divided by the "
                    "number of incidents to produce a per-incident average."
                ),
            },
            {
                "id": "d",
                "text": "1,457 hours per incident, because uptime should be divided by the failure count",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the MTBF formula (available operating hours minus downtime, divided "
                    "by failure count) to a question that is asking for MTTR, which uses only total downtime and "
                    "incident count."
                ),
            },
        ],
        "explanation": (
            "MTTR = total downtime / number of failures = 18 / 6 = 3 hours per incident. This differs from MTBF, "
            "which measures the average time between failures using operating (uptime) hours, not downtime."
        ),
    },
    {
        "id": "nd5c-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "Select the TWO statements that correctly distinguish recovery point objective (RPO) from recovery "
            "time objective (RTO) in a business impact analysis."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "RPO defines the maximum tolerable amount of data loss, expressed as a point in time, and "
                    "directly drives backup frequency and replication design"
                ),
                "correct": True,
                "rationale": (
                    "Correct. RPO answers 'how much data can we afford to lose,' measured backward in time from "
                    "the point of disruption, which determines how often data must be backed up or replicated."
                ),
            },
            {
                "id": "b",
                "text": (
                    "RTO defines the maximum acceptable duration between a disruption and the restoration of a "
                    "system or process to an operational state"
                ),
                "correct": True,
                "rationale": (
                    "Correct. RTO answers 'how quickly must this be back up,' measured forward in time from the "
                    "point of disruption to restoration."
                ),
            },
            {
                "id": "c",
                "text": "RPO defines how quickly, in hours, a help desk must acknowledge an incident ticket",
                "correct": False,
                "rationale": (
                    "Incorrect. That describes a service-level response-time metric, not RPO. RPO is specifically "
                    "about the acceptable data-loss window, not ticket acknowledgment speed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "RTO defines the average time between failures for a given system, based on historical "
                    "uptime data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. That describes MTBF (mean time between failures), not RTO. RTO is a target "
                    "recovery duration set during BIA planning, not a historical reliability statistic."
                ),
            },
        ],
        "explanation": (
            "RPO governs acceptable data loss (driving backup/replication design); RTO governs acceptable "
            "downtime duration (driving recovery approach). Neither is a help-desk SLA metric or a historical "
            "reliability statistic like MTBF."
        ),
    },
    {
        "id": "nd5c-008",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A German subsidiary of a multinational retailer must transfer EU customers' personal data to an "
            "unaffiliated, US-based email marketing vendor for campaign execution. The United States has no EU "
            "adequacy decision. Which mechanism should the company implement to lawfully authorize this transfer "
            "under GDPR?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard contractual clauses (SCCs) incorporated into the vendor contract",
                "correct": True,
                "rationale": (
                    "Correct. SCCs are the standard, EU Commission-approved mechanism for authorizing transfers "
                    "to processors or controllers in third countries lacking an adequacy decision, including "
                    "transfers to unaffiliated vendors."
                ),
            },
            {
                "id": "b",
                "text": "Binding corporate rules (BCRs)",
                "correct": False,
                "rationale": (
                    "Incorrect. BCRs govern transfers within a single corporate group (intra-group transfers "
                    "between affiliated entities); the email marketing vendor here is an unaffiliated third "
                    "party, not part of the retailer's corporate group."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Relying on the vendor's SOC 2 Type II report as sufficient legal basis for the transfer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A SOC 2 report attests to the design and operating effectiveness of the vendor's "
                    "controls; it is not a GDPR-recognized legal mechanism for authorizing an international "
                    "personal data transfer."
                ),
            },
            {
                "id": "d",
                "text": "Obtaining the vendor's verbal assurance that it will comply with GDPR",
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR requires documented, enforceable transfer safeguards; an informal verbal "
                    "assurance provides no legal basis and no enforceable protection for data subjects."
                ),
            },
        ],
        "explanation": (
            "For transfers of EU personal data to unaffiliated entities in third countries without an adequacy "
            "decision, standard contractual clauses are the primary general-purpose transfer mechanism under "
            "GDPR."
        ),
    },
    {
        "id": "nd5c-009",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A mobile fitness app requests permission to access users' complete contact lists and continuous "
            "precise GPS location history, even though its step-counting feature only requires the phone's "
            "built-in accelerometer. Which GDPR principle does this data collection MOST directly violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data minimization",
                "correct": True,
                "rationale": (
                    "Correct. The data minimization principle (Article 5(1)(c)) requires that personal data "
                    "collected be adequate, relevant, and limited to what is necessary for the stated purpose. "
                    "Contacts and precise location are not necessary for step counting."
                ),
            },
            {
                "id": "b",
                "text": "Purpose limitation",
                "correct": False,
                "rationale": (
                    "Incorrect. Purpose limitation concerns using data already collected for a purpose "
                    "incompatible with the one originally stated, not the initial scope of what is collected. "
                    "Here the problem is over-collection at the outset."
                ),
            },
            {
                "id": "c",
                "text": "Storage limitation",
                "correct": False,
                "rationale": (
                    "Incorrect. Storage limitation concerns how long data is retained, not how much data is "
                    "collected in the first place."
                ),
            },
            {
                "id": "d",
                "text": "Accountability",
                "correct": False,
                "rationale": (
                    "Incorrect. Accountability concerns an organization's ability to demonstrate compliance with "
                    "GDPR principles overall; it is not the specific principle governing the scope of data "
                    "collected for a given purpose."
                ),
            },
        ],
        "explanation": (
            "Collecting data (contacts, precise location) far beyond what a stated purpose (step counting) "
            "requires violates the data minimization principle."
        ),
    },
    {
        "id": "nd5c-010",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "An organization failed to maintain a required record of processing activities (ROPA) and did not "
            "appoint a data protection officer despite meeting the statutory threshold, but no data breach or "
            "unlawful processing occurred. Under GDPR's tiered administrative fine structure, this violation is "
            "subject to which maximum fine?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Up to €10 million or 2% of the company's total worldwide annual turnover of the preceding "
                    "financial year, whichever is higher"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the lower administrative fine tier, reserved for procedural and "
                    "organizational obligations such as recordkeeping (ROPA) and DPO appointment failures."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Up to €20 million or 4% of the company's total worldwide annual turnover of the preceding "
                    "financial year, whichever is higher"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The higher fine tier is reserved for violations of core data-processing "
                    "principles, lawful basis, and data subject rights, which did not occur in this scenario."
                ),
            },
            {
                "id": "c",
                "text": "A flat €10 million fine, regardless of the company's revenue",
                "correct": False,
                "rationale": (
                    "Incorrect. The lower tier uses whichever figure (the fixed €10 million amount or 2% of "
                    "worldwide turnover) is higher, not a flat rate divorced from company size."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No monetary fine is possible; only a compliance order can be issued for first-time "
                    "procedural violations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Supervisory authorities may impose fines directly for procedural violations; a "
                    "prior compliance order or warning is not a legal prerequisite to issuing a fine."
                ),
            },
        ],
        "explanation": (
            "GDPR uses a two-tier fine structure. Procedural/organizational violations (recordkeeping, DPO "
            "appointment) fall under the lower tier: up to €10 million or 2% of global turnover, whichever is "
            "higher. Core principle and data subject rights violations fall under the higher 4%/€20 million tier."
        ),
    },
    {
        "id": "nd5c-011",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "A retailer publishes a quarterly investor report containing total store-count figures and "
            "industry-wide aggregated sales-trend percentages that were already publicly disclosed in a prior SEC "
            "filing, with no way to trace the figures back to individual customers or transactions. Which "
            "classification level is MOST appropriate for this dataset?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Public",
                "correct": True,
                "rationale": (
                    "Correct. The data was already publicly disclosed, is non-sensitive, and carries no "
                    "re-identification risk to individuals, matching the Public classification level."
                ),
            },
            {
                "id": "b",
                "text": "Internal",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal classification restricts access to employees only; applying it here "
                    "would unnecessarily restrict information that is already public with no confidentiality "
                    "interest remaining."
                ),
            },
            {
                "id": "c",
                "text": "Confidential",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidential applies to information that would cause harm to the organization or "
                    "individuals if disclosed; this dataset offers no such harm since it is already public."
                ),
            },
            {
                "id": "d",
                "text": "Restricted",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricted is reserved for the organization's most sensitive data (e.g., trade "
                    "secrets, unreleased material information); already-public aggregate figures do not qualify."
                ),
            },
        ],
        "explanation": (
            "Data that has already been publicly disclosed and carries no re-identification or competitive risk "
            "should be classified Public, the lowest sensitivity tier."
        ),
    },
    {
        "id": "nd5c-012",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A single report contains an 'Internal' section summarizing routine department headcount totals and "
            "a 'Restricted' section detailing an unannounced executive reorganization and pending layoffs. Per "
            "standard data classification handling rules, how should the ENTIRE document be labeled and handled "
            "while it exists as a single file?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Restricted, the highest classification level present in the document",
                "correct": True,
                "rationale": (
                    "Correct. A document containing multiple classification levels must be labeled and handled "
                    "at the highest level present; otherwise the access, storage, and transmission controls "
                    "required for the most sensitive section would not be applied to the whole file."
                ),
            },
            {
                "id": "b",
                "text": "Internal, since that reflects most of the document's routine content",
                "correct": False,
                "rationale": (
                    "Incorrect. This would leave the sensitive Restricted section without adequate protection "
                    "controls (encryption, need-to-know access, transmission restrictions) while it remains part "
                    "of the same file."
                ),
            },
            {
                "id": "c",
                "text": (
                    "No whole-document label is required as long as each page eventually receives a separate "
                    "label once the document is split"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Splitting the document by sensitivity is a good long-term practice, but until "
                    "that separation happens the entire file must carry the highest applicable label so handling "
                    "controls are not under-applied while it exists as one document."
                ),
            },
            {
                "id": "d",
                "text": "Public, because most of the content (headcount totals) is routine",
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores the sensitive Restricted content entirely and would expose "
                    "unannounced layoff information with no protective controls at all."
                ),
            },
        ],
        "explanation": (
            "The standard rule for mixed-sensitivity documents is to label and protect the entire document at "
            "the highest classification level present until the sensitive content can be separated."
        ),
    },
    {
        "id": "nd5c-013",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "A DLP system is configured to automatically block outbound email attachments labeled 'Restricted' "
            "but allow attachments labeled 'Public' to be sent freely, with 'Internal' and 'Confidential' "
            "attachments triggering intermediate handling rules. What is the PRIMARY purpose served by assigning "
            "data classification labels in this environment?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "To trigger proportionate, automated handling and protection controls based on a dataset's "
                    "sensitivity"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification labels here directly drive automated technical enforcement (DLP "
                    "blocking rules), applying stronger protection to more sensitive data — the core purpose of "
                    "a classification scheme."
                ),
            },
            {
                "id": "b",
                "text": "To satisfy an annual audit checklist requirement with no operational effect",
                "correct": False,
                "rationale": (
                    "Incorrect. The labels have a direct, active operational effect in this scenario (blocking "
                    "or allowing outbound attachments), not merely a paperwork exercise."
                ),
            },
            {
                "id": "c",
                "text": "To determine which department is billed for data storage costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Storage cost allocation is unrelated to the function of sensitivity-based "
                    "classification labeling."
                ),
            },
            {
                "id": "d",
                "text": "To identify which data can be legally sold to third parties",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification concerns sensitivity and handling requirements, not the legal "
                    "right to sell or share data with third parties, which is governed by consent and ownership "
                    "policies."
                ),
            },
        ],
        "explanation": (
            "Data classification exists to drive proportionate handling and protection controls — here, "
            "automated DLP enforcement scaled to each label's sensitivity."
        ),
    },
    {
        "id": "nd5c-014",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "For the 'customer master data' domain, one team defines naming conventions, resolves data-quality "
            "conflicts between departments, and ensures records are labeled per the classification policy, while "
            "a separate IT operations team implements the actual database backups, access-control lists, and "
            "encryption at rest. Which role does the IT operations team fulfill?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data custodian",
                "correct": True,
                "rationale": (
                    "Correct. Custodians handle the technical implementation of storage, backup, and security "
                    "controls according to policies and standards set by others, exactly as described for the IT "
                    "operations team."
                ),
            },
            {
                "id": "b",
                "text": "Data steward",
                "correct": False,
                "rationale": (
                    "Incorrect. That is the first team's role — a business-facing role focused on data quality, "
                    "meaning, and classification standards, not day-to-day technical implementation."
                ),
            },
            {
                "id": "c",
                "text": "Data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. A controller determines the purposes and means of processing (typically a "
                    "business owner making decisions about why and how data is used), not the team implementing "
                    "technical backup and access controls."
                ),
            },
            {
                "id": "d",
                "text": "Data processor",
                "correct": False,
                "rationale": (
                    "Incorrect. Processor is a legal/regulatory term for a separate organization processing data "
                    "on a controller's behalf under contract, not an internal IT team executing internal policy."
                ),
            },
        ],
        "explanation": (
            "The steward defines data quality/classification standards; the custodian implements the technical "
            "controls (backups, ACLs, encryption) that carry out those standards day to day."
        ),
    },
    {
        "id": "nd5c-015",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A payroll-processing vendor is contractually engaged to process client employee data strictly "
            "according to each client's documented instructions. Auditors discover the vendor has independently "
            "begun using that same payroll data, without client authorization, to train its own commercial "
            "credit-risk-scoring product sold to banks. What is the MOST accurate characterization of the "
            "vendor's role for this additional use?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The vendor is acting as a data controller for this specific processing activity, since it "
                    "independently determined a new purpose and means, while remaining a processor for the "
                    "original payroll function"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A party's role is determined by who actually decides the purpose and means of a "
                    "given processing activity. By independently deciding to reuse the data for its own product, "
                    "the vendor is acting as a controller for that activity."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The vendor remains solely a data processor for all activities, since its original contract "
                    "was a processor agreement"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Role classification follows the actual factual decision-making for each "
                    "processing activity, not the label of the original contract; unauthorized independent reuse "
                    "changes the role for that specific activity."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The vendor becomes the data subjects' data owner, transferring all client obligations to "
                    "the vendor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'Data owner' does not carry this legal meaning, and the client-controller retains "
                    "its own independent obligations regardless of the vendor's unauthorized actions."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The vendor is acting as a data custodian for the credit-scoring use case, since it is "
                    "exercising technical control over the data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Custodian is an operational/technical implementation role; deciding to create and "
                    "sell a new product using the data is a purpose-and-means decision, which defines a "
                    "controller, not a custodian."
                ),
            },
        ],
        "explanation": (
            "A vendor's role can differ by processing activity. Deciding independently to use data for a new, "
            "unauthorized purpose makes the vendor a controller for that activity, regardless of its original "
            "processor contract."
        ),
    },
    {
        "id": "nd5c-016",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "Select the TWO statements that correctly describe the obligations and characteristics of a data "
            "processor under GDPR."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A processor may only process personal data according to the documented instructions of the "
                    "data controller"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Processors act on behalf of, and strictly within the instructions of, the "
                    "controller; independent decisions about purpose fall outside the processor role."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A processor must notify the data controller without undue delay after becoming aware of a "
                    "personal data breach"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR Article 28 requires processors to notify controllers promptly of any personal "
                    "data breach so the controller can meet its own regulatory notification obligations."
                ),
            },
            {
                "id": "c",
                "text": "A processor independently determines the purposes and legal basis for processing personal data",
                "correct": False,
                "rationale": (
                    "Incorrect. Determining the purposes and legal basis of processing is the defining "
                    "characteristic of a controller, not a processor."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A processor is contractually and legally exempt from any direct GDPR obligations, since "
                    "only controllers are regulated"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR imposes direct obligations on processors, including breach notification and "
                    "processing-agreement requirements; processors are not exempt from regulation."
                ),
            },
        ],
        "explanation": (
            "Processors act only on documented controller instructions and must notify controllers of breaches "
            "without undue delay — they do not independently set purposes and are not exempt from GDPR."
        ),
    },
    {
        "id": "nd5c-017",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "After several near-miss incidents tied to a legacy public-facing FTP service used by only a handful "
            "of customers, and after determining that adequately securing the protocol is not cost-effective "
            "relative to its business value, leadership permanently decommissions the FTP service and requires "
            "all customers to migrate to a modern SFTP gateway used elsewhere in the environment. Which risk "
            "management strategy does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk avoidance",
                "correct": True,
                "rationale": (
                    "Correct. Eliminating the risk-bearing activity entirely (decommissioning the FTP service) "
                    "rather than continuing to operate it with added controls is the definition of risk "
                    "avoidance."
                ),
            },
            {
                "id": "b",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation would mean adding controls to the existing FTP service while "
                    "continuing to operate it (e.g., IP restrictions, TLS); here the activity itself is "
                    "eliminated, not controlled."
                ),
            },
            {
                "id": "c",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. No third party is assuming the risk or its financial impact; the organization "
                    "simply stops offering the service."
                ),
            },
            {
                "id": "d",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance means continuing to operate with the risk unaddressed and documented; "
                    "here the exposure is proactively removed rather than tolerated."
                ),
            },
        ],
        "explanation": (
            "Permanently discontinuing a risk-bearing activity, rather than controlling it, insuring it, or "
            "tolerating it, is risk avoidance."
        ),
    },
    {
        "id": "nd5c-018",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A business unit requests permission to run a legacy application that cannot support the "
            "organization's mandatory disk-encryption standard for the foreseeable future, with no planned "
            "remediation date, and receives permanent, formally documented approval to deviate from the standard "
            "with compensating monitoring controls. Which governance mechanism does this represent, and how does "
            "it differ from a risk exception?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A risk exemption — a permanent, indefinite approved deviation from policy; a risk "
                    "exception, by contrast, is a temporary deviation with a defined expiration or remediation "
                    "date"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The defining distinction between an exemption and an exception is duration: an "
                    "exemption has no planned end date, while an exception is time-bound and tied to a "
                    "remediation timeline."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A risk exception, because it involves compensating controls; exemptions never involve "
                    "compensating controls"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Exemptions can also include compensating controls; the presence of compensating "
                    "controls does not distinguish an exception from an exemption. Duration is the "
                    "distinguishing factor."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A risk exemption — identical in meaning to risk acceptance, since both simply document that "
                    "a risk will not be remediated"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risk acceptance is a broader risk-response strategy; an exemption is a specific "
                    "formal policy-deviation mechanism. The scenario's hallmark — indefinite duration with no "
                    "remediation date — is what specifically defines an exemption versus a time-bound exception."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A risk exception, because the business unit initiated the request; exemptions can only be "
                    "granted proactively by the security team"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Both exceptions and exemptions are typically request-driven by the business unit "
                    "seeking the deviation; who initiates the request is not the distinguishing factor."
                ),
            },
        ],
        "explanation": (
            "A risk exemption is a permanent, indefinite approved deviation from a mandatory standard. A risk "
            "exception is time-bound, with a defined expiration or remediation date. Duration, not the presence "
            "of compensating controls or who initiates the request, is the key distinction."
        ),
    },
    {
        "id": "nd5c-019",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A company migrates a workload to a public cloud IaaS provider under a shared-responsibility model "
            "(the provider secures the underlying physical infrastructure and hypervisor; the customer secures "
            "its own OS, data, and applications), and separately purchases a standalone cyber insurance policy to "
            "cover breach-litigation costs for that same workload. How should these two actions be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The shared-responsibility cloud migration represents risk sharing (dividing responsibility "
                    "for different risk components between two parties who each retain their portion), while "
                    "the insurance purchase represents risk transference (shifting the financial impact of a "
                    "realized risk to a third party)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Shared responsibility divides and retains distinct risk components between the "
                    "provider and customer (sharing), while insurance purely shifts financial impact after a "
                    "loss occurs to an insurer (transference) — two distinct strategies."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Both actions represent risk transference, since in both cases another organization is now "
                    "handling part of the security burden"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Shared responsibility divides and retains distinct obligations between the "
                    "customer and provider rather than shifting the customer's own retained risk elsewhere; only "
                    "the insurance purchase purely transfers financial impact."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both actions represent risk mitigation, since both reduce the overall likelihood of a "
                    "breach occurring"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance does not reduce the likelihood of a breach at all — it only offsets "
                    "financial impact after a loss has already occurred."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The cloud migration represents risk avoidance, since the customer is no longer responsible "
                    "for infrastructure security, while the insurance represents risk acceptance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The customer still retains and must manage substantial risk (OS/data/app layer) "
                    "under the shared model, which is not avoidance; and purchasing insurance is the definition "
                    "of transference, not acceptance."
                ),
            },
        ],
        "explanation": (
            "Shared-responsibility cloud models split and retain risk between provider and customer (risk "
            "sharing). Insurance purely shifts the financial consequence of a realized risk to a third party "
            "(risk transference). Neither reduces breach likelihood (mitigation) nor eliminates the activity "
            "(avoidance)."
        ),
    },
    {
        "id": "nd5c-020",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "The board publishes a formal statement: 'The organization has zero appetite for risks that could "
            "result in unplanned downtime of the core trading platform.' Operationally, the risk management team "
            "documents that brief, unplanned outages of up to 2 minutes per quarter are considered acceptable "
            "variance and do not trigger executive escalation, while anything beyond that does. What does the "
            "2-minutes-per-quarter figure represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk tolerance",
                "correct": True,
                "rationale": (
                    "Correct. Tolerance defines the acceptable range of variation around a stated risk appetite; "
                    "it operationalizes the qualitative appetite statement into a measurable, actionable "
                    "threshold."
                ),
            },
            {
                "id": "b",
                "text": "Risk appetite",
                "correct": False,
                "rationale": (
                    "Incorrect. The appetite is the board's qualitative 'zero unplanned downtime' statement "
                    "itself; the 2-minute figure is the practical, measurable boundary derived from it, which is "
                    "tolerance."
                ),
            },
            {
                "id": "c",
                "text": "Residual risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Residual risk is the risk remaining after controls are applied to a specific "
                    "identified risk item, not a general acceptable-variance threshold applied across outages."
                ),
            },
            {
                "id": "d",
                "text": "Inherent risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Inherent risk is the level of risk before any controls are applied, unrelated to "
                    "an acceptable-variance threshold like this one."
                ),
            },
        ],
        "explanation": (
            "Risk appetite is the qualitative, high-level statement of willingness to accept risk. Risk "
            "tolerance is the specific, measurable acceptable variance around that appetite — here, 2 minutes of "
            "downtime per quarter."
        ),
    },
    {
        "id": "nd5c-021",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "Two risk register entries both currently carry an identical 'moderate' residual risk score of 9. "
            "Entry A's score has been stable at 9 for the past three quarterly reviews. Entry B's score has risen "
            "from 4 to 6 to 9 over the same three reviews and continues climbing. Despite having the same current "
            "score, which entry should risk owners prioritize for a response, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Entry B, because its high risk velocity (the rate at which its score is increasing) "
                    "suggests it will soon exceed the organization's risk tolerance if left unaddressed, even "
                    "though its current score matches Entry A's"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk velocity/trend is a valid, recognized input to prioritization alongside the "
                    "current score. A rapidly climbing risk warrants earlier intervention than a stable risk at "
                    "the same current level."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Entry A, because a score that has remained unchanged for three reviews indicates the "
                    "underlying control has definitively failed and must be replaced immediately"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stable score more plausibly indicates a steady-state condition, not control "
                    "failure; nothing in the scenario indicates Entry A's conditions are worsening."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both entries equally, because current residual risk score is the only factor that should "
                    "ever influence prioritization, and trend data is not a valid input to risk decisions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risk trend/velocity is a recognized, valid input alongside the current score for "
                    "prioritization decisions, not something to be disregarded."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither entry requires prioritization, since both remain in the 'moderate' banding and "
                    "moderate risks are automatically deprioritized in favor of only 'severe'-banded risks"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Banding alone should not be used to blanket-deprioritize a risk that is actively "
                    "trending toward a higher band; velocity matters precisely because it predicts near-future "
                    "severity."
                ),
            },
        ],
        "explanation": (
            "Risk velocity (the rate of change in a risk's score over time) is a valid prioritization input "
            "distinct from the current score alone. A rapidly rising risk deserves earlier attention than a "
            "stable risk at the same current level."
        ),
    },
    {
        "id": "nd5c-022",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Risk register & appetite",
        "stem": (
            "Select the TWO fields/data points that a mature, well-formed risk register entry should include to "
            "support effective risk oversight."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A named, accountable risk owner responsible for tracking and reporting on the risk's status"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An assigned owner ensures accountability for monitoring, escalating, and driving "
                    "response for each risk entry — a foundational risk register field."
                ),
            },
            {
                "id": "b",
                "text": "A target remediation date or review cadence for tracking progress against the risk",
                "correct": True,
                "rationale": (
                    "Correct. A remediation timeline or review cadence prevents risks from sitting indefinitely "
                    "unaddressed and enables progress tracking over time."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The personal performance-review rating of the risk owner's most recent annual evaluation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Personnel performance data is irrelevant to risk tracking and has no bearing on "
                    "the risk itself or its remediation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The marketing department's unrelated quarterly advertising budget, included for "
                    "organizational completeness"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Unrelated budget data has no bearing on risk oversight and does not belong in a "
                    "risk register entry."
                ),
            },
        ],
        "explanation": (
            "A well-formed risk register entry includes a named risk owner and a target remediation date/review "
            "cadence, among other fields — not unrelated personnel or budget data."
        ),
    },
    {
        "id": "nd5c-023",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A batch of self-encrypting drives (SEDs) that stored internal project files is being reassigned to "
            "a different internal team for continued use — not resold or destroyed. Which sanitization method is "
            "MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cryptographic erase (destroying the drive's internal encryption key)",
                "correct": True,
                "rationale": (
                    "Correct. Cryptographic erase instantly and verifiably renders all previously stored data "
                    "unrecoverable on a self-encrypting drive, while leaving the drive fully functional for "
                    "reuse — ideal for redeployment scenarios."
                ),
            },
            {
                "id": "b",
                "text": "Degaussing",
                "correct": False,
                "rationale": (
                    "Incorrect. Degaussing is ineffective against SSD/flash-based media (including most SEDs) "
                    "because it targets magnetic platters, and it would also permanently damage the drive's "
                    "electronics, making reuse impossible."
                ),
            },
            {
                "id": "c",
                "text": "Physical destruction (shredding)",
                "correct": False,
                "rationale": (
                    "Incorrect. Destruction ruins a drive intended to be reused, wasting a functional asset when "
                    "a much faster, equally effective sanitization option exists."
                ),
            },
            {
                "id": "d",
                "text": "Formatting the drive through the operating system's standard quick-format utility",
                "correct": False,
                "rationale": (
                    "Incorrect. A quick format only clears the file allocation table and leaves underlying data "
                    "recoverable with forensic tools; it does not meet a defensible sanitization standard."
                ),
            },
        ],
        "explanation": (
            "For self-encrypting drives being reused internally, cryptographic erase provides fast, verifiable "
            "sanitization without damaging or destroying reusable hardware."
        ),
    },
    {
        "id": "nd5c-024",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A defense contractor is decommissioning a batch of hard drives that stored top-secret program data. "
            "The drives will be leaving organizational custody entirely and will not be reused, resold, or "
            "retained in any form. Per NIST SP 800-88 media sanitization guidance, which category of sanitization "
            "is required for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Destroy",
                "correct": True,
                "rationale": (
                    "Correct. NIST SP 800-88 recommends the Destroy category (e.g., disintegration, "
                    "incineration, or shredding to a specified particle size) for the highest-sensitivity data "
                    "that is leaving organizational control with no intent for reuse."
                ),
            },
            {
                "id": "b",
                "text": "Clear",
                "correct": False,
                "rationale": (
                    "Incorrect. Clear (e.g., a standard overwrite) is intended for media being reused within the "
                    "organization's control at a lower or equivalent sensitivity, and provides only "
                    "logical-level protection against simple recovery methods, not the level required here."
                ),
            },
            {
                "id": "c",
                "text": "Purge",
                "correct": False,
                "rationale": (
                    "Incorrect. Purge (e.g., cryptographic erase, degaussing) provides stronger protection than "
                    "Clear and may be sufficient for media being reused or resold, but NIST reserves Destroy "
                    "specifically for the combination of highest sensitivity and permanent departure from "
                    "organizational control described here."
                ),
            },
            {
                "id": "d",
                "text": "Retain",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Retain' is not a NIST SP 800-88 sanitization category, and the scenario "
                    "explicitly states the drives will not be retained."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-88 recommends Destroy for the highest-sensitivity media leaving organizational control "
            "permanently with no reuse intended, as opposed to Clear or Purge, which suit lower-sensitivity or "
            "reuse/resale scenarios."
        ),
    },
    {
        "id": "nd5c-025",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A medical clinic is closing permanently and must dispose of decades of paper-based patient records "
            "containing PHI that are not subject to any ongoing legal hold or retention requirement. Which "
            "disposal method is MOST appropriate to meet HIPAA-aligned secure destruction expectations?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cross-cut shredding or pulping performed in-house or by a bonded, contracted destruction "
                    "vendor, with a certificate of destruction retained as evidence"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cross-cut shredding or pulping renders physical records unreadable and "
                    "unreconstructable, and a retained certificate of destruction provides auditable proof of "
                    "proper disposal."
                ),
            },
            {
                "id": "b",
                "text": "Placing the records in a standard recycling bin, since paper is a recyclable material",
                "correct": False,
                "rationale": (
                    "Incorrect. Intact or lightly shredded paper PHI placed in standard recycling is trivially "
                    "reconstructable and readable, failing to protect patient confidentiality."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Storing the records indefinitely in a locked, offsite archive rather than destroying them, "
                    "since retention is always safer than destruction"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Retaining PHI beyond any legal or business requirement increases exposure risk "
                    "and violates data minimization/retention-limitation expectations once no legal hold or "
                    "retention need exists."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Donating the filing cabinets and their contents to a local charity for reuse, since the "
                    "cabinets are company property"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This would disclose PHI to an unauthorized third party rather than sanitizing or "
                    "destroying it."
                ),
            },
        ],
        "explanation": (
            "Secure destruction of paper PHI with no remaining legal hold requires cross-cut shredding or "
            "pulping (in-house or via a bonded vendor) with a retained certificate of destruction as auditable "
            "proof."
        ),
    },
    {
        "id": "nd5c-026",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "A security awareness program's phishing-simulation click rate has plateaued around 8% for a year "
            "despite repeated training. The security team wants to further reduce risk by increasing the rate at "
            "which employees proactively report suspicious emails, not just avoid clicking. Which change is MOST "
            "likely to directly improve the reporting rate specifically?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Publicly recognizing and rewarding employees (e.g., a small gift card and shout-out) each "
                    "time they correctly report a real or simulated phishing email using the 'report phish' "
                    "button"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Positive reinforcement tied directly to the desired reporting behavior is a "
                    "well-established way to increase that specific behavior."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increasing the frequency of mandatory annual compliance training video modules from once to "
                    "twice per year"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Passive video-based compliance training has a weak, indirect relationship to the "
                    "specific behavior of proactively reporting suspicious emails."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Publicly listing, by name, every employee who failed a simulated phishing test in the "
                    "company-wide newsletter"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Public shaming tends to suppress open reporting behavior, as employees fear "
                    "embarrassment and may hide mistakes rather than report them."
                ),
            },
            {
                "id": "d",
                "text": "Reducing the number of phishing simulations sent per year to minimize employee annoyance",
                "correct": False,
                "rationale": (
                    "Incorrect. This reduces practice opportunities and is unlikely to improve the reporting "
                    "rate; it would likely reduce overall engagement with the program."
                ),
            },
        ],
        "explanation": (
            "Positive reinforcement directly tied to the target behavior (reporting) is more effective at "
            "changing that specific behavior than generic training volume increases or punitive public shaming."
        ),
    },
    {
        "id": "nd5c-027",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "A financial services firm's generic annual security awareness training covers phishing and password "
            "hygiene for all staff. Post-incident analysis reveals that most recent incidents involved developers "
            "introducing SQL injection flaws and finance staff falling for BEC-style wire-transfer fraud — issues "
            "the generic training does not address. What change would MOST directly address these specific gaps?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Supplementing the generic training with role-based modules: secure coding practices for "
                    "developers and wire-transfer verification procedures for finance staff"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tailoring training content to each role's actual risk exposure directly targets "
                    "the specific failure modes identified in the post-incident analysis."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increasing the pass-score threshold on the existing generic annual training quiz from 70% "
                    "to 90%"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Raising the bar on content that doesn't cover secure coding or wire-fraud "
                    "verification will not address either identified gap."
                ),
            },
            {
                "id": "c",
                "text": "Extending the generic training's length by adding more general password-hygiene content",
                "correct": False,
                "rationale": (
                    "Incorrect. Additional password-hygiene content does not address either identified gap "
                    "(SQL injection, BEC wire fraud)."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Making the existing generic training optional for tenured employees with more than five "
                    "years of service"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reduces training coverage rather than closing the identified content gaps, "
                    "and tenure is unrelated to role-specific risk exposure."
                ),
            },
        ],
        "explanation": (
            "Role-based training that addresses each group's actual risk exposure (secure coding for developers, "
            "wire-fraud verification for finance) closes gaps that generic, one-size-fits-all training misses."
        ),
    },
    {
        "id": "nd5c-028",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "Completion records show 100% of staff finished mandatory annual security awareness training on time "
            "for three consecutive years. However, the click-through rate on quarterly phishing simulations has "
            "remained flat at 19%, and the number of employees using the 'report phish' button has not "
            "increased. What does this pattern MOST likely indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The training program is achieving compliance (completion) but not producing genuine "
                    "behavior change, and its content, delivery method, or reinforcement approach likely needs "
                    "to be redesigned"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 100% completion is a checkbox/compliance metric, while click-through and reporting "
                    "rates are behavioral outcome metrics; flat behavioral metrics despite full completion "
                    "indicate the training isn't changing actual behavior."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The organization's employees are already performing at an optimal security awareness "
                    "level, since completion is at its maximum possible value of 100%"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Completion has no necessary relationship to behavioral effectiveness, and a flat "
                    "19% click rate with no reporting improvement is not an optimal outcome."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The phishing simulation tool is miscalibrated and should be discontinued, since click rates "
                    "should decrease automatically as completion rates rise"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This assumes a direct causal link between completion and click rate that the "
                    "data itself contradicts; the more defensible conclusion is that the training isn't "
                    "effective, not that the measurement tool is broken."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No further action is needed, because click-through rate is not a meaningful metric for "
                    "evaluating awareness training effectiveness"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Click-through rate, alongside reporting rate, is one of the primary behavioral "
                    "metrics used to evaluate awareness program effectiveness."
                ),
            },
        ],
        "explanation": (
            "Completion rate is a checkbox/compliance metric. Flat click-through and reporting rates despite "
            "100% completion signal that the training content or delivery is not producing real behavior change "
            "and needs redesign."
        ),
    },
    {
        "id": "nd5c-029",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "One governance document states, 'All remote access VPN connections must use TLS 1.2 or higher; TLS "
            "1.0 and 1.1 are prohibited' — a mandatory, specific technical requirement. A separate document "
            "states, 'When available, administrators are encouraged to prefer client-based VPN software over "
            "clientless/browser-based portals for a better user experience' — a recommended but non-mandatory "
            "practice. Which governance document types are these, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The first is a standard (mandatory, specific technical requirement); the second is a "
                    "guideline (recommended, non-mandatory best practice)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Standards impose mandatory, specific technical requirements; guidelines offer "
                    "recommended, non-mandatory best practices — exactly matching the mandatory/prohibited vs. "
                    "encouraged language in each document."
                ),
            },
            {
                "id": "b",
                "text": "The first is a policy; the second is a procedure",
                "correct": False,
                "rationale": (
                    "Incorrect. A policy is a high-level statement of management intent/goals, not a specific "
                    "mandatory technical value like the TLS version rule; a procedure would be a detailed "
                    "step-by-step how-to, not a general recommendation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both are policies, since both documents govern VPN usage within the same overall program"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. They differ meaningfully in mandatory vs. recommended language, which is exactly "
                    "what distinguishes standards from guidelines regardless of shared subject matter."
                ),
            },
            {
                "id": "d",
                "text": "The first is a guideline; the second is a standard",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the definitions: the first uses mandatory ('must,' 'prohibited') "
                    "language typical of a standard, and the second uses recommending ('encouraged') language "
                    "typical of a guideline."
                ),
            },
        ],
        "explanation": (
            "Standards set mandatory, specific technical requirements. Guidelines offer recommended, "
            "non-mandatory best practices. The presence of 'must'/'prohibited' versus 'encouraged' language "
            "identifies which is which."
        ),
    },
    {
        "id": "nd5c-030",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A newly appointed CISO at a company with a decentralized security governance model, where each "
            "business unit sets and enforces its own security policies independently, is evaluating whether to "
            "shift toward a centralized model with a single enterprise-wide policy set enforced by a central "
            "security team. Which tradeoff should the CISO expect from making this shift?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Centralization would likely improve consistency and simplify enterprise-wide compliance "
                    "reporting, but could reduce each business unit's ability to tailor policies to its unique "
                    "regulatory or operational needs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the classic, well-documented tradeoff between centralized and "
                    "decentralized governance models: consistency and reporting simplicity gained, local "
                    "flexibility reduced."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Centralization would have no measurable effect on policy consistency, since consistency is "
                    "determined solely by the number of employees rather than the governance structure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Governance structure (centralized vs. decentralized) directly affects policy "
                    "consistency across a company, independent of headcount."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Centralization would eliminate the need for any policy exceptions across the enterprise, "
                    "since a single central authority can anticipate every business unit's operational "
                    "requirement in advance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is unrealistic; exception processes remain necessary under either "
                    "governance model, since no single policy set can anticipate every local operational "
                    "constraint."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Centralization would automatically reduce the organization's overall compliance and audit "
                    "burden to zero, since only one policy set would need to be audited"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This overstates the benefit; audits would still need to verify implementation "
                    "and enforcement across every business unit, even under a single, unified policy set."
                ),
            },
        ],
        "explanation": (
            "Centralized governance improves consistency and simplifies enterprise-wide reporting but trades "
            "away local flexibility; it does not eliminate exceptions or audit burden entirely."
        ),
    },
    {
        "id": "nd5c-031",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A business unit operating a legacy point-of-sale system that cannot support the organization's "
            "mandatory MFA standard requests to continue operating it without MFA. Which approach BEST reflects "
            "sound security governance for handling this request?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require the business unit to submit a formal, time-bound exception request that documents "
                    "compensating controls (e.g., network segmentation, enhanced monitoring), receives "
                    "risk-owner and security leadership sign-off, and is tracked in the risk register with a "
                    "remediation or re-review date"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the standard, auditable governance process for handling policy deviations "
                    "— documented, approved, compensated, and tracked toward eventual remediation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Allow the business unit to informally continue operating without MFA, since raising the "
                    "issue through a formal process would slow down business operations unnecessarily"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Undocumented, unapproved deviations from mandatory standards create untracked "
                    "risk and audit findings, undermining governance."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Automatically deny the request and force immediate decommissioning of the legacy system "
                    "regardless of business impact, since MFA is a mandatory standard with no exception mechanism"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Most mature governance programs include a formal exception process specifically "
                    "to handle legitimate cases like unsupported legacy systems, rather than a rigid, "
                    "zero-flexibility stance."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Quietly update the MFA standard's written wording to exclude point-of-sale systems, without "
                    "any documented risk acceptance, review, or executive sign-off"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Silently rewriting policy to avoid an inconvenient finding bypasses governance "
                    "oversight and hides the actual risk rather than formally accepting and tracking it."
                ),
            },
        ],
        "explanation": (
            "Sound governance handles legitimate policy deviations through a formal, documented, time-bound "
            "exception process with compensating controls and sign-off — not informal tolerance, blanket denial, "
            "or silently rewriting policy."
        ),
    },
    {
        "id": "nd5c-032",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two competing hospital networks are in preliminary talks about a potential clinical-data-sharing "
            "research partnership. Before either side is willing to disclose any proprietary patient-outcome "
            "methodologies or unpublished research data during exploratory talks, they want a legally binding "
            "commitment that neither party will disclose or use the other's information outside the discussions. "
            "No cooperative project, budget, or resource commitment exists yet. Which agreement type is MOST "
            "appropriate at this stage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A non-disclosure agreement (NDA)",
                "correct": True,
                "rationale": (
                    "Correct. An NDA's sole purpose is to create a binding confidentiality obligation protecting "
                    "sensitive information exchanged during discussions, independent of any actual cooperative "
                    "undertaking."
                ),
            },
            {
                "id": "b",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents a general intent to cooperate on a shared undertaking; at this "
                    "exploratory stage neither party is ready to document cooperative intent, only "
                    "confidentiality."
                ),
            },
            {
                "id": "c",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes an actual partnership's structure (roles, profit/loss sharing, "
                    "responsibilities), which is premature before any partnership has even been agreed to."
                ),
            },
            {
                "id": "d",
                "text": "A service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines measurable performance/service metrics for an ongoing service "
                    "relationship, which doesn't exist here."
                ),
            },
        ],
        "explanation": (
            "When two parties need only a binding confidentiality obligation before any cooperative commitment "
            "exists, an NDA — not an MOU, BPA, or SLA — is the appropriate agreement."
        ),
    },
    {
        "id": "nd5c-033",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two independent companies — a software vendor and a regional systems integrator — agree to formally "
            "partner: the integrator will resell the vendor's product bundled with its own installation "
            "services, and the two companies will split resulting revenue according to a defined formula, with "
            "each company's operational responsibilities spelled out. Which agreement type BEST governs this "
            "arrangement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A business partnership agreement (BPA)",
                "correct": True,
                "rationale": (
                    "Correct. A BPA formalizes the structure of an actual business partnership, including "
                    "revenue/profit sharing and each partner's defined responsibilities — exactly what this "
                    "reseller arrangement requires."
                ),
            },
            {
                "id": "b",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is typically a non-binding or loosely binding statement of intent to "
                    "cooperate, not a formal agreement defining specific revenue splits and operational "
                    "responsibilities."
                ),
            },
            {
                "id": "c",
                "text": "A non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA addresses confidentiality obligations only, not revenue sharing or "
                    "operational structure."
                ),
            },
            {
                "id": "d",
                "text": "A master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA establishes overarching terms (payment, liability, confidentiality) for "
                    "future individual service engagements between a customer and a services provider, not a "
                    "revenue-sharing reseller partnership structure between two independent businesses."
                ),
            },
        ],
        "explanation": (
            "A formal revenue-sharing reseller partnership with defined responsibilities is governed by a "
            "business partnership agreement (BPA), not an MOU, NDA, or MSA."
        ),
    },
    {
        "id": "nd5c-034",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A company has a signed master service agreement (MSA) with a cybersecurity consulting firm that "
            "establishes standard payment terms, liability caps, and confidentiality obligations applicable to "
            "all future engagements. The company now wants to engage the firm for a specific 10-week penetration "
            "test, and needs to formally document the exact scope, deliverables, timeline, and price for that "
            "specific engagement. Which document should be executed for this specific engagement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A statement of work (SOW)",
                "correct": True,
                "rationale": (
                    "Correct. An SOW documents the specific scope, deliverables, timeline, and pricing for an "
                    "individual engagement, operating under the general terms already established by the MSA."
                ),
            },
            {
                "id": "b",
                "text": "A new master service agreement",
                "correct": False,
                "rationale": (
                    "Incorrect. This would unnecessarily duplicate and potentially conflict with the general "
                    "terms already established in the existing MSA; MSAs are meant to be reused across multiple "
                    "engagements."
                ),
            },
            {
                "id": "c",
                "text": "A memorandum of understanding",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding statement of intent to cooperate, not a mechanism for "
                    "defining binding scope, deliverables, and price for a specific paid engagement."
                ),
            },
            {
                "id": "d",
                "text": "A business partnership agreement",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes a partnership structure (e.g., profit sharing between co-owners "
                    "of a venture), not a client-vendor service engagement's scope and deliverables."
                ),
            },
        ],
        "explanation": (
            "An MSA sets overarching terms reused across engagements; each specific engagement's scope, "
            "deliverables, timeline, and price are documented in a statement of work (SOW)."
        ),
    },
    {
        "id": "nd5c-035",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A procurement team is drafting a request for proposal (RFP) to select a new cloud backup vendor. "
            "Which practice reflects the MOST effective, proactive approach to vendor risk management at this "
            "stage?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Embedding mandatory security requirements (e.g., encryption standards, breach notification "
                    "timelines, right-to-audit clauses) directly into the RFP's evaluation criteria, so that "
                    "vendor security posture is scored alongside price and features before any vendor is "
                    "selected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This shifts vendor risk management to before contract signature, when the "
                    "organization has the most leverage to require security controls as a condition of "
                    "selection."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Selecting the lowest-cost vendor first, then requiring the vendor to complete a security "
                    "questionnaire once onboarding has already begun"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Evaluating security only after selection removes negotiating leverage and risks "
                    "discovering disqualifying issues after the organization has already committed."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deferring all security evaluation to the legal team's standard contract boilerplate, "
                    "without involving the security team in RFP criteria"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Generic legal boilerplate is unlikely to capture the specific technical security "
                    "requirements relevant to a cloud backup vendor."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Requiring the vendor to sign a generic non-disclosure agreement only, treating that as "
                    "sufficient assurance of the vendor's security posture"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects confidentiality of shared information but says nothing about the "
                    "vendor's actual security controls or practices."
                ),
            },
        ],
        "explanation": (
            "Embedding security requirements into RFP evaluation criteria applies vendor risk management "
            "proactively, before contract signature, when the organization retains the most leverage."
        ),
    },
    {
        "id": "nd5c-036",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "While reviewing a critical vendor's SOC 2 Type II report, the customer's security team notices a "
            "section listing 'complementary user entity controls' (CUECs) that specifies actions the customer "
            "itself must perform (e.g., managing its own user provisioning/deprovisioning within the vendor's "
            "platform) for the vendor's overall control environment to be considered effective. What should the "
            "security team do with this information?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Verify that the organization has actually implemented each listed complementary control on "
                    "its own side, since the vendor's audited control environment assumes those customer-side "
                    "controls are in place and functioning"
                ),
                "correct": True,
                "rationale": (
                    "Correct. CUECs are controls the report's auditor explicitly assumed the customer "
                    "implements; failing to implement them undermines the assurance the SOC 2 report otherwise "
                    "provides."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Disregard the CUEC section, since SOC 2 reports only describe the vendor's own controls and "
                    "any customer-side content is not relevant to vendor risk management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CUECs are a standard, relevant part of SOC 2 reports specifically because the "
                    "control environment's effectiveness depends on both parties."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Reject the vendor's SOC 2 report as invalid, since the presence of any customer-side "
                    "responsibilities means the vendor's controls are inadequate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CUECs are a normal, expected feature of SOC 2 reports reflecting shared "
                    "responsibility, and do not indicate an inadequate or invalid report."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Request that the vendor's auditor remove the CUEC section from future reports, since "
                    "customer responsibilities should not appear in a vendor's audit report"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Removing CUECs would misrepresent the actual assurance boundary and hide "
                    "legitimate shared-responsibility items from report readers."
                ),
            },
        ],
        "explanation": (
            "Complementary user entity controls (CUECs) in a SOC 2 report identify customer-side controls the "
            "auditor assumed were in place. The customer must verify it has actually implemented them for the "
            "report's assurance to hold."
        ),
    },
    {
        "id": "nd5c-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Vendor risk management",
        "stem": (
            "Select the TWO practices that are core components of an effective, ONGOING (continuous) "
            "third-party/vendor risk monitoring program, beyond the initial onboarding assessment."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Periodically reviewing the vendor's updated attestation reports (e.g., annual SOC 2 Type "
                    "II) and reassessing risk if the vendor's environment, subcontractors, or control scope "
                    "changes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ongoing monitoring requires reviewing updated attestations and reassessing when "
                    "material changes occur, not relying on a one-time assessment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Monitoring external threat intelligence, breach-notification services, and "
                    "financial-health indicators for signs the vendor's risk posture has changed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuous external monitoring surfaces emerging vendor risk (breaches, financial "
                    "distress) between formal reassessment cycles."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Relying exclusively on the security questionnaire the vendor completed before contract "
                    "signature, treating that snapshot as sufficient for the life of the contract"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A one-time onboarding snapshot does not account for changes in the vendor's "
                    "environment over time, which is the core gap ongoing monitoring is designed to address."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Assuming that a signed contract with security clauses guarantees the vendor's ongoing "
                    "compliance without further verification"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A signed contract establishes obligations but does not itself verify or "
                    "guarantee ongoing compliance; active monitoring is still required."
                ),
            },
        ],
        "explanation": (
            "Effective ongoing vendor risk monitoring combines periodic reassessment of updated attestations "
            "with continuous external monitoring (threat intel, breach disclosures, financial health) — not a "
            "one-time onboarding snapshot or blind reliance on contract language."
        ),
    },
    {
        "id": "nd5c-038",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A large manufacturer requires its critical raw-materials supplier to undergo a security assessment "
            "conducted directly by the manufacturer's own internal audit team, rather than relying on a report "
            "the supplier commissioned itself. What type of audit does this represent from the manufacturer's "
            "perspective?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A second-party audit",
                "correct": True,
                "rationale": (
                    "Correct. A second-party audit is conducted by one organization (the customer) directly "
                    "against another organization (its supplier/vendor) with whom it has a business "
                    "relationship, distinct from a first-party (internal) audit or an independent third-party "
                    "audit."
                ),
            },
            {
                "id": "b",
                "text": "A first-party (internal) audit",
                "correct": False,
                "rationale": (
                    "Incorrect. A first-party audit is conducted by an organization on itself; here the "
                    "manufacturer is auditing an external supplier, not its own operations."
                ),
            },
            {
                "id": "c",
                "text": "A third-party audit",
                "correct": False,
                "rationale": (
                    "Incorrect. A third-party audit is performed by an independent organization with no direct "
                    "business relationship to the entity being audited (e.g., a regulator or independent CPA "
                    "firm); here the manufacturer itself, a direct business party, is conducting the audit."
                ),
            },
            {
                "id": "d",
                "text": "A regulatory examination",
                "correct": False,
                "rationale": (
                    "Incorrect. A regulatory examination is conducted by a government or industry regulator with "
                    "legal authority, not by a business customer auditing its own supplier."
                ),
            },
        ],
        "explanation": (
            "A customer directly auditing its own supplier is a second-party audit — distinct from a first-party "
            "(self) audit or a third-party (independent) audit."
        ),
    },
    {
        "id": "nd5c-039",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A prospective customer asks a cloud vendor to prove its security posture. The vendor can provide "
            "either an independent auditor's SOC 2 Type II report (an attestation of control design and "
            "operating effectiveness over a review period) or an ISO/IEC 27001 certificate (confirmation that "
            "its information security management system conforms to a defined international standard, issued by "
            "an accredited certification body). What is the KEY distinction between these two forms of assurance?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An attestation (SOC 2) is an auditor's opinion on whether specific described controls were "
                    "suitably designed and operated effectively during a review period, while a certification "
                    "(ISO 27001) confirms an organization's management system conforms to the requirements of a "
                    "specific, externally defined standard"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This captures the fundamental distinction: SOC 2 is an opinion on entity-specific "
                    "described controls, while ISO 27001 certification confirms conformance to a standardized "
                    "management-system framework."
                ),
            },
            {
                "id": "b",
                "text": (
                    "They are functionally identical, since both are produced by independent, accredited "
                    "external assessors using the same underlying framework"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SOC 2 is based on the AICPA Trust Services Criteria describing entity-specific "
                    "controls, while ISO 27001 certification confirms conformance to a distinct, standardized "
                    "ISMS framework; the review approach and resulting deliverable differ."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SOC 2 is a one-time, point-in-time snapshot with no ongoing surveillance, while ISO 27001 "
                    "certification requires continuous, unbroken real-time monitoring with no periodic "
                    "reassessment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A SOC 2 Type II report itself already covers a review period, not a single point "
                    "in time, and ISO 27001 certification involves periodic surveillance audits and periodic "
                    "recertification, not continuous real-time monitoring."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Certification (ISO 27001) is always a stronger form of assurance than attestation (SOC 2) "
                    "for every use case, making SOC 2 reports unnecessary once ISO certification is obtained"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The two serve different purposes and audiences; many customers specifically "
                    "require a SOC 2 report regardless of ISO certification status, so one does not universally "
                    "substitute for the other."
                ),
            },
        ],
        "explanation": (
            "An attestation (SOC 2) is an auditor's opinion on specific, described controls over a review "
            "period. A certification (ISO 27001) confirms conformance of a management system to a standardized, "
            "externally defined framework. Neither universally substitutes for the other."
        ),
    },
    {
        "id": "nd5c-040",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A client wants a penetration test that most realistically simulates an external attacker with zero "
            "prior knowledge of the target's internal network topology, credentials, or architecture, in order "
            "to test detection and response capabilities from a true outsider's perspective. Which test "
            "environment type should be specified in the rules of engagement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unknown environment (black-box) testing",
                "correct": True,
                "rationale": (
                    "Correct. The tester is given no prior internal knowledge, most closely simulating a true "
                    "external attacker and testing detection/response from a cold start."
                ),
            },
            {
                "id": "b",
                "text": "Known environment (white-box) testing",
                "correct": False,
                "rationale": (
                    "Incorrect. Testers are given full internal knowledge (network diagrams, source code, "
                    "credentials), which accelerates testing but does not simulate a zero-knowledge external "
                    "attacker."
                ),
            },
            {
                "id": "c",
                "text": "Partially known environment (gray-box) testing",
                "correct": False,
                "rationale": (
                    "Incorrect. Testers are given some but not complete knowledge (e.g., limited credentials or "
                    "partial architecture information), a middle ground that doesn't match the stated "
                    "zero-prior-knowledge requirement."
                ),
            },
            {
                "id": "d",
                "text": "A vulnerability scan",
                "correct": False,
                "rationale": (
                    "Incorrect. An automated vulnerability scan identifies potential weaknesses without any "
                    "active exploitation and is not itself a penetration test environment/knowledge "
                    "classification."
                ),
            },
        ],
        "explanation": (
            "Unknown environment (black-box) testing gives the tester zero prior internal knowledge, most "
            "realistically simulating an external attacker with no inside information — distinct from known "
            "(white-box) and partially known (gray-box) testing."
        ),
    },
]
