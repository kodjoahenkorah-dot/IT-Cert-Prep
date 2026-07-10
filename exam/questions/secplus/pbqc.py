"""CompTIA Security+ SY0-701 Performance-Based Questions (PBQs), file C.

12 questions covering the nine highest-yield real-exam PBQ archetypes: log
analysis/investigation, firewall/ACL configuration, network architecture zone
placement, IAM/access control assignment, vulnerability prioritization AND
remediation matching, cryptographic solution selection, email-authentication
(SPF/DKIM/DMARC) triage, backup/DR/BC term matching, and security-control
acronym/purpose matching. Several archetypes get a second, differently-shaped
question to reach the full set of 12.

Type breakdown: 7 pbq_matching, 1 pbq_ordering, 4 pbq_categorize.
Domain breakdown: D1 x1, D3 x3, D4 x8.

Archetype coverage:
  1. Log analysis / investigation          -> npbqc-001 (matching), npbqc-011 (categorize)
  2. Firewall / ACL configuration          -> npbqc-002 (matching)
  3. Network architecture / secure design  -> npbqc-003 (categorize)
  4. IAM / access control                  -> npbqc-004 (matching)
  5. Vulnerability management/remediation  -> npbqc-005 (ordering), npbqc-006 (matching)
  6. Cryptography / PKI / certificate      -> npbqc-007 (matching)
  7. Email security / phishing             -> npbqc-008 (categorize)
  8. Backup / DR / business continuity     -> npbqc-009 (matching)
  9. Acronym / control matching            -> npbqc-010 (matching), npbqc-012 (categorize)
"""

QUESTIONS = [
    # ══════════════════════════════════════════════════════════════════
    # 1. LOG ANALYSIS / INVESTIGATION
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-001",
        "domain": 4,
        "objective": "4.1",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A SOC analyst pulls the following log excerpts from the last 15 minutes:\n\n"
            "Firewall/NetFlow: 2026-07-10 09:14:02 ALLOW TCP 10.40.7.23:51502 -> 185.220.101.17:4444 "
            "(outbound, novel destination, first seen on this network)\n"
            "Firewall/NetFlow: 2026-07-10 09:14:47 ALLOW TCP 10.40.7.23:51503 -> 185.220.101.17:4444 "
            "(outbound, repeat connection, ~45s interval)\n"
            "EDR process log, host FIN-WKS-014 (10.40.7.23): winword.exe (PID 4102) spawned "
            "powershell.exe (PID 5590), command line 'powershell -enc SQBFAFgAKABOAGUAdw...'\n"
            "IDS alert: [1:2024897] ET MALWARE Cobalt Strike Beacon 4.x Malleable C2 Checkin  "
            "src=10.40.7.23 dst=185.220.101.17:4444 sid:2024897\n\n"
            "Match each investigative question to the answer this specific evidence supports."
        ),
        "prompts": [
            {"id": "p1", "text": "Which host is infected and must be prioritized for containment?"},
            {"id": "p2", "text": "What attack does the combined IDS and EDR evidence indicate?"},
            {"id": "p3", "text": "What external IP is the malware communicating with?"},
            {"id": "p4", "text": "What is the single best immediate remediation step given the evidence collected so far?"},
        ],
        "targets": [
            {"id": "t1", "text": "FIN-WKS-014 (10.40.7.23) — the host that spawned the encoded PowerShell command and is beaconing outward"},
            {"id": "t2", "text": "MAIL-SRV02 (10.40.7.19) — a host never referenced anywhere in the collected log lines"},
            {"id": "t3", "text": "A Cobalt Strike command-and-control beacon following malicious macro execution (encoded PowerShell spawned by winword.exe, confirmed by a signature match on the outbound traffic)"},
            {"id": "t4", "text": "A SQL injection attack against a web application — no HTTP request or query-string indicator appears anywhere in this evidence"},
            {"id": "t5", "text": "185.220.101.17 — the repeated outbound destination flagged by both the firewall log and the IDS signature"},
            {"id": "t6", "text": "10.40.7.23 — this is the internal, already-compromised host's own address, not the external destination the question asked for"},
            {"id": "t7", "text": "Isolate FIN-WKS-014 from the network immediately and begin full incident-response triage (memory capture, credential rotation, scope hunt) rather than only blocking the single C2 IP"},
            {"id": "t8", "text": "Add a firewall rule blocking outbound traffic to 185.220.101.17 only, and consider the incident resolved"},
        ],
        "answer": {"p1": "t1", "p2": "t3", "p3": "t5", "p4": "t7"},
        "rationales": {
            "p1": "Every piece of evidence — the outbound firewall connections, the EDR process lineage, and the IDS alert — all key on 10.40.7.23/FIN-WKS-014; t2 is a trap because that host never appears in any log line shown.",
            "p2": "winword.exe spawning encoded PowerShell, immediately followed by a signature-matched Cobalt Strike beacon to the same destination, is the textbook chain of macro-delivered C2 establishment; t4 (SQL injection) has zero supporting evidence here — no HTTP payload or database query appears anywhere.",
            "p3": "185.220.101.17 is the destination in both the firewall log and the IDS alert; t6 is a classic reading trap that swaps the internal source IP for the external destination the question actually asked about.",
            "p4": "A single infected host with confirmed C2 beaconing requires isolation plus full IR triage; t8 only blocks one destination IP and declares victory, ignoring that the attacker may already have persistence, harvested credentials, or additional C2 infrastructure not yet observed.",
        },
        "explanation": (
            "Investigation PBQs test whether you can trace one coherent story across independent log sources — network, "
            "endpoint, and IDS — rather than treating each alert in isolation. The most common failure mode is stopping "
            "remediation at 'block the IP' instead of treating the host itself as compromised and scoping the incident further."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 2. FIREWALL / ACL CONFIGURATION
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-002",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A network engineer must implement four business requirements on the edge firewall for a three-tier "
            "e-commerce environment (web tier 10.60.1.0/24, app tier 10.60.2.0/24, db tier 10.60.3.0/24, app "
            "server 10.60.2.5, database 10.60.3.20 on port 1433). Match each requirement to the single ACL rule "
            "that correctly and precisely implements it. Not every target is used, and some are deliberately "
            "close near-misses of the correct rule."
        ),
        "prompts": [
            {"id": "p1", "text": "The public web server (10.60.1.10) must be reachable from the Internet over HTTPS only"},
            {"id": "p2", "text": "The database server must be reachable only from the application server, over its SQL port, and from nowhere else"},
            {"id": "p3", "text": "SSH (TCP/22) management access to any host must be blocked from the public Internet"},
            {"id": "p4", "text": "The application and database tiers must never be directly reachable from the public Internet"},
        ],
        "targets": [
            {"id": "t1", "text": "PERMIT TCP any -> 10.60.1.10:443"},
            {"id": "t2", "text": "PERMIT TCP any -> 10.60.1.10:22"},
            {"id": "t3", "text": "PERMIT TCP 10.60.2.5 -> 10.60.3.20:1433"},
            {"id": "t4", "text": "PERMIT TCP 10.60.1.0/24 -> 10.60.3.20:1433"},
            {"id": "t5", "text": "DENY TCP any -> any:22"},
            {"id": "t6", "text": "PERMIT TCP 10.10.9.0/24 -> any:22"},
            {"id": "t7", "text": "DENY TCP any -> 10.60.2.0/24:any  and  DENY TCP any -> 10.60.3.0/24:any"},
            {"id": "t8", "text": "PERMIT TCP 10.60.1.0/24 -> 10.60.2.0/24:any"},
        ],
        "answer": {"p1": "t1", "p2": "t3", "p3": "t5", "p4": "t7"},
        "rationales": {
            "p1": "t1 permits only TCP/443 from any source to the specific web-server IP, exactly matching 'public HTTPS only'; t2 is a near-miss that opens SSH — not HTTPS — publicly to the same host and would fail p1's requirement entirely.",
            "p2": "t3 scopes SQL access to exactly the app server's single IP; t4 is the classic over-permissive trap, granting the entire web subnet database access instead of the one authorized host, violating least privilege.",
            "p3": "t5 denies SSH from any source at the edge, satisfying 'blocked from the Internet'; t6 only permits an admin subnet — it doesn't itself block Internet-sourced SSH attempts and would need a separate deny to actually satisfy this requirement.",
            "p4": "t7 explicitly denies all Internet-sourced traffic to both the app and db subnets, directly satisfying the requirement; t8 is a distractor about web-to-app traffic that says nothing about blocking Internet access and is also far more permissive ('any' port) than any stated need.",
        },
        "explanation": (
            "Each requirement has a rule that matches it precisely and at least one 'looks similar but is wrong' rule "
            "nearby: same host with the wrong port (t1/t2), same purpose but the wrong source scope (t3/t4), and a permit "
            "rule that doesn't actually implement the required deny (t5/t6). Precision on source, destination, port, and "
            "action — not just topic — is what the exam is testing."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 3. NETWORK ARCHITECTURE / SECURE DESIGN
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-003",
        "domain": 3,
        "objective": "3.1",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A security architect is laying out zones for a new enterprise network build. Place each device into "
            "the network zone where it should be deployed."
        ),
        "categories": [
            {"id": "c1", "text": "Internet edge"},
            {"id": "c2", "text": "DMZ"},
            {"id": "c3", "text": "Internal (trusted) network"},
            {"id": "c4", "text": "Management / security-operations zone"},
        ],
        "items": [
            {"id": "i1", "text": "The next-generation firewall that terminates the ISP circuit and is the first device to inspect all inbound and outbound Internet traffic before it reaches any other segment"},
            {"id": "i2", "text": "The public-facing web application server that customers reach directly over HTTPS, deliberately placed so a breach of it cannot pivot straight into internal systems"},
            {"id": "i3", "text": "The web application firewall placed directly in front of the public web server to inspect and filter HTTP/HTTPS payloads before they reach the application"},
            {"id": "i4", "text": "The VPN concentrator that terminates encrypted remote-access tunnels from traveling employees, sitting alongside the edge firewall before decrypted traffic is handed to any internal segment"},
            {"id": "i5", "text": "The SIEM platform that ingests and correlates logs from every zone; it must never be directly reachable from the Internet or from general user workstations, only from SOC analyst workstations"},
            {"id": "i6", "text": "The hardened jump box (bastion host) that administrators must authenticate through before reaching any production server for maintenance, itself reachable only from a small set of admin workstations"},
            {"id": "i7", "text": "The IPS sensor placed inline at the boundary between the DMZ and the internal network, positioned to catch anything that gets past the edge firewall and WAF before it reaches internal systems"},
            {"id": "i8", "text": "The database server holding customer PII, which application logic requires but which must never be exposed to the public Internet or accept connections from the DMZ web tier directly"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c2", "i4": "c1", "i5": "c4", "i6": "c4", "i7": "c3", "i8": "c3"},
        "rationales": {
            "i1": "The device terminating the ISP circuit and inspecting all traffic first, before any other segment sees it, is by definition sitting at the Internet edge.",
            "i2": "A server that must be directly reachable by anonymous public users, yet isolated so its compromise doesn't reach internal systems, is the textbook purpose of the DMZ.",
            "i3": "The WAF's entire job is application-layer inspection of traffic destined for the public web server, so it sits alongside that server in the DMZ — not at the edge (which handles all traffic generically) and not internally (the public never reaches that far).",
            "i4": "Like the edge firewall, the VPN concentrator terminates external connections and makes the initial trust decision before traffic is handed off further inward, placing it at the Internet edge alongside the firewall.",
            "i5": "A SIEM that must never be reachable by the Internet or general users, only by SOC analysts, belongs in a restricted management/security-operations zone rather than the general internal network where ordinary users and their workstations reside.",
            "i6": "A bastion host's entire purpose is to be the single, tightly controlled chokepoint administrators pass through before touching production, which is the defining function of a management zone, not the general trusted network.",
            "i7": "This IPS defends the internal network from anything that slipped past the DMZ-facing controls, so its protective scope — and therefore its placement — is on the internal side of that boundary, distinct from the DMZ devices (i2/i3) that protect the public-facing web tier specifically.",
            "i8": "A database holding sensitive data that must never be Internet-facing and never accept direct DMZ connections is placed in the internal network, reachable only indirectly through the app tier.",
        },
        "explanation": (
            "The recurring trap is conflating 'security tool' with 'internal zone': a SIEM and a bastion host are both "
            "security-critical, but their requirement for restricted, admin-only reachability puts them in a dedicated "
            "management zone — not the same internal segment as ordinary trusted workstations and application servers. "
            "Likewise, a WAF belongs with the DMZ asset it protects, while an IPS defending the internal side of that "
            "same boundary belongs with the internal zone it protects."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 4. IAM / ACCESS CONTROL
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-004",
        "domain": 4,
        "objective": "4.6",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "An identity team is assigning the correct access-control approach to five job-role scenarios. Match "
            "each scenario to the single best-fitting control."
        ),
        "prompts": [
            {"id": "p1", "text": "A newly hired accounts-payable clerk must enter and approve vendor invoices up to $500, but must never be able to modify vendor banking details or approve an invoice they personally entered"},
            {"id": "p2", "text": "A domain administrator only needs elevated rights during two scheduled maintenance windows a month; the rest of the time their standard account should hold no domain-admin privileges at all"},
            {"id": "p3", "text": "A remote sales rep who has always logged in from Ohio during business hours suddenly authenticates from a new country, on a personal unmanaged laptop, at 3 a.m."},
            {"id": "p4", "text": "A third-party contractor engaged for a 6-week project needs access to exactly one file share relevant to that project, with access ending automatically when the contract ends"},
            {"id": "p5", "text": "A payroll manager currently both enters payroll changes and approves payroll runs; audit policy requires those two functions be performed by different people or systems"},
        ],
        "targets": [
            {"id": "t1", "text": "A role-based least-privilege permission set combined with separation-of-duties controls that prevent the clerk from approving invoices they created"},
            {"id": "t2", "text": "Standing (always-on) domain administrator group membership, protected only by a strong password policy"},
            {"id": "t3", "text": "Privileged access management (PAM) with just-in-time elevation: a standard account by default, with admin rights checked out only for the scheduled window and automatically expiring"},
            {"id": "t4", "text": "A conditional/risk-based access policy that requires step-up MFA and device-compliance verification when the sign-in context is anomalous"},
            {"id": "t5", "text": "A single shared 'contractor' account provisioned with broad file-share access for convenience, protected only by a strong password"},
            {"id": "t6", "text": "A named, time-limited least-privilege account scoped to only the required file share, with an expiration date matching the contract end date and automatic disablement"},
            {"id": "t7", "text": "Separation of duties requiring payroll entry and payroll approval to be performed by two different authorized individuals or systems, with no single account holding both capabilities"},
            {"id": "t8", "text": "Mandatory access control (MAC) labels applied uniformly to every payroll-system user regardless of job function"},
        ],
        "answer": {"p1": "t1", "p2": "t3", "p3": "t4", "p4": "t6", "p5": "t7"},
        "rationales": {
            "p1": "The requirement is both least privilege (limited to entering/approving small invoices) and separation of duties (can't approve their own entry), which is exactly what t1 provides.",
            "p2": "The requirement is explicitly time-bound elevation, which is PAM with just-in-time access, not merely MFA on a permanently privileged account (t2) — standing admin membership violates least privilege regardless of password strength.",
            "p3": "New country, unmanaged device, and off-hours timing are classic anomalous sign-in risk signals that should trigger conditional/risk-based access requiring step-up verification, not a static, always-applied control.",
            "p4": "The requirement calls for individual accountability and automatic expiration tied to the contract, which t6 provides; t5's shared account defeats accountability and grants broader access than the one needed share.",
            "p5": "The requirement is explicitly to split creation and approval across two different actors, which is separation of duties; t8's uniform MAC labeling does nothing to address who is allowed to perform which specific function.",
        },
        "explanation": (
            "PAM with just-in-time elevation is frequently confused with 'just add MFA to the admin account' — MFA verifies "
            "the person, but doesn't remove the standing privilege itself, which is the actual risk when an account is "
            "compromised. Similarly, a shared account can still be 'least privilege' in scope but still fails accountability, "
            "which is a separate control objective the exam tests independently."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 5a. VULNERABILITY MANAGEMENT — PRIORITIZATION (ordering)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-005",
        "domain": 4,
        "objective": "4.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability management team has six open findings. Order them from MOST urgent to LEAST urgent "
            "to remediate, based on real-world risk (exploitability, exposure, business/data impact, and existing "
            "compensating controls) — not simply by CVSS base score."
        ),
        "items": [
            {"id": "i1", "text": "Internet-facing VPN appliance, CVSS 9.8 critical RCE, listed on the CISA Known Exploited Vulnerabilities catalog and actively being exploited in the wild against this vendor's appliances this week, no compensating control in place, provides a direct path into the internal network"},
            {"id": "i2", "text": "Public marketing website contact form, CVSS 6.1 medium reflected XSS, but WAF logs show active exploitation attempts against this exact form over the past 48 hours, and the site is the company's primary revenue channel"},
            {"id": "i3", "text": "Point-of-sale terminal firmware, CVSS 7.5 high, no public exploit code known yet, processes cardholder data (PCI DSS scope) and is network-adjacent to the payment gateway; vendor patch is available now"},
            {"id": "i4", "text": "Internal HR reporting application, CVSS 9.1 critical RCE, reachable only from a single management VLAN restricted to three trusted administrators, and an inline IPS signature already virtually patches the specific exploit pattern"},
            {"id": "i5", "text": "Internal file server, CVSS 8.8 high privilege-escalation flaw, public exploit code exists but requires an authenticated local session to use, affects only a low-criticality test-lab share with no production data"},
            {"id": "i6", "text": "Deprecated internal development server, CVSS 9.8 critical RCE, isolated on its own segmented VLAN with no production data, and already scheduled for full decommission next week"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6"],
        "rationales": {
            "i1": "A KEV-listed, actively-exploited-in-the-wild critical RCE on an Internet-facing appliance with no compensating control and a direct path inward is the single highest real-world risk on the list, regardless of what else scores 9.8.",
            "i2": "Even at a medium CVSS, evidence of active exploitation attempts this week against an Internet-facing, revenue-critical asset makes this more urgent than any finding with only theoretical exploitability — active attack in progress outranks unexploited critical/high findings.",
            "i3": "No public exploit exists yet, but the asset's PCI DSS scope and adjacency to the payment gateway make the business impact severe, and a patch is already available — this should be closed before it becomes the next actively-exploited item, ranking above findings that already have exposure-limiting factors.",
            "i4": "The CVSS is critical, but restricted reachability (three trusted admins on one management VLAN) plus an existing virtual patch via IPS substantially reduce real exposure; it still needs a true fix, but it is measurably less urgent than i1-i3's live or PCI-scoped exposure.",
            "i5": "A high CVSS score is undercut by the requirement for authenticated local access and the low criticality of the affected test-lab asset, placing this below every finding with either external exposure or regulated data at stake.",
            "i6": "This finding has the highest raw CVSS number on the list, yet its isolation, absence of production data, and imminent decommission make its real-world risk the lowest of all six — a clear illustration that CVSS base score alone is not a prioritization method.",
        },
        "explanation": (
            "Real prioritization weighs exploitability (is it in the KEV catalog / being actively exploited right now?), "
            "exposure (Internet-facing vs. restricted-VLAN vs. requires local auth), data/business criticality (PCI scope, "
            "revenue impact), and any existing compensating control (virtual patching, segmentation) against the raw CVSS "
            "number. i6 and i4 both carry higher CVSS scores than i2 or i3, but genuinely lower real-world risk — the "
            "opposite of a naive 'sort by CVSS descending' ordering."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 5b. VULNERABILITY MANAGEMENT — REMEDIATION (matching)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-006",
        "domain": 4,
        "objective": "4.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "Match each vulnerability finding to the single best remediation approach. Several targets are "
            "deliberately close near-misses of the correct action."
        ),
        "prompts": [
            {"id": "p1", "text": "A critical RCE (CVSS 9.8) in an Internet-facing VPN appliance has a vendor-released patch available today"},
            {"id": "p2", "text": "A legacy ICS/SCADA HMI has a known critical vulnerability; the vendor will not patch this end-of-life firmware, and the device cannot be taken offline because it controls live physical plant equipment"},
            {"id": "p3", "text": "A public web application has a SQL injection flaw in custom code; a proper code fix is scheduled for release in 3 weeks, but exploitation attempts are already appearing in WAF logs today"},
            {"id": "p4", "text": "A scan flags an unused test server with no production data, already scheduled for retirement in two weeks"},
            {"id": "p5", "text": "A finding affects a business-critical application, but the CVSS is low (3.1) and exploitation requires physical console access already restricted to two trusted data-center staff"},
        ],
        "targets": [
            {"id": "t1", "text": "Apply the vendor patch immediately through an expedited/emergency change process given the exposure and severity"},
            {"id": "t2", "text": "Defer the vendor patch to the next scheduled quarterly maintenance window since the appliance has been stable"},
            {"id": "t3", "text": "Implement a compensating control — strict network segmentation, ACL restriction, and enhanced monitoring around the HMI — since no vendor patch exists and the device cannot go offline"},
            {"id": "t4", "text": "Take the HMI offline immediately to apply a patch, accepting the resulting halt to physical plant operations"},
            {"id": "t5", "text": "Deploy an interim WAF virtual patch blocking the specific SQL injection pattern while the permanent code fix proceeds on its scheduled release"},
            {"id": "t6", "text": "Deploy the WAF virtual patch and cancel the scheduled code fix, treating the vulnerability as fully remediated"},
            {"id": "t7", "text": "Decommission the test server on its planned retirement schedule rather than diverting remediation effort to a soon-to-be-destroyed asset"},
            {"id": "t8", "text": "Formally document and obtain sign-off for risk acceptance, given the low CVSS and existing physical-access restriction"},
            {"id": "t9", "text": "Close the finding with no documentation, since it only appeared on a single scan"},
        ],
        "answer": {"p1": "t1", "p2": "t3", "p3": "t5", "p4": "t7", "p5": "t8"},
        "rationales": {
            "p1": "A critical, exposed vulnerability with a patch already available should be remediated immediately via expedited change control, not deferred to routine maintenance (t2), which leaves the exposure open far longer than necessary.",
            "p2": "When no patch exists and the asset cannot be taken offline, a compensating control is the textbook response; taking the HMI offline (t4) is operationally unsafe and directly contradicts the stated constraint that it controls live physical equipment.",
            "p3": "A virtual patch via the WAF is the correct interim mitigation while the real code-level fix ships on schedule; canceling the code fix (t6) mistakes a temporary mitigation for a permanent one — the underlying vulnerable code still needs to be fixed.",
            "p4": "Remediation effort is not worth spending on an asset that is already scheduled for destruction with no production data at risk; decommissioning on schedule resolves the finding without wasted work.",
            "p5": "A low-severity finding with likelihood already constrained by existing physical controls, where remediation cost would exceed the residual risk, is the classic case for formal, documented risk acceptance — not silent closure (t9), which leaves no audit trail and could hide a real gap.",
        },
        "explanation": (
            "Remediation isn't always 'patch it': the correct action depends on whether a patch exists, whether the asset "
            "can tolerate downtime, whether an interim mitigation is appropriate while a permanent fix is pending, and "
            "whether the residual risk is low enough to formally accept. Confusing a virtual patch with a permanent fix, "
            "or silent closure with documented risk acceptance, are the two most common wrong answers here."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 6. CRYPTOGRAPHY / PKI / CERTIFICATE
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-007",
        "domain": 1,
        "objective": "1.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Certificates",
        "stem": (
            "A security architect must select the correct cryptographic solution for each business need. Match "
            "each requirement to the single best solution."
        ),
        "prompts": [
            {"id": "p1", "text": "Protect the contents of every laptop's hard drive so that, if a device is lost or stolen, the data is unreadable without the correct key"},
            {"id": "p2", "text": "Prove that a downloaded software update has not been altered or corrupted since the vendor published it"},
            {"id": "p3", "text": "Attribute a signed contract to the specific executive who approved it, such that they cannot later credibly deny having signed it"},
            {"id": "p4", "text": "Encrypt traffic between customers' browsers and the e-commerce checkout page, and prove the site's identity to the browser"},
            {"id": "p5", "text": "Let the payment processor keep a stand-in value for a customer's card number in the order database so the real PAN never has to be retained after the transaction completes"},
            {"id": "p6", "text": "Ensure a busy e-commerce web server's private TLS key is generated and stored so it can never be extracted, while still supporting high-volume signing during peak sales traffic"},
        ],
        "targets": [
            {"id": "t1", "text": "Full-disk encryption using a symmetric algorithm such as AES"},
            {"id": "t2", "text": "One-way cryptographic hashing (e.g., SHA-256) of the drive contents"},
            {"id": "t3", "text": "A cryptographic hash/digest published alongside the file for integrity verification"},
            {"id": "t4", "text": "A digital signature applied with the signer's private key, verifiable with their public key"},
            {"id": "t5", "text": "A symmetric session key shared out-of-band before the purchase, with no certificate involved"},
            {"id": "t6", "text": "Transport Layer Security (TLS) using a publicly trusted PKI certificate bound to the site's domain"},
            {"id": "t7", "text": "Tokenization: the real card number is replaced with a token that cannot be reversed without the separate vault the tokenization provider maintains"},
            {"id": "t8", "text": "Data masking that displays only the last four digits on screen while the full card number remains stored in the database"},
            {"id": "t9", "text": "A hardware security module (HSM): a dedicated, tamper-resistant appliance that generates/stores the private key and performs high-throughput signing for the server"},
            {"id": "t10", "text": "A Trusted Platform Module (TPM) bound to the web server's motherboard"},
        ],
        "answer": {"p1": "t1", "p2": "t3", "p3": "t4", "p4": "t6", "p5": "t7", "p6": "t9"},
        "rationales": {
            "p1": "Data at rest that must later be read back requires reversible encryption; t2's one-way hashing can never be decrypted back into usable drive contents, making it useless for this purpose despite sounding cryptographically strong.",
            "p2": "A published hash lets anyone independently recompute and compare it to detect any alteration to the file — exactly an integrity check, not a confidentiality or identity mechanism.",
            "p3": "A digital signature, created with the signer's own private key, is what legally and cryptographically binds the action to that specific individual and provides non-repudiation.",
            "p4": "Confidential, anonymous browsers need both encryption and proof of the site's identity; t5's private out-of-band symmetric key can't scale to anonymous public customers and provides no identity proof, which is the entire point of a PKI certificate.",
            "p5": "Tokenization replaces the sensitive value itself in storage so the real PAN doesn't need to be retained; t8's masking only changes what's displayed on screen while the full number remains stored, which does not satisfy the stated requirement to avoid retaining it.",
            "p6": "An HSM is a dedicated, high-throughput appliance built for server-side key storage and bulk signing; a TPM (t10) is instead bound to one specific device for platform/boot integrity and is not designed for a busy server's shared, high-volume signing workload.",
        },
        "explanation": (
            "This item deliberately pairs each correct answer with a plausible-sounding wrong tool: hashing vs. encryption "
            "(one-way vs. reversible), masking vs. tokenization (display control vs. storage replacement), and HSM vs. TPM "
            "(shared server appliance vs. single-device platform chip). Recognizing the mechanism's actual property — "
            "reversible or not, stored value changed or just displayed differently, shared or bound to one device — is "
            "what separates the correct choice from the near-miss."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 7. EMAIL SECURITY / PHISHING
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-008",
        "domain": 4,
        "objective": "4.3",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A messaging administrator reviews Authentication-Results header lines for six recent messages. "
            "Classify each by which authentication mechanism is the true cause of failure, or confirm the "
            "message fully passed."
        ),
        "categories": [
            {"id": "c1", "text": "SPF failed"},
            {"id": "c2", "text": "DKIM failed"},
            {"id": "c3", "text": "DMARC failed due to alignment (SPF and DKIM each individually passed, but for a domain that doesn't align with the visible From: header)"},
            {"id": "c4", "text": "All authentication passed (legitimate)"},
        ],
        "items": [
            {"id": "i1", "text": "Authentication-Results: spf=fail (198.51.100.9 is not a designated sender for paypal-secure-alerts.com) smtp.mailfrom=paypal-secure-alerts.com; dkim=none; dmarc=fail (p=reject) header.from=paypal-secure-alerts.com"},
            {"id": "i2", "text": "Authentication-Results: spf=pass smtp.mailfrom=news.vendor.com; dkim=fail (body hash did not verify, signature invalid) header.d=vendor.com; dmarc=fail (p=quarantine) header.from=vendor.com"},
            {"id": "i3", "text": "Authentication-Results: spf=pass smtp.mailfrom=bounce.marketingcloud.net; dkim=pass header.d=marketingcloud.net; dmarc=fail (p=quarantine, no alignment between mailfrom/d= and header.from) header.from=yourbank.com"},
            {"id": "i4", "text": "Authentication-Results: spf=pass smtp.mailfrom=notifications.company.com; dkim=pass header.d=company.com; dmarc=pass (p=none) header.from=company.com"},
            {"id": "i5", "text": "Authentication-Results: spf=softfail (~all, sending IP not listed but domain has not committed to a hard fail) smtp.mailfrom=oldserver.company.com; dkim=pass header.d=company.com; dmarc=pass (DKIM alignment is sufficient) header.from=company.com"},
            {"id": "i6", "text": "Authentication-Results: spf=fail (203.0.113.5 not authorized) smtp.mailfrom=noreply@it-support-desk.co; dkim=pass header.d=it-support-desk.co; dmarc=fail (p=reject, mailfrom domain it-support-desk.co does not align with header.from company.com) header.from=company.com"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c4", "i6": "c1"},
        "rationales": {
            "i1": "spf=fail shows the sending IP was never authorized for the mailfrom domain, and no DKIM signature exists at all — the message fails at the most basic authentication layer, making SPF the direct cause.",
            "i2": "SPF passes here, but the DKIM signature explicitly fails verification (an invalid body hash), meaning the message was altered or improperly signed in transit — DKIM is the mechanism that actually broke.",
            "i3": "Both SPF and DKIM technically pass, but only for marketingcloud.net — neither result aligns with the visible header.from of yourbank.com, so DMARC alone catches the spoofing attempt even though the individual checks look clean; this is the classic alignment-failure trap.",
            "i4": "SPF, DKIM, and DMARC all explicitly pass and every domain aligns to company.com — this is a fully authenticated, legitimate message.",
            "i5": "A softfail is not a hard failure, and DKIM's pass and alignment with company.com are sufficient for DMARC to pass overall — this illustrates that a marginal SPF result does not automatically doom the message if DKIM alignment covers it.",
            "i6": "Although dkim=pass appears in the header, it verifies for the unrelated/lookalike domain it-support-desk.co, not company.com — that pass is meaningless for spoofing purposes. The message is spoofing company.com, and SPF's explicit failure alongside DMARC's alignment rejection makes SPF the true root cause, not the irrelevant DKIM pass for a different domain.",
        },
        "explanation": (
            "The two hardest traps here are i3 and i6: both show SPF and/or DKIM 'passing,' but the pass is for the wrong "
            "domain entirely and does not align with the visible From: address the recipient actually sees — which is "
            "precisely the spoofing technique DMARC alignment exists to catch. A candidate who stops at 'SPF/DKIM says "
            "pass' without checking WHICH domain passed will misclassify both."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 8. BACKUP / DR / BUSINESS CONTINUITY
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-009",
        "domain": 3,
        "objective": "3.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "Match each business-continuity statement to the single correct recovery term or solution. Two "
            "targets are deliberately close near-misses that should not be used."
        ),
        "prompts": [
            {"id": "p1", "text": "The order-processing database must be back online and processing transactions within 4 hours of any outage, per the signed BC plan"},
            {"id": "p2", "text": "Continuous replication ensures that, in the worst case, no more than 5 minutes of transaction data will ever be lost in a failure"},
            {"id": "p3", "text": "The organization maintains a fully equipped, continuously data-synchronized duplicate data center that can take over processing within minutes of a declared disaster"},
            {"id": "p4", "text": "The organization leases data-center space with power, cooling, and connectivity already in place and basic hardware racked, but data must be restored from backups and systems configured before it can serve traffic — a multi-day process"},
            {"id": "p5", "text": "The organization has a contractual right to an empty data-center shell with power and space, but must ship in and install all hardware from scratch before recovery can even begin — a multi-week process"},
            {"id": "p6", "text": "Every Sunday night a full copy of all data is captured; every other night, only the data changed since the LAST FULL backup is captured, so Thursday's restore needs only the full backup plus Thursday's own backup"},
            {"id": "p7", "text": "Every Sunday night a full copy of all data is captured; every other night, only the data changed since the PREVIOUS backup (full or incremental) is captured, so Thursday's restore needs the full backup plus every incremental from Monday through Thursday, in sequence"},
            {"id": "p8", "text": "Historical data shows this storage array's redundant power supply runs an average of 50,000 hours before any failure occurs"},
            {"id": "p9", "text": "After the last four outages, the team's average elapsed time from failure detection to full service restoration was 65 minutes"},
        ],
        "targets": [
            {"id": "t1", "text": "Recovery Time Objective (RTO)"},
            {"id": "t2", "text": "Recovery Point Objective (RPO)"},
            {"id": "t3", "text": "Hot site"},
            {"id": "t4", "text": "Warm site"},
            {"id": "t5", "text": "Cold site"},
            {"id": "t6", "text": "Differential backup"},
            {"id": "t7", "text": "Incremental backup"},
            {"id": "t8", "text": "Mean Time Between Failures (MTBF)"},
            {"id": "t9", "text": "Mean Time to Repair/Restore (MTTR)"},
            {"id": "t10", "text": "Full backup (every night, every file captured in its entirety)"},
            {"id": "t11", "text": "Maximum Tolerable Downtime (MTD) — the absolute ceiling of outage time before the business suffers unrecoverable harm"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5", "p6": "t6", "p7": "t7", "p8": "t8", "p9": "t9"},
        "rationales": {
            "p1": "A defined target time to restore service after an outage is the Recovery Time Objective; t11's MTD is a related but distinct ceiling concept — the absolute maximum the business can survive, not the planned recovery target itself.",
            "p2": "A defined maximum tolerable amount of data loss, measured in time between backups/replication, is the Recovery Point Objective.",
            "p3": "A continuously synchronized, fully staffed duplicate site that can take over within minutes is the textbook definition of a hot site.",
            "p4": "Infrastructure in place but requiring a multi-day restore-and-configure effort before serving traffic is a warm site — faster than cold, slower than hot.",
            "p5": "An empty shell requiring hardware to be shipped and installed from scratch, taking weeks, is a cold site — the slowest and cheapest recovery-site option.",
            "p6": "Backing up everything changed since the last FULL backup each night, so a restore only ever needs the full backup plus one differential, is the definition of a differential backup.",
            "p7": "Backing up everything changed since the PREVIOUS backup (whatever it was) each night, requiring the full backup plus every incremental in sequence to restore, is the definition of an incremental backup — note this restore takes longer than a differential's despite each nightly job being smaller.",
            "p8": "An average time between failures for a piece of hardware, describing reliability rather than recovery speed, is Mean Time Between Failures.",
            "p9": "An average elapsed time to actually fix/restore service after a failure occurs is Mean Time to Repair/Restore, distinct from MTBF's failure-frequency measurement.",
        },
        "explanation": (
            "The two hardest discriminators are differential vs. incremental (both compare against a full backup, but "
            "differential always compares to the last FULL, while incremental compares to whatever the LAST backup was — "
            "making incremental restores faster to back up nightly but slower to restore) and RTO vs. MTD (RTO is the "
            "planned target; MTD is the outer limit the business can survive before an outage becomes existential). t10 "
            "(full backup) and t11 (MTD) are included specifically because they are the terms most often confused with "
            "differential/incremental and RTO, respectively."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 9a. ACRONYM / CONTROL MATCHING
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-010",
        "domain": 4,
        "objective": "4.5",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "Match each security control acronym to its correct purpose. Two targets are deliberately close "
            "near-misses that should not be used."
        ),
        "prompts": [
            {"id": "p1", "text": "SIEM"},
            {"id": "p2", "text": "SOAR"},
            {"id": "p3", "text": "EDR"},
            {"id": "p4", "text": "XDR"},
            {"id": "p5", "text": "DLP"},
            {"id": "p6", "text": "IDS"},
            {"id": "p7", "text": "IPS"},
            {"id": "p8", "text": "WAF"},
            {"id": "p9", "text": "NAC"},
        ],
        "targets": [
            {"id": "t1", "text": "Centrally aggregates and correlates log/event data from many sources to generate alerts and support investigation, but does not itself take automated remediation action"},
            {"id": "t2", "text": "Ingests alerts (often from a SIEM) and executes automated, predefined playbooks to contain or remediate an incident without waiting for a human to perform every step"},
            {"id": "t3", "text": "Monitors and records process, file, and network activity on an individual endpoint, and can isolate or kill malicious processes on that one host"},
            {"id": "t4", "text": "Correlates and responds to telemetry across endpoints, network, email, and cloud sources together, extending single-host endpoint visibility into a unified cross-layer detection and response capability"},
            {"id": "t5", "text": "Inspects outbound content (email, USB, cloud upload) for sensitive data patterns and blocks or flags the transfer before it leaves the organization"},
            {"id": "t6", "text": "Passively monitors a copy of network traffic (e.g., via a SPAN/mirror port) and generates an alert on a signature/anomaly match, but cannot itself drop or block the traffic"},
            {"id": "t7", "text": "Sits inline in the active traffic path and automatically drops packets matching a known malicious signature the instant it is detected, without waiting for a human decision"},
            {"id": "t8", "text": "Sits in front of a web application and inspects HTTP/HTTPS requests specifically for application-layer attacks such as SQL injection and XSS"},
            {"id": "t9", "text": "Evaluates a device's identity, posture (patch level, AV status), and credentials before granting network access at the switch port or wireless association, and can quarantine non-compliant devices"},
            {"id": "t10", "text": "Legacy signature-based antivirus scanning limited to known malware definitions on a single host, with no behavioral detection or automated isolation capability"},
            {"id": "t11", "text": "A perimeter device that filters traffic strictly by IP address, port, and protocol, with no application-layer awareness of the request content"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5", "p6": "t6", "p7": "t7", "p8": "t8", "p9": "t9"},
        "rationales": {
            "p1": "A SIEM's core role is aggregation and correlation for alerting/investigation; t2 (SOAR) is the near-miss that instead performs the automated response action a SIEM by itself does not.",
            "p2": "SOAR is specifically the orchestration/automation layer that executes playbooks in response to alerts, distinguishing it from the SIEM that generates those alerts in the first place.",
            "p3": "EDR's defining scope is a single endpoint; t4 (XDR) is the near-miss that extends this same behavioral concept across multiple telemetry sources simultaneously.",
            "p4": "XDR's differentiator from EDR is explicitly the cross-layer correlation (endpoint + network + email + cloud together), not just deeper single-host visibility.",
            "p5": "DLP is defined by its focus on the sensitive data content itself, regardless of which channel (email, USB, cloud) it is leaving through — t10 and t11 are unrelated distractors describing legacy AV and basic packet filtering, neither of which inspects data content.",
            "p6": "IDS is passive and detection-only by definition — it cannot act on the traffic it sees, which is precisely what distinguishes it from t7 (IPS).",
            "p7": "IPS's defining trait is inline placement with the automatic ability to block/drop traffic in real time, the direct opposite of IDS's passive, alert-only posture.",
            "p8": "A WAF is specifically application-layer aware, inspecting HTTP/HTTPS payload content for attacks like SQLi/XSS; t11 is the near-miss describing a basic Layer 3/4 firewall with no such application awareness.",
            "p9": "NAC's defining function is evaluating device identity/posture at the point of network admission (port or wireless) and quarantining non-compliant devices, distinct from any of the traffic-inspection or endpoint tools above.",
        },
        "explanation": (
            "The exam consistently pairs IDS/IPS (passive alert-only vs. active inline block) and EDR/XDR (single-host vs. "
            "cross-layer correlation) as near-miss traps. t10 and t11 exist purely as decoys: legacy AV is often mistaken "
            "for EDR because both run on the endpoint, and a plain packet-filtering firewall is often mistaken for a WAF "
            "because both sit 'in front of' something — but neither provides the defining capability the correct acronym does."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 1b. LOG ANALYSIS / INVESTIGATION — extra (triage disposition)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-011",
        "domain": 4,
        "objective": "4.4",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC analyst is triaging six SIEM alerts generated overnight. Classify each by its correct "
            "disposition after reviewing the full context provided."
        ),
        "categories": [
            {"id": "c1", "text": "Confirmed malicious — escalate to incident response"},
            {"id": "c2", "text": "Confirmed benign / expected activity — close as false positive"},
            {"id": "c3", "text": "Inconclusive — requires additional log correlation before a determination can be made"},
        ],
        "items": [
            {"id": "i1", "text": "User 'jsmith' authenticates successfully from Dallas at 9:02 AM, then again from Kyiv, Ukraine at 9:09 AM — a physically impossible travel velocity between the two logon locations, both using valid credentials, with no MFA challenge shown in the logs"},
            {"id": "i2", "text": "EDR flags a PowerShell execution on WKS-2209; review shows the command was 'Get-ADUser -Filter *', run by the help-desk technician's account during business hours, matching a documented, approved weekly AD-hygiene script that always runs from that exact workstation"},
            {"id": "i3", "text": "200 failed RDP logon attempts hit a single Internet-facing jump box within 3 minutes, from an IP with no prior history anywhere in the environment, followed by zero successful logons and then silence"},
            {"id": "i4", "text": "DLP flags an email from the CFO's account to an external personal Gmail address containing an attachment named 'Q3_board_deck.pptx'; the naming pattern has been seen before, but no baseline exists for whether this CFO has ever emailed personal accounts, and Legal has not yet responded to confirm whether this transfer was pre-authorized"},
            {"id": "i5", "text": "A service account used only by a nightly backup job authenticates interactively (console logon) at 2:47 AM from a workstation it has never used before, immediately followed by an attempt to add itself to the Domain Admins group"},
            {"id": "i6", "text": "A vulnerability scanner flags a missing patch on a server that, per an approved change-management ticket, was intentionally powered down and disconnected from the network three days ago for hardware replacement and remains fully offline"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c1", "i4": "c3", "i5": "c1", "i6": "c2"},
        "rationales": {
            "i1": "Two successful logons from geographically impossible locations minutes apart, with no MFA challenge recorded, is the classic 'impossible travel' indicator of a compromised credential in active use — this warrants immediate escalation, not a wait-and-see approach.",
            "i2": "Once the specific command, account, workstation, and schedule all match a pre-documented, approved administrative script, the alert is fully explained as expected activity and can be closed with confidence.",
            "i3": "Even with zero successful logons, 200 rapid-fire failed attempts from a never-before-seen source against an Internet-facing system is an active brute-force attack in progress and must be escalated for blocking and hardening, not dismissed simply because it didn't succeed.",
            "i4": "The alert lacks two things needed for a confident disposition: a behavioral baseline for this specific user and confirmation from Legal on authorization — until at least one of those gaps is closed, this cannot be responsibly labeled either malicious or benign.",
            "i5": "A service account interactively logging on from a new workstation and immediately attempting self-elevation to Domain Admins violates its expected behavior on every dimension (logon type, source, and privilege action) — this is a strong, unambiguous privilege-escalation indicator requiring escalation.",
            "i6": "Because the asset is confirmed offline and disconnected per an approved change ticket, the scan result reflects stale inventory data rather than any live exposure, making this a safe false-positive closure.",
        },
        "explanation": (
            "Not every alert resolves cleanly to malicious or benign on first review — i4 is intentionally built so that "
            "neither label is yet justified by the evidence, which is itself a realistic and testable SOC skill: knowing "
            "when to gather more information (a user baseline, a Legal confirmation) rather than forcing a premature call "
            "in either direction. Alerts should never be closed as benign, and never escalated as malicious, on data that "
            "doesn't actually establish it."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # 9b. ACRONYM / CONTROL MATCHING — extra (function classification)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqc-012",
        "domain": 4,
        "objective": "4.4",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "Classify each described control deployment by its PRIMARY function as configured. Read carefully — "
            "some controls are deployed in a mode that differs from their usual textbook classification."
        ),
        "categories": [
            {"id": "c1", "text": "Prevention (automatically blocks/stops malicious activity)"},
            {"id": "c2", "text": "Detection only (alerts but does not block)"},
            {"id": "c3", "text": "Response & orchestration (automates or coordinates remediation actions)"},
            {"id": "c4", "text": "Data-centric protection (focused specifically on protecting sensitive data, not general network/endpoint threats)"},
        ],
        "items": [
            {"id": "i1", "text": "A network access control (NAC) system automatically shunts a non-compliant laptop (missing AV updates) into a quarantine VLAN with no access to production resources, before the device can communicate with anything else"},
            {"id": "i2", "text": "An intrusion detection system (IDS) receives a mirrored copy of core-switch traffic and raises an alert on a matched signature, but has no ability to interrupt the session"},
            {"id": "i3", "text": "A SOAR platform, upon receiving a 'malware confirmed' alert from the EDR platform, automatically opens a ticket, isolates the affected host, and disables the associated user account — all without analyst intervention"},
            {"id": "i4", "text": "A DLP solution inspects an outbound email attachment, recognizes a pattern matching 40 unmasked Social Security numbers, and blocks the send before the message leaves the mail gateway"},
            {"id": "i5", "text": "An inline intrusion prevention system (IPS), positioned in the active traffic path, automatically drops any packet matching a signature for a known exploit kit, without waiting for a human decision"},
            {"id": "i6", "text": "A web application firewall (WAF) is deployed in monitor-only/alert mode during a staging rollout, logging suspicious requests for review but not yet blocking any traffic"},
            {"id": "i7", "text": "An XDR platform correlates a phishing email, a malicious macro execution, and an anomalous outbound connection into a single incident, and automatically triggers account lockout and network isolation across all three affected systems"},
            {"id": "i8", "text": "A DLP agent installed on endpoints blocks any attempt to copy files tagged 'Confidential' onto a USB drive, regardless of the file-system permissions otherwise granted to that user on that folder"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c1", "i6": "c2", "i7": "c3", "i8": "c4"},
        "rationales": {
            "i1": "The device automatically blocks the non-compliant device's access before any communication occurs, which is prevention, not merely alerting.",
            "i2": "By design this IDS receives only a mirrored copy of traffic and structurally cannot block anything — its function here is detection only, regardless of what signature matched.",
            "i3": "Automated ticket creation, host isolation, and account disablement triggered by an alert, without a human performing each step, is precisely response and orchestration — the SOAR layer, not the detection or prevention layer.",
            "i4": "The control's entire purpose is recognizing sensitive data content (SSNs) and stopping its egress, which is a data-centric protection function distinct from generic network or endpoint threat blocking.",
            "i5": "An inline device that automatically drops matching packets without human involvement is prevention by definition.",
            "i6": "Even though a WAF is normally thought of as a prevention tool, THIS deployment is explicitly configured in monitor-only/alert mode and is not blocking anything during the staging rollout — its function as configured right now is detection only, not prevention; classifying it by its usual reputation rather than its actual configuration is the trap here.",
            "i7": "Although XDR is often described loosely as a 'detection' tool, this specific deployment is described as automatically triggering account lockout and network isolation across systems — that is response and orchestration behavior, not passive detection, based on what it is actually doing in this scenario.",
            "i8": "Blocking copies specifically because of a data-classification tag, independent of the user's underlying file permissions, is a data-centric control acting on the sensitivity of the data itself, not a general endpoint or network protection.",
        },
        "explanation": (
            "i6 and i7 are the deliberate traps: a WAF and an XDR platform both have a 'usual' textbook category, but this "
            "item asks for classification by actual configured behavior in the scenario, not by acronym reputation. A WAF "
            "running in alert-only mode is not currently preventing anything, and an XDR platform that is explicitly "
            "described as auto-triggering isolation and lockout has moved beyond passive detection into orchestrated "
            "response — reading the specific behavior described, rather than pattern-matching on the acronym, is required "
            "to answer both correctly."
        ),
    },
]
