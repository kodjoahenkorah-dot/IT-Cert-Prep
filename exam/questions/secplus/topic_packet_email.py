"""CompTIA Security+ SY0-701 practice questions — topical batch: Packet Capture
and Email Authentication (SPF/DKIM/DMARC).

Part A (tpke-001..015) presents packet-capture / traffic-analysis excerpts
(SYN floods, DNS tunneling, C2 beaconing, port scans, ARP spoofing, plaintext
credential exposure, data exfiltration) and asks the reader to identify the
attack, the malicious host, or the correct response.

Part B (tpke-016..030) presents email headers and authentication results and
asks the reader to interpret SPF/DKIM/DMARC pass/fail, alignment, and the
correct disposition. Distractors are deliberately plausible red herrings
(reversed pass/fail meaning, confusing envelope-from vs. header-from,
mistaking DKIM signing for encryption, etc.).
"""

QUESTIONS = [
    # ===============================================================
    # Part A — Packet capture / traffic analysis (Log data sources)
    # ===============================================================
    {
        "id": "tpke-001",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A packet capture on a web server's uplink shows thousands of these frames per second from many "
            "different source IPs:\n"
            "  IP 198.51.100.x > 10.0.0.5: TCP 40000+ > 443 [SYN] seq=... win=1024\n"
            "The server's connection table is full of half-open connections and legitimate clients are timing "
            "out. No matching [SYN,ACK]/[ACK] completions are seen. What is happening?"
        ),
        "options": [
            {"id": "a", "text": "A SYN flood (TCP half-open) denial-of-service attack", "correct": True,
             "rationale": "Correct. A high rate of SYN packets that never complete the three-way handshake, "
                          "filling the backlog with half-open connections and exhausting resources, is the "
                          "defining signature of a SYN flood."},
            {"id": "b", "text": "A normal traffic spike from a marketing campaign", "correct": False,
             "rationale": "Incorrect. Legitimate clients complete the handshake (SYN, SYN-ACK, ACK) and establish "
                          "sessions; here no handshakes complete and the connection table is saturated with "
                          "half-open entries, which is not normal load."},
            {"id": "c", "text": "A DNS amplification attack", "correct": False,
             "rationale": "Incorrect. DNS amplification abuses UDP/53 open resolvers to reflect large responses; "
                          "this capture is TCP SYN traffic to port 443, not UDP DNS reflection."},
            {"id": "d", "text": "An ARP poisoning attack on the local segment", "correct": False,
             "rationale": "Incorrect. ARP poisoning manipulates layer-2 MAC/IP mappings via gratuitous ARP "
                          "replies; nothing here shows ARP traffic — these are layer-4 TCP SYN packets."},
        ],
        "explanation": (
            "A flood of SYN packets with no completing ACKs, leaving many half-open connections and starving "
            "the backlog queue, is a SYN flood. Mitigations include SYN cookies, rate limiting, and upstream "
            "DDoS scrubbing."
        ),
    },
    {
        "id": "tpke-002",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst reviews DNS query logs from one internal workstation:\n"
            "  10.2.4.9 -> A?  d3f9a1c2b7.exfil.attacker-domain.com\n"
            "  10.2.4.9 -> A?  a71bc39ff0.exfil.attacker-domain.com\n"
            "  10.2.4.9 -> A?  9c2e01aa4d.exfil.attacker-domain.com\n"
            "Hundreds of these appear per minute, each with a unique long random-looking subdomain to the same "
            "parent domain, and the responses are TXT records. What is the MOST likely explanation?"
        ),
        "options": [
            {"id": "a", "text": "DNS tunneling used for data exfiltration or C2", "correct": True,
             "rationale": "Correct. A high volume of queries encoding unique high-entropy subdomains to a single "
                          "attacker-controlled domain, with data returned in TXT records, is the hallmark of DNS "
                          "tunneling used to smuggle data or command-and-control traffic past egress controls."},
            {"id": "b", "text": "A misconfigured NTP client", "correct": False,
             "rationale": "Incorrect. NTP uses UDP/123 to a small set of time servers with fixed hostnames; it "
                          "does not generate hundreds of unique random subdomain DNS lookups."},
            {"id": "c", "text": "Normal CDN content delivery", "correct": False,
             "rationale": "Incorrect. CDNs use a small, stable set of hostnames and return A/AAAA/CNAME records; "
                          "they do not produce a stream of unique random subdomains resolved as TXT records."},
            {"id": "d", "text": "A cache-poisoning attack against the resolver", "correct": False,
             "rationale": "Incorrect. Cache poisoning injects forged responses for legitimate names; the pattern "
                          "here is an internal host generating outbound queries to a single malicious parent "
                          "domain, which is tunneling/exfiltration, not poisoning."},
        ],
        "explanation": (
            "High-entropy, high-volume subdomain queries to one domain with data carried in TXT records is "
            "classic DNS tunneling. Detect it with query-length/entropy analysis and block/inspect DNS egress."
        ),
    },
    {
        "id": "tpke-003",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A capture shows an internal host contacting the same external IP on port 443 at almost exactly the "
            "same interval — every 60 seconds, ±2s — with small, similarly-sized outbound payloads and small "
            "responses, continuously for days including overnight. What does this pattern MOST strongly suggest?"
        ),
        "options": [
            {"id": "a", "text": "Command-and-control (C2) beaconing by malware", "correct": True,
             "rationale": "Correct. Regular, low-jitter periodic connections of consistent small size to a fixed "
                          "external host around the clock is textbook C2 beaconing — the implant checking in for "
                          "instructions on a fixed interval."},
            {"id": "b", "text": "A user streaming video", "correct": False,
             "rationale": "Incorrect. Video streaming produces large, sustained, variable-size inbound throughput "
                          "during active use, not tiny fixed-size bidirectional exchanges on a precise 60-second "
                          "beat running overnight when no one is present."},
            {"id": "c", "text": "Automatic OS update checks", "correct": False,
             "rationale": "Incorrect. Update checks are infrequent (hours/days), go to vendor domains, and vary "
                          "in size; a precise 60-second beat to a single IP for days is far more regular than "
                          "legitimate update polling."},
            {"id": "d", "text": "NTP time synchronization", "correct": False,
             "rationale": "Incorrect. NTP uses UDP/123 to time servers, not TCP/443 to an arbitrary external "
                          "host; the transport and destination do not match time sync."},
        ],
        "explanation": (
            "Low-jitter periodic check-ins of consistent size to a fixed destination, continuing around the "
            "clock, is beaconing. Analysts hunt for it with interval/jitter and byte-count consistency analysis."
        ),
    },
    {
        "id": "tpke-004",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "In Wireshark, an analyst follows a TCP stream to an internal application and sees:\n"
            "  POST /login HTTP/1.1\n"
            "  Host: intranet.corp.local\n"
            "  Content-Type: application/x-www-form-urlencoded\n\n"
            "  username=jsmith&password=Summer2025!\n"
            "The traffic is on TCP/80. What is the PRIMARY security finding?"
        ),
        "options": [
            {"id": "a", "text": "Credentials are transmitted in cleartext over unencrypted HTTP", "correct": True,
             "rationale": "Correct. The username and password are visible in plaintext because the login is over "
                          "HTTP (port 80) with no TLS; anyone able to capture the traffic can read the "
                          "credentials. The fix is to require HTTPS/TLS."},
            {"id": "b", "text": "The password is too weak", "correct": False,
             "rationale": "Incorrect. Password strength is a secondary concern; the PRIMARY finding visible in "
                          "the capture is that credentials traverse the network unencrypted, which exposes any "
                          "password regardless of its strength."},
            {"id": "c", "text": "The server is vulnerable to SQL injection", "correct": False,
             "rationale": "Incorrect. Nothing in the request demonstrates injection; the request is a normal "
                          "form POST. The observable problem is the lack of transport encryption exposing the "
                          "credentials."},
            {"id": "d", "text": "A CSRF token is missing from the request", "correct": False,
             "rationale": "Incorrect. While CSRF protection may be worth reviewing, the capture directly reveals "
                          "cleartext credentials over HTTP, which is the immediate and primary exposure."},
        ],
        "explanation": (
            "Seeing credentials in a plaintext HTTP body in a packet capture is a direct confidentiality "
            "failure. Enforce TLS (HTTPS) and HSTS so login data is never sent in the clear."
        ),
    },
    {
        "id": "tpke-005",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Log data sources",
        "stem": (
            "A capture on a switch shows repeated unsolicited ARP replies:\n"
            "  ARP reply 10.0.0.1 is-at 00:11:22:aa:bb:cc  (the gateway's real MAC is 00:0a:95:9d:68:16)\n"
            "sent to multiple hosts, immediately followed by those hosts' traffic to the internet flowing "
            "through 00:11:22:aa:bb:cc. What attack is occurring?"
        ),
        "options": [
            {"id": "a", "text": "ARP spoofing/poisoning enabling an on-path (MITM) attack", "correct": True,
             "rationale": "Correct. Forged ARP replies claiming the gateway IP maps to the attacker's MAC cause "
                          "victims to send their traffic through the attacker, placing them on-path for "
                          "interception — classic ARP poisoning used for a man-in-the-middle attack."},
            {"id": "b", "text": "A rogue DHCP server handing out bad leases", "correct": False,
             "rationale": "Incorrect. Rogue DHCP manipulates address/gateway assignment via DHCP OFFER/ACK "
                          "messages; this capture shows forged ARP replies rebinding the gateway's IP to a new "
                          "MAC, which is ARP poisoning, not DHCP abuse."},
            {"id": "c", "text": "DNS spoofing", "correct": False,
             "rationale": "Incorrect. DNS spoofing forges name-to-IP responses; here the layer-2 IP-to-MAC "
                          "mapping is being poisoned, redirecting traffic at the data-link layer, not via DNS."},
            {"id": "d", "text": "A MAC flooding attack against the switch CAM table", "correct": False,
             "rationale": "Incorrect. MAC flooding overwhelms the switch's CAM table with many bogus source MACs "
                          "to force fail-open flooding; this capture shows targeted forged ARP replies for the "
                          "gateway IP, which is poisoning, not CAM exhaustion."},
        ],
        "explanation": (
            "Gratuitous/unsolicited ARP replies that rebind the gateway IP to the attacker's MAC are ARP "
            "poisoning. Mitigate with Dynamic ARP Inspection (DAI), DHCP snooping, and port security."
        ),
    },
    {
        "id": "tpke-006",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "NetFlow shows a single internal database server (10.5.5.20) uploading 48 GB over TLS to an "
            "external cloud-storage IP between 01:00 and 04:00, far outside its normal baseline of a few MB of "
            "outbound traffic. Inbound to the server was negligible. What is the MOST likely concern?"
        ),
        "options": [
            {"id": "a", "text": "Data exfiltration of database contents to an external destination", "correct": True,
             "rationale": "Correct. A large volume of outbound data from a sensitive host to an external "
                          "destination, occurring off-hours and vastly exceeding baseline, is the classic "
                          "signature of data exfiltration and warrants immediate investigation and containment."},
            {"id": "b", "text": "A scheduled OS patch download", "correct": False,
             "rationale": "Incorrect. Patch downloads are inbound (the server receives update files); this is 48 "
                          "GB flowing outbound from the server, the opposite direction of a download."},
            {"id": "c", "text": "Normal database replication to a peer", "correct": False,
             "rationale": "Incorrect. Legitimate replication goes to a known internal/approved replica on a "
                          "consistent schedule; a one-off 48 GB upload to an unrecognized external cloud IP far "
                          "above baseline is not routine replication."},
            {"id": "d", "text": "A backup restore operation", "correct": False,
             "rationale": "Incorrect. A restore writes data into the server (inbound); this flow is massive "
                          "outbound egress, consistent with exfiltration rather than a restore."},
        ],
        "explanation": (
            "Large off-hours outbound transfers from sensitive systems to unfamiliar external endpoints are a "
            "top exfiltration indicator. Flow data (NetFlow) is ideal for spotting these volume/direction "
            "anomalies even when the payload is encrypted."
        ),
    },
    {
        "id": "tpke-007",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A capture from one source IP shows connection attempts to 10.0.0.5 on ports 1, 2, 3, 4, 5, ... "
            "sequentially climbing through the entire range in seconds, with the target sending RST for closed "
            "ports and SYN-ACK for a handful of open ones. Which scan type is this?"
        ),
        "options": [
            {"id": "a", "text": "A TCP connect/SYN port scan enumerating open services on one host", "correct": True,
             "rationale": "Correct. Sequentially sweeping the port range on a single target and inferring open "
                          "vs. closed from SYN-ACK vs. RST responses is a port scan enumerating that host's "
                          "listening services."},
            {"id": "b", "text": "A ping sweep of the subnet", "correct": False,
             "rationale": "Incorrect. A ping sweep sends ICMP echo requests across many hosts to find live "
                          "systems; this traffic targets many ports on one host via TCP, which is a port scan, "
                          "not a host-discovery sweep."},
            {"id": "c", "text": "A brute-force password attack", "correct": False,
             "rationale": "Incorrect. Brute forcing hammers one authenticating service with credential guesses; "
                          "this is layer-4 probing across the whole port range with no authentication attempts."},
            {"id": "d", "text": "A slowloris HTTP DoS", "correct": False,
             "rationale": "Incorrect. Slowloris holds many partial HTTP requests open on port 80/443 to exhaust "
                          "a web server; it does not sweep the full TCP port range on a host."},
        ],
        "explanation": (
            "Sequential probing of a host's port range, reading SYN-ACK (open) vs. RST (closed), is a port "
            "scan. It is a reconnaissance precursor to targeted exploitation of discovered services."
        ),
    },
    {
        "id": "tpke-008",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst captures traffic during a suspected compromise and sees an internal host establish an "
            "outbound TCP/4444 session to an external IP, after which an interactive shell's command output "
            "(whoami, ipconfig, dir) is visible in the stream flowing back to that external IP. What does this "
            "indicate?"
        ),
        "options": [
            {"id": "a", "text": "A reverse shell — the victim connected outbound to the attacker's listener", "correct": True,
             "rationale": "Correct. The victim initiating the outbound connection (commonly to a port like 4444) "
                          "with interactive command output streaming to the external host is a reverse shell, "
                          "which is favored because outbound connections often bypass ingress firewall rules."},
            {"id": "b", "text": "A bind shell where the attacker connected inbound to the victim", "correct": False,
             "rationale": "Incorrect. In a bind shell the attacker connects INBOUND to a listener on the victim; "
                          "here the victim originated the OUTBOUND connection to the attacker, which is a reverse "
                          "shell — the direction distinguishes the two."},
            {"id": "c", "text": "A normal SSH administrative session", "correct": False,
             "rationale": "Incorrect. SSH uses TCP/22 and is encrypted so command output would not be visible in "
                          "cleartext; this is an unencrypted interactive shell over an unusual port, not SSH."},
            {"id": "d", "text": "A RDP remote-desktop session", "correct": False,
             "rationale": "Incorrect. RDP uses TCP/3389 and a graphical/encrypted protocol; a cleartext text "
                          "command shell over port 4444 is a reverse shell, not RDP."},
        ],
        "explanation": (
            "Outbound connections from a victim carrying interactive shell I/O are reverse shells. Egress "
            "filtering, allow-listing, and monitoring for shells on odd ports help detect and contain them."
        ),
    },
    {
        "id": "tpke-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A pcap shows an HTTP GET to a web app:\n"
            "  GET /product?id=1%27%20OR%20%271%27%3D%271 HTTP/1.1\n"
            "URL-decoded, the id parameter is: 1' OR '1'='1\n"
            "What attack is being attempted?"
        ),
        "options": [
            {"id": "a", "text": "SQL injection", "correct": True,
             "rationale": "Correct. The payload 1' OR '1'='1 is a canonical SQL injection tautology designed to "
                          "make a WHERE clause always evaluate true, manipulating the backend query through the "
                          "id parameter."},
            {"id": "b", "text": "Cross-site scripting (XSS)", "correct": False,
             "rationale": "Incorrect. XSS injects script/markup (e.g., <script>...) to run in a victim's browser; "
                          "this payload is SQL syntax targeting the database query, not client-side script."},
            {"id": "c", "text": "Directory traversal", "correct": False,
             "rationale": "Incorrect. Directory traversal uses sequences like ../../ to escape the web root and "
                          "read files; this payload contains SQL quote/OR logic, which targets the database."},
            {"id": "d", "text": "Server-side request forgery (SSRF)", "correct": False,
             "rationale": "Incorrect. SSRF supplies an internal URL to make the server issue requests on the "
                          "attacker's behalf; the id parameter here contains a SQL tautology, indicating "
                          "injection into a query."},
        ],
        "explanation": (
            "The OR '1'='1 tautology is a textbook SQL injection probe. Defend with parameterized queries/"
            "prepared statements and input validation; a WAF can flag such payloads in transit."
        ),
    },
    {
        "id": "tpke-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst wants to confirm that traffic captured on TCP/443 to an external host is truly TLS and "
            "not an attacker abusing port 443 to blend in. Which TWO observations would BEST support that the "
            "session is anomalous (not normal HTTPS)?"
        ),
        "options": [
            {"id": "a", "text": "There is no TLS ClientHello/ServerHello handshake — raw bytes flow immediately",
             "correct": True,
             "rationale": "Correct. Legitimate HTTPS begins with a TLS handshake (ClientHello, ServerHello, "
                          "certificate exchange); raw payload with no handshake on port 443 indicates a "
                          "non-TLS protocol tunneled over the port to evade detection."},
            {"id": "b", "text": "The session shows a precise fixed-interval beacon of tiny identical payloads",
             "correct": True,
             "rationale": "Correct. Perfectly periodic, uniform tiny exchanges are characteristic of C2 "
                          "beaconing rather than interactive human web browsing, supporting an anomalous "
                          "verdict even if TLS is present."},
            {"id": "c", "text": "The destination presents a valid, CA-signed certificate for a known domain",
             "correct": False,
             "rationale": "Incorrect. A valid certificate for a recognized domain is consistent with legitimate "
                          "HTTPS and would argue against the traffic being anomalous."},
            {"id": "d", "text": "The session uses TLS 1.3 with a modern cipher suite", "correct": False,
             "rationale": "Incorrect. Modern TLS 1.3 with a strong cipher is normal, healthy HTTPS behavior and "
                          "does not by itself indicate anomalous or malicious activity."},
        ],
        "explanation": (
            "Attackers abuse port 443 to blend in. Absence of a real TLS handshake and machine-like beaconing "
            "are strong anomaly signals; a valid cert and modern TLS are signs of legitimate traffic."
        ),
    },
    {
        "id": "tpke-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A capture shows UDP/53 responses arriving at a victim's public IP that are 40–50x larger than the "
            "queries, from many open DNS resolvers, and the victim never sent those queries. The victim's link "
            "is saturated. What attack is this?"
        ),
        "options": [
            {"id": "a", "text": "A DNS amplification/reflection DDoS", "correct": True,
             "rationale": "Correct. Spoofing the victim's source IP in queries to open resolvers so large "
                          "responses flood the victim — with a big response-to-query size ratio — is a DNS "
                          "amplification reflection attack."},
            {"id": "b", "text": "DNS tunneling exfiltration from the victim", "correct": False,
             "rationale": "Incorrect. Tunneling involves the victim SENDING many encoded queries outbound; here "
                          "the victim is RECEIVING unsolicited large responses it never requested, which is "
                          "reflection/amplification."},
            {"id": "c", "text": "A cache-poisoning attack", "correct": False,
             "rationale": "Incorrect. Cache poisoning injects forged records into a resolver's cache; this is a "
                          "volumetric flood of reflected responses saturating the link, which is a DoS, not "
                          "poisoning."},
            {"id": "d", "text": "A SYN flood", "correct": False,
             "rationale": "Incorrect. A SYN flood is TCP half-open traffic; this is UDP/53 reflected DNS "
                          "responses, a different transport and mechanism."},
        ],
        "explanation": (
            "Unsolicited, oversized DNS responses from many resolvers indicate a reflection/amplification DDoS "
            "using the victim's spoofed source IP. Mitigate with upstream scrubbing and by closing open "
            "resolvers."
        ),
    },
    {
        "id": "tpke-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "During analysis of captured SMB traffic, an analyst sees one workstation (10.3.3.7) opening SMB "
            "sessions to hundreds of other workstations in rapid succession, authenticating with the same "
            "domain account and accessing ADMIN$ / C$ shares. What activity does this MOST likely represent?"
        ),
        "options": [
            {"id": "a", "text": "Lateral movement across the network", "correct": True,
             "rationale": "Correct. A single host authenticating to many peers and touching administrative "
                          "shares (ADMIN$/C$) with the same credentials is the signature of lateral movement — "
                          "an attacker spreading from an initial foothold using compromised credentials."},
            {"id": "b", "text": "A normal software deployment from SCCM", "correct": False,
             "rationale": "Incorrect. Managed deployments originate from designated management servers using "
                          "service accounts, not from an ordinary workstation fanning out to hundreds of peers "
                          "with a single account — the source and pattern point to lateral movement."},
            {"id": "c", "text": "A DDoS attack", "correct": False,
             "rationale": "Incorrect. DDoS is about overwhelming a target with volume from many sources; this is "
                          "one host authenticating to many hosts and accessing admin shares, which is spreading, "
                          "not flooding."},
            {"id": "d", "text": "Routine file-server backups", "correct": False,
             "rationale": "Incorrect. Backups pull from designated servers on a schedule via backup agents; a "
                          "workstation rapidly authenticating to hundreds of endpoints' admin shares is not a "
                          "backup workflow."},
        ],
        "explanation": (
            "Rapid authenticated access to many peers' administrative shares from one host is lateral movement. "
            "Detect it with east-west monitoring, and limit it with least privilege, LAPS, and segmentation."
        ),
    },
    {
        "id": "tpke-013",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A pcap of an FTP session shows:\n"
            "  USER admin\n"
            "  PASS P@ssw0rd2025\n"
            "  RETR customer_export.csv\n"
            "all readable in plaintext. Which control BEST addresses the exposure this reveals?"
        ),
        "options": [
            {"id": "a", "text": "Replace FTP with a secure protocol such as SFTP or FTPS", "correct": True,
             "rationale": "Correct. FTP sends credentials and data in cleartext; migrating to SFTP (SSH) or FTPS "
                          "(TLS) encrypts both authentication and the file transfer, directly fixing the "
                          "plaintext exposure seen in the capture."},
            {"id": "b", "text": "Require a longer FTP password", "correct": False,
             "rationale": "Incorrect. A longer password is still transmitted in cleartext over FTP and captured "
                          "trivially; the exposure is the lack of encryption, not password length."},
            {"id": "c", "text": "Enable an account lockout policy on the FTP server", "correct": False,
             "rationale": "Incorrect. Lockout limits brute forcing but does nothing about the credentials and "
                          "data already flowing in the clear on the wire, which is the exposure the capture "
                          "shows."},
            {"id": "d", "text": "Move the FTP server to a non-standard port", "correct": False,
             "rationale": "Incorrect. Changing the port is security through obscurity; the traffic remains "
                          "unencrypted and readable to anyone capturing it regardless of port number."},
        ],
        "explanation": (
            "Plaintext FTP exposes credentials and data. The correct remediation is an encrypted transfer "
            "protocol (SFTP/FTPS), not tweaks to passwords, lockout, or port numbers."
        ),
    },
    {
        "id": "tpke-014",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Log data sources",
        "stem": (
            "An IDS flags traffic and the analyst pulls the packet. The TCP flags field shows FIN, PSH, and URG "
            "all set with no prior SYN handshake for that connection, sent to many closed ports. What is the "
            "attacker MOST likely doing?"
        ),
        "options": [
            {"id": "a", "text": "A Xmas-tree scan to fingerprint the host/firewall by observing responses",
             "correct": True,
             "rationale": "Correct. Packets with FIN+PSH+URG set (the 'Christmas tree' flag combination) with no "
                          "established session are crafted to elicit different responses from open vs. closed "
                          "ports and to probe how the stack/firewall handles out-of-state packets — a stealth "
                          "scan / OS-fingerprinting technique."},
            {"id": "b", "text": "Establishing a normal TLS session", "correct": False,
             "rationale": "Incorrect. A normal session begins with a SYN handshake; a packet with FIN+PSH+URG "
                          "and no handshake is deliberately malformed for scanning, not a legitimate connection."},
            {"id": "c", "text": "A SYN flood", "correct": False,
             "rationale": "Incorrect. A SYN flood sends many SYN packets; this packet has FIN, PSH, and URG set "
                          "(and no SYN), which is a Xmas scan, a different technique."},
            {"id": "d", "text": "Transferring a large file", "correct": False,
             "rationale": "Incorrect. A bulk transfer rides an established connection with ordinary ACK/PSH data "
                          "segments; sending crafted FIN+PSH+URG packets to many closed ports is scanning, not "
                          "data transfer."},
        ],
        "explanation": (
            "The FIN+PSH+URG 'Christmas tree' flag set on unsolicited packets is a stealth/OS-fingerprinting "
            "scan that abuses how stacks respond to out-of-state flags. IDS signatures and stateful firewalls "
            "catch it."
        ),
    },
    {
        "id": "tpke-015",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst captures traffic and notices a host requesting the same web page every 5 minutes, but "
            "the User-Agent string is 'python-requests/2.31' and each response body is being parsed for a "
            "specific hidden field before the host makes an outbound POST to a different external server. What "
            "should the analyst conclude?"
        ),
        "options": [
            {"id": "a", "text": "The host is running an automated script/bot, warranting investigation for C2 "
                                "or scraping", "correct": True,
             "rationale": "Correct. A scripting-library User-Agent, fixed polling interval, programmatic parsing, "
                          "and chained outbound POSTs indicate automated (non-human) activity that should be "
                          "investigated as possible C2, scraping, or unauthorized automation."},
            {"id": "b", "text": "This is normal interactive browsing", "correct": False,
             "rationale": "Incorrect. Human browsing uses real browser User-Agents with irregular timing; a "
                          "'python-requests' agent polling on a fixed 5-minute beat and auto-parsing responses "
                          "is scripted automation, not interactive use."},
            {"id": "c", "text": "The web server is misconfigured", "correct": False,
             "rationale": "Incorrect. Nothing indicates a server fault; the notable behavior is the client-side "
                          "automation pattern, which is what should be investigated."},
            {"id": "d", "text": "The traffic is encrypted and cannot be analyzed", "correct": False,
             "rationale": "Incorrect. The analyst can read the User-Agent, timing, and POST behavior, so the "
                          "traffic is observable; the concern is the automated pattern it reveals."},
        ],
        "explanation": (
            "Scripting-library User-Agents, fixed intervals, and programmatic response handling reveal bots. "
            "Correlate with allow-lists and threat intel to decide if it is benign automation or malicious C2."
        ),
    },
    # ===============================================================
    # Part B — Email authentication (SPF / DKIM / DMARC)
    # ===============================================================
    {
        "id": "tpke-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "An inbound message shows these Authentication-Results:\n"
            "  spf=pass (sender IP is authorized) smtp.mailfrom=news.vendor.com\n"
            "  dkim=pass header.d=vendor.com\n"
            "  dmarc=fail (p=reject)\n"
            "SPF and DKIM both passed, yet DMARC failed. What is the MOST likely reason?"
        ),
        "options": [
            {"id": "a", "text": "Neither the SPF-authenticated domain nor the DKIM d= domain is aligned with the "
                                "From: header domain", "correct": True,
             "rationale": "Correct. DMARC requires that a passing mechanism ALIGN with the RFC5322 From: header "
                          "domain. SPF passed for smtp.mailfrom=news.vendor.com and DKIM signed for "
                          "d=vendor.com, but if the visible From: is a different organizational domain, neither "
                          "aligns and DMARC fails despite the underlying passes."},
            {"id": "b", "text": "DMARC always fails when the message is encrypted with TLS", "correct": False,
             "rationale": "Incorrect. DMARC evaluates SPF/DKIM alignment and has nothing to do with TLS "
                          "transport encryption; TLS does not cause DMARC to fail."},
            {"id": "c", "text": "A DMARC failure means the DKIM signature was cryptographically invalid",
             "correct": False,
             "rationale": "Incorrect. The results explicitly show dkim=pass, so the signature was valid; DMARC "
                          "failed on alignment, not on signature validity."},
            {"id": "d", "text": "SPF and DKIM passing guarantees DMARC passes", "correct": False,
             "rationale": "Incorrect. A pass on SPF or DKIM is necessary but not sufficient — DMARC additionally "
                          "requires domain alignment with the From: header, which is why it can still fail here."},
        ],
        "explanation": (
            "DMARC = (SPF pass AND SPF alignment) OR (DKIM pass AND DKIM alignment). Underlying passes without "
            "alignment to the From: domain still produce dmarc=fail. Alignment is the concept most often "
            "tested."
        ),
    },
    {
        "id": "tpke-017",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A phishing email spoofs the display name 'IT Help Desk <helpdesk@yourcompany.com>'. Analysis shows:\n"
            "  Envelope MAIL FROM: bounce@sketchy-mailer.ru\n"
            "  From: helpdesk@yourcompany.com\n"
            "  spf=pass smtp.mailfrom=sketchy-mailer.ru\n"
            "  dkim=none\n"
            "Your domain publishes DMARC p=reject. Why should this message be rejected/quarantined even though "
            "spf=pass?"
        ),
        "options": [
            {"id": "a", "text": "SPF authenticated sketchy-mailer.ru (the envelope domain), which is not aligned "
                                "with the yourcompany.com From: domain, and there is no DKIM — so DMARC fails",
             "correct": True,
             "rationale": "Correct. SPF validated the ENVELOPE (MAIL FROM) domain sketchy-mailer.ru, not the "
                          "visible From: yourcompany.com. Because the authenticated domain does not align with "
                          "the From: header and DKIM is absent, DMARC fails and p=reject applies — blocking the "
                          "spoof."},
            {"id": "b", "text": "spf=pass means the message is safe and it should be delivered", "correct": False,
             "rationale": "Incorrect. spf=pass only means the sending IP was authorized for the envelope domain; "
                          "it says nothing about the spoofed From: header. Relying on SPF pass alone would let "
                          "this spoof through, which is exactly what DMARC alignment prevents."},
            {"id": "c", "text": "The message failed because DKIM was cryptographically broken", "correct": False,
             "rationale": "Incorrect. DKIM was not broken — it was absent (dkim=none). There was no signature to "
                          "break; DMARC fails due to lack of an aligned, passing mechanism."},
            {"id": "d", "text": "SPF checks the From: header, and it failed there", "correct": False,
             "rationale": "Incorrect. SPF checks the envelope MAIL FROM (return-path), not the RFC5322 From: "
                          "header. That envelope-vs-header distinction is precisely why an attacker can get "
                          "spf=pass while spoofing the visible From:."},
        ],
        "explanation": (
            "SPF authenticates the envelope sender; DMARC ties authentication to the visible From: via "
            "alignment. Spoofers pass SPF for their own envelope domain but fail DMARC alignment — the reason "
            "DMARC exists."
        ),
    },
    {
        "id": "tpke-018",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "What does a DKIM signature actually provide for an email message?"
        ),
        "options": [
            {"id": "a", "text": "Cryptographic proof that specified header fields and the body were not altered "
                                "in transit and that the signing domain authorized the message", "correct": True,
             "rationale": "Correct. DKIM applies a domain's private-key signature over selected headers and the "
                          "body; the recipient verifies it with the public key in DNS, providing integrity and "
                          "domain-level authenticity (that d= domain took responsibility for the message)."},
            {"id": "b", "text": "End-to-end encryption of the message body so only the recipient can read it",
             "correct": False,
             "rationale": "Incorrect. DKIM signs, it does not encrypt — the body remains readable to anyone in "
                          "transit. Confidentiality would require S/MIME or PGP, not DKIM."},
            {"id": "c", "text": "A list of IP addresses authorized to send for the domain", "correct": False,
             "rationale": "Incorrect. That describes SPF, which publishes authorized sending IPs in DNS. DKIM "
                          "uses cryptographic signatures, not an IP list."},
            {"id": "d", "text": "A policy telling receivers what to do when authentication fails", "correct": False,
             "rationale": "Incorrect. That describes the DMARC policy (p=none/quarantine/reject). DKIM provides "
                          "the signature/integrity mechanism, not the failure-handling policy."},
        ],
        "explanation": (
            "DKIM = signature for integrity + domain authenticity (not encryption). SPF = authorized-IP list. "
            "DMARC = alignment policy and reporting built on top of SPF/DKIM. Keep the three roles distinct."
        ),
    },
    {
        "id": "tpke-019",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company publishes: v=DMARC1; p=none; rua=mailto:dmarc@company.com. Legitimate mail flows are all "
            "authenticated, and reports show no unauthorized senders. What is the correct NEXT step to actually "
            "protect the domain from spoofing?"
        ),
        "options": [
            {"id": "a", "text": "Tighten the policy (e.g., to p=quarantine, then p=reject) now that reporting "
                                "confirms legitimate mail passes", "correct": True,
             "rationale": "Correct. p=none only monitors and reports; it does not stop spoofed mail. After using "
                          "rua reports to confirm all legitimate sources authenticate and align, the domain "
                          "should progress to p=quarantine and ultimately p=reject to enforce protection."},
            {"id": "b", "text": "Leave p=none permanently because it is the most secure setting", "correct": False,
             "rationale": "Incorrect. p=none is the LEAST protective policy — it takes no action on failing mail. "
                          "It is a starting/monitoring posture, not the secure end state."},
            {"id": "c", "text": "Remove the DMARC record since SPF and DKIM already pass", "correct": False,
             "rationale": "Incorrect. Removing DMARC eliminates alignment enforcement and reporting, re-enabling "
                          "From: spoofing that SPF/DKIM alone do not prevent. The goal is to enforce, not "
                          "remove."},
            {"id": "d", "text": "Switch SPF to -all only and delete DKIM", "correct": False,
             "rationale": "Incorrect. Deleting DKIM weakens authentication and breaks a key DMARC pathway "
                          "(especially through forwarders); the correct move is to enforce the DMARC policy, "
                          "keeping both SPF and DKIM."},
        ],
        "explanation": (
            "DMARC rollout: start p=none to observe via rua reports, confirm all legit senders align, then "
            "escalate to quarantine and reject. p=none alone provides visibility, not protection."
        ),
    },
    {
        "id": "tpke-020",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A newsletter sent through a third-party marketing platform is failing DMARC at recipients. Results "
            "show:\n"
            "  spf=pass smtp.mailfrom=bounce.mktplatform.com\n"
            "  dkim=pass header.d=mktplatform.com\n"
            "  From: news@company.com\n"
            "  DMARC policy for company.com: p=reject\n"
            "What is the BEST fix so the mail authenticates under company.com's DMARC without weakening it?"
        ),
        "options": [
            {"id": "a", "text": "Have the platform DKIM-sign with a company.com selector (or configure an "
                                "aligned SPF domain) so an authenticated mechanism aligns with the From: domain",
             "correct": True,
             "rationale": "Correct. The mail passes SPF/DKIM only for the platform's own domain, which is not "
                          "aligned with From: company.com. Configuring the platform to sign DKIM as "
                          "d=company.com (via a delegated selector) — or to use an aligned return-path — makes "
                          "an authenticated mechanism align, so DMARC passes without relaxing the policy."},
            {"id": "b", "text": "Change company.com's DMARC to p=none", "correct": False,
             "rationale": "Incorrect. Dropping to p=none would stop the failures by disabling enforcement, but "
                          "it also removes spoofing protection for the whole domain — weakening security rather "
                          "than fixing alignment for this one sender."},
            {"id": "c", "text": "Add the marketing platform's IPs to company.com's SPF record only", "correct": False,
             "rationale": "Incorrect. Adding IPs to SPF authorizes them for the envelope, but if the envelope "
                          "MAIL FROM stays bounce.mktplatform.com, SPF still authenticates the platform domain "
                          "and does not align with From: company.com. Alignment, not just authorization, is "
                          "required."},
            {"id": "d", "text": "Tell recipients to allow-list the newsletter", "correct": False,
             "rationale": "Incorrect. Asking every recipient to create exceptions is not scalable and does not "
                          "fix the underlying alignment problem; the sending configuration should be corrected."},
        ],
        "explanation": (
            "Third-party senders fail DMARC when they authenticate only for their own domain. The fix is "
            "alignment — DKIM-sign as your domain (delegated selector) or use an aligned return-path — never "
            "downgrading the policy."
        ),
    },
    {
        "id": "tpke-021",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "An SPF record reads: v=spf1 include:_spf.google.com include:sendgrid.net ~all\n"
            "A message from an IP not covered by any include mechanism arrives. What result does the '~all' "
            "produce, and what does it mean?"
        ),
        "options": [
            {"id": "a", "text": "SoftFail — the sender is probably not authorized; accept but mark/suspect it",
             "correct": True,
             "rationale": "Correct. '~all' is a SoftFail: unlisted senders are treated as probably unauthorized. "
                          "Receivers typically accept the mail but flag it as suspicious rather than outright "
                          "rejecting, unlike '-all' (hard fail)."},
            {"id": "b", "text": "HardFail — the message must be rejected", "correct": False,
             "rationale": "Incorrect. A hard fail is '-all'. The tilde in '~all' is a SoftFail, a weaker "
                          "assertion that suggests marking rather than rejecting."},
            {"id": "c", "text": "Pass — the sender is authorized", "correct": False,
             "rationale": "Incorrect. 'all' matches senders not covered by earlier mechanisms; with the '~' "
                          "qualifier that is a SoftFail for unlisted senders, not a pass."},
            {"id": "d", "text": "Neutral — no policy assertion is made", "correct": False,
             "rationale": "Incorrect. Neutral is '?all'. '~all' explicitly asserts a SoftFail (probably not "
                          "authorized), which is a stronger statement than neutral."},
        ],
        "explanation": (
            "SPF 'all' qualifiers: -all = HardFail (reject), ~all = SoftFail (mark/suspect), ?all = Neutral, "
            "+all = Pass (never use). Know the tilde vs. hyphen distinction cold."
        ),
    },
    {
        "id": "tpke-022",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A legitimate message is forwarded by a mailing list. At the final recipient:\n"
            "  spf=fail (the list server's IP is not in the original domain's SPF)\n"
            "  dkim=pass header.d=originaldomain.com (signature still valid)\n"
            "  dmarc=pass\n"
            "Why did DMARC PASS even though SPF failed after forwarding?"
        ),
        "options": [
            {"id": "a", "text": "DMARC passes if EITHER SPF or DKIM passes with alignment; the DKIM signature "
                                "survived forwarding and remained aligned", "correct": True,
             "rationale": "Correct. Forwarding breaks SPF because the forwarder's IP is not authorized for the "
                          "original domain, but a properly scoped DKIM signature survives forwarding. Since DKIM "
                          "passed and aligned with the From: domain, DMARC passes on the DKIM path — one of the "
                          "reasons DKIM is important for forwarded mail."},
            {"id": "b", "text": "DMARC requires BOTH SPF and DKIM to pass, so this should have failed",
             "correct": False,
             "rationale": "Incorrect. DMARC requires only ONE aligned, passing mechanism (SPF OR DKIM). Here "
                          "DKIM satisfied it, so DMARC passed despite the SPF failure."},
            {"id": "c", "text": "SPF failures are ignored by DMARC entirely", "correct": False,
             "rationale": "Incorrect. DMARC does consider SPF; it simply also accepts DKIM. SPF is not ignored — "
                          "it just was not the mechanism that satisfied DMARC in this case."},
            {"id": "d", "text": "The forwarder re-signed the message as the original domain", "correct": False,
             "rationale": "Incorrect. The results show the original d=originaldomain.com signature still valid — "
                          "the forwarder did not (and normally cannot) sign as another domain. DKIM survived "
                          "forwarding intact."},
        ],
        "explanation": (
            "Forwarding commonly breaks SPF but preserves DKIM, and DMARC needs only one aligned pass. This is "
            "why DKIM matters for forwarded/mailing-list mail (and why ARC exists to preserve results)."
        ),
    },
    {
        "id": "tpke-023",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A security awareness scenario: users receive an email whose From: is 'ceo@company.com' asking for "
            "an urgent gift-card purchase. Header analysis shows dmarc=pass for company.com and the message "
            "genuinely originated from the company's own mail system. What does this tell the analyst?"
        ),
        "options": [
            {"id": "a", "text": "Email authentication passed, so this is likely a compromised internal account "
                                "or insider — not domain spoofing", "correct": True,
             "rationale": "Correct. DMARC/SPF/DKIM verify that the sending DOMAIN is legitimate; they do not "
                          "verify intent or that the human is trustworthy. A genuine dmarc=pass from the real "
                          "system points to account compromise (or insider abuse), which authentication cannot "
                          "catch — requiring behavioral/BEC controls instead."},
            {"id": "b", "text": "The message must be safe because DMARC passed", "correct": False,
             "rationale": "Incorrect. DMARC only proves the domain was not spoofed; it cannot tell whether the "
                          "account was hijacked or the request is fraudulent. A passing BEC email from a "
                          "compromised mailbox is still malicious."},
            {"id": "b2", "text": "This is definitely display-name spoofing from an external domain", "correct": False,
             "rationale": "Incorrect. dmarc=pass for company.com from the company's own system means it is NOT "
                          "external spoofing; the mail authentically came from inside, consistent with a "
                          "compromised account."},
            {"id": "d", "text": "SPF failed, which is why the email is suspicious", "correct": False,
             "rationale": "Incorrect. The scenario states DMARC passed (which implies an aligned SPF or DKIM "
                          "pass); SPF did not fail. The suspicion comes from the request/content, not an "
                          "authentication failure."},
        ],
        "explanation": (
            "Email authentication stops domain spoofing, not business email compromise from legitimate/"
            "hijacked accounts. Pair DMARC with BEC detection, out-of-band verification, and user training."
        ),
    },
    {
        "id": "tpke-024",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "Which TWO statements correctly describe the relationship between SPF, DKIM, and DMARC?"
        ),
        "options": [
            {"id": "a", "text": "DMARC builds on SPF and DKIM by adding From:-header alignment and a "
                                "published failure policy", "correct": True,
             "rationale": "Correct. DMARC does not replace SPF/DKIM; it leverages their results, adds the "
                          "requirement that a passing mechanism align with the visible From: domain, and lets "
                          "the domain owner publish a policy (none/quarantine/reject) plus reporting."},
            {"id": "b", "text": "SPF validates the envelope (MAIL FROM) sender, while the From: header is what "
                                "users see and what DMARC aligns against", "correct": True,
             "rationale": "Correct. SPF authenticates the envelope/return-path domain, which can differ from the "
                          "visible RFC5322 From: header; DMARC's alignment check ties authentication back to "
                          "that visible From: domain."},
            {"id": "c", "text": "DKIM encrypts the message so SPF can decrypt it at the destination",
             "correct": False,
             "rationale": "Incorrect. DKIM signs for integrity/authenticity and does not encrypt; SPF is an "
                          "IP-authorization check and performs no decryption. The two are independent "
                          "mechanisms, not an encrypt/decrypt pair."},
            {"id": "d", "text": "Publishing DMARC automatically creates SPF and DKIM records for you",
             "correct": False,
             "rationale": "Incorrect. SPF and DKIM must be configured independently; a DMARC record only "
                          "references their results and does not generate them. Without working SPF/DKIM, DMARC "
                          "has nothing to align."},
        ],
        "explanation": (
            "SPF = envelope IP authorization; DKIM = cryptographic signature/integrity; DMARC = alignment to "
            "the visible From: plus policy and reporting on top of the other two."
        ),
    },
    {
        "id": "tpke-025",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "An analyst inspects a suspicious email's full headers and finds the Received: chain shows the "
            "message first entered through 'mail.free-smtp-relay.xyz' before reaching the company gateway, and "
            "the From: displays 'billing@trustedvendor.com'. DMARC result is 'fail'. What is the BEST "
            "interpretation?"
        ),
        "options": [
            {"id": "a", "text": "The message is a spoof/phish impersonating the vendor; the failing DMARC and "
                                "untrusted originating relay confirm it did not come from the vendor",
             "correct": True,
             "rationale": "Correct. A DMARC fail on a message claiming to be from trustedvendor.com, combined "
                          "with an originating relay unrelated to the vendor in the Received: chain, indicates "
                          "the From: is forged and the mail should be quarantined/rejected."},
            {"id": "b", "text": "The Received: chain is irrelevant; only the From: header determines origin",
             "correct": False,
             "rationale": "Incorrect. The From: header is trivially forgeable; the Received: chain (added by each "
                          "hop) is a key forensic trail for tracing true origin, and here it contradicts the "
                          "claimed sender."},
            {"id": "c", "text": "A DMARC fail is normal for legitimate vendor mail and can be ignored",
             "correct": False,
             "rationale": "Incorrect. A well-configured legitimate vendor with DMARC should pass; a fail on "
                          "spoofable content from an unrelated relay is a strong phishing indicator, not "
                          "something to ignore."},
            {"id": "d", "text": "The message is safe because it reached the gateway", "correct": False,
             "rationale": "Incorrect. Reaching the gateway says nothing about legitimacy; the DMARC failure and "
                          "suspicious originating relay indicate spoofing regardless of successful delivery "
                          "attempt."},
        ],
        "explanation": (
            "Read headers bottom-up: the earliest Received: hop reveals true origin. Combined with a DMARC "
            "fail, an unrelated originating relay for a 'trusted vendor' From: is a clear spoofing signal."
        ),
    },
    {
        "id": "tpke-026",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A DKIM verification returns 'dkim=fail (body hash did not verify)'. SPF passed and is aligned, and "
            "the domain's DMARC is p=reject. The message still passed DMARC. Separately, why might the DKIM "
            "body hash fail even for a legitimate message?"
        ),
        "options": [
            {"id": "a", "text": "A device in transit (e.g., a mailing list or gateway) modified the body after "
                                "signing, invalidating the hash", "correct": True,
             "rationale": "Correct. DKIM signs a hash of the body; any in-transit modification — footer "
                          "injection by a list, content rewriting by a gateway, or reformatting — changes the "
                          "body so the recomputed hash no longer matches, causing a body-hash failure even for "
                          "genuine mail. (DMARC still passed here via aligned SPF.)"},
            {"id": "b", "text": "DKIM body hashes fail whenever TLS is used on the connection", "correct": False,
             "rationale": "Incorrect. TLS protects the transport hop and is unrelated to the DKIM body hash, "
                          "which is computed over the message content itself, not the connection."},
            {"id": "c", "text": "A failing body hash means the sender's SPF record is missing", "correct": False,
             "rationale": "Incorrect. SPF and DKIM are independent; a DKIM body-hash failure has nothing to do "
                          "with the presence of an SPF record (and the scenario states SPF passed)."},
            {"id": "d", "text": "It means the recipient's mailbox is full", "correct": False,
             "rationale": "Incorrect. Mailbox capacity is unrelated to DKIM verification; a body-hash failure is "
                          "about content being altered relative to what was signed."},
        ],
        "explanation": (
            "DKIM signs body + selected headers; any in-transit body change breaks the hash. This is common "
            "with mailing lists/gateways and is why DMARC accepts an aligned SPF pass as an alternative path."
        ),
    },
    {
        "id": "tpke-027",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "Which DNS record type and location is used to publish a domain's SPF policy?"
        ),
        "options": [
            {"id": "a", "text": "A TXT record at the domain root beginning with 'v=spf1'", "correct": True,
             "rationale": "Correct. SPF is published as a DNS TXT record on the domain (e.g., company.com) whose "
                          "value starts with 'v=spf1' and lists authorized sending mechanisms and an 'all' "
                          "qualifier."},
            {"id": "b", "text": "An MX record pointing to the authorized senders", "correct": False,
             "rationale": "Incorrect. MX records designate inbound mail servers for receiving mail; SPF's list "
                          "of authorized OUTBOUND senders is published in a TXT record, not MX."},
            {"id": "c", "text": "A dedicated SPF resource record type (RRTYPE 99)", "correct": False,
             "rationale": "Incorrect. The experimental SPF RRTYPE (99) was deprecated; SPF policies are "
                          "published in TXT records in practice."},
            {"id": "d", "text": "A CNAME record aliasing to the mail provider", "correct": False,
             "rationale": "Incorrect. CNAME aliases one name to another and is used for things like DKIM "
                          "selector delegation, not for publishing the SPF policy itself, which lives in a TXT "
                          "record."},
        ],
        "explanation": (
            "SPF lives in a TXT record (v=spf1 ...) at the domain. DKIM public keys live at "
            "selector._domainkey.domain (TXT), and DMARC at _dmarc.domain (TXT) — know where each is "
            "published."
        ),
    },
    {
        "id": "tpke-028",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A DKIM public key is published in DNS so receivers can verify signatures. At which DNS name is the "
            "DKIM public key for selector 's1' and domain 'company.com' found?"
        ),
        "options": [
            {"id": "a", "text": "s1._domainkey.company.com", "correct": True,
             "rationale": "Correct. DKIM public keys are published as TXT records at "
                          "<selector>._domainkey.<domain> — here s1._domainkey.company.com — which lets "
                          "receivers fetch the key referenced by the message's s= selector and d= domain."},
            {"id": "b", "text": "_dmarc.company.com", "correct": False,
             "rationale": "Incorrect. _dmarc.company.com hosts the DMARC policy record, not DKIM keys. DKIM keys "
                          "use the _domainkey subtree with a selector label."},
            {"id": "c", "text": "company.com (root TXT record)", "correct": False,
             "rationale": "Incorrect. The root TXT record commonly holds SPF; DKIM keys are published under a "
                          "selector-specific _domainkey name, not at the apex."},
            {"id": "d", "text": "dkim.company.com", "correct": False,
             "rationale": "Incorrect. The DKIM naming convention is <selector>._domainkey.<domain>, not a plain "
                          "'dkim' subdomain; receivers derive the lookup name from the message's selector."},
        ],
        "explanation": (
            "DKIM lookup name = <selector>._domainkey.<domain>. The message header carries s= (selector) and "
            "d= (domain), which the receiver combines to fetch the public key from DNS."
        ),
    },
    {
        "id": "tpke-029",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "An organization sees legitimate mail from a business unit getting rejected after moving DMARC to "
            "p=reject. Reports show that unit sends through a SaaS app that neither DKIM-signs as the corporate "
            "domain nor uses an aligned return-path. What is the correct resolution?"
        ),
        "options": [
            {"id": "a", "text": "Onboard the SaaS sender properly — configure aligned DKIM signing (or an "
                                "aligned MAIL FROM) for the corporate domain before enforcing reject",
             "correct": True,
             "rationale": "Correct. The rejection is legitimate mail failing alignment. The fix is to configure "
                          "the SaaS platform to authenticate as the corporate domain (delegated DKIM selector "
                          "or aligned return-path) so it passes DMARC, rather than loosening the org-wide "
                          "policy."},
            {"id": "b", "text": "Roll the entire domain back to p=none indefinitely", "correct": False,
             "rationale": "Incorrect. Reverting the whole domain to p=none to accommodate one misconfigured "
                          "sender removes spoofing protection everywhere; the right scope is fixing that "
                          "sender's authentication."},
            {"id": "c", "text": "Add +all to the SPF record to force a pass", "correct": False,
             "rationale": "Incorrect. '+all' authorizes every IP on the internet to send as your domain — a "
                          "catastrophic misconfiguration that invites spoofing. It is never an acceptable fix."},
            {"id": "d", "text": "Tell the business unit to stop using email", "correct": False,
             "rationale": "Incorrect. That is not a security control and ignores the real issue: the SaaS "
                          "sender simply needs to be configured to authenticate and align with the corporate "
                          "domain."},
        ],
        "explanation": (
            "Before enforcing p=reject, inventory and onboard every legitimate sender (delegated DKIM / aligned "
            "return-path) using rua reports. Fix the sender's alignment — never weaken SPF (+all) or the "
            "policy."
        ),
    },
    {
        "id": "tpke-030",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "Analysis of a phishing wave shows attackers registered 'c0mpany.com' (zero for the 'o') and sent "
            "mail that legitimately passes SPF, DKIM, and DMARC — for c0mpany.com. Which control category BEST "
            "addresses this specific technique?"
        ),
        "options": [
            {"id": "a", "text": "Look-alike/cousin-domain detection and user awareness — DMARC only protects "
                                "your exact domain, not confusingly similar ones", "correct": True,
             "rationale": "Correct. DMARC authenticates and protects your own domain; it cannot stop an attacker "
                          "who authenticates for a different, look-alike domain they legitimately control. "
                          "Defenses are homoglyph/look-alike domain monitoring, defensive registration, "
                          "external-sender banners, and user training."},
            {"id": "b", "text": "Strengthening your own DMARC to p=reject stops look-alike domains", "correct": False,
             "rationale": "Incorrect. Your DMARC policy governs only your domain; a separate domain like "
                          "c0mpany.com has its own DNS and can pass its own SPF/DKIM/DMARC, so tightening your "
                          "policy does not affect it."},
            {"id": "c", "text": "Adding the look-alike domain to your SPF record", "correct": False,
             "rationale": "Incorrect. You cannot and should not authorize an attacker-controlled domain in your "
                          "SPF; that would not even apply, since the look-alike sends under its own domain, not "
                          "yours."},
            {"id": "d", "text": "Enabling TLS on your mail gateway", "correct": False,
             "rationale": "Incorrect. TLS encrypts transport and does nothing to detect or block a cousin/"
                          "look-alike domain that authenticates for itself; this is a naming/impersonation "
                          "problem, not a transport-security one."},
        ],
        "explanation": (
            "Email authentication cannot stop look-alike domains that authenticate for themselves. Counter "
            "cousin-domain phishing with domain monitoring, defensive registration, external banners, and "
            "awareness training."
        ),
    },
]
