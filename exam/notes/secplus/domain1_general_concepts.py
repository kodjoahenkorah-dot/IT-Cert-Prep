"""
CompTIA Security+ (SY0-701) Domain 1: General Security Concepts
Study notes aligned to official exam objectives.
"""

NOTES = [
    {
        "domain": 1,
        "topic": "Security control categories and types",
        "objective": "1.1",
        "video": "Security Controls",
        "study_topics": [
            "Security control categories",
            "Security control categories and types",
            "Security control types",
        ],
        "body": (
            "<p>Security controls are safeguards or countermeasures used to reduce risk. "
            "They are classified by <strong>category</strong> (how they are implemented) "
            "and by <strong>type</strong> (what they accomplish).</p>"
            "<p><strong>Control Categories</strong></p>"
            "<ul>"
            "<li><strong>Technical (Logical)</strong> – Implemented through technology: "
            "firewalls, IDS/IPS, encryption, access control lists, MFA, antivirus.</li>"
            "<li><strong>Managerial (Administrative)</strong> – Policies, procedures, and "
            "governance: risk assessments, security policies, background checks, training.</li>"
            "<li><strong>Operational</strong> – Day-to-day people and process controls: "
            "security awareness training, incident response procedures, change management.</li>"
            "<li><strong>Physical</strong> – Controls you can touch: locks, fences, guards, "
            "cameras, badge readers, mantraps/airlocks.</li>"
            "</ul>"
            "<p><strong>Control Types</strong></p>"
            "<ul>"
            "<li><strong>Preventive</strong> – Stop an incident before it occurs "
            "(e.g., firewall, encryption, access control).</li>"
            "<li><strong>Deterrent</strong> – Discourage an attacker without blocking "
            "(e.g., warning banners, security cameras, security guards).</li>"
            "<li><strong>Detective</strong> – Identify and record an incident "
            "(e.g., IDS, audit logs, CCTV recording, motion sensors).</li>"
            "<li><strong>Corrective</strong> – Minimize damage and restore operations "
            "(e.g., backups, patch management, incident response).</li>"
            "<li><strong>Compensating</strong> – Alternative control when a primary "
            "control is not feasible (e.g., enhanced monitoring instead of patching "
            "a legacy system).</li>"
            "<li><strong>Directive</strong> – Specify behavior through policy or instruction "
            "(e.g., acceptable use policies, training requirements, compliance mandates).</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> A single control can span multiple types "
            "(e.g., a security camera is both deterrent and detective). "
            "Always consider context when mapping controls to types.</p>"
        ),
        "key_points": [
            "Four control categories: Technical, Managerial, Operational, Physical.",
            "Six control types: Preventive, Deterrent, Detective, Corrective, Compensating, Directive.",
            "Compensating controls are used when primary controls cannot be implemented.",
            "Directive controls guide behavior; deterrent controls discourage but do not block.",
            "One control can satisfy multiple types simultaneously.",
        ],
    },
    {
        "domain": 1,
        "topic": "CIA triad and non-repudiation",
        "objective": "1.2",
        "video": "Security Concepts",
        "study_topics": ["CIA triad and non-repudiation"],
        "body": (
            "<p>The <strong>CIA Triad</strong> is the foundational model of information security, "
            "describing three core objectives every security program must address.</p>"
            "<ul>"
            "<li><strong>Confidentiality</strong> – Ensure information is accessible only to "
            "authorized parties. Controls: encryption, access controls, data classification, "
            "need-to-know, steganography.</li>"
            "<li><strong>Integrity</strong> – Ensure information is accurate and has not been "
            "improperly altered. Controls: hashing (SHA-256), digital signatures, version "
            "control, checksums, write-protect mechanisms.</li>"
            "<li><strong>Availability</strong> – Ensure systems and data are accessible when "
            "needed by authorized users. Controls: redundancy, RAID, load balancing, UPS, "
            "backups, disaster recovery, DDoS protection.</li>"
            "</ul>"
            "<p><strong>Non-repudiation</strong> is often considered a fourth security goal. "
            "It ensures that a party cannot deny having sent or received a message or performed "
            "an action. Non-repudiation is achieved through:</p>"
            "<ul>"
            "<li><strong>Digital signatures</strong> – Bind a message to the sender's private key, "
            "proving origin and integrity (uses asymmetric cryptography).</li>"
            "<li><strong>Audit logs</strong> – Tamper-evident records that document actions taken.</li>"
            "<li><strong>Certificates</strong> – Trusted third-party verification of identity.</li>"
            "<li><strong>Video surveillance / timestamps</strong> – Physical non-repudiation evidence.</li>"
            "</ul>"
            "<p><strong>Common exam scenarios:</strong> An attacker intercepting data = confidentiality "
            "breach; modifying data in transit = integrity breach; a DDoS attack = availability breach; "
            "a user denying they sent an email = non-repudiation issue.</p>"
        ),
        "key_points": [
            "CIA stands for Confidentiality, Integrity, and Availability.",
            "Non-repudiation prevents denial of an action; implemented via digital signatures.",
            "Encryption primarily addresses confidentiality.",
            "Hashing and digital signatures address integrity.",
            "Redundancy and backups address availability.",
            "A DDoS attack targets availability; eavesdropping targets confidentiality.",
        ],
    },
    {
        "domain": 1,
        "topic": "AAA framework",
        "objective": "1.2",
        "video": "Authentication and Authorization",
        "study_topics": ["AAA framework"],
        "body": (
            "<p>The <strong>AAA framework</strong> defines how users gain access to systems "
            "and how that access is tracked. It stands for "
            "Authentication, Authorization, and Accounting (Auditing).</p>"
            "<p><strong>Authentication</strong> – Verifying <em>who</em> a user is. "
            "The five authentication factors are:</p>"
            "<ul>"
            "<li><strong>Something you know</strong> – Password, PIN, security question.</li>"
            "<li><strong>Something you have</strong> – Smart card, hardware token, OTP app.</li>"
            "<li><strong>Something you are</strong> – Biometrics (fingerprint, retina, face).</li>"
            "<li><strong>Somewhere you are</strong> – Geolocation, IP address.</li>"
            "<li><strong>Something you do</strong> – Behavioral biometrics (keystroke dynamics).</li>"
            "</ul>"
            "<p><strong>Multi-Factor Authentication (MFA)</strong> requires two or more different "
            "factor categories. Two passwords = NOT MFA.</p>"
            "<p><strong>Authorization</strong> – Determining <em>what</em> an authenticated user "
            "is permitted to do. Common models:</p>"
            "<ul>"
            "<li><strong>DAC</strong> (Discretionary) – Resource owner grants permissions.</li>"
            "<li><strong>MAC</strong> (Mandatory) – Labels and clearances enforced by policy.</li>"
            "<li><strong>RBAC</strong> (Role-Based) – Permissions tied to job roles.</li>"
            "<li><strong>ABAC</strong> (Attribute-Based) – Policies based on user/resource attributes.</li>"
            "</ul>"
            "<p><strong>Accounting / Auditing</strong> – Recording <em>what</em> an authenticated, "
            "authorized user did. Supports non-repudiation, forensics, and compliance. "
            "Key mechanisms: audit logs, SIEM, RADIUS/TACACS+ accounting records.</p>"
            "<p><strong>RADIUS vs TACACS+:</strong> RADIUS encrypts only the password and combines "
            "authentication/authorization; TACACS+ encrypts the full payload and separates AAA functions.</p>"
        ),
        "key_points": [
            "AAA = Authentication (who), Authorization (what), Accounting (when/what was done).",
            "MFA requires two factors from DIFFERENT categories.",
            "RADIUS uses UDP; TACACS+ uses TCP and encrypts the entire payload.",
            "Authorization models: DAC (owner-controlled), MAC (label-based), RBAC (role-based), ABAC (attribute-based).",
            "Accounting logs support non-repudiation and forensic investigations.",
        ],
    },
    {
        "domain": 1,
        "topic": "Gap analysis",
        "objective": "1.2",
        "video": "Security Governance",
        "study_topics": ["Gap analysis"],
        "body": (
            "<p>A <strong>gap analysis</strong> is a formal process that compares an organization's "
            "current security posture against a desired target state — typically defined by a "
            "framework, regulation, or internal policy — to identify deficiencies that must be remediated.</p>"
            "<p><strong>Common reference frameworks used in gap analysis:</strong></p>"
            "<ul>"
            "<li><strong>NIST Cybersecurity Framework (CSF)</strong> – Identify, Protect, Detect, "
            "Respond, Recover.</li>"
            "<li><strong>ISO/IEC 27001</strong> – International information security management standard.</li>"
            "<li><strong>PCI DSS</strong> – Payment card industry data security standard.</li>"
            "<li><strong>HIPAA Security Rule</strong> – Healthcare data protection requirements.</li>"
            "<li><strong>CIS Controls</strong> – Prioritized set of cybersecurity best practices.</li>"
            "</ul>"
            "<p><strong>Gap analysis steps:</strong></p>"
            "<ol>"
            "<li>Define the <strong>baseline/target state</strong> (which framework or regulation).</li>"
            "<li>Assess the <strong>current state</strong> by reviewing policies, controls, and processes.</li>"
            "<li>Identify <strong>gaps</strong> — areas where current controls fall short.</li>"
            "<li>Prioritize gaps by <strong>risk level</strong> and business impact.</li>"
            "<li>Develop a <strong>remediation roadmap</strong> with milestones and ownership.</li>"
            "</ol>"
            "<p><strong>Outputs:</strong> A written report documenting gaps, risk ratings, recommended "
            "controls, timelines, and responsible parties. Often fed into a risk register or "
            "treatment plan.</p>"
            "<p><strong>Exam tip:</strong> Gap analysis is a prerequisite to effective security planning "
            "and is commonly triggered by regulatory audits, mergers, or adoption of a new framework.</p>"
        ),
        "key_points": [
            "Gap analysis compares current security posture to a target/desired state.",
            "Common frameworks used: NIST CSF, ISO 27001, PCI DSS, HIPAA, CIS Controls.",
            "Output is a remediation roadmap prioritized by risk.",
            "Gap analysis feeds into the risk register and treatment plan.",
            "Often triggered by compliance audits, new regulations, or framework adoption.",
        ],
    },
    {
        "domain": 1,
        "topic": "Zero Trust architecture",
        "objective": "1.2",
        "video": "Zero Trust",
        "study_topics": ["Zero Trust architecture"],
        "body": (
            "<p><strong>Zero Trust</strong> is a security model based on the principle "
            "<em>'never trust, always verify.'</em> It abandons the concept of a trusted "
            "internal network perimeter and requires continuous verification of every user, "
            "device, and application regardless of location.</p>"
            "<p><strong>Core Zero Trust principles:</strong></p>"
            "<ul>"
            "<li>Verify explicitly — always authenticate and authorize based on all available data points.</li>"
            "<li>Use least-privilege access — limit user rights to the minimum necessary.</li>"
            "<li>Assume breach — minimize blast radius, segment access, encrypt everything.</li>"
            "</ul>"
            "<p><strong>Zero Trust architecture components (NIST SP 800-207):</strong></p>"
            "<p><em>Control Plane</em> — makes access decisions:</p>"
            "<ul>"
            "<li><strong>Policy Engine (PE)</strong> – Evaluates access requests against policy "
            "and grants/denies access. Uses identity, device health, threat intel, and context.</li>"
            "<li><strong>Policy Administrator (PA)</strong> – Translates the policy engine's "
            "decision into instructions; establishes or terminates communication paths.</li>"
            "</ul>"
            "<p><em>Data Plane</em> — enforces decisions:</p>"
            "<ul>"
            "<li><strong>Policy Enforcement Point (PEP)</strong> – The gateway that allows or "
            "blocks actual traffic based on instructions from the PA. Acts as the gatekeeper "
            "between subjects and resources.</li>"
            "</ul>"
            "<p><strong>Implicit trust zones</strong> are eliminated in Zero Trust — no network "
            "segment is trusted by default. Micro-segmentation, software-defined perimeters (SDP), "
            "and identity-aware proxies are common implementation technologies.</p>"
            "<p><strong>Exam tip:</strong> Know the PE/PA/PEP roles and that Zero Trust applies "
            "equally to internal and external traffic.</p>"
        ),
        "key_points": [
            "Zero Trust: 'Never trust, always verify' — no implicit trust for any network segment.",
            "Control plane: Policy Engine (decides) + Policy Administrator (communicates decisions).",
            "Data plane: Policy Enforcement Point (PEP) enforces access decisions.",
            "Core principles: verify explicitly, least-privilege, assume breach.",
            "Micro-segmentation and identity-aware proxies are key Zero Trust technologies.",
            "Based on NIST SP 800-207.",
        ],
    },
    {
        "domain": 1,
        "topic": "Physical security",
        "objective": "1.2",
        "video": "Physical Security",
        "study_topics": ["Physical security"],
        "body": (
            "<p><strong>Physical security</strong> protects hardware, facilities, personnel, "
            "and physical assets from unauthorized access, damage, or disruption. "
            "It is the first line of defense — no logical control compensates for poor physical security.</p>"
            "<p><strong>Perimeter controls:</strong></p>"
            "<ul>"
            "<li><strong>Fencing and bollards</strong> – Deter and delay vehicle/pedestrian access.</li>"
            "<li><strong>Lighting</strong> – Deters criminal activity and supports CCTV effectiveness.</li>"
            "<li><strong>Guards and receptionists</strong> – Authenticate visitors and enforce policy.</li>"
            "<li><strong>Signage</strong> – Warns of monitoring and legal consequences (deterrent).</li>"
            "</ul>"
            "<p><strong>Entry controls:</strong></p>"
            "<ul>"
            "<li><strong>Badge/proximity readers</strong> – RFID/smart card authentication.</li>"
            "<li><strong>Mantraps (access control vestibules)</strong> – Two-door airlock preventing "
            "tailgating; one door must close before the other opens.</li>"
            "<li><strong>Biometric scanners</strong> – Fingerprint, retina, facial recognition at "
            "high-security access points.</li>"
            "<li><strong>Key management</strong> – Locked key cabinets and key logs.</li>"
            "</ul>"
            "<p><strong>Surveillance and monitoring:</strong></p>"
            "<ul>"
            "<li><strong>CCTV / IP cameras</strong> – Continuous or motion-triggered recording; "
            "placement at entry/exit points, server rooms.</li>"
            "<li><strong>Motion sensors</strong> – PIR sensors, ultrasonic, microwave detection.</li>"
            "<li><strong>Alarms</strong> – Intrusion detection tied to monitoring services.</li>"
            "</ul>"
            "<p><strong>Data center considerations:</strong> "
            "Locate server rooms away from exterior walls; use raised flooring, hot/cold aisles; "
            "restrict with two-factor physical access (badge + PIN or biometric). "
            "Secure hardware disposal (degaussing, shredding) prevents data remanence.</p>"
        ),
        "key_points": [
            "Mantraps (access control vestibules) prevent tailgating with two sequential doors.",
            "Defense-in-depth layers: perimeter fencing → entry controls → interior monitoring → server room.",
            "CCTV is both a deterrent and a detective control.",
            "Biometric scanners provide strong authentication for high-security areas.",
            "Physical security failures often bypass all logical/technical controls.",
            "Data remanence requires secure disposal: degaussing or physical destruction.",
        ],
    },
    {
        "domain": 1,
        "topic": "Deception and disruption technologies",
        "objective": "1.2",
        "video": "Deception and Disruption",
        "study_topics": ["Deception and disruption technologies"],
        "body": (
            "<p><strong>Deception technologies</strong> lure attackers into interacting with "
            "fake resources, revealing attacker presence and tactics without exposing real assets.</p>"
            "<p><strong>Key deception technologies:</strong></p>"
            "<ul>"
            "<li><strong>Honeypot</strong> – A single decoy system that mimics a real server "
            "(e.g., a fake database) to attract attackers and log their activity. "
            "Low-interaction honeypots emulate services; high-interaction honeypots run real OS/services.</li>"
            "<li><strong>Honeynet</strong> – A network of honeypots forming a realistic fake environment, "
            "allowing observation of attacker lateral movement and TTPs.</li>"
            "<li><strong>Honeyfile</strong> – A fake file (e.g., <code>passwords.txt</code>) placed in "
            "a monitored location; access triggers an alert indicating insider threat or compromise.</li>"
            "<li><strong>Honeytoken</strong> – Fake credentials, API keys, or data records embedded in "
            "systems; if used, they immediately signal a breach.</li>"
            "<li><strong>DNS sinkhole</strong> – Redirects malicious domain lookups to a controlled "
            "server, blocking malware C2 communication and identifying infected hosts.</li>"
            "</ul>"
            "<p><strong>Disruption technologies</strong> actively interfere with attacker operations:</p>"
            "<ul>"
            "<li><strong>Tarpits</strong> – Slow down attackers or automated scanners by introducing "
            "artificial delays in connections.</li>"
            "<li><strong>Bogons / darknets</strong> – Monitor unused IP space; unexpected traffic "
            "reveals scanning or worm propagation.</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> Honeyfiles and honeytokens are especially useful for detecting "
            "insider threats. DNS sinkholes are a reactive control used during incident response.</p>"
        ),
        "key_points": [
            "Honeypot = single decoy system; honeynet = network of honeypots.",
            "Honeyfile = fake file that triggers alerts when accessed.",
            "Honeytoken = fake credentials or data embedded to detect misuse.",
            "DNS sinkhole blocks C2 communication and identifies infected hosts.",
            "Deception technologies are detective controls — they reveal attacker activity.",
            "Tarpits slow down automated scanning and attacks.",
        ],
    },
    {
        "domain": 1,
        "topic": "Change management",
        "objective": "1.3",
        "video": "Change Management",
        "study_topics": ["Change management"],
        "body": (
            "<p><strong>Change management</strong> is a formal process ensuring that changes to "
            "IT systems are properly planned, tested, approved, and documented to minimize risk "
            "and unintended consequences.</p>"
            "<p><strong>Change management process steps:</strong></p>"
            "<ol>"
            "<li><strong>Request for Change (RFC)</strong> – Document the proposed change, reason, "
            "and scope.</li>"
            "<li><strong>Impact analysis</strong> – Assess technical, business, and security risks.</li>"
            "<li><strong>Approval</strong> – Change Advisory Board (CAB) or designated authority reviews.</li>"
            "<li><strong>Testing</strong> – Validate in a non-production (staging) environment.</li>"
            "<li><strong>Scheduling</strong> – Change window (often during maintenance windows to "
            "minimize user impact).</li>"
            "<li><strong>Implementation</strong> – Carry out the change with a rollback plan ready.</li>"
            "<li><strong>Documentation</strong> – Update configuration management databases (CMDB), "
            "procedures, and records.</li>"
            "<li><strong>Post-change review</strong> – Verify success; close or escalate the RFC.</li>"
            "</ol>"
            "<p><strong>Key change types:</strong></p>"
            "<ul>"
            "<li><strong>Standard change</strong> – Pre-approved, low-risk, routine (e.g., password reset).</li>"
            "<li><strong>Normal change</strong> – Goes through full CAB approval process.</li>"
            "<li><strong>Emergency change</strong> – Expedited approval for critical incidents "
            "(retrospective review required).</li>"
            "</ul>"
            "<p><strong>Security considerations:</strong> Unauthorized changes are a primary source of "
            "outages and security incidents. Version control, backout plans, and separation of duties "
            "(developer cannot deploy to production) are essential. Change management also supports "
            "compliance and audit evidence.</p>"
        ),
        "key_points": [
            "RFC → Impact analysis → CAB approval → Testing → Scheduling → Implementation → Documentation → Review.",
            "CAB (Change Advisory Board) approves normal changes.",
            "Emergency changes require expedited approval and retrospective review.",
            "Separation of duties: developers should not push changes directly to production.",
            "Backout/rollback plans are mandatory before implementing changes.",
            "CMDB (Configuration Management Database) must be updated after every change.",
        ],
    },
    {
        "domain": 1,
        "topic": "Certificates",
        "objective": "1.4",
        "video": "Public Key Infrastructure",
        "study_topics": ["Certificates"],
        "body": (
            "<p>A <strong>digital certificate</strong> binds a public key to an identity and is "
            "issued by a trusted <strong>Certificate Authority (CA)</strong>. Certificates underpin "
            "TLS/SSL, code signing, S/MIME email, and VPN authentication.</p>"
            "<p><strong>PKI components:</strong></p>"
            "<ul>"
            "<li><strong>Certificate Authority (CA)</strong> – Issues and signs certificates. "
            "Root CAs are offline; Intermediate/Subordinate CAs issue end-entity certificates.</li>"
            "<li><strong>Registration Authority (RA)</strong> – Verifies requestor identity before "
            "the CA issues a certificate.</li>"
            "<li><strong>Certificate Signing Request (CSR)</strong> – Generated by the requestor; "
            "contains the public key and identity info submitted to the CA for signing.</li>"
            "<li><strong>Certificate Revocation List (CRL)</strong> – Periodically published list "
            "of revoked certificate serial numbers.</li>"
            "<li><strong>OCSP (Online Certificate Status Protocol)</strong> – Real-time certificate "
            "status check; more efficient than downloading a full CRL. "
            "OCSP Stapling allows the server to cache the OCSP response.</li>"
            "</ul>"
            "<p><strong>Certificate types:</strong></p>"
            "<ul>"
            "<li><strong>Wildcard certificate</strong> – Secures a domain and all its first-level "
            "subdomains (e.g., <code>*.example.com</code>). Cannot cover sub-subdomains.</li>"
            "<li><strong>SAN (Subject Alternative Name)</strong> – Secures multiple distinct "
            "hostnames in a single certificate (e.g., <code>example.com</code>, "
            "<code>mail.example.com</code>, <code>example.org</code>).</li>"
            "<li><strong>Self-signed certificate</strong> – Signed by the same entity that issued it; "
            "not trusted by browsers by default; used in internal/test environments.</li>"
            "<li><strong>DV / OV / EV</strong> – Domain Validated (domain ownership only), "
            "Organization Validated (org identity), Extended Validation (rigorous legal verification).</li>"
            "</ul>"
            "<p><strong>Certificate pinning</strong> hard-codes a certificate or public key into an "
            "application to prevent MITM attacks using fraudulent certificates.</p>"
        ),
        "key_points": [
            "CSR is generated by the requester and submitted to the CA for signing.",
            "CRL is a periodically published revocation list; OCSP provides real-time status.",
            "OCSP Stapling lets the server cache and serve the OCSP response for performance.",
            "Wildcard cert (*.example.com) covers one level of subdomains only.",
            "SAN certificates support multiple distinct hostnames in one cert.",
            "Root CAs are kept offline; intermediate CAs issue end-entity certificates.",
            "Certificate pinning prevents MITM attacks by hard-coding expected certificates.",
        ],
    },
    {
        "domain": 1,
        "topic": "Cryptographic hardware and key-management tools",
        "objective": "1.4",
        "video": "Cryptographic Hardware",
        "study_topics": [
            "Cryptographic hardware",
            "Cryptographic hardware and key-management tools",
        ],
        "body": (
            "<p>Dedicated cryptographic hardware provides tamper-resistant environments for "
            "key generation, storage, and cryptographic operations, preventing key exposure "
            "even to privileged OS users.</p>"
            "<p><strong>Trusted Platform Module (TPM)</strong></p>"
            "<ul>"
            "<li>A chip soldered to the motherboard providing hardware-based cryptographic functions.</li>"
            "<li>Stores cryptographic keys, certificates, passwords, and platform measurements.</li>"
            "<li>Supports secure boot (measures boot components and detects tampering), "
            "full-disk encryption key storage (BitLocker), and device attestation.</li>"
            "<li>Version 2.0 is the current standard; required for Windows 11.</li>"
            "</ul>"
            "<p><strong>Hardware Security Module (HSM)</strong></p>"
            "<ul>"
            "<li>A dedicated, tamper-evident hardware appliance (or PCIe card) for high-volume "
            "cryptographic operations and secure key storage.</li>"
            "<li>Used by CAs to protect root/signing keys, and by enterprises for PKI, TLS "
            "offloading, code signing, and database encryption.</li>"
            "<li>FIPS 140-2/3 Level 3+ validated — physically tamper-resistant and responsive.</li>"
            "</ul>"
            "<p><strong>Key Management System (KMS)</strong></p>"
            "<ul>"
            "<li>Software or cloud service (e.g., AWS KMS, Azure Key Vault) that manages "
            "cryptographic key lifecycle: creation, storage, rotation, distribution, and destruction.</li>"
            "<li>Enforces separation of duties — key custodians vs. key users.</li>"
            "<li>Supports key rotation policies and audit logging of all key operations.</li>"
            "</ul>"
            "<p><strong>Secure Enclave</strong></p>"
            "<ul>"
            "<li>An isolated execution environment within a processor (e.g., Apple Secure Enclave, "
            "Intel SGX, ARM TrustZone) that protects sensitive data and cryptographic operations "
            "from the main OS and applications.</li>"
            "<li>Used for biometric data storage, payment credentials, and device unlock keys.</li>"
            "</ul>"
        ),
        "key_points": [
            "TPM is soldered to the motherboard; stores keys and supports secure boot and BitLocker.",
            "HSM is a dedicated hardware appliance for high-assurance key storage and crypto operations.",
            "HSM is FIPS 140-2/3 Level 3+ validated (tamper-resistant and tamper-responsive).",
            "KMS manages key lifecycle: creation, rotation, distribution, and destruction.",
            "Secure Enclave isolates sensitive operations from the main OS (Apple, Intel SGX, ARM TrustZone).",
            "HSMs are used by CAs to protect root signing keys.",
        ],
    },
    {
        "domain": 1,
        "topic": "Hashing and salting",
        "objective": "1.4",
        "video": "Hashing and Digital Signatures",
        "study_topics": ["Hashing and salting"],
        "body": (
            "<p><strong>Hashing</strong> is a one-way cryptographic function that produces a "
            "fixed-length digest (hash value) from arbitrary input. The same input always "
            "produces the same output, but the process is computationally irreversible.</p>"
            "<p><strong>Properties of a secure hash function:</strong></p>"
            "<ul>"
            "<li><strong>Pre-image resistance</strong> – Cannot reverse the hash to find the input.</li>"
            "<li><strong>Second pre-image resistance</strong> – Cannot find a different input with "
            "the same hash.</li>"
            "<li><strong>Collision resistance</strong> – Cannot find any two inputs with the same hash.</li>"
            "</ul>"
            "<p><strong>Common hash algorithms:</strong></p>"
            "<table>"
            "<tr><th>Algorithm</th><th>Output Size</th><th>Status</th></tr>"
            "<tr><td>MD5</td><td>128-bit</td><td>Broken — collision attacks possible; avoid for security</td></tr>"
            "<tr><td>SHA-1</td><td>160-bit</td><td>Deprecated — collision demonstrated (SHAttered 2017)</td></tr>"
            "<tr><td>SHA-256 (SHA-2)</td><td>256-bit</td><td>Current standard; widely used</td></tr>"
            "<tr><td>SHA-3</td><td>Variable</td><td>NIST standard; Keccak algorithm, different design</td></tr>"
            "<tr><td>RIPEMD-160</td><td>160-bit</td><td>Used in Bitcoin addresses</td></tr>"
            "</table>"
            "<p><strong>Salting</strong> adds a random, unique value (the salt) to each password "
            "before hashing. This ensures that identical passwords produce different hash values, "
            "defeating rainbow table and dictionary attacks.</p>"
            "<p><strong>Password hashing best practices:</strong> Use purpose-built algorithms "
            "such as <strong>bcrypt</strong>, <strong>scrypt</strong>, or <strong>Argon2</strong> "
            "(winner of the Password Hashing Competition). These are intentionally slow and "
            "memory-hard, making brute-force attacks impractical.</p>"
            "<p><strong>HMAC (Hash-based Message Authentication Code)</strong> combines a secret "
            "key with a hash to provide both integrity and authentication of a message.</p>"
        ),
        "key_points": [
            "Hashing is one-way; it provides integrity, not confidentiality.",
            "MD5 and SHA-1 are considered broken/deprecated for security use.",
            "SHA-256 is the current recommended standard hash algorithm.",
            "Salting defeats rainbow table and dictionary attacks against stored passwords.",
            "bcrypt, scrypt, and Argon2 are recommended for password hashing (slow by design).",
            "HMAC uses a secret key + hash to provide message integrity AND authentication.",
        ],
    },
    {
        "domain": 1,
        "topic": "Symmetric vs asymmetric encryption",
        "objective": "1.4",
        "video": "Symmetric and Asymmetric Encryption",
        "study_topics": ["Symmetric vs asymmetric encryption"],
        "body": (
            "<p>Encryption transforms plaintext into ciphertext to protect confidentiality. "
            "The two fundamental paradigms differ in how keys are used.</p>"
            "<p><strong>Symmetric Encryption</strong></p>"
            "<ul>"
            "<li>Uses a <strong>single shared key</strong> for both encryption and decryption.</li>"
            "<li><strong>Advantages:</strong> Very fast; suitable for bulk data encryption.</li>"
            "<li><strong>Disadvantages:</strong> Key distribution problem — how to securely share "
            "the key? Scales poorly: n parties need n(n-1)/2 key pairs.</li>"
            "<li><strong>Algorithms:</strong> AES (128/192/256-bit, current standard), "
            "3DES (deprecated), ChaCha20, Blowfish.</li>"
            "<li><strong>AES modes:</strong> ECB (insecure), CBC (needs IV), CTR (stream mode), "
            "GCM (authenticated encryption — provides confidentiality AND integrity).</li>"
            "</ul>"
            "<p><strong>Asymmetric Encryption</strong></p>"
            "<ul>"
            "<li>Uses a <strong>key pair</strong>: public key (shareable) and private key (secret).</li>"
            "<li><strong>Encrypt with public key → decrypt with private key</strong> (confidentiality).</li>"
            "<li><strong>Sign with private key → verify with public key</strong> (non-repudiation/integrity).</li>"
            "<li><strong>Advantages:</strong> Solves the key distribution problem; enables digital "
            "signatures and PKI.</li>"
            "<li><strong>Disadvantages:</strong> Computationally expensive; not used for bulk data.</li>"
            "<li><strong>Algorithms:</strong> RSA (2048-bit minimum), ECC (smaller keys, "
            "equivalent strength — ECDSA, ECDH), Diffie-Hellman (key exchange).</li>"
            "</ul>"
            "<p><strong>Hybrid encryption</strong> combines both: asymmetric crypto exchanges a "
            "symmetric session key, which then encrypts bulk data. This is how TLS works.</p>"
            "<p><strong>Key lengths:</strong> AES-128 is considered secure; RSA-2048 ≈ AES-112 strength; "
            "ECC-256 ≈ RSA-3072 strength.</p>"
        ),
        "key_points": [
            "Symmetric = single shared key; fast; used for bulk data encryption.",
            "Asymmetric = key pair (public + private); solves key distribution; used for key exchange and signatures.",
            "AES is the standard symmetric algorithm; RSA and ECC are standard asymmetric algorithms.",
            "AES-GCM provides both confidentiality and integrity (authenticated encryption).",
            "TLS uses hybrid encryption: RSA/ECC for key exchange, AES for bulk data.",
            "Encrypt with recipient's public key; sign with your own private key.",
            "ECC provides equivalent security to RSA with smaller key sizes.",
        ],
    },
    {
        "domain": 1,
        "topic": "Obfuscation techniques",
        "objective": "1.4",
        "video": "Obfuscation",
        "study_topics": ["Obfuscation techniques"],
        "body": (
            "<p><strong>Obfuscation</strong> makes data or code harder to understand or interpret "
            "without necessarily encrypting it. It reduces clarity of information to impede analysis "
            "by unauthorized parties.</p>"
            "<p><strong>Steganography</strong></p>"
            "<ul>"
            "<li>Hides a secret message <em>within</em> an innocuous carrier file "
            "(image, audio, video, text) so that the existence of the message is concealed.</li>"
            "<li>Uses techniques such as least-significant-bit (LSB) substitution in images.</li>"
            "<li>Used by attackers to exfiltrate data hidden in images, and by security researchers "
            "for digital watermarking.</li>"
            "<li>Combines with encryption for layered protection: encrypt, then hide.</li>"
            "</ul>"
            "<p><strong>Tokenization</strong></p>"
            "<ul>"
            "<li>Replaces sensitive data (e.g., a credit card number) with a non-sensitive "
            "<strong>token</strong> stored in a mapping table (token vault).</li>"
            "<li>The original data never leaves the secure vault; the token is useless to attackers.</li>"
            "<li>Used extensively in PCI DSS compliance to protect cardholder data.</li>"
            "<li>Unlike encryption, tokenization is not mathematically reversible without vault access.</li>"
            "</ul>"
            "<p><strong>Data Masking</strong></p>"
            "<ul>"
            "<li>Replaces real data with realistic but fictitious data for use in non-production "
            "environments (dev, testing, analytics).</li>"
            "<li>Static masking: creates a permanent masked copy of the database.</li>"
            "<li>Dynamic masking: masks data on-the-fly at query time based on user role.</li>"
            "</ul>"
            "<p><strong>Code obfuscation</strong></p>"
            "<ul>"
            "<li>Transforms source or compiled code to make reverse engineering difficult "
            "(variable renaming, control flow flattening, dead code insertion).</li>"
            "<li>Used by malware authors and by legitimate developers to protect IP.</li>"
            "</ul>"
        ),
        "key_points": [
            "Steganography hides the existence of a message within a carrier file.",
            "Tokenization replaces sensitive data with a token; original stays in a secure vault.",
            "Tokenization is used in PCI DSS to protect cardholder data.",
            "Data masking creates realistic fake data for dev/test environments.",
            "Dynamic masking shows different data based on user role at query time.",
            "Obfuscation ≠ encryption; it reduces clarity but may not provide strong confidentiality.",
        ],
    },
    {
        "domain": 1,
        "topic": "Blockchain and open public ledger",
        "objective": "1.4",
        "video": "Blockchain",
        "study_topics": ["Blockchain and open public ledger"],
        "body": (
            "<p>A <strong>blockchain</strong> is a distributed, append-only ledger that records "
            "transactions in cryptographically linked blocks. Once data is written, it is "
            "computationally infeasible to alter without detection.</p>"
            "<p><strong>How blockchain works:</strong></p>"
            "<ol>"
            "<li>Transactions are grouped into a <strong>block</strong>.</li>"
            "<li>Each block contains a <strong>cryptographic hash of the previous block</strong>, "
            "creating a chain. Changing any block invalidates all subsequent blocks.</li>"
            "<li>Blocks are distributed across a <strong>peer-to-peer network</strong> of nodes "
            "— no single point of control or failure.</li>"
            "<li><strong>Consensus mechanisms</strong> (Proof of Work, Proof of Stake) ensure "
            "all nodes agree on the valid chain.</li>"
            "</ol>"
            "<p><strong>Security properties:</strong></p>"
            "<ul>"
            "<li><strong>Integrity</strong> – Hash chaining makes tampering detectable.</li>"
            "<li><strong>Non-repudiation</strong> – Transactions are signed with private keys.</li>"
            "<li><strong>Availability/Resilience</strong> – Decentralized; no single point of failure.</li>"
            "<li><strong>Transparency</strong> – Public blockchains are openly auditable by anyone.</li>"
            "</ul>"
            "<p><strong>Open public ledger</strong> — a blockchain that anyone can read and verify "
            "(e.g., Bitcoin, Ethereum). All transactions are visible, providing full auditability.</p>"
            "<p><strong>Security use cases:</strong></p>"
            "<ul>"
            "<li>Certificate transparency logs — publicly audit issued TLS certificates.</li>"
            "<li>Supply chain provenance — track authenticity of components.</li>"
            "<li>Voting and record integrity — tamper-evident audit trails.</li>"
            "<li>Smart contracts — self-executing code on the blockchain.</li>"
            "</ul>"
            "<p><strong>Limitations:</strong> Immutability means errors cannot be corrected; "
            "51% attacks on small networks; scalability challenges.</p>"
        ),
        "key_points": [
            "Blockchain is an append-only, distributed ledger secured by hash chaining.",
            "Each block contains the hash of the previous block — altering one block breaks all following blocks.",
            "Provides integrity, non-repudiation, and resilience through decentralization.",
            "Public/open ledgers are transparent and auditable by anyone.",
            "Certificate transparency logs use blockchain-like structures to audit TLS certificates.",
            "Smart contracts are self-executing code stored on the blockchain.",
        ],
    },
    {
        "domain": 1,
        "topic": "Attack type identification",
        "objective": "1.2",
        "video": "Attack Frameworks",
        "study_topics": ["Attack type identification"],
        "body": (
            "<p>Identifying attack types is foundational to security analysis, incident response, "
            "and threat modeling. The SY0-701 exam tests recognition of attack categories and "
            "specific techniques.</p>"
            "<p><strong>Social Engineering attacks:</strong></p>"
            "<ul>"
            "<li><strong>Phishing</strong> – Mass fraudulent email to steal credentials or deliver malware.</li>"
            "<li><strong>Spear phishing</strong> – Targeted phishing against a specific individual or org.</li>"
            "<li><strong>Whaling</strong> – Spear phishing targeting executives (high-value targets).</li>"
            "<li><strong>Vishing</strong> – Voice/phone-based social engineering.</li>"
            "<li><strong>Smishing</strong> – SMS-based phishing.</li>"
            "<li><strong>Pretexting</strong> – Fabricated scenario to manipulate a victim.</li>"
            "<li><strong>Tailgating/Piggybacking</strong> – Following authorized personnel through "
            "a secure door without authenticating.</li>"
            "</ul>"
            "<p><strong>Network-based attacks:</strong></p>"
            "<ul>"
            "<li><strong>DDoS</strong> – Flooding a service with traffic to deny availability.</li>"
            "<li><strong>Man-in-the-Middle (MitM)</strong> – Intercepting communication between parties.</li>"
            "<li><strong>ARP poisoning</strong> – Sending fake ARP replies to redirect LAN traffic.</li>"
            "<li><strong>DNS poisoning</strong> – Inserting false DNS records to redirect users.</li>"
            "<li><strong>VLAN hopping</strong> – Exploiting 802.1Q to access other VLANs.</li>"
            "</ul>"
            "<p><strong>Application attacks:</strong></p>"
            "<ul>"
            "<li><strong>SQL injection</strong> – Injecting SQL code into input fields.</li>"
            "<li><strong>XSS (Cross-Site Scripting)</strong> – Injecting client-side scripts into web pages.</li>"
            "<li><strong>CSRF (Cross-Site Request Forgery)</strong> – Tricks authenticated users into "
            "submitting malicious requests.</li>"
            "<li><strong>Buffer overflow</strong> – Writing data beyond a buffer's bounds to overwrite memory.</li>"
            "<li><strong>Directory traversal</strong> – Using <code>../</code> sequences to access "
            "files outside the web root.</li>"
            "</ul>"
            "<p><strong>Cryptographic attacks:</strong></p>"
            "<ul>"
            "<li><strong>Brute force</strong> – Trying all possible keys or passwords.</li>"
            "<li><strong>Rainbow table</strong> – Pre-computed hash lookup to crack passwords "
            "(mitigated by salting).</li>"
            "<li><strong>Birthday attack</strong> – Exploits hash collision probability.</li>"
            "<li><strong>Downgrade attack</strong> – Forces use of weaker protocol/cipher (e.g., POODLE).</li>"
            "</ul>"
        ),
        "key_points": [
            "Phishing (mass) → Spear phishing (targeted) → Whaling (executives).",
            "Vishing = voice; smishing = SMS; pretexting = fabricated scenario.",
            "DDoS targets availability; MitM attacks confidentiality and integrity.",
            "SQL injection and XSS are top application-layer attacks; mitigated by input validation.",
            "Rainbow table attacks are defeated by password salting.",
            "Downgrade attacks force weaker protocols/ciphers (POODLE exploited SSL 3.0).",
            "CSRF exploits the trust a server has in an authenticated browser session.",
        ],
    },
]
