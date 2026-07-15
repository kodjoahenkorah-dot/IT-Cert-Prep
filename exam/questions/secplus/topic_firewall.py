"""CompTIA Security+ (SY0-701) practice question bank — targeted topic drill:
Firewalls, ACL/rule logic, and appliance identification.

44 scenario-driven questions (40 multiple_choice + 4 multiple_response), all
domain 3, focused on:

  * Firewall rules and ACLs — source/destination/port/protocol, allow vs.
    deny, inbound vs. outbound, implicit deny, rule order (specific-before-
    general, shadowed rules), DMZ/screened-subnet placement, and
    least-privilege firewall logic, including small ACL tables rendered in
    the stem.
  * Appliance/control identification under pressure: WAF vs. firewall vs.
    IDS vs. IPS vs. TLS, with distractors drawn from the *other* correct-in-
    a-different-scenario appliance so only real understanding scores.

study_topic values are restricted to the domain-3 labels: "Firewalls",
"Network appliances", "Secure communication (VPN/TLS/IPSec)", "Attack
surface reduction", "SDN and logical segmentation", and "Port security and
802.1X".
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # 1-10: ACL / rule-table reading and rule-order logic (Firewalls)
    # ------------------------------------------------------------------ #
    {
        "id": "tfw-001",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A perimeter firewall's ACL is evaluated top-down. The current rule set is:\n"
            "1. PERMIT  TCP  ANY          10.0.5.10  443\n"
            "2. DENY    TCP  ANY          10.0.5.0/24  ANY\n"
            "3. PERMIT  TCP  10.0.1.0/24  10.0.5.20  22\n"
            "4. DENY    ANY  ANY          ANY  ANY  (implicit)\n"
            "A host on 10.0.1.0/24 attempts an SSH (TCP/22) connection to 10.0.5.20. "
            "What is the outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The connection is denied, because rule 2 matches the destination "
                    "subnet first and the firewall stops evaluating further rules"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rule evaluation is top-down and stops at the first "
                    "match. Rule 2 (deny any TCP to 10.0.5.0/24) matches before the "
                    "engine ever reaches rule 3, so the SSH attempt is blocked — a "
                    "classic shadowed-rule problem caused by a general deny placed "
                    "above a more specific permit."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The connection is permitted, because rule 3 specifically allows "
                    "10.0.1.0/24 to reach 10.0.5.20 on port 22"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule 3 would allow this traffic if it were reached, "
                    "but first-match, top-down evaluation means rule 2's broader "
                    "deny is applied before the engine ever gets to rule 3."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The connection is denied, because no rule explicitly matches "
                    "TCP/22 traffic and the implicit deny at the bottom applies"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The traffic is denied, but not by the implicit "
                    "deny — rule 2 matches and blocks it long before evaluation "
                    "reaches the bottom of the list."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The connection is permitted, because rule 1 already allows "
                    "traffic to 10.0.5.10 and this extends to the entire /24"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule 1 only matches the single host 10.0.5.10, not "
                    "the whole /24, and does not apply to a connection destined for "
                    "10.0.5.20."
                ),
            },
        ],
        "explanation": (
            "This ACL demonstrates a shadowed rule: a specific permit (rule 3) "
            "placed below a broader deny (rule 2) is never reached, because "
            "top-down, first-match evaluation stops at rule 2. Specific rules must "
            "be placed above general ones to take effect."
        ),
    },
    {
        "id": "tfw-002",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "An administrator wants hosts on 10.0.1.0/24 to reach a database server "
            "at 10.0.5.20 on TCP/1433, while all other traffic to the 10.0.5.0/24 "
            "subnet remains blocked. The current ACL is:\n"
            "1. DENY  TCP  ANY  10.0.5.0/24  ANY\n"
            "2. DENY  ANY  ANY  ANY  ANY  (implicit)\n"
            "Which change correctly achieves the goal?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Insert a new rule ABOVE rule 1: PERMIT TCP 10.0.1.0/24 10.0.5.20 1433"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because evaluation is top-down and stops at first "
                    "match, the specific permit must be placed before the broader "
                    "deny so it is evaluated first for matching traffic, while all "
                    "other traffic to 10.0.5.0/24 still falls through to rule 1's "
                    "deny."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Insert a new rule BELOW rule 1: PERMIT TCP 10.0.1.0/24 10.0.5.20 1433"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Placed below rule 1, the new permit would be "
                    "shadowed — rule 1's broad deny already matches all TCP "
                    "traffic to the 10.0.5.0/24 subnet and stops evaluation before "
                    "the new rule is ever reached."
                ),
            },
            {
                "id": "c",
                "text": "Change rule 1 from DENY to PERMIT for the entire subnet",
                "correct": False,
                "rationale": (
                    "Incorrect. This would open all TCP traffic from anywhere to "
                    "the entire 10.0.5.0/24 subnet, violating least privilege and "
                    "the requirement that only the database port be reachable, and "
                    "only from 10.0.1.0/24."
                ),
            },
            {
                "id": "d",
                "text": "Delete the implicit deny (rule 2) so unmatched traffic is allowed",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing the implicit deny — which cannot actually "
                    "be deleted on most platforms — would allow all otherwise "
                    "unmatched traffic through, the opposite of least-privilege "
                    "ACL design."
                ),
            },
        ],
        "explanation": (
            "In a top-down, first-match ACL, more specific permit rules must be "
            "ordered above broader deny rules that would otherwise shadow them; "
            "the deny should remain to block all other traffic to the subnet."
        ),
    },
    {
        "id": "tfw-003",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall ACL reads:\n"
            "1. PERMIT  TCP  ANY  10.0.2.30  80\n"
            "2. PERMIT  TCP  ANY  10.0.2.30  443\n"
            "3. DENY    TCP  ANY  10.0.2.0/24  ANY\n"
            "4. PERMIT  UDP  10.0.3.0/24  10.0.2.40  53\n"
            "5. DENY    ANY  ANY  ANY  ANY  (implicit)\n"
            "A host on 10.0.3.0/24 sends a DNS query (UDP/53) to 10.0.2.40. What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The query is permitted by rule 4, because rules 1-3 only match "
                    "TCP traffic and do not affect UDP evaluation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rules 1-3 all specify protocol TCP, so a UDP packet "
                    "does not match any of them regardless of destination. "
                    "Evaluation continues to rule 4, which explicitly permits UDP/53 "
                    "from 10.0.3.0/24 to 10.0.2.40."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The query is denied by rule 3, because 10.0.2.40 falls within "
                    "the 10.0.2.0/24 subnet that rule 3 blocks"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule 3 only matches protocol TCP; a UDP packet "
                    "never matches it, so evaluation continues past rule 3 instead "
                    "of being blocked there."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The query is denied by the implicit deny, because no rule "
                    "before it references UDP traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule 4 explicitly matches this UDP/53 traffic, so "
                    "evaluation never reaches the implicit deny at the bottom of "
                    "the list."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The query is denied, because rules 1 and 2 only permit web "
                    "traffic and every other port is implicitly blocked by them"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rules 1 and 2 do not create a blanket restriction "
                    "on all other ports — each ACL rule matches independently, and "
                    "unmatched traffic simply continues to the next rule rather "
                    "than being denied by an unrelated permit rule."
                ),
            },
        ],
        "explanation": (
            "ACL rules match on the full tuple of protocol, source, destination, "
            "and port. A rule that specifies TCP has no effect on UDP traffic, no "
            "matter how similar the addresses look, so evaluation correctly falls "
            "through to the rule that matches all fields."
        ),
    },
    {
        "id": "tfw-004",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A junior analyst asks why an internal host cannot reach an external "
            "website even though no explicit DENY rule references that website's "
            "IP address anywhere in the firewall's ACL. Which concept BEST explains "
            "this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Implicit deny: firewalls drop any traffic that does not match "
                    "an explicit permit rule, even without a specific deny entry"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Implicit deny is the default final rule on virtually "
                    "all firewalls: traffic that fails to match any explicit permit "
                    "rule is dropped by default, with no dedicated deny rule "
                    "required."
                ),
            },
            {
                "id": "b",
                "text": (
                    "NAT exhaustion: the firewall has run out of available public "
                    "IP addresses to translate outbound connections"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NAT exhaustion produces failed outbound connections "
                    "for unrelated reasons — a lack of translation addresses — not "
                    "the ACL-based blocking behavior described, and nothing in the "
                    "scenario suggests a pool of NAT addresses is even in use."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Split tunneling: the client's VPN configuration is routing "
                    "this traffic around the corporate gateway"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Split tunneling concerns how a remote VPN client "
                    "routes traffic between the tunnel and the local internet "
                    "connection; it has no bearing on an internal host's firewall "
                    "ACL evaluation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Asymmetric routing: return traffic is taking a different path "
                    "than outbound traffic and is dropped by a stateful inspection "
                    "mismatch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Asymmetric routing can cause stateful firewalls to "
                    "drop legitimate return traffic, but the question specifically "
                    "asks why there is no explicit rule at all governing this "
                    "traffic — that is the signature of implicit deny, not a "
                    "routing/state mismatch."
                ),
            },
        ],
        "explanation": (
            "Implicit deny means a firewall blocks anything not explicitly "
            "permitted, so the absence of a deny rule for a specific destination "
            "does not mean traffic to it is allowed."
        ),
    },
    {
        "id": "tfw-005",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall ACL is:\n"
            "1. PERMIT  TCP  10.0.4.0/24  ANY  ANY\n"
            "2. DENY    TCP  10.0.4.15    ANY  ANY\n"
            "3. DENY    ANY  ANY          ANY  ANY  (implicit)\n"
            "Host 10.0.4.15 is a member of the 10.0.4.0/24 subnet and needs to be "
            "blocked from all outbound TCP traffic while the rest of the subnet "
            "keeps access. Does this rule set achieve that, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "No — 10.0.4.15 still has full outbound TCP access, because "
                    "rule 1 already matches its traffic and permits it before rule "
                    "2 is ever evaluated"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 10.0.4.15 is part of 10.0.4.0/24, so rule 1's broad "
                    "permit matches its traffic first under top-down, first-match "
                    "evaluation. Rule 2's more specific deny is shadowed and never "
                    "takes effect, so the host is not actually blocked."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Yes — rule 2 specifically denies 10.0.4.15, so its traffic is "
                    "blocked regardless of where the rule appears in the list"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule order matters: because rule 1 is evaluated "
                    "first and already matches 10.0.4.15's traffic, rule 2 is never "
                    "reached for that host, so it is not blocked."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Yes — more specific host-based rules always take precedence "
                    "over broader subnet-based rules automatically, regardless of "
                    "position"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Most firewall ACLs do not automatically reorder by "
                    "specificity; they evaluate strictly in the order the rules are "
                    "listed, so position determines precedence, not specificity "
                    "alone."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No — the implicit deny at the bottom overrides rule 1, "
                    "blocking all subnet traffic including 10.0.4.15"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The implicit deny only applies to traffic that "
                    "matches no earlier rule; rule 1 already matches and permits "
                    "traffic from the entire subnet, so the implicit deny is never "
                    "reached for this traffic."
                ),
            },
        ],
        "explanation": (
            "To block a specific host within an otherwise-permitted subnet, the "
            "host-specific deny rule must be placed ABOVE the subnet-wide permit "
            "rule; as written, rule 1 shadows rule 2 and the goal is not achieved."
        ),
    },
    {
        "id": "tfw-006",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A stateful firewall's outbound ACL permits TCP/443 from internal hosts "
            "to any destination. An analyst notices that return traffic from an "
            "external web server (source port 443, destined back to the internal "
            "client's ephemeral port) is allowed through even though no explicit "
            "inbound rule permits traffic sourced from TCP/443. Why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The firewall is stateful and automatically permits return "
                    "traffic that belongs to an already-established, tracked "
                    "outbound connection"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Stateful firewalls maintain a connection state table "
                    "and automatically allow return traffic matching an existing, "
                    "internally initiated session, without requiring a separate "
                    "inbound permit rule for the reply."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The firewall is stateless and evaluates each packet solely "
                    "against static header fields, coincidentally matching an "
                    "existing permit rule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stateless firewall would require an explicit "
                    "inbound rule permitting source port 443 traffic; the scenario "
                    "describes automatic handling of return traffic, which is the "
                    "defining behavior of a stateful firewall, not a stateless one."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The traffic is passing through a proxy ARP entry that "
                    "reclassifies it as internal and therefore always trusted"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Proxy ARP resolves Layer 2 address queries on "
                    "behalf of another host; it has no role in a Layer 3/4 firewall "
                    "ACL decision about permitting return traffic."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The implicit deny only applies to inbound traffic, so all "
                    "outbound-initiated replies bypass firewall evaluation "
                    "entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Implicit deny applies to any unmatched traffic in "
                    "either direction; the reply traffic isn't bypassing "
                    "evaluation, it is being explicitly matched and permitted "
                    "because of state tracking, not direction-based exemption."
                ),
            },
        ],
        "explanation": (
            "Stateful inspection is what distinguishes a stateful firewall from a "
            "simple stateless packet filter: it tracks the state of each "
            "connection and automatically permits legitimate return traffic "
            "without a matching inbound rule."
        ),
    },
    {
        "id": "tfw-007",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "An organization places its public-facing web server, mail relay, and "
            "DNS resolver in a screened subnet separated from both the internet and "
            "the internal LAN by two firewalls, so that a compromise of one of "
            "these servers does not directly expose internal workstations. What is "
            "this segment called?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A demilitarized zone (DMZ) / screened subnet",
                "correct": True,
                "rationale": (
                    "Correct. A DMZ (screened subnet) is a buffer network that "
                    "hosts internet-facing services, isolated from the internal LAN "
                    "by firewall boundaries so a compromised public server cannot "
                    "directly reach internal hosts."
                ),
            },
            {
                "id": "b",
                "text": "A management VLAN reachable only through a jump server",
                "correct": False,
                "rationale": (
                    "Incorrect. A management VLAN is used to isolate administrative "
                    "access to infrastructure devices, not to host public-facing "
                    "services like a web server or mail relay for internet users."
                ),
            },
            {
                "id": "c",
                "text": "An extranet shared with a trusted business partner",
                "correct": False,
                "rationale": (
                    "Incorrect. An extranet provides limited external-partner "
                    "access to specific internal resources; it does not describe a "
                    "buffer segment for the organization's own internet-facing "
                    "servers."
                ),
            },
            {
                "id": "d",
                "text": "A guest network isolated for visitor Wi-Fi access",
                "correct": False,
                "rationale": (
                    "Incorrect. A guest network isolates untrusted visitor devices "
                    "from the corporate LAN; it is unrelated to hosting the "
                    "organization's own public-facing servers between two "
                    "firewalls."
                ),
            },
        ],
        "explanation": (
            "The screened subnet (DMZ) pattern, bounded by firewalls on both "
            "sides, is the standard architecture for exposing public-facing "
            "services while protecting the internal network from a compromise of "
            "those services."
        ),
    },
    {
        "id": "tfw-008",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A three-legged firewall has interfaces for the internal LAN, a DMZ "
            "hosting a public web server, and the internet. Which rule set BEST "
            "reflects least-privilege placement of that web server?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Permit internet -> DMZ on TCP/443 only; permit DMZ -> internal "
                    "database server on the specific DB port only; deny DMZ -> "
                    "internal LAN for everything else; deny internet -> internal LAN "
                    "entirely"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This grants only the traffic each zone actually "
                    "needs: the public gets HTTPS to the DMZ only, the DMZ server "
                    "gets only the specific database port it requires, and the "
                    "internet never reaches the internal LAN directly — least "
                    "privilege in both direction and scope."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Permit internet -> DMZ on all ports; permit DMZ -> internal "
                    "LAN on all ports, to simplify troubleshooting"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Opening all ports from the internet to the DMZ and "
                    "from the DMZ to the internal LAN defeats the purpose of "
                    "segmentation and gives an attacker who compromises the web "
                    "server unrestricted reach into the internal network."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Permit internal LAN -> DMZ on all ports so administrators can "
                    "manage the server freely; deny all internet access to the DMZ"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Denying internet access to the DMZ web server "
                    "defeats its purpose of being publicly reachable, and granting "
                    "all ports from the internal LAN to the DMZ is broader access "
                    "than administrative management requires."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Permit internet -> internal LAN directly on TCP/443, bypassing "
                    "the DMZ, so the web server has direct access to internal "
                    "resources"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Routing internet traffic directly to the internal "
                    "LAN eliminates the entire purpose of the DMZ as a buffer zone "
                    "and exposes internal hosts directly to untrusted traffic."
                ),
            },
        ],
        "explanation": (
            "Least-privilege DMZ design permits only the specific service ports "
            "each zone legitimately needs in each direction, and never allows the "
            "internet to reach the internal LAN directly."
        ),
    },
    {
        "id": "tfw-009",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "An ACL blocks outbound traffic on TCP/23, TCP/21, and UDP/69 at the "
            "network edge, while permitting TCP/22, TCP/443, and TCP/989/990. What "
            "is the security rationale for this specific set of blocked ports?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The blocked ports (Telnet, FTP, TFTP) correspond to legacy "
                    "protocols that transmit credentials and data in cleartext, "
                    "while the permitted ports correspond to their encrypted "
                    "replacements (SSH, HTTPS, FTPS)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Telnet (23), FTP (21), and TFTP (69) send "
                    "authentication and data in cleartext, while SSH (22), HTTPS "
                    "(443), and FTPS (989/990) provide encrypted equivalents — this "
                    "ACL enforces a policy of blocking cleartext protocols in favor "
                    "of encrypted ones."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The blocked ports are all associated with routing protocols "
                    "that should never cross the network edge"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Telnet, FTP, and TFTP are remote-access and file-"
                    "transfer protocols, not routing protocols; this mischaracterizes "
                    "what the blocked ports are actually used for."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The blocked ports are deprecated and no longer assigned by "
                    "IANA, so blocking them has no operational impact"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ports 21, 23, and 69 remain officially assigned "
                    "and are still used by legacy systems in many environments; "
                    "they are blocked for security reasons (cleartext transmission), "
                    "not because they are unassigned."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The blocked ports are only used by peer-to-peer file-sharing "
                    "applications that violate acceptable use policy"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Telnet, FTP, and TFTP are standard remote "
                    "administration and file-transfer protocols, not P2P "
                    "file-sharing applications; this mischaracterizes their purpose."
                ),
            },
        ],
        "explanation": (
            "This ACL pattern reflects a common hardening practice: blocking "
            "legacy cleartext protocols (Telnet, FTP, TFTP) while permitting their "
            "encrypted counterparts (SSH, HTTPS, FTPS) to prevent credentials and "
            "data from crossing the network in the clear."
        ),
    },
    {
        "id": "tfw-010",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall administrator reviews an inbound ACL applied to the WAN "
            "interface and an outbound ACL applied to the same interface. A "
            "marketing employee reports being unable to upload files to an "
            "approved external SFTP server, even though the inbound ACL fully "
            "permits TCP/22 from that server's IP. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The outbound ACL does not permit TCP/22 traffic leaving the "
                    "network toward that destination, so the connection is blocked "
                    "before the inbound rule is ever relevant"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The employee's client initiates the SFTP session, so "
                    "the traffic is outbound first; if the outbound ACL doesn't "
                    "permit TCP/22 to that destination, the session never leaves "
                    "the network, regardless of how permissive the inbound ACL is."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The inbound ACL's permit rule for TCP/22 is being shadowed by "
                    "an earlier, broader deny rule on the same interface"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The question states the inbound ACL fully permits "
                    "this traffic, and inbound rules govern return traffic from the "
                    "server, not the employee's outbound-initiated request that is "
                    "failing here."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SFTP requires UDP/22 rather than TCP/22, and the ACL only "
                    "permits the TCP protocol"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SFTP (SSH File Transfer Protocol) runs over SSH, "
                    "which uses TCP/22, not UDP/22; this option describes an "
                    "inaccurate protocol requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The DMZ's screened subnet rules are blocking traffic between "
                    "two internal LAN endpoints"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario involves an internal employee "
                    "reaching an external SFTP server across the WAN interface, "
                    "not communication between two internal LAN endpoints governed "
                    "by DMZ rules."
                ),
            },
        ],
        "explanation": (
            "Inbound and outbound ACLs are evaluated independently for their "
            "respective direction of traffic; a fully permissive inbound rule "
            "does not help if the outbound ACL blocks the employee's "
            "connection-initiating traffic in the first place."
        ),
    },
    # ------------------------------------------------------------------ #
    # 11-20: WAF vs firewall vs IDS vs IPS vs TLS identification
    # ------------------------------------------------------------------ #
    {
        "id": "tfw-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A security architect needs a control that inspects HTTP request "
            "bodies and parameters to detect and block SQL injection and "
            "cross-site scripting payloads targeting a public order-entry form, "
            "without requiring changes to the application's code. Which control "
            "BEST fits?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Web application firewall (WAF)",
                "correct": True,
                "rationale": (
                    "Correct. A WAF inspects application-layer HTTP content — "
                    "including request bodies and parameters — against rule sets "
                    "designed to detect and block injection and XSS payloads, "
                    "without modifying the application itself."
                ),
            },
            {
                "id": "b",
                "text": "Stateful network firewall filtering by IP, port, and protocol",
                "correct": False,
                "rationale": (
                    "Incorrect. A standard stateful firewall filters based on "
                    "Layer 3/4 header information and cannot parse or inspect "
                    "HTTP request bodies for injection or XSS payloads."
                ),
            },
            {
                "id": "c",
                "text": "Passive network intrusion detection system (NIDS)",
                "correct": False,
                "rationale": (
                    "Incorrect. A passive NIDS can alert on suspicious patterns "
                    "in a copy of traffic, but it does not block traffic inline; "
                    "the requirement here is to actively block the malicious "
                    "requests, not just detect and alert."
                ),
            },
            {
                "id": "d",
                "text": "TLS termination at the load balancer",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS termination decrypts traffic in transit for "
                    "downstream processing but performs no content inspection or "
                    "filtering of the decrypted payload for attack patterns."
                ),
            },
        ],
        "explanation": (
            "Blocking application-layer web attacks such as SQL injection and XSS "
            "in HTTP request content is the defining purpose of a WAF, distinct "
            "from network-layer firewalls, passive detection systems, and "
            "encryption-in-transit mechanisms."
        ),
    },
    {
        "id": "tfw-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A security operations center wants a device deployed inline on the "
            "network path that will automatically and immediately drop packets "
            "matching a known exploit signature, without waiting for an analyst to "
            "review an alert. Which control satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Intrusion prevention system (IPS)",
                "correct": True,
                "rationale": (
                    "Correct. An IPS is deployed inline and actively blocks "
                    "traffic matching malicious signatures or behavior in real "
                    "time, with no analyst intervention required — unlike a "
                    "detection-only system."
                ),
            },
            {
                "id": "b",
                "text": "Intrusion detection system (IDS) in passive/tap mode",
                "correct": False,
                "rationale": (
                    "Incorrect. A passive IDS only alerts on suspicious traffic "
                    "using a copy of the traffic stream; it has no ability to drop "
                    "packets inline because it is not in the traffic's actual path."
                ),
            },
            {
                "id": "c",
                "text": "Stateless packet-filtering firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. A stateless firewall filters based on static "
                    "header rules (IP, port, protocol) rather than recognizing "
                    "exploit signatures or behavioral attack patterns."
                ),
            },
            {
                "id": "d",
                "text": "TLS inspection proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A TLS inspection proxy decrypts traffic so it can "
                    "be examined by other security tools; by itself it does not "
                    "perform signature-based detection and automatic blocking of "
                    "exploit traffic."
                ),
            },
        ],
        "explanation": (
            "Automatic, real-time blocking of traffic matching malicious "
            "signatures is the defining capability of an inline IPS, as opposed "
            "to passive detection (IDS), generic packet filtering (firewall), or "
            "decryption (TLS proxy)."
        ),
    },
    {
        "id": "tfw-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "An e-commerce site needs to ensure that credit card numbers entered "
            "into its checkout form cannot be read by an attacker performing a "
            "man-in-the-middle attack while the data travels from the customer's "
            "browser to the web server. Which control directly addresses this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TLS encrypting the HTTPS session between browser and server",
                "correct": True,
                "rationale": (
                    "Correct. TLS provides confidentiality and integrity for data "
                    "in transit between the browser and server, which is exactly "
                    "what prevents an on-path attacker from reading the "
                    "credit card data as it travels across the network."
                ),
            },
            {
                "id": "b",
                "text": "A web application firewall inspecting form submissions for malicious payloads",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF blocks malicious request content like "
                    "injection attacks; it does not provide encryption of data in "
                    "transit and does not stop an eavesdropper from reading "
                    "cleartext traffic."
                ),
            },
            {
                "id": "c",
                "text": "A stateful firewall permitting only TCP/443 traffic to the web server",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting traffic to port 443 controls which "
                    "port is reachable but does not itself provide encryption — "
                    "traffic to port 443 could still be unencrypted HTTP if TLS "
                    "isn't actually configured."
                ),
            },
            {
                "id": "d",
                "text": "An intrusion prevention system blocking known attack signatures",
                "correct": False,
                "rationale": (
                    "Incorrect. An IPS blocks recognized malicious traffic "
                    "patterns; it has no function related to encrypting data in "
                    "transit against passive or active eavesdropping."
                ),
            },
        ],
        "explanation": (
            "Confidentiality of data in transit against a man-in-the-middle "
            "attack is provided by encryption — TLS — not by firewalls, WAFs, or "
            "IPS devices, which serve access-control and detection/blocking "
            "purposes rather than encryption."
        ),
    },
    {
        "id": "tfw-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A retail company's network engineer wants a single control that "
            "restricts which external hosts may establish connections to the "
            "internal network based on IP address, destination port, and "
            "protocol, without any awareness of application-layer content. Which "
            "control BEST matches this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A traditional network firewall enforcing an ACL",
                "correct": True,
                "rationale": (
                    "Correct. Filtering connections based on IP address, port, and "
                    "protocol — without inspecting application-layer content — is "
                    "the core function of a traditional (Layer 3/4) firewall "
                    "enforcing access control lists."
                ),
            },
            {
                "id": "b",
                "text": "A web application firewall (WAF)",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF is specifically built for deep application-"
                    "layer content inspection of HTTP traffic, which exceeds — and "
                    "is a different function from — the simple IP/port/protocol "
                    "filtering requested here."
                ),
            },
            {
                "id": "c",
                "text": "An intrusion prevention system using behavioral heuristics",
                "correct": False,
                "rationale": (
                    "Incorrect. An IPS analyzes traffic behavior and signatures to "
                    "detect attacks, which is a form of content awareness — the "
                    "requirement explicitly calls for a control with no "
                    "application-layer awareness."
                ),
            },
            {
                "id": "d",
                "text": "A TLS-terminating reverse proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A TLS-terminating reverse proxy decrypts and "
                    "forwards application traffic, which requires application-"
                    "layer awareness and is unrelated to basic IP/port/protocol "
                    "access control."
                ),
            },
        ],
        "explanation": (
            "Filtering purely on IP address, port, and protocol without content "
            "awareness is the classic definition of a network (Layer 3/4) "
            "firewall, distinguishing it from WAFs, IPS, and proxies that "
            "operate with application-layer visibility."
        ),
    },
    {
        "id": "tfw-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A SOC analyst reviews an alert generated by a network sensor that "
            "flagged a suspicious payload but took no action to stop it — the "
            "traffic reached its destination normally. Which type of device MOST "
            "likely generated this alert?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An intrusion detection system (IDS) operating in passive mode",
                "correct": True,
                "rationale": (
                    "Correct. An IDS monitors a copy of traffic and generates "
                    "alerts for review, but it does not sit inline and cannot "
                    "block traffic — matching the described behavior of "
                    "detection without prevention."
                ),
            },
            {
                "id": "b",
                "text": "An intrusion prevention system (IPS) operating inline",
                "correct": False,
                "rationale": (
                    "Incorrect. An inline IPS is positioned to actively block "
                    "matching traffic in real time; if the traffic reached its "
                    "destination unimpeded, the device did not behave as an IPS "
                    "would."
                ),
            },
            {
                "id": "c",
                "text": "A firewall enforcing a deny rule",
                "correct": False,
                "rationale": (
                    "Incorrect. A firewall deny rule drops matching traffic before "
                    "it reaches its destination; this scenario describes traffic "
                    "that was allowed through despite the alert."
                ),
            },
            {
                "id": "d",
                "text": "A web application firewall (WAF) in blocking mode",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF in blocking mode actively stops matching "
                    "requests from reaching the application; the traffic here "
                    "reached its destination, which is inconsistent with active "
                    "blocking mode."
                ),
            },
        ],
        "explanation": (
            "Alerting without blocking is the defining, detection-only behavior "
            "of an IDS (or a WAF/IPS explicitly running in monitor-only mode); "
            "any device actively enforcing traffic would have stopped the "
            "payload from reaching its destination."
        ),
    },
    {
        "id": "tfw-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A company's public API is protected by a stateful firewall that "
            "permits only TCP/443 from any source. Attackers begin sending "
            "crafted JSON payloads over that permitted HTTPS connection that "
            "exploit an insecure deserialization flaw in the API code. Which "
            "statement BEST explains why the firewall does not stop this attack, "
            "and what control would?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The firewall only evaluates IP, port, and protocol, so a "
                    "malicious payload inside an otherwise-permitted TCP/443 "
                    "session passes through unnoticed; a WAF with application-layer "
                    "inspection is needed to detect and block it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A traditional firewall has no visibility into "
                    "encrypted or application-layer payload content — it only "
                    "confirms the connection is permitted at the network/transport "
                    "layer. A WAF (or a decrypting proxy feeding one) is needed to "
                    "inspect and block malicious content within the allowed "
                    "session."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The firewall's implicit deny rule is misconfigured and should "
                    "be changed to explicitly deny TCP/443 traffic entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking all TCP/443 traffic would take the public "
                    "API offline entirely, which is a far more disruptive and "
                    "imprecise response than adding application-layer inspection "
                    "for the specific malicious payloads."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The firewall failed to fail closed, and switching its failure "
                    "mode from fail-open to fail-closed would have stopped the "
                    "malicious payloads"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Failure mode governs what happens if the device "
                    "itself stops functioning; it has no bearing on how a "
                    "functioning firewall evaluates permitted traffic that "
                    "contains a malicious application-layer payload."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The firewall's ACL rule order is reversed, causing the "
                    "malicious traffic to match a permit rule before reaching a "
                    "deny rule further down the list"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This scenario is not a rule-ordering problem — "
                    "there is no ACL rule anywhere capable of recognizing "
                    "malicious JSON payload content in the first place, regardless "
                    "of order, because the firewall lacks application-layer "
                    "visibility."
                ),
            },
        ],
        "explanation": (
            "Traditional firewalls filter at Layer 3/4 and have no visibility "
            "into payload content within a permitted session; stopping "
            "application-layer attacks like insecure deserialization requires a "
            "control with deep packet/content inspection, such as a WAF."
        ),
    },
    {
        "id": "tfw-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A company wants remote branch offices to establish an encrypted, "
            "authenticated site-to-site tunnel over the public internet to reach "
            "resources at headquarters, such that all traffic between the sites is "
            "confidential and protected from tampering. Which control provides "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An IPSec VPN tunnel between the branch and headquarters gateways",
                "correct": True,
                "rationale": (
                    "Correct. IPSec provides authenticated, encrypted site-to-site "
                    "tunnels across an untrusted network like the internet, "
                    "delivering confidentiality and integrity for all traffic "
                    "between the two sites."
                ),
            },
            {
                "id": "b",
                "text": "A stateful firewall permitting only the branch office's public IP",
                "correct": False,
                "rationale": (
                    "Incorrect. IP-based firewall permit rules control which "
                    "source addresses may connect but provide no encryption or "
                    "integrity protection for the traffic itself."
                ),
            },
            {
                "id": "c",
                "text": "A web application firewall placed in front of the headquarters resources",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF inspects HTTP(S) application traffic for "
                    "web-specific attacks; it does not establish or encrypt a "
                    "site-to-site network tunnel."
                ),
            },
            {
                "id": "d",
                "text": "An IDS monitoring traffic between the two sites for anomalies",
                "correct": False,
                "rationale": (
                    "Incorrect. An IDS detects and alerts on suspicious traffic "
                    "patterns; it provides no encryption or confidentiality for "
                    "data crossing the internet between sites."
                ),
            },
        ],
        "explanation": (
            "Site-to-site confidentiality and integrity across an untrusted "
            "network is the purpose of an IPSec VPN tunnel, not firewall ACLs, "
            "WAFs, or IDS, which serve access-control and detection functions "
            "rather than encryption."
        ),
    },
    {
        "id": "tfw-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A financial services firm needs to (1) restrict which ports and "
            "protocols may cross its network perimeter, and separately (2) detect "
            "and alert on statistically anomalous outbound data volumes that could "
            "indicate exfiltration, without blocking any traffic automatically "
            "because false positives previously disrupted business operations. "
            "Which pairing of controls matches these two distinct needs?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A firewall to enforce the port/protocol ACL, and a passive "
                    "IDS to detect and alert on the anomalous traffic without "
                    "blocking it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A firewall is the right tool for enforcing which "
                    "ports/protocols may cross the perimeter, while a passive IDS "
                    "detects and alerts on anomalies without the automatic-"
                    "blocking risk of an inline IPS, matching the requirement to "
                    "avoid further false-positive disruption."
                ),
            },
            {
                "id": "b",
                "text": (
                    "An inline IPS to enforce the port/protocol ACL, and a WAF to "
                    "detect the anomalous traffic without blocking it"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An IPS actively blocks matching traffic inline, "
                    "risking the same false-positive disruption the firm wants to "
                    "avoid, and a WAF inspects web application content rather than "
                    "overall traffic volume anomalies."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A WAF to enforce the port/protocol ACL, and a firewall to "
                    "detect the anomalous traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF filters application-layer HTTP content, not "
                    "general port/protocol access; and a standard firewall "
                    "enforces access rules rather than detecting statistical "
                    "traffic anomalies."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A single inline IPS configured to both enforce the ACL and "
                    "alert on anomalies, since one appliance can fully replace "
                    "both needs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Using an inline IPS for both functions "
                    "reintroduces automatic blocking behavior for the anomaly "
                    "detection use case, directly conflicting with the requirement "
                    "not to block traffic automatically after prior disruption."
                ),
            },
        ],
        "explanation": (
            "Each control has a distinct role: firewalls enforce port/protocol "
            "access rules, while a passive (non-blocking) IDS is the appropriate "
            "choice when detection and alerting are required without the risk of "
            "an inline device automatically blocking legitimate traffic."
        ),
    },
    {
        "id": "tfw-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A company's NGFW blocks outbound TCP/25 (SMTP) from all hosts except "
            "the approved mail relay, and separately, a WAF blocks malicious "
            "requests to the public web application. During an incident, an "
            "attacker who compromised a workstation is found exfiltrating data by "
            "encoding it within DNS queries (TCP/UDP 53) to an external "
            "attacker-controlled domain, since DNS is permitted outbound by "
            "default. Which statement BEST explains why neither existing control "
            "stopped this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The SMTP restriction and the WAF each address a narrow, "
                    "different traffic type (mail relay abuse and web application "
                    "attacks); neither inspects DNS query content, so DNS "
                    "tunneling exfiltration falls outside both controls' scope"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The SMTP rule only restricts email traffic and the "
                    "WAF only inspects HTTP(S) web requests — neither is designed "
                    "to analyze DNS query content, so DNS-based exfiltration "
                    "bypasses both, illustrating the need for DNS-specific "
                    "filtering or monitoring (e.g., a secure DNS resolver or "
                    "dedicated DNS security tool)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The WAF should have been placed inline on all outbound "
                    "traffic instead of only in front of the web application to "
                    "catch this"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF is designed to inspect HTTP(S) web traffic "
                    "specifically; even placed elsewhere, it does not analyze DNS "
                    "protocol content, so relocating it would not address DNS "
                    "tunneling."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The NGFW's implicit deny rule failed to trigger because SMTP "
                    "traffic was involved"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The exfiltration occurred over DNS, not SMTP; the "
                    "implicit deny is unrelated to this traffic and the SMTP "
                    "restriction functioned correctly for its own protocol."
                ),
            },
            {
                "id": "d",
                "text": (
                    "TLS encryption on the DNS queries prevented both controls "
                    "from inspecting the exfiltrated content"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario does not indicate encrypted DNS was "
                    "used, and even unencrypted DNS tunneling would bypass both "
                    "controls because neither is built to inspect DNS query "
                    "content in the first place."
                ),
            },
        ],
        "explanation": (
            "Security controls are typically scoped to specific traffic types; "
            "an SMTP restriction and a WAF have no visibility into DNS protocol "
            "content, so an attacker abusing DNS for tunneling/exfiltration will "
            "not be caught by either, highlighting the importance of matching "
            "controls to the actual traffic being abused."
        ),
    },
    {
        "id": "tfw-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A security team needs to encrypt individual client-to-server "
            "database connections (rather than a whole network tunnel) so that "
            "credentials and query results are protected from network "
            "eavesdropping between an application server and its database. Which "
            "control is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TLS enabled on the database connection itself",
                "correct": True,
                "rationale": (
                    "Correct. Enabling TLS directly on the database connection "
                    "encrypts the specific client-to-server session, protecting "
                    "credentials and query data from network eavesdropping without "
                    "requiring a broader network tunnel."
                ),
            },
            {
                "id": "b",
                "text": "A site-to-site IPSec VPN between the two data centers",
                "correct": False,
                "rationale": (
                    "Incorrect. A site-to-site VPN encrypts traffic between two "
                    "network segments broadly; it is a heavier-weight solution "
                    "than needed when only a specific application-to-database "
                    "connection must be encrypted, and may not even apply if both "
                    "servers are in the same data center."
                ),
            },
            {
                "id": "c",
                "text": "A firewall rule restricting database access to the application server's IP",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting source IPs controls who may connect "
                    "but does not encrypt the data exchanged during that "
                    "connection, leaving credentials and query results readable "
                    "to anyone who can observe the traffic."
                ),
            },
            {
                "id": "d",
                "text": "An IDS monitoring the database server's network segment",
                "correct": False,
                "rationale": (
                    "Incorrect. An IDS can detect suspicious database access "
                    "patterns but provides no encryption of the traffic itself, "
                    "so eavesdropping on cleartext credentials would remain "
                    "possible."
                ),
            },
        ],
        "explanation": (
            "TLS applied directly to the database connection is the appropriate, "
            "targeted control for encrypting a specific application-to-database "
            "session, as opposed to broader network tunnels, access-restricting "
            "firewall rules, or detection-only monitoring."
        ),
    },
    # ------------------------------------------------------------------ #
    # 21-30: Network appliances / additional firewall scenarios
    # ------------------------------------------------------------------ #
    {
        "id": "tfw-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company wants internal clients' outbound web requests to be "
            "cached, content-filtered, and have their source IP hidden from "
            "external destinations before leaving the network. Which appliance "
            "BEST fulfills this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forward proxy server",
                "correct": True,
                "rationale": (
                    "Correct. A forward proxy sits between internal clients and "
                    "the internet, caching content, enforcing content filtering "
                    "policy, and masking the originating client's IP address from "
                    "external destinations — exactly the described requirements."
                ),
            },
            {
                "id": "b",
                "text": "Reverse proxy server",
                "correct": False,
                "rationale": (
                    "Incorrect. A reverse proxy sits in front of internal servers "
                    "to handle traffic coming from external clients; it does not "
                    "manage internal clients' outbound requests to the internet."
                ),
            },
            {
                "id": "c",
                "text": "Load balancer",
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes incoming requests "
                    "across multiple backend servers; it does not cache or "
                    "content-filter internal clients' outbound web traffic."
                ),
            },
            {
                "id": "d",
                "text": "VPN concentrator",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN concentrator terminates encrypted remote-"
                    "access tunnels; it does not provide caching, content "
                    "filtering, or IP masking for outbound web browsing."
                ),
            },
        ],
        "explanation": (
            "A forward proxy is purpose-built to sit between internal clients and "
            "external destinations, providing caching, content filtering, and "
            "source IP masking for outbound traffic."
        ),
    },
    {
        "id": "tfw-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A web farm behind a single public IP address needs incoming HTTPS "
            "requests distributed across several backend servers based on current "
            "server load, with unhealthy servers automatically removed from "
            "rotation. Which appliance is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Load balancer",
                "correct": True,
                "rationale": (
                    "Correct. A load balancer is purpose-built to distribute "
                    "incoming requests across multiple backend servers using a "
                    "chosen algorithm and to perform health checks that remove "
                    "unhealthy servers from rotation."
                ),
            },
            {
                "id": "b",
                "text": "Forward proxy server",
                "correct": False,
                "rationale": (
                    "Incorrect. A forward proxy manages outbound requests from "
                    "internal clients to external destinations, not inbound "
                    "distribution of requests across a farm of backend servers."
                ),
            },
            {
                "id": "c",
                "text": "Intrusion prevention system (IPS)",
                "correct": False,
                "rationale": (
                    "Incorrect. An IPS detects and blocks malicious traffic "
                    "patterns; it has no built-in capability to distribute load "
                    "or perform backend server health checks."
                ),
            },
            {
                "id": "d",
                "text": "Jump server (bastion host)",
                "correct": False,
                "rationale": (
                    "Incorrect. A jump server is an administrative access "
                    "chokepoint for management sessions; it is unrelated to "
                    "distributing production HTTPS traffic across web servers."
                ),
            },
        ],
        "explanation": (
            "Distributing traffic across multiple backend servers with health-"
            "based failover is the defining function of a load balancer, "
            "distinct from proxies, IPS devices, or bastion hosts."
        ),
    },
    {
        "id": "tfw-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network appliances",
        "stem": (
            "A company wants to publish an internal web application to external "
            "users without exposing the application server's real IP address or "
            "internal network topology, while also terminating TLS and applying "
            "URL-based routing to different backend services. Which appliance "
            "BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reverse proxy",
                "correct": True,
                "rationale": (
                    "Correct. A reverse proxy sits in front of internal servers, "
                    "accepting external requests on their behalf, hiding backend "
                    "topology and IPs, and can terminate TLS and route by URL to "
                    "different backend services."
                ),
            },
            {
                "id": "b",
                "text": "Forward proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A forward proxy manages outbound traffic from "
                    "internal clients to external destinations, which is the "
                    "opposite direction from publishing an internal service to "
                    "external users."
                ),
            },
            {
                "id": "c",
                "text": "VPN concentrator",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN concentrator provides authenticated, "
                    "encrypted remote-access tunnels for specific users; it is not "
                    "designed for publicly routing and load-distributing general "
                    "web traffic by URL."
                ),
            },
            {
                "id": "d",
                "text": "Jump server (bastion host)",
                "correct": False,
                "rationale": (
                    "Incorrect. A jump server brokers administrative shell/RDP "
                    "sessions for IT staff; it does not terminate TLS or route "
                    "public web application traffic by URL."
                ),
            },
        ],
        "explanation": (
            "Publishing internal services to external users while hiding backend "
            "topology, terminating TLS, and routing by URL is the classic use "
            "case for a reverse proxy, distinct from forward proxies, VPN "
            "concentrators, or bastion hosts."
        ),
    },
    {
        "id": "tfw-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A security team wants a single appliance combining firewall, IPS, "
            "antivirus, and content filtering to reduce hardware footprint and "
            "management overhead at a small branch office with limited IT staff. "
            "Which appliance category matches this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unified threat management (UTM) appliance",
                "correct": True,
                "rationale": (
                    "Correct. A UTM appliance is specifically designed to "
                    "consolidate multiple security functions — firewall, IPS, "
                    "antivirus, and content filtering — into a single device, "
                    "reducing hardware and management overhead."
                ),
            },
            {
                "id": "b",
                "text": "Standalone Layer 2 switch with port security enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. A Layer 2 switch with port security controls "
                    "which devices may connect to physical ports; it provides "
                    "none of the firewall, IPS, antivirus, or content-filtering "
                    "functions requested."
                ),
            },
            {
                "id": "c",
                "text": "Dedicated hardware security module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. An HSM is a specialized device for secure "
                    "cryptographic key storage and operations; it has no firewall, "
                    "IPS, antivirus, or content-filtering functionality."
                ),
            },
            {
                "id": "d",
                "text": "VPN concentrator with split-tunnel support",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN concentrator terminates remote-access "
                    "tunnels; it does not provide antivirus scanning or content "
                    "filtering, and consolidating those functions is not its "
                    "purpose."
                ),
            },
        ],
        "explanation": (
            "UTM appliances exist specifically to bundle multiple security "
            "functions into one device for environments — like small branch "
            "offices — where minimizing hardware and management complexity is a "
            "priority."
        ),
    },
    {
        "id": "tfw-025",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A vulnerability scan of an internet-facing firewall's management "
            "interface finds that HTTPS administration is reachable from any "
            "public IP address on TCP/443, using the same port as the protected "
            "web application behind it. Which change BEST reduces the attack "
            "surface of the management interface specifically?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restrict management access to a dedicated management "
                    "interface/VLAN reachable only from specific internal "
                    "administrator IP ranges, separate from the public-facing "
                    "application port"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Moving administrative access to a separate, "
                    "restricted management path reachable only by authorized "
                    "internal sources directly eliminates public exposure of the "
                    "management interface, which is the specific attack surface "
                    "issue described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Enable additional logging on the management interface so "
                    "unauthorized access attempts are recorded for later review"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Logging improves detection and forensic capability "
                    "after the fact, but it does not reduce the exposure itself — "
                    "the interface remains reachable from any public IP."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy a WAF in front of the firewall's management interface "
                    "to filter malicious HTTPS requests"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding another layer of filtering leaves the "
                    "management interface publicly reachable and adds complexity, "
                    "rather than removing the unnecessary public exposure "
                    "entirely."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Require a longer, more complex administrator password for "
                    "the management interface"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stronger password improves authentication "
                    "strength but does nothing to reduce the fact that the "
                    "interface itself remains reachable from the entire public "
                    "internet."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means eliminating unnecessary exposure "
            "itself — restricting the management interface to a dedicated, "
            "access-controlled path — rather than merely adding monitoring, "
            "filtering, or authentication in front of an interface that remains "
            "publicly reachable."
        ),
    },
    {
        "id": "tfw-026",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "A network switch port in an unmonitored lobby area needs to stop "
            "operating if more than one MAC address is observed on it, since only "
            "a single approved kiosk device should ever be connected there. Which "
            "control BEST enforces this at the switch port itself?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Port security with a maximum MAC address count of one and a violation action of shutdown",
                "correct": True,
                "rationale": (
                    "Correct. Port security lets an administrator cap the number "
                    "of learned MAC addresses on a port and define a violation "
                    "action (such as shutting the port down) when that limit is "
                    "exceeded — precisely matching the single-device requirement."
                ),
            },
            {
                "id": "b",
                "text": "802.1X port-based authentication using EAP-TLS certificates",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X authenticates devices/users before granting "
                    "access, but by itself it does not limit or count how many MAC "
                    "addresses may be active on a single port; that is the "
                    "specific function of port security."
                ),
            },
            {
                "id": "c",
                "text": "A firewall ACL denying traffic from unrecognized source IP addresses",
                "correct": False,
                "rationale": (
                    "Incorrect. A firewall ACL operates at Layer 3 on IP "
                    "addresses and is typically enforced elsewhere in the network, "
                    "not as a Layer 2 control limiting how many MAC addresses "
                    "connect to a specific switch port."
                ),
            },
            {
                "id": "d",
                "text": "VLAN trunking configured on the port to segment kiosk traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN trunking carries traffic for multiple VLANs "
                    "over one link; it does not limit or count the number of MAC "
                    "addresses connected to the port."
                ),
            },
        ],
        "explanation": (
            "Port security's MAC address limiting and violation actions are the "
            "specific switch-port control for restricting how many (and which) "
            "devices may connect to a given port, distinct from 802.1X "
            "authentication, Layer 3 ACLs, or VLAN trunking."
        ),
    },
    {
        "id": "tfw-027",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A firewall administrator wants to apply consistent security group "
            "rules to virtual workloads based on tags such as \"web-tier\" or "
            "\"db-tier\" that automatically follow the workload if it migrates to "
            "a different physical host or subnet, rather than being tied to a "
            "static IP address or VLAN. Which approach enables this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Software-defined networking (SDN) with policy enforced "
                    "through logical/tag-based security groups rather than "
                    "physical topology"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SDN decouples policy from physical network location, "
                    "allowing security groups defined by workload tags/identity to "
                    "automatically follow a workload as it moves, rather than "
                    "being bound to a static IP or VLAN."
                ),
            },
            {
                "id": "b",
                "text": "Traditional VLAN assignment based on the switch port a workload is physically connected to",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN assignment tied to a physical switch port is "
                    "exactly the static, topology-bound approach the requirement "
                    "explicitly wants to avoid — rules would not follow a migrated "
                    "workload automatically."
                ),
            },
            {
                "id": "c",
                "text": "Static ACLs referencing each workload's fixed IP address",
                "correct": False,
                "rationale": (
                    "Incorrect. IP-based static ACLs must be manually updated "
                    "whenever a workload's address changes; they do not "
                    "automatically follow a workload based on tags or identity."
                ),
            },
            {
                "id": "d",
                "text": "Physical air-gapping of the web tier and database tier onto separate hardware",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical air-gapping is a rigid, hardware-bound "
                    "isolation method that cannot dynamically follow workloads as "
                    "they migrate between hosts or subnets."
                ),
            },
        ],
        "explanation": (
            "SDN's separation of policy from physical topology allows tag- or "
            "identity-based security groups to travel with a workload, which "
            "static VLANs, IP-based ACLs, and physical segmentation cannot do."
        ),
    },
    {
        "id": "tfw-028",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "An organization's firewall administrator is asked to justify why an "
            "outbound rule permitting TCP/3389 (RDP) from the entire internal "
            "network to any external destination exists. No business need is "
            "found for outbound RDP to the internet. Which action reflects "
            "correct least-privilege firewall management?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove the overly broad rule; if RDP to specific external "
                    "destinations is later needed, add a narrowly scoped rule for "
                    "just those source hosts and destinations"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Least-privilege firewall management means removing "
                    "rules that grant broader access than any documented business "
                    "need requires, and adding new rules only as narrowly scoped "
                    "as an actual justified need demands."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Leave the rule in place but add logging so any use of it can "
                    "be reviewed after the fact"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Logging provides visibility but does not reduce "
                    "the unnecessary exposure itself; an unjustified broad "
                    "outbound rule remains a standing risk whether or not it is "
                    "logged."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Change the rule's action from permit to deny but leave the "
                    "source scope as the entire internal network for future "
                    "flexibility"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While denying is the right general direction, "
                    "the question asks about correct least-privilege management "
                    "of firewall rules overall — keeping an unnecessarily broad "
                    "scope \"for flexibility\" if the rule is ever re-enabled "
                    "runs counter to least privilege and to change management "
                    "discipline."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Convert the rule to apply only during business hours instead "
                    "of removing it"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Time-restricting the rule still leaves an "
                    "unjustified, overly broad outbound RDP permission active "
                    "during those hours, without addressing the underlying lack "
                    "of business need."
                ),
            },
        ],
        "explanation": (
            "Least-privilege firewall management requires removing rules that "
            "lack a documented business justification and replacing them, if "
            "ever needed, with the narrowest possible scope — not merely adding "
            "logging, time restrictions, or leaving broad scope intact."
        ),
    },
    {
        "id": "tfw-029",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall ACL protecting an internal file server is:\n"
            "1. PERMIT  TCP  10.0.6.0/24  10.0.9.5  445\n"
            "2. DENY    TCP  ANY          10.0.9.5  445\n"
            "3. PERMIT  TCP  10.0.6.50    10.0.9.5  445\n"
            "4. DENY    ANY  ANY          ANY  ANY  (implicit)\n"
            "A workstation at 10.0.6.50 (a member of 10.0.6.0/24) attempts an "
            "SMB (TCP/445) connection to the file server. What happens, and why "
            "was rule 3 written?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The connection is permitted by rule 1, since 10.0.6.50 is "
                    "already covered by the 10.0.6.0/24 subnet; rule 3 is "
                    "redundant and has no effect because it is never reached"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 10.0.6.50 falls within 10.0.6.0/24, so rule 1 "
                    "matches and permits the connection before evaluation ever "
                    "reaches rule 2 or rule 3. Rule 3 is a redundant, unreachable "
                    "rule that adds no functional value and should be flagged "
                    "during ACL review/cleanup."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The connection is denied by rule 2, because it specifically "
                    "blocks all TCP/445 traffic to 10.0.9.5 regardless of source"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule 1 is evaluated before rule 2 and already "
                    "matches this traffic (10.0.6.50 is part of 10.0.6.0/24), so "
                    "the connection is permitted before evaluation ever reaches "
                    "rule 2."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The connection is permitted specifically by rule 3, which "
                    "was necessary to override rule 2's blanket deny for this "
                    "single host"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule 3 is never reached for this traffic because "
                    "rule 1 already matches and permits it first; rule 3 is not "
                    "what actually grants access here, making it functionally "
                    "redundant."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The connection is denied by the implicit deny, because rules "
                    "1 and 3 conflict with each other and the firewall discards "
                    "the entire matching traffic flow"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. ACL evaluation does not discard traffic due to "
                    "later redundant or conflicting rules; it simply stops at the "
                    "first match, which is rule 1 in this case, permitting the "
                    "connection."
                ),
            },
        ],
        "explanation": (
            "Because ACL evaluation stops at the first match, a broad permit "
            "rule (rule 1) placed above a narrower permit rule (rule 3) for a "
            "host it already covers makes that narrower rule redundant and "
            "unreachable — a common finding during firewall rule-base cleanup."
        ),
    },
    {
        "id": "tfw-030",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A security engineer configures a new firewall to deny all traffic by "
            "default and then adds explicit permit rules only for traffic flows "
            "that have a documented business need, rather than starting with "
            "permit-all and adding deny rules for known-bad traffic. Which firewall "
            "design principle does this reflect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Least privilege / default-deny (allowlisting)",
                "correct": True,
                "rationale": (
                    "Correct. Starting from a default-deny posture and explicitly "
                    "permitting only justified traffic is the definition of "
                    "least-privilege, allowlist-based firewall design — it "
                    "minimizes exposure to any traffic that wasn't specifically "
                    "considered and approved."
                ),
            },
            {
                "id": "b",
                "text": "Fail-open availability design",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open/fail-closed describes what a device does "
                    "when it stops functioning, not the philosophy behind how its "
                    "normal rule base is structured."
                ),
            },
            {
                "id": "c",
                "text": "Blocklisting (denylisting) known-malicious traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. Blocklisting is the opposite approach described in "
                    "the question stem: starting from permit-all and adding deny "
                    "rules for known-bad traffic, rather than default-deny with "
                    "explicit permits."
                ),
            },
            {
                "id": "d",
                "text": "Separation of duties",
                "correct": False,
                "rationale": (
                    "Incorrect. Separation of duties concerns dividing "
                    "administrative responsibilities among multiple people so no "
                    "single person has excessive control; it does not describe how "
                    "a firewall rule base itself is structured."
                ),
            },
        ],
        "explanation": (
            "Default-deny with explicit, justified permit rules is the "
            "least-privilege (allowlist) approach to firewall design, contrasted "
            "with a permissive default paired with denylisting known threats."
        ),
    },
    # ------------------------------------------------------------------ #
    # 31-40: additional mixed scenarios across allowed topics
    # ------------------------------------------------------------------ #
    {
        "id": "tfw-031",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "An employee working from a coffee shop connects to the corporate "
            "network. Security policy requires that only traffic destined for "
            "corporate resources traverse the encrypted tunnel, while the "
            "employee's general internet browsing exits directly through the "
            "local Wi-Fi to preserve corporate bandwidth. Which VPN configuration "
            "matches this policy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Split tunnel VPN",
                "correct": True,
                "rationale": (
                    "Correct. A split tunnel routes only corporate-destined "
                    "traffic through the encrypted VPN tunnel while general "
                    "internet traffic exits locally, preserving corporate "
                    "bandwidth — exactly matching the described policy."
                ),
            },
            {
                "id": "b",
                "text": "Full tunnel VPN",
                "correct": False,
                "rationale": (
                    "Incorrect. A full tunnel routes ALL of the employee's "
                    "traffic, including general internet browsing, through the "
                    "corporate network, which is the opposite of what this policy "
                    "requires."
                ),
            },
            {
                "id": "c",
                "text": "Site-to-site IPSec tunnel",
                "correct": False,
                "rationale": (
                    "Incorrect. Site-to-site tunnels connect two networks (such "
                    "as branch offices) to each other, not an individual remote "
                    "user's laptop to the corporate network."
                ),
            },
            {
                "id": "d",
                "text": "Clientless SSL VPN portal",
                "correct": False,
                "rationale": (
                    "Incorrect. A clientless portal provides browser-based access "
                    "to specific internal web applications rather than the "
                    "selective full-traffic routing behavior (split tunneling) "
                    "described in the policy."
                ),
            },
        ],
        "explanation": (
            "Split tunneling is the VPN configuration that sends only "
            "corporate-destined traffic through the tunnel while letting general "
            "internet traffic exit locally, trading some inspection visibility "
            "for reduced corporate bandwidth and latency."
        ),
    },
    {
        "id": "tfw-032",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall administrator writes a new rule permitting inbound "
            "TCP/3306 (MySQL) from the internet directly to a production database "
            "server, to make it easier for a remote developer to connect from "
            "home without a VPN. From a firewall rule design perspective, what is "
            "the PRIMARY problem with this rule?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It violates least privilege by exposing a database service "
                    "directly to the entire internet instead of restricting the "
                    "source to the developer's specific IP or requiring VPN access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Permitting database access from ANY source on the "
                    "internet is far broader than necessary; least-privilege "
                    "firewall design calls for scoping the source to the specific "
                    "IP needed, or better, requiring the developer to connect "
                    "through a VPN rather than exposing the database directly."
                ),
            },
            {
                "id": "b",
                "text": (
                    "TCP/3306 is not a registered port, so the firewall would "
                    "reject the rule outright"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TCP/3306 is the well-known registered port for "
                    "MySQL and is a valid, configurable port on virtually any "
                    "firewall; the rule would be accepted by the device."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Inbound rules cannot reference specific destination ports, "
                    "only source ports"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall ACLs commonly filter on destination port "
                    "as a primary matching criterion; this option misstates basic "
                    "ACL rule structure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The rule should have used UDP instead of TCP, since database "
                    "protocols require UDP for query performance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MySQL uses TCP, not UDP, for client connections; "
                    "this option describes an inaccurate protocol requirement, "
                    "and protocol choice is not the primary security problem with "
                    "this rule regardless."
                ),
            },
        ],
        "explanation": (
            "The core problem is scope: exposing a database service directly to "
            "any internet source violates least privilege. The correct fix is "
            "restricting the source (or, better, requiring VPN access) rather "
            "than leaving the rule open to the entire internet."
        ),
    },
    {
        "id": "tfw-033",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A security team wants to decrypt outbound HTTPS traffic so that a "
            "separate DLP engine and antivirus scanner can inspect the plaintext "
            "content before re-encrypting it and forwarding it to its destination. "
            "Which appliance performs this function?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TLS/SSL inspection (interception) proxy",
                "correct": True,
                "rationale": (
                    "Correct. A TLS inspection proxy terminates the client's TLS "
                    "session, decrypts the traffic for inspection by tools like "
                    "DLP and antivirus, then re-encrypts it before forwarding to "
                    "the original destination."
                ),
            },
            {
                "id": "b",
                "text": "A stateful firewall permitting only TCP/443",
                "correct": False,
                "rationale": (
                    "Incorrect. A stateful firewall permits or denies connections "
                    "based on header information; it does not decrypt TLS traffic "
                    "for content inspection by other tools."
                ),
            },
            {
                "id": "c",
                "text": "An IDS operating in passive tap mode",
                "correct": False,
                "rationale": (
                    "Incorrect. A passive IDS receives a copy of traffic but "
                    "cannot decrypt TLS-protected content without the same "
                    "interception capability described in the correct answer; it "
                    "also does not re-encrypt and forward traffic."
                ),
            },
            {
                "id": "d",
                "text": "A load balancer configured for round-robin distribution",
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes traffic across "
                    "backend servers; distributing traffic is unrelated to "
                    "decrypting it for content inspection by DLP/AV tools."
                ),
            },
        ],
        "explanation": (
            "Decrypting traffic so other security tools can inspect plaintext "
            "content, then re-encrypting and forwarding it, is the specific "
            "function of a TLS/SSL inspection (interception) proxy."
        ),
    },
    {
        "id": "tfw-034",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall ACL contains the following rules for traffic to a "
            "payment-processing server:\n"
            "1. PERMIT  TCP  10.0.7.0/24  10.0.8.10  443\n"
            "2. PERMIT  TCP  10.0.7.0/24  10.0.8.10  22\n"
            "3. DENY    TCP  ANY          10.0.8.10  22\n"
            "4. DENY    ANY  ANY          ANY  ANY  (implicit)\n"
            "A PCI-DSS auditor flags this rule set. What is the finding, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Rule 2 permits SSH management access to the payment server "
                    "from an entire /24 subnet rather than from specific, "
                    "individually justified administrator hosts, violating least "
                    "privilege for a system in cardholder data scope"
                ),
                "correct": True,
                "rationale": (
                    "Correct. PCI-DSS requires strict least-privilege access "
                    "control for systems that store, process, or transmit "
                    "cardholder data. Permitting SSH management from an entire "
                    "/24 subnet — rather than from specific administrator "
                    "hosts or a jump server — is broader access than necessary "
                    "and a legitimate audit finding."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Rule 3 is unreachable and irrelevant because rule 2 already "
                    "permits the same traffic first, so PCI-DSS considers it a "
                    "critical vulnerability requiring an emergency change"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While rule 3 is indeed shadowed and functionally "
                    "redundant, an unreachable deny rule is a housekeeping/rule-"
                    "hygiene issue, not the primary compliance concern here — the "
                    "overly broad permit in rule 2 is the substantive access-"
                    "control finding."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rule 1 should be removed because PCI-DSS prohibits any "
                    "HTTPS traffic to payment-processing servers under any "
                    "circumstance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. PCI-DSS does not prohibit encrypted HTTPS "
                    "traffic to payment systems — HTTPS/TLS is the expected, "
                    "required way to protect cardholder data in transit, not a "
                    "violation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The implicit deny at the end of the ACL is a PCI-DSS "
                    "violation because it silently drops traffic without logging"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Implicit deny as a default final rule is a "
                    "standard, expected, and PCI-DSS-compliant firewall practice; "
                    "logging is typically configured as a separate setting and "
                    "isn't inherently precluded by having an implicit deny."
                ),
            },
        ],
        "explanation": (
            "PCI-DSS requires least-privilege access to systems in cardholder "
            "data scope; permitting administrative access (SSH) from an entire "
            "subnet rather than specific authorized hosts is a common and valid "
            "audit finding, distinct from unrelated rule-hygiene or encryption "
            "misconceptions."
        ),
    },
    {
        "id": "tfw-035",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "During a firewall rule audit, an analyst finds a rule permitting "
            "inbound TCP/3389 (RDP) from ANY source to a single internal "
            "workstation, created six months ago for a vendor's one-time remote "
            "session that has long since ended. Which action is the CORRECT next "
            "step?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove the rule, since it no longer serves a documented "
                    "business purpose and exposes RDP directly to the internet"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Firewall rule review should remove rules that no "
                    "longer have a valid business justification; leaving an "
                    "any-source RDP rule active long after its purpose ended is "
                    "an unnecessary, high-risk exposure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Leave the rule in place in case the same vendor needs "
                    "similar access again in the future"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Keeping an unjustified, internet-exposed RDP rule "
                    "active \"just in case\" leaves a significant, ongoing "
                    "attack surface open with no current business need — a rule "
                    "should be re-created narrowly if and when actually needed "
                    "again."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Change the rule's port from 3389 to a random high port to "
                    "obscure the RDP service while keeping any-source access"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Security through obscurity (moving the port) does "
                    "not address the underlying issue that RDP remains reachable "
                    "from any source on the internet; the rule itself is no "
                    "longer needed at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enable multifactor authentication on the workstation and "
                    "leave the any-source rule active"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MFA strengthens authentication but does not "
                    "address the fact that the firewall rule itself is stale, "
                    "unjustified, and unnecessarily exposes RDP to the entire "
                    "internet."
                ),
            },
        ],
        "explanation": (
            "Periodic firewall rule review should remove stale rules that no "
            "longer have a documented business justification, rather than "
            "obscuring, compensating for, or indefinitely preserving unnecessary "
            "exposure."
        ),
    },
    {
        "id": "tfw-036",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A firewall administrator is asked to reduce the number of open "
            "inbound rules on the perimeter firewall. Which of these existing "
            "rules should be prioritized for removal FIRST, assuming each was "
            "reviewed independently for current business need?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "PERMIT TCP ANY -> 10.0.2.5 23 (Telnet), left over from a "
                    "decommissioned legacy device that was retired last year"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This rule both serves no current purpose (the "
                    "device is decommissioned) and exposes an inherently insecure "
                    "cleartext protocol to any source — the clearest candidate "
                    "for removal to reduce attack surface."
                ),
            },
            {
                "id": "b",
                "text": (
                    "PERMIT TCP 203.0.113.0/24 -> 10.0.5.10 443, restricting HTTPS "
                    "access to the company's single actively used SaaS partner "
                    "integration IP range"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This rule is narrowly scoped to a specific "
                    "source range, uses an encrypted protocol, and supports an "
                    "active, documented business integration — it should remain."
                ),
            },
            {
                "id": "c",
                "text": (
                    "PERMIT TCP 198.51.100.20 -> 10.0.9.5 22, restricting SSH "
                    "management access to a single administrator's static IP for "
                    "an actively used jump server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This rule is tightly scoped to one source host "
                    "and one destination for active, ongoing administrative use "
                    "— it reflects good least-privilege practice, not a candidate "
                    "for removal."
                ),
            },
            {
                "id": "d",
                "text": (
                    "PERMIT TCP ANY -> 10.0.5.10 443, allowing public HTTPS access "
                    "to the company's actively used public website"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A public web server legitimately needs to accept "
                    "HTTPS connections from any internet source; this rule "
                    "reflects a current, valid business need and should remain."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction prioritizes removing rules that combine "
            "no current business justification with inherently risky, insecure, "
            "or overly broad access — such as an any-source Telnet rule for a "
            "decommissioned device — over well-scoped rules supporting active, "
            "encrypted business needs."
        ),
    },
    {
        "id": "tfw-037",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "In an SDN architecture, network switches and routers forward "
            "packets according to instructions pushed down from a centralized "
            "controller, but they no longer make independent forwarding-policy "
            "decisions themselves. Which SDN concept does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Separation of the control plane (centralized in the "
                    "controller) from the data plane (packet forwarding on the "
                    "switches)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SDN's defining architectural principle is "
                    "separating the control plane — where forwarding decisions "
                    "and policy are determined, centralized in the controller — "
                    "from the data plane, where switches simply forward packets "
                    "according to those instructions."
                ),
            },
            {
                "id": "b",
                "text": "Implicit deny as the default forwarding behavior of every switch",
                "correct": False,
                "rationale": (
                    "Incorrect. Implicit deny is a firewall ACL concept "
                    "describing default behavior for unmatched traffic; it does "
                    "not describe the architectural separation of decision-making "
                    "and forwarding functions in SDN."
                ),
            },
            {
                "id": "c",
                "text": "Micro-segmentation of workloads at the individual host level",
                "correct": False,
                "rationale": (
                    "Incorrect. Micro-segmentation describes fine-grained, "
                    "workload-level policy enforcement, which is a capability SDN "
                    "can enable, but it is not the same concept as the control-"
                    "plane/data-plane separation described in the scenario."
                ),
            },
            {
                "id": "d",
                "text": "Stateful failover between redundant firewall appliances",
                "correct": False,
                "rationale": (
                    "Incorrect. Stateful failover concerns high-availability "
                    "clustering of firewall devices; it is unrelated to how SDN "
                    "centralizes forwarding-policy decisions away from individual "
                    "switches."
                ),
            },
        ],
        "explanation": (
            "SDN centralizes forwarding-policy logic in a controller (the "
            "control plane) while switches simply execute forwarding instructions "
            "(the data plane) — this control/data plane separation is the core "
            "architectural concept that enables programmatic, centralized network "
            "management."
        ),
    },
    {
        "id": "tfw-038",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A next-generation firewall (NGFW) is configured with an application-"
            "aware rule blocking the \"BitTorrent\" application signature, "
            "regardless of the port or IP address a client uses to reach it. A "
            "traditional Layer 3/4 stateful firewall, by contrast, could only "
            "block this traffic by denying specific ports. What capability of the "
            "NGFW enables its approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deep packet inspection with application identification, "
                    "allowing policy to be written against the application itself "
                    "rather than only IP/port tuples"
                ),
                "correct": True,
                "rationale": (
                    "Correct. NGFWs perform deep packet inspection and "
                    "application-layer identification, letting administrators "
                    "write rules based on the actual application in use — "
                    "regardless of the port or IP it happens to use — which a "
                    "traditional Layer 3/4 firewall cannot do."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Stateful connection tracking, which every modern firewall, "
                    "including traditional ones, already performs identically"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Stateful tracking (monitoring connection state) "
                    "is common to both traditional stateful firewalls and NGFWs; "
                    "it is not the differentiating capability that enables "
                    "application-based (rather than port-based) policy."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Implicit deny, which only NGFWs implement as their default "
                    "final rule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Implicit deny is a standard feature of virtually "
                    "all firewalls, traditional and next-generation alike; it is "
                    "not unique to NGFWs and does not explain application-aware "
                    "blocking."
                ),
            },
            {
                "id": "d",
                "text": (
                    "NAT translation, which allows the NGFW to rewrite the "
                    "application's traffic to a different, blocked port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates addresses/ports for routing "
                    "purposes; it does not identify or classify applications and "
                    "is unrelated to how the NGFW recognizes BitTorrent traffic "
                    "regardless of port."
                ),
            },
        ],
        "explanation": (
            "The differentiator between an NGFW and a traditional stateful "
            "firewall is deep packet inspection with application awareness, "
            "which allows policy to target the application itself rather than "
            "being limited to IP addresses, ports, and protocols."
        ),
    },
    {
        "id": "tfw-039",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "An attacker plugs a rogue laptop into an open network jack in an "
            "empty conference room and obtains full network access without any "
            "authentication. Which control would have MOST directly prevented "
            "this specific outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "802.1X port-based authentication requiring a valid "
                    "certificate or credential before the port grants network "
                    "access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 802.1X requires successful authentication before a "
                    "connected device is granted network access on that port, "
                    "which would have blocked the unauthenticated rogue laptop "
                    "from gaining access in the first place."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A web application firewall protecting the internal "
                    "applications the attacker might target"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF protects specific web applications from "
                    "application-layer attacks; it does nothing to prevent a "
                    "rogue device from gaining basic network connectivity through "
                    "an open switch port in the first place."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A stateful firewall permitting only outbound HTTPS traffic "
                    "from the internal network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting outbound protocols at the network "
                    "perimeter does not prevent a rogue device from obtaining "
                    "Layer 2/3 network access via an unsecured internal switch "
                    "port."
                ),
            },
            {
                "id": "d",
                "text": (
                    "TLS encryption enforced for all internal application traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting application traffic protects "
                    "confidentiality in transit but does not control whether a "
                    "device is permitted onto the network in the first place."
                ),
            },
        ],
        "explanation": (
            "802.1X port-based network access control is specifically designed "
            "to require authentication before a device connected to a physical "
            "switch port is granted network access, directly preventing this "
            "kind of rogue-device connection."
        ),
    },
    {
        "id": "tfw-040",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A cloud security engineer manages security groups in a public cloud "
            "environment. A security group attached to a web server instance "
            "permits inbound TCP/443 from 0.0.0.0/0 and denies everything else by "
            "default. An auditor asks how this differs functionally from a "
            "traditional on-premises firewall ACL. What is the MOST accurate "
            "answer?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Functionally, both enforce allow/deny logic on traffic based "
                    "on source, destination, port, and protocol with an implicit "
                    "deny for anything unmatched; the cloud security group is "
                    "simply instance-scoped and API-managed rather than applied to "
                    "a physical network appliance"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cloud security groups apply the same fundamental "
                    "allow/deny, source/destination/port/protocol, and implicit-"
                    "deny logic as a traditional firewall ACL — the key "
                    "difference is that they are attached directly to individual "
                    "instances/resources and managed via API/console rather than "
                    "configured on a physical appliance."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Security groups only evaluate source IP address and ignore "
                    "port and protocol entirely, unlike traditional firewall ACLs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cloud security groups do filter on port and "
                    "protocol in addition to source, just as traditional firewall "
                    "ACLs do; this option misstates their actual matching "
                    "criteria."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Security groups have no implicit deny and permit all "
                    "unmatched traffic by default, unlike traditional firewall "
                    "ACLs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cloud security groups in major providers deny "
                    "unmatched inbound traffic by default, functioning the same "
                    "way as a traditional ACL's implicit deny, not the opposite."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Security groups operate only at Layer 2 and cannot filter "
                    "based on Layer 3 or 4 information such as IP address or port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Security groups filter based on Layer 3/4 "
                    "attributes (IP, port, protocol), just like a traditional "
                    "firewall ACL; this option incorrectly limits them to Layer 2."
                ),
            },
        ],
        "explanation": (
            "Cloud security groups implement the same core allow/deny, "
            "source/destination/port/protocol, and implicit-deny logic as "
            "traditional firewall ACLs; the practical difference is architectural "
            "— instance-level scope and API-driven management — not a difference "
            "in underlying filtering logic."
        ),
    },
    # ------------------------------------------------------------------ #
    # 41-44: multiple_response (2+ correct)
    # ------------------------------------------------------------------ #
    {
        "id": "tfw-041",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall rule-base review of an inbound ACL finds the following "
            "problems. Which TWO represent genuine rule-order or implicit-deny "
            "issues that require reordering or restructuring rules (rather than "
            "issues unrelated to rule order)? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A specific host-level DENY rule is placed below a broader "
                    "subnet-level PERMIT rule that already matches the same "
                    "traffic, making the DENY unreachable (shadowed)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is a textbook shadowed-rule problem: because "
                    "evaluation is top-down and stops at first match, the broader "
                    "permit above prevents the more specific deny below it from "
                    "ever taking effect. Fixing it requires reordering the rules."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A narrowly scoped PERMIT rule for a legitimate business flow "
                    "is placed below a broad DENY rule that already matches the "
                    "same source/destination, making the PERMIT unreachable "
                    "(shadowed)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is also a shadowed-rule problem, in the "
                    "opposite direction: the general deny above blocks the "
                    "traffic before the specific permit below it is ever "
                    "evaluated, requiring the permit to be moved above the deny."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A rule references a destination IP address that was "
                    "reassigned to a different server six months ago and is now "
                    "stale"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stale IP reference is a data-accuracy/rule-"
                    "hygiene issue that requires updating the rule's content, not "
                    "a rule-order or shadowing problem — its position in the list "
                    "is irrelevant to this defect."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A rule's rationale field lacks a change-ticket reference "
                    "documenting who approved it and why"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Missing documentation is a change-management/"
                    "governance gap, not a rule-order or implicit-deny issue; it "
                    "does not affect how the rule is evaluated relative to others."
                ),
            },
            {
                "id": "e",
                "text": (
                    "A rule uses TCP where the intended traffic is actually UDP, "
                    "causing legitimate traffic to fall through to a later rule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a protocol-mismatch/rule-accuracy defect "
                    "in the rule's criteria, not a problem with the order in "
                    "which correctly written rules are evaluated relative to one "
                    "another."
                ),
            },
        ],
        "explanation": (
            "Shadowed rules — whether a specific deny hidden below a broad "
            "permit, or a specific permit hidden below a broad deny — are the "
            "genuine rule-order defects that require reordering; stale data, "
            "missing documentation, and protocol mismatches are real problems "
            "but are not rule-ordering issues."
        ),
    },
    {
        "id": "tfw-042",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A security architect is selecting controls for a new public-facing "
            "e-commerce deployment. Which TWO of the following statements "
            "correctly match a security control to the SPECIFIC threat it "
            "addresses? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A WAF is the appropriate control to detect and block SQL "
                    "injection attempts submitted through the checkout form's "
                    "input fields"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A WAF inspects HTTP request content, including form "
                    "field input, specifically to detect and block injection "
                    "attacks like SQL injection — a precise match of control to "
                    "threat."
                ),
            },
            {
                "id": "b",
                "text": (
                    "TLS is the appropriate control to prevent an on-path "
                    "attacker from reading credit card numbers as they travel "
                    "from the browser to the server"
                ),
                "correct": True,
                "rationale": (
                    "Correct. TLS provides encryption in transit, which is "
                    "precisely the control needed to prevent an eavesdropper from "
                    "reading sensitive data as it crosses the network."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A stateful firewall permitting only TCP/443 is sufficient by "
                    "itself to detect and block SQL injection payloads sent over "
                    "that permitted port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stateful firewall filters based on IP/port/"
                    "protocol/state and cannot inspect or block malicious "
                    "application-layer payloads within a permitted TCP/443 "
                    "session; that is the WAF's job, not the firewall's."
                ),
            },
            {
                "id": "d",
                "text": (
                    "An IDS operating in passive mode is sufficient by itself to "
                    "actively block malicious traffic in real time before it "
                    "reaches the web server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A passive IDS only detects and alerts; it cannot "
                    "block traffic because it is not inline. Active, real-time "
                    "blocking requires an inline control such as an IPS or WAF in "
                    "blocking mode."
                ),
            },
            {
                "id": "e",
                "text": (
                    "A load balancer is the appropriate control to encrypt "
                    "credit card data at rest in the database"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes traffic across "
                    "backend servers; it has no role in encrypting stored data. "
                    "Data-at-rest encryption is handled by database/storage-layer "
                    "encryption controls, not a load balancer."
                ),
            },
        ],
        "explanation": (
            "Correctly matching controls to threats requires precision: a WAF "
            "for application-layer web attacks, TLS for confidentiality in "
            "transit — as opposed to firewalls (port/protocol only), passive IDS "
            "(detection only, no blocking), and load balancers (traffic "
            "distribution, not encryption), each of which addresses a different "
            "problem entirely."
        ),
    },
    {
        "id": "tfw-043",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall ACL protecting a DMZ web server is:\n"
            "1. PERMIT  TCP  ANY  10.0.3.10  443\n"
            "2. PERMIT  TCP  ANY  10.0.3.10  80\n"
            "3. DENY    TCP  ANY  10.0.3.10  22\n"
            "4. DENY    ANY  ANY  ANY  ANY  (implicit)\n"
            "Which TWO statements about this ACL are accurate? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An external SSH (TCP/22) connection attempt to 10.0.3.10 is "
                    "denied by rule 3"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rule 3 explicitly matches and denies TCP/22 traffic "
                    "to 10.0.3.10 from any source, and no earlier rule matches "
                    "SSH traffic, so rule 3 correctly blocks it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Rule 3 is technically redundant in this specific rule set, "
                    "since the implicit deny (rule 4) would have blocked "
                    "unmatched SSH traffic anyway"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because no permit rule earlier in the list matches "
                    "TCP/22 traffic, that traffic would already fall through to "
                    "the implicit deny at rule 4 even without rule 3 present — "
                    "making the explicit deny functionally redundant here, though "
                    "it may still be kept for clarity or auditability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "An external HTTP (TCP/80) connection to 10.0.3.10 is denied "
                    "because rule 1 only permits TCP/443, not TCP/80"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rule 2 explicitly permits TCP/80 to 10.0.3.10 "
                    "from any source, so HTTP traffic is allowed, not denied."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This ACL permits unrestricted TCP traffic on all ports to "
                    "10.0.3.10, since at least one PERMIT rule exists for that "
                    "destination"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Each PERMIT rule matches only its specific port "
                    "(443 or 80); the existence of some permit rules for a "
                    "destination does not open all ports to it, and everything "
                    "else still falls through to a deny."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Traffic on TCP/8080 to 10.0.3.10 is permitted because it is "
                    "close in value to the permitted port 80"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall ACLs match ports as exact values (or "
                    "explicitly defined ranges), not by numeric proximity; TCP/"
                    "8080 does not match rule 2's port-80 permit and falls "
                    "through to the implicit deny."
                ),
            },
        ],
        "explanation": (
            "Careful ACL reading requires matching each field exactly: rule 3 "
            "correctly (if redundantly, given the implicit deny) blocks SSH, "
            "rule 2 explicitly permits HTTP, and no rule grants blanket or "
            "proximity-based port access."
        ),
    },
    {
        "id": "tfw-044",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "Which TWO of the following are legitimate reasons a network "
            "architect would place a public-facing server in a DMZ/screened "
            "subnet rather than directly on the internal LAN? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It limits an attacker who compromises the public server to "
                    "the DMZ segment, since a separate firewall boundary still "
                    "stands between the DMZ and the internal LAN"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The core purpose of a DMZ is containment: if the "
                    "public server is compromised, the attacker still faces a "
                    "second firewall boundary before reaching the internal LAN, "
                    "rather than having immediate internal network access."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It allows firewall rules to permit only the specific "
                    "inbound ports the public server needs (e.g., 443) without "
                    "exposing internal LAN hosts and services to the same "
                    "inbound rule"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Placing the server in its own segment lets the "
                    "firewall scope inbound internet access narrowly to that "
                    "segment and only the required ports, without needing to "
                    "open equivalent inbound access to the internal LAN where "
                    "workstations and internal servers reside."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It automatically encrypts all traffic between the public "
                    "server and internet clients without needing to configure "
                    "TLS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A DMZ is a network segmentation construct and "
                    "provides no encryption on its own; TLS must still be "
                    "explicitly configured on the server to encrypt traffic to "
                    "internet clients."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It eliminates the need for any firewall rules at all "
                    "between the DMZ and the internet, since the DMZ is "
                    "inherently trusted"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A DMZ is explicitly treated as an untrusted or "
                    "semi-trusted zone requiring firewall rules on both the "
                    "internet-facing and internal-facing boundaries; it is not "
                    "an inherently trusted segment that bypasses filtering."
                ),
            },
            {
                "id": "e",
                "text": (
                    "It guarantees the public server cannot be compromised, "
                    "since DMZ placement itself patches any application-layer "
                    "vulnerabilities"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A DMZ limits the blast radius of a compromise but "
                    "does nothing to prevent or patch application-layer "
                    "vulnerabilities on the server itself; the server can still "
                    "be compromised."
                ),
            },
        ],
        "explanation": (
            "A DMZ's value lies in containment and scoped, minimal exposure of "
            "inbound firewall rules — not in providing encryption, eliminating "
            "the need for filtering, or guaranteeing invulnerability, all of "
            "which are separate concerns handled by other controls."
        ),
    },
]
