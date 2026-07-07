"""
CompTIA Security+ (SY0-701) Domain 5: Security Program Management and Oversight
Study notes covering objectives 5.1 through 5.6.
"""

NOTES = [
    {
        "domain": 5,
        "topic": "Security governance & policies",
        "objective": "5.1",
        "video": "Security Governance",
        "study_topics": ["Security governance & policies"],
        "body": (
            "<p>Security governance is the framework of policies, procedures, standards, and guidelines "
            "that direct an organization's information security program. Governance ensures that security "
            "activities align with business objectives and satisfy legal/regulatory requirements.</p>"
            "<p><strong>Key governance documents:</strong></p>"
            "<ul>"
            "<li><strong>Policy</strong> – High-level management directive (e.g., Acceptable Use Policy). "
            "Sets intent; mandatory and enforceable.</li>"
            "<li><strong>Standard</strong> – Specific mandatory requirements that implement a policy "
            "(e.g., password must be 12+ characters).</li>"
            "<li><strong>Guideline</strong> – Recommended best practices; not mandatory.</li>"
            "<li><strong>Procedure</strong> – Step-by-step instructions to perform a task.</li>"
            "<li><strong>Baseline</strong> – Minimum security configuration for a system type.</li>"
            "</ul>"
            "<p><strong>Governance structures:</strong></p>"
            "<ul>"
            "<li><strong>Board of Directors / Executives</strong> – Set risk appetite and strategic direction.</li>"
            "<li><strong>CISO</strong> – Owns the security program; reports to executive leadership.</li>"
            "<li><strong>Security committee</strong> – Cross-functional team that reviews policy and risk.</li>"
            "</ul>"
            "<p><strong>Regulatory drivers:</strong> HIPAA (healthcare PHI), PCI-DSS (payment card data), "
            "SOX (financial controls), FERPA (student records), and GDPR (EU personal data) all impose "
            "policy requirements. Organizations must map internal policies to applicable regulations.</p>"
            "<p><strong>Policy lifecycle:</strong> Draft → Review → Approve → Publish → Train → Enforce → Review/Update.</p>"
        ),
        "key_points": [
            "Policies are mandatory management directives; guidelines are recommended.",
            "Standards define specific, measurable requirements that implement a policy.",
            "The CISO owns the security program and typically reports to the CIO or CEO.",
            "Regulatory frameworks (HIPAA, PCI-DSS, GDPR) drive policy requirements.",
            "Baselines define the minimum acceptable security configuration for a system type.",
        ],
    },
    {
        "domain": 5,
        "topic": "Risk management strategies",
        "objective": "5.2",
        "video": "Risk Management",
        "study_topics": ["Risk management strategies"],
        "body": (
            "<p>Risk management is the continuous process of identifying, assessing, and responding to risks "
            "that could impact organizational assets. The four core risk response strategies are:</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Strategy</th><th>Description</th><th>Example</th></tr>"
            "<tr><td><strong>Avoid</strong></td><td>Eliminate the activity that creates the risk.</td>"
            "<td>Discontinue a vulnerable legacy application.</td></tr>"
            "<tr><td><strong>Transfer (Share)</strong></td><td>Shift financial impact to a third party.</td>"
            "<td>Purchase cyber liability insurance; outsource to a managed service provider.</td></tr>"
            "<tr><td><strong>Mitigate (Reduce)</strong></td><td>Implement controls to lower probability or impact.</td>"
            "<td>Deploy firewalls, patch management, MFA.</td></tr>"
            "<tr><td><strong>Accept</strong></td><td>Acknowledge the risk and take no further action.</td>"
            "<td>Accept residual risk after controls are in place; document in risk register.</td></tr>"
            "</table>"
            "<p><strong>Risk terminology:</strong></p>"
            "<ul>"
            "<li><strong>Inherent risk</strong> – Risk before any controls are applied.</li>"
            "<li><strong>Residual risk</strong> – Risk remaining after controls are implemented.</li>"
            "<li><strong>Risk appetite</strong> – Total risk an organization is willing to accept.</li>"
            "<li><strong>Risk tolerance</strong> – Acceptable deviation from the risk appetite.</li>"
            "<li><strong>Risk threshold</strong> – The point at which risk becomes unacceptable.</li>"
            "</ul>"
            "<p><strong>Risk assessment types:</strong></p>"
            "<ul>"
            "<li><strong>Qualitative</strong> – Uses descriptive ratings (High/Medium/Low) and expert judgment.</li>"
            "<li><strong>Quantitative</strong> – Uses numerical values and financial calculations (SLE, ALE, ARO).</li>"
            "<li><strong>Semi-quantitative</strong> – Assigns numerical scores to qualitative ratings.</li>"
            "</ul>"
        ),
        "key_points": [
            "The four risk strategies are: Avoid, Transfer, Mitigate, and Accept.",
            "Risk transference includes cyber insurance and outsourcing to third parties.",
            "Residual risk is what remains after controls are applied; it should be accepted formally.",
            "Risk acceptance must be documented and signed off by appropriate management.",
            "Risk appetite is the total risk an org will accept; tolerance is the acceptable variance.",
        ],
    },
    {
        "domain": 5,
        "topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "objective": "5.2",
        "video": "Risk Analysis",
        "study_topics": ["Quantitative risk analysis (SLE/ALE/ARO)"],
        "body": (
            "<p>Quantitative risk analysis assigns monetary values to risks, enabling objective prioritization "
            "and cost-benefit analysis of security controls.</p>"
            "<p><strong>Core formulas:</strong></p>"
            "<ul>"
            "<li><strong>SLE (Single Loss Expectancy)</strong> = Asset Value (AV) × Exposure Factor (EF)</li>"
            "<li><strong>ALE (Annualized Loss Expectancy)</strong> = SLE × ARO</li>"
            "<li><strong>ARO (Annualized Rate of Occurrence)</strong> = Expected number of times an event occurs per year</li>"
            "<li><strong>Cost-benefit check</strong>: Implement a control only if its annual cost &lt; ALE reduction</li>"
            "</ul>"
            "<p><strong>Definitions:</strong></p>"
            "<ul>"
            "<li><strong>Asset Value (AV)</strong> – Dollar value of the asset (hardware, data, reputation).</li>"
            "<li><strong>Exposure Factor (EF)</strong> – Percentage of asset value lost in a single incident (0–1).</li>"
            "<li><strong>SLE</strong> – Expected monetary loss from a single occurrence of the threat.</li>"
            "<li><strong>ARO</strong> – How many times the event is expected to occur in one year.</li>"
            "<li><strong>ALE</strong> – Expected annual monetary loss from a specific threat.</li>"
            "</ul>"
            "<p><strong>Worked example:</strong></p>"
            "<ul>"
            "<li>A web server is valued at <strong>$200,000</strong>.</li>"
            "<li>A ransomware attack would destroy <strong>40%</strong> of its value (EF = 0.40).</li>"
            "<li>Ransomware attacks are expected <strong>twice per year</strong> (ARO = 2).</li>"
            "<li>SLE = $200,000 × 0.40 = <strong>$80,000</strong></li>"
            "<li>ALE = $80,000 × 2 = <strong>$160,000/year</strong></li>"
            "<li>A security control costing $50,000/year that reduces ARO to 0.5 yields:</li>"
            "<li>New ALE = $80,000 × 0.5 = $40,000 → Savings = $120,000 &gt; $50,000 cost → <strong>justified</strong></li>"
            "</ul>"
        ),
        "key_points": [
            "SLE = Asset Value × Exposure Factor (dollar loss per single incident).",
            "ALE = SLE × ARO (expected annual dollar loss from a threat).",
            "ARO is the annualized rate of occurrence (e.g., 0.5 = once every two years).",
            "A control is cost-effective when its annual cost is less than the ALE reduction it provides.",
            "Exposure Factor (EF) is expressed as a percentage (0 to 1) of asset value lost per event.",
        ],
    },
    {
        "domain": 5,
        "topic": "Risk register & appetite",
        "objective": "5.2",
        "video": "Risk Register",
        "study_topics": ["Risk register & appetite"],
        "body": (
            "<p>A <strong>risk register</strong> (also called a risk log) is the authoritative document used to "
            "track identified risks, their assessed likelihood and impact, assigned owners, and the chosen "
            "response strategy and controls.</p>"
            "<p><strong>Typical risk register columns:</strong></p>"
            "<ul>"
            "<li>Risk ID and description</li>"
            "<li>Threat source and vulnerability</li>"
            "<li>Likelihood rating (e.g., 1–5 scale)</li>"
            "<li>Impact rating (e.g., 1–5 scale)</li>"
            "<li>Risk score (Likelihood × Impact)</li>"
            "<li>Response strategy (avoid/transfer/mitigate/accept)</li>"
            "<li>Control(s) applied</li>"
            "<li>Residual risk score</li>"
            "<li>Risk owner</li>"
            "<li>Review date</li>"
            "</ul>"
            "<p><strong>Risk appetite vs. risk tolerance:</strong></p>"
            "<ul>"
            "<li><strong>Risk appetite</strong> – The overall level of risk an organization is willing to pursue "
            "or retain in order to achieve its objectives. Set by executive leadership / board.</li>"
            "<li><strong>Risk tolerance</strong> – The acceptable variance or deviation around the risk appetite "
            "(the &ldquo;wiggle room&rdquo;).</li>"
            "<li><strong>Risk threshold</strong> – A specific point beyond which a risk requires escalation "
            "or mandatory action.</li>"
            "</ul>"
            "<p>Risk appetite directly influences how risks are treated in the register. A low risk appetite means "
            "even moderate risks require mitigation; a high risk appetite may allow more residual risk to be accepted.</p>"
            "<p><strong>Risk heat map</strong> – A visual matrix plotting likelihood vs. impact to quickly "
            "communicate risk severity across the organization.</p>"
        ),
        "key_points": [
            "The risk register tracks all identified risks, owners, scores, responses, and residual risk.",
            "Risk appetite is set by executives/board and reflects how much risk the org will accept.",
            "Risk tolerance defines acceptable variance around the appetite; threshold triggers escalation.",
            "Each risk in the register must have a named owner accountable for the response.",
            "A risk heat map visualizes likelihood vs. impact to prioritize risk treatment.",
        ],
    },
    {
        "domain": 5,
        "topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "objective": "5.4",
        "video": "Business Impact Analysis",
        "study_topics": ["Business impact analysis (RTO/RPO/MTTR/MTBF)"],
        "body": (
            "<p>A <strong>Business Impact Analysis (BIA)</strong> identifies critical business functions "
            "and quantifies the impact of disruptions. BIA outputs drive recovery planning and resource allocation.</p>"
            "<p><strong>Key BIA metrics:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Metric</th><th>Definition</th><th>Who sets it</th></tr>"
            "<tr><td><strong>RTO (Recovery Time Objective)</strong></td>"
            "<td>Maximum acceptable time to restore a function after disruption.</td>"
            "<td>Business owners</td></tr>"
            "<tr><td><strong>RPO (Recovery Point Objective)</strong></td>"
            "<td>Maximum acceptable data loss measured in time (how old can the restored data be?).</td>"
            "<td>Business owners</td></tr>"
            "<tr><td><strong>MTTR (Mean Time to Repair/Restore)</strong></td>"
            "<td>Average time to repair a failed component and restore service.</td>"
            "<td>IT/Operations (measured)</td></tr>"
            "<tr><td><strong>MTBF (Mean Time Between Failures)</strong></td>"
            "<td>Average time between successive failures of a system; measures reliability.</td>"
            "<td>IT/Operations (measured)</td></tr>"
            "</table>"
            "<p><strong>Additional BIA concepts:</strong></p>"
            "<ul>"
            "<li><strong>MTTF (Mean Time to Failure)</strong> – Used for non-repairable components; "
            "average lifespan before first failure.</li>"
            "<li><strong>Maximum Tolerable Downtime (MTD)</strong> – The absolute maximum time a business "
            "process can be unavailable before causing irreversible harm. RTO must be &le; MTD.</li>"
            "<li><strong>Critical path analysis</strong> – Identifies dependent systems that must recover "
            "in sequence.</li>"
            "</ul>"
            "<p><strong>Example:</strong> If RPO = 4 hours, backups must run at least every 4 hours. "
            "If RTO = 2 hours, recovery procedures must restore service within 2 hours.</p>"
        ),
        "key_points": [
            "RTO is the maximum time allowed to restore a system after failure (time-based goal).",
            "RPO defines the maximum acceptable data loss measured in time (backup frequency driver).",
            "MTTR is the average repair time; lower MTTR indicates better incident response capability.",
            "MTBF measures reliability; higher MTBF means fewer failures over time.",
            "RTO must always be less than or equal to the Maximum Tolerable Downtime (MTD).",
        ],
    },
    {
        "domain": 5,
        "topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "objective": "5.3",
        "video": "Third-Party Agreements",
        "study_topics": ["Third-party agreements (SLA/MOU/MSA/BPA)"],
        "body": (
            "<p>Organizations use formal agreements to define expectations, responsibilities, and security "
            "requirements when working with third parties. Knowing each agreement type is critical for the exam.</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Agreement</th><th>Full Name</th><th>Purpose</th></tr>"
            "<tr><td><strong>SLA</strong></td><td>Service Level Agreement</td>"
            "<td>Defines measurable service standards (uptime %, response times, penalties). Legally binding.</td></tr>"
            "<tr><td><strong>MOU / MOA</strong></td><td>Memorandum of Understanding / Agreement</td>"
            "<td>Documents a general intent to cooperate; less formal, often between government or internal entities. "
            "Usually not legally binding.</td></tr>"
            "<tr><td><strong>MSA</strong></td><td>Master Service Agreement</td>"
            "<td>Umbrella contract covering general terms; individual work governed by SOWs.</td></tr>"
            "<tr><td><strong>BPA</strong></td><td>Business Partnership Agreement</td>"
            "<td>Defines responsibilities, liabilities, and profit-sharing between business partners.</td></tr>"
            "<tr><td><strong>SOW</strong></td><td>Statement of Work</td>"
            "<td>Details specific deliverables, timelines, and costs for a project under an MSA.</td></tr>"
            "<tr><td><strong>NDA</strong></td><td>Non-Disclosure Agreement</td>"
            "<td>Legally binds parties to protect confidential information shared during business dealings.</td></tr>"
            "</table>"
            "<p><strong>Security considerations in third-party agreements:</strong></p>"
            "<ul>"
            "<li>Include right-to-audit clauses to verify vendor security posture.</li>"
            "<li>Specify data handling, breach notification timelines, and encryption requirements.</li>"
            "<li>Define ownership of data and intellectual property.</li>"
            "<li>Include termination procedures and data return/destruction requirements.</li>"
            "</ul>"
        ),
        "key_points": [
            "SLA defines measurable service metrics and is legally binding; MOU/MOA is typically not.",
            "MSA is the overarching contract; SOW describes specific work under that contract.",
            "BPA governs relationships between business partners, including profit and liability.",
            "NDAs protect confidential information and are legally enforceable.",
            "Agreements should include right-to-audit clauses and breach notification requirements.",
        ],
    },
    {
        "domain": 5,
        "topic": "Vendor risk management",
        "objective": "5.3",
        "video": "Vendor Risk Management",
        "study_topics": ["Vendor risk management"],
        "body": (
            "<p>Vendor risk management (also called supply chain risk management) ensures that third-party "
            "relationships do not introduce unacceptable risk into the organization.</p>"
            "<p><strong>Vendor assessment activities:</strong></p>"
            "<ul>"
            "<li><strong>Due diligence</strong> – Review vendor security policies, certifications (SOC 2, ISO 27001), "
            "financial stability, and references before engagement.</li>"
            "<li><strong>Questionnaires / self-assessments</strong> – Standardized forms (e.g., SIG, CAIQ) "
            "asking vendors about security controls.</li>"
            "<li><strong>Third-party audits</strong> – Independent auditors verify vendor controls (SOC 2 Type II).</li>"
            "<li><strong>Penetration testing</strong> – May be required by contract for vendors handling sensitive data.</li>"
            "<li><strong>Ongoing monitoring</strong> – Continuous assessment via risk platforms (e.g., SecurityScorecard, "
            "BitSight) rather than point-in-time reviews only.</li>"
            "</ul>"
            "<p><strong>Supply chain risks:</strong></p>"
            "<ul>"
            "<li><strong>Hardware tampering</strong> – Malicious components inserted during manufacturing.</li>"
            "<li><strong>Software supply chain</strong> – Malicious code in open-source dependencies or "
            "software updates (e.g., SolarWinds attack).</li>"
            "<li><strong>Fourth-party risk</strong> – Risk introduced by your vendor's vendors.</li>"
            "</ul>"
            "<p><strong>Vendor lifecycle management:</strong></p>"
            "<ol>"
            "<li>Selection and due diligence</li>"
            "<li>Contract negotiation (security requirements, SLA, right-to-audit)</li>"
            "<li>Onboarding and access provisioning</li>"
            "<li>Ongoing monitoring and periodic reassessment</li>"
            "<li>Offboarding (access revocation, data return/destruction)</li>"
            "</ol>"
        ),
        "key_points": [
            "Due diligence before signing includes reviewing SOC 2 reports, certifications, and financials.",
            "SOC 2 Type II reports cover a period of time and are more valuable than Type I (point-in-time).",
            "Supply chain attacks target hardware or software dependencies to compromise downstream organizations.",
            "Right-to-audit clauses in contracts allow the organization to verify vendor security controls.",
            "Vendor risk must be reassessed continuously, not just at onboarding.",
        ],
    },
    {
        "domain": 5,
        "topic": "Compliance & privacy (GDPR)",
        "objective": "5.5",
        "video": "Compliance and Privacy",
        "study_topics": ["Compliance & privacy (GDPR)"],
        "body": (
            "<p>Compliance involves adhering to laws, regulations, and standards applicable to the organization. "
            "Privacy focuses on protecting personal data and giving individuals control over their information.</p>"
            "<p><strong>Key regulations:</strong></p>"
            "<ul>"
            "<li><strong>GDPR (General Data Protection Regulation)</strong> – EU regulation protecting personal "
            "data of EU residents. Applies to any organization processing EU personal data regardless of location.</li>"
            "<li><strong>HIPAA</strong> – U.S. law protecting health information (PHI).</li>"
            "<li><strong>PCI-DSS</strong> – Industry standard for payment card data security.</li>"
            "<li><strong>CCPA</strong> – California Consumer Privacy Act; grants California residents data rights.</li>"
            "<li><strong>SOX</strong> – Sarbanes-Oxley; financial reporting controls for public companies.</li>"
            "</ul>"
            "<p><strong>GDPR key principles:</strong></p>"
            "<ul>"
            "<li>Lawfulness, fairness, and transparency in processing</li>"
            "<li>Purpose limitation – data collected for specified, explicit purposes</li>"
            "<li>Data minimization – collect only what is necessary</li>"
            "<li>Accuracy – keep data up to date</li>"
            "<li>Storage limitation – retain only as long as necessary</li>"
            "<li>Integrity and confidentiality – protect with appropriate security</li>"
            "</ul>"
            "<p><strong>Individual rights under GDPR:</strong> Right to access, right to rectification, "
            "right to erasure (&ldquo;right to be forgotten&rdquo;), right to data portability, "
            "right to object, right to restrict processing.</p>"
            "<p><strong>Breach notification:</strong> GDPR requires notification to supervisory authority "
            "within <strong>72 hours</strong> of discovery; affected individuals notified without undue delay.</p>"
        ),
        "key_points": [
            "GDPR applies to any organization processing EU residents' personal data, regardless of location.",
            "GDPR requires breach notification to supervisory authority within 72 hours of discovery.",
            "Data minimization means collecting only data that is necessary for the stated purpose.",
            "The right to erasure ('right to be forgotten') allows individuals to request deletion of their data.",
            "Privacy by design means integrating privacy controls into systems from the start, not as an afterthought.",
        ],
    },
    {
        "domain": 5,
        "topic": "Data roles (controller/processor/custodian)",
        "objective": "5.5",
        "video": "Data Roles and Responsibilities",
        "study_topics": ["Data roles (controller/processor/custodian)"],
        "body": (
            "<p>Defining data roles establishes accountability for data throughout its lifecycle. "
            "These roles appear in both corporate governance frameworks and legal regulations like GDPR.</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Role</th><th>Responsibilities</th></tr>"
            "<tr><td><strong>Data Owner</strong></td>"
            "<td>Senior manager/executive accountable for a data set. Sets classification level, "
            "approves access policies, and accepts residual risk. Ultimately responsible for the data.</td></tr>"
            "<tr><td><strong>Data Steward</strong></td>"
            "<td>Manages data quality, metadata, and ensures data is used consistently per policy. "
            "Bridges owner and custodian.</td></tr>"
            "<tr><td><strong>Data Custodian</strong></td>"
            "<td>IT staff responsible for the day-to-day technical protection of data: backups, "
            "encryption, access control implementation. Does NOT set policy.</td></tr>"
            "<tr><td><strong>Data Processor (GDPR)</strong></td>"
            "<td>Organization or individual that processes personal data on behalf of the controller. "
            "Must follow controller's instructions and sign a Data Processing Agreement (DPA).</td></tr>"
            "<tr><td><strong>Data Controller (GDPR)</strong></td>"
            "<td>Determines the purposes and means of processing personal data. Bears primary legal "
            "responsibility under GDPR. Equivalent to the data owner in many frameworks.</td></tr>"
            "<tr><td><strong>Data Subject (GDPR)</strong></td>"
            "<td>The individual whose personal data is being processed; has rights under GDPR.</td></tr>"
            "</table>"
            "<p><strong>Privacy Officer / DPO (Data Protection Officer)</strong> – Required under GDPR for "
            "certain organizations. Oversees compliance with data protection laws, serves as point of contact "
            "for supervisory authorities and data subjects.</p>"
        ),
        "key_points": [
            "Data owner is the accountable executive; data custodian is IT staff who implements protections.",
            "Under GDPR, the data controller determines how/why data is processed; the processor acts on their behalf.",
            "Data processors must have a signed Data Processing Agreement (DPA) with the controller.",
            "Data stewards focus on data quality and ensuring consistent application of data policies.",
            "The DPO (Data Protection Officer) oversees GDPR compliance and is required for certain organizations.",
        ],
    },
    {
        "domain": 5,
        "topic": "Data classification levels",
        "objective": "5.5",
        "video": "Data Classification",
        "study_topics": ["Data classification levels"],
        "body": (
            "<p>Data classification assigns sensitivity labels to data so that appropriate security controls "
            "can be applied. Classification drives decisions about encryption, access control, handling, "
            "storage, and disposal.</p>"
            "<p><strong>Government / military classification levels (high to low):</strong></p>"
            "<ul>"
            "<li><strong>Top Secret</strong> – Unauthorized disclosure could cause exceptionally grave damage to national security.</li>"
            "<li><strong>Secret</strong> – Unauthorized disclosure could cause serious damage to national security.</li>"
            "<li><strong>Confidential</strong> – Unauthorized disclosure could cause damage to national security.</li>"
            "<li><strong>Unclassified</strong> – Not sensitive; publicly releasable.</li>"
            "</ul>"
            "<p><strong>Corporate / commercial classification levels (common framework):</strong></p>"
            "<ul>"
            "<li><strong>Public (Unrestricted)</strong> – Approved for public release; no harm if disclosed.</li>"
            "<li><strong>Internal / Private</strong> – For internal use only; limited harm if disclosed.</li>"
            "<li><strong>Confidential / Sensitive</strong> – Restricted; significant harm if disclosed (e.g., PII, financials).</li>"
            "<li><strong>Restricted / Critical</strong> – Highest corporate sensitivity; severe harm if disclosed "
            "(e.g., trade secrets, regulated data).</li>"
            "</ul>"
            "<p><strong>Classification process:</strong></p>"
            "<ol>"
            "<li>Data owner identifies and classifies data assets.</li>"
            "<li>Apply labels and markings to data and containers.</li>"
            "<li>Implement controls matching the classification (encryption, access restrictions, DLP).</li>"
            "<li>Train users on handling requirements for each level.</li>"
            "<li>Reclassify or declassify as data sensitivity changes over time.</li>"
            "</ol>"
            "<p><strong>Data Loss Prevention (DLP)</strong> tools can enforce classification policies by "
            "scanning for sensitive data patterns and blocking unauthorized transfers.</p>"
        ),
        "key_points": [
            "Government classifications (Top Secret, Secret, Confidential, Unclassified) are based on national security impact.",
            "Corporate classifications typically map to: Public, Internal, Confidential, and Restricted.",
            "The data owner is responsible for assigning the classification level.",
            "Controls (encryption, access, DLP) must be commensurate with the classification level.",
            "Data should be reclassified or declassified as its sensitivity changes over time.",
        ],
    },
    {
        "domain": 5,
        "topic": "Audits & penetration testing",
        "objective": "5.6",
        "video": "Audits and Assessments",
        "study_topics": ["Audits & penetration testing"],
        "body": (
            "<p>Audits and assessments verify that security controls are in place, operating effectively, "
            "and meeting policy and regulatory requirements.</p>"
            "<p><strong>Audit types:</strong></p>"
            "<ul>"
            "<li><strong>Internal audit</strong> – Conducted by the organization's own audit team; "
            "identifies gaps before external review.</li>"
            "<li><strong>External audit</strong> – Independent third-party auditors; results carry more "
            "credibility (e.g., SOC 2, ISO 27001 certification audit).</li>"
            "<li><strong>Compliance audit</strong> – Verifies adherence to a specific regulation or standard "
            "(PCI-DSS QSA assessment, HIPAA audit).</li>"
            "</ul>"
            "<p><strong>Penetration testing phases:</strong></p>"
            "<ol>"
            "<li><strong>Reconnaissance</strong> – Gather information about the target (passive or active).</li>"
            "<li><strong>Scanning / Enumeration</strong> – Identify open ports, services, and vulnerabilities.</li>"
            "<li><strong>Exploitation</strong> – Attempt to exploit vulnerabilities to gain access.</li>"
            "<li><strong>Post-exploitation</strong> – Assess impact, move laterally, escalate privileges.</li>"
            "<li><strong>Reporting</strong> – Document findings, risk ratings, and remediation recommendations.</li>"
            "</ol>"
            "<p><strong>Penetration test types:</strong></p>"
            "<ul>"
            "<li><strong>Black box</strong> – Tester has no prior knowledge of the environment.</li>"
            "<li><strong>White box</strong> – Tester has full knowledge (source code, network diagrams).</li>"
            "<li><strong>Gray box</strong> – Tester has partial knowledge (e.g., valid user credentials).</li>"
            "</ul>"
            "<p><strong>Vulnerability assessment vs. penetration test:</strong> Vulnerability scanning identifies "
            "potential weaknesses without exploiting them; penetration testing actively exploits vulnerabilities "
            "to demonstrate real-world impact.</p>"
            "<p>Always obtain written authorization (<strong>Rules of Engagement / ROE</strong>) before testing.</p>"
        ),
        "key_points": [
            "Penetration testing actively exploits vulnerabilities; vulnerability scanning only identifies them.",
            "Black box = no prior knowledge; white box = full knowledge; gray box = partial knowledge.",
            "Always get written authorization (Rules of Engagement) before conducting penetration tests.",
            "SOC 2 Type II is an external audit covering a period of time, more valuable than Type I.",
            "Pen test phases: Reconnaissance → Scanning → Exploitation → Post-exploitation → Reporting.",
        ],
    },
    {
        "domain": 5,
        "topic": "Security awareness training",
        "objective": "5.6",
        "video": "Security Awareness",
        "study_topics": ["Security awareness training"],
        "body": (
            "<p>Security awareness training is one of the most cost-effective security controls. "
            "It reduces the human element of risk by ensuring employees recognize threats and follow "
            "secure behaviors.</p>"
            "<p><strong>Key training topics to include:</strong></p>"
            "<ul>"
            "<li>Phishing and social engineering recognition</li>"
            "<li>Password hygiene and use of password managers/MFA</li>"
            "<li>Physical security (tailgating, clean desk policy, screen locking)</li>"
            "<li>Data handling and classification requirements</li>"
            "<li>Incident reporting procedures</li>"
            "<li>Acceptable use of corporate systems and data</li>"
            "<li>Removable media and BYOD policies</li>"
            "</ul>"
            "<p><strong>Training delivery methods:</strong></p>"
            "<ul>"
            "<li><strong>Computer-based training (CBT)</strong> – Scalable online modules with quizzes.</li>"
            "<li><strong>Phishing simulations</strong> – Fake phishing emails sent to employees to measure "
            "click rates and reinforce awareness.</li>"
            "<li><strong>Gamification</strong> – Points, badges, and competitions to increase engagement.</li>"
            "<li><strong>In-person / live training</strong> – Workshops, lunch-and-learns, tabletop exercises.</li>"
            "<li><strong>Posters and newsletters</strong> – Ongoing reminders for key security behaviors.</li>"
            "</ul>"
            "<p><strong>Measuring effectiveness:</strong></p>"
            "<ul>"
            "<li>Phishing simulation click rates (before vs. after training)</li>"
            "<li>Number of reported incidents vs. actual incidents</li>"
            "<li>Quiz/assessment pass rates</li>"
            "<li>Security incident trends attributed to human error</li>"
            "</ul>"
            "<p><strong>Role-based training</strong> ensures that users receive training relevant to their "
            "specific job functions and access levels (e.g., developers trained on secure coding, "
            "executives on spear phishing).</p>"
        ),
        "key_points": [
            "Security awareness training is one of the most cost-effective controls against social engineering.",
            "Phishing simulations measure real-world susceptibility and reinforce training outcomes.",
            "Role-based training tailors content to specific job functions and access levels.",
            "Effectiveness is measured by click rates, incident reporting rates, and quiz pass rates.",
            "Training should be recurring, not a one-time event; threats and policies evolve.",
        ],
    },
    {
        "domain": 5,
        "topic": "Secure asset decommissioning and media sanitization",
        "objective": "5.5",
        "video": "Data Destruction and Media Sanitization",
        "study_topics": ["Secure asset decommissioning and media sanitization"],
        "body": (
            "<p>When assets reach end-of-life, data must be securely destroyed to prevent unauthorized "
            "recovery. The appropriate sanitization method depends on data sensitivity and media type.</p>"
            "<p><strong>Media sanitization methods (NIST SP 800-88 framework):</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Method</th><th>Description</th><th>Use Case</th></tr>"
            "<tr><td><strong>Clear</strong></td>"
            "<td>Overwrite data using standard write commands (e.g., zero-fill). Protects against "
            "basic recovery tools.</td>"
            "<td>Reuse within the same organization at the same classification level.</td></tr>"
            "<tr><td><strong>Purge</strong></td>"
            "<td>Use advanced techniques (cryptographic erase, secure erase commands) that prevent "
            "recovery even with laboratory equipment.</td>"
            "<td>Media to be reused outside the organization or in lower-trust environments.</td></tr>"
            "<tr><td><strong>Destroy</strong></td>"
            "<td>Physical destruction: shredding, disintegration, incineration, degaussing (magnetic), "
            "or pulverization. Renders media completely unusable.</td>"
            "<td>Highest-sensitivity data; end-of-life media with no reuse value.</td></tr>"
            "</table>"
            "<p><strong>Additional sanitization techniques:</strong></p>"
            "<ul>"
            "<li><strong>Degaussing</strong> – Exposes magnetic media to a strong magnetic field; "
            "destroys data but also renders the drive unusable. Does NOT work on SSDs.</li>"
            "<li><strong>Cryptographic erasure (crypto-shredding)</strong> – Destroys the encryption key "
            "for encrypted data, making it unrecoverable. Fast and effective for SSDs and cloud storage.</li>"
            "<li><strong>Shredding</strong> – Physical shredding of HDDs, optical media, or paper.</li>"
            "</ul>"
            "<p><strong>Certificate of destruction</strong> – Third-party vendors should provide a "
            "certificate of destruction as proof that media was securely sanitized or destroyed.</p>"
            "<p><strong>Secure decommissioning process:</strong> Inventory → Data backup → Remove from service "
            "→ Apply sanitization → Update asset records → Dispose / transfer / store.</p>"
        ),
        "key_points": [
            "NIST SP 800-88 defines three sanitization categories: Clear, Purge, and Destroy.",
            "Degaussing destroys data on magnetic media by exposing it to a strong magnetic field but does not work on SSDs.",
            "Cryptographic erasure (crypto-shredding) destroys the encryption key, making encrypted data unrecoverable.",
            "Destroy (shredding, incineration, pulverization) is required for highest-sensitivity data at end-of-life.",
            "Always obtain a certificate of destruction from third-party disposal vendors.",
        ],
    },
]
