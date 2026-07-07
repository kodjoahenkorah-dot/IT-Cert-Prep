QUESTIONS = [
    # ── Q1 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A developer's workstation can browse HTTPS websites but cannot push code to a "
            "remote Git repository using SSH. The corporate firewall log shows outbound "
            "connections on port 22 are being dropped. Which firewall rule change is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Allow outbound TCP 22 to the Git server's IP",
                "correct": True,
                "rationale": (
                    "Correct. SSH uses TCP 22. Git over SSH requires an outbound TCP 22 "
                    "connection from the developer to the remote server. Permitting TCP 22 "
                    "outbound resolves the issue."
                ),
            },
            {
                "id": "b",
                "text": "Allow outbound TCP 443 to the Git server's IP",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 443 is HTTPS/TLS. Git over SSH uses TCP 22, not 443. "
                    "HTTPS git access would use a different URL scheme (https://) and the "
                    "developer is using SSH."
                ),
            },
            {
                "id": "c",
                "text": "Allow outbound UDP 22 to the Git server's IP",
                "correct": False,
                "rationale": (
                    "Incorrect. SSH operates over TCP, not UDP. UDP 22 is not used by SSH "
                    "and opening it would not restore SSH connectivity."
                ),
            },
            {
                "id": "d",
                "text": "Allow outbound TCP 3389 to the Git server's IP",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 3389 is Remote Desktop Protocol (RDP), used for graphical "
                    "remote-desktop sessions. It has nothing to do with SSH or Git."
                ),
            },
        ],
        "explanation": (
            "SSH (Secure Shell) uses TCP port 22 for all operations, including interactive "
            "terminal sessions and Git-over-SSH repository access. HTTPS-based Git uses TCP 443. "
            "When firewall logs show TCP 22 drops, the fix is to permit outbound TCP 22 to the "
            "specific server or destination range."
        ),
    },
    # ── Q2 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "An IT technician is configuring a new FTP server. The manager wants to allow "
            "passive FTP from internet clients. The firewall currently permits only TCP 21. "
            "After enabling passive mode on the FTP server, clients still cannot transfer "
            "files. What additional firewall rule is needed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Allow inbound TCP on the high ephemeral port range the FTP server advertises for passive data connections",
                "correct": True,
                "rationale": (
                    "Correct. In passive FTP, the server opens a random high port (1024–65535 "
                    "or a configured range) for data transfer and tells the client which port to "
                    "connect to. The firewall must permit inbound TCP connections to that port "
                    "range, in addition to TCP 21 for the control channel."
                ),
            },
            {
                "id": "b",
                "text": "Allow inbound TCP 20 for active FTP data transfer",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 20 is used in active FTP mode, where the server initiates "
                    "the data connection back to the client. The scenario specifies passive mode, "
                    "which does not use TCP 20 as an inbound connection from the server."
                ),
            },
            {
                "id": "c",
                "text": "Allow inbound UDP 21 alongside TCP 21",
                "correct": False,
                "rationale": (
                    "Incorrect. FTP uses TCP, not UDP. UDP 21 is not part of the FTP specification. "
                    "Adding a UDP 21 rule would not fix passive FTP data transfers."
                ),
            },
            {
                "id": "d",
                "text": "Replace FTP with TFTP on UDP 69 to avoid the dual-port issue",
                "correct": False,
                "rationale": (
                    "Incorrect. TFTP (Trivial File Transfer Protocol) on UDP 69 is a completely "
                    "different, unauthenticated file transfer protocol used for things like network "
                    "booting. It is not a solution for configuring internet FTP access."
                ),
            },
        ],
        "explanation": (
            "FTP has two channels: control (TCP 21) and data. In active mode, the server "
            "connects to the client on TCP 20; in passive mode, the server listens on a high "
            "ephemeral port and the client connects to it. Passive mode is firewall-friendly "
            "for clients but requires the server-side firewall to permit inbound connections "
            "on the configured passive port range."
        ),
    },
    # ── Q3 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Ports & protocols",
        "stem": (
            "A compliance officer discovers that a network appliance is sending syslog events "
            "to a SIEM over the default unencrypted port. The organization's security policy "
            "requires all log traffic to be encrypted in transit. Which port should the "
            "appliance be reconfigured to use for encrypted syslog delivery?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 6514",
                "correct": True,
                "rationale": (
                    "Correct. RFC 5425 defines syslog over TLS (Transport Layer Security) "
                    "on TCP 6514. This provides encrypted, authenticated log delivery, "
                    "satisfying the compliance requirement."
                ),
            },
            {
                "id": "b",
                "text": "UDP 514",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 514 is the default unencrypted syslog port (RFC 3164). "
                    "This is the port the appliance is already using — it does not provide "
                    "encryption."
                ),
            },
            {
                "id": "c",
                "text": "TCP 162",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 162 is the SNMP trap port. TCP 162 is not a standard "
                    "syslog transport and would not satisfy the encrypted syslog requirement."
                ),
            },
            {
                "id": "d",
                "text": "UDP 161",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 161 is the SNMP agent polling port. It is unrelated to "
                    "syslog and does not provide log encryption."
                ),
            },
        ],
        "explanation": (
            "Standard syslog (RFC 3164) uses UDP 514 with no encryption or authentication. "
            "RFC 5424/5425 defines syslog over TLS using TCP 6514 for secure, reliable log "
            "delivery. Security-conscious environments should migrate to TCP 6514 to protect "
            "log confidentiality and integrity. SNMP uses UDP 161/162 for a completely "
            "different monitoring function."
        ),
    },
    # ── Q4 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-004",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A technician runs 'nmap -sV 10.1.1.5' and sees port 389/tcp open with the "
            "service identified as 'ldap'. The organization's security team flags this as "
            "a risk because credentials traverse the network unencrypted. Which port and "
            "protocol should be used instead to encrypt directory queries?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 636 (LDAPS — LDAP over SSL/TLS)",
                "correct": True,
                "rationale": (
                    "Correct. LDAPS (LDAP over SSL/TLS) uses TCP 636 and wraps the LDAP "
                    "protocol in a TLS session, encrypting directory bind credentials and "
                    "query results. It is the encrypted alternative to plaintext LDAP on TCP 389."
                ),
            },
            {
                "id": "b",
                "text": "TCP 389 with NTLM authentication enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. NTLM authentication on port 389 still transmits LDAP attribute "
                    "data unencrypted. Enabling NTLM does not encrypt the LDAP traffic channel "
                    "itself."
                ),
            },
            {
                "id": "c",
                "text": "UDP 389 (LDAP over UDP for encryption)",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP can use UDP 389 for connectionless queries (e.g., ping "
                    "operations), but UDP does not add encryption. There is no 'LDAP over UDP "
                    "for encryption' standard."
                ),
            },
            {
                "id": "d",
                "text": "TCP 88 (Kerberos)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP/UDP 88 is Kerberos, an authentication protocol. While "
                    "Kerberos encrypts authentication tickets, it does not replace LDAP for "
                    "directory queries and does not run on the LDAP port."
                ),
            },
        ],
        "explanation": (
            "LDAP (Lightweight Directory Access Protocol) on TCP 389 transmits bind passwords "
            "and query data in cleartext. LDAPS on TCP 636 wraps LDAP in TLS, encrypting the "
            "entire session. Alternatively, LDAP with STARTTLS upgrades an existing TCP 389 "
            "connection to TLS, but TCP 636 with LDAPS is the traditional encrypted option. "
            "Kerberos (TCP/UDP 88) handles authentication tokens separately."
        ),
    },
    # ── Q5 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-005",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A help desk technician needs to use a Windows built-in tool to remotely control "
            "a user's desktop to assist with a software issue. The corporate firewall permits "
            "only specific ports. Which port must be open on the target workstation's firewall "
            "to allow an inbound RDP connection?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 3389",
                "correct": True,
                "rationale": (
                    "Correct. Remote Desktop Protocol (RDP) uses TCP 3389 by default for "
                    "inbound connections. The target workstation must have TCP 3389 permitted "
                    "through its local firewall and Remote Desktop must be enabled."
                ),
            },
            {
                "id": "b",
                "text": "TCP 5900",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 5900 is used by VNC (Virtual Network Computing), a "
                    "different remote desktop protocol. Windows RDP uses TCP 3389, not 5900."
                ),
            },
            {
                "id": "c",
                "text": "TCP 22",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 22 is SSH, which provides command-line remote access "
                    "on Linux/Unix systems. It does not provide Windows graphical remote desktop "
                    "functionality."
                ),
            },
            {
                "id": "d",
                "text": "UDP 3389",
                "correct": False,
                "rationale": (
                    "Incorrect. While RDP can optionally use UDP 3389 for multimedia streaming "
                    "enhancements (RDP 8.0+), the primary and required transport for an RDP "
                    "connection is TCP 3389. UDP alone is insufficient."
                ),
            },
        ],
        "explanation": (
            "RDP (Remote Desktop Protocol) uses TCP 3389 as its primary port. Windows Firewall "
            "must permit inbound TCP 3389 and Remote Desktop must be enabled via System Properties "
            "or Group Policy. VNC uses TCP 5900; SSH uses TCP 22. Modern RDP clients can also "
            "use UDP 3389 for enhanced multimedia, but TCP 3389 remains the required baseline."
        ),
    },
    # ── Q6 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-006",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Ports & protocols",
        "stem": (
            "A network printer is configured for IPP (Internet Printing Protocol) printing. "
            "A workstation cannot submit print jobs and the firewall log shows blocked "
            "outbound connections to the printer. IPP uses which port and transport by default?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 631",
                "correct": True,
                "rationale": (
                    "Correct. IPP (Internet Printing Protocol) uses TCP 631 by default. "
                    "It is the protocol behind CUPS (Common Unix Printing System) and modern "
                    "driverless printing (IPP Everywhere). Firewalls must permit TCP 631 for "
                    "IPP print jobs."
                ),
            },
            {
                "id": "b",
                "text": "TCP 9100",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 9100 is the raw/JetDirect printing port used by HP printers "
                    "and many network printers for direct socket-based print data transmission. "
                    "It is not the IPP port."
                ),
            },
            {
                "id": "c",
                "text": "UDP 515",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 515 is the LPD/LPR (Line Printer Daemon/Remote) port, "
                    "an older Unix printing protocol. IPP uses TCP 631, and the protocol is "
                    "TCP, not UDP."
                ),
            },
            {
                "id": "d",
                "text": "TCP 443",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 443 is HTTPS. While IPPS (IPP over TLS) does use TCP 443 "
                    "in some configurations for encrypted printing, the default unencrypted IPP "
                    "port is TCP 631."
                ),
            },
        ],
        "explanation": (
            "IPP (Internet Printing Protocol) is the modern cross-platform printing protocol "
            "defined in RFC 8011, using TCP 631. CUPS on Linux/macOS uses IPP natively. "
            "Compare with: LPD/LPR = TCP 515; raw/JetDirect = TCP 9100; IPPS (encrypted) = "
            "TCP 443. Knowing these printer ports is commonly tested on CompTIA A+."
        ),
    },
    # ── Q7 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "A technician is connecting a new network switch to an existing switch to expand "
            "port count. The link between the two switches must carry traffic for VLANs 10, "
            "20, and 30. Which type of port configuration must be used on the connecting "
            "ports of both switches?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trunk port with 802.1Q tagging enabled for all three VLANs",
                "correct": True,
                "rationale": (
                    "Correct. A trunk port carries traffic for multiple VLANs simultaneously "
                    "by tagging frames with 802.1Q VLAN IDs. Both inter-switch ports must be "
                    "configured as trunk ports with VLANs 10, 20, and 30 permitted."
                ),
            },
            {
                "id": "b",
                "text": "Three separate access ports, one for each VLAN, with three physical cables",
                "correct": False,
                "rationale": (
                    "Incorrect. While this would technically work, it wastes ports and cables. "
                    "Trunk ports are the designed solution for carrying multiple VLANs over a "
                    "single physical link."
                ),
            },
            {
                "id": "c",
                "text": "Access port assigned to VLAN 1 as the native VLAN",
                "correct": False,
                "rationale": (
                    "Incorrect. An access port carries traffic for only one VLAN. Assigning the "
                    "inter-switch link to VLAN 1 as an access port would not pass traffic for "
                    "VLANs 10, 20, or 30."
                ),
            },
            {
                "id": "d",
                "text": "Routed port with an IP address on each VLAN's subnet",
                "correct": False,
                "rationale": (
                    "Incorrect. Routed (Layer 3) ports are used for inter-VLAN routing, not "
                    "for simple Layer 2 switch-to-switch connectivity. Trunk ports with 802.1Q "
                    "are the correct choice for this scenario."
                ),
            },
        ],
        "explanation": (
            "Inter-switch links (ISLs) that must carry traffic for multiple VLANs must be "
            "configured as 802.1Q trunk ports on both ends. Trunk ports insert a 4-byte 802.1Q "
            "tag into Ethernet frames to identify the VLAN. Access ports carry only a single "
            "VLAN (untagged) and are used for end-device connections."
        ),
    },
    # ── Q8 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "After a core switch fails, the network operations team discovers there was no "
            "redundant path between the distribution layer and access-layer switches. "
            "They want to add a redundant uplink but prevent broadcast storms caused by "
            "the resulting loop. Which protocol automatically blocks redundant Layer 2 "
            "paths to prevent loops while keeping the backup link ready?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spanning Tree Protocol (STP / 802.1D)",
                "correct": True,
                "rationale": (
                    "Correct. STP (IEEE 802.1D) detects Layer 2 loops, elects a root bridge, "
                    "and places redundant ports into a blocking state. If the active path fails, "
                    "STP transitions the blocked port to forwarding, restoring connectivity."
                ),
            },
            {
                "id": "b",
                "text": "OSPF (Open Shortest Path First)",
                "correct": False,
                "rationale": (
                    "Incorrect. OSPF is a Layer 3 routing protocol that handles IP route "
                    "selection between routers. It does not operate at Layer 2 and cannot "
                    "prevent Ethernet broadcast storms caused by switching loops."
                ),
            },
            {
                "id": "c",
                "text": "NAT (Network Address Translation)",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates IP addresses between private and public networks. "
                    "It operates at Layer 3/4 and has no ability to detect or prevent Layer 2 "
                    "switching loops."
                ),
            },
            {
                "id": "d",
                "text": "LACP (Link Aggregation Control Protocol)",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP (802.3ad) bundles multiple physical links into one logical "
                    "link for increased bandwidth and redundancy. However, it does not handle "
                    "separate redundant loop-prevention; STP is still needed for that."
                ),
            },
        ],
        "explanation": (
            "STP (IEEE 802.1D) prevents Layer 2 broadcast storms by placing redundant switch "
            "ports into a Blocking state. RSTP (802.1w) is the faster-converging successor. "
            "The root bridge is elected by lowest Bridge ID; non-root ports that would create "
            "loops are blocked. On failure, STP reconverges to use the backup path."
        ),
    },
    # ── Q9 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-009",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "PoE",
        "stem": (
            "A technician is deploying a pan-tilt-zoom (PTZ) security camera that requires "
            "71 W of continuous power and is IEEE 802.3bt compliant. The existing switch "
            "has 802.3at (PoE+) ports. Why will the camera fail to operate at full capacity, "
            "and which standard is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.3at delivers a maximum of 30 W at the port; 802.3bt Type 3 (up to 60 W) or Type 4 (up to 90 W) is required for a 71 W device",
                "correct": True,
                "rationale": (
                    "Correct. IEEE 802.3at (PoE+) provides up to 30 W at the PSE port. A "
                    "71 W PTZ camera requires 802.3bt Type 4, which delivers up to 90 W at "
                    "the port (~71.3 W at the powered device after cable loss)."
                ),
            },
            {
                "id": "b",
                "text": "802.3at only works with Cat 5e; the camera requires Cat 8 cabling",
                "correct": False,
                "rationale": (
                    "Incorrect. Cabling category is not the limiting factor. 802.3at works "
                    "with Cat 5e or better. The constraint is the maximum wattage — 30 W for "
                    "802.3at versus the camera's 71 W requirement."
                ),
            },
            {
                "id": "c",
                "text": "PoE cannot power devices above 25 W regardless of the standard used",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.3bt (PoE++) Type 3 delivers up to 60 W and Type 4 up to "
                    "90 W. The 25 W ceiling applies only to 802.3af (15.4 W) and 802.3at (30 W)."
                ),
            },
            {
                "id": "d",
                "text": "802.3at supports four-pair power delivery sufficient for 71 W devices",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.3at uses two pairs and is capped at 30 W. Four-pair "
                    "power delivery is a feature of 802.3bt, not 802.3at."
                ),
            },
        ],
        "explanation": (
            "PoE power budget by standard: 802.3af (PoE) = 15.4 W at port; "
            "802.3at (PoE+) = 30 W at port; 802.3bt Type 3 (PoE++) = 60 W at port; "
            "802.3bt Type 4 (PoE++) = 90 W at port. For a 71 W PTZ camera, 802.3bt Type 4 "
            "is required. Always verify both the PSE (switch) and PD (device) standards match."
        ),
    },
    # ── Q10 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A warehouse deploys handheld barcode scanners that use 802.11b/g. A new AP "
            "is added supporting 802.11a/b/g/n/ac. After the upgrade, the scanners connect "
            "but the warehouse manager reports that the new AP seems to run at the speed of "
            "the old scanners rather than full 802.11ac speeds. What is MOST likely happening?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The 802.11b clients are causing protection mechanisms (RTS/CTS) that slow all devices on the same 2.4 GHz channel",
                "correct": True,
                "rationale": (
                    "Correct. When 802.11b devices share a 2.4 GHz BSS with faster clients, "
                    "the AP enables 802.11b protection (ERP-OFDM / RTS-CTS or CTS-to-self) "
                    "to prevent collisions. This overhead significantly reduces the throughput "
                    "of all devices on that channel."
                ),
            },
            {
                "id": "b",
                "text": "802.11ac is incompatible with 802.11b hardware and the scanners should disconnect",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11ac operates on 5 GHz and is backward compatible via the "
                    "AP's 2.4 GHz radio, which supports 802.11b/g/n. The scanners can connect "
                    "but trigger protection overhead."
                ),
            },
            {
                "id": "c",
                "text": "The AP automatically upgrades the scanners' firmware to 802.11n",
                "correct": False,
                "rationale": (
                    "Incorrect. APs do not flash or upgrade the firmware of connected client "
                    "devices. The scanners remain 802.11b/g hardware regardless of the AP upgrade."
                ),
            },
            {
                "id": "d",
                "text": "The AP defaults to 802.11a mode because it is the fastest and drops b/g support",
                "correct": False,
                "rationale": (
                    "Incorrect. The AP supports multiple modes simultaneously on different radios. "
                    "802.11a uses 5 GHz; 802.11b/g uses 2.4 GHz. The AP will not drop 2.4 GHz "
                    "support automatically."
                ),
            },
        ],
        "explanation": (
            "Legacy 802.11b devices use DSSS modulation; faster devices use OFDM. When both "
            "share the same BSS, the AP activates ERP (Extended Rate Protection) mode, adding "
            "RTS/CTS or CTS-to-self overhead before every OFDM frame. This drastically reduces "
            "effective throughput. The fix is to disable 802.11b rates on the AP or use a "
            "dedicated 5 GHz SSID for faster clients."
        ),
    },
    # ── Q11 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wi-Fi channels & frequencies",
        "stem": (
            "A network administrator configures two neighboring APs in a 5 GHz deployment "
            "and sets both to channel 100. Users connected to both APs report intermittent "
            "disconnections when nearby radar systems operate. What feature must be enabled "
            "on the APs to legally operate on channel 100 in the U.S., and what does it do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DFS (Dynamic Frequency Selection) — detects radar signals and automatically moves to a different channel",
                "correct": True,
                "rationale": (
                    "Correct. Channel 100 is in the UNII-2e band, which requires DFS per FCC "
                    "regulations. DFS causes the AP to continuously monitor for radar; upon "
                    "detection it must vacate the channel within 10 seconds and stay off it "
                    "for 30 minutes."
                ),
            },
            {
                "id": "b",
                "text": "TPC (Transmit Power Control) — reduces AP power to avoid interfering with radar",
                "correct": False,
                "rationale": (
                    "Incorrect. TPC (Transmit Power Control) reduces transmit power to minimize "
                    "interference, but it does not detect radar or vacate channels. DFS is the "
                    "required mechanism for radar avoidance on UNII-2/2e channels."
                ),
            },
            {
                "id": "c",
                "text": "Band steering — moves clients from 5 GHz to 2.4 GHz when radar is detected",
                "correct": False,
                "rationale": (
                    "Incorrect. Band steering moves clients between frequency bands for load "
                    "balancing purposes. It is not a regulatory radar-avoidance mechanism and "
                    "does not satisfy the DFS requirement."
                ),
            },
            {
                "id": "d",
                "text": "Beamforming — focuses the Wi-Fi signal away from radar sources",
                "correct": False,
                "rationale": (
                    "Incorrect. Beamforming focuses signal toward clients to improve throughput "
                    "and range. It does not detect or respond to radar and does not fulfill the "
                    "regulatory DFS requirement for UNII-2/2e channels."
                ),
            },
        ],
        "explanation": (
            "5 GHz channels 52–144 (UNII-2 and UNII-2e) require DFS (Dynamic Frequency "
            "Selection) and TPC per FCC Part 15 rules because they share spectrum with "
            "weather radar, military radar, and TDWR systems. APs must detect radar and "
            "switch channels within 10 seconds. UNII-1 (36–48) and UNII-3 (149–165) do not "
            "require DFS in the U.S."
        ),
    },
    # ── Q12 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A building automation system uses a mesh network of low-power sensors that "
            "report temperature and humidity to a central controller. The sensors run on "
            "AA batteries and must last at least two years. Data packets are small (< 100 "
            "bytes) and infrequent. Which wireless standard is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Zigbee (IEEE 802.15.4)",
                "correct": True,
                "rationale": (
                    "Correct. Zigbee is designed for low-power, low-data-rate IoT mesh "
                    "networking. It operates in the 2.4 GHz band, supports mesh topology, "
                    "and is optimized for battery-powered sensors with multi-year battery life."
                ),
            },
            {
                "id": "b",
                "text": "802.11ax (Wi-Fi 6)",
                "correct": False,
                "rationale": (
                    "Incorrect. While Wi-Fi 6 has improved power efficiency (TWT), it is "
                    "far too power-hungry for battery-operated IoT sensors requiring two-year "
                    "battery life. It is designed for high-throughput client devices."
                ),
            },
            {
                "id": "c",
                "text": "Bluetooth Classic (BR/EDR)",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth Classic is designed for continuous audio and data "
                    "streaming, not low-power IoT sensor mesh networks. Bluetooth LE would be "
                    "a closer fit, but Zigbee is the industry standard for building automation."
                ),
            },
            {
                "id": "d",
                "text": "LTE Cat-M1 (cellular IoT)",
                "correct": False,
                "rationale": (
                    "Incorrect. LTE Cat-M1 is a cellular IoT standard requiring SIM cards "
                    "and carrier infrastructure. It is appropriate for wide-area IoT, not "
                    "indoor building automation mesh networks on battery power."
                ),
            },
        ],
        "explanation": (
            "Zigbee (IEEE 802.15.4) operates at 250 kbps on 2.4 GHz, supports mesh networking "
            "with up to thousands of nodes, and is specifically designed for low-power sensors. "
            "It dominates building automation (thermostats, sensors, smart lighting). Compare "
            "with Z-Wave (proprietary, 908 MHz), Bluetooth LE (point-to-point/star), and "
            "Thread (newer IPv6-based mesh protocol for IoT)."
        ),
    },
    # ── Q13 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-013",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network services",
        "stem": (
            "An organization wants to allow employees to browse the internet while preventing "
            "access to social media and streaming video sites during business hours. All web "
            "traffic should be inspected for malware before reaching client machines. "
            "Which network appliance/service should be deployed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Proxy server with content filtering and SSL inspection",
                "correct": True,
                "rationale": (
                    "Correct. A forward proxy with URL/category-based content filtering blocks "
                    "social media and streaming categories. SSL/TLS inspection (HTTPS inspection) "
                    "allows the proxy to scan encrypted traffic for malware before forwarding it "
                    "to the client."
                ),
            },
            {
                "id": "b",
                "text": "DNS server with split-horizon zones for internal resolution",
                "correct": False,
                "rationale": (
                    "Incorrect. Split-horizon DNS serves different answers to internal vs. "
                    "external queries but does not block category-based web access or scan "
                    "traffic for malware."
                ),
            },
            {
                "id": "c",
                "text": "DHCP server with scope options restricting client MAC addresses",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP scope options configure client network parameters (gateway, "
                    "DNS). DHCP cannot filter web categories or inspect traffic for malware."
                ),
            },
            {
                "id": "d",
                "text": "Load balancer distributing traffic across multiple ISP uplinks",
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes traffic for redundancy and bandwidth "
                    "aggregation. It does not perform URL filtering or malware scanning."
                ),
            },
        ],
        "explanation": (
            "A forward proxy server intercepts client HTTP/HTTPS requests, applies URL and "
            "category filtering policies, and can perform SSL inspection (HTTPS decryption/re-"
            "encryption) to scan encrypted web traffic for malware. This is the standard "
            "enterprise solution for web content control. UTM appliances often incorporate "
            "proxy functionality alongside firewall and IPS."
        ),
    },
    # ── Q14 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-014",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network services",
        "stem": (
            "A company's web application receives an unexpected traffic spike that overwhelms "
            "a single IP address. The operations team wants to distribute requests so that "
            "each client session always returns to the same backend server (session persistence). "
            "Which load-balancing method achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sticky sessions (session affinity / source IP persistence)",
                "correct": True,
                "rationale": (
                    "Correct. Sticky sessions bind a client's requests to the same backend server "
                    "using the client's source IP or a session cookie. This ensures stateful "
                    "application sessions (e.g., shopping carts) remain on the same server."
                ),
            },
            {
                "id": "b",
                "text": "Round-robin distribution",
                "correct": False,
                "rationale": (
                    "Incorrect. Round-robin evenly cycles requests across servers in order. "
                    "It does not guarantee the same client always returns to the same server, "
                    "which breaks session state in stateful applications."
                ),
            },
            {
                "id": "c",
                "text": "Least-connections algorithm",
                "correct": False,
                "rationale": (
                    "Incorrect. Least-connections sends each new request to the server with "
                    "the fewest active connections. It optimizes server utilization but does "
                    "not maintain session persistence for a specific client."
                ),
            },
            {
                "id": "d",
                "text": "Weighted round-robin with health checking",
                "correct": False,
                "rationale": (
                    "Incorrect. Weighted round-robin assigns more traffic to higher-capacity "
                    "servers but still distributes individual client requests across multiple "
                    "servers without session persistence."
                ),
            },
        ],
        "explanation": (
            "Session persistence (sticky sessions) ensures a client is always directed to the "
            "same backend server during a session. Methods include source IP affinity (hash "
            "the client IP) or cookie-based persistence (insert a cookie identifying the server). "
            "Without persistence, stateful apps (shopping carts, authenticated sessions) fail "
            "when requests hit different servers lacking shared session state."
        ),
    },
    # ── Q15 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-015",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A network engineer is given the block 172.16.50.0/23 and must create four "
            "equal-sized subnets. What is the correct subnet mask for each subnet, how many "
            "usable hosts does each provide, and what is the first usable host of the third subnet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mask /25 (255.255.255.128); 126 usable hosts each; first usable host of third subnet is 172.16.51.128.1 — which is invalid; correct third subnet first usable is 172.16.51.129",
                "correct": False,
                "rationale": (
                    "Incorrect. /25 from a /23 base creates 4 subnets of 128 addresses (126 "
                    "usable), but the address math here is wrong. /23 spans 172.16.50.0–172.16.51.255 "
                    "(512 addresses). Splitting into 4 equal subnets gives /25 blocks: "
                    "172.16.50.0/25, 172.16.50.128/25, 172.16.51.0/25, 172.16.51.128/25. "
                    "The third subnet's first usable host is 172.16.51.1, not 172.16.51.129."
                ),
            },
            {
                "id": "b",
                "text": "Mask /25 (255.255.255.128); 126 usable hosts each; first usable host of third subnet is 172.16.51.1",
                "correct": True,
                "rationale": (
                    "Correct. A /23 block has 512 addresses. Dividing into 4 equal subnets "
                    "requires borrowing 2 more bits: /23 + 2 = /25. Each /25 has 128 addresses "
                    "(126 usable). The four subnets are: 172.16.50.0/25, 172.16.50.128/25, "
                    "172.16.51.0/25, 172.16.51.128/25. Third subnet network = 172.16.51.0; "
                    "first usable host = 172.16.51.1."
                ),
            },
            {
                "id": "c",
                "text": "Mask /24 (255.255.255.0); 254 usable hosts each; first usable host of third subnet is 172.16.52.1",
                "correct": False,
                "rationale": (
                    "Incorrect. /24 from a /23 base creates only 2 subnets (172.16.50.0/24 "
                    "and 172.16.51.0/24), not 4. The address 172.16.52.1 is outside the /23 "
                    "block entirely."
                ),
            },
            {
                "id": "d",
                "text": "Mask /26 (255.255.255.192); 62 usable hosts each; first usable host of third subnet is 172.16.50.129",
                "correct": False,
                "rationale": (
                    "Incorrect. /26 from a /23 base creates 8 subnets of 64 addresses each "
                    "(62 usable), not 4. To create exactly 4 equal subnets from /23, /25 is "
                    "correct."
                ),
            },
        ],
        "explanation": (
            "172.16.50.0/23 contains 2^(32-23) = 512 addresses (172.16.50.0–172.16.51.255). "
            "To split into 4 equal subnets: borrow 2 bits → /25. Each /25 = 128 addresses, "
            "126 usable. Subnet 1: 172.16.50.0/25 (.0–.127); Subnet 2: 172.16.50.128/25 "
            "(.128–.255); Subnet 3: 172.16.51.0/25 (.0–.127 in .51 octet); Subnet 4: "
            "172.16.51.128/25 (.128–.255). Third subnet first usable = 172.16.51.1."
        ),
    },
    # ── Q16 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A host is assigned 192.168.4.97/28. A technician needs to identify the network "
            "address, broadcast address, and valid host range for this subnet. Which answer "
            "is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Network: 192.168.4.96, Broadcast: 192.168.4.111, Hosts: 192.168.4.97–192.168.4.110",
                "correct": True,
                "rationale": (
                    "Correct. /28 = 255.255.255.240. Block size = 256 - 240 = 16. "
                    "Subnet boundaries at multiples of 16: .80, .96, .112. The host .97 falls "
                    "in the .96 block. Network = .96, Broadcast = .111, usable range = .97–.110."
                ),
            },
            {
                "id": "b",
                "text": "Network: 192.168.4.80, Broadcast: 192.168.4.95, Hosts: 192.168.4.81–192.168.4.94",
                "correct": False,
                "rationale": (
                    "Incorrect. The .80 subnet spans .80–.95. The host .97 is not in this subnet. "
                    "It falls in the next /28 block starting at .96."
                ),
            },
            {
                "id": "c",
                "text": "Network: 192.168.4.96, Broadcast: 192.168.4.127, Hosts: 192.168.4.97–192.168.4.126",
                "correct": False,
                "rationale": (
                    "Incorrect. A /28 has 16 addresses (block size 16), not 32. The broadcast "
                    "for the .96/28 subnet is .111, not .127. .127 would be the broadcast of a "
                    "/25 subnet."
                ),
            },
            {
                "id": "d",
                "text": "Network: 192.168.4.64, Broadcast: 192.168.4.127, Hosts: 192.168.4.65–192.168.4.126",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a /26 subnet (block size 64). A /28 has a block "
                    "size of 16. The host .97 belongs to the /28 block starting at .96."
                ),
            },
        ],
        "explanation": (
            "/28 = 255.255.255.240. Block size = 256 - 240 = 16. Subnet increments: "
            ".0, .16, .32, .48, .64, .80, .96, .112 … The host 192.168.4.97 falls in the "
            ".96 block. Network = 192.168.4.96, Broadcast = 192.168.4.111 (.96 + 16 - 1), "
            "Usable hosts = .97–.110 (14 hosts)."
        ),
    },
    # ── Q17 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 addressing",
        "stem": (
            "An IPv6-enabled workstation receives the prefix 2001:db8:abcd:1::/64 via a "
            "Router Advertisement. Using SLAAC with EUI-64, the workstation has a MAC address "
            "of A4:C3:F0:12:34:56. Which statement about the resulting interface identifier "
            "is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "EUI-64 inserts FFFE in the middle of the MAC, flips the 7th bit of the first byte, producing an IID of A6:C3:F0:FF:FE:12:34:56",
                "correct": True,
                "rationale": (
                    "Correct. EUI-64 converts a 48-bit MAC to a 64-bit IID by inserting FF:FE "
                    "between bytes 3 and 4, then flipping the Universal/Local (U/L) bit — the "
                    "7th bit of the first byte. A4 = 10100100; flipping bit 7 → 10100110 = A6. "
                    "IID = A6C3:F0FF:FE12:3456."
                ),
            },
            {
                "id": "b",
                "text": "SLAAC generates a random 64-bit IID and ignores the MAC address for privacy",
                "correct": False,
                "rationale": (
                    "Incorrect. Classic EUI-64 SLAAC derives the IID from the MAC address. "
                    "Privacy extensions (RFC 4941) generate a random IID, but the question "
                    "specifically asks about EUI-64."
                ),
            },
            {
                "id": "c",
                "text": "EUI-64 appends 0000 to the end of the MAC address to form the IID",
                "correct": False,
                "rationale": (
                    "Incorrect. EUI-64 inserts FF:FE in the middle (between bytes 3 and 4) and "
                    "flips the U/L bit. It does not simply append zeros to the MAC address."
                ),
            },
            {
                "id": "d",
                "text": "The router assigns a /128 address to the workstation based on its MAC via DHCPv6",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes SLAAC (Stateless Address Autoconfiguration) "
                    "via Router Advertisement, not DHCPv6. SLAAC allows the host to self-generate "
                    "its full /128 address using the advertised prefix and EUI-64."
                ),
            },
        ],
        "explanation": (
            "IPv6 SLAAC EUI-64 process: (1) Split the 48-bit MAC at byte 3; (2) Insert FF:FE "
            "between bytes 3 and 4 to create a 64-bit value; (3) Flip the U/L bit (bit 7, "
            "counting from left) of the first byte. For MAC A4:C3:F0:12:34:56 → IID = "
            "A6C3:F0FF:FE12:3456. Full address = 2001:db8:abcd:1:a6c3:f0ff:fe12:3456."
        ),
    },
    # ── Q18 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP",
        "stem": (
            "A network technician notices that clients in a remote building are obtaining IP "
            "addresses in the 192.168.1.0/24 range from the central DHCP server, even though "
            "the remote building is on a different subnet (192.168.5.0/24) separated by a "
            "router. What must be configured on the router to allow remote DHCP functionality?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP relay agent (ip helper-address) on the router interface facing the remote subnet",
                "correct": True,
                "rationale": (
                    "Correct. DHCP Discover and Request messages are broadcasts that cannot "
                    "cross router boundaries. A DHCP relay agent (configured with the DHCP "
                    "server's unicast IP via 'ip helper-address') forwards client broadcasts "
                    "as unicast packets to the DHCP server."
                ),
            },
            {
                "id": "b",
                "text": "A second DHCP server deployed in the remote building",
                "correct": False,
                "rationale": (
                    "Incorrect. A local DHCP server would work but contradicts the scenario "
                    "where the central DHCP server is intended to serve both subnets. A relay "
                    "agent is the correct solution for extending a single DHCP server across "
                    "multiple subnets."
                ),
            },
            {
                "id": "c",
                "text": "Enable IP directed broadcasts on the router to forward DHCP broadcasts",
                "correct": False,
                "rationale": (
                    "Incorrect. IP directed broadcast forwarding is a separate feature that "
                    "carries security risks (Smurf amplification attacks) and is not the "
                    "recommended mechanism. DHCP relay is the proper solution."
                ),
            },
            {
                "id": "d",
                "text": "Configure a static route on the DHCP server pointing to the remote subnet",
                "correct": False,
                "rationale": (
                    "Incorrect. A static route on the DHCP server would not help because DHCP "
                    "Discover packets are L2 broadcasts and never reach the server across a "
                    "router without a relay agent — routing is irrelevant at the broadcast level."
                ),
            },
        ],
        "explanation": (
            "DHCP uses UDP broadcast (255.255.255.255 or subnet-directed broadcast) which routers "
            "do not forward by default. A DHCP relay agent (RFC 1542, 'ip helper-address' in "
            "Cisco IOS) on the router converts client broadcasts to unicast DHCP messages "
            "directed at the DHCP server. The server uses the relay's source IP (giaddr) to "
            "select the correct scope for the remote subnet."
        ),
    },
    # ── Q19 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP",
        "stem": (
            "A DHCP server administrator shortens the default lease time from 8 days to "
            "1 hour for a wireless guest network that hosts hundreds of short-visit users. "
            "Which consequence of this change must the administrator plan for?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Increased DHCP traffic as clients renew leases more frequently, potentially overloading the DHCP server",
                "correct": True,
                "rationale": (
                    "Correct. With 1-hour leases, clients attempt renewal at 30 minutes "
                    "(T1 = 50% of lease) and rebind at 52.5 minutes (T2 = 87.5%). Hundreds of "
                    "short-visit clients cycling through 1-hour leases generate significantly "
                    "more DHCP traffic than with 8-day leases, increasing server load."
                ),
            },
            {
                "id": "b",
                "text": "The DHCP scope will run out of addresses faster because short leases cannot be reused",
                "correct": False,
                "rationale": (
                    "Incorrect. Shorter leases actually help address reuse by returning "
                    "addresses to the pool sooner after clients disconnect. Address exhaustion "
                    "is less likely, not more, with short leases."
                ),
            },
            {
                "id": "c",
                "text": "Clients will receive static IP addresses because DHCP renewal is too frequent",
                "correct": False,
                "rationale": (
                    "Incorrect. Frequent renewals do not cause clients to switch to static "
                    "addressing. DHCP clients continue using dynamic addressing regardless of "
                    "lease duration."
                ),
            },
            {
                "id": "d",
                "text": "DNS records for guest devices will be permanently cached for 8 days by external resolvers",
                "correct": False,
                "rationale": (
                    "Incorrect. Guest wireless clients typically do not have DNS records "
                    "registered for external resolution. DNS TTLs are independently configurable "
                    "and are unrelated to DHCP lease duration."
                ),
            },
        ],
        "explanation": (
            "DHCP lease duration is a trade-off: longer leases reduce DHCP server load but "
            "waste addresses when clients disconnect; shorter leases free addresses quickly "
            "but increase renewal traffic. For high-turnover environments (guest Wi-Fi, "
            "conference rooms), short leases (1–4 hours) are appropriate but require a "
            "DHCP server capable of handling the higher transaction rate. T1 = 50% of lease "
            "(renewal), T2 = 87.5% (rebind)."
        ),
    },
    # ── Q20 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-020",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DNS records",
        "stem": (
            "A technician uses 'nslookup 203.0.113.77' and gets no result. The A record for "
            "the corresponding hostname exists in the forward lookup zone. What additional "
            "DNS record must be created to allow IP-to-hostname resolution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PTR record in the 113.0.203.in-addr.arpa reverse lookup zone",
                "correct": True,
                "rationale": (
                    "Correct. A PTR (Pointer) record maps an IP address to a hostname in a "
                    "reverse lookup zone. For 203.0.113.77, the PTR record is "
                    "77.113.0.203.in-addr.arpa → hostname. Without a PTR record, reverse "
                    "DNS lookups return no result."
                ),
            },
            {
                "id": "b",
                "text": "AAAA record mapping the hostname to 203.0.113.77",
                "correct": False,
                "rationale": (
                    "Incorrect. An AAAA record maps a hostname to an IPv6 address. "
                    "203.0.113.77 is an IPv4 address. AAAA records do not enable reverse DNS "
                    "lookup (IP to hostname)."
                ),
            },
            {
                "id": "c",
                "text": "CNAME record aliasing 203.0.113.77 to the hostname",
                "correct": False,
                "rationale": (
                    "Incorrect. CNAME records create hostname-to-hostname aliases, not "
                    "IP-to-hostname mappings. A CNAME cannot point to or from an IP address."
                ),
            },
            {
                "id": "d",
                "text": "SOA record updating the zone's serial number for the forward zone",
                "correct": False,
                "rationale": (
                    "Incorrect. The SOA (Start of Authority) record contains zone metadata "
                    "(serial, refresh, retry intervals) and has nothing to do with reverse "
                    "IP-to-hostname resolution."
                ),
            },
        ],
        "explanation": (
            "Reverse DNS resolution maps an IP address to a hostname using PTR records in "
            "special reverse lookup zones (in-addr.arpa for IPv4, ip6.arpa for IPv6). "
            "For 203.0.113.77, the PTR record lives at 77.113.0.203.in-addr.arpa. Many "
            "services (email deliverability, SSH, syslog) depend on valid PTR records. "
            "Forward A records alone do not enable reverse lookup."
        ),
    },
    # ── Q21 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-021",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DNS records",
        "stem": (
            "A company hosts multiple services on a single IP address (203.0.113.10) and "
            "wants mail.company.com, vpn.company.com, and ftp.company.com to all resolve to "
            "that IP without creating individual A records for each. Which DNS record type "
            "allows these hostnames to be aliased to a single canonical hostname that has "
            "the A record?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CNAME records for each alias pointing to a single canonical hostname",
                "correct": True,
                "rationale": (
                    "Correct. CNAME (Canonical Name) records create hostname aliases. "
                    "mail.company.com → services.company.com (CNAME); services.company.com "
                    "→ 203.0.113.10 (A record). Changing the A record automatically updates "
                    "all CNAMEs pointing to the canonical name."
                ),
            },
            {
                "id": "b",
                "text": "Multiple A records for each service hostname pointing directly to 203.0.113.10",
                "correct": False,
                "rationale": (
                    "Incorrect. This would work but creates maintenance overhead — changing "
                    "the IP requires updating every A record individually. CNAMEs + one A "
                    "record is the more maintainable solution the question asks for."
                ),
            },
            {
                "id": "c",
                "text": "MX records for each service hostname pointing to 203.0.113.10",
                "correct": False,
                "rationale": (
                    "Incorrect. MX (Mail Exchanger) records are exclusively for designating "
                    "mail servers for a domain. They cannot be used as general-purpose hostname "
                    "aliases."
                ),
            },
            {
                "id": "d",
                "text": "NS records delegating each subdomain to 203.0.113.10",
                "correct": False,
                "rationale": (
                    "Incorrect. NS (Name Server) records delegate DNS authority for a zone to "
                    "specific name servers. They are not used for hostname-to-IP aliasing."
                ),
            },
        ],
        "explanation": (
            "CNAME records create aliases: the alias name resolves to the canonical name's A "
            "record. This simplifies IP changes (only the A record needs updating) and "
            "reduces duplication. Important limitation: CNAME cannot coexist with other record "
            "types at the same name (especially the zone apex/root), so CNAMEs cannot be used "
            "for bare domain names like company.com itself (use ALIAS/ANAME or A record instead)."
        ),
    },
    # ── Q22 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-022",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLAN/VPN",
        "stem": (
            "A managed switch port is configured as an access port on VLAN 30. A new IP "
            "phone is plugged into that port, and the phone's PC port connects a workstation. "
            "The switch detects the phone via LLDP-MED and assigns voice VLAN 40 to the "
            "phone. Which statement accurately describes the resulting traffic behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The phone sends 802.1Q-tagged frames with VLAN ID 40; the workstation sends untagged frames on VLAN 30; both coexist on the single physical port",
                "correct": True,
                "rationale": (
                    "Correct. The voice VLAN feature allows one port to carry both untagged "
                    "data VLAN traffic (VLAN 30, for the PC) and 802.1Q-tagged voice VLAN "
                    "traffic (VLAN 40, tagged by the phone). The switch handles both on the "
                    "single port."
                ),
            },
            {
                "id": "b",
                "text": "The workstation is automatically placed on VLAN 40 because it shares a port with the phone",
                "correct": False,
                "rationale": (
                    "Incorrect. The workstation connected through the phone's data port receives "
                    "untagged traffic on the configured access VLAN (VLAN 30), not the voice VLAN. "
                    "The phone separates and tags its own voice traffic."
                ),
            },
            {
                "id": "c",
                "text": "The port must be reconfigured as a trunk to support two VLANs, and the workstation must be VLAN-capable",
                "correct": False,
                "rationale": (
                    "Incorrect. The voice VLAN feature specifically avoids requiring a full "
                    "trunk configuration or VLAN-aware workstation. The switch handles tagging "
                    "for the phone; the workstation sees only untagged data-VLAN traffic."
                ),
            },
            {
                "id": "d",
                "text": "The native VLAN changes to VLAN 40 for all frames including the workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. The native VLAN (untagged VLAN) remains VLAN 30 for the "
                    "workstation. Only the phone's traffic is tagged with VLAN 40. The native "
                    "VLAN does not change."
                ),
            },
        ],
        "explanation": (
            "The voice VLAN (auxiliary VLAN) feature lets a single access port carry two "
            "VLANs: the PC's traffic is untagged on the data VLAN; the IP phone tags its "
            "own RTP/SIP traffic with the voice VLAN ID using 802.1Q. The phone learns the "
            "voice VLAN ID via CDP or LLDP-MED. This eliminates the need for separate "
            "cabling while maintaining QoS and security separation."
        ),
    },
    # ── Q23 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-023",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "VLAN/VPN",
        "stem": (
            "Two branch offices need secure connectivity over the public internet. The "
            "connection must encrypt all site-to-site traffic, support routing protocols "
            "between the sites, and be transparent to end users. The IT team wants to avoid "
            "per-user VPN client software. Which VPN type is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "IPSec tunnel mode site-to-site VPN between the branch routers/firewalls",
                "correct": True,
                "rationale": (
                    "Correct. IPSec in tunnel mode encapsulates entire IP packets between two "
                    "gateways (routers/firewalls), encrypting all site-to-site traffic. It is "
                    "transparent to end users, supports routing protocols (GRE over IPSec), "
                    "and requires no per-user client software."
                ),
            },
            {
                "id": "b",
                "text": "SSL/TLS clientless VPN portal on each branch's web server",
                "correct": False,
                "rationale": (
                    "Incorrect. A clientless SSL VPN portal provides browser-based access to "
                    "specific web applications — it does not create a network-layer tunnel that "
                    "transparently connects two sites or supports routing protocols."
                ),
            },
            {
                "id": "c",
                "text": "PPTP VPN with MPPE encryption on each branch router",
                "correct": False,
                "rationale": (
                    "Incorrect. PPTP (Point-to-Point Tunneling Protocol) with MPPE is a legacy, "
                    "deprecated protocol with known cryptographic weaknesses. It should not be "
                    "used for new site-to-site VPN deployments."
                ),
            },
            {
                "id": "d",
                "text": "Remote access VPN with individual client certificates for each employee",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote access VPNs are designed for individual users connecting "
                    "from outside the office — they require client software or certificates per "
                    "user. Site-to-site IPSec is the designed solution for connecting entire "
                    "office networks."
                ),
            },
        ],
        "explanation": (
            "Site-to-site IPSec VPNs connect two entire networks via gateway devices "
            "(routers or firewalls), encrypting all inter-site traffic in tunnel mode. "
            "GRE (Generic Routing Encapsulation) over IPSec adds support for multicast "
            "and dynamic routing protocols. End users have no VPN client; the gateway "
            "handles all encryption transparently. This is the enterprise standard for "
            "branch interconnection over the public internet."
        ),
    },
    # ── Q24 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-024",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Internet connection types",
        "stem": (
            "A SOHO customer has a DSL connection with a rated speed of 50 Mbps down / 10 "
            "Mbps up. The customer reports that downstream speeds are always much higher than "
            "upstream. Which DSL characteristic explains this inherent asymmetry?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ADSL allocates more subcarriers in the downstream direction because residential users download more than they upload",
                "correct": True,
                "rationale": (
                    "Correct. ADSL (Asymmetric DSL) intentionally allocates more DMT subcarriers "
                    "for downstream than upstream, matching the typical residential usage pattern "
                    "of heavy downloading and light uploading. This asymmetry is a design feature, "
                    "not a defect."
                ),
            },
            {
                "id": "b",
                "text": "DSL signal degrades faster in the upstream direction due to twisted-pair copper resistance",
                "correct": False,
                "rationale": (
                    "Incorrect. Upstream and downstream signals experience similar attenuation "
                    "on copper. The asymmetry is an intentional engineering choice about frequency "
                    "band allocation, not a result of directional resistance differences."
                ),
            },
            {
                "id": "c",
                "text": "The ISP throttles upstream traffic to prevent customers from running servers",
                "correct": False,
                "rationale": (
                    "Incorrect. While ISPs may enforce AUP restrictions, the fundamental "
                    "asymmetry of ADSL is an inherent technical design — it exists even before "
                    "any policy throttling is applied."
                ),
            },
            {
                "id": "d",
                "text": "Full-duplex copper cannot support equal speeds in both directions simultaneously",
                "correct": False,
                "rationale": (
                    "Incorrect. DSL uses frequency division to achieve full-duplex over a single "
                    "copper pair. SDSL (Symmetric DSL) achieves equal speeds in both directions — "
                    "proving the asymmetry is a design choice, not a physical limitation of "
                    "full-duplex copper."
                ),
            },
        ],
        "explanation": (
            "ADSL (Asymmetric DSL) uses DMT (Discrete Multi-Tone) modulation, dividing the "
            "copper line's frequency spectrum into 256 subcarriers (bins). Downstream uses "
            "many more bins than upstream (e.g., bins 32–255 down, 6–31 up). SDSL allocates "
            "bins equally for symmetric speeds. Fiber-based internet (GPON) and cable (DOCSIS) "
            "can also be asymmetric but for different technical reasons."
        ),
    },
    # ── Q25 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-025",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Internet connection types",
        "stem": (
            "A business subscribes to a dedicated internet connection where the provider "
            "guarantees that the subscribed bandwidth is available 100% of the time and is "
            "not shared with other customers. Upload and download speeds are equal. "
            "Which type of connection is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dedicated leased line (e.g., T1/T3 or Dedicated Ethernet)",
                "correct": True,
                "rationale": (
                    "Correct. A dedicated leased line (T1, T3, or modern dedicated Ethernet "
                    "circuits) provides guaranteed, unshared symmetric bandwidth with an SLA. "
                    "Unlike consumer broadband, bandwidth is never shared with other customers."
                ),
            },
            {
                "id": "b",
                "text": "Cable broadband (DOCSIS)",
                "correct": False,
                "rationale": (
                    "Incorrect. DOCSIS cable internet uses shared downstream bandwidth among "
                    "neighbors on the same cable node. Speeds vary with neighborhood usage "
                    "and are inherently asymmetric. It does not provide guaranteed dedicated "
                    "bandwidth."
                ),
            },
            {
                "id": "c",
                "text": "ADSL2+ (Asymmetric DSL)",
                "correct": False,
                "rationale": (
                    "Incorrect. ADSL2+ is asymmetric (faster down than up) and shares DSLAM "
                    "uplinks with other subscribers. It does not provide guaranteed dedicated "
                    "symmetric bandwidth."
                ),
            },
            {
                "id": "d",
                "text": "Fixed wireless access (FWA) using 5G NR",
                "correct": False,
                "rationale": (
                    "Incorrect. Fixed wireless access shares a cellular base station's spectrum "
                    "among users. While fast, it does not typically offer guaranteed dedicated "
                    "bandwidth with an SLA equivalent to a leased line."
                ),
            },
        ],
        "explanation": (
            "Dedicated leased lines (T1 = 1.544 Mbps, T3 = 44.736 Mbps, or dedicated Ethernet "
            "circuits at 10/100/1000 Mbps+) provide point-to-point connectivity with guaranteed, "
            "unshared, symmetric bandwidth backed by SLAs. They are more expensive than shared "
            "broadband but essential for businesses requiring predictable performance and uptime "
            "guarantees."
        ),
    },
    # ── Q26 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-026",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network types (LAN/WAN/PAN)",
        "stem": (
            "A university has multiple buildings across a 2-mile campus connected by a "
            "high-speed fiber backbone it owns and operates. Each building has its own LAN. "
            "The fiber backbone linking the buildings is too large for a LAN but confined "
            "to the campus — it does not span a city. What type of network describes "
            "the campus backbone?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CAN (Campus Area Network)",
                "correct": True,
                "rationale": (
                    "Correct. A CAN (Campus Area Network) covers a geographically limited area "
                    "such as a university campus or corporate park — larger than a LAN but "
                    "smaller than a MAN. It is owned by the organization and connects multiple "
                    "buildings on a single property."
                ),
            },
            {
                "id": "b",
                "text": "WAN (Wide Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAN spans large geographic areas (cities, countries) and "
                    "typically uses third-party carrier services. A campus fiber backbone "
                    "confined to a 2-mile area does not qualify as a WAN."
                ),
            },
            {
                "id": "c",
                "text": "MAN (Metropolitan Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A MAN spans a city or metropolitan area, typically using ISP "
                    "or carrier infrastructure. A 2-mile campus network is smaller in scope "
                    "than a MAN."
                ),
            },
            {
                "id": "d",
                "text": "PAN (Personal Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A PAN covers very short distances (< 10 m) for personal "
                    "devices like headsets, watches, and phones. It bears no resemblance to "
                    "a multi-building campus backbone."
                ),
            },
        ],
        "explanation": (
            "Network scope hierarchy: PAN < LAN < CAN (campus) < MAN (metro/city) < WAN "
            "(wide area). A CAN (also sometimes called a corporate area network) is the "
            "network within a campus or multi-building facility owned by one organization. "
            "It is a common but sometimes overlooked network type on the A+ exam."
        ),
    },
    # ── Q27 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-027",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A fiber optic cable installer is testing a newly installed multimode OM4 "
            "cable run. The optical power meter shows high insertion loss. The technician "
            "suspects dirty connectors. Before cleaning, which tool should be used to "
            "visually inspect the fiber end-face for contamination or damage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fiber inspection scope (fiber microscope / video inspection probe)",
                "correct": True,
                "rationale": (
                    "Correct. A fiber inspection scope or video inspection probe (VIP) "
                    "magnifies the fiber end-face (200x–400x) to reveal contamination, "
                    "scratches, chips, or cracks. Inspection before cleaning confirms the "
                    "problem and after cleaning verifies the result."
                ),
            },
            {
                "id": "b",
                "text": "Optical time-domain reflectometer (OTDR)",
                "correct": False,
                "rationale": (
                    "Incorrect. An OTDR sends light pulses into the fiber and analyzes "
                    "reflections to locate splices, breaks, and attenuation events. It does "
                    "not visually inspect the connector end-face for contamination."
                ),
            },
            {
                "id": "c",
                "text": "Tone generator and probe (Fox and Hound)",
                "correct": False,
                "rationale": (
                    "Incorrect. A tone generator and probe are used to trace and identify "
                    "copper cable pairs. They do not work with fiber optic cables."
                ),
            },
            {
                "id": "d",
                "text": "Multimeter with continuity tester",
                "correct": False,
                "rationale": (
                    "Incorrect. A multimeter tests electrical continuity and voltage on copper "
                    "conductors. Fiber optic cables carry light, not electricity, so a "
                    "multimeter cannot test or inspect fiber end-faces."
                ),
            },
        ],
        "explanation": (
            "Dirty fiber connectors are the most common cause of fiber link failures. The "
            "correct procedure is: inspect with a fiber scope → clean with dry cassette "
            "cleaner or IPA wipe → re-inspect to confirm cleanliness. An OTDR measures "
            "link length and identifies macro-faults; an optical power meter measures "
            "loss; a fiber scope inspects the physical end-face condition."
        ),
    },
    # ── Q28 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-028",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A technician is installing a structured cabling system and must choose between "
            "single-mode and multimode fiber for a 400-meter run inside a large office "
            "complex. Cost is a concern. Which fiber type is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Multimode fiber (OM3 or OM4) with 850 nm transceivers",
                "correct": True,
                "rationale": (
                    "Correct. OM3 multimode fiber supports 10GBase-SR up to 300 m and 40/100G "
                    "at shorter distances; OM4 extends to 400 m for 10G. Multimode uses less "
                    "expensive VCSELs (850 nm) rather than the laser diodes required by "
                    "single-mode. For intra-building 400 m runs, OM4 multimode is standard "
                    "and cost-effective."
                ),
            },
            {
                "id": "b",
                "text": "Single-mode fiber (OS2) with 1310 nm transceivers",
                "correct": False,
                "rationale": (
                    "Incorrect. Single-mode fiber and 1310 nm transceivers are more expensive "
                    "than multimode. While OS2 single-mode easily supports 400 m and much "
                    "longer runs, it is cost-overkill for an intra-building installation within "
                    "multimode's range."
                ),
            },
            {
                "id": "c",
                "text": "Cat 6a UTP copper at 10GBase-T",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 6a copper supports 10GBase-T up to 100 m. A 400-meter run "
                    "far exceeds copper's maximum segment length. Fiber is required for this "
                    "distance."
                ),
            },
            {
                "id": "d",
                "text": "Multimode OM1 fiber with 62.5 µm core diameter",
                "correct": False,
                "rationale": (
                    "Incorrect. OM1 (62.5 µm) is legacy multimode that supports 10GBase-SR "
                    "only to 33 m. At 400 m, OM1 is insufficient for 10G. OM3 or OM4 is "
                    "required."
                ),
            },
        ],
        "explanation": (
            "Fiber type selection: OM1 (62.5 µm, legacy) < OM2 (50 µm) < OM3 (50 µm laser-"
            "optimized, 10G to 300 m) < OM4 (50 µm, 10G to 400 m) < OM5 (wideband). "
            "Single-mode OS1/OS2 supports kilometers but costs more (laser sources). "
            "For intra-building runs ≤ 400 m, OM4 is the cost-effective choice. Copper "
            "max is 100 m for any speed."
        ),
    },
    # ── Q29 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-029",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "T568A/B wiring",
        "stem": (
            "A technician is punching down a Cat 6 cable into a 110-style patch panel and "
            "must follow T568B wiring. The cable has arrived with the following visible pair "
            "colors: blue, orange, green, brown. Which color should be punched on pin 1 "
            "of the T568B patch panel?"
        ),
        "options": [
            {
                "id": "a",
                "text": "White/Orange (the white-striped wire of the orange pair)",
                "correct": True,
                "rationale": (
                    "Correct. T568B pin order: 1=W/O, 2=O, 3=W/G, 4=BL, 5=W/BL, 6=G, "
                    "7=W/BR, 8=BR. Pin 1 receives the white-orange wire (white with orange "
                    "stripe, or orange with white stripe — the striped/tip wire of the "
                    "orange pair)."
                ),
            },
            {
                "id": "b",
                "text": "White/Green (the white-striped wire of the green pair)",
                "correct": False,
                "rationale": (
                    "Incorrect. White/Green is T568B pin 3, not pin 1. In T568A, White/Green "
                    "is pin 1. This is a common confusion between the two standards."
                ),
            },
            {
                "id": "c",
                "text": "Blue (the solid blue wire of the blue pair)",
                "correct": False,
                "rationale": (
                    "Incorrect. Solid Blue is T568B pin 4 (and T568A pin 4). It is never "
                    "placed on pin 1 in either wiring standard."
                ),
            },
            {
                "id": "d",
                "text": "White/Blue (the white-striped wire of the blue pair)",
                "correct": False,
                "rationale": (
                    "Incorrect. White/Blue is T568B pin 5 (and T568A pin 5). It is the tip "
                    "of the blue pair and belongs on pin 5 in both T568A and T568B."
                ),
            },
        ],
        "explanation": (
            "T568B pin assignments: 1=W/Orange, 2=Orange, 3=W/Green, 4=Blue, 5=W/Blue, "
            "6=Green, 7=W/Brown, 8=Brown. T568A swaps the orange and green pairs: "
            "1=W/Green, 2=Green, 3=W/Orange, 6=Orange. The key difference between A and B "
            "is which color appears on pins 1/2 vs 3/6. T568B is more common in North America."
        ),
    },
    # ── Q30 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-030",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A technician uses Wireshark on a workstation and captures a UDP packet destined "
            "for port 69 on a server. The payload contains a request for 'router-config.txt'. "
            "Which protocol is being used, and what is its primary use case?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TFTP (Trivial File Transfer Protocol) — used for diskless booting and transferring router/switch configuration files",
                "correct": True,
                "rationale": (
                    "Correct. TFTP uses UDP 69 and is a simple, authentication-free file "
                    "transfer protocol. It is widely used to transfer router/switch configs, "
                    "firmware images, and PXE boot files (boot ROM images). Requesting "
                    "'router-config.txt' confirms TFTP usage."
                ),
            },
            {
                "id": "b",
                "text": "FTP (File Transfer Protocol) — used for authenticated file uploads and downloads",
                "correct": False,
                "rationale": (
                    "Incorrect. FTP uses TCP 20/21, not UDP 69. FTP provides authentication "
                    "and reliable transfer. The capture clearly shows UDP 69 which is TFTP."
                ),
            },
            {
                "id": "c",
                "text": "SFTP (SSH File Transfer Protocol) — used for encrypted file transfer over SSH",
                "correct": False,
                "rationale": (
                    "Incorrect. SFTP runs over SSH on TCP 22. It uses TCP, not UDP, and operates "
                    "on port 22 — not port 69."
                ),
            },
            {
                "id": "d",
                "text": "DNS (Domain Name System) — requesting a TXT record named 'router-config'",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS uses UDP 53, not UDP 69. DNS query format is entirely "
                    "different from a TFTP read request."
                ),
            },
        ],
        "explanation": (
            "TFTP (Trivial File Transfer Protocol) — UDP 69 — is a lightweight, unauthenticated "
            "file transfer protocol. It is used for: PXE/network booting (transferring boot "
            "images to diskless clients); router/switch IOS/firmware upgrades; configuration "
            "backups on network devices. Its simplicity (no authentication, no directory "
            "listing) makes it unsuitable for general file sharing but ideal for embedded "
            "device workflows."
        ),
    },
    # ── Q31 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-031",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A technician is designing a network and needs to accommodate exactly 500 hosts "
            "on a single subnet, while wasting as few addresses as possible. The ISP assigns "
            "the block 10.10.0.0/16. Which subnet mask provides exactly enough space for "
            "500 hosts with minimum address waste?"
        ),
        "options": [
            {
                "id": "a",
                "text": "/23 (255.255.254.0) — 510 usable hosts",
                "correct": True,
                "rationale": (
                    "Correct. /23 provides 2^9 - 2 = 510 usable host addresses, which is the "
                    "smallest subnet that accommodates 500 hosts. /24 provides only 254, which "
                    "is insufficient. /22 provides 1022, which wastes more than /23."
                ),
            },
            {
                "id": "b",
                "text": "/24 (255.255.255.0) — 254 usable hosts",
                "correct": False,
                "rationale": (
                    "Incorrect. A /24 provides only 254 usable hosts, which is insufficient "
                    "for 500 hosts. A larger subnet (smaller mask number) is required."
                ),
            },
            {
                "id": "c",
                "text": "/22 (255.255.252.0) — 1022 usable hosts",
                "correct": False,
                "rationale": (
                    "Incorrect. A /22 provides 1022 usable hosts, which accommodates 500 but "
                    "wastes over 500 addresses. /23 is the more efficient choice for exactly "
                    "500 hosts."
                ),
            },
            {
                "id": "d",
                "text": "/25 (255.255.255.128) — 126 usable hosts",
                "correct": False,
                "rationale": (
                    "Incorrect. A /25 provides only 126 usable hosts — far fewer than the "
                    "500 required. This subnet is too small."
                ),
            },
        ],
        "explanation": (
            "To find the minimum subnet for N hosts: find the smallest power of 2 greater "
            "than N+2, then calculate the prefix. For 500 hosts: need at least 502 addresses "
            "→ 2^9 = 512 → /32-9 = /23. /23 gives 512 addresses, 510 usable (512-2). "
            "/24 = 256 addresses / 254 usable (insufficient). Always choose the smallest "
            "subnet that fits, not just the smallest subnet that seems 'close.'"
        ),
    },
    # ── Q32 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-032",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Internet connection types",
        "stem": (
            "A retail chain is deploying credit card payment terminals at 50 small kiosk "
            "locations where no wired broadband is available. Each location needs low-latency "
            "internet connectivity for PCI-DSS compliant transactions. The solution must be "
            "rapidly deployable. Which connection type is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cellular 4G LTE with a fixed wireless router at each kiosk",
                "correct": True,
                "rationale": (
                    "Correct. 4G LTE cellular internet is rapidly deployable (SIM card "
                    "activation), provides low latency (20–60 ms), adequate throughput for "
                    "payment processing, and is available wherever mobile coverage exists. "
                    "A cellular router provides wired connections for the terminals."
                ),
            },
            {
                "id": "b",
                "text": "Geostationary satellite internet at each kiosk",
                "correct": False,
                "rationale": (
                    "Incorrect. Geostationary satellite has latency of 500–600 ms, which "
                    "can cause payment transaction timeouts and a poor user experience. "
                    "It also requires dish installation, making deployment slower and more complex."
                ),
            },
            {
                "id": "c",
                "text": "ISDN BRI (Integrated Services Digital Network Basic Rate Interface)",
                "correct": False,
                "rationale": (
                    "Incorrect. ISDN BRI is a legacy technology (128 kbps, two B channels) "
                    "that has been largely decommissioned. It is not a viable choice for new "
                    "deployments at 50 kiosk locations."
                ),
            },
            {
                "id": "d",
                "text": "Dial-up modem over POTS at 56 kbps",
                "correct": False,
                "rationale": (
                    "Incorrect. Dial-up (56 kbps) is far too slow for modern PCI-DSS compliant "
                    "payment processing, which requires faster, more reliable connections. "
                    "Dial-up is also functionally obsolete."
                ),
            },
        ],
        "explanation": (
            "Cellular LTE/5G provides on-demand, rapidly deployable broadband with acceptable "
            "latency for payment transactions. For IoT, POS, and kiosk applications without "
            "fixed-line infrastructure, cellular is the standard solution. Geostationary "
            "satellite's 500+ ms latency is a deal-breaker for interactive transactions. "
            "Low-Earth orbit satellite (Starlink) is improving latency to 20–40 ms but "
            "requires dish installation."
        ),
    },
    # ── Q33 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-033",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "A security administrator wants to monitor all traffic passing between the core "
            "switch and the internet firewall without disrupting production traffic. A network "
            "tap is not available. Which managed switch feature copies all traffic from the "
            "uplink port to a designated analysis port?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Port mirroring (SPAN — Switch Port Analyzer)",
                "correct": True,
                "rationale": (
                    "Correct. SPAN (Switch Port Analyzer) or port mirroring copies ingress "
                    "and/or egress traffic from a source port (or VLAN) to a destination port "
                    "where a network analyzer or IDS sensor is connected — without interrupting "
                    "production traffic."
                ),
            },
            {
                "id": "b",
                "text": "Port security with MAC address filtering",
                "correct": False,
                "rationale": (
                    "Incorrect. Port security limits which MAC addresses can connect to a port "
                    "to prevent rogue devices. It does not copy or forward traffic to an "
                    "analysis device."
                ),
            },
            {
                "id": "c",
                "text": "QoS policy marking voice traffic with DSCP EF",
                "correct": False,
                "rationale": (
                    "Incorrect. QoS (Quality of Service) policies prioritize traffic types "
                    "by marking DSCP values. They do not copy traffic to monitoring interfaces."
                ),
            },
            {
                "id": "d",
                "text": "VLAN pruning to restrict broadcast domains",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN pruning limits which VLANs are allowed on trunk ports "
                    "to reduce unnecessary broadcast traffic. It is a traffic management "
                    "feature, not a monitoring feature."
                ),
            },
        ],
        "explanation": (
            "SPAN (Switch Port Analyzer) / port mirroring sends copies of specified traffic "
            "to a monitoring port. Source can be one or more ports or a VLAN; destination is "
            "the analysis port (IDS sensor, Wireshark workstation, etc.). RSPAN (Remote SPAN) "
            "extends this across a network. A dedicated network tap provides non-intrusive "
            "passive copying but requires hardware insertion in the cable path."
        ),
    },
    # ── Q34 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-034",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A user reports that their smartphone's Wi-Fi signal shows full bars but internet "
            "browsing is extremely slow. Other users on the same AP are also experiencing "
            "slowdowns. A site survey reveals 8 APs from neighboring offices are all "
            "broadcasting on 5 GHz channel 36. What is the MOST likely cause of the slowdown "
            "and what should be done?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Co-channel interference (CCI) from multiple APs on channel 36; reassign APs to non-overlapping 5 GHz channels",
                "correct": True,
                "rationale": (
                    "Correct. When multiple APs use the same channel in overlapping RF "
                    "coverage areas, they contend for the same medium causing co-channel "
                    "interference. Clients see strong signal (RSSI) but low throughput because "
                    "they must wait for competing APs and clients to finish transmitting. "
                    "Assigning different non-overlapping 5 GHz channels eliminates CCI."
                ),
            },
            {
                "id": "b",
                "text": "The DHCP scope is exhausted and clients are receiving APIPA addresses",
                "correct": False,
                "rationale": (
                    "Incorrect. APIPA addresses (169.254.x.x) would prevent connectivity "
                    "entirely, not cause slow browsing. The symptom of 'full bars, slow speed' "
                    "points to a wireless medium contention issue, not an IP addressing problem."
                ),
            },
            {
                "id": "c",
                "text": "The AP is using WPA2 encryption, which degrades performance compared to open networks",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2/WPA3 encryption has negligible performance impact on "
                    "modern hardware. Encryption is not the cause of the described slowdown "
                    "when multiple APs share the same channel."
                ),
            },
            {
                "id": "d",
                "text": "The AP is operating in 802.11b compatibility mode, limiting speeds to 11 Mbps",
                "correct": False,
                "rationale": (
                    "Incorrect. Channel 36 is a 5 GHz channel; 802.11b only operates on "
                    "2.4 GHz. An AP on 5 GHz channel 36 cannot be in 802.11b mode."
                ),
            },
        ],
        "explanation": (
            "Co-channel interference (CCI) occurs when multiple APs share the same frequency "
            "channel in overlapping areas. All devices on the same channel share one collision "
            "domain (CSMA/CA), so adding more APs/clients on the same channel reduces—not "
            "increases—effective throughput. The 5 GHz band's 25 non-overlapping 20 MHz "
            "channels allow proper channel planning to avoid CCI."
        ),
    },
    # ── Q35 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-035",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 addressing",
        "stem": (
            "An administrator is reviewing IPv6 addresses on a Windows server and sees the "
            "address ::1 assigned to the loopback interface. A second address begins with "
            "fc00::. What type of address is fc00:: and what is its intended use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unique Local Address (ULA, fc00::/7) — equivalent to RFC 1918 private addressing; routable within an organization but not on the global internet",
                "correct": True,
                "rationale": (
                    "Correct. ULA (Unique Local Address) uses the fc00::/7 prefix (fc00:: or "
                    "fd00:: with L bit). Like IPv4 private ranges (10/8, 172.16/12, 192.168/16), "
                    "ULAs are not routable on the public internet but are used for internal "
                    "intra-organization traffic."
                ),
            },
            {
                "id": "b",
                "text": "Global unicast address — fully routable on the public IPv6 internet",
                "correct": False,
                "rationale": (
                    "Incorrect. Global unicast addresses use the 2000::/3 prefix. fc00::/7 "
                    "is explicitly defined as Unique Local and is not globally routable."
                ),
            },
            {
                "id": "c",
                "text": "Multicast address — used to send packets to a group of interfaces",
                "correct": False,
                "rationale": (
                    "Incorrect. IPv6 multicast uses the ff00::/8 prefix. fc00:: is a unicast "
                    "address type (Unique Local), not multicast."
                ),
            },
            {
                "id": "d",
                "text": "Link-local address — valid only on the directly connected link",
                "correct": False,
                "rationale": (
                    "Incorrect. Link-local addresses use the fe80::/10 prefix. fc00::/7 "
                    "(Unique Local) is valid beyond the local link and can be routed within "
                    "the organization, unlike link-local addresses."
                ),
            },
        ],
        "explanation": (
            "IPv6 address type prefixes: ::1/128 = loopback; fe80::/10 = link-local (auto); "
            "fc00::/7 (fd00::/8 in practice) = Unique Local Address (ULA), analogous to "
            "RFC 1918 private; 2000::/3 = global unicast (internet-routable); ff00::/8 = "
            "multicast. ULA was standardized in RFC 4193 as the IPv6 successor to private "
            "IPv4 addressing."
        ),
    },
    # ── Q36 — multiple_response ──────────────────────────────────────────────
    {
        "id": "a1d2v3-036",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A firewall administrator is creating an allow rule for secure email services. "
            "Which TWO ports are associated with encrypted email protocols? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 993 (IMAPS — IMAP over SSL/TLS)",
                "correct": True,
                "rationale": (
                    "Correct. TCP 993 is IMAPS, which wraps IMAP email retrieval in SSL/TLS. "
                    "It is the encrypted version of IMAP (TCP 143) and is used for secure "
                    "mobile and desktop email client connections."
                ),
            },
            {
                "id": "b",
                "text": "TCP 995 (POP3S — POP3 over SSL/TLS)",
                "correct": True,
                "rationale": (
                    "Correct. TCP 995 is POP3S, the SSL/TLS-encrypted version of POP3 "
                    "(TCP 110). It allows email clients to securely download messages from "
                    "a mail server."
                ),
            },
            {
                "id": "c",
                "text": "TCP 25 (SMTP — Simple Mail Transfer Protocol)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 25 is standard (unencrypted) SMTP used for server-to-server "
                    "mail relay. It is not an encrypted email protocol. SMTPS uses TCP 465, "
                    "and SMTP with STARTTLS uses TCP 587."
                ),
            },
            {
                "id": "d",
                "text": "TCP 110 (POP3 — Post Office Protocol v3)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 110 is standard (unencrypted) POP3. The encrypted version "
                    "is POP3S on TCP 995. TCP 110 should not be permitted when the requirement "
                    "is for encrypted email."
                ),
            },
        ],
        "explanation": (
            "Encrypted email port summary: IMAPS = TCP 993 (IMAP + SSL/TLS); "
            "POP3S = TCP 995 (POP3 + SSL/TLS); SMTPS = TCP 465 (SMTP + SSL/TLS); "
            "SMTP STARTTLS = TCP 587. The unencrypted counterparts are IMAP TCP 143, "
            "POP3 TCP 110, and SMTP TCP 25. Modern deployments should prefer the "
            "encrypted ports for all client connections."
        ),
    },
    # ── Q37 — multiple_response ──────────────────────────────────────────────
    {
        "id": "a1d2v3-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A technician is troubleshooting two hosts that are in the same /24 subnet "
            "but cannot communicate. Host A has IP 10.1.10.50/24 and Host B has IP "
            "10.1.10.180/24 with subnet mask 255.255.255.240. Which TWO statements "
            "correctly identify the problem? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Host B's subnet mask (/28) places it in a different subnet than Host A (/24), so they cannot communicate at Layer 2 without a router",
                "correct": True,
                "rationale": (
                    "Correct. Host B uses /28 (255.255.255.240), placing it in the subnet "
                    "10.1.10.176/28 (range .176–.191). Host A uses /24, placing its subnet "
                    "as 10.1.10.0/24. Because Host B's mask is inconsistent with the intended "
                    "/24, it calculates its network as .176, not .0 — they are on different "
                    "logical subnets from Host B's perspective."
                ),
            },
            {
                "id": "b",
                "text": "The subnet mask mismatch is the root cause; Host B should be corrected to 255.255.255.0 (/24) to match Host A",
                "correct": True,
                "rationale": (
                    "Correct. The fix is to correct Host B's subnet mask to /24 "
                    "(255.255.255.0). After correction, both hosts will be in 10.1.10.0/24 "
                    "and communicate directly at Layer 2."
                ),
            },
            {
                "id": "c",
                "text": "The hosts cannot communicate because they are in different Class A networks",
                "correct": False,
                "rationale": (
                    "Incorrect. Both hosts share the same first three octets (10.1.10.x), so "
                    "classful network membership is not the issue. The problem is the subnet "
                    "mask mismatch, not class boundaries."
                ),
            },
            {
                "id": "d",
                "text": "A new router must be deployed between the hosts to resolve the routing between /24 and /28",
                "correct": False,
                "rationale": (
                    "Incorrect. The correct fix is to correct the misconfigured subnet mask on "
                    "Host B, not to add a router. Adding a router would work around the problem "
                    "but does not resolve the misconfiguration."
                ),
            },
        ],
        "explanation": (
            "Subnet mask mismatches (VLSM inconsistencies) cause connectivity failures even "
            "when hosts share the same IP range. Host B with /28 calculates its network as "
            "10.1.10.176 and believes anything outside .176–.191 requires a router. Host A "
            "with /24 sees the entire .0–.255 range as local. ARP and L2 forwarding fail "
            "because the hosts disagree on whether a router is needed."
        ),
    },
    # ── Q38 — multiple_response ──────────────────────────────────────────────
    {
        "id": "a1d2v3-038",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "An organization is upgrading its wireless infrastructure and comparing WPA2 "
            "and WPA3. Which TWO features are EXCLUSIVE to WPA3 and not available in "
            "WPA2? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "SAE (Simultaneous Authentication of Equals) replacing the PSK four-way handshake",
                "correct": True,
                "rationale": (
                    "Correct. WPA3-Personal replaces WPA2's PSK (Pre-Shared Key) four-way "
                    "handshake with SAE (Dragonfly handshake). SAE prevents offline dictionary "
                    "attacks against captured handshakes and provides forward secrecy."
                ),
            },
            {
                "id": "b",
                "text": "Forward secrecy ensuring past session keys cannot be decrypted if the password is later compromised",
                "correct": True,
                "rationale": (
                    "Correct. WPA3's SAE provides forward secrecy (Perfect Forward Secrecy). "
                    "Each session generates unique keys; compromising the Wi-Fi password later "
                    "does not expose previously captured traffic. WPA2-PSK does not provide "
                    "forward secrecy."
                ),
            },
            {
                "id": "c",
                "text": "AES encryption for data protection",
                "correct": False,
                "rationale": (
                    "Incorrect. AES (specifically AES-CCMP) was introduced in WPA2 and is "
                    "also used in WPA3. It is not exclusive to WPA3."
                ),
            },
            {
                "id": "d",
                "text": "802.1X authentication support for enterprise networks",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X RADIUS-based authentication was supported in WPA2-"
                    "Enterprise. WPA3-Enterprise also uses 802.1X but this feature is not "
                    "exclusive to WPA3."
                ),
            },
        ],
        "explanation": (
            "WPA3 improvements over WPA2: SAE (Simultaneous Authentication of Equals) "
            "replaces PSK, preventing KRACK and offline dictionary attacks; forward secrecy "
            "via ephemeral keys per session; Enhanced Open (OWE) for open networks; "
            "192-bit security mode in WPA3-Enterprise. AES and 802.1X were already in "
            "WPA2 — they are shared features, not WPA3 exclusives."
        ),
    },
    # ── Q39 — multiple_response ──────────────────────────────────────────────
    {
        "id": "a1d2v3-039",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A technician is troubleshooting a newly installed Cat 6 cable run that fails "
            "certification tests. The certifier reports 'Near-End Crosstalk (NEXT) failure' "
            "and 'return loss failure'. Which TWO installation errors MOST likely caused "
            "these failures? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Excessive untwisting of pairs at the termination point (more than 13 mm / 0.5 inch for Cat 6)",
                "correct": True,
                "rationale": (
                    "Correct. Untwisting pairs at terminations beyond the maximum allowed "
                    "distance (13 mm for Cat 6, 6 mm for Cat 6a) disrupts the pair geometry "
                    "that cancels crosstalk. Excessive untwisting is a primary cause of NEXT "
                    "failures."
                ),
            },
            {
                "id": "b",
                "text": "Over-tightening of cable ties that deform the cable jacket and compress the pairs",
                "correct": True,
                "rationale": (
                    "Correct. Over-tightening cable ties compresses and deforms the twisted "
                    "pairs, changing their impedance and geometry. This causes return loss "
                    "failures (impedance discontinuities) and can also degrade NEXT performance."
                ),
            },
            {
                "id": "c",
                "text": "Using T568A wiring on one end and T568B on the other end",
                "correct": False,
                "rationale": (
                    "Incorrect. Using T568A on one end and T568B on the other creates a "
                    "crossover cable, which would cause the cable to fail a straight-through "
                    "wire map test — but not specifically NEXT or return loss failures. "
                    "Wire map failures are a separate test category."
                ),
            },
            {
                "id": "d",
                "text": "Running Cat 6 cable in conduit alongside other network cables",
                "correct": False,
                "rationale": (
                    "Incorrect. Co-routing network cables in conduit can cause alien crosstalk "
                    "(ANEXT) on 10GBase-T, but standard NEXT is an intra-cable measurement "
                    "and is not caused by routing near other Cat 6 cables."
                ),
            },
        ],
        "explanation": (
            "Common Cat 6 installation failures: NEXT — caused by excessive pair untwisting, "
            "split pairs, or poor termination technique; Return loss — caused by impedance "
            "discontinuities from over-bent cable, over-tightened cable ties, or sharp kinks; "
            "Wire map failures — crossed pairs, T568A/B mix, split pairs; Length failures — "
            "cable run exceeds 100 m channel length. TIA-568 specifies max untwist: 13 mm "
            "for Cat 5e/6, 6 mm for Cat 6a."
        ),
    },
    # ── Q40 — multiple_response ──────────────────────────────────────────────
    {
        "id": "a1d2v3-040",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "VLAN/VPN",
        "stem": (
            "A network administrator is implementing network segmentation using VLANs. "
            "Which TWO benefits does VLAN segmentation provide compared to a flat (single "
            "broadcast domain) network? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reduced broadcast domain size, decreasing broadcast traffic overhead on each segment",
                "correct": True,
                "rationale": (
                    "Correct. Each VLAN is its own broadcast domain. Splitting a 500-host flat "
                    "network into five 100-host VLANs reduces broadcast traffic to 1/5 on each "
                    "segment, improving performance and reducing unnecessary interrupts on "
                    "unrelated hosts."
                ),
            },
            {
                "id": "b",
                "text": "Improved security by isolating traffic between groups (e.g., HR, Finance, guest) at Layer 2",
                "correct": True,
                "rationale": (
                    "Correct. VLANs provide Layer 2 isolation: hosts on VLAN 10 (HR) cannot "
                    "communicate with VLAN 20 (Finance) without passing through a router or "
                    "Layer 3 switch with ACLs. This limits lateral movement in case of a "
                    "compromise."
                ),
            },
            {
                "id": "c",
                "text": "Increased total bandwidth because each VLAN gets its own dedicated physical uplink",
                "correct": False,
                "rationale": (
                    "Incorrect. VLANs are a logical segmentation technology. Multiple VLANs "
                    "can share the same physical trunk link — bandwidth is not automatically "
                    "increased by creating VLANs. Link aggregation (LACP) increases bandwidth."
                ),
            },
            {
                "id": "d",
                "text": "Elimination of the need for a router since VLANs enable direct Layer 2 communication between all subnets",
                "correct": False,
                "rationale": (
                    "Incorrect. VLANs create Layer 2 isolation — inter-VLAN communication "
                    "still requires a Layer 3 device (router or Layer 3 switch). VLANs do "
                    "not replace routing; they necessitate it for cross-VLAN traffic."
                ),
            },
        ],
        "explanation": (
            "VLAN benefits: (1) Broadcast containment — each VLAN is an independent broadcast "
            "domain, reducing unnecessary traffic; (2) Security isolation — Layer 2 separation "
            "of different user groups or systems; (3) Logical flexibility — group hosts by "
            "function regardless of physical location; (4) Simplified management — apply "
            "policies per VLAN. VLANs do not increase bandwidth or eliminate routing requirements."
        ),
    },
    # ── Q41 — multiple_response ──────────────────────────────────────────────
    {
        "id": "a1d2v3-041",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Network services",
        "stem": (
            "An organization is deploying a network access control (NAC) solution to "
            "ensure only compliant devices can connect to the corporate network. Which "
            "TWO technologies are commonly used together to implement 802.1X port-based "
            "network access control? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "EAP (Extensible Authentication Protocol) carried over the network to authenticate supplicants",
                "correct": True,
                "rationale": (
                    "Correct. 802.1X uses EAP (Extensible Authentication Protocol) as the "
                    "authentication framework. EAP messages are carried over LAN (EAPOL — "
                    "EAP over LAN) between the supplicant (client) and authenticator (switch/AP), "
                    "and via RADIUS to the authentication server."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS server as the authentication server that validates credentials and returns accept/reject",
                "correct": True,
                "rationale": (
                    "Correct. A RADIUS (Remote Authentication Dial-In User Service) server acts "
                    "as the 802.1X authentication server (AS). The authenticator (switch or AP) "
                    "forwards EAP credentials to RADIUS, which validates them against a directory "
                    "(AD/LDAP) and returns Access-Accept or Access-Reject."
                ),
            },
            {
                "id": "c",
                "text": "MAC address filtering on the switch as the primary authentication method",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC address filtering is a weak access control method (MAC "
                    "addresses can be spoofed) and is not part of 802.1X. 802.1X uses "
                    "credential-based or certificate-based authentication via EAP."
                ),
            },
            {
                "id": "d",
                "text": "WEP encryption to protect credentials during the 802.1X exchange",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP is a broken legacy wireless encryption protocol. 802.1X "
                    "authentication does not use WEP. For wireless, WPA2/WPA3-Enterprise with "
                    "AES is used; for wired, the EAPOL exchange itself uses TLS within EAP "
                    "tunneling methods (PEAP, EAP-TLS)."
                ),
            },
        ],
        "explanation": (
            "802.1X NAC architecture has three roles: Supplicant (client with 802.1X software), "
            "Authenticator (switch or AP that blocks traffic until authenticated), and "
            "Authentication Server (RADIUS). The supplicant sends EAP credentials; the "
            "authenticator forwards them via RADIUS to the server; upon Access-Accept, the "
            "switch port is opened. EAP methods include EAP-TLS (certificates) and PEAP "
            "(password wrapped in TLS)."
        ),
    },
    # ── Q42 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-042",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "A network engineer is designing a high-availability network and wants to "
            "aggregate two 1 Gbps switch uplinks into a single 2 Gbps logical link that "
            "also provides redundancy if one physical link fails. Which technology should "
            "be configured on both switches?"
        ),
        "options": [
            {
                "id": "a",
                "text": "LACP (Link Aggregation Control Protocol — IEEE 802.3ad/802.1AX)",
                "correct": True,
                "rationale": (
                    "Correct. LACP bundles multiple physical links into one logical EtherChannel "
                    "(LAG — Link Aggregation Group), increasing bandwidth and providing "
                    "redundancy. If one physical link fails, traffic continues on the remaining "
                    "links. LACP is the IEEE standard (802.3ad / 802.1AX)."
                ),
            },
            {
                "id": "b",
                "text": "STP (Spanning Tree Protocol) with one link in forwarding and one in blocking state",
                "correct": False,
                "rationale": (
                    "Incorrect. STP would block one of the two links to prevent a loop — "
                    "providing redundancy but not bandwidth aggregation. The blocked link "
                    "carries zero traffic until the active link fails."
                ),
            },
            {
                "id": "c",
                "text": "Dual-homing with static routes on each switch",
                "correct": False,
                "rationale": (
                    "Incorrect. Static routes are a Layer 3 technique for IP routing failover, "
                    "not Layer 2 link aggregation. Static routes do not aggregate bandwidth on "
                    "switch uplinks."
                ),
            },
            {
                "id": "d",
                "text": "Bridge Protocol Data Units (BPDUs) to combine the two links",
                "correct": False,
                "rationale": (
                    "Incorrect. BPDUs are control frames used by STP to elect root bridges "
                    "and detect loops. They do not aggregate link bandwidth."
                ),
            },
        ],
        "explanation": (
            "LACP (802.3ad / 802.1AX) creates a Link Aggregation Group (LAG) or EtherChannel "
            "by combining multiple physical links. Traffic is distributed across links using "
            "a hashing algorithm (src/dst MAC or IP). If one link fails, the remaining links "
            "continue forwarding with no disruption. Both ends must have LACP configured. "
            "Cisco-proprietary PAgP is an alternative but LACP is the IEEE standard."
        ),
    },
    # ── Q43 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-043",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network types (LAN/WAN/PAN)",
        "stem": (
            "A field service technician uses a cellular smartphone as a portable hotspot "
            "to connect a laptop and a tablet simultaneously for on-site work. The network "
            "formed between the technician's devices is best described as which type?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PAN (Personal Area Network)",
                "correct": True,
                "rationale": (
                    "Correct. A PAN (Personal Area Network) is a short-range network centered "
                    "on an individual's personal devices. The hotspot connecting the technician's "
                    "phone, laptop, and tablet is a PAN — all devices belong to one person and "
                    "are within close physical proximity."
                ),
            },
            {
                "id": "b",
                "text": "LAN (Local Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A LAN typically refers to a building- or floor-level network "
                    "with infrastructure (switches, APs). A personal hotspot connecting a "
                    "handful of individual devices is better classified as a PAN."
                ),
            },
            {
                "id": "c",
                "text": "MAN (Metropolitan Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A MAN spans a city or metro area using carrier infrastructure. "
                    "A personal device hotspot confined to arm's reach is not a MAN."
                ),
            },
            {
                "id": "d",
                "text": "SAN (Storage Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A SAN is a specialized network for block-level storage access "
                    "using Fibre Channel or iSCSI. It has no relevance to a personal device "
                    "hotspot."
                ),
            },
        ],
        "explanation": (
            "A PAN (Personal Area Network) encompasses devices used by a single person within "
            "a very short range (< 10 m typically). Examples: Bluetooth earbuds + phone, "
            "Wi-Fi hotspot connecting personal devices, USB tethering. PANs may use Bluetooth, "
            "Wi-Fi Direct, USB, NFC, or cellular hotspot technologies. The key differentiator "
            "is personal-scale use by one individual."
        ),
    },
    # ── Q44 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-044",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "T568A/B wiring",
        "stem": (
            "A technician is making a straight-through patch cable using T568A on both ends "
            "to connect a workstation to a wall jack that is punched down to T568B. "
            "Will connectivity be established, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "No — the T568A-to-T568A cable combined with T568B at the wall jack creates a crossover configuration, likely preventing auto-MDI/MDIX from negotiating correctly on non-MDI/MDIX ports",
                "correct": False,
                "rationale": (
                    "Incorrect. While the channel crossover is real, modern auto-MDI/MDIX "
                    "equipment (mandatory for 1000BASE-T) automatically corrects the crossover "
                    "and establishes connectivity. This answer overstates the failure risk for "
                    "modern hardware, making it the wrong choice."
                ),
            },
            {
                "id": "b",
                "text": "Yes on modern auto-MDI/MDIX equipment, but the overall channel is effectively a crossover; older equipment without auto-MDI/MDIX would fail",
                "correct": True,
                "rationale": (
                    "Correct. The patch cable (T568A–T568A) combined with the T568B wall jack "
                    "creates a crossover on the permanent link. Modern 1000BASE-T and faster "
                    "equipment mandates auto-MDI/MDIX, which detects and corrects the crossover "
                    "automatically. Legacy 10/100 equipment without auto-MDI/MDIX would fail."
                ),
            },
            {
                "id": "c",
                "text": "Yes — T568A and T568B are electrically identical so mixing them has no effect",
                "correct": False,
                "rationale": (
                    "Incorrect. T568A and T568B differ in which pairs occupy pins 1/2 and 3/6. "
                    "Mixing them in a channel creates a crossover, which is not the same as "
                    "using a consistent standard throughout. They are not electrically identical "
                    "in terms of pin pairing."
                ),
            },
            {
                "id": "d",
                "text": "No — T568A cables cannot connect to T568B jacks under any circumstances",
                "correct": False,
                "rationale": (
                    "Incorrect. The physical RJ-45 connector is identical regardless of "
                    "T568A or T568B wiring. The standards only differ in which colored wire "
                    "occupies each pin. Mixing them creates a crossover that auto-MDI/MDIX "
                    "resolves on modern hardware."
                ),
            },
        ],
        "explanation": (
            "Consistency matters: a T568A patch cable + T568B wall jack creates a crossover "
            "channel (T568A pin 1→T568B pin 3, etc.). IEEE 802.3-2008 mandated auto-MDI/MDIX "
            "for 1000BASE-T and above, so modern Gigabit/10G devices automatically negotiate "
            "regardless of crossover. However, mixing standards during installation is poor "
            "practice and fails certification. Best practice: use T568B consistently "
            "throughout North American enterprise installations."
        ),
    },
    # ── Q45 ──────────────────────────────────────────────────────────────────
    {
        "id": "a1d2v3-045",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network services",
        "stem": (
            "A network engineer is configuring QoS on a switch to prioritize VoIP traffic. "
            "The voice VLAN is VLAN 40. The engineer wants to mark all voice RTP packets "
            "at Layer 3 so that all downstream devices honor the priority. Which field in "
            "the IP header should be set, and what DSCP value is used for voice bearer traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DSCP field in the IP header; set to EF (Expedited Forwarding, DSCP 46 / binary 101110)",
                "correct": True,
                "rationale": (
                    "Correct. QoS for voice RTP uses DSCP EF (Expedited Forwarding), value 46 "
                    "(decimal) / 101110 (binary), in the IP header's DSCP field (formerly Type "
                    "of Service). EF provides the lowest latency and jitter treatment, "
                    "making it the standard DSCP value for voice bearer (RTP) traffic per "
                    "RFC 3246 and Cisco/industry best practices."
                ),
            },
            {
                "id": "b",
                "text": "802.1p CoS field in the Ethernet header; set to value 7 (highest priority)",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1p CoS (Class of Service) is a Layer 2 QoS mechanism in "
                    "the 802.1Q VLAN tag (3 bits, 0–7). While CoS 5 is typically used for "
                    "voice, the question asks for Layer 3 marking. Also, CoS 7 is reserved for "
                    "network control traffic, not voice."
                ),
            },
            {
                "id": "c",
                "text": "TTL field in the IP header; set to 255 to prioritize voice packets",
                "correct": False,
                "rationale": (
                    "Incorrect. The TTL (Time To Live) field counts hop limits and is "
                    "decremented by each router. It is not a QoS marking field and does "
                    "not affect packet priority treatment."
                ),
            },
            {
                "id": "d",
                "text": "DSCP field in the IP header; set to AF41 (Assured Forwarding, DSCP 34)",
                "correct": False,
                "rationale": (
                    "Incorrect. AF41 (DSCP 34) is used for video conferencing or high-priority "
                    "data. EF (DSCP 46) is the correct marking for voice bearer (RTP) traffic "
                    "requiring minimum latency and jitter guarantees."
                ),
            },
        ],
        "explanation": (
            "DSCP QoS markings for unified communications: EF (DSCP 46) = voice bearer/RTP; "
            "CS3 (DSCP 24) = call signaling (SIP/H.323); AF41 (DSCP 34) = video conferencing; "
            "CS7 (DSCP 56) = network control (routing protocols). EF (Expedited Forwarding, "
            "RFC 3246) provides a 'low-latency, low-jitter, low-loss' service class essential "
            "for real-time voice quality. DSCP markings are in the 6 MSBs of the IP header's "
            "ToS/DSCP byte."
        ),
    },
]
