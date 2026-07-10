"""CompTIA Security+ SY0-701 Performance-Based Questions (PBQs), file B.

18 questions across domains 2, 3, 4, and 5, styled after Cyberkraft PBQ
simulations: egress/firewall rule matching and ordering, authentication-log
and email-authentication analysis, concrete incident-response sequences
(insider exfiltration, BEC wire fraud, cloud key leak, web-shell
eradication), and domain-5 vendor/risk/BIA/compliance classification.

Type breakdown: 6 pbq_matching, 6 pbq_ordering, 6 pbq_categorize.
Domain breakdown: D2 x3, D3 x4, D4 x6, D5 x5.
"""

QUESTIONS = [
    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 3 (4 questions) — firewall / egress-filtering / appliances
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqb-001",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A network engineer is writing egress-filtering rules on the internal-to-internet firewall. "
            "Match each business requirement to the single ACL rule that correctly implements it. One target "
            "is a distractor that should NOT be used."
        ),
        "prompts": [
            {"id": "p1", "text": "Allow all internal workstations (10.20.0.0/16) outbound HTTPS access for general web browsing"},
            {"id": "p2", "text": "Allow only the patch management server (10.20.5.5) to reach the vendor's update repository at 198.51.100.20 over HTTPS"},
            {"id": "p3", "text": "Block all outbound traffic from the internal network to a threat-intel-flagged malicious range, on any port"},
            {"id": "p4", "text": "Allow the internal DNS resolver (10.20.1.53) to forward queries to the upstream public resolver 1.1.1.1, DNS only"},
        ],
        "targets": [
            {"id": "t1", "text": "PERMIT TCP 10.20.0.0/16 -> any:443"},
            {"id": "t2", "text": "PERMIT TCP 10.20.5.5 -> 198.51.100.20:443"},
            {"id": "t3", "text": "DENY IP 10.20.0.0/16 -> 203.0.113.0/24:any"},
            {"id": "t4", "text": "PERMIT UDP 10.20.1.53 -> 1.1.1.1:53"},
            {"id": "t5", "text": "PERMIT TCP 10.20.0.0/16 -> 198.51.100.20:443"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "t1 permits TCP/443 from the entire workstation subnet to any destination, matching general outbound HTTPS browsing.",
            "p2": "t2 scopes the permit to exactly one source host and one destination host/port, matching 'only the patch server, only that repo.'",
            "p3": "t3 denies all IP traffic on any port from the internal network to the flagged range, matching the 'any port' blanket-block requirement.",
            "p4": "t4 permits only UDP/53 from the resolver to the specific upstream IP, matching the DNS-only scope.",
        },
        "explanation": (
            "t5 is the distractor: it permits the ENTIRE workstation subnet to reach the vendor repository, not just the patch "
            "server. Candidates who pattern-match on 'destination 198.51.100.20:443' without checking the source scope will "
            "incorrectly select t5 instead of the correctly-scoped t2 — the same source-scope trap tested from the opposite "
            "direction (inbound to a DMZ host) in the firewall matching item in file A."
        ),
    },
    {
        "id": "npbqb-002",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "An engineer inherited the following egress ACL from an internal network to the internet, listed in "
            "no particular order. Reorder the rules into the correct evaluation order so specific/security-critical "
            "rules take effect before general ones and the implicit/explicit deny sits last."
        ),
        "items": [
            {"id": "i1", "text": "PERMIT TCP 10.20.0.0/16 -> any:443  (general outbound HTTPS for all workstations)"},
            {"id": "i2", "text": "DENY IP 10.20.0.0/16 -> 203.0.113.0/24:any  (block known-malicious destination range, any port)"},
            {"id": "i3", "text": "PERMIT TCP 10.20.5.5 -> 198.51.100.20:443  (patch server to vendor update repo)"},
            {"id": "i4", "text": "DENY IP any -> any  (implicit/explicit deny all)"},
            {"id": "i5", "text": "PERMIT UDP 10.20.1.53 -> 1.1.1.1:53  (internal DNS resolver to public resolver)"},
            {"id": "i6", "text": "DENY TCP 10.20.0.0/16 -> any:6667  (block outbound IRC, a legacy C2 channel)"},
        ],
        "answer": ["i2", "i3", "i5", "i6", "i1", "i4"],
        "rationales": {
            "i2": "The malicious-range block must be evaluated first: it overlaps port 443 with the general HTTPS permit (i1), so if i1 were evaluated first, traffic to that range over port 443 would be wrongly permitted before the deny is ever reached.",
            "i3": "The single-host patch-server permit is narrower than the general HTTPS permit that follows it; specific host/port permits are conventionally placed ahead of broad allow rules for auditability even though, here, both are permits and don't strictly conflict.",
            "i5": "The DNS-only permit is a narrow, single-purpose rule for a different protocol/port than the general HTTPS rule, so it is grouped with the other specific rules ahead of the broad permit.",
            "i6": "The explicit IRC block is a security-relevant deny; grouping it with the other specific/critical rules ahead of the general HTTPS permit guarantees it is never accidentally buried below a future broadened allow rule, even though today's ports don't overlap.",
            "i1": "Only after every rule that needed to intercept specific traffic (the malicious-range block and the narrow permits) has been placed does the broad 'permit HTTPS for everyone' rule belong, since it is the most general permit in the set.",
            "i4": "The deny-all must always be the final rule, catching any traffic (e.g., non-HTTPS, non-DNS protocols) not matched by an earlier, more specific rule.",
        },
        "explanation": (
            "The critical dependency is i2 before i1: both touch port 443, and first-match-wins means the more specific "
            "destination-based deny has to be evaluated before the broad 'any destination' permit or it would be shadowed, "
            "letting traffic reach a known-malicious range disguised as ordinary HTTPS. Rules that don't overlap in scope (i3, "
            "i5, i6 relative to each other) are still ordered specific-to-general by convention, ending in the explicit deny-all."
        ),
    },
    {
        "id": "npbqb-003",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A network architect is documenting the function of each appliance in the security stack ahead of a "
            "topology review. Classify each device by the single category that best matches its described behavior."
        ),
        "categories": [
            {"id": "c1", "text": "Next-generation firewall (NGFW)"},
            {"id": "c2", "text": "Intrusion prevention system (IPS)"},
            {"id": "c3", "text": "Load balancer"},
            {"id": "c4", "text": "Forward proxy"},
            {"id": "c5", "text": "Web application firewall (WAF)"},
            {"id": "c6", "text": "Intrusion detection system (IDS)"},
        ],
        "items": [
            {"id": "i1", "text": "A device sits inline in front of a public web application and inspects HTTP/HTTPS requests specifically for SQL injection and XSS payloads, blocking malicious requests before they reach the application server"},
            {"id": "i2", "text": "A device distributes incoming client connections across four identical backend web servers based on current load and health checks, improving availability and response time"},
            {"id": "i3", "text": "A device sits inline on the network path and automatically drops packets matching a known exploit signature the instant it detects them, without waiting for administrator action"},
            {"id": "i4", "text": "A single appliance combines traditional port/protocol filtering with application-layer awareness (identifying an application regardless of the port it uses) and integrated threat-intelligence feeds"},
            {"id": "i5", "text": "A device sits between internal users and the internet, intercepting all outbound web requests to enforce acceptable-use policy, cache frequently requested content, and hide internal client IP addresses from external sites"},
            {"id": "i6", "text": "A device receives a mirrored copy of network traffic from a SPAN port, analyzes it against known attack signatures, and generates an alert — but because it only sees a copy of the traffic, it cannot itself block or drop the malicious packets"},
        ],
        "answer": {"i1": "c5", "i2": "c3", "i3": "c2", "i4": "c1", "i5": "c4", "i6": "c6"},
        "rationales": {
            "i1": "Inspecting application-layer HTTP(S) requests for injection/XSS payloads aimed at a specific web application is the defining function of a WAF, distinct from network-layer devices.",
            "i2": "Distributing connections across backend servers by load and health is the core function of a load balancer, not a security-inspection device.",
            "i3": "Sitting inline and automatically dropping matched traffic in real time is what distinguishes an IPS from an IDS — the 'P' means it actively prevents, not just alerts.",
            "i4": "Combining traditional filtering with application awareness and threat intelligence in one appliance is the defining trait of an NGFW.",
            "i5": "Intercepting outbound requests, enforcing acceptable-use policy, caching, and masking internal client IPs describes a forward proxy acting on behalf of internal clients.",
            "i6": "Working from a mirrored copy of traffic and only alerting — never blocking — is the defining, exam-favorite distinction between an IDS (detects, cannot act) and an IPS (inline, can drop).",
        },
        "explanation": (
            "The IDS/IPS pair (i3 vs. i6) is the classic discriminator: both use signatures, but placement (inline vs. a mirrored "
            "SPAN-port copy) determines whether the device can actually block traffic. WAF is scoped to application-layer web "
            "attacks specifically, while NGFW is a broader, multi-layer appliance; load balancer and forward proxy serve "
            "availability and outbound-policy functions rather than threat detection."
        ),
    },
    {
        "id": "npbqb-004",
        "domain": 3,
        "objective": "3.2",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A network architect must select the correct secure-communication technology for each requirement. "
            "Match each requirement to the single best-fitting technology. One target is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "Give remote employees full network-layer access to internal resources as if their laptop were plugged into the corporate LAN, via installed client software"},
            {"id": "p2", "text": "Securely connect two branch-office networks over the public internet so traffic between the two LANs is encrypted, without requiring any per-user client software"},
            {"id": "p3", "text": "Encrypt web traffic between a customer's browser and an e-commerce checkout page, including a certificate that proves the site's identity to the browser"},
            {"id": "p4", "text": "Provide remote access without a heavyweight installed client, letting users reach a limited set of internal web applications through a standard browser portal"},
            {"id": "p5", "text": "Establish network-layer encryption and mutual authentication between two hosts using ESP for confidentiality and AH for integrity, operating below the transport layer"},
        ],
        "targets": [
            {"id": "t1", "text": "Remote-access VPN (client-based)"},
            {"id": "t2", "text": "Site-to-site VPN"},
            {"id": "t3", "text": "Transport Layer Security (TLS)"},
            {"id": "t4", "text": "Clientless SSL/TLS VPN portal"},
            {"id": "t5", "text": "IPsec (ESP/AH)"},
            {"id": "t6", "text": "Secure Access Service Edge (SASE)"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "A client-based remote-access VPN is what places a single remote user's device onto the corporate network at layer 3 via installed software.",
            "p2": "A site-to-site VPN encrypts a gateway-to-gateway tunnel between two networks and requires no client software on individual end-user devices.",
            "p3": "TLS is the protocol that encrypts a single browser-to-server session and carries the certificate used to verify the site's identity.",
            "p4": "A clientless SSL/TLS VPN portal delivers browser-based access to specific internal web apps without installing a full VPN client, unlike t1.",
            "p5": "IPsec's ESP (confidentiality) and AH (integrity) operating at the network layer is the textbook description of IPsec itself, distinct from the transport-layer TLS in p3.",
        },
        "explanation": (
            "t6 (SASE) is the distractor: SASE is a cloud-delivered architecture that bundles networking and security services "
            "(including VPN/SD-WAN and security functions), but it is not itself an encryption protocol matching any single "
            "requirement here. The client vs. clientless VPN distinction (p1 vs. p4) and the TLS-vs-IPsec layer distinction "
            "(p3 vs. p5) are the two most commonly confused pairs in this objective."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 2 (3 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqb-005",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A SOC analyst pulls six authentication-log excerpts flagged by an anomaly-detection rule. Classify "
            "each excerpt by the pattern it represents."
        ),
        "categories": [
            {"id": "c1", "text": "Brute force (single account, many passwords)"},
            {"id": "c2", "text": "Password spraying (many accounts, one/few passwords)"},
            {"id": "c3", "text": "Credential stuffing (breached username/password pairs)"},
            {"id": "c4", "text": "Normal/benign authentication activity"},
        ],
        "items": [
            {"id": "i1", "text": "auth.log: 14,822 failed login attempts against account 'admin' from a single IP within 10 minutes, using a sequential wordlist (password1, password2, password3...)"},
            {"id": "i2", "text": "auth.log: three successful logins for account 'jsmith', all from the same Chicago-area IP, all during normal business hours over one week, each preceded by a single correctly entered password"},
            {"id": "i3", "text": "auth.log: 600 distinct usernames, each attempted exactly once with the password 'Password123!', originating from 40 different IPs consistent with a botnet, across a two-hour window"},
            {"id": "i4", "text": "auth.log: 50,000 login attempts using 50,000 unique username/password pairs sourced from a known third-party breach dump, each account tried exactly once with its own unique breached password, achieving a 0.4% success rate"},
            {"id": "i5", "text": "auth.log: account 'dbadmin' receives 25,000 failed login attempts within 5 minutes from a single IP, cycling through a dictionary wordlist against that one account only"},
            {"id": "i6", "text": "auth.log: account 'rjones' logs one failed attempt (fat-fingered password) immediately followed by one successful login, from the same IP that has authenticated as rjones every workday for the past 90 days"},
        ],
        "answer": {"i1": "c1", "i2": "c4", "i3": "c2", "i4": "c3", "i5": "c1", "i6": "c4"},
        "rationales": {
            "i1": "Many password guesses against one single account from one source is the definition of brute force.",
            "i2": "A consistent user/location/time pattern with correct credentials on each attempt is ordinary, expected authentication activity.",
            "i3": "One attempt per account, across hundreds of accounts, all using the same single password from many distributed sources is the signature of password spraying — it avoids per-account lockouts by never repeating attempts against one account.",
            "i4": "Unique username/password pairs per attempt, sourced from a breach dump, with a low but nonzero success rate from reused passwords, is the definition of credential stuffing — distinct from spraying because each pair is a real (breached) credential, not a single guessed password reused across accounts.",
            "i5": "A second brute-force example: very high volume of password guesses concentrated on one account from one source.",
            "i6": "A single mistyped password followed immediately by a successful login, from a device/location with 90 days of consistent prior success, is normal user error, not an attack pattern.",

        },
        "explanation": (
            "The four-way split hinges on two axes: how many accounts are targeted (one vs. many) and where the passwords "
            "came from (a guessed list vs. real breached pairs). Brute force = one account, many guesses; spraying = many "
            "accounts, one guessed password; stuffing = many accounts, each with its OWN previously-breached password. i6's "
            "single failed-then-succeeded attempt is a common false-positive trap that should not be classified as brute force."
        ),
    },
    {
        "id": "npbqb-006",
        "domain": 2,
        "objective": "2.1",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A threat intelligence analyst is profiling five recent incidents. Match each scenario to the single "
            "best-fitting threat actor type. One target is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "A well-resourced group runs a multi-year, low-noise campaign against a defense contractor, using custom zero-day tooling and patient lateral movement to steal intellectual property without being detected"},
            {"id": "p2", "text": "A former employee, terminated two weeks earlier, uses credentials that were never disabled to log into the file server after hours and deletes several project folders out of spite"},
            {"id": "p3", "text": "A group defaces a company's website and posts a manifesto after the company was linked to a controversial project, stating the attack was meant to 'raise awareness,' not to profit"},
            {"id": "p4", "text": "An attacker with minimal technical skill downloads a publicly available exploit kit from a forum and runs it against random internet-facing IP ranges without understanding how it works"},
            {"id": "p5", "text": "A criminal group encrypts a hospital's systems and demands a $2 million cryptocurrency ransom, having chosen the target because it judged the hospital would pay quickly to restore patient-care systems"},
        ],
        "targets": [
            {"id": "t1", "text": "Nation-state / advanced persistent threat (APT) actor"},
            {"id": "t2", "text": "Insider threat"},
            {"id": "t3", "text": "Hacktivist"},
            {"id": "t4", "text": "Script kiddie / unskilled attacker"},
            {"id": "t5", "text": "Organized crime"},
            {"id": "t6", "text": "Competitor conducting corporate espionage"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "Extended timeline, custom zero-day tooling, and patience aimed at intellectual-property theft from a defense contractor are the resourcing and motivation hallmarks of a nation-state APT rather than a competitor.",
            "p2": "Access from a still-valid former-employee credential used for malicious deletion is the definition of an insider threat.",
            "p3": "Ideological motivation ('raise awareness') rather than financial or espionage motivation is the defining trait of a hacktivist.",
            "p4": "Using a prepackaged, publicly available tool without understanding it, against untargeted victims, is the definition of a script kiddie/unskilled attacker.",
            "p5": "Targeting selected for likely, fast ransom payment, for financial gain, by an organized group is the hallmark of organized crime rather than ideological or state motivation.",
        },
        "explanation": (
            "t6 is the distractor: corporate espionage by a competitor is plausible-sounding for p1's IP-theft scenario, but the "
            "combination of custom zero-day tooling, extreme patience, and a defense-sector target is far more consistent with "
            "nation-state resourcing and motive than with a private competitor. APT vs. organized crime is the other key "
            "distinction: both are well-resourced, but organized crime is financially motivated while APTs pursue "
            "espionage/strategic advantage."
        ),
    },
    {
        "id": "npbqb-007",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "A malware analyst is writing up behavioral summaries from a recent sandbox detonation batch. "
            "Classify each description by the malware type it represents."
        ),
        "categories": [
            {"id": "c1", "text": "Ransomware"},
            {"id": "c2", "text": "Worm"},
            {"id": "c3", "text": "Rootkit"},
            {"id": "c4", "text": "Logic bomb"},
            {"id": "c5", "text": "Trojan"},
        ],
        "items": [
            {"id": "i1", "text": "Malware encrypts every file on the finance share and displays a countdown timer demanding cryptocurrency payment before files are permanently deleted"},
            {"id": "i2", "text": "A vulnerable SMB service allows the malware to self-propagate across the network with no user interaction, infecting over 200 hosts in under an hour"},
            {"id": "i3", "text": "Forensic analysis finds kernel-mode code that hooks system calls to hide a malicious process from Task Manager and antivirus scans, even while that process is actively running"},
            {"id": "i4", "text": "A disgruntled developer embeds code in the payroll application that silently wipes the entire employee database the moment their own account is ever removed from the HR system"},
            {"id": "i5", "text": "An email attachment disguised as a legitimate invoice-viewer application actually installs a remote-access backdoor when run, while displaying a fake 'file is corrupted' error to appear harmless"},
            {"id": "i6", "text": "A 'free' PDF-to-Word converter downloaded from a torrent site secretly installs a keylogger and a hidden remote-access tool alongside the advertised (and functional) conversion feature"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c5", "i6": "c5"},
        "rationales": {
            "i1": "Encrypting files and demanding payment under threat of deletion is the defining behavior of ransomware.",
            "i2": "Self-propagation across a network through a vulnerability, with no user interaction required, is the defining behavior of a worm.",
            "i3": "Kernel-level hooking that hides an active process from standard tools is the defining behavior of a rootkit.",
            "i4": "Code that remains dormant until a specific triggering condition (the account being removed) is the definition of a logic bomb.",
            "i5": "Malware disguised as a legitimate, seemingly useful program that instead delivers a hidden malicious payload is the definition of a trojan.",
            "i6": "A second trojan example: a program that appears to perform its advertised function while secretly bundling malicious tools is still a trojan regardless of the delivery channel (torrent vs. email).",
        },
        "explanation": (
            "The discriminators are propagation method (worm = self-spreading, no user action) versus disguise (trojan = "
            "poses as something legitimate and requires the user to run it) versus stealth (rootkit = hides existing "
            "compromise) versus trigger condition (logic bomb = dormant until a specific event) versus impact/intent "
            "(ransomware = extortion via encryption)."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 4 (6 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqb-008",
        "domain": 4,
        "objective": "4.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A messaging administrator reviews four Authentication-Results header lines from recently delivered "
            "mail. Match each header to the conclusion it supports about the message's authenticity."
        ),
        "prompts": [
            {"id": "p1", "text": "spf=fail (sender IP not in SPF record) smtp.mailfrom=attacker.com; dkim=none; dmarc=fail action=reject header.from=company.com"},
            {"id": "p2", "text": "spf=pass smtp.mailfrom=news.company.com; dkim=pass header.d=company.com; dmarc=pass action=none header.from=company.com"},
            {"id": "p3", "text": "spf=pass smtp.mailfrom=vendor-billing.net; dkim=none; dmarc=fail action=quarantine header.from=company.com"},
            {"id": "p4", "text": "spf=softfail smtp.mailfrom=company.com; dkim=pass header.d=company.com; dmarc=pass action=none header.from=company.com"},
        ],
        "targets": [
            {"id": "t1", "text": "Forged email correctly rejected — the sending IP was unauthorized, no valid signature existed, and DMARC enforcement blocked delivery"},
            {"id": "t2", "text": "Legitimate, fully authenticated message — sending infrastructure, signature, and domain alignment all pass, delivered normally"},
            {"id": "t3", "text": "Envelope/header domain mismatch — the sending domain itself passes SPF, but it does not align with the visible From: domain, so DMARC correctly quarantines it as likely spoofing"},
            {"id": "t4", "text": "Message passed despite a marginal SPF result because a valid, aligned DKIM signature let DMARC pass anyway — DKIM alignment can compensate for an SPF softfail"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "SPF fail, no DKIM signature, and a DMARC reject action together describe a forged message that authentication correctly stopped.",
            "p2": "All three checks pass and are aligned to the same company.com domain, describing a fully legitimate, properly authenticated message.",
            "p3": "The envelope-from domain (vendor-billing.net) passes SPF on its own, but the visible From: header claims company.com — that misalignment is exactly what causes DMARC to fail and quarantine even though SPF itself passed.",
            "p4": "DMARC passes if EITHER SPF or DKIM aligns; here SPF only softfails (a weak signal) but DKIM passes and aligns with the From domain, which is sufficient for DMARC to pass overall.",
        },
        "explanation": (
            "DMARC does not require both SPF and DKIM to pass — it requires that at least one of them pass AND align with the "
            "visible From: domain. p3 and p4 test that nuance directly: p3 shows an SPF pass that still fails DMARC due to "
            "misalignment, while p4 shows a weak SPF result that still passes DMARC because DKIM alignment covered for it."
        ),
    },
    {
        "id": "npbqb-009",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A DLP alert flags an employee uploading a large volume of proprietary design files to a personal "
            "cloud-storage account shortly after applying for a competitor's job. Order the insider-threat "
            "investigation steps as they must be carried out."
        ),
        "items": [
            {"id": "i1", "text": "Confirm the DLP alert is valid (not a false positive) by reviewing the flagged transfer's file names, size, and destination"},
            {"id": "i2", "text": "Engage HR and Legal to authorize continued monitoring/investigation of the employee under the insider-threat policy before any invasive steps are taken"},
            {"id": "i3", "text": "Covertly preserve the employee's endpoint forensic image and relevant logs (USB, cloud upload, email, print) before the employee becomes aware of the investigation"},
            {"id": "i4", "text": "Restrict the employee's access to sensitive systems and revoke remote data-transfer capabilities (disable USB, block the personal cloud-storage domain)"},
            {"id": "i5", "text": "Review the employee's historical access patterns and the data classification of the exfiltrated files to determine sensitivity and scope"},
            {"id": "i6", "text": "Interview the employee, with HR/Legal present, once evidence is secured and access has been contained"},
            {"id": "i7", "text": "Document findings, determine appropriate disciplinary/legal action, and update DLP policies and egress rules to prevent recurrence"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "The alert must first be validated as a real, sensitive transfer before an insider-threat investigation is opened at all.",
            "i2": "Insider investigations touch employment and legal risk, so HR/Legal authorization must be obtained before any deeper monitoring or evidence collection proceeds.",
            "i3": "Evidence is preserved covertly next, while the employee is still unaware, so nothing can be destroyed or altered once they realize they are under investigation.",
            "i4": "Only after evidence is secured is access restricted — restricting access first risks tipping off the employee before critical evidence has been captured.",
            "i5": "With evidence preserved and further transfer blocked, the team determines exactly how sensitive the exfiltrated data was and how far the exposure extends.",
            "i6": "The employee interview happens only after evidence and scope are established, so investigators can ask informed questions and are not relying on the employee's own account first.",
            "i7": "Documentation, disciplinary/legal action, and policy updates are the final step, closing out the case using everything gathered in the prior steps.",
        },
        "explanation": (
            "Insider investigations flip the usual 'contain first' instinct: because tipping off the subject can cause evidence "
            "destruction or retaliation, covert evidence preservation (i3) must happen BEFORE any access restriction that the "
            "employee would notice (i4) — the opposite order used in an external malware incident, where isolating the host "
            "happens immediately."
        ),
    },
    {
        "id": "npbqb-010",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "The finance department wired $340,000 to what it believed was a vendor's updated bank account, "
            "following an email that appeared to come from the CEO. The transfer was sent 25 minutes ago and is "
            "now confirmed fraudulent. Order the response actions."
        ),
        "items": [
            {"id": "i1", "text": "Immediately call the sending bank to request an emergency wire recall/hold before the funds move further at the receiving institution"},
            {"id": "i2", "text": "File a report with law enforcement (e.g., FBI IC3) and the receiving bank's fraud department to support the recall request"},
            {"id": "i3", "text": "Preserve the fraudulent email with full headers and all related correspondence for forensic and law-enforcement review"},
            {"id": "i4", "text": "Determine whether the CEO's or finance staff's mailbox was actually compromised (account takeover) versus the message merely being spoofed, by reviewing mail flow and authentication logs"},
            {"id": "i5", "text": "If account takeover is confirmed, reset credentials, revoke active sessions, and review the affected mailbox for attacker-created forwarding rules"},
            {"id": "i6", "text": "Brief finance staff and implement/reinforce out-of-band callback verification for all future wire-transfer requests"},
            {"id": "i7", "text": "Document the full incident timeline and financial impact for the cyber-insurance claim and executive/board reporting"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "In wire fraud, every minute matters for a possible recall, so the time-critical bank call happens before any other step, even evidence preservation.",
            "i2": "Law enforcement and the receiving bank's fraud desk are engaged immediately after the recall request to maximize the chance of freezing the funds while they're still traceable.",
            "i3": "With the financial recall effort underway, the fraudulent email and related messages are preserved for the forensic and law-enforcement review that will follow.",
            "i4": "Once evidence is secured, investigators determine whether an actual mailbox compromise occurred or the message was simply spoofed, which changes the containment steps needed.",
            "i5": "Only if takeover is confirmed does credential reset and session revocation happen — this is a conditional containment step that depends on the outcome of i4.",
            "i6": "Process and training reinforcement (callback verification) follows once the technical investigation is resolved, addressing the human-process gap that enabled the fraud.",
            "i7": "Documentation for insurance and leadership reporting is the final step, capturing financial impact and the full timeline.",
        },
        "explanation": (
            "BEC wire fraud is the one incident type where the FIRST action is a financial/banking action rather than a "
            "technical containment or evidence-preservation step, because wire recalls have a narrow time window that closes "
            "within hours. This is a deliberate contrast to the insider-exfiltration and ransomware sequences, where technical "
            "containment or evidence capture comes first."
        ),
    },
    {
        "id": "npbqb-011",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A developer accidentally committed a cloud-provider API key with broad administrative permissions to "
            "a public GitHub repository. Automated scanning shows the key was scraped and used from an unfamiliar "
            "region within minutes. Order the response."
        ),
        "items": [
            {"id": "i1", "text": "Immediately deactivate/revoke the exposed access key in the cloud provider's IAM console so it can no longer authenticate"},
            {"id": "i2", "text": "Review the cloud audit log (e.g., CloudTrail) for all API activity performed with the leaked key to determine what actions the attacker took"},
            {"id": "i3", "text": "Identify and terminate/roll back any unauthorized resources the attacker created with the compromised key (rogue instances, IAM users, storage buckets)"},
            {"id": "i4", "text": "Rotate any other credentials/secrets that were exposed in the same repository or reachable via the compromised key's permissions"},
            {"id": "i5", "text": "Purge the key from the full git history (not just the latest commit) and invalidate any cached/forked copies of the repository"},
            {"id": "i6", "text": "Require secret-scanning on the repository and issue scoped, least-privilege keys going forward instead of broad administrative keys"},
            {"id": "i7", "text": "Document the incident and notify affected customers or stakeholders if attacker activity touched shared or production resources"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Revoking the key first stops any further unauthorized use immediately, before anything else is investigated or cleaned up.",
            "i2": "With the key dead, the team reviews the audit log to establish exactly what the attacker did while the key was live.",
            "i3": "Knowing what the attacker did, the team can now identify and remove/roll back any unauthorized resources they created.",
            "i4": "Because the leaked key or its permissions may have exposed other secrets, those are rotated next to close any secondary exposure.",
            "i5": "Purging the key from git history is a hygiene step that can follow remediation, since the key is already revoked and cannot be used even if it's still recoverable from history — but it must still be removed to prevent confusion and future accidental reuse.",
            "i6": "Preventive controls (secret scanning, least-privilege key issuance) are implemented once the immediate incident is fully remediated.",
            "i7": "Documentation and any required notification are the final step, once scope and impact are fully known.",
        },
        "explanation": (
            "The key insight is that revocation (i1) — not evidence review — is the very first action, because a live, "
            "over-privileged cloud credential represents ongoing, escalating exposure every second it remains valid. Only "
            "after the credential is dead does the investigation proceed to scope, cleanup, and prevention."
        ),
    },
    {
        "id": "npbqb-012",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A SOC discovers a web shell (a suspicious .aspx file) on a public-facing IIS server, granting an "
            "attacker remote command execution. Order the eradication process."
        ),
        "items": [
            {"id": "i1", "text": "Isolate the web server at the network layer (remove from the load balancer, block inbound/outbound except forensic access) while keeping it powered on"},
            {"id": "i2", "text": "Preserve a forensic disk image and capture running process/memory state before making further changes"},
            {"id": "i3", "text": "Identify the initial access vector (e.g., an unpatched CMS plugin) and every file the attacker created or modified, using file-integrity and timestamp analysis"},
            {"id": "i4", "text": "Determine what commands were executed through the web shell and whether the attacker pivoted to other internal hosts, using web-server logs and EDR/network telemetry"},
            {"id": "i5", "text": "Remove the web shell and any other attacker-planted backdoors or scheduled tasks, then patch the vulnerability that allowed initial access"},
            {"id": "i6", "text": "Rebuild the web server from a known-good image rather than trusting the cleaned host, and restore content from a verified pre-compromise backup"},
            {"id": "i7", "text": "Return the rebuilt server to production behind updated WAF rules and monitoring tuned to detect the same web-shell signature, then conduct a post-incident review"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Isolating the server first stops further attacker access while preserving disk state for forensics, without powering it off.",
            "i2": "Volatile evidence is captured immediately after isolation, before any cleanup activity can overwrite process or memory artifacts.",
            "i3": "With evidence preserved, investigators identify how the attacker got in and every file they touched, establishing the full footprint.",
            "i4": "Understanding command execution and any lateral movement extends the scope investigation before cleanup begins, so no other compromised host is missed.",
            "i5": "Eradication — removing the shell/backdoors and patching the entry vector — happens only once the full scope is known, so cleanup isn't undone by a persistence mechanism found later.",
            "i6": "Rebuilding from a known-good image rather than trusting a manually cleaned host guards against any backdoor the investigation may have missed.",
            "i7": "The server returns to production last, hardened with updated detection, followed by the post-incident review.",
        },
        "explanation": (
            "This mirrors the general contain -> preserve evidence -> scope -> eradicate -> recover -> harden pattern, but "
            "with a web-shell-specific emphasis: eradication is never trusted alone — the host is rebuilt from a known-good "
            "image (i6) rather than relying on manual removal of the shell (i5), since web shells are frequently paired with "
            "additional, less obvious backdoors."
        ),
    },
    {
        "id": "npbqb-013",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A SOC manager is mapping recent incident-handling actions to the correct phase of the incident "
            "response lifecycle for a post-incident training deck. Classify each action by its phase."
        ),
        "categories": [
            {"id": "c1", "text": "Preparation"},
            {"id": "c2", "text": "Detection & Analysis"},
            {"id": "c3", "text": "Containment"},
            {"id": "c4", "text": "Eradication"},
            {"id": "c5", "text": "Recovery"},
            {"id": "c6", "text": "Post-Incident Activity (lessons learned)"},
        ],
        "items": [
            {"id": "i1", "text": "The security team maintains an up-to-date incident response plan, runs quarterly tabletop exercises, and ensures the EDR agent is deployed to 100% of endpoints before any incident occurs"},
            {"id": "i2", "text": "A SIEM correlation rule fires; the analyst triages the alert, confirms it represents true malicious activity, and determines its severity and scope"},
            {"id": "i3", "text": "The team disables the compromised account's network access and segments the infected VLAN from the rest of the network while the investigation continues"},
            {"id": "i4", "text": "The team removes the malware, closes the vulnerability that was exploited, and confirms via scanning that no backdoors remain on any affected host"},
            {"id": "i5", "text": "The team restores affected systems from clean backups, returns them to production, and closely monitors them for signs of reinfection"},
            {"id": "i6", "text": "Two weeks after the incident is closed, the team holds a retrospective meeting, documents what worked and what didn't, and updates the IR playbook and detection rules accordingly"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c5", "i6": "c6"},
        "rationales": {
            "i1": "Building readiness before any incident happens — plans, exercises, and tooling deployment — is the Preparation phase.",
            "i2": "Triaging an alert and confirming/scoping true malicious activity is Detection & Analysis, before any action is taken against the threat itself.",
            "i3": "Actively limiting the spread of a confirmed incident (disabling access, segmenting a VLAN) is Containment.",
            "i4": "Removing the malware and the root cause and verifying no backdoors remain is Eradication, distinct from merely stopping the spread.",
            "i5": "Restoring systems to production and monitoring for reinfection is Recovery, which happens only after eradication is confirmed complete.",
            "i6": "A retrospective held after closure, focused on improving the plan and detections going forward, is Post-Incident Activity.",
        },
        "explanation": (
            "This is the standard NIST SP 800-61 lifecycle (Preparation; Detection & Analysis; Containment, Eradication & "
            "Recovery; Post-Incident Activity). The exam frequently tests whether candidates can tell containment (stop the "
            "bleeding) apart from eradication (remove the cause) apart from recovery (bring it back safely) — three distinct "
            "phases that are often collapsed together in casual usage."
        ),
    },

    # ══════════════════════════════════════════════════════════════════
    # DOMAIN 5 (5 questions)
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "npbqb-014",
        "domain": 5,
        "objective": "5.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "Procurement wants to onboard a new SaaS vendor that will process regulated customer data. Order the "
            "vendor risk management workflow from initial request through ongoing oversight."
        ),
        "items": [
            {"id": "i1", "text": "Conduct a business needs assessment and confirm no existing approved vendor already provides the required capability"},
            {"id": "i2", "text": "Distribute a vendor security questionnaire and request evidence of relevant certifications/attestations (e.g., SOC 2 Type II, ISO 27001)"},
            {"id": "i3", "text": "Perform a risk assessment of the vendor based on the questionnaire responses, the sensitivity of the data involved, and the vendor's compliance posture"},
            {"id": "i4", "text": "Negotiate and execute contractual protections — SLA, data processing agreement, right-to-audit clause, and breach-notification terms"},
            {"id": "i5", "text": "Formally approve the vendor and add it to the organization's vendor risk register with an assigned risk owner and review cadence"},
            {"id": "i6", "text": "Provision the vendor with least-privilege access and configure integration/data-flow controls (encryption, API scoping) before production data is shared"},
            {"id": "i7", "text": "Conduct periodic reassessment (e.g., annually or at contract renewal) and monitor the vendor for security incidents or SLA breaches throughout the relationship"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Confirming the need and ruling out an existing approved vendor happens before any vendor-specific evaluation begins.",
            "i2": "Gathering the vendor's own security evidence is the first data-collection step once a specific vendor is being considered.",
            "i3": "The formal risk assessment can only be performed once questionnaire evidence and data sensitivity are known.",
            "i4": "Contractual protections are negotiated once the risk assessment confirms the relationship is acceptable to pursue, translating risk findings into binding terms.",
            "i5": "Formal approval and registration happen once contracts are signed, giving the vendor an accountable owner and a defined review cadence going forward.",
            "i6": "Technical provisioning with least-privilege access happens after formal approval, as the implementation step that puts the approved relationship into production.",
            "i7": "Ongoing reassessment and monitoring is the final, continuous step that spans the life of the vendor relationship after go-live.",
        },
        "explanation": (
            "Vendor onboarding follows assess-need -> gather-evidence -> assess-risk -> contract -> approve/register -> "
            "provision -> monitor. A common mistake is provisioning technical access before the vendor is formally approved "
            "and registered, which leaves production data flowing to a vendor with no assigned risk owner of record."
        ),
    },
    {
        "id": "npbqb-015",
        "domain": 5,
        "objective": "5.2",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A risk committee reviews six proposed responses to newly identified risks. Classify each response by "
            "the risk management strategy it represents."
        ),
        "categories": [
            {"id": "c1", "text": "Avoid"},
            {"id": "c2", "text": "Transfer"},
            {"id": "c3", "text": "Mitigate"},
            {"id": "c4", "text": "Accept"},
        ],
        "items": [
            {"id": "i1", "text": "After discovering a legacy VPN concentrator has a known unpatched vulnerability with no available patch, the security team decommissions it entirely and migrates remote access to a modern ZTNA solution"},
            {"id": "i2", "text": "The organization purchases a cyber-liability insurance rider specifically covering regulatory fines resulting from a potential data breach"},
            {"id": "i3", "text": "A finding shows the marketing team's cloud storage bucket allows public read access; the team applies a policy restricting access to authenticated internal roles and enables access logging"},
            {"id": "i4", "text": "The board reviews a finding that a rarely used internal reporting tool has a low-severity XSS flaw affecting only three internal analysts; given the low likelihood/impact and the remediation cost, leadership formally signs off on taking no further action and documents the decision"},
            {"id": "i5", "text": "Rather than build and operate an in-house SMS gateway for MFA, which would require additional telecom compliance overhead, the company contracts a specialized MFA-as-a-service provider that assumes operational and compliance responsibility for that function"},
            {"id": "i6", "text": "A proposed product feature requiring collection of biometric data in a jurisdiction with strict biometric-privacy law is dropped from the roadmap entirely due to the associated legal and breach liability"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c2", "i6": "c1"},
        "rationales": {
            "i1": "Decommissioning the vulnerable component entirely removes the risky activity, which is the definition of avoidance.",
            "i2": "Purchasing insurance shifts the financial consequence of the risk to a third party (the insurer), the definition of transfer.",
            "i3": "Restricting access and adding logging reduces the likelihood/impact of the exposure without eliminating the underlying activity — mitigation.",
            "i4": "A formal, documented sign-off to continue operating with no further control action, because residual risk is within appetite, is acceptance.",
            "i5": "Outsourcing the function to a specialized provider that assumes operational and compliance responsibility shifts the risk to that party, even though the underlying capability (MFA via SMS) is still delivered — transfer.",
            "i6": "Dropping the feature entirely, before it is ever built, removes the risky activity altogether — avoidance, not mitigation, since nothing is deployed to be secured.",
        },
        "explanation": (
            "i5 is the discriminator: outsourcing a function to a provider who assumes the compliance burden is transfer, not "
            "avoidance, because the capability itself still exists and is still relied upon — only the operational/compliance "
            "risk moves to the third party. True avoidance (i1, i6) means the risky activity or feature never happens at all."
        ),
    },
    {
        "id": "npbqb-016",
        "domain": 5,
        "objective": "5.2",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A business continuity analyst is documenting measured and target values from the latest BIA and "
            "post-incident reviews. Match each statement to the metric it describes. One target is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "The order-processing database must be restored and functioning within 4 hours of an outage, per the signed business continuity plan"},
            {"id": "p2", "text": "Backups run every 15 minutes, meaning at most 15 minutes of transaction data can be lost in a failure"},
            {"id": "p3", "text": "Field data shows the storage array's redundant power supply has historically run an average of 43,800 hours between failures"},
            {"id": "p4", "text": "After last month's outage, the team measured that it took an average of 90 minutes from the first alert to full service restoration, based on the last 12 incidents"},
        ],
        "targets": [
            {"id": "t1", "text": "Recovery Time Objective (RTO)"},
            {"id": "t2", "text": "Recovery Point Objective (RPO)"},
            {"id": "t3", "text": "Mean Time Between Failures (MTBF)"},
            {"id": "t4", "text": "Mean Time to Repair/Restore (MTTR)"},
            {"id": "t5", "text": "Maximum Tolerable Downtime (MTD)"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "A target time to restore a specific system, defined in the BCP, is the Recovery Time Objective.",
            "p2": "A tolerance for how much data loss is acceptable, driven by backup frequency, is the Recovery Point Objective.",
            "p3": "An average historical duration between failures of a repairable component is Mean Time Between Failures.",
            "p4": "An average MEASURED duration to actually restore service across past incidents is Mean Time to Repair/Restore — a historical average, not a target.",
        },
        "explanation": (
            "t5 (MTD) is the distractor: MTD is the absolute outer limit of downtime the business can survive before "
            "irreparable harm, and it must be greater than RTO — it is often confused with RTO, but p1 describes a planned "
            "TARGET (RTO), not the survival ceiling. MTTR vs. RTO is the other key distinction: MTTR is a measured historical "
            "average from real incidents, while RTO is a forward-looking objective set in the BCP."
        ),
    },
    {
        "id": "npbqb-017",
        "domain": 5,
        "objective": "5.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A privacy officer is documenting data governance roles for an upcoming audit. Match each description "
            "to the single best-fitting role. One target is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "The retail company that collects customers' personal data through its website and decides what marketing purposes that data will be used for"},
            {"id": "p2", "text": "A third-party email marketing platform that sends campaigns on the retailer's behalf, strictly following the retailer's instructions about how customer data may be used"},
            {"id": "p3", "text": "The IT team responsible for the day-to-day technical safeguarding of a database — applying backups, access controls, and encryption — without deciding what the data is used for"},
            {"id": "p4", "text": "A business-unit VP who is accountable for a specific dataset's classification, approves who may access it, and answers for its proper handling within the organization"},
            {"id": "p5", "text": "An analyst on the marketing team who directly enters, updates, and works with customer records daily as part of routine job duties, applying handling rules set by the data owner"},
        ],
        "targets": [
            {"id": "t1", "text": "Data controller"},
            {"id": "t2", "text": "Data processor"},
            {"id": "t3", "text": "Data custodian"},
            {"id": "t4", "text": "Data owner"},
            {"id": "t5", "text": "Data steward"},
            {"id": "t6", "text": "Data subject"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "The entity that decides the purpose and means of processing personal data is the data controller under GDPR-style terminology.",
            "p2": "An entity that processes data only under the controller's instructions, without deciding its purpose, is the data processor.",
            "p3": "Applying technical safeguards (backups, access controls, encryption) without making usage decisions is the data custodian role.",
            "p4": "Business accountability for a dataset's classification and access approval belongs to the data owner, distinct from the technical custodian.",
            "p5": "Routine, day-to-day handling of records per rules set by the owner is the data steward role, distinct from the accountable owner and the technical custodian.",
        },
        "explanation": (
            "t6 (data subject) is the distractor: the data subject is the individual the data is ABOUT, not an organizational "
            "role responsible for handling it, so it cannot correctly match any of these prompts. Owner (accountable, sets "
            "classification) vs. custodian (technical safeguarding) vs. steward (routine day-to-day handling) is the other "
            "frequently confused trio, separate from the GDPR-specific controller/processor pair."
        ),
    },
    {
        "id": "npbqb-018",
        "domain": 5,
        "objective": "5.4",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A privacy team is mapping recent operational changes to the GDPR principle or right each one "
            "addresses. Classify each item accordingly."
        ),
        "categories": [
            {"id": "c1", "text": "Lawful basis for processing"},
            {"id": "c2", "text": "Data minimization"},
            {"id": "c3", "text": "Right to erasure ('right to be forgotten')"},
            {"id": "c4", "text": "Breach notification requirement"},
            {"id": "c5", "text": "Privacy by design and by default"},
            {"id": "c6", "text": "Right to access / data portability"},
        ],
        "items": [
            {"id": "i1", "text": "Before launching a new loyalty program, the company obtains explicit, informed consent from each customer before collecting any of their purchase history"},
            {"id": "i2", "text": "The signup form is redesigned to collect only a customer's email and zip code instead of the previously requested full home address and date of birth, since only those two fields are actually needed for the promotion"},
            {"id": "i3", "text": "A former customer emails support requesting that all of their personal data be permanently deleted from company systems, and the company complies absent any legal ground to retain it"},
            {"id": "i4", "text": "After discovering unauthorized access to a database containing EU residents' personal data, the company must notify the relevant supervisory authority within 72 hours of becoming aware of the breach"},
            {"id": "i5", "text": "When architecting a new mobile app, the development team builds in field-level encryption and default-private profile settings from the first design sprint, rather than adding privacy controls after launch"},
            {"id": "i6", "text": "A customer submits a form requesting a copy of all personal data the company holds about them, in a portable, machine-readable format"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c5", "i6": "c6"},
        "rationales": {
            "i1": "Obtaining explicit consent before processing establishes the lawful basis required before personal data collection begins.",
            "i2": "Collecting only the fields actually needed for the stated purpose, rather than the maximum available, is the data minimization principle.",
            "i3": "Honoring a deletion request in the absence of a legal ground to retain the data is the right to erasure.",
            "i4": "The 72-hour notification requirement to a supervisory authority after becoming aware of a breach is the breach notification requirement.",
            "i5": "Building privacy protections into the architecture from the start, rather than retrofitting them, is privacy by design and by default.",
            "i6": "Providing a copy of held personal data in a portable, machine-readable format on request is the right to access/data portability.",
        },
        "explanation": (
            "GDPR bundles several distinct obligations that are easy to conflate: minimization limits WHAT is collected, "
            "lawful basis governs WHETHER collection is permitted at all, erasure and access/portability are individual "
            "rights exercised on request, breach notification is a time-bound obligation triggered by an incident, and "
            "privacy by design is an architectural requirement applied before data is ever collected."
        ),
    },
]
