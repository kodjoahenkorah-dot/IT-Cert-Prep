"""
CompTIA A+ Core 2 (220-1202) — Domain 4: Operational Procedures
Study notes aligned with Professor Messer's 220-1202 playlist order.
"""

NOTES = [
    {
        "domain": 4,
        "topic": "Documentation and ticketing systems",
        "objective": "4.1",
        "video": "Documentation and Support Systems",
        "study_topics": ["Documentation & ticketing"],
        "body": (
            "<p>Proper documentation and ticketing are the backbone of an efficient IT support operation. "
            "Every interaction with a user or system should be recorded so that problems can be tracked, "
            "escalated, and resolved consistently.</p>"
            "<h3>Help Desk / Ticketing Systems</h3>"
            "<ul>"
            "<li><strong>Ticket</strong> – a formal record of a reported issue; contains user info, description, "
            "priority, assigned technician, timestamps, and resolution notes.</li>"
            "<li><strong>Categories</strong> – tickets are classified (hardware, software, network, security) so "
            "they can be routed to the correct team.</li>"
            "<li><strong>Priority levels</strong> – typically Low / Medium / High / Critical, based on business "
            "impact and number of users affected.</li>"
            "<li><strong>Escalation</strong> – if Tier 1 cannot resolve, the ticket is escalated to Tier 2 or "
            "Tier 3 with all notes intact.</li>"
            "</ul>"
            "<h3>Key Documentation Types</h3>"
            "<ul>"
            "<li><strong>Network diagrams</strong> – logical and physical maps of the infrastructure.</li>"
            "<li><strong>Knowledge base</strong> – searchable articles with known fixes and procedures.</li>"
            "<li><strong>Runbooks / SOPs</strong> – step-by-step standard operating procedures.</li>"
            "<li><strong>Inventory / asset lists</strong> – hardware and software records.</li>"
            "<li><strong>Acceptable Use Policy (AUP)</strong> – rules governing employee use of IT resources.</li>"
            "</ul>"
            "<h3>Best Practices</h3>"
            "<ul>"
            "<li>Document steps taken and outcomes, not just the final fix.</li>"
            "<li>Use clear, jargon-free language so other technicians can follow up.</li>"
            "<li>Close tickets only after confirming user satisfaction.</li>"
            "<li>Review closed tickets to identify recurring problems (trend analysis).</li>"
            "</ul>"
        ),
        "key_points": [
            "Every incident should generate a ticket with description, priority, and resolution notes.",
            "Escalation passes the ticket—with all notes—to the next support tier.",
            "Knowledge bases reduce repeat resolution time by documenting known fixes.",
            "Trend analysis of closed tickets reveals systemic problems.",
            "SOPs ensure consistent, repeatable procedures across the team.",
        ],
    },
    {
        "domain": 4,
        "topic": "Asset management",
        "objective": "4.1",
        "video": "Asset Management",
        "study_topics": ["Asset management"],
        "body": (
            "<p>Asset management is the systematic tracking of an organization's hardware and software "
            "resources throughout their entire lifecycle — from procurement to disposal.</p>"
            "<h3>Hardware Asset Tracking</h3>"
            "<ul>"
            "<li><strong>Asset tags</strong> – physical labels (barcode or RFID) affixed to devices; used to "
            "match physical items to database records.</li>"
            "<li><strong>Inventory database</strong> – records make, model, serial number, location, owner, "
            "purchase date, and warranty status.</li>"
            "<li><strong>Check-in / check-out</strong> – formal process for loaner devices or shared equipment.</li>"
            "</ul>"
            "<h3>Software Asset Management (SAM)</h3>"
            "<ul>"
            "<li>Track all licensed software: product keys, number of seats, expiration dates.</li>"
            "<li>Audit installed software against purchased licenses to avoid over-deployment or under-licensing.</li>"
            "<li>Maintain an approved software list to prevent unauthorized installations.</li>"
            "</ul>"
            "<h3>Lifecycle Phases</h3>"
            "<ol>"
            "<li><strong>Procurement</strong> – purchasing, receiving, and initial configuration.</li>"
            "<li><strong>Deployment</strong> – imaging, policy application, issuing to users.</li>"
            "<li><strong>Maintenance</strong> – patching, repairs, upgrades.</li>"
            "<li><strong>Disposal / EOL</strong> – data sanitization (wipe, degauss, shred) before recycling or "
            "donation; certificate of destruction for regulated data.</li>"
            "</ol>"
            "<h3>Disposal Regulations</h3>"
            "<ul>"
            "<li>Electronics must often be recycled through certified e-waste programs (e.g., R2, e-Stewards).</li>"
            "<li>Batteries, toner cartridges, and CRTs may have specific hazardous-waste requirements.</li>"
            "</ul>"
        ),
        "key_points": [
            "Asset tags (barcode/RFID) tie physical devices to database records.",
            "SAM audits prevent license compliance violations.",
            "The asset lifecycle ends with secure data sanitization before disposal.",
            "Certificates of destruction document proper disposal of devices holding regulated data.",
            "Approved software lists block unauthorized installs.",
        ],
    },
    {
        "domain": 4,
        "topic": "Change management",
        "objective": "4.1",
        "video": "Change Management",
        "study_topics": ["Change management"],
        "body": (
            "<p>Change management is a structured process for requesting, reviewing, approving, implementing, "
            "and documenting changes to IT systems. Its goal is to reduce risk and unplanned outages.</p>"
            "<h3>Change Management Workflow</h3>"
            "<ol>"
            "<li><strong>Change Request (CR)</strong> – requester submits a form describing the proposed change, "
            "reason, systems affected, and rollback plan.</li>"
            "<li><strong>Risk assessment</strong> – evaluate impact, likelihood of failure, and business risk.</li>"
            "<li><strong>Change Advisory Board (CAB)</strong> – committee reviews and approves/denies the CR.</li>"
            "<li><strong>Scheduling</strong> – changes are slotted into a maintenance window (typically off-peak).</li>"
            "<li><strong>Implementation</strong> – the change is applied following the documented procedure.</li>"
            "<li><strong>Verification</strong> – confirm the change achieved its goal and systems function correctly.</li>"
            "<li><strong>Documentation</strong> – update records; close the change ticket.</li>"
            "</ol>"
            "<h3>Key Concepts</h3>"
            "<ul>"
            "<li><strong>Rollback plan</strong> – documented steps to undo the change if something goes wrong.</li>"
            "<li><strong>Sandbox / test environment</strong> – validate changes before production.</li>"
            "<li><strong>Emergency change</strong> – expedited approval path for critical fixes (e.g., zero-day patch).</li>"
            "<li><strong>Standard change</strong> – pre-approved, low-risk, repetitive tasks (e.g., password reset).</li>"
            "</ul>"
            "<h3>Why It Matters for the Exam</h3>"
            "<p>The A+ exam may present a scenario where a system breaks after an undocumented change. The correct "
            "approach is always to follow the change management process, get approval, and document everything.</p>"
        ),
        "key_points": [
            "Every change starts with a Change Request that includes scope, risk, and a rollback plan.",
            "The CAB reviews and approves changes before implementation.",
            "Test changes in a sandbox before applying to production.",
            "Emergency changes use an expedited approval path but still require documentation.",
            "Always document what was done, when, by whom, and the outcome.",
        ],
    },
    {
        "domain": 4,
        "topic": "Backup types",
        "objective": "4.3",
        "video": "Backup and Recovery",
        "study_topics": ["Backup types"],
        "body": (
            "<p>Backups protect data from loss due to hardware failure, ransomware, accidental deletion, or "
            "disasters. Understanding the differences between backup types is critical for the exam.</p>"
            "<h3>Backup Type Comparison</h3>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Type</th><th>What is backed up</th><th>Backup speed</th><th>Restore speed</th>"
            "<th>Archive bit</th></tr>"
            "<tr><td><strong>Full</strong></td><td>All selected data</td><td>Slowest</td><td>Fastest (one set)</td>"
            "<td>Cleared</td></tr>"
            "<tr><td><strong>Incremental</strong></td><td>Data changed since the <em>last backup of any type</em></td>"
            "<td>Fastest</td><td>Slowest (need full + all incrementals)</td><td>Cleared</td></tr>"
            "<tr><td><strong>Differential</strong></td><td>Data changed since the <em>last full backup</em></td>"
            "<td>Medium (grows over time)</td><td>Fast (need full + latest differential)</td>"
            "<td>Not cleared</td></tr>"
            "<tr><td><strong>Synthetic full</strong></td><td>Created by merging a full + incrementals on the server</td>"
            "<td>No client impact</td><td>Same as full</td><td>N/A</td></tr>"
            "</table>"
            "<h3>Key Distinctions</h3>"
            "<ul>"
            "<li><strong>Incremental vs Differential</strong> — both back up changed data, but incremental resets "
            "the archive bit after each run (only new changes next time), while differential does not (keeps "
            "accumulating since the last full).</li>"
            "<li><strong>Restore complexity</strong> — incremental restores require the full backup plus every "
            "incremental in order; differential only needs the full plus the most recent differential.</li>"
            "</ul>"
            "<h3>Recovery Objectives</h3>"
            "<ul>"
            "<li><strong>RTO (Recovery Time Objective)</strong> – maximum acceptable downtime.</li>"
            "<li><strong>RPO (Recovery Point Objective)</strong> – maximum acceptable data loss (age of last backup).</li>"
            "</ul>"
        ),
        "key_points": [
            "Full backup: all data, slowest to back up, fastest single-set restore.",
            "Incremental: changes since last backup of ANY type; fast backup, slow restore (need full + all incrementals).",
            "Differential: changes since last FULL; slower backup over time, faster restore (full + latest diff).",
            "Synthetic full: created server-side by merging full + incrementals; no impact on production clients.",
            "RTO = max downtime allowed; RPO = max data loss allowed.",
        ],
    },
    {
        "domain": 4,
        "topic": "Backup rotation schemes and the 3-2-1 rule",
        "objective": "4.3",
        "video": "Backup and Recovery",
        "study_topics": ["Backup rotation (GFS/3-2-1)"],
        "body": (
            "<p>Backup rotation schemes define how backup media is reused over time to balance storage cost "
            "with recovery depth. Two key frameworks appear on the exam: GFS and the 3-2-1 rule.</p>"
            "<h3>Grandfather-Father-Son (GFS)</h3>"
            "<ul>"
            "<li><strong>Son (daily)</strong> – incremental or full backup taken each weekday; media is reused "
            "weekly. Provides recovery for individual days within the past week.</li>"
            "<li><strong>Father (weekly)</strong> – full backup taken at the end of each week (e.g., Friday). "
            "Retained for a month. Provides weekly recovery points.</li>"
            "<li><strong>Grandfather (monthly)</strong> – full backup taken at the end of each month. Often "
            "retained for a year or longer. Provides long-term recovery points.</li>"
            "</ul>"
            "<p>GFS minimizes the number of media sets needed while providing daily, weekly, and monthly "
            "restore points. Off-site storage is typically used for grandfather tapes.</p>"
            "<h3>The 3-2-1 Rule</h3>"
            "<ul>"
            "<li><strong>3</strong> copies of data (1 primary + 2 backups)</li>"
            "<li><strong>2</strong> different storage media types (e.g., local disk + tape or cloud)</li>"
            "<li><strong>1</strong> copy stored off-site (protects against site-level disasters like fire or flood)</li>"
            "</ul>"
            "<p>The 3-2-1 rule is media-agnostic and applies to any backup strategy. Off-site can be a physical "
            "location, a cloud backup service, or both.</p>"
            "<h3>Testing Backups</h3>"
            "<p>Backups must be regularly tested by performing restore drills. An untested backup may be corrupt "
            "or incomplete. Document each test with date, files restored, and success/failure outcome.</p>"
        ),
        "key_points": [
            "GFS uses daily (Son), weekly (Father), and monthly (Grandfather) sets to provide layered recovery points.",
            "3-2-1 rule: 3 copies, 2 media types, 1 off-site.",
            "Off-site storage protects against site-wide disasters.",
            "Test backups regularly with restore drills; an untested backup is an unreliable backup.",
            "GFS grandfather tapes are often stored off-site to satisfy the 3-2-1 rule.",
        ],
    },
    {
        "domain": 4,
        "topic": "Safety procedures and ESD",
        "objective": "4.4",
        "video": "Safety Procedures",
        "study_topics": ["Safety procedures (ESD)"],
        "body": (
            "<p>Electrostatic discharge (ESD) and physical safety hazards are addressed in Domain 4. "
            "Understanding protective measures is essential for working safely with computer hardware.</p>"
            "<h3>Electrostatic Discharge (ESD)</h3>"
            "<p>ESD can instantly destroy semiconductor components with a discharge invisible to the human eye. "
            "As little as 100 volts can damage a chip, far below the 3,000 V threshold for human sensation.</p>"
            "<ul>"
            "<li><strong>Anti-static wrist strap</strong> – worn on the wrist, clipped to chassis ground; bleeds "
            "off static continuously. Do NOT wear when working inside a CRT or power supply.</li>"
            "<li><strong>Anti-static mat</strong> – placed on workbench; components set on the mat are grounded.</li>"
            "<li><strong>Anti-static bags</strong> – metallic (Faraday cage) bags for transporting components; "
            "never set components ON TOP of a bag — only inside it.</li>"
            "<li><strong>Grounding</strong> – touch the metal chassis before handling components if a strap is "
            "unavailable.</li>"
            "<li><strong>Humidity</strong> – low humidity (below ~40%) increases static buildup; maintaining "
            "40–60% relative humidity reduces ESD risk.</li>"
            "</ul>"
            "<h3>Other Physical Safety Practices</h3>"
            "<ul>"
            "<li><strong>Lifting technique</strong> – lift with legs, not the back; use dollies for heavy equipment.</li>"
            "<li><strong>Cable management</strong> – secure cables to prevent trip hazards.</li>"
            "<li><strong>Power safety</strong> – always power off and unplug before internal work; use a UPS to "
            "protect equipment from power fluctuations.</li>"
            "<li><strong>Fire extinguisher types</strong> – Class C (electrical fires); never use water on "
            "electrical fires. Modern data centers use clean agent (FM-200) systems.</li>"
            "<li><strong>MSDS / SDS sheets</strong> – Material Safety Data Sheets for hazardous materials "
            "(toner, cleaning solvents).</li>"
            "</ul>"
        ),
        "key_points": [
            "ESD can damage components with discharges too small to feel (as low as 100 V).",
            "Anti-static wrist strap is clipped to chassis ground — do not wear near CRTs or PSUs.",
            "Store components inside anti-static bags, never on top of them.",
            "Maintain 40–60% relative humidity to reduce static buildup.",
            "Use Class C extinguisher on electrical fires; clean-agent systems in data centers.",
        ],
    },
    {
        "domain": 4,
        "topic": "Environmental controls",
        "objective": "4.4",
        "video": "Environmental Controls",
        "study_topics": ["Environmental controls"],
        "body": (
            "<p>Proper environmental controls ensure that hardware operates within safe temperature, humidity, "
            "and power parameters, reducing failure rates and extending equipment life.</p>"
            "<h3>Temperature and Cooling</h3>"
            "<ul>"
            "<li>Servers and network equipment generate significant heat; ASHRAE recommends inlet air temperature "
            "of 64–80 °F (18–27 °C) for data centers.</li>"
            "<li><strong>Hot aisle / cold aisle</strong> – racks are arranged so equipment intakes face cold "
            "aisles and exhausts face hot aisles, preventing hot exhaust from re-entering intakes.</li>"
            "<li><strong>CRAC units</strong> (Computer Room Air Conditioning) cool and dehumidify server rooms.</li>"
            "<li>Proper ventilation in wiring closets is critical; a sealed closet becomes an oven.</li>"
            "</ul>"
            "<h3>Humidity</h3>"
            "<ul>"
            "<li>Too low (&lt;40%) – increases ESD risk.</li>"
            "<li>Too high (&gt;60%) – risks condensation and corrosion on circuit boards.</li>"
            "<li>Target: 40–60% relative humidity for data center and server rooms.</li>"
            "</ul>"
            "<h3>Power Quality</h3>"
            "<ul>"
            "<li><strong>UPS (Uninterruptible Power Supply)</strong> – provides battery backup during outages and "
            "filters power irregularities (surges, sags, brownouts). Gives time for graceful shutdown.</li>"
            "<li><strong>Surge protector</strong> – protects against voltage spikes only; no battery backup.</li>"
            "<li><strong>Power strip</strong> – provides extra outlets but NO surge or battery protection.</li>"
            "<li><strong>Generator</strong> – provides long-term power during extended outages; UPS bridges the "
            "gap until the generator spins up.</li>"
            "</ul>"
            "<h3>Location Controls</h3>"
            "<ul>"
            "<li>Keep server rooms free of food, drinks, and unnecessary personnel.</li>"
            "<li>Use raised flooring in data centers for airflow and cable routing.</li>"
            "<li>Positive pressure rooms prevent dust and contaminants from entering.</li>"
            "</ul>"
        ),
        "key_points": [
            "Hot aisle / cold aisle layout prevents hot exhaust from recirculating into equipment intakes.",
            "Target 40–60% relative humidity to balance ESD and condensation risks.",
            "UPS provides battery backup AND power conditioning; a power strip does neither.",
            "A generator takes time to spin up; the UPS bridges that gap.",
            "CRAC units provide precision cooling and humidity control in server rooms.",
        ],
    },
    {
        "domain": 4,
        "topic": "Prohibited content, incident response, and chain of custody",
        "objective": "4.5",
        "video": "Incident Response",
        "study_topics": ["Prohibited content & incident response (chain of custody)"],
        "body": (
            "<p>When a technician discovers potentially illegal content or a security incident, a structured "
            "incident response process must be followed to preserve evidence and protect the organization.</p>"
            "<h3>Incident Response Steps (CompTIA Order)</h3>"
            "<ol>"
            "<li><strong>Identify</strong> – recognize that an incident has occurred (e.g., malware, prohibited "
            "content, data breach).</li>"
            "<li><strong>Report through proper channels</strong> – notify a supervisor or security team "
            "immediately; do not handle alone.</li>"
            "<li><strong>Preserve the evidence</strong> – do not power off, do not delete files, do not attempt "
            "your own investigation unless instructed.</li>"
            "<li><strong>Document</strong> – record what was observed, timestamps, and any actions taken.</li>"
            "<li><strong>Contain</strong> – isolate the affected system from the network to prevent spread.</li>"
            "<li><strong>Remediate</strong> – remove malware, restore from backup, apply patches.</li>"
            "<li><strong>Recover</strong> – return system to normal operation.</li>"
            "<li><strong>Lessons learned</strong> – post-incident review to improve future response.</li>"
            "</ol>"
            "<h3>Chain of Custody</h3>"
            "<ul>"
            "<li>Documents every person who handled the evidence, when, and what they did.</li>"
            "<li>Preserves admissibility of evidence in legal proceedings.</li>"
            "<li><strong>Make a forensic copy (image)</strong> of the drive before any analysis — work only on the "
            "copy, never the original.</li>"
            "<li>Use write blockers when imaging drives to prevent accidental modification.</li>"
            "<li>Store original evidence in a sealed, tamper-evident bag in a secure location.</li>"
            "<li>Log each transfer of evidence with signature, date, and purpose.</li>"
            "</ul>"
            "<h3>Prohibited Content</h3>"
            "<ul>"
            "<li>Illegal content (e.g., CSAM) must be reported to law enforcement; the technician must not "
            "investigate further.</li>"
            "<li>Company policy violations (pirated software, harassment) are reported to HR/management.</li>"
            "</ul>"
        ),
        "key_points": [
            "Do not power off or delete files when you discover potential evidence — preserve the scene.",
            "Report through proper channels; do not investigate prohibited content on your own.",
            "Chain of custody documents every person who touched the evidence and when.",
            "Always work from a forensic copy (image) of a drive, never the original.",
            "Use a write blocker during imaging to prevent altering the original evidence.",
        ],
    },
    {
        "domain": 4,
        "topic": "Licensing, regulated data, and compliance",
        "objective": "4.1",
        "video": "Licensing and Regulated Data",
        "study_topics": ["Licensing & regulated data (PII/PCI/GDPR/PHI)"],
        "body": (
            "<p>Technicians must understand software licensing models and how to handle regulated categories "
            "of data to keep organizations legally compliant.</p>"
            "<h3>Software Licensing Models</h3>"
            "<ul>"
            "<li><strong>EULA (End User License Agreement)</strong> – legal contract granting the right to use "
            "software under specific terms; must be accepted before installation.</li>"
            "<li><strong>Open-source</strong> – source code is freely available; licenses vary (MIT, GPL, Apache). "
            "GPL requires derivative works to also be open-source (copyleft).</li>"
            "<li><strong>Commercial / proprietary</strong> – software owned by a vendor; users purchase a license, "
            "not the software itself.</li>"
            "<li><strong>Personal license</strong> – single user on a limited number of devices.</li>"
            "<li><strong>Corporate / enterprise license</strong> – covers multiple users or devices within an "
            "organization; often a volume or site license.</li>"
            "<li><strong>Subscription</strong> – recurring payment model (e.g., Microsoft 365); access ends if "
            "subscription lapses.</li>"
            "<li><strong>Concurrent use</strong> – limits the number of simultaneous active users.</li>"
            "</ul>"
            "<h3>Regulated Data Categories</h3>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Acronym</th><th>Full name</th><th>Scope / Key requirement</th></tr>"
            "<tr><td><strong>PII</strong></td><td>Personally Identifiable Information</td>"
            "<td>Any data that can identify an individual (name, SSN, address, email). Must be protected and "
            "disclosed in breach notifications.</td></tr>"
            "<tr><td><strong>PCI DSS</strong></td><td>Payment Card Industry Data Security Standard</td>"
            "<td>Governs storage, transmission, and processing of credit card data. Mandatory for any entity "
            "handling card payments.</td></tr>"
            "<tr><td><strong>GDPR</strong></td><td>General Data Protection Regulation</td>"
            "<td>EU regulation protecting personal data of EU residents globally. Requires consent, right to "
            "erasure, and breach notification within 72 hours.</td></tr>"
            "<tr><td><strong>PHI</strong></td><td>Protected Health Information</td>"
            "<td>Health data covered by HIPAA (US). Strict rules on access, sharing, and storage of patient "
            "records.</td></tr>"
            "</table>"
            "<p>Mishandling regulated data can result in significant fines and legal liability. Technicians should "
            "minimize exposure to regulated data and report accidental access immediately.</p>"
        ),
        "key_points": [
            "An EULA licenses the use of software — users do not own the software itself.",
            "GPL (copyleft) requires derivative works to also be open-source.",
            "PII = any data that identifies an individual; PCI DSS governs card payment data.",
            "GDPR applies globally to data of EU residents; breach notification required within 72 hours.",
            "PHI is health information protected by HIPAA; access controls and audit logs are required.",
        ],
    },
    {
        "domain": 4,
        "topic": "Professionalism and communication",
        "objective": "4.6",
        "video": "Professionalism and Communication",
        "study_topics": ["Communication & professionalism"],
        "body": (
            "<p>CompTIA A+ tests not just technical skills but also the soft skills needed to interact "
            "effectively with users and colleagues. Domain 4 dedicates significant attention to professional "
            "behavior and communication.</p>"
            "<h3>Communication Best Practices</h3>"
            "<ul>"
            "<li><strong>Active listening</strong> – let the user finish; do not interrupt. Restate the problem "
            "to confirm understanding.</li>"
            "<li><strong>Use plain language</strong> – avoid technical jargon with non-technical users.</li>"
            "<li><strong>Set expectations</strong> – inform the user of what you are doing and when they can "
            "expect resolution.</li>"
            "<li><strong>Follow up</strong> – after resolving, check that the user is satisfied and the issue "
            "has not recurred.</li>"
            "</ul>"
            "<h3>Professional Behavior</h3>"
            "<ul>"
            "<li>Be on time for appointments; notify users if you will be late.</li>"
            "<li>Respect the user's workspace — avoid moving or using personal items without permission.</li>"
            "<li>Maintain a positive attitude even when dealing with difficult users.</li>"
            "<li>Do not disclose private information about users or the organization.</li>"
            "<li>Avoid personal calls, texting, or socializing while working on a user's problem.</li>"
            "<li>Dress appropriately for the work environment.</li>"
            "</ul>"
            "<h3>Handling Difficult Situations</h3>"
            "<ul>"
            "<li><strong>Angry users</strong> – stay calm, do not argue, do not take it personally. Acknowledge "
            "the frustration: 'I understand this is impacting your work.'</li>"
            "<li><strong>Multiple users</strong> – prioritize by impact/urgency; communicate triage decisions.</li>"
            "<li><strong>Cultural sensitivity</strong> – be respectful of cultural differences in communication "
            "styles and norms.</li>"
            "</ul>"
            "<h3>Ethical Conduct</h3>"
            "<ul>"
            "<li>Do not browse a user's personal data beyond what is necessary to resolve the issue.</li>"
            "<li>Report ethical violations (bribes, illegal requests) through proper channels.</li>"
            "</ul>"
        ),
        "key_points": [
            "Active listening means letting the user finish speaking before responding.",
            "Avoid technical jargon; use plain language with non-technical users.",
            "Stay calm with difficult users — acknowledge frustration, do not argue.",
            "Set clear expectations about timeline and follow up after resolution.",
            "Do not access user data beyond what is required to solve the reported problem.",
        ],
    },
    {
        "domain": 4,
        "topic": "Scripting basics",
        "objective": "4.8",
        "video": "Scripting Basics",
        "study_topics": ["Scripting basics"],
        "body": (
            "<p>Basic scripting knowledge helps technicians automate repetitive tasks, manage configurations, "
            "and understand scripts encountered in the field. The exam tests recognition of scripting "
            "environments and file types, not deep programming skill.</p>"
            "<h3>Common Script File Extensions</h3>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Extension</th><th>Language / Environment</th><th>Common Use</th></tr>"
            "<tr><td><strong>.bat</strong></td><td>Windows Batch (cmd.exe)</td>"
            "<td>Simple automation: copy files, map drives, run programs.</td></tr>"
            "<tr><td><strong>.ps1</strong></td><td>PowerShell (Windows)</td>"
            "<td>Advanced Windows automation: AD management, system config, security tasks.</td></tr>"
            "<tr><td><strong>.vbs</strong></td><td>VBScript (Windows Script Host)</td>"
            "<td>Legacy Windows automation; COM object interaction. Declining use.</td></tr>"
            "<tr><td><strong>.sh</strong></td><td>Bash / Shell (Linux/macOS)</td>"
            "<td>Linux/Unix automation: system admin, cron jobs, deployment scripts.</td></tr>"
            "<tr><td><strong>.py</strong></td><td>Python (cross-platform)</td>"
            "<td>Cross-platform scripting, data processing, network automation.</td></tr>"
            "<tr><td><strong>.js</strong></td><td>JavaScript (Node.js or browser)</td>"
            "<td>Web automation, server-side scripting with Node.js.</td></tr>"
            "</table>"
            "<h3>Key Scripting Concepts</h3>"
            "<ul>"
            "<li><strong>Variables</strong> – store values for reuse.</li>"
            "<li><strong>Loops</strong> – repeat actions (for, while).</li>"
            "<li><strong>Conditionals</strong> – branch logic (if/else).</li>"
            "<li><strong>Comments</strong> – document script purpose; different syntax per language "
            "(# in Python/Bash, REM in .bat, // in JS).</li>"
            "<li><strong>Environment variables</strong> – system-level values accessible to scripts "
            "(%TEMP%, $HOME, $PATH).</li>"
            "</ul>"
            "<h3>Security Considerations</h3>"
            "<ul>"
            "<li>Scripts can be used to spread malware — treat unsigned scripts with caution.</li>"
            "<li>PowerShell execution policy controls which scripts can run (Restricted, RemoteSigned, Unrestricted).</li>"
            "<li>Never run scripts from untrusted sources without reviewing the code.</li>"
            "</ul>"
        ),
        "key_points": [
            ".bat = Windows Batch; .ps1 = PowerShell; .vbs = VBScript (legacy Windows).",
            ".sh = Bash/Shell (Linux/macOS); .py = Python (cross-platform); .js = JavaScript.",
            "PowerShell execution policy restricts which scripts can run on Windows.",
            "Never run scripts from untrusted sources without reviewing the code first.",
            "Variables, loops, and conditionals are the building blocks of any script.",
        ],
    },
    {
        "domain": 4,
        "topic": "Remote access technologies",
        "objective": "4.7",
        "video": "Remote Access Technologies",
        "study_topics": ["Remote access technologies"],
        "body": (
            "<p>Remote access tools allow technicians to support users and manage systems without being "
            "physically present. The exam covers several remote access methods, each with distinct "
            "use cases and security considerations.</p>"
            "<h3>Common Remote Access Technologies</h3>"
            "<ul>"
            "<li><strong>RDP (Remote Desktop Protocol)</strong> – Microsoft protocol for full graphical desktop "
            "access over TCP port 3389. Used for Windows-to-Windows remote sessions. Strong encryption; "
            "restrict with Network Level Authentication (NLA) and firewall rules.</li>"
            "<li><strong>VPN (Virtual Private Network)</strong> – creates an encrypted tunnel between the "
            "remote client and the corporate network. Allows access to internal resources as if on-site. "
            "Types: SSL/TLS VPN (browser or client), IPSec VPN. Split tunneling routes only corporate traffic "
            "through the VPN.</li>"
            "<li><strong>VNC (Virtual Network Computing)</strong> – cross-platform screen-sharing protocol; "
            "shares the actual display (not a separate session like RDP). Uses RFB protocol; less secure by "
            "default — should run over an encrypted tunnel (SSH or VPN).</li>"
            "<li><strong>SSH (Secure Shell)</strong> – encrypted command-line access to Linux/Unix systems "
            "over TCP port 22. Replaces unencrypted Telnet (port 23). Supports key-based authentication "
            "for stronger security than passwords.</li>"
            "<li><strong>RMM (Remote Monitoring and Management)</strong> – agent-based tools used by MSPs to "
            "monitor, patch, and remotely control endpoints at scale (e.g., NinjaRMM, Kaseya, ConnectWise).</li>"
            "<li><strong>MSRA (Microsoft Remote Assistance)</strong> – allows a user to invite a technician to "
            "view or share their screen. Session is user-initiated and consent-based. Uses invitation files "
            "(.msrcincident) or Easy Connect.</li>"
            "</ul>"
            "<h3>Security Considerations</h3>"
            "<ul>"
            "<li>Always use encrypted protocols; avoid Telnet, unencrypted VNC, and FTP.</li>"
            "<li>Enable MFA for remote access solutions when possible.</li>"
            "<li>Limit RDP access with NLA and restrict port 3389 at the firewall.</li>"
            "<li>Log and audit remote sessions for accountability.</li>"
            "<li>Use least-privilege accounts for remote access; avoid connecting as Administrator.</li>"
            "</ul>"
        ),
        "key_points": [
            "RDP = Microsoft graphical remote desktop, TCP 3389; use NLA for added security.",
            "VPN creates an encrypted tunnel to the corporate network for remote users.",
            "VNC shares the physical display and is cross-platform but less secure; tunnel it over SSH or VPN.",
            "SSH (port 22) provides encrypted CLI access to Linux/Unix; prefer key-based auth over passwords.",
            "MSRA is user-initiated remote assistance built into Windows — consent-based.",
            "RMM tools provide agent-based monitoring and management at scale for MSPs.",
        ],
    },
]
