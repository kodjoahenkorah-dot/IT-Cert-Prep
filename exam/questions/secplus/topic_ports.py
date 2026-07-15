"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations): Ports & Protocols."""

QUESTIONS = [
    {
        "id": "tprt-001",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A network scan of a branch router's management interface shows TCP port 23 open and reachable from "
            "the internal LAN. Administrators use it daily to configure the device. Which secure replacement "
            "protocol and port should the analyst recommend?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSH on TCP 22",
                "correct": True,
                "rationale": (
                    "Correct. Port 23 is Telnet, which transmits all traffic, including login credentials, in "
                    "cleartext. SSH on TCP 22 provides an encrypted, authenticated replacement for interactive "
                    "device management."
                ),
            },
            {
                "id": "b",
                "text": "SFTP on TCP 22",
                "correct": False,
                "rationale": (
                    "Incorrect. SFTP also runs over the SSH transport on port 22, but it is a file-transfer "
                    "subsystem, not an interactive terminal/CLI replacement for Telnet-based device management."
                ),
            },
            {
                "id": "c",
                "text": "TLS-wrapped Telnet on TCP 992",
                "correct": False,
                "rationale": (
                    "Incorrect. While a TLS-wrapped Telnet variant using port 992 technically exists, it is not a "
                    "standard, widely supported enterprise practice; SSH on port 22 is the recognized secure "
                    "replacement tested on the exam."
                ),
            },
            {
                "id": "d",
                "text": "RDP on TCP 3389",
                "correct": False,
                "rationale": (
                    "Incorrect. RDP is a graphical remote desktop protocol for Windows hosts, not a CLI "
                    "replacement for Telnet on network devices, and using it here would not match the router's "
                    "management interface."
                ),
            },
        ],
        "explanation": (
            "Telnet (TCP 23) sends credentials and session data in cleartext. SSH (TCP 22) is the standard "
            "encrypted replacement for interactive command-line administration of network devices."
        ),
    },
    {
        "id": "tprt-002",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A packet capture on a file transfer job shows credentials and file contents traversing TCP ports 20 "
            "and 21 in cleartext between a vendor and an internal server. Which change eliminates the cleartext "
            "exposure while reusing the organization's existing SSH infrastructure and key-based authentication?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Migrate the transfer to SFTP over TCP 22",
                "correct": True,
                "rationale": (
                    "Correct. SFTP is a subsystem of SSH that runs entirely over TCP 22, encrypting both "
                    "authentication and file data, and it can reuse existing SSH key infrastructure — matching "
                    "both requirements in the scenario."
                ),
            },
            {
                "id": "b",
                "text": "Migrate the transfer to FTPS on TCP 989/990",
                "correct": False,
                "rationale": (
                    "Incorrect. FTPS does encrypt the session using TLS, but it relies on X.509 certificates over "
                    "a separate implicit FTPS port pair (989/990), not the organization's existing SSH key "
                    "infrastructure as required."
                ),
            },
            {
                "id": "c",
                "text": "Keep FTP but restrict it to TCP 21 only and block TCP 20",
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking the data channel (20) while leaving the control channel (21) open does "
                    "not add encryption; both channels still transmit credentials and data in cleartext."
                ),
            },
            {
                "id": "d",
                "text": "Move the FTP service to a non-standard high port above 1024",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the port number is security through obscurity; the protocol remains "
                    "unencrypted FTP and credentials/data are still exposed in cleartext."
                ),
            },
        ],
        "explanation": (
            "SFTP (Secure FTP) is a file-transfer subsystem of the SSH protocol running on TCP 22. It provides "
            "encryption and can leverage existing SSH key-based authentication, unlike FTPS which uses TLS "
            "certificates over separate ports 989/990."
        ),
    },
    {
        "id": "tprt-003",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A firewall log shows a workstation on the internal network establishing a session to a jump server "
            "on TCP 3389. Which statement about this traffic is MOST accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is RDP traffic, and encryption depends on configuration — Network Level Authentication and TLS should be enforced rather than assumed by default.",
                "correct": True,
                "rationale": (
                    "Correct. TCP 3389 is the well-known RDP port. RDP supports encryption, but legacy or "
                    "misconfigured deployments can use weak or no encryption; best practice enforces NLA and TLS "
                    "rather than assuming security by default."
                ),
            },
            {
                "id": "b",
                "text": "It is SSH traffic and is always encrypted end-to-end by default.",
                "correct": False,
                "rationale": (
                    "Incorrect. SSH uses TCP 22, not 3389. This option misidentifies both the protocol and the "
                    "port."
                ),
            },
            {
                "id": "c",
                "text": "It is SMB traffic used for file share access between the two hosts.",
                "correct": False,
                "rationale": (
                    "Incorrect. SMB uses TCP 445, not 3389. This option misidentifies the protocol/port pairing "
                    "entirely."
                ),
            },
            {
                "id": "d",
                "text": "It is LDAPS traffic used to query directory services over TLS.",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAPS uses TCP 636, not 3389, and is unrelated to a jump-server remote desktop "
                    "session."
                ),
            },
        ],
        "explanation": (
            "TCP 3389 is RDP. Unlike SSH, which is encrypted by design, RDP's security posture depends on "
            "configuration (NLA, TLS/CredSSP); administrators must explicitly enforce encryption rather than "
            "assume it is always active."
        ),
    },
    {
        "id": "tprt-004",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A network management review finds that switches are polled using SNMP with the community string "
            "'public' sent in cleartext on UDP 161, and traps are received on UDP 162. Which remediation BEST "
            "addresses the security weakness while preserving the same UDP ports?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Upgrade from SNMPv1/v2c to SNMPv3, which adds authentication and encryption while continuing to use UDP 161/162",
                "correct": True,
                "rationale": (
                    "Correct. SNMPv3 introduces user-based authentication and message encryption (privacy) that "
                    "SNMPv1/v2c lack, while still operating on the same standard UDP 161 (queries) and 162 "
                    "(traps) ports — directly fixing the cleartext community-string weakness."
                ),
            },
            {
                "id": "b",
                "text": "Switch community strings from 'public' to 'private' to add security",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the community string value does not add encryption or strong "
                    "authentication; SNMPv1/v2c community strings are still transmitted in cleartext regardless "
                    "of the chosen string."
                ),
            },
            {
                "id": "c",
                "text": "Move SNMP traffic to TCP 161/162 instead of UDP",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP standardly operates over UDP; changing transport protocol does not address "
                    "the lack of authentication and encryption inherent in SNMPv1/v2c."
                ),
            },
            {
                "id": "d",
                "text": "Disable trap forwarding on UDP 162 while leaving polling on UDP 161 unchanged",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling traps removes event notifications but does nothing to encrypt or "
                    "authenticate the polling traffic on port 161, leaving the core weakness unresolved."
                ),
            },
        ],
        "explanation": (
            "SNMPv1 and SNMPv2c use cleartext community strings for authorization with no encryption. SNMPv3 "
            "adds per-user authentication and optional encryption (privacy) while keeping the same well-known "
            "UDP 161/162 ports, making it the direct secure upgrade path."
        ),
    },
    {
        "id": "tprt-005",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "An internal application authenticates users against Active Directory by binding to the directory "
            "service on TCP 389 with a plaintext username and password. A penetration test captured these "
            "credentials via ARP spoofing. Which change should the developer make?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reconfigure the application to bind over LDAPS on TCP 636",
                "correct": True,
                "rationale": (
                    "Correct. LDAPS wraps the LDAP session in TLS on TCP 636, encrypting the bind credentials and "
                    "all subsequent directory traffic, which directly prevents the credential capture seen with "
                    "plaintext port 389 binds."
                ),
            },
            {
                "id": "b",
                "text": "Continue binding on TCP 389 but shorten the password expiration interval",
                "correct": False,
                "rationale": (
                    "Incorrect. Shortening password expiration does not encrypt the bind traffic; credentials "
                    "would still be captured in cleartext until they expire, and the underlying exposure remains."
                ),
            },
            {
                "id": "c",
                "text": "Switch the application to query the directory over TCP 88 instead",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 88 is Kerberos, a different authentication protocol with a different query "
                    "model; simply changing the destination port does not make an LDAP bind operation encrypted."
                ),
            },
            {
                "id": "d",
                "text": "Move the LDAP bind traffic to UDP 389 instead of TCP 389",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP binds use TCP, and changing transport protocol does nothing to encrypt the "
                    "credentials; the packets would still be readable in cleartext."
                ),
            },
        ],
        "explanation": (
            "Standard LDAP on TCP 389 is unencrypted. LDAPS (TCP 636) wraps the entire LDAP session in TLS, "
            "protecting bind credentials and query data from interception — the correct fix for cleartext "
            "directory authentication."
        ),
    },
    {
        "id": "tprt-006",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A mail administrator finds that TCP port 25 on the perimeter firewall accepts inbound connections "
            "from any external host and is being used by internal users to submit outgoing mail directly from "
            "their laptops, bypassing authentication. Which change enforces authenticated mail submission from "
            "end-user clients?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Require end-user mail clients to submit outgoing mail on TCP 587 with authentication and STARTTLS, reserving TCP 25 for server-to-server relay only",
                "correct": True,
                "rationale": (
                    "Correct. TCP 587 is the standard message submission port, designed specifically to require "
                    "client authentication and STARTTLS encryption. TCP 25 should be restricted to authenticated "
                    "MTA-to-MTA relay, not open client submission."
                ),
            },
            {
                "id": "b",
                "text": "Require end-user mail clients to submit outgoing mail on TCP 143 with authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 143 is IMAP, used for retrieving/reading mail, not for submitting outgoing "
                    "messages; it does not address the outbound submission problem."
                ),
            },
            {
                "id": "c",
                "text": "Block TCP 25 entirely at the perimeter with no alternative submission port",
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking port 25 entirely would also stop legitimate server-to-server mail relay; "
                    "it does not provide end users an authenticated way to submit outgoing mail."
                ),
            },
            {
                "id": "d",
                "text": "Require end-user mail clients to submit outgoing mail on TCP 110 with authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 110 is POP3, used for retrieving mail from a mailbox, not for submitting "
                    "outbound messages."
                ),
            },
        ],
        "explanation": (
            "TCP 25 is intended for server-to-server SMTP relay and is frequently abused for open relay or "
            "unauthenticated submission. TCP 587 (message submission) is the standard port requiring client "
            "authentication and STARTTLS for end-user outgoing mail."
        ),
    },
    {
        "id": "tprt-007",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A SOC analyst reviewing firewall logs sees a workstation sending a large volume of UDP port 53 "
            "queries to an external resolver every few seconds, and management asks whether this traffic can be "
            "encrypted end-to-end so intermediate networks cannot see which domains are being resolved. Which "
            "port should the client be reconfigured to use for DNS over TLS?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 853",
                "correct": True,
                "rationale": (
                    "Correct. DNS over TLS (DoT) uses a dedicated TCP port, 853, to encrypt DNS queries and "
                    "responses end-to-end between client and resolver, preventing on-path observation of the "
                    "plaintext queries seen on UDP 53."
                ),
            },
            {
                "id": "b",
                "text": "UDP 53 with a longer TTL configured on the resolver",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting cache TTL values has no effect on confidentiality; queries on UDP 53 "
                    "remain unencrypted regardless of TTL settings."
                ),
            },
            {
                "id": "c",
                "text": "TCP 989",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 989 is associated with the FTPS data channel, not DNS over TLS."
                ),
            },
            {
                "id": "d",
                "text": "TCP 636",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 636 is LDAPS, used to encrypt directory service traffic, not DNS queries."
                ),
            },
        ],
        "explanation": (
            "DNS over TLS (DoT) encrypts DNS traffic on a dedicated TCP port, 853, distinct from the cleartext "
            "UDP/TCP 53 used by traditional DNS. DNS over HTTPS (DoH) is the other common encrypted option, "
            "typically tunneled over standard HTTPS on TCP 443."
        ),
    },
    {
        "id": "tprt-008",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A security architect is choosing between SFTP and FTPS to replace legacy FTP for a partner file "
            "exchange. Select the TWO statements that correctly describe the technical differences between "
            "these two protocols."
        ),
        "options": [
            {
                "id": "a",
                "text": "SFTP runs entirely over a single SSH connection on TCP 22, encrypting both the control and data channels together.",
                "correct": True,
                "rationale": (
                    "Correct. SFTP is an SSH subsystem, so a single TCP 22 connection handles authentication, "
                    "command, and data transfer, all protected by the SSH transport's encryption."
                ),
            },
            {
                "id": "b",
                "text": "FTPS uses TLS/SSL and, in its implicit mode, typically listens on TCP 990 for control and TCP 989 for data, separate from plain FTP's ports.",
                "correct": True,
                "rationale": (
                    "Correct. Implicit FTPS establishes a TLS session immediately on TCP 990 for the control "
                    "channel and TCP 989 for the data channel, distinct from unencrypted FTP's ports 21/20."
                ),
            },
            {
                "id": "c",
                "text": "SFTP requires an X.509 certificate issued by a public certificate authority for every server, identical to FTPS.",
                "correct": False,
                "rationale": (
                    "Incorrect. SFTP relies on SSH key pairs or password authentication over the SSH protocol; it "
                    "does not require X.509 PKI certificates the way TLS-based FTPS does."
                ),
            },
            {
                "id": "d",
                "text": "FTPS and SFTP both use the exact same TCP port numbers, making them interchangeable at the firewall.",
                "correct": False,
                "rationale": (
                    "Incorrect. SFTP uses TCP 22 while FTPS uses 989/990 (implicit) or 21 with STARTTLS "
                    "(explicit); the port numbers differ and firewall rules must be configured separately for "
                    "each."
                ),
            },
        ],
        "explanation": (
            "SFTP is an SSH subsystem on TCP 22 using SSH key-based or password authentication. FTPS is FTP "
            "secured with TLS, using certificate-based authentication and separate implicit ports 989/990 (or "
            "explicit TLS negotiated on port 21). They are not interchangeable at the firewall or in trust model."
        ),
    },
    {
        "id": "tprt-009",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A vulnerability scan reports that an email server accepts mailbox retrieval connections on TCP 110 "
            "without requiring TLS, exposing usernames and passwords to interception. Which port should the "
            "server be reconfigured to use for encrypted mailbox retrieval?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 995 (POP3S)",
                "correct": True,
                "rationale": (
                    "Correct. TCP 995 is POP3 over implicit TLS (POP3S), encrypting the authentication and "
                    "message retrieval session that is exposed in cleartext on TCP 110."
                ),
            },
            {
                "id": "b",
                "text": "TCP 993 (IMAPS)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 993 secures IMAP, a different mailbox access protocol with different "
                    "semantics (server-side folder management); it is not the encrypted counterpart to POP3 on "
                    "110."
                ),
            },
            {
                "id": "c",
                "text": "TCP 465 (SMTPS)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 465 secures SMTP for message submission/relay, not mailbox retrieval; it "
                    "does not replace POP3 functionality."
                ),
            },
            {
                "id": "d",
                "text": "TCP 587 (message submission)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 587 is used by clients to submit outgoing mail with authentication and "
                    "STARTTLS; it has no role in retrieving mail from a mailbox."
                ),
            },
        ],
        "explanation": (
            "POP3 (TCP 110) is cleartext by default. POP3S (TCP 995) wraps the session in implicit TLS, "
            "encrypting credentials and mail content — the direct secure replacement for the vulnerability found."
        ),
    },
    {
        "id": "tprt-010",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A help desk technician configures a new mail client to synchronize mail across multiple devices "
            "while keeping messages organized in server-side folders, and management requires the connection be "
            "encrypted. Which port should the technician configure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 993",
                "correct": True,
                "rationale": (
                    "Correct. TCP 993 is IMAPS — IMAP over implicit TLS. IMAP natively supports server-side "
                    "folder synchronization across multiple devices, and port 993 satisfies the encryption "
                    "requirement."
                ),
            },
            {
                "id": "b",
                "text": "TCP 995",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 995 is POP3S. POP3 typically downloads mail to a single client and does not "
                    "natively maintain synchronized server-side folder structures across multiple devices the "
                    "way IMAP does."
                ),
            },
            {
                "id": "c",
                "text": "TCP 143",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 143 is standard IMAP without encryption; it satisfies the multi-device "
                    "folder-sync requirement but not the encryption requirement management specified."
                ),
            },
            {
                "id": "d",
                "text": "TCP 110",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 110 is standard POP3, which is both unencrypted and not designed for "
                    "maintaining synchronized server-side folders across devices."
                ),
            },
        ],
        "explanation": (
            "IMAP (TCP 143) is designed for multi-device, server-side mailbox synchronization, unlike POP3. "
            "IMAPS (TCP 993) adds implicit TLS encryption, satisfying both the functional and security "
            "requirements described."
        ),
    },
    {
        "id": "tprt-011",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A firewall administrator is writing an outbound rule so that internal mail clients can submit "
            "authenticated outgoing messages through the corporate mail relay using STARTTLS negotiation rather "
            "than implicit TLS. Which single port should the rule permit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 587",
                "correct": True,
                "rationale": (
                    "Correct. TCP 587 is the standard message submission port defined for client mail "
                    "submission; it begins in plaintext and upgrades to encryption via STARTTLS, matching the "
                    "requirement exactly."
                ),
            },
            {
                "id": "b",
                "text": "TCP 465",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 465 is used for SMTPS with implicit TLS — the session is encrypted from the "
                    "first packet rather than upgraded mid-session via STARTTLS, which does not match the "
                    "administrator's requirement."
                ),
            },
            {
                "id": "c",
                "text": "TCP 25",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 25 is intended for server-to-server relay traffic, not authenticated client "
                    "submission, and best practice reserves it away from end-user mail clients."
                ),
            },
            {
                "id": "d",
                "text": "TCP 990",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 990 is the implicit FTPS control port, unrelated to SMTP mail submission."
                ),
            },
        ],
        "explanation": (
            "TCP 587 (message submission) is specifically designed for authenticated client mail submission "
            "using STARTTLS to upgrade an initially plaintext connection to TLS, distinguishing it from port 465 "
            "(implicit TLS from the start) and port 25 (server-to-server relay)."
        ),
    },
    {
        "id": "tprt-012",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "Workstations in a segmented VLAN cannot authenticate to an Active Directory domain controller after "
            "a new internal firewall rule set was deployed, and users see ticket-related authentication failures "
            "specifically. Which port was MOST likely blocked?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP/UDP 88 (Kerberos)",
                "correct": True,
                "rationale": (
                    "Correct. Kerberos, the ticket-based authentication protocol used by Active Directory, "
                    "operates on port 88. Blocking it directly causes ticket-granting failures during domain "
                    "authentication."
                ),
            },
            {
                "id": "b",
                "text": "TCP 636 (LDAPS)",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAPS handles encrypted directory queries, not ticket-granting authentication; "
                    "blocking it would affect directory lookups, not specifically Kerberos ticket errors."
                ),
            },
            {
                "id": "c",
                "text": "UDP 123 (NTP)",
                "correct": False,
                "rationale": (
                    "Incorrect. While Kerberos is time-sensitive and severe clock drift caused by blocked NTP can "
                    "indirectly cause ticket validation failures, the scenario describes a direct authentication "
                    "port block, which points to Kerberos itself (88) as the most likely cause."
                ),
            },
            {
                "id": "d",
                "text": "TCP 445 (SMB)",
                "correct": False,
                "rationale": (
                    "Incorrect. SMB handles file and printer sharing traffic; blocking it would impact file "
                    "share access, not the ticket-granting authentication process described."
                ),
            },
        ],
        "explanation": (
            "Kerberos (TCP/UDP 88) is the authentication protocol Active Directory uses to issue and validate "
            "tickets. Blocking this port directly produces ticket-related authentication failures, distinct from "
            "LDAP/LDAPS (directory queries) or SMB (file sharing)."
        ),
    },
    {
        "id": "tprt-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "An external threat actor sends a spoofed UDP packet to a publicly reachable time server on port 123 "
            "with a forged source address, causing an amplified flood of traffic toward the victim. Which "
            "protocol and port pairing is being abused in this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "NTP on UDP 123",
                "correct": True,
                "rationale": (
                    "Correct. NTP operates on UDP 123 and has historically been abused for amplification "
                    "attacks, where a small spoofed query (such as the 'monlist' command on older servers) "
                    "generates a much larger response directed at the spoofed victim address."
                ),
            },
            {
                "id": "b",
                "text": "DNS on UDP 53",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS amplification is a real and similar attack pattern, but it uses UDP 53, not "
                    "123; the scenario specifically identifies port 123, which is NTP."
                ),
            },
            {
                "id": "c",
                "text": "SNMP on UDP 161",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP amplification abuses UDP 161, not 123; while it is also a known "
                    "amplification vector, it does not match the port stated in the scenario."
                ),
            },
            {
                "id": "d",
                "text": "Syslog on UDP 514",
                "correct": False,
                "rationale": (
                    "Incorrect. Syslog on UDP 514 is used for log message forwarding and is not a recognized "
                    "amplification-attack vector, nor does it match the port described."
                ),
            },
        ],
        "explanation": (
            "UDP 123 is NTP. Because NTP is connectionless and certain legacy commands return responses far "
            "larger than the request, attackers spoof the victim's source IP to trigger reflected, amplified "
            "floods — a well-known abuse of this port."
        ),
    },
    {
        "id": "tprt-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "Following a ransomware outbreak that propagated using a Windows file-sharing protocol vulnerability, "
            "the security team wants to block that protocol from crossing the network perimeter while still "
            "allowing it within trusted internal segments. Which port should be blocked at the internet-facing "
            "firewall?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 445",
                "correct": True,
                "rationale": (
                    "Correct. TCP 445 is used by SMB, the Windows file-sharing protocol exploited by several "
                    "major worms (e.g., WannaCry). Best practice blocks SMB at the internet perimeter while "
                    "permitting it on trusted internal segments only."
                ),
            },
            {
                "id": "b",
                "text": "TCP 3389",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 3389 is RDP, a different remote-access protocol; while it should also be "
                    "restricted at the perimeter, it is not the file-sharing protocol described in this "
                    "scenario."
                ),
            },
            {
                "id": "c",
                "text": "TCP 143",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 143 is IMAP, an email retrieval protocol unrelated to Windows file sharing or "
                    "the described propagation vector."
                ),
            },
            {
                "id": "d",
                "text": "UDP 161",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 161 is SNMP, used for network device management, not file sharing, and is "
                    "unrelated to this ransomware propagation method."
                ),
            },
        ],
        "explanation": (
            "TCP 445 carries SMB traffic, the Windows file/print-sharing protocol whose vulnerabilities (e.g., "
            "EternalBlue) have been exploited by self-propagating ransomware. Perimeter firewalls should block "
            "inbound/outbound 445 while allowing it only within trusted internal network segments."
        ),
    },
    {
        "id": "tprt-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A packet capture on the directory services subnet shows a TLS handshake (ClientHello/ServerHello) "
            "immediately followed by encrypted application data on TCP 636, with no plaintext bind request "
            "visible beforehand. Which conclusion is MOST accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This is LDAPS, which establishes TLS immediately upon connection before any LDAP operations occur, so no plaintext bind is ever exposed.",
                "correct": True,
                "rationale": (
                    "Correct. LDAPS on TCP 636 is an implicit-TLS protocol: the TLS handshake completes first, "
                    "and all subsequent LDAP operations, including the bind (authentication) request, occur "
                    "inside the encrypted tunnel — consistent with the capture."
                ),
            },
            {
                "id": "b",
                "text": "This is standard LDAP that has been misconfigured to use port 636 instead of 389.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard cleartext LDAP does not perform a TLS handshake at connection start; "
                    "the observed TLS negotiation is characteristic of LDAPS, not a misconfigured cleartext "
                    "service."
                ),
            },
            {
                "id": "c",
                "text": "This is LDAP using StartTLS, which always operates on port 636.",
                "correct": False,
                "rationale": (
                    "Incorrect. StartTLS begins as a plaintext connection on the standard LDAP port (389) and "
                    "then upgrades to TLS mid-session; a TLS handshake occurring immediately with no prior "
                    "plaintext traffic indicates implicit LDAPS on 636, not StartTLS."
                ),
            },
            {
                "id": "d",
                "text": "This is Kerberos pre-authentication traffic encapsulated inside LDAP.",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos operates as its own protocol on port 88 and is not encapsulated inside "
                    "LDAP traffic on port 636; this mischaracterizes the protocol layering."
                ),
            },
        ],
        "explanation": (
            "TCP 636 is the implicit-TLS LDAPS port: the TLS session is established before any LDAP operation, "
            "including the bind, so no plaintext credentials are ever visible on the wire — unlike StartTLS, "
            "which negotiates encryption after an initial plaintext connection on port 389."
        ),
    },
    {
        "id": "tprt-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A firewall rule set permits inbound connections to a file transfer server on TCP 989 and TCP 990 "
            "only, with all other file-transfer ports blocked. Which protocol is this configuration designed to "
            "support?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FTPS operating in implicit TLS mode",
                "correct": True,
                "rationale": (
                    "Correct. Implicit FTPS conventionally uses TCP 990 for the control channel and TCP 989 for "
                    "the data channel, with TLS negotiated immediately upon connection — matching exactly the "
                    "ports permitted."
                ),
            },
            {
                "id": "b",
                "text": "SFTP operating over the SSH transport",
                "correct": False,
                "rationale": (
                    "Incorrect. SFTP uses a single TCP 22 connection for both control and data; it does not use "
                    "the 989/990 port pair at all."
                ),
            },
            {
                "id": "c",
                "text": "Plain FTP using active mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Plain FTP uses TCP 21 for control and TCP 20 for active-mode data transfer, not "
                    "989/990, and provides no encryption."
                ),
            },
            {
                "id": "d",
                "text": "TFTP using a randomized ephemeral port range",
                "correct": False,
                "rationale": (
                    "Incorrect. TFTP is a UDP-based protocol that typically starts on UDP 69 and uses ephemeral "
                    "ports for transfer, not the fixed TCP 989/990 pairing described."
                ),
            },
        ],
        "explanation": (
            "TCP 990 (control) and TCP 989 (data) are the conventional ports for implicit-mode FTPS, where TLS "
            "is established immediately, distinguishing it from SFTP (port 22), plain FTP (21/20), and TFTP "
            "(UDP 69)."
        ),
    },
    {
        "id": "tprt-017",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A compliance auditor notes that all network devices forward log messages to the SIEM over UDP 514 "
            "in plaintext, with no delivery guarantee and no encryption. Which change addresses both the "
            "confidentiality and reliability concerns?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reconfigure devices to send syslog over TCP using TLS on port 6514",
                "correct": True,
                "rationale": (
                    "Correct. Syslog over TLS (RFC 5425) uses TCP on port 6514, which provides both a reliable, "
                    "connection-oriented transport and encryption for log data in transit — resolving both "
                    "concerns raised by the auditor."
                ),
            },
            {
                "id": "b",
                "text": "Increase the UDP buffer size on the SIEM collector to reduce dropped log packets",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting buffer size may reduce packet loss somewhat but does nothing to "
                    "encrypt the log traffic, leaving the confidentiality concern unaddressed."
                ),
            },
            {
                "id": "c",
                "text": "Move syslog traffic to UDP port 161 to align with existing network management traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 161 is used by SNMP; repurposing it for syslog would cause conflicts and "
                    "still leaves the traffic both unencrypted and unreliable (UDP-based)."
                ),
            },
            {
                "id": "d",
                "text": "Compress the syslog payloads before sending them over UDP 514",
                "correct": False,
                "rationale": (
                    "Incorrect. Compression reduces bandwidth but provides no encryption or delivery guarantee; "
                    "the underlying transport remains unreliable and readable to anyone intercepting the traffic."
                ),
            },
        ],
        "explanation": (
            "Traditional syslog over UDP 514 is unencrypted and unreliable (no delivery confirmation). Syslog "
            "over TLS on TCP 6514 provides both encryption and TCP's reliable, connection-oriented delivery, "
            "directly resolving both concerns."
        ),
    },
    {
        "id": "tprt-018",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A network engineer is comparing DNS over HTTPS (DoH) and DNS over TLS (DoT) for encrypting client "
            "DNS resolution. Select the TWO statements that are technically accurate."
        ),
        "options": [
            {
                "id": "a",
                "text": "DoT uses a dedicated TCP port, 853, making it easy for network administrators to identify and separately allow or block encrypted DNS traffic.",
                "correct": True,
                "rationale": (
                    "Correct. DoT was designed with its own port, 853, specifically so DNS traffic could be "
                    "distinguished from other traffic at the network layer for filtering or monitoring purposes."
                ),
            },
            {
                "id": "b",
                "text": "DoH typically tunnels DNS queries inside standard HTTPS traffic on TCP 443, which can make it difficult to distinguish from other web traffic for network-level filtering.",
                "correct": True,
                "rationale": (
                    "Correct. DoH blends DNS queries into the same TCP 443 stream used by ordinary web browsing, "
                    "which is convenient for bypassing DNS-based filtering but complicates network visibility and "
                    "policy enforcement."
                ),
            },
            {
                "id": "c",
                "text": "Both DoH and DoT operate over UDP 53, identical to traditional unencrypted DNS.",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither protocol uses UDP 53. DoT uses TCP 853, and DoH uses TCP 443, both "
                    "distinct from the unencrypted UDP/TCP 53 traditional DNS port."
                ),
            },
            {
                "id": "d",
                "text": "DoT is indistinguishable from general web browsing traffic because it shares the same port as HTTPS.",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes DoH, not DoT. DoT's dedicated port 853 is precisely what makes it "
                    "distinguishable from web traffic, unlike DoH, which shares port 443 with HTTPS."
                ),
            },
        ],
        "explanation": (
            "DoT (TCP 853) uses a dedicated port that network defenders can filter or monitor distinctly. DoH "
            "(TCP 443) blends into normal HTTPS traffic, improving privacy from network-level observation but "
            "reducing an organization's ability to enforce DNS-based security policy."
        ),
    },
    {
        "id": "tprt-019",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A web application currently accepts connections on TCP 80 only, and a recent audit flags that "
            "session cookies and login form data are transmitted without encryption. Which minimal change "
            "resolves the finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy a valid TLS certificate and require all traffic to use HTTPS on TCP 443, redirecting or disabling TCP 80",
                "correct": True,
                "rationale": (
                    "Correct. HTTPS on TCP 443 encrypts the entire HTTP session, including login forms and "
                    "session cookies, using TLS. Redirecting or disabling plaintext TCP 80 ensures no fallback to "
                    "an unencrypted channel remains."
                ),
            },
            {
                "id": "b",
                "text": "Hash the session cookie value before sending it over TCP 80",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing a cookie value client-side does not create a secure, reversible session "
                    "mechanism and does nothing to encrypt the transport channel itself; the login form data "
                    "would still be exposed."
                ),
            },
            {
                "id": "c",
                "text": "Move the web application to TCP 8080 to reduce automated scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing to a different plaintext port is security through obscurity and does not "
                    "add encryption; traffic remains readable to anyone capturing packets."
                ),
            },
            {
                "id": "d",
                "text": "Enable HTTP compression to reduce the size of transmitted session data",
                "correct": False,
                "rationale": (
                    "Incorrect. Compression reduces bandwidth usage but provides no confidentiality protection; "
                    "compressed cleartext is still cleartext."
                ),
            },
        ],
        "explanation": (
            "HTTPS (TCP 443) uses TLS to encrypt the full HTTP session, protecting credentials, form data, and "
            "session cookies from interception — the standard remediation for a plaintext HTTP (TCP 80) finding."
        ),
    },
    {
        "id": "tprt-020",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A mail server administrator must choose between configuring outbound mail submission with TLS "
            "negotiated immediately upon connection versus TLS negotiated after an initial plaintext handshake. "
            "The organization's legacy mail relay only supports implicit TLS. Which port should be configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 465",
                "correct": True,
                "rationale": (
                    "Correct. TCP 465 is the SMTPS port using implicit TLS, where encryption is established "
                    "immediately upon connection — matching the legacy relay's requirement, unlike STARTTLS-based "
                    "submission."
                ),
            },
            {
                "id": "b",
                "text": "TCP 587",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 587 uses STARTTLS, where the connection begins in plaintext and is later "
                    "upgraded to TLS — the opposite of the implicit-TLS-only capability described for the legacy "
                    "relay."
                ),
            },
            {
                "id": "c",
                "text": "TCP 25",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 25 is intended for unauthenticated or server-to-server relay and, when "
                    "encrypted, typically also relies on STARTTLS rather than implicit TLS."
                ),
            },
            {
                "id": "d",
                "text": "TCP 993",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 993 is IMAPS, used for retrieving mail from a mailbox, not for submitting "
                    "outbound messages."
                ),
            },
        ],
        "explanation": (
            "TCP 465 (SMTPS) uses implicit TLS, encrypting the session from the very first byte, which is the "
            "correct choice for a mail relay that does not support the STARTTLS upgrade model used by port 587."
        ),
    },
    {
        "id": "tprt-021",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "Remote employees need to access internal Windows desktops for support. The security team wants to "
            "avoid exposing the remote desktop port directly to the internet. Which architecture BEST balances "
            "functionality and risk while still ultimately using the standard RDP port internally?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Require employees to establish a VPN tunnel first, after which RDP traffic on TCP 3389 is only reachable on the internal network",
                "correct": True,
                "rationale": (
                    "Correct. Placing RDP behind a VPN removes TCP 3389 from direct internet exposure while "
                    "still allowing the standard RDP port to be used once the encrypted, authenticated VPN tunnel "
                    "is established — reducing the attack surface without changing the underlying protocol port."
                ),
            },
            {
                "id": "b",
                "text": "Publish TCP 3389 directly to the internet but change the listening port to 33890 on each desktop",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the port number is obscurity, not a security control; the service "
                    "remains directly internet-facing and scannable, which is exactly what the team wants to "
                    "avoid."
                ),
            },
            {
                "id": "c",
                "text": "Disable NLA on all desktops to simplify direct internet access to RDP",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling Network Level Authentication removes a pre-authentication security "
                    "layer, increasing risk, and still leaves RDP exposed directly to the internet."
                ),
            },
            {
                "id": "d",
                "text": "Forward TCP 3389 through the firewall to all desktops using destination NAT with no additional authentication layer",
                "correct": False,
                "rationale": (
                    "Incorrect. Direct port forwarding to internet-facing RDP with no additional authentication "
                    "layer is a well-known high-risk configuration frequently targeted by ransomware operators."
                ),
            },
        ],
        "explanation": (
            "Best practice is to never expose RDP (TCP 3389) directly to the internet. Instead, require a VPN "
            "or equivalent authenticated tunnel first, so RDP traffic only traverses the internal network once "
            "the remote user is already authenticated and encrypted."
        ),
    },
    {
        "id": "tprt-022",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "During a firewall rule audit, an analyst finds both TCP 22 and TCP 23 open on a Linux jump host. "
            "Interviews confirm SSH is the standard access method and Telnet is a leftover from initial "
            "provisioning that nobody uses. Which action is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable the Telnet service and close TCP 23, retaining TCP 22 with key-based authentication enforced",
                "correct": True,
                "rationale": (
                    "Correct. Telnet (TCP 23) is unused and transmits cleartext credentials, so it should be "
                    "disabled and closed. SSH (TCP 22) with key-based authentication should remain as the sole, "
                    "secure access method."
                ),
            },
            {
                "id": "b",
                "text": "Close TCP 22 and rely solely on TCP 23 since it is already configured and functioning",
                "correct": False,
                "rationale": (
                    "Incorrect. This removes the secure, encrypted access method (SSH) and leaves only the "
                    "cleartext Telnet service active — the opposite of the intended hardening outcome."
                ),
            },
            {
                "id": "c",
                "text": "Leave both ports open since Telnet is confirmed to be unused and therefore poses no risk",
                "correct": False,
                "rationale": (
                    "Incorrect. An open, listening Telnet service is still an active attack surface regardless "
                    "of whether administrators currently use it; unused open ports should be closed as part of "
                    "hardening, not left available."
                ),
            },
            {
                "id": "d",
                "text": "Change the Telnet listening port from 23 to a random high port to reduce scanning exposure",
                "correct": False,
                "rationale": (
                    "Incorrect. Relocating an insecure, cleartext service to a different port is obscurity, not "
                    "a fix; the credentials remain unencrypted and the service should simply be disabled."
                ),
            },
        ],
        "explanation": (
            "Hardening requires removing unnecessary, insecure services entirely, not merely deprioritizing "
            "them. With SSH already serving as the standard access method, the unused cleartext Telnet listener "
            "should be disabled and its port closed."
        ),
    },
    {
        "id": "tprt-023",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "An internal port scan of a mail server returns TCP 995 as open and responding to a TLS handshake. "
            "Which service is MOST likely running on this port?"
        ),
        "options": [
            {
                "id": "a",
                "text": "POP3S — encrypted mailbox retrieval",
                "correct": True,
                "rationale": (
                    "Correct. TCP 995 is the well-known port for POP3 over implicit TLS (POP3S), used by mail "
                    "clients to securely download messages from a mailbox."
                ),
            },
            {
                "id": "b",
                "text": "IMAPS — encrypted mailbox synchronization",
                "correct": False,
                "rationale": (
                    "Incorrect. IMAPS uses TCP 993, not 995. This option misidentifies the specific port/protocol "
                    "pairing."
                ),
            },
            {
                "id": "c",
                "text": "SMTPS — encrypted mail submission",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTPS uses TCP 465, not 995, and handles outgoing mail submission rather than "
                    "mailbox retrieval."
                ),
            },
            {
                "id": "d",
                "text": "LDAPS — encrypted directory queries",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAPS uses TCP 636, not 995, and has nothing to do with mailbox retrieval."
                ),
            },
        ],
        "explanation": (
            "TCP 995 is the standard port for POP3S. Distinguishing the near-identical mail security ports is a "
            "common exam pattern: 995 (POP3S), 993 (IMAPS), 465 (SMTPS), and 587 (submission with STARTTLS)."
        ),
    },
    {
        "id": "tprt-024",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A firewall rule review shows outbound TCP 993 permitted from all corporate laptops to an external "
            "mail provider. Which of the following BEST describes this traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Encrypted IMAP traffic, allowing users to synchronize mailbox folders securely across devices",
                "correct": True,
                "rationale": (
                    "Correct. TCP 993 is IMAPS, the implicit-TLS version of IMAP, which supports encrypted, "
                    "server-side mailbox folder synchronization across multiple devices."
                ),
            },
            {
                "id": "b",
                "text": "Encrypted POP3 traffic used to download and delete messages from the server",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypted POP3 (POP3S) operates on TCP 995, not 993, and does not perform "
                    "server-side folder synchronization the way IMAP does."
                ),
            },
            {
                "id": "c",
                "text": "Encrypted SMTP traffic used to relay outbound messages between mail servers",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypted SMTP relay/submission uses TCP 465 or 587, not 993, and handles "
                    "outbound message delivery rather than mailbox synchronization."
                ),
            },
            {
                "id": "d",
                "text": "An LDAPS query validating the user's directory credentials before mail access is granted",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAPS operates on TCP 636, not 993, and is unrelated to mailbox synchronization "
                    "traffic."
                ),
            },
        ],
        "explanation": (
            "TCP 993 is IMAPS — encrypted IMAP used for synchronized, server-side mailbox access across multiple "
            "devices, distinct from POP3S (995), SMTPS (465), and LDAPS (636)."
        ),
    },
    {
        "id": "tprt-025",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "An open-port inventory for a bastion host lists TCP 21, TCP 22, and TCP 23 as all currently "
            "listening. The host's only sanctioned function is encrypted remote administration and secure file "
            "transfer for administrators. Which ports should be closed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 21 and TCP 23, since both are cleartext services (FTP and Telnet) not required for the sanctioned function",
                "correct": True,
                "rationale": (
                    "Correct. FTP (TCP 21) and Telnet (TCP 23) are unencrypted legacy services. Because the "
                    "sanctioned function is encrypted administration and file transfer, both can be met entirely "
                    "through SSH/SFTP on TCP 22, making 21 and 23 unnecessary and insecure to leave open."
                ),
            },
            {
                "id": "b",
                "text": "TCP 22 only, since SSH consumes more system resources than the other two services",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 22 (SSH) is the encrypted service that fulfills the sanctioned function; "
                    "closing it while leaving cleartext FTP and Telnet open would be the opposite of secure "
                    "hardening."
                ),
            },
            {
                "id": "c",
                "text": "None of the ports, since having multiple remote access options improves availability",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving unnecessary cleartext services open increases the attack surface without "
                    "providing a legitimate availability benefit when an encrypted alternative already satisfies "
                    "all sanctioned functions."
                ),
            },
            {
                "id": "d",
                "text": "TCP 22 and TCP 23, keeping TCP 21 open for anonymous FTP downloads",
                "correct": False,
                "rationale": (
                    "Incorrect. This closes the required encrypted service (SSH) while retaining both cleartext "
                    "services, directly contradicting the stated sanctioned function of encrypted administration "
                    "and file transfer."
                ),
            },
        ],
        "explanation": (
            "SSH (TCP 22) provides both encrypted interactive administration and, via the SFTP subsystem, secure "
            "file transfer — fully covering the sanctioned function. FTP (21) and Telnet (23) are cleartext "
            "legacy services that should be disabled as unnecessary attack surface."
        ),
    },
    {
        "id": "tprt-026",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A third-party HR application needs to authenticate users against the corporate Active Directory "
            "over the internet through a reverse proxy. Which port should be exposed through the proxy to allow "
            "encrypted directory queries without exposing the internal LDAP service in cleartext?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 636",
                "correct": True,
                "rationale": (
                    "Correct. TCP 636 is LDAPS, which encrypts the entire directory query and bind process with "
                    "TLS, making it the appropriate port to expose for external encrypted directory "
                    "authentication."
                ),
            },
            {
                "id": "b",
                "text": "TCP 389",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 389 is standard cleartext LDAP; exposing it externally would transmit bind "
                    "credentials and directory queries unencrypted, contradicting the requirement."
                ),
            },
            {
                "id": "c",
                "text": "TCP 88",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 88 is Kerberos, a ticket-based authentication protocol with a different "
                    "trust model that is not typically exposed externally for third-party directory queries in "
                    "this manner."
                ),
            },
            {
                "id": "d",
                "text": "TCP 3268",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 3268 is the unencrypted Global Catalog port used for forest-wide searches; "
                    "like port 389, it does not provide TLS encryption and would still expose queries in "
                    "cleartext."
                ),
            },
        ],
        "explanation": (
            "LDAPS (TCP 636) wraps the entire directory session, including the bind, in TLS. Standard LDAP "
            "(389) and the Global Catalog (3268) are both cleartext by default and should not be exposed for "
            "external authentication without their encrypted equivalents (636 and 3269, respectively)."
        ),
    },
    {
        "id": "tprt-027",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A network monitoring platform is configured to receive unsolicited notifications whenever a managed "
            "switch's interface goes down, in addition to periodically polling device statistics. Which two "
            "port roles describe the poll traffic and the unsolicited notification traffic, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP 161 for polling (GET requests) and UDP 162 for unsolicited trap notifications",
                "correct": True,
                "rationale": (
                    "Correct. SNMP managers poll agents for statistics using GET requests on UDP 161, while "
                    "agents proactively push unsolicited trap notifications, such as an interface-down event, to "
                    "the manager on UDP 162."
                ),
            },
            {
                "id": "b",
                "text": "UDP 162 for polling and UDP 161 for unsolicited trap notifications",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the standard roles; polling occurs on 161 and traps are received "
                    "on 162, not the other way around."
                ),
            },
            {
                "id": "c",
                "text": "TCP 161 for polling and TCP 162 for unsolicited trap notifications",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP conventionally operates over UDP, not TCP, for both polling and trap "
                    "delivery; specifying TCP misidentifies the transport protocol."
                ),
            },
            {
                "id": "d",
                "text": "UDP 514 for polling and UDP 162 for unsolicited trap notifications",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 514 is used for syslog message forwarding, not SNMP polling; this option "
                    "misidentifies the polling port."
                ),
            },
        ],
        "explanation": (
            "SNMP uses UDP 161 for manager-initiated polling (GET/GETNEXT/SET requests) and UDP 162 for "
            "agent-initiated, unsolicited trap and inform notifications — a commonly tested port-role "
            "distinction."
        ),
    },
    {
        "id": "tprt-028",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A secure baseline standard for newly imaged servers requires the removal of legacy insecure "
            "protocols. Select the TWO changes that correctly implement 'disable insecure remote administration "
            "and file-transfer protocols' as part of the baseline."
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable the Telnet daemon (TCP 23) and require SSH (TCP 22) with key-based authentication for all remote CLI administration.",
                "correct": True,
                "rationale": (
                    "Correct. Telnet transmits credentials in cleartext and has no legitimate place in a modern "
                    "secure baseline; SSH with key-based authentication is the standard, encrypted replacement "
                    "for CLI administration."
                ),
            },
            {
                "id": "b",
                "text": "Disable the plaintext FTP service (TCP 20/21) and require SFTP (TCP 22) or FTPS (TCP 989/990) for file transfer.",
                "correct": True,
                "rationale": (
                    "Correct. Plaintext FTP exposes credentials and file contents; replacing it with SFTP or "
                    "FTPS ensures file transfers are encrypted, satisfying the baseline's secure protocol "
                    "requirement."
                ),
            },
            {
                "id": "c",
                "text": "Leave Telnet enabled on TCP 23 but require a strong, complex password for the Telnet login prompt.",
                "correct": False,
                "rationale": (
                    "Incorrect. A stronger password does not encrypt the session; Telnet still transmits that "
                    "password itself in cleartext, so the credential remains exposed regardless of its "
                    "complexity."
                ),
            },
            {
                "id": "d",
                "text": "Move the FTP service from TCP 21 to a randomized high port while keeping the protocol unencrypted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Relocating an unencrypted protocol to a different port is obscurity, not "
                    "encryption; the baseline requires eliminating cleartext protocols, not merely hiding them."
                ),
            },
        ],
        "explanation": (
            "A secure baseline eliminates cleartext protocols (Telnet, FTP) entirely, replacing them with "
            "encrypted equivalents (SSH for administration; SFTP or FTPS for file transfer) rather than relying "
            "on stronger passwords or port obscurity, neither of which adds encryption."
        ),
    },
    {
        "id": "tprt-029",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A legacy public file drop server allows anonymous FTP logins on TCP 21 so external partners can "
            "upload files without individual credentials. A security review flags this as unacceptable due to "
            "cleartext transmission and lack of accountability. Which replacement satisfies both encryption and "
            "per-partner accountability requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Issue each partner an individual SSH key pair and require uploads via SFTP on TCP 22",
                "correct": True,
                "rationale": (
                    "Correct. SFTP over SSH (TCP 22) encrypts the session, and issuing individual key pairs per "
                    "partner provides accountability (each connection is tied to a specific identity), directly "
                    "resolving both the encryption and accountability gaps."
                ),
            },
            {
                "id": "b",
                "text": "Keep anonymous FTP but require partners to email their intended filenames in advance for tracking",
                "correct": False,
                "rationale": (
                    "Incorrect. Emailing filenames does not encrypt the FTP session or tie individual uploads to "
                    "authenticated identities; anonymous cleartext access remains fundamentally unaccountable."
                ),
            },
            {
                "id": "c",
                "text": "Restrict anonymous FTP to read-only access on TCP 21",
                "correct": False,
                "rationale": (
                    "Incorrect. Read-only access does not address the requirement, since partners still need to "
                    "upload files, and the session remains unencrypted and anonymous regardless of permission "
                    "level."
                ),
            },
            {
                "id": "d",
                "text": "Allow anonymous FTP only from an allow-listed range of partner IP addresses",
                "correct": False,
                "rationale": (
                    "Incorrect. IP allow-listing narrows the source but does nothing to encrypt the session or "
                    "identify which specific individual uploaded a file, leaving both the confidentiality and "
                    "accountability gaps unresolved."
                ),
            },
        ],
        "explanation": (
            "SFTP over SSH (TCP 22) with individually issued key pairs provides both encryption in transit and "
            "per-user accountability, resolving the two specific weaknesses of anonymous cleartext FTP: lack of "
            "confidentiality and lack of identity attribution."
        ),
    },
    {
        "id": "tprt-030",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A DNS administrator observes an unusually large response on TCP port 53 from an external secondary "
            "name server, distinct from the typical small UDP query/response pairs seen for ordinary lookups. "
            "Which activity MOST likely explains this traffic pattern?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A zone transfer (AXFR/IXFR), which uses TCP 53 because the response can exceed the size limits of a single UDP datagram",
                "correct": True,
                "rationale": (
                    "Correct. Zone transfers between primary and secondary name servers use TCP 53 specifically "
                    "because the full zone data typically exceeds what fits in a single UDP packet, unlike "
                    "ordinary resolution queries which use UDP 53."
                ),
            },
            {
                "id": "b",
                "text": "A standard recursive DNS lookup for a single hostname",
                "correct": False,
                "rationale": (
                    "Incorrect. A single-hostname recursive lookup is small and normally uses UDP 53, not a "
                    "large TCP 53 response, and would not match the traffic pattern described."
                ),
            },
            {
                "id": "c",
                "text": "A DNS over TLS session between the resolver and an upstream provider",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS over TLS uses TCP port 853, not port 53; this option misidentifies the port "
                    "associated with encrypted DNS."
                ),
            },
            {
                "id": "d",
                "text": "An NTP time synchronization request from the name server",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP uses UDP 123 and has nothing to do with DNS zone data; it would not appear "
                    "as large TCP 53 traffic between name servers."
                ),
            },
        ],
        "explanation": (
            "While ordinary DNS queries and responses typically use UDP 53, zone transfers between authoritative "
            "and secondary name servers use TCP 53 because the transferred zone data commonly exceeds a single "
            "UDP datagram's size limit — a well-known exception to the 'DNS is UDP' generalization."
        ),
    },
    {
        "id": "tprt-031",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A hardening checklist for network switches requires disabling any protocol that transmits "
            "authorization strings in cleartext over UDP for device monitoring. Which specific change satisfies "
            "this requirement while preserving existing monitoring dashboards built around the same UDP ports?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable SNMPv1/v2c and enable SNMPv3 with authentication and privacy (encryption) on UDP 161/162",
                "correct": True,
                "rationale": (
                    "Correct. SNMPv1/v2c community strings are cleartext authorization tokens over UDP. SNMPv3 "
                    "adds authenticated, encrypted communication while remaining on the same UDP 161 (polling) "
                    "and 162 (traps) ports, preserving compatibility with existing dashboards."
                ),
            },
            {
                "id": "b",
                "text": "Migrate all device monitoring from SNMP to syslog on UDP 514",
                "correct": False,
                "rationale": (
                    "Incorrect. Syslog on UDP 514 is also cleartext and serves a different purpose (log message "
                    "forwarding, not polling device statistics); it does not satisfy the requirement and would "
                    "break existing SNMP-based dashboards."
                ),
            },
            {
                "id": "c",
                "text": "Continue using SNMPv2c but rotate the community string every 24 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. Frequent rotation reduces the exposure window slightly but does not eliminate "
                    "cleartext transmission; the community string is still sent unencrypted with every request."
                ),
            },
            {
                "id": "d",
                "text": "Restrict SNMPv2c traffic to a dedicated management VLAN without changing the protocol version",
                "correct": False,
                "rationale": (
                    "Incorrect. Network segmentation reduces exposure to a smaller set of hosts but does not "
                    "encrypt the community strings; anyone with access to that VLAN can still capture cleartext "
                    "credentials."
                ),
            },
        ],
        "explanation": (
            "SNMPv3 directly resolves the cleartext-authorization weakness of SNMPv1/v2c by adding "
            "authentication and optional encryption, all while remaining on the standard UDP 161/162 ports — "
            "satisfying the hardening requirement without breaking existing monitoring integrations."
        ),
    },
    {
        "id": "tprt-032",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A configuration management tool used to build the organization's golden server image is found to "
            "enable both the Telnet daemon and an anonymous FTP server by default, because the base OS image "
            "ships that way. Which fix belongs in the golden image build process itself, rather than as a "
            "post-deployment task?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Modify the golden image build script to disable and remove the Telnet and anonymous FTP services before the image is captured and distributed",
                "correct": True,
                "rationale": (
                    "Correct. Fixing the golden image at build time ensures every server provisioned from that "
                    "image is hardened from first boot, eliminating the need for error-prone, inconsistent "
                    "post-deployment remediation across the fleet."
                ),
            },
            {
                "id": "b",
                "text": "Add a manual step to the deployment runbook instructing administrators to disable Telnet and FTP after each new server is provisioned",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual, per-server remediation steps are exactly the error-prone process that "
                    "leads to configuration drift; the fix belongs in the automated image build, not a manual "
                    "runbook step performed inconsistently after the fact."
                ),
            },
            {
                "id": "c",
                "text": "Schedule a quarterly vulnerability scan to catch any servers still running Telnet or FTP",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning only detects the problem after every new server has already been "
                    "provisioned insecurely; it does not prevent the root-cause misconfiguration baked into the "
                    "golden image itself."
                ),
            },
            {
                "id": "d",
                "text": "Document the risk in the organization's risk register and accept it as a known limitation of the base OS image",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk acceptance leaves the insecure default services active fleet-wide when a "
                    "straightforward build-time fix is available; accepting an easily remediable, high-impact "
                    "gap is not appropriate here."
                ),
            },
        ],
        "explanation": (
            "Secure baselines must be enforced at the source — the golden image build process — so that every "
            "server provisioned from it inherits the hardened configuration automatically, rather than relying "
            "on inconsistent manual steps or after-the-fact detection."
        ),
    },
    {
        "id": "tprt-033",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A host-based firewall baseline policy requires that only ports required for a server's specific "
            "role remain open, following the principle of least functionality. An audit of a database server "
            "shows TCP 22, TCP 1433 (its database port), TCP 21, and TCP 23 all listening. Which ports should "
            "the baseline close?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 21 and TCP 23, since FTP and Telnet are not required for the server's database role and are cleartext legacy services",
                "correct": True,
                "rationale": (
                    "Correct. Least functionality requires closing any port/service not needed for the server's "
                    "defined role. FTP and Telnet serve no purpose on a dedicated database server and are also "
                    "insecure cleartext protocols, making them clear candidates for closure."
                ),
            },
            {
                "id": "b",
                "text": "TCP 22 and TCP 1433, since SSH and the database service are the highest-risk ports on the host",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 22 (administrative SSH access) and TCP 1433 (the database service itself) "
                    "are both required for the server's role; closing them would break required functionality, "
                    "which contradicts the goal of the baseline."
                ),
            },
            {
                "id": "c",
                "text": "All four ports, to achieve the most restrictive possible configuration",
                "correct": False,
                "rationale": (
                    "Incorrect. Closing TCP 22 and TCP 1433 would eliminate legitimate administrative access and "
                    "the database service itself, breaking required functionality rather than applying least "
                    "functionality correctly."
                ),
            },
            {
                "id": "d",
                "text": "None of the ports, since a host-based firewall should only filter inbound internet traffic, not internal role-based access",
                "correct": False,
                "rationale": (
                    "Incorrect. Host-based firewalls are specifically used to enforce least functionality by "
                    "restricting listening services to only those required for the host's role, regardless of "
                    "whether traffic originates internally or externally."
                ),
            },
        ],
        "explanation": (
            "Least functionality requires disabling any service unnecessary for a host's defined role. On a "
            "dedicated database server, SSH (administration) and the database port are required, while cleartext "
            "legacy services like FTP and Telnet serve no role-related purpose and should be closed."
        ),
    },
    {
        "id": "tprt-034",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A web server's administrative console is currently reachable on TCP 80 from the internal management "
            "VLAN, and the secure baseline standard requires all administrative interfaces to be encrypted in "
            "transit. Which change brings the console into compliance with the baseline?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable HTTPS on TCP 443 for the administrative console with a valid certificate, and disable the plaintext TCP 80 listener",
                "correct": True,
                "rationale": (
                    "Correct. Moving the administrative interface to HTTPS on TCP 443 encrypts all console "
                    "traffic, including login credentials, and disabling the plaintext TCP 80 listener ensures "
                    "there is no unencrypted fallback path, satisfying the baseline requirement."
                ),
            },
            {
                "id": "b",
                "text": "Restrict access to TCP 80 using source IP allow-listing from the management VLAN only",
                "correct": False,
                "rationale": (
                    "Incorrect. IP allow-listing limits which hosts can connect but does not encrypt the "
                    "session; traffic between an allowed host and the console remains cleartext and vulnerable "
                    "to interception on the internal network."
                ),
            },
            {
                "id": "c",
                "text": "Require a stronger administrative password on the console while keeping it on TCP 80",
                "correct": False,
                "rationale": (
                    "Incorrect. A stronger password does not encrypt the transport channel; it would still be "
                    "transmitted in cleartext over TCP 80, failing the encryption requirement of the baseline."
                ),
            },
            {
                "id": "d",
                "text": "Move the administrative console from TCP 80 to TCP 8080, keeping the protocol unchanged",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the port number without adding TLS is obscurity, not encryption; the "
                    "console traffic remains unencrypted plaintext HTTP."
                ),
            },
        ],
        "explanation": (
            "A secure baseline requiring encrypted administrative interfaces is satisfied by enabling HTTPS "
            "(TCP 443) with a valid certificate and eliminating the plaintext HTTP (TCP 80) fallback, not by "
            "access restriction, password strength, or port obscurity alone."
        ),
    },
    {
        "id": "tprt-035",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "As part of a secure email baseline, the security team requires that mailbox retrieval protocols "
            "used by internal staff never transmit credentials in cleartext, regardless of whether staff use "
            "POP3-style or IMAP-style clients. Which single configuration change enforces this across both "
            "client types?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable plaintext listeners on TCP 110 and TCP 143, permitting mailbox retrieval only on TCP 995 (POP3S) and TCP 993 (IMAPS)",
                "correct": True,
                "rationale": (
                    "Correct. Disabling the cleartext POP3 (110) and IMAP (143) listeners while requiring their "
                    "encrypted counterparts, POP3S (995) and IMAPS (993), ensures credentials are protected "
                    "regardless of which mailbox protocol style staff use."
                ),
            },
            {
                "id": "b",
                "text": "Disable TCP 110 only, since IMAP on TCP 143 is inherently more secure than POP3",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard IMAP on TCP 143 is just as cleartext as POP3 on TCP 110; leaving it "
                    "enabled would still expose IMAP client credentials, failing the baseline for that client "
                    "type."
                ),
            },
            {
                "id": "c",
                "text": "Require staff to change their mailbox password monthly while keeping TCP 110 and TCP 143 open",
                "correct": False,
                "rationale": (
                    "Incorrect. Frequent password changes do not encrypt the retrieval session; credentials sent "
                    "on TCP 110 or TCP 143 remain exposed in cleartext regardless of how often they are rotated."
                ),
            },
            {
                "id": "d",
                "text": "Restrict TCP 110 and TCP 143 to the internal network only, without requiring encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting network scope reduces external exposure but does nothing to encrypt "
                    "credentials on the internal segment, where interception via ARP spoofing or a compromised "
                    "host remains possible."
                ),
            },
        ],
        "explanation": (
            "To eliminate cleartext credential exposure across both mailbox-retrieval styles, the baseline must "
            "disable both cleartext listeners (110 and 143) and require their encrypted equivalents (995 and "
            "993) — password policy and network restriction alone do not add encryption."
        ),
    },
    {
        "id": "tprt-036",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM correlation rule generates a high-priority alert after detecting repeated successful "
            "outbound connections from an internal server to multiple external hosts on TCP 23. No legitimate "
            "business justification exists for this traffic. Which finding and follow-up action are MOST "
            "appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The server is generating outbound Telnet connections, a cleartext protocol rarely legitimate for outbound use; the analyst should isolate the host and investigate for compromise or unauthorized software.",
                "correct": True,
                "rationale": (
                    "Correct. TCP 23 is Telnet. Unexplained outbound Telnet connections to multiple external "
                    "hosts are a strong indicator of compromise (e.g., malware scanning for other Telnet-exposed "
                    "devices), warranting isolation and investigation rather than dismissal."
                ),
            },
            {
                "id": "b",
                "text": "The server is generating outbound HTTPS connections, which is normal web browsing behavior and can be closed as a false positive.",
                "correct": False,
                "rationale": (
                    "Incorrect. HTTPS uses TCP 443, not TCP 23; this option misidentifies the protocol and would "
                    "cause the analyst to dismiss a legitimate indicator of compromise."
                ),
            },
            {
                "id": "c",
                "text": "The server is performing routine LDAPS directory queries and no further action is required.",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAPS uses TCP 636, not TCP 23; this misidentification would lead to closing an "
                    "alert that actually warrants investigation."
                ),
            },
            {
                "id": "d",
                "text": "The server is performing scheduled NTP time synchronization and the alert can be tuned to suppress this port going forward.",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP uses UDP 123, not TCP 23; suppressing this alert based on a misidentified "
                    "protocol would hide a legitimate security concern from future detection."
                ),
            },
        ],
        "explanation": (
            "TCP 23 is Telnet. Repeated unexplained outbound Telnet connections from an internal server are a "
            "classic indicator of malware scanning for other exposed devices; SIEM analysts should correctly "
            "identify the port and escalate to isolation and investigation rather than dismiss it."
        ),
    },
    {
        "id": "tprt-037",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM dashboard shows a spike in TCP 445 connection attempts from a single compromised workstation "
            "to dozens of other internal hosts within a short time window, none of which are file servers. Which "
            "conclusion should the analyst draw, and what does the involved port indicate about the likely "
            "technique?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This pattern is consistent with SMB-based lateral movement, since TCP 445 is the Windows file-sharing port commonly abused to spread between hosts after initial compromise.",
                "correct": True,
                "rationale": (
                    "Correct. TCP 445 (SMB) is frequently abused by attackers and worms for lateral movement, "
                    "using stolen credentials or exploits to connect to and infect additional internal hosts — "
                    "matching the fan-out pattern described."
                ),
            },
            {
                "id": "b",
                "text": "This pattern is consistent with normal DNS resolution traffic between the workstation and internal resolvers.",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS uses port 53, not 445; this option misidentifies the protocol and would "
                    "cause the analyst to overlook a likely lateral-movement indicator."
                ),
            },
            {
                "id": "c",
                "text": "This pattern is consistent with legitimate NTP synchronization requests from the workstation to internal time servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP uses UDP 123, not TCP 445, and would not exhibit a fan-out pattern to dozens "
                    "of non-time-server hosts; this misidentifies the protocol."
                ),
            },
            {
                "id": "d",
                "text": "This pattern is consistent with the workstation performing routine LDAPS queries against multiple domain controllers.",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAPS uses TCP 636, not 445, and organizations typically have only a handful of "
                    "domain controllers, not dozens of destination hosts, making this an implausible explanation."
                ),
            },
        ],
        "explanation": (
            "TCP 445 is SMB, historically abused for worm propagation and attacker lateral movement due to its "
            "file-sharing and remote-execution capabilities. A single host rapidly connecting to many internal "
            "peers on 445 is a well-known indicator that SIEM correlation rules are specifically built to detect."
        ),
    },
    {
        "id": "tprt-038",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "While tuning SIEM correlation rules for insecure-protocol usage, an analyst wants alerts to fire "
            "only on genuinely cleartext, credential-bearing protocols rather than their encrypted counterparts. "
            "Select the TWO port/protocol pairings that should be flagged as cleartext and therefore included in "
            "the insecure-protocol detection rule."
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 143 (IMAP) carrying an unencrypted authentication exchange",
                "correct": True,
                "rationale": (
                    "Correct. Standard IMAP on TCP 143 transmits credentials in cleartext unless STARTTLS is "
                    "explicitly negotiated; observing plaintext authentication on this port is a valid indicator "
                    "for the insecure-protocol rule."
                ),
            },
            {
                "id": "b",
                "text": "TCP 389 (LDAP) carrying an unencrypted simple bind request",
                "correct": True,
                "rationale": (
                    "Correct. Standard LDAP on TCP 389 transmits simple bind credentials in cleartext unless "
                    "StartTLS is used; a plaintext bind on this port is a legitimate indicator for the "
                    "insecure-protocol detection rule."
                ),
            },
            {
                "id": "c",
                "text": "TCP 993 (IMAPS) carrying a TLS-encrypted authentication exchange",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 993 is the implicit-TLS IMAPS port; a TLS-encrypted exchange on this port is "
                    "the expected, secure behavior and should not be flagged as an insecure-protocol finding."
                ),
            },
            {
                "id": "d",
                "text": "TCP 636 (LDAPS) carrying a TLS-encrypted bind request",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 636 is the implicit-TLS LDAPS port; an encrypted bind on this port is exactly "
                    "the secure behavior expected and should not trigger the insecure-protocol rule."
                ),
            },
        ],
        "explanation": (
            "A well-tuned insecure-protocol correlation rule should alert on cleartext authentication over the "
            "unencrypted ports (143/IMAP, 389/LDAP, 110/POP3, 21/FTP, 23/Telnet) while excluding their properly "
            "encrypted counterparts (993/995/636/990/22), which represent expected, secure traffic."
        ),
    },
    {
        "id": "tprt-039",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM analyst notices that a single internal host is generating an abnormally high volume of UDP "
            "port 53 queries with unusually long, encoded-looking subdomain labels directed at an external "
            "authoritative name server the organization does not recognize. Which conclusion and recommended "
            "control BEST fit this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The pattern is consistent with DNS tunneling used for data exfiltration or command-and-control; the analyst should investigate the host and consider enforcing DNS filtering or requiring encrypted, inspected DNS through an approved resolver.",
                "correct": True,
                "rationale": (
                    "Correct. Abnormally long, encoded subdomain labels sent at high volume to an unrecognized "
                    "external authoritative server are a textbook signature of DNS tunneling, which abuses port "
                    "53's near-universal firewall allowance to exfiltrate data or maintain covert C2 channels."
                ),
            },
            {
                "id": "b",
                "text": "The pattern is normal recursive resolution behavior and requires no further investigation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Ordinary recursive lookups do not involve abnormally long encoded labels sent at "
                    "high volume to an unfamiliar external authoritative server; dismissing this pattern ignores "
                    "a known exfiltration technique."
                ),
            },
            {
                "id": "c",
                "text": "The pattern indicates the host is performing a legitimate zone transfer and should be allowed to continue uninterrupted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Zone transfers use TCP 53 between authorized primary/secondary name servers, not "
                    "high-volume UDP queries with encoded labels from an arbitrary internal host to an unknown "
                    "external server."
                ),
            },
            {
                "id": "d",
                "text": "The pattern indicates the host is using DNS over TLS and the traffic is already fully encrypted and safe to ignore.",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS over TLS uses TCP 853, not UDP 53; this traffic is explicitly on UDP 53 and "
                    "is not DoT, so this explanation misidentifies both the port and the risk."
                ),
            },
        ],
        "explanation": (
            "DNS tunneling abuses the near-universal outbound allowance for port 53 by encoding data into "
            "subdomain labels sent to an attacker-controlled authoritative server. SIEM correlation rules "
            "watching for abnormal query volume, label length/entropy, and unrecognized destination servers are "
            "designed specifically to catch this technique."
        ),
    },
    {
        "id": "tprt-040",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM correlation rule flags an internal user account requesting an unusually large number of "
            "service tickets on port 88 in a short period, a pattern associated with an attacker harvesting "
            "ticket-granting service tickets for offline password cracking. Which port and protocol are involved, "
            "and what is the technique commonly called?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Kerberos on TCP/UDP 88; the technique is Kerberoasting, which harvests service tickets to crack service account passwords offline.",
                "correct": True,
                "rationale": (
                    "Correct. Port 88 is Kerberos. Kerberoasting abuses legitimate service ticket requests "
                    "(which are encrypted with the service account's password hash) to harvest tickets for "
                    "offline brute-force or dictionary cracking, matching the described alert pattern."
                ),
            },
            {
                "id": "b",
                "text": "LDAP on TCP 389; the technique is an LDAP injection attack against the directory service.",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP uses TCP 389, not port 88, and LDAP injection is a different attack "
                    "targeting malformed query input, not the mass ticket-request pattern described."
                ),
            },
            {
                "id": "c",
                "text": "SMB on TCP 445; the technique is pass-the-hash lateral movement.",
                "correct": False,
                "rationale": (
                    "Incorrect. SMB uses TCP 445, not port 88, and pass-the-hash involves reusing captured NTLM "
                    "hashes for authentication, not requesting Kerberos service tickets at an abnormal rate."
                ),
            },
            {
                "id": "d",
                "text": "RDP on TCP 3389; the technique is a brute-force password-spraying attack.",
                "correct": False,
                "rationale": (
                    "Incorrect. RDP uses TCP 3389, not port 88, and password spraying targets login attempts "
                    "directly rather than harvesting Kerberos service tickets for offline cracking."
                ),
            },
        ],
        "explanation": (
            "Kerberos operates on TCP/UDP 88. Kerberoasting exploits the fact that service tickets are encrypted "
            "with a service account's password hash, allowing an attacker who requests many such tickets to "
            "attempt offline cracking without triggering account lockouts — a pattern SIEM rules can detect via "
            "abnormal ticket-request volume per account."
        ),
    },
]
