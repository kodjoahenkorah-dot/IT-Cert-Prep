QUESTIONS = [
    # ── cd5v3-001 ── ACL wildcard mask: /19 ──────────────────────────────────
    {
        "id": "cd5v3-001",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "A network administrator needs to deny all traffic from the 192.168.96.0/19 subnet "
            "using a single standard ACL entry. Which command is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "access-list 10 deny 192.168.96.0 0.0.31.255",
                "correct": True,
                "rationale": (
                    "Correct. A /19 prefix uses subnet mask 255.255.224.0. "
                    "Inverting each octet: 255-224=31 in the third octet, 255-0=255 in the fourth → wildcard 0.0.31.255. "
                    "This matches all 8192 addresses in 192.168.96.0–192.168.127.255."
                ),
            },
            {
                "id": "b",
                "text": "access-list 10 deny 192.168.96.0 0.0.15.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.15.255 is the inverse of a /20 mask (255.255.240.0), "
                    "covering only 192.168.96.0–192.168.111.255. It does not span the full /19 range."
                ),
            },
            {
                "id": "c",
                "text": "access-list 10 deny 192.168.96.0 255.255.224.0",
                "correct": False,
                "rationale": (
                    "Incorrect. 255.255.224.0 is the subnet mask, not the wildcard mask. "
                    "ACLs require inverse (wildcard) masks. Using the subnet mask here produces incorrect matching behavior."
                ),
            },
            {
                "id": "d",
                "text": "access-list 10 deny 192.168.96.0 0.0.63.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.63.255 is the inverse of a /18 mask (255.255.192.0), "
                    "which covers 192.168.64.0–192.168.127.255 — a much larger range than the intended /19."
                ),
            },
        ],
        "explanation": (
            "To find the wildcard mask: subtract the subnet mask from 255.255.255.255. "
            "For /19: 255.255.255.255 − 255.255.224.0 = 0.0.31.255. "
            "A /19 contains 2^13 = 8192 addresses. The network 192.168.96.0/19 spans 192.168.96.0–192.168.127.255. "
            "Standard ACLs (1–99, 1300–1999) match only the source address and should be placed close to the destination."
        ),
    },
    # ── cd5v3-002 ── ACL wildcard mask: matching two /24s with one entry ──────
    {
        "id": "cd5v3-002",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "An engineer wants a single ACL entry that matches ONLY the two subnets "
            "10.10.4.0/24 and 10.10.5.0/24 without matching any other addresses. "
            "Which entry achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "access-list 1 permit 10.10.4.0 0.0.1.255",
                "correct": True,
                "rationale": (
                    "Correct. The wildcard 0.0.1.255 holds the first three octets fixed (0.0) except "
                    "for bit-0 of the third octet (the '1' in 0.0.1), allowing it to be 0 or 1. "
                    "This matches 10.10.4.x (third octet binary ...00000100) and 10.10.5.x (...00000101) only, "
                    "covering exactly both /24 blocks."
                ),
            },
            {
                "id": "b",
                "text": "access-list 1 permit 10.10.4.0 0.0.3.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.3.255 allows bits 0 and 1 of the third octet to vary, "
                    "matching 10.10.4.0–10.10.7.255 (four /24s), not just the two intended subnets."
                ),
            },
            {
                "id": "c",
                "text": "access-list 1 permit 10.10.4.0 0.0.0.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.0.255 matches only 10.10.4.0–10.10.4.255 (one /24). "
                    "A second ACE would be needed for 10.10.5.0/24."
                ),
            },
            {
                "id": "d",
                "text": "access-list 1 permit 10.10.0.0 0.0.7.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.7.255 matches 10.10.0.0–10.10.7.255 (eight /24 subnets), "
                    "which is far broader than the two intended subnets."
                ),
            },
        ],
        "explanation": (
            "Wildcard masks work bit-by-bit: a '0' bit means 'must match', a '1' bit means 'don't care'. "
            "10.10.4.0 in binary third octet is 00000100; 10.10.5.0 is 00000101. "
            "They differ only in bit-0, so the wildcard for that octet is 00000001 = 1, "
            "giving 0.0.1.255. This is a key exam topic — summarizing non-contiguous address ranges."
        ),
    },
    # ── cd5v3-003 ── ACL wildcard: host keyword vs 0.0.0.0 ───────────────────
    {
        "id": "cd5v3-003",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "A security policy requires denying all traffic except from the management host 10.1.1.100. "
            "An engineer writes:\n\n"
            "access-list 99 permit 10.1.1.100 0.0.0.0\n\n"
            "A colleague suggests using 'access-list 99 permit host 10.1.1.100' instead. "
            "Which statement is TRUE?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Both commands are functionally identical; 'host' is syntactic shorthand for the 0.0.0.0 wildcard mask.",
                "correct": True,
                "rationale": (
                    "Correct. On Cisco IOS, 'host <ip>' in an ACL is equivalent to '<ip> 0.0.0.0'. "
                    "Both require all 32 bits to match exactly, permitting only the single host 10.1.1.100."
                ),
            },
            {
                "id": "b",
                "text": "The 'host' keyword applies only to extended ACLs; standard ACLs must use the explicit wildcard 0.0.0.0.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'host' keyword is valid in both standard and extended ACLs on Cisco IOS. "
                    "It is always equivalent to the 0.0.0.0 wildcard mask."
                ),
            },
            {
                "id": "c",
                "text": "The 'host' keyword matches the host and its directly connected /30 subnet.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'host' keyword matches only the exact single IP address — it does not expand to any subnet. "
                    "It is strictly equivalent to a 0.0.0.0 wildcard mask (all 32 bits must match)."
                ),
            },
            {
                "id": "d",
                "text": "The explicit 0.0.0.0 wildcard is processed faster by the router because it avoids keyword expansion.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no processing speed difference. Cisco IOS internally converts the 'host' keyword "
                    "to a 0.0.0.0 wildcard entry; both are represented identically in the ACL data structure."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS ACL keyword shortcuts: 'host <ip>' = '<ip> 0.0.0.0' (match exactly one host). "
            "'any' = '0.0.0.0 255.255.255.255' (match all addresses). "
            "These keywords improve readability without changing behavior. "
            "When an ACL has only permit entries, remember the implicit deny-all at the end blocks everything else."
        ),
    },
    # ── cd5v3-004 ── Extended ACL: placement close to source ─────────────────
    {
        "id": "cd5v3-004",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "Topology: Engineering PCs (172.16.10.0/24) connect to R1 Gi0/0. "
            "R1 Gi0/1 connects to R2 Gi0/0. R2 Gi0/1 connects to Finance servers (172.16.20.0/24). "
            "R2 Gi0/2 connects to HR servers (172.16.30.0/24). "
            "Policy: Engineering must not reach Finance servers (TCP port 443), but may reach HR servers. "
            "Where should an extended ACL be placed for optimal bandwidth conservation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Inbound on R1 Gi0/0 (the interface facing the Engineering PCs).",
                "correct": True,
                "rationale": (
                    "Correct. Extended ACLs should be placed as close to the SOURCE as possible. "
                    "An inbound ACL on R1 Gi0/0 drops the denied traffic immediately, before it consumes "
                    "bandwidth across the R1-to-R2 WAN link. Because it is an extended ACL, it can specify "
                    "both source (Engineering) and destination (Finance/port 443), avoiding collateral blocking."
                ),
            },
            {
                "id": "b",
                "text": "Outbound on R2 Gi0/1 (the interface facing the Finance servers).",
                "correct": False,
                "rationale": (
                    "Incorrect. Placing the ACL outbound on R2 Gi0/1 would work logically, but it wastes bandwidth: "
                    "the denied packets travel all the way from Engineering across R1, over the WAN, through R2 before "
                    "being dropped. Extended ACLs should be as close to the source as possible."
                ),
            },
            {
                "id": "c",
                "text": "Outbound on R1 Gi0/1 (the WAN-facing interface toward R2).",
                "correct": False,
                "rationale": (
                    "Incorrect. While this is closer to the source than R2's interface, the best placement for an "
                    "extended ACL is inbound on the interface closest to the traffic origin — R1 Gi0/0 inbound. "
                    "Applying it outbound on R1 Gi0/1 still allows the packets to enter R1 before being dropped."
                ),
            },
            {
                "id": "d",
                "text": "Inbound on R2 Gi0/0 (the WAN interface on R2).",
                "correct": False,
                "rationale": (
                    "Incorrect. This placement still allows the traffic to traverse the R1-R2 WAN link, wasting bandwidth. "
                    "The optimal placement drops traffic at the source — inbound on R1 Gi0/0."
                ),
            },
        ],
        "explanation": (
            "ACL placement best practices: "
            "Standard ACLs → place close to the DESTINATION (they match source IP only and could block too broadly near source). "
            "Extended ACLs → place close to the SOURCE (they match both src/dst/port so they can be precise, "
            "and dropping traffic early conserves WAN bandwidth). "
            "The engineering network's traffic should be caught at ingress on R1 before crossing any WAN links."
        ),
    },
    # ── cd5v3-005 ── Extended ACL: processing order & implicit deny ───────────
    {
        "id": "cd5v3-005",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "An extended named ACL is applied inbound on Gi0/0:\n\n"
            "ip access-list extended FILTER_IN\n"
            " 10 permit tcp 10.0.0.0 0.255.255.255 any eq 80\n"
            " 20 permit tcp 10.0.0.0 0.255.255.255 any eq 443\n"
            " 30 deny icmp any any\n\n"
            "Host 10.1.1.1 sends an ICMP ping to 8.8.8.8. Host 10.2.2.2 sends an HTTP "
            "request (TCP port 80) to 8.8.8.8. Host 172.16.1.1 sends a DNS query (UDP port 53) to 8.8.8.8. "
            "Which traffic is permitted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Only the HTTP request from 10.2.2.2 is permitted.",
                "correct": True,
                "rationale": (
                    "Correct. 10.2.2.2's HTTP (TCP 80) matches ACE 10 (source in 10.0.0.0/8, dest port 80) → permitted. "
                    "10.1.1.1's ICMP matches ACE 30 (deny icmp any any) → denied. "
                    "172.16.1.1's DNS (UDP 53) does not match ACEs 10, 20, or 30, so it hits the implicit deny-all → denied."
                ),
            },
            {
                "id": "b",
                "text": "HTTP from 10.2.2.2 and DNS from 172.16.1.1 are permitted; ICMP from 10.1.1.1 is denied.",
                "correct": False,
                "rationale": (
                    "Incorrect. The DNS query from 172.16.1.1 does not match any permit ACE and reaches the implicit "
                    "deny-all at the end of the ACL. It is denied, not permitted."
                ),
            },
            {
                "id": "c",
                "text": "All three packets are denied because the implicit deny-all overrides everything.",
                "correct": False,
                "rationale": (
                    "Incorrect. The implicit deny is only reached if no explicit ACE matches. "
                    "ACE 10 explicitly permits TCP port 80 from 10.0.0.0/8; 10.2.2.2's HTTP matches and is permitted."
                ),
            },
            {
                "id": "d",
                "text": "ICMP from 10.1.1.1 and HTTP from 10.2.2.2 are permitted; DNS from 172.16.1.1 is denied.",
                "correct": False,
                "rationale": (
                    "Incorrect. ICMP from 10.1.1.1 matches ACE 30 which explicitly denies all ICMP. "
                    "It is not permitted."
                ),
            },
        ],
        "explanation": (
            "ACL processing is strictly top-down, first-match. ACE 10 permits TCP/80 from 10.0.0.0/8; "
            "ACE 20 permits TCP/443 from 10.0.0.0/8; ACE 30 denies all ICMP. "
            "Anything not matched by ACEs 10-30 hits the implicit 'deny ip any any'. "
            "UDP traffic (DNS) is never matched by TCP-specific permit entries, so it falls to the implicit deny."
        ),
    },
    # ── cd5v3-006 ── ACL: editing a named ACL sequence number ─────────────────
    {
        "id": "cd5v3-006",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "A named extended ACL currently has these entries:\n\n"
            " 10 deny tcp 192.168.1.0 0.0.0.255 any eq 23\n"
            " 20 permit ip any any\n\n"
            "An engineer needs to also deny TCP port 22 (SSH) from the same subnet, "
            "and the new entry must be evaluated BEFORE the permit on line 20 but AFTER line 10. "
            "Which command correctly inserts this entry?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Under 'ip access-list extended <name>': 15 deny tcp 192.168.1.0 0.0.0.255 any eq 22",
                "correct": True,
                "rationale": (
                    "Correct. Named ACLs support sequence-number-based insertion. "
                    "Entering sequence number 15 inserts the new ACE between existing entries 10 and 20, "
                    "ensuring it is evaluated after the Telnet deny and before the permit-all."
                ),
            },
            {
                "id": "b",
                "text": "Delete the ACL and recreate all three entries in the correct order.",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting and recreating is the required workaround for numbered ACLs in legacy mode, "
                    "but named ACLs support direct sequence-number insertion without requiring full recreation."
                ),
            },
            {
                "id": "c",
                "text": "Under 'ip access-list extended <name>': deny tcp 192.168.1.0 0.0.0.255 any eq 22 (no sequence number)",
                "correct": False,
                "rationale": (
                    "Incorrect. Without a sequence number, the entry is appended at the end of the ACL "
                    "(after sequence 20), placing it after the 'permit ip any any'. "
                    "The permit would match all traffic before the new deny is reached."
                ),
            },
            {
                "id": "d",
                "text": "Use the 'ip access-list resequence' command to shift existing entries, then add the new entry as sequence 20.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip access-list resequence' renumbers existing entries with a new starting number "
                    "and increment. While it can create gaps for insertion, the direct approach is simply to assign "
                    "the new entry sequence number 15, which inserts it between 10 and 20 without resequencing."
                ),
            },
        ],
        "explanation": (
            "Named ACLs (both standard and extended) allow inserting, deleting, and replacing individual ACEs "
            "using sequence numbers. To insert an entry between sequence 10 and 20, assign any number between "
            "them (e.g., 15). The router sorts ACEs by sequence number. With numbered ACLs in legacy mode, "
            "new entries always append to the end; to insert mid-list you must delete and recreate the entire ACL. "
            "IOS 12.3+ supports named-ACL-style sequence editing even for numbered ACLs via the named-ACL submode."
        ),
    },
    # ── cd5v3-007 ── ACL: reflexive / stateful comparison ────────────────────
    {
        "id": "cd5v3-007",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "A firewall administrator notices that a static extended ACL on a router permits "
            "established TCP return traffic using 'permit tcp any any established'. "
            "A colleague proposes replacing it with a reflexive ACL using 'reflect' and 'evaluate'. "
            "Which statement BEST explains the security advantage of the reflexive ACL approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A reflexive ACL dynamically creates a temporary permit for the return flow based on the exact 5-tuple of the outbound session, whereas 'established' matches any TCP packet with ACK or RST bits set regardless of whether a session was initiated internally.",
                "correct": True,
                "rationale": (
                    "Correct. 'permit tcp any any established' allows any TCP segment with ACK/RST set inbound, "
                    "even if no corresponding outbound session exists — an attacker can craft such a packet. "
                    "Reflexive ACLs dynamically create per-session permit entries (matching src IP, dst IP, src port, "
                    "dst port, protocol) and remove them when the session ends, providing true stateful behavior."
                ),
            },
            {
                "id": "b",
                "text": "Reflexive ACLs encrypt return traffic while 'established' permits it in cleartext.",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither reflexive ACLs nor the 'established' keyword provides encryption. "
                    "Both are access-control mechanisms only. Encryption is provided by IPsec or TLS."
                ),
            },
            {
                "id": "c",
                "text": "The 'established' keyword performs deep packet inspection and verifies the TCP sequence numbers, making it more secure than reflexive ACLs.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'established' keyword only checks the ACK or RST bit in the TCP header — "
                    "it does not verify sequence numbers or track session state. It is stateless."
                ),
            },
            {
                "id": "d",
                "text": "Reflexive ACLs require a RADIUS server to authorize each return session, providing authentication that 'established' lacks.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reflexive ACLs do not involve RADIUS or any authentication server. "
                    "They operate entirely within the router's ACL subsystem, creating dynamic permit entries "
                    "based on observed outbound traffic."
                ),
            },
        ],
        "explanation": (
            "The 'established' keyword is stateless — it matches any TCP segment with ACK or RST bits set, "
            "making it exploitable by an attacker crafting packets with those flags. "
            "Reflexive ACLs ('reflect' on the outbound ACL, 'evaluate' on the inbound ACL) are dynamic: "
            "they create a temporary, specific permit entry for each outbound session and tear it down when "
            "the session closes. This prevents unsolicited inbound TCP segments from matching. "
            "Cisco Zone-Based Firewall and ASA/FTD use fully stateful inspection, the modern successor to reflexive ACLs."
        ),
    },
    # ── cd5v3-008 ── Port security: aging absolute vs inactivity ─────────────
    {
        "id": "cd5v3-008",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security",
        "stem": (
            "An access switchport is configured:\n\n"
            "switchport port-security maximum 3\n"
            "switchport port-security aging time 5\n"
            "switchport port-security aging type inactivity\n"
            "switchport port-security\n\n"
            "Three devices learn their MACs on the port. All three go silent for 6 minutes. "
            "A fourth device then sends a frame. What is the result?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The fourth device's MAC is learned because the three inactive MACs aged out after 5 minutes of inactivity.",
                "correct": True,
                "rationale": (
                    "Correct. With aging type 'inactivity' and aging time 5 minutes, a MAC is removed from the "
                    "secure MAC table if no traffic is seen from it for 5 minutes. After 6 minutes of silence, "
                    "all three MACs have aged out. The port now has 0 secure MACs, so the fourth device's MAC "
                    "is learned as a new secure MAC without triggering a violation."
                ),
            },
            {
                "id": "b",
                "text": "The port is err-disabled because the fourth MAC exceeds the maximum of 3.",
                "correct": False,
                "rationale": (
                    "Incorrect. If aging were disabled, the port would already be at maximum and a fourth device "
                    "would trigger a violation. However, inactivity aging removes MACs that have been silent for "
                    "5 minutes — all three previous MACs have aged out before the fourth device appears."
                ),
            },
            {
                "id": "c",
                "text": "All three original MACs remain because port-security aging only applies to dynamically learned MACs, not configured maximums.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port security aging applies to dynamically learned and sticky MACs (unless aging type "
                    "is configured to exclude sticky MACs with 'switchport port-security aging static'). "
                    "Dynamic MACs are removed after the configured inactivity period."
                ),
            },
            {
                "id": "d",
                "text": "The fourth device's frame is dropped silently because protect is the default violation mode.",
                "correct": False,
                "rationale": (
                    "Incorrect. The default violation mode is 'shutdown', not 'protect'. "
                    "More importantly, with inactivity aging the previous MACs have timed out, "
                    "so the fourth MAC does not actually cause a violation."
                ),
            },
        ],
        "explanation": (
            "Port security aging has two types: 'absolute' (MACs are removed after the aging time regardless of activity) "
            "and 'inactivity' (MACs are removed only after they have been silent for the aging time). "
            "With 'inactivity' and a 5-minute timer, a MAC that produces no frames for >5 minutes is cleared. "
            "This allows the port to accept new devices after periods of inactivity without administrator intervention. "
            "Sticky MACs can also be aged if 'aging static' is not set."
        ),
    },
    # ── cd5v3-009 ── Port security: err-disabled recovery ────────────────────
    {
        "id": "cd5v3-009",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security",
        "stem": (
            "An access port Fa0/12 is in err-disabled state due to a port-security violation. "
            "The network administrator wants the switch to automatically re-enable the port "
            "after 300 seconds without manual intervention. Which configuration achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "errdisable recovery cause psecure-violation\nerrdisable recovery interval 300",
                "correct": True,
                "rationale": (
                    "Correct. 'errdisable recovery cause psecure-violation' enables automatic recovery specifically "
                    "for port-security err-disable events. 'errdisable recovery interval 300' sets the wait time "
                    "to 300 seconds (5 minutes) before the switch attempts to re-enable the port."
                ),
            },
            {
                "id": "b",
                "text": "interface Fa0/12\n switchport port-security violation restrict",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the violation mode to 'restrict' only affects future violations. "
                    "It does not recover the currently err-disabled port. To change the violation mode, "
                    "the port still needs to be manually re-enabled first."
                ),
            },
            {
                "id": "c",
                "text": "interface Fa0/12\n spanning-tree portfast",
                "correct": False,
                "rationale": (
                    "Incorrect. PortFast enables a port to skip STP listening/learning states. "
                    "It has no effect on err-disabled state caused by port-security violations."
                ),
            },
            {
                "id": "d",
                "text": "errdisable recovery cause bpduguard\nerrdisable recovery interval 300",
                "correct": False,
                "rationale": (
                    "Incorrect. 'errdisable recovery cause bpduguard' enables recovery for BPDU Guard "
                    "err-disable events, not port-security violations. The cause must match the reason "
                    "for the err-disable condition."
                ),
            },
        ],
        "explanation": (
            "The 'errdisable recovery' feature can automatically bring ports out of err-disabled state. "
            "Each cause (psecure-violation, bpduguard, udld, etc.) must be enabled independently. "
            "The global interval sets the recovery timer for all enabled causes. "
            "Manual recovery still requires 'shutdown' followed by 'no shutdown' on the interface. "
            "Common errdisable causes: port-security (psecure-violation), BPDU Guard, UDLD, storm-control."
        ),
    },
    # ── cd5v3-010 ── Port security: show command interpretation ──────────────
    {
        "id": "cd5v3-010",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Port security",
        "stem": (
            "A network engineer runs 'show port-security interface Gi1/0/10' and sees:\n\n"
            "Port Security              : Enabled\n"
            "Port Status                : Secure-shutdown\n"
            "Violation Mode             : Shutdown\n"
            "Security Violation Count   : 1\n"
            "Maximum MAC Addresses      : 1\n"
            "Total MAC Addresses        : 1\n"
            "Configured MAC Addresses   : 0\n"
            "Sticky MAC Addresses       : 1\n\n"
            "Which sequence of events MOST likely caused this state?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A device was connected and its MAC was learned as a sticky entry; a second device was then connected to the same port, triggering the shutdown violation.",
                "correct": True,
                "rationale": (
                    "Correct. One sticky MAC was learned (filling the maximum of 1). "
                    "When a second device appeared, its different MAC exceeded the maximum, "
                    "triggering the 'shutdown' violation mode and err-disabling the port. "
                    "The violation count of 1 confirms exactly one violation event occurred."
                ),
            },
            {
                "id": "b",
                "text": "The port was configured with a static MAC address that does not match any connected device.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Configured MAC Addresses: 0' means no static MAC was manually configured. "
                    "All secure MACs on this port were learned dynamically (Sticky MAC Addresses: 1)."
                ),
            },
            {
                "id": "c",
                "text": "The port aged out its sticky MAC and was shut down due to an empty MAC table.",
                "correct": False,
                "rationale": (
                    "Incorrect. An empty MAC table does not trigger a port-security violation. "
                    "Violations occur when a MAC address exceeds the configured maximum. "
                    "The output shows 1 sticky MAC is still present."
                ),
            },
            {
                "id": "d",
                "text": "The DHCP snooping process err-disabled the port after detecting a rogue DHCP server.",
                "correct": False,
                "rationale": (
                    "Incorrect. The output explicitly shows 'Violation Mode: Shutdown' and 'Security Violation Count: 1', "
                    "which indicates a port-security-triggered err-disable. DHCP snooping violations are reported "
                    "separately and produce different syslog messages."
                ),
            },
        ],
        "explanation": (
            "Reading 'show port-security interface' output: "
            "'Secure-shutdown' = err-disabled by port security. 'Security Violation Count: 1' = one triggering event. "
            "'Configured MAC Addresses: 0' = no static entries. 'Sticky MAC Addresses: 1' = one dynamically learned sticky MAC. "
            "The sequence: sticky MAC learned (port full at max 1) → second device connected → violation → err-disable. "
            "Recovery: 'shutdown' then 'no shutdown' on the interface, or enable errdisable recovery."
        ),
    },
    # ── cd5v3-011 ── DHCP snooping: Option 82 ────────────────────────────────
    {
        "id": "cd5v3-011",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "DHCP snooping is enabled globally and on VLAN 30 on a Cisco Catalyst switch. "
            "A DHCP client on an untrusted access port sends a DHCP DISCOVER. The switch inserts "
            "DHCP Option 82 (relay agent information) before forwarding the DISCOVER upstream. "
            "The upstream DHCP server does not recognize Option 82 and drops the request. "
            "Which command on the switch prevents Option 82 insertion while keeping snooping active?"
        ),
        "options": [
            {
                "id": "a",
                "text": "no ip dhcp snooping information option",
                "correct": True,
                "rationale": (
                    "Correct. The command 'ip dhcp snooping information option' (enabled by default) causes the "
                    "switch to insert Option 82 into client DHCP messages. Issuing 'no ip dhcp snooping information option' "
                    "disables Option 82 insertion while leaving DHCP snooping active."
                ),
            },
            {
                "id": "b",
                "text": "no ip dhcp snooping vlan 30",
                "correct": False,
                "rationale": (
                    "Incorrect. This command disables DHCP snooping entirely on VLAN 30, removing the security "
                    "protection. The goal is to keep snooping active but stop Option 82 insertion."
                ),
            },
            {
                "id": "c",
                "text": "ip dhcp snooping trust (applied to all access ports)",
                "correct": False,
                "rationale": (
                    "Incorrect. Trusting all access ports defeats the purpose of DHCP snooping, allowing rogue "
                    "DHCP servers to operate. Option 82 behavior is controlled separately with 'no ip dhcp snooping "
                    "information option'."
                ),
            },
            {
                "id": "d",
                "text": "ip dhcp relay information trust-all",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip dhcp relay information trust-all' is a DHCP relay agent command that instructs "
                    "the router to forward DHCP messages that already contain Option 82 from untrusted sources. "
                    "It does not prevent the switch from inserting Option 82."
                ),
            },
        ],
        "explanation": (
            "DHCP snooping inserts Option 82 by default when it relays DISCOVER/REQUEST frames from clients. "
            "Some DHCP servers reject or drop packets with Option 82 if they are not configured to handle it. "
            "'no ip dhcp snooping information option' disables this behavior globally. "
            "Alternatively, if the server is under your control, configure it to accept Option 82. "
            "Option 82 is useful for IPAM and policy control when the DHCP server is Option-82-aware."
        ),
    },
    # ── cd5v3-012 ── DHCP snooping: binding table and DAI interaction ─────────
    {
        "id": "cd5v3-012",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "A network engineer enables DHCP snooping and Dynamic ARP Inspection (DAI) on VLAN 50. "
            "A host with a statically assigned IP address (192.168.50.100) and MAC 00:11:22:33:44:55 "
            "is connected to an untrusted access port. The host's IP-to-MAC mapping is NOT in the "
            "DHCP snooping binding table. The host sends an ARP request. What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DAI drops the ARP because the static-IP host's mapping is not in the DHCP snooping binding table.",
                "correct": True,
                "rationale": (
                    "Correct. By default, DAI validates ARP packets on untrusted ports against the DHCP snooping "
                    "binding table. A host with a static IP never goes through DHCP, so its IP-MAC mapping is "
                    "never added to the binding table. DAI cannot validate the ARP and drops it."
                ),
            },
            {
                "id": "b",
                "text": "DAI forwards the ARP because static IP hosts are automatically exempt from DAI inspection.",
                "correct": False,
                "rationale": (
                    "Incorrect. DAI does not automatically exempt static-IP hosts. Without a binding table entry "
                    "or an explicit ARP ACL, the ARP from a static-IP host on an untrusted port is dropped."
                ),
            },
            {
                "id": "c",
                "text": "DAI forwards the ARP because it only inspects ARP replies, not ARP requests.",
                "correct": False,
                "rationale": (
                    "Incorrect. By default DAI inspects both ARP requests and ARP replies on untrusted ports. "
                    "The type of ARP (request vs. reply) does not exempt a packet from inspection."
                ),
            },
            {
                "id": "d",
                "text": "DHCP snooping automatically adds a static binding for the host when it detects the ARP.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping builds its binding table from DHCP ACK messages only. "
                    "It does not create binding entries by inspecting ARP traffic. "
                    "Static bindings must be added manually with 'ip dhcp snooping binding'."
                ),
            },
        ],
        "explanation": (
            "For hosts with static IP addresses, you must create a manual DHCP snooping binding entry: "
            "'ip dhcp snooping binding <MAC> vlan <id> <IP> interface <intf> expiry <seconds>' "
            "Or create an ARP ACL: 'arp access-list STATIC_HOSTS' with 'permit ip host <IP> mac host <MAC>', "
            "then apply it to DAI with 'ip arp inspection filter STATIC_HOSTS vlan 50'. "
            "This is a common operational pitfall when DAI is deployed in networks with mixed DHCP and static hosts."
        ),
    },
    # ── cd5v3-013 ── DAI: trusted port on uplink ──────────────────────────────
    {
        "id": "cd5v3-013",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "DAI is enabled on VLAN 100. The distribution switch uplink (Gi0/24) connects to a "
            "router that acts as the default gateway. ARP traffic from the router is being dropped. "
            "The DHCP snooping binding table has no entry for the router's IP (10.100.0.1) because "
            "the router uses a static IP. What is the BEST fix that maintains security for end hosts?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure 'ip arp inspection trust' on Gi0/24 so the router's uplink port bypasses DAI.",
                "correct": True,
                "rationale": (
                    "Correct. Uplink ports to trusted infrastructure devices (routers, other switches) should be "
                    "marked as DAI-trusted with 'ip arp inspection trust'. This exempts ARP from the router from "
                    "validation while untrusted access ports facing end hosts remain protected."
                ),
            },
            {
                "id": "b",
                "text": "Disable DAI on VLAN 100 with 'no ip arp inspection vlan 100'.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling DAI entirely on the VLAN removes ARP spoofing protection for all hosts. "
                    "The correct approach is to trust only the specific uplink port, not disable DAI globally."
                ),
            },
            {
                "id": "c",
                "text": "Enable DHCP snooping trust on Gi0/24 to allow the router's IP into the binding table.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping trust controls which ports can receive DHCP server messages, "
                    "not ARP validation. DAI uses a separate trust configuration via 'ip arp inspection trust'. "
                    "The router's static IP will still not appear in the DHCP binding table."
                ),
            },
            {
                "id": "d",
                "text": "Create a static DHCP snooping binding for 10.100.0.1 on every access port in VLAN 100.",
                "correct": False,
                "rationale": (
                    "Incorrect. Static bindings are per-interface and per-VLAN; adding them on every access port "
                    "is operationally impractical. The simple and correct solution is to trust the uplink port Gi0/24."
                ),
            },
        ],
        "explanation": (
            "DAI trusted ports bypass ARP inspection. Uplinks to routers and trusted switches should be DAI-trusted "
            "to prevent false positives on infrastructure ARP traffic. Use 'ip arp inspection trust' under the "
            "interface configuration. This is separate from DHCP snooping trust ('ip dhcp snooping trust'). "
            "Both features have independent trust configurations, but in practice both are typically set together "
            "on the same uplink interfaces."
        ),
    },
    # ── cd5v3-014 ── AAA: TACACS+ per-command authorization flow ─────────────
    {
        "id": "cd5v3-014",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A Cisco router is configured for AAA with TACACS+ for device administration. "
            "An engineer logs in and enters privileged EXEC mode. She types 'show running-config'. "
            "The TACACS+ server has a policy denying this command for her privilege level. "
            "Which AAA function enforces this restriction, and what does the router do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Authorization: the router sends the command to the TACACS+ server for approval; the server returns a FAIL response and the router rejects the command.",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ authorization can evaluate individual commands. When the engineer types a command, "
                    "the router sends an authorization request to the TACACS+ server. The server checks its policy "
                    "and returns PASS or FAIL. A FAIL response causes the router to deny the command execution."
                ),
            },
            {
                "id": "b",
                "text": "Authentication: the TACACS+ server challenges the engineer with a second password prompt before allowing the command.",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication verifies identity at login, not at command execution. "
                    "The per-command control described is the authorization function of AAA."
                ),
            },
            {
                "id": "c",
                "text": "Accounting: the TACACS+ server logs the command attempt and sends a DENY record to block future attempts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Accounting records what users do (for audit trails) but does not make allow/deny decisions. "
                    "Authorization is the AAA function that controls whether an action is permitted."
                ),
            },
            {
                "id": "d",
                "text": "Authorization: the router checks the local privilege level (1–15) and denies the command because the engineer's privilege level is below 15.",
                "correct": False,
                "rationale": (
                    "Incorrect. Local privilege-level enforcement is not AAA authorization. "
                    "When TACACS+ authorization is configured, the router defers the allow/deny decision "
                    "to the TACACS+ server, which can apply per-user, per-command policies independent of local privilege levels."
                ),
            },
        ],
        "explanation": (
            "TACACS+ AAA for device administration: "
            "Authentication = who are you (login). Authorization = what are you allowed to do (per command). "
            "Accounting = record what you did (audit log). "
            "TACACS+ authorization sends each command to the server for evaluation — enabling very granular control "
            "(e.g., allow 'show' commands, deny 'configure terminal'). This is the primary reason TACACS+ is "
            "preferred over RADIUS for network device administration."
        ),
    },
    # ── cd5v3-015 ── AAA: RADIUS accounting ports ─────────────────────────────
    {
        "id": "cd5v3-015",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A network engineer is configuring a Cisco router to use a RADIUS server at 10.0.0.10 "
            "for 802.1X network access authentication and RADIUS accounting. "
            "The security team requires the standard IANA-assigned ports for both functions. "
            "Which configuration is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "radius server ISE\n address ipv4 10.0.0.10 auth-port 1812 acct-port 1813\n key Str0ngKey",
                "correct": True,
                "rationale": (
                    "Correct. IANA assigns UDP port 1812 for RADIUS authentication/authorization "
                    "and UDP port 1813 for RADIUS accounting. These are the modern standard ports "
                    "that replaced the older unofficial ports 1645/1646."
                ),
            },
            {
                "id": "b",
                "text": "radius server ISE\n address ipv4 10.0.0.10 auth-port 1645 acct-port 1646\n key Str0ngKey",
                "correct": False,
                "rationale": (
                    "Incorrect. Ports 1645 and 1646 are the original unofficial RADIUS ports from early "
                    "implementations. IANA formally assigned ports 1812 (authentication) and 1813 (accounting) "
                    "in RFC 2865/2866. Most modern deployments use 1812/1813."
                ),
            },
            {
                "id": "c",
                "text": "radius server ISE\n address ipv4 10.0.0.10 auth-port 49 acct-port 1813\n key Str0ngKey",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP port 49 is used by TACACS+, not RADIUS. "
                    "RADIUS uses UDP ports 1812 for authentication and 1813 for accounting."
                ),
            },
            {
                "id": "d",
                "text": "radius server ISE\n address ipv4 10.0.0.10 auth-port 1812 acct-port 1812\n key Str0ngKey",
                "correct": False,
                "rationale": (
                    "Incorrect. Using the same port 1812 for both authentication and accounting is wrong. "
                    "Authentication uses UDP 1812 and accounting uses a separate port: UDP 1813."
                ),
            },
        ],
        "explanation": (
            "RADIUS port reference: UDP 1812 = authentication and authorization (RFC 2865). "
            "UDP 1813 = accounting (RFC 2866). Older legacy ports: 1645 (auth) and 1646 (acct). "
            "TACACS+ uses TCP 49 (all AAA functions on one port). "
            "Cisco IOS 'radius server' stanza syntax (IOS 15.x+): 'address ipv4 <ip> auth-port <n> acct-port <n>' "
            "with 'key <shared-secret>'."
        ),
    },
    # ── cd5v3-016 ── AAA: local fallback ──────────────────────────────────────
    {
        "id": "cd5v3-016",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A router is configured with:\n\n"
            "aaa new-model\n"
            "aaa authentication login VTY_AUTH group tacacs+ local\n"
            "line vty 0 4\n"
            " login authentication VTY_AUTH\n\n"
            "The TACACS+ server is unreachable. An engineer attempts to log in using local credentials. "
            "What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router falls back to the local user database because 'local' is listed as the second method after 'group tacacs+'.",
                "correct": True,
                "rationale": (
                    "Correct. AAA method lists are evaluated left to right. If the first method (TACACS+) is unreachable "
                    "(server timeout/unavailable), IOS tries the next method (local). The engineer can log in with "
                    "locally configured credentials."
                ),
            },
            {
                "id": "b",
                "text": "Login is denied because when TACACS+ is unreachable, the router treats it as an authentication failure.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Server unreachable' is treated differently from 'server returned FAIL'. "
                    "When a server is unreachable (timeout), IOS moves to the next method in the list. "
                    "Only if the server explicitly returns an authentication failure does IOS stop (without trying the next method)."
                ),
            },
            {
                "id": "c",
                "text": "The console port can be used but VTY access is completely blocked when TACACS+ is down.",
                "correct": False,
                "rationale": (
                    "Incorrect. The method list includes 'local' as a fallback. VTY access is available via local "
                    "credentials when TACACS+ is unreachable. The console port typically uses a separate method list."
                ),
            },
            {
                "id": "d",
                "text": "The router prompts for the TACACS+ server's IP address so the engineer can redirect the request.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no mechanism in Cisco IOS AAA to prompt for a server address at login. "
                    "The fallback to 'local' is automatic when the configured AAA server is unreachable."
                ),
            },
        ],
        "explanation": (
            "AAA method lists define an ordered sequence of authentication methods. IOS tries each method left to right "
            "only when the previous method's server is unreachable (ERROR). If a server responds with an explicit "
            "REJECT, IOS does NOT try the next method — authentication fails immediately. "
            "Best practice: always include 'local' or 'none' as a final fallback to prevent lockout if AAA servers fail. "
            "For highest security, configure 'aaa authentication login default group tacacs+ local enable' on the console."
        ),
    },
    # ── cd5v3-017 ── Device access control: SSH v2 prerequisites ─────────────
    {
        "id": "cd5v3-017",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "An engineer is configuring SSH version 2 on a router but receives the error "
            "'SSH v2 requires RSA key pair'. The router currently has no domain name configured. "
            "Which ordered sequence of commands is required to enable SSH v2 with a local login?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "1) ip domain-name corp.local  "
                    "2) crypto key generate rsa modulus 2048  "
                    "3) ip ssh version 2  "
                    "4) line vty 0 4: login local, transport input ssh"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SSH requires a domain name (used in RSA key label), then key generation (minimum 768 bits "
                    "for SSHv2, best practice 2048), then 'ip ssh version 2' to restrict to SSHv2 only, "
                    "then VTY configuration for local authentication and SSH-only transport."
                ),
            },
            {
                "id": "b",
                "text": (
                    "1) crypto key generate rsa modulus 2048  "
                    "2) ip domain-name corp.local  "
                    "3) ip ssh version 2  "
                    "4) line vty 0 4: login local, transport input ssh"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'crypto key generate rsa' requires a fully qualified domain name to create the key label "
                    "(hostname.domainname). The 'ip domain-name' command must be configured BEFORE key generation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "1) ip domain-name corp.local  "
                    "2) ip ssh version 2  "
                    "3) crypto key generate rsa modulus 2048  "
                    "4) line vty 0 4: login local, transport input ssh"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip ssh version 2' can be entered before key generation, but the key must exist "
                    "for SSH to function. More importantly, the standard best-practice sequence generates the key "
                    "before enabling SSH version 2, ensuring a clean configuration."
                ),
            },
            {
                "id": "d",
                "text": (
                    "1) ip domain-name corp.local  "
                    "2) crypto key generate rsa modulus 512  "
                    "3) ip ssh version 2  "
                    "4) line vty 0 4: login local, transport input ssh"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A 512-bit RSA key is insufficient for SSHv2. Cisco IOS requires a minimum of 768 bits "
                    "for SSHv2; the CCNA-recommended best practice is 2048 bits."
                ),
            },
        ],
        "explanation": (
            "SSH v2 configuration checklist: (1) hostname (must be set). (2) ip domain-name. "
            "(3) crypto key generate rsa modulus 2048 (minimum 768 for SSHv2). "
            "(4) ip ssh version 2. (5) username <name> secret <pw>. "
            "(6) line vty 0 4 → login local + transport input ssh. "
            "Optionally: ip ssh time-out 60, ip ssh authentication-retries 3."
        ),
    },
    # ── cd5v3-018 ── Device access control: console timeout ──────────────────
    {
        "id": "cd5v3-018",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "A security audit finding states that router console sessions remain active indefinitely "
            "after an administrator walks away. The organization's policy requires console sessions "
            "to time out after 5 minutes of inactivity. Which configuration satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "line con 0\n exec-timeout 5 0",
                "correct": True,
                "rationale": (
                    "Correct. The 'exec-timeout <minutes> <seconds>' command under 'line con 0' sets the inactivity "
                    "timeout for the console. 'exec-timeout 5 0' disconnects the session after 5 minutes 0 seconds of inactivity."
                ),
            },
            {
                "id": "b",
                "text": "line con 0\n session-timeout 5",
                "correct": False,
                "rationale": (
                    "Incorrect. 'session-timeout' controls the timeout for outbound sessions initiated FROM the line "
                    "(e.g., Telnet to another device). 'exec-timeout' is the correct command for the local EXEC session inactivity timer."
                ),
            },
            {
                "id": "c",
                "text": "line vty 0 4\n exec-timeout 5 0",
                "correct": False,
                "rationale": (
                    "Incorrect. 'line vty 0 4' configures VTY (Telnet/SSH) lines, not the physical console port. "
                    "The console is configured under 'line con 0'."
                ),
            },
            {
                "id": "d",
                "text": "line con 0\n exec-timeout 0 5",
                "correct": False,
                "rationale": (
                    "Incorrect. 'exec-timeout 0 5' sets a timeout of 0 minutes and 5 seconds — a 5-second timeout, "
                    "not 5 minutes. The syntax is 'exec-timeout <minutes> <seconds>'. "
                    "Note: 'exec-timeout 0 0' disables the timeout entirely."
                ),
            },
        ],
        "explanation": (
            "'exec-timeout <minutes> <seconds>' is the IOS command for session inactivity timeout. "
            "It applies under 'line con 0' (console), 'line aux 0' (auxiliary port), "
            "and 'line vty 0 4' (VTY lines) independently. "
            "'exec-timeout 0 0' disables the timeout (dangerous — sessions never expire). "
            "The console line does not have transport input/output settings since it is always present."
        ),
    },
    # ── cd5v3-019 ── Device access control: privilege levels ─────────────────
    {
        "id": "cd5v3-019",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "A company wants junior network operators to run 'show' commands on routers but "
            "NOT be able to enter configuration mode or run 'debug' commands. "
            "The engineer creates a local user with privilege level 7 and assigns specific "
            "commands to that level. An operator logs in at privilege 7. "
            "Which statement is TRUE about this operator's access?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The operator can execute only the commands explicitly assigned to privilege level 7 or below (levels 1–7), plus any commands that default to a lower privilege level.",
                "correct": True,
                "rationale": (
                    "Correct. Privilege levels are cumulative: a user at level 7 can execute all commands at levels "
                    "1 through 7. By default, 'show' commands are at level 1 (user EXEC), so they are accessible. "
                    "'configure terminal' is at level 15 and is not accessible at level 7 unless explicitly reassigned."
                ),
            },
            {
                "id": "b",
                "text": "The operator automatically gains privilege level 15 after successfully authenticating because all local users default to the highest privilege.",
                "correct": False,
                "rationale": (
                    "Incorrect. Local users have the privilege level specified in their account definition. "
                    "The default privilege level for 'username' accounts without explicit level specification is 1, "
                    "not 15. Privilege 15 must be explicitly assigned."
                ),
            },
            {
                "id": "c",
                "text": "The operator can use 'enable' to elevate to privilege 15 without a password because privilege levels only apply in user EXEC mode.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'enable' command requires the enable secret (or enable password for the target "
                    "privilege level) to elevate. A user at privilege 7 cannot jump to 15 without the correct password."
                ),
            },
            {
                "id": "d",
                "text": "Privilege levels 2–14 are reserved by Cisco and cannot be assigned to custom commands.",
                "correct": False,
                "rationale": (
                    "Incorrect. Privilege levels 2–14 are fully customizable. The reserved fixed levels are 0 "
                    "(disable, enable, exit, help, logout), 1 (user EXEC defaults), and 15 (privileged EXEC). "
                    "Levels 2–14 are free for administrators to assign commands as needed."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS has 16 privilege levels (0–15). Level 1 = user EXEC (default), Level 15 = privileged EXEC. "
            "Commands can be moved between levels with 'privilege exec level <n> <command>'. "
            "A user at level N can execute all commands assigned to levels 0 through N. "
            "Local user accounts: 'username <name> privilege <n> secret <pw>'. "
            "The 'enable' command can raise privilege but requires the matching enable secret for the target level."
        ),
    },
    # ── cd5v3-020 ── Wireless security: WPA3-Enterprise ───────────────────────
    {
        "id": "cd5v3-020",
        "domain": 5,
        "objective": "5.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "A financial institution is upgrading its wireless infrastructure to WPA3-Enterprise. "
            "The security team requires 192-bit minimum security. "
            "Which cipher suite and key management combination satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "AES-GCMP-256 encryption with ECDH and ECDSA using 384-bit elliptic curves (Suite B).",
                "correct": True,
                "rationale": (
                    "Correct. WPA3-Enterprise 192-bit mode (defined in Wi-Fi CERTIFIED WPA3) requires AES-GCMP-256 "
                    "for data encryption, ECDH with P-384 for key exchange, and ECDSA-384 for authentication. "
                    "This aligns with NSA Suite B cryptography for sensitive environments."
                ),
            },
            {
                "id": "b",
                "text": "AES-CCMP-128 encryption with RSA-2048 certificates and EAP-PEAP.",
                "correct": False,
                "rationale": (
                    "Incorrect. AES-CCMP-128 provides 128-bit security and does not satisfy the 192-bit minimum "
                    "requirement. WPA3-Enterprise 192-bit mode requires AES-GCMP-256 and ECDH/ECDSA with 384-bit curves."
                ),
            },
            {
                "id": "c",
                "text": "TKIP-256 with SHA-256 HMAC, providing backward compatibility with WPA2 devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP is deprecated and is prohibited in WPA3. WPA3 requires AES-based encryption. "
                    "There is no 'TKIP-256' — TKIP was limited to 128-bit RC4-based encryption."
                ),
            },
            {
                "id": "d",
                "text": "AES-CCMP-256 with RSA-4096 and SAE key exchange.",
                "correct": False,
                "rationale": (
                    "Incorrect. SAE (Dragonfly) is specific to WPA3-Personal, not WPA3-Enterprise. "
                    "WPA3-Enterprise 192-bit mode uses 802.1X/EAP with Suite B cryptography (ECDH/ECDSA), not SAE. "
                    "AES-GCMP-256 (not AES-CCMP-256) is the specified cipher."
                ),
            },
        ],
        "explanation": (
            "WPA3-Enterprise has two modes: standard (similar to WPA2-Enterprise with stronger requirements) "
            "and 192-bit mode. The 192-bit mode uses: AES-GCMP-256 for data protection, "
            "ECDH-384 and ECDSA-384 (P-384 curve) for key exchange and authentication, "
            "SHA-384 for HMAC. This maps to NSA CNSS Policy No. 15 Suite B. "
            "EAP-TLS with Suite B certificates (ECDSA) is the authentication method."
        ),
    },
    # ── cd5v3-021 ── Wireless security: open vs WEP vs WPA ────────────────────
    {
        "id": "cd5v3-021",
        "domain": 5,
        "objective": "5.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "A network administrator is reviewing legacy wireless deployments. "
            "One SSID uses WEP-64 with a static 40-bit key. The admin proposes upgrading to WPA2-Personal. "
            "Which statement BEST explains why WEP is considered cryptographically broken?"
        ),
        "options": [
            {
                "id": "a",
                "text": "WEP uses RC4 with a static key and a weak 24-bit IV that repeats, allowing passive attacks to recover the key by collecting enough IVs.",
                "correct": True,
                "rationale": (
                    "Correct. WEP's fundamental weakness is its 24-bit initialization vector (IV), which repeats "
                    "frequently in busy networks. Using tools like Aircrack-ng, an attacker can passively capture "
                    "IV collisions and statistically derive the RC4 key within minutes."
                ),
            },
            {
                "id": "b",
                "text": "WEP is broken because it uses a 56-bit DES cipher, which is vulnerable to brute-force attacks on modern hardware.",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP uses RC4, not DES. The 56-bit DES vulnerability applies to older protocols like "
                    "MS-CHAPv1. WEP's weakness is the short, reusable IV combined with the RC4 stream cipher."
                ),
            },
            {
                "id": "c",
                "text": "WEP is broken because it uses AES in ECB mode, which leaks patterns in plaintext.",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP uses RC4 (a stream cipher), not AES. AES-ECB's pattern-leakage is a different "
                    "vulnerability entirely unrelated to WEP."
                ),
            },
            {
                "id": "d",
                "text": "WEP is broken because its PSK handshake is vulnerable to offline dictionary attacks using captured 4-way handshakes.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 4-way handshake dictionary attack applies to WPA/WPA2-PSK (PBKDF2-based PMK). "
                    "WEP does not use a 4-way handshake; it uses a simple challenge-response or open authentication "
                    "with a shared static RC4 key."
                ),
            },
        ],
        "explanation": (
            "WEP (Wired Equivalent Privacy) uses RC4 with a 40-bit or 104-bit key XORed with a 24-bit IV. "
            "The 24-bit IV space (16,777,216 values) is exhausted quickly on busy networks, causing IV reuse. "
            "Fluhrer-Mantin-Shamir (FMS) attack and later PTW attack can recover WEP keys in under 60 seconds "
            "with ~40,000 captured IV packets. WEP was deprecated by the IEEE 802.11i amendment in 2004. "
            "Upgrade path: WEP → WPA (TKIP) → WPA2 (AES-CCMP) → WPA3 (AES-GCMP + SAE)."
        ),
    },
    # ── cd5v3-022 ── Wireless security: rogue AP and evil twin ────────────────
    {
        "id": "cd5v3-022",
        "domain": 5,
        "objective": "5.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "An attacker sets up an unauthorized access point broadcasting the same SSID as the corporate "
            "WLAN on the same channel with higher transmit power, causing clients to associate with the "
            "attacker's AP. What type of attack is this, and which Cisco WLC feature can detect it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Evil twin attack; detected by the Cisco WLC rogue AP detection feature using RF scanning and comparing BSSID against the authorized AP list.",
                "correct": True,
                "rationale": (
                    "Correct. An evil twin uses the same SSID to lure clients. Cisco WLC can detect rogue APs "
                    "through dedicated monitor-mode APs or dual-band scanning, comparing discovered BSSIDs against "
                    "the known authorized AP list. Unrecognized BSSIDs with matching SSIDs trigger rogue AP alerts."
                ),
            },
            {
                "id": "b",
                "text": "Deauthentication flood attack; detected by the WLC using RSSI threshold monitoring.",
                "correct": False,
                "rationale": (
                    "Incorrect. A deauthentication flood sends spoofed 802.11 deauth frames to disconnect clients. "
                    "The scenario describes an evil twin (duplicate SSID AP), not a deauth flood."
                ),
            },
            {
                "id": "c",
                "text": "ARP poisoning attack; detected by Dynamic ARP Inspection on the WLC.",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning targets wired Layer 2 segments and is a post-association attack. "
                    "The scenario describes a wireless-layer attack where the client associates with a rogue AP. "
                    "DAI is a wired switch security feature, not a wireless intrusion detection mechanism."
                ),
            },
            {
                "id": "d",
                "text": "MAC flooding attack; detected by the WLC using port-security on the AP uplink.",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding fills a switch's CAM table to cause it to broadcast frames. "
                    "The scenario describes an evil twin wireless attack. Port security on an AP uplink does not "
                    "detect or prevent wireless-layer evil twin attacks."
                ),
            },
        ],
        "explanation": (
            "An evil twin AP replicates a legitimate SSID to intercept client traffic. "
            "Cisco WLC rogue detection uses monitor-mode APs (or time-sliced scanning) to identify all 802.11 "
            "frames in range. Any BSSID not in the authorized list is flagged as a rogue. "
            "Automatic containment (airewave director) can send deauth frames to clients connecting to rogues. "
            "Client-side protection: WPA2/WPA3 mutual authentication (server certificate validation in EAP-TLS/PEAP) "
            "helps clients verify they are connecting to the legitimate corporate infrastructure."
        ),
    },
    # ── cd5v3-023 ── IPsec VPNs: IKE Phase 1 vs Phase 2 ──────────────────────
    {
        "id": "cd5v3-023",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPsec VPNs",
        "stem": (
            "During IKEv1 site-to-site VPN establishment between two routers, Phase 1 completes "
            "successfully but Phase 2 fails. The engineer runs 'debug crypto ipsec' and sees "
            "'no matching crypto map'. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The crypto map on one or both routers specifies an access-list (interesting traffic selector) that does not match the actual traffic being tunneled.",
                "correct": True,
                "rationale": (
                    "Correct. IKE Phase 2 establishes the IPsec SA for actual data traffic. The crypto map's "
                    "access-list defines 'interesting traffic' — the source/destination networks to be tunneled. "
                    "If the ACLs on the two peers are not mirror images of each other, Phase 2 fails with "
                    "'no matching crypto map entry' or similar errors."
                ),
            },
            {
                "id": "b",
                "text": "The pre-shared keys on the two peers do not match.",
                "correct": False,
                "rationale": (
                    "Incorrect. Mismatched pre-shared keys would prevent Phase 1 (ISAKMP SA) from completing. "
                    "Since Phase 1 succeeded, the PSKs match. The Phase 2 failure points to a mismatch in the "
                    "IPsec transform set or traffic selectors."
                ),
            },
            {
                "id": "c",
                "text": "IKE Phase 1 and Phase 2 use the same ISAKMP SA, so a Phase 2 failure automatically invalidates Phase 1.",
                "correct": False,
                "rationale": (
                    "Incorrect. Phase 1 (ISAKMP SA) and Phase 2 (IPsec SA) are independent. Phase 1 establishes "
                    "a secure channel for Phase 2 negotiation. A Phase 2 failure does not automatically tear down Phase 1."
                ),
            },
            {
                "id": "d",
                "text": "The routers use different IKE versions (one uses IKEv1, the other IKEv2), causing incompatibility in Phase 2.",
                "correct": False,
                "rationale": (
                    "Incorrect. An IKEv1/IKEv2 mismatch would typically cause Phase 1 to fail, not Phase 2. "
                    "Also, the debug message 'no matching crypto map' specifically indicates a traffic selector "
                    "or policy mismatch within the same IKE version."
                ),
            },
        ],
        "explanation": (
            "IKEv1 Phase 1 negotiates the ISAKMP SA (encryption/hash/auth/DH for the control channel). "
            "IKEv1 Phase 2 (Quick Mode) negotiates the IPsec SA using the Phase 1 tunnel. "
            "Phase 2 requires matching: (1) crypto map access-lists (mirror-image ACLs on both peers), "
            "(2) transform sets (AES algorithm, HMAC, PFS group). "
            "A common mistake is non-mirrored ACLs: Router A permits 10.1.0.0/24→10.2.0.0/24, "
            "but Router B permits 10.2.0.0/24→10.3.0.0/24. These do not match, causing Phase 2 failure."
        ),
    },
    # ── cd5v3-024 ── IPsec VPNs: tunnel vs transport mode ────────────────────
    {
        "id": "cd5v3-024",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPsec VPNs",
        "stem": (
            "An IPsec VPN is built between two routers to protect traffic between two branch office networks. "
            "The VPN uses ESP in tunnel mode. Which header structure correctly describes an encrypted packet "
            "as it traverses the internet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "New outer IP header | ESP header | Original IP header | Original payload | ESP trailer | ESP auth",
                "correct": True,
                "rationale": (
                    "Correct. In ESP tunnel mode, the entire original IP packet (header + payload) is encrypted "
                    "and encapsulated inside a new ESP packet with a new outer IP header bearing the tunnel "
                    "endpoint addresses. This hides the original source and destination from observers on the internet."
                ),
            },
            {
                "id": "b",
                "text": "Original IP header | ESP header | Original payload | ESP trailer | ESP auth",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the structure for ESP in TRANSPORT mode, where the original IP header "
                    "is preserved and only the payload is encrypted. Transport mode is used for host-to-host "
                    "IPsec, not gateway-to-gateway site-to-site VPNs."
                ),
            },
            {
                "id": "c",
                "text": "New outer IP header | AH header | Original IP header | Original payload",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes AH tunnel mode, which provides authentication and integrity but "
                    "NOT confidentiality (no encryption). The scenario uses ESP, which provides encryption."
                ),
            },
            {
                "id": "d",
                "text": "Original IP header | GRE header | New inner IP header | Original payload",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes plain GRE tunneling without IPsec encryption. "
                    "GRE does not provide confidentiality, integrity, or authentication on its own."
                ),
            },
        ],
        "explanation": (
            "IPsec modes: Transport mode preserves the original IP header and encrypts only the payload "
            "(used for host-to-host IPsec). Tunnel mode encapsulates the entire original packet with a new "
            "outer IP header (used for gateway-to-gateway site-to-site VPNs). "
            "ESP tunnel mode packet structure: [New IP hdr][ESP hdr][Encrypted: Orig IP hdr + payload][ESP trailer][ESP ICV]. "
            "The original IP header is encrypted, hiding internal network topology from internet observers."
        ),
    },
    # ── cd5v3-025 ── IPsec VPNs: GRE over IPsec use case ─────────────────────
    {
        "id": "cd5v3-025",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPsec VPNs",
        "stem": (
            "A company uses a site-to-site IPsec VPN between two branch offices and wants to run "
            "OSPF routing updates across the tunnel. The engineer finds that OSPF adjacency cannot "
            "form over the native IPsec tunnel. Which solution addresses this limitation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wrap the IPsec tunnel inside a GRE tunnel (GRE over IPsec), which provides a point-to-point logical interface for OSPF to use.",
                "correct": True,
                "rationale": (
                    "Correct. Native IPsec does not provide a multicast-capable logical interface, so routing protocols "
                    "that rely on multicast (like OSPF using 224.0.0.5/6) cannot form adjacencies. "
                    "GRE creates a logical tunnel interface that OSPF can treat as a point-to-point link, "
                    "and IPsec encrypts the GRE traffic for security."
                ),
            },
            {
                "id": "b",
                "text": "Configure static routes on both routers, as OSPF is not supported across any VPN type.",
                "correct": False,
                "rationale": (
                    "Incorrect. OSPF can run across VPN tunnels — specifically across GRE tunnel interfaces. "
                    "The limitation is native IPsec crypto maps, not VPNs in general. DMVPN and VTI-based IPsec "
                    "also support dynamic routing protocols."
                ),
            },
            {
                "id": "c",
                "text": "Switch from IKEv1 to IKEv2, which adds native multicast support to the IPsec SA.",
                "correct": False,
                "rationale": (
                    "Incorrect. IKEv2 improves the key exchange protocol but does not add multicast support to "
                    "native IPsec crypto map tunnels. A logical tunnel interface (GRE or VTI) is still required "
                    "to carry routing protocol multicast traffic."
                ),
            },
            {
                "id": "d",
                "text": "Enable OSPF passive interfaces on both tunnel endpoints so OSPF can run without multicast.",
                "correct": False,
                "rationale": (
                    "Incorrect. OSPF passive interfaces suppress Hello packets, preventing adjacency formation entirely. "
                    "This would not allow OSPF to propagate routes across the tunnel — the opposite of the goal."
                ),
            },
        ],
        "explanation": (
            "Native IPsec (crypto map–based) encrypts specific IP traffic flows defined by ACLs and does not "
            "create a logical interface. Routing protocols like OSPF, EIGRP use multicast hellos that do not "
            "match typical IPsec ACLs, and there is no interface for OSPF to bind to. "
            "GRE over IPsec: GRE creates a 'tunnel 0' logical interface (OSPF-capable), "
            "IPsec protects all GRE traffic with encryption/integrity. "
            "Modern alternative: IPsec Virtual Tunnel Interface (VTI) also provides a routable interface without GRE overhead."
        ),
    },
    # ── cd5v3-026 ── Security concepts: phishing vs spear phishing ────────────
    {
        "id": "cd5v3-026",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An attacker researches a specific CFO's name, bank, and recent business trips on social media, "
            "then sends a targeted email impersonating the CFO's bank, containing a malicious link. "
            "A separate campaign sends the same generic fake bank email to 500,000 random addresses. "
            "Which terms BEST describe these two attack techniques, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spear phishing (targeted CFO attack); phishing (mass email campaign).",
                "correct": True,
                "rationale": (
                    "Correct. Spear phishing is a highly targeted phishing attack tailored to a specific individual "
                    "using personal research. Generic mass phishing sends identical lures to large, undifferentiated "
                    "recipient lists without personalization."
                ),
            },
            {
                "id": "b",
                "text": "Whaling (targeted CFO attack); spear phishing (mass email campaign).",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling is a specific subtype of spear phishing targeting senior executives (C-suite). "
                    "The mass campaign is generic phishing, not spear phishing — spear phishing implies targeted personalization."
                ),
            },
            {
                "id": "c",
                "text": "Vishing (targeted CFO attack); phishing (mass email campaign).",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing (voice phishing) uses telephone calls, not email. "
                    "The CFO attack is conducted via targeted email, making it spear phishing."
                ),
            },
            {
                "id": "d",
                "text": "Pretexting (targeted CFO attack); smishing (mass email campaign).",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting involves fabricating a false scenario (it can be part of the spear phishing "
                    "approach but is not the attack name). Smishing uses SMS text messages, not email."
                ),
            },
        ],
        "explanation": (
            "Social engineering taxonomy: Phishing = mass undirected email lure. "
            "Spear phishing = targeted, personalized phishing at a specific individual or group. "
            "Whaling = spear phishing targeting executives/VIPs. Vishing = voice/phone phishing. "
            "Smishing = SMS phishing. Pretexting = creating a fabricated scenario to manipulate targets. "
            "Defenses: security awareness training, email filtering (SPF/DKIM/DMARC), URL inspection, MFA."
        ),
    },
    # ── cd5v3-027 ── Security concepts: man-in-the-middle ────────────────────
    {
        "id": "cd5v3-027",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An attacker on a switched LAN sends unsolicited ARP replies to Host A claiming that "
            "the default gateway's IP (192.168.1.1) maps to the attacker's MAC address. "
            "Host A updates its ARP cache. The attacker also sends a spoofed ARP reply to the gateway "
            "claiming Host A's IP maps to the attacker's MAC. "
            "What attack is described and what is its primary goal?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ARP poisoning / man-in-the-middle attack; the attacker intercepts traffic between Host A and the gateway by positioning itself in the forwarding path.",
                "correct": True,
                "rationale": (
                    "Correct. By poisoning both endpoints' ARP caches to map each other's IPs to the attacker's MAC, "
                    "all traffic between Host A and the gateway is forwarded through the attacker, who can inspect, "
                    "modify, or drop it — a classic Layer 2 man-in-the-middle attack."
                ),
            },
            {
                "id": "b",
                "text": "MAC flooding attack; the attacker fills the switch CAM table to cause the switch to broadcast all frames.",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding injects thousands of fake source MACs to overflow the CAM table. "
                    "The scenario describes targeted gratuitous ARP replies to specific hosts — ARP poisoning."
                ),
            },
            {
                "id": "c",
                "text": "DHCP starvation attack; the attacker exhausts the DHCP pool so legitimate hosts cannot obtain IP addresses.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP starvation uses spoofed DHCP DISCOVER messages with different client-IDs "
                    "to exhaust the IP address pool. The scenario describes ARP manipulation, not DHCP."
                ),
            },
            {
                "id": "d",
                "text": "IP spoofing attack; the attacker impersonates Host A's source IP to gain unauthorized access to the gateway.",
                "correct": False,
                "rationale": (
                    "Incorrect. IP spoofing forges the source IP address in IP packets. The scenario describes "
                    "ARP cache poisoning at Layer 2, which is different from IP-layer source address forgery."
                ),
            },
        ],
        "explanation": (
            "ARP poisoning exploits the stateless, unauthenticated nature of ARP. By sending gratuitous ARP replies, "
            "an attacker maps a victim's IP to their own MAC in the victim's ARP cache. "
            "Mitigations: Dynamic ARP Inspection (DAI) on Cisco switches validates ARP against DHCP snooping "
            "bindings; static ARP entries; 802.1X port authentication; encryption (TLS) to protect data even "
            "if intercepted. DAI is the primary Layer 2 control for ARP poisoning on Cisco platforms."
        ),
    },
    # ── cd5v3-028 ── Security program elements: defense in depth ─────────────
    {
        "id": "cd5v3-028",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security program elements",
        "stem": (
            "A security architect proposes layering the following controls: firewall at the perimeter, "
            "IPS on the core switches, endpoint antivirus on workstations, and ACLs on distribution routers. "
            "Which security principle does this strategy represent, and why is it effective?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Defense in depth; multiple independent control layers ensure that if one layer is bypassed or fails, other layers can still detect or block the attack.",
                "correct": True,
                "rationale": (
                    "Correct. Defense in depth (layered security) deploys multiple overlapping controls so that "
                    "no single failure or bypass defeats all protections. An attacker who bypasses the firewall "
                    "still faces IPS, ACLs, and endpoint AV — each providing an independent opportunity to detect "
                    "or block the threat."
                ),
            },
            {
                "id": "b",
                "text": "Least privilege; each control limits user access to only necessary resources.",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege is the principle of granting only the minimum permissions needed "
                    "for a task. The scenario describes layered security technologies, not permission restriction."
                ),
            },
            {
                "id": "c",
                "text": "Separation of duties; different teams manage each security layer to prevent insider fraud.",
                "correct": False,
                "rationale": (
                    "Incorrect. Separation of duties is an organizational/access control principle requiring "
                    "multiple people to complete sensitive tasks. The layered technical controls described "
                    "represent defense in depth."
                ),
            },
            {
                "id": "d",
                "text": "Security through obscurity; hiding the network topology makes it harder for attackers to identify targets.",
                "correct": False,
                "rationale": (
                    "Incorrect. Security through obscurity relies on hiding information as the primary defense. "
                    "Defense in depth uses known, independently effective controls — it does not rely on secrecy "
                    "of the security mechanisms themselves."
                ),
            },
        ],
        "explanation": (
            "Defense in depth (also called layered security) is a foundational cybersecurity principle: "
            "deploy multiple security controls so an attacker must bypass all of them. "
            "CCNA-relevant layers: perimeter (firewall, ACLs), network (IPS, VLAN segmentation), "
            "endpoint (antivirus, host firewall), data (encryption, DLP), identity (AAA, MFA). "
            "No single control is foolproof; overlapping independent layers raise the cost and complexity of attacks."
        ),
    },
    # ── cd5v3-029 ── Security program elements: incident response ─────────────
    {
        "id": "cd5v3-029",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security program elements",
        "stem": (
            "During a security incident, a network administrator discovers that a worm is spreading "
            "across the internal LAN. The worm is actively exploiting an unpatched SMB vulnerability. "
            "Ordering the response steps below, which is the FIRST action the administrator should take "
            "according to standard incident response procedures?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Contain the spread by isolating infected segments — for example, blocking SMB ports (TCP 445) at distribution switches using ACLs.",
                "correct": True,
                "rationale": (
                    "Correct. The standard NIST/SANS incident response lifecycle is: Preparation → Identification → "
                    "Containment → Eradication → Recovery → Lessons Learned. After identifying the incident, "
                    "the FIRST active response step is containment — limiting the blast radius before eradication."
                ),
            },
            {
                "id": "b",
                "text": "Eradicate the worm by immediately patching all systems with the SMB security update.",
                "correct": False,
                "rationale": (
                    "Incorrect. Patching (eradication) comes AFTER containment. Attempting to patch while the worm "
                    "is still spreading is ineffective; the worm can re-infect systems faster than patches are applied. "
                    "Containment must limit the spread first."
                ),
            },
            {
                "id": "c",
                "text": "Perform a post-incident lessons-learned review to document how the worm entered the network.",
                "correct": False,
                "rationale": (
                    "Incorrect. Lessons learned is the FINAL phase, conducted after full recovery. "
                    "During an active incident, the immediate priority is containment."
                ),
            },
            {
                "id": "d",
                "text": "Restore all infected systems from backup to achieve the fastest recovery.",
                "correct": False,
                "rationale": (
                    "Incorrect. Recovery (restoring from backup) comes after eradication and confirmation that the "
                    "threat is removed. Restoring while the worm is still spreading and the vulnerability is unpatched "
                    "would result in immediate re-infection."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-61 Incident Response Phases: (1) Preparation, (2) Detection & Analysis, "
            "(3) Containment → (4) Eradication → (5) Recovery → (6) Post-Incident Activity. "
            "Containment strategies: network segmentation, ACL blocks, VLAN isolation, shutdown of infected ports. "
            "The goal is to stop lateral movement before attempting eradication or recovery."
        ),
    },
    # ── cd5v3-030 ── Password policies & MFA: TOTP vs HOTP ───────────────────
    {
        "id": "cd5v3-030",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Password policies & MFA",
        "stem": (
            "A company implements two-factor authentication using a software token app that generates "
            "a new 6-digit code every 30 seconds based on the current time and a shared secret. "
            "A help desk ticket reports that a user's token codes are rejected even though they appear correct. "
            "The user's phone clock is 3 minutes ahead. What is the MOST likely cause and fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The OTP system uses TOTP (time-based OTP); the authentication server rejects codes outside its allowed time window. The fix is to synchronize the user's phone clock via NTP.",
                "correct": True,
                "rationale": (
                    "Correct. TOTP (RFC 6238) generates codes from HMAC(shared-secret, current-time/30). "
                    "If the client clock is off by more than the server's tolerance window (typically ±1 to ±2 "
                    "time steps = 30–90 seconds), codes appear valid on the phone but are rejected by the server. "
                    "NTP synchronization resolves clock skew."
                ),
            },
            {
                "id": "b",
                "text": "The OTP system uses HOTP (counter-based OTP); the user's counter is out of sync. Re-enrolling the token resets the counter.",
                "correct": False,
                "rationale": (
                    "Incorrect. HOTP (RFC 4226) is counter-based and not affected by clock skew. "
                    "The scenario's 30-second rotation interval specifically identifies TOTP, "
                    "and the 3-minute clock difference explains the rejection."
                ),
            },
            {
                "id": "c",
                "text": "The shared secret has been compromised; the attacker is consuming the OTP codes before the user can use them.",
                "correct": False,
                "rationale": (
                    "Incorrect. If an attacker were consuming codes, the symptom would be intermittent or specific "
                    "failures, not systematic rejection. A 3-minute clock skew causing all codes to be rejected "
                    "is a much more likely and simpler explanation."
                ),
            },
            {
                "id": "d",
                "text": "The RADIUS server's UDP port 1813 is blocked, preventing accounting records from being sent and causing authentication to fail.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS port 1813 is for accounting, not authentication. Authentication uses UDP 1812. "
                    "More fundamentally, blocked accounting does not cause authentication failures in standard RADIUS implementations."
                ),
            },
        ],
        "explanation": (
            "TOTP (Time-based OTP, RFC 6238) = HOTP with time as the moving factor. OTP = HMAC-SHA1(key, T) "
            "where T = floor(current_unix_time / 30). Clock synchronization is critical — typical servers allow "
            "±1 time step (30s tolerance). A 3-minute skew (6 time steps) exceeds this window. "
            "HOTP (Counter-based, RFC 4226) is not time-sensitive but can desync if the user generates codes "
            "without using them. Both use a shared secret provisioned via QR code during enrollment."
        ),
    },
    # ── cd5v3-031 ── Password policies & MFA: password complexity ─────────────
    {
        "id": "cd5v3-031",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Password policies & MFA",
        "stem": (
            "A company enforces password complexity: minimum 8 characters, requiring uppercase, "
            "lowercase, numbers, and special characters. An auditor flags that the policy is insufficient "
            "against modern brute-force attacks and recommends a change. "
            "Which recommendation provides the GREATEST improvement to password security?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Increase minimum password length to 16+ characters (passphrases), as length has exponentially greater impact on search space than complexity rules alone.",
                "correct": True,
                "rationale": (
                    "Correct. Each additional character multiplies the search space by the character set size. "
                    "An 8-character complex password has ~6.6×10^15 combinations. A 16-character passphrase "
                    "from a ~26-character set has ~4.4×10^22 combinations — far more than adding one more "
                    "complexity requirement to 8-character passwords. NIST SP 800-63B recommends length over complexity."
                ),
            },
            {
                "id": "b",
                "text": "Require users to change passwords every 30 days, reducing the window an attacker has to use a stolen credential.",
                "correct": False,
                "rationale": (
                    "Incorrect. Frequent mandatory rotation encourages weaker passwords (users make predictable "
                    "incremental changes). NIST SP 800-63B specifically recommends AGAINST mandatory periodic rotation "
                    "unless there is evidence of compromise. Rotation does not address brute-force resistance."
                ),
            },
            {
                "id": "c",
                "text": "Enforce four character classes (upper, lower, number, symbol) with a minimum of 8 characters, which provides sufficient entropy.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the existing policy. 8-character passwords, even with full complexity, "
                    "can be cracked by modern GPU clusters in hours. Increasing length to 16+ is far more effective "
                    "than enforcing additional complexity on short passwords."
                ),
            },
            {
                "id": "d",
                "text": "Store passwords using MD5 hashing with a static salt, which is computationally irreversible.",
                "correct": False,
                "rationale": (
                    "Incorrect. MD5 is a fast hash — attackers can compute billions of MD5 hashes per second on GPUs. "
                    "Password storage should use slow adaptive hashing (bcrypt, scrypt, Argon2, PBKDF2). "
                    "Also, a static salt does not prevent attacks on multiple users' passwords simultaneously."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-63B key guidance: Prioritize password LENGTH over complexity rules. "
            "Entropy scales exponentially with length but only linearly with added complexity categories. "
            "NIST also recommends: check against known-breached password lists, allow all printable ASCII/Unicode, "
            "do NOT force arbitrary complexity rules or periodic rotation without compromise evidence, "
            "DO implement account lockout and MFA. For infrastructure devices, use passphrases or certificate auth."
        ),
    },
    # ── cd5v3-032 ── Multiple response: ACL best practices ────────────────────
    {
        "id": "cd5v3-032",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "Select TWO statements that are TRUE about extended ACLs on Cisco IOS routers."
        ),
        "options": [
            {
                "id": "a",
                "text": "Extended ACLs filter traffic based on source IP, destination IP, protocol, and optionally source and destination port numbers.",
                "correct": True,
                "rationale": (
                    "Correct. Extended ACLs (numbered 100–199, 2000–2699, or named) can match on Layer 3 (src/dst IP) "
                    "and Layer 4 (TCP/UDP port numbers, ICMP types) fields, allowing precise traffic filtering."
                ),
            },
            {
                "id": "b",
                "text": "Extended ACLs should be placed as close to the destination as possible to conserve bandwidth.",
                "correct": False,
                "rationale": (
                    "Incorrect. Extended ACLs should be placed as close to the SOURCE as possible. Because extended "
                    "ACLs can specify both source and destination, placing them near the source drops unwanted traffic "
                    "early, conserving bandwidth on intermediate links."
                ),
            },
            {
                "id": "c",
                "text": "The 'eq' keyword in an extended ACL matches traffic with a port number equal to the specified value.",
                "correct": True,
                "rationale": (
                    "Correct. Port comparison operators in extended ACLs: 'eq' (equal), 'neq' (not equal), "
                    "'lt' (less than), 'gt' (greater than), 'range' (inclusive range). "
                    "'eq 80' matches only TCP/UDP port 80; 'range 1024 65535' matches all ephemeral ports."
                ),
            },
            {
                "id": "d",
                "text": "Extended ACLs can only be applied in the inbound direction on router interfaces.",
                "correct": False,
                "rationale": (
                    "Incorrect. Extended ACLs can be applied in both inbound and outbound directions on any router "
                    "interface, as well as on VTY lines (access-class) and in other contexts. "
                    "Direction restrictions are not a property of extended vs. standard ACLs."
                ),
            },
        ],
        "explanation": (
            "Extended ACL characteristics: source IP + destination IP + protocol (IP, TCP, UDP, ICMP, OSPF, etc.) "
            "+ L4 port operators (eq, neq, lt, gt, range). Numbered range: 100–199 (original), 2000–2699 (expanded). "
            "Placement: close to SOURCE. Extended ACLs can use 'established' keyword for return TCP traffic. "
            "Named extended ACLs support per-entry sequence number editing."
        ),
    },
    # ── cd5v3-033 ── Multiple response: DHCP snooping key facts ──────────────
    {
        "id": "cd5v3-033",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "Select TWO TRUE statements about DHCP snooping on Cisco Catalyst switches."
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP snooping builds a binding table mapping client MAC addresses to their leased IP addresses, VLAN, and switch port.",
                "correct": True,
                "rationale": (
                    "Correct. The DHCP snooping binding table (viewable with 'show ip dhcp snooping binding') stores "
                    "{MAC, IP, VLAN, interface, lease expiry} tuples derived from DHCP ACK messages on trusted ports. "
                    "This table is also consumed by DAI for ARP validation."
                ),
            },
            {
                "id": "b",
                "text": "DHCP snooping drops DHCP DISCOVER messages received on trusted ports to prevent server spoofing.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP DISCOVER is a client-originated message. It is permitted on BOTH trusted and "
                    "untrusted ports. DHCP snooping drops server-originated messages (OFFER, ACK, NAK) received "
                    "on UNTRUSTED ports, not client messages on trusted ports."
                ),
            },
            {
                "id": "c",
                "text": "The 'ip dhcp snooping limit rate' command can cause a port to be err-disabled if the DHCP packet rate exceeds the configured threshold.",
                "correct": True,
                "rationale": (
                    "Correct. 'ip dhcp snooping limit rate <pps>' sets a per-port rate limit for DHCP packets. "
                    "If the rate is exceeded (e.g., during a DHCP starvation attack), the port is err-disabled. "
                    "This protects the switch CPU from DHCP flood attacks."
                ),
            },
            {
                "id": "d",
                "text": "DHCP snooping must be enabled on each VLAN using 'ip dhcp snooping vlan' before the global 'ip dhcp snooping' command takes effect.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both commands are required, but the global 'ip dhcp snooping' command must be "
                    "configured AND DHCP snooping must be enabled on the specific VLAN with 'ip dhcp snooping vlan <id>'. "
                    "The VLAN command does not take precedence over the global command — both are needed. "
                    "The sequence does not strictly matter, but the global command is typically shown first."
                ),
            },
        ],
        "explanation": (
            "DHCP snooping configuration summary: (1) 'ip dhcp snooping' (global enable). "
            "(2) 'ip dhcp snooping vlan <id>' (per-VLAN enable). "
            "(3) 'ip dhcp snooping trust' on uplinks to legitimate DHCP servers. "
            "(4) Optionally: 'ip dhcp snooping limit rate <pps>' on access ports to prevent DoS. "
            "The binding table is used by DAI, IP Source Guard, and can be viewed with 'show ip dhcp snooping binding'."
        ),
    },
    # ── cd5v3-034 ── Multiple response: AAA protocol comparison ──────────────
    {
        "id": "cd5v3-034",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "Select TWO statements that are TRUE when comparing RADIUS and TACACS+ for network AAA."
        ),
        "options": [
            {
                "id": "a",
                "text": "RADIUS combines authentication and authorization into a single Access-Request/Access-Accept exchange, while TACACS+ uses separate exchanges for each AAA function.",
                "correct": True,
                "rationale": (
                    "Correct. RADIUS sends authentication credentials in Access-Request; the server returns "
                    "authorization attributes (AVPs) in the Access-Accept. TACACS+ has distinct exchanges for "
                    "authentication, authorization (each command), and accounting."
                ),
            },
            {
                "id": "b",
                "text": "Both RADIUS and TACACS+ use TCP for reliable, ordered delivery of all AAA messages.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS uses UDP (ports 1812/1813). TCP is used only by TACACS+ (port 49). "
                    "RADIUS handles reliability at the application layer (retransmit timers)."
                ),
            },
            {
                "id": "c",
                "text": "RADIUS is the required AAA protocol for IEEE 802.1X port-based network access control.",
                "correct": True,
                "rationale": (
                    "Correct. IEEE 802.1X defines EAP over LAN (EAPOL). The authenticator (switch/AP) "
                    "communicates with the authentication server using RADIUS (EAP carried in RADIUS Access-Request "
                    "attributes). TACACS+ is not used in 802.1X implementations."
                ),
            },
            {
                "id": "d",
                "text": "TACACS+ encrypts only the password field to comply with GDPR data minimization requirements.",
                "correct": False,
                "rationale": (
                    "Incorrect. It is RADIUS that encrypts only the password (User-Password attribute). "
                    "TACACS+ encrypts the entire packet body (excluding the fixed header). "
                    "Neither protocol's encryption design is specifically tied to GDPR."
                ),
            },
        ],
        "explanation": (
            "RADIUS: UDP 1812/1813, encrypts only password, combines auth+authz, used for network access (802.1X, VPN). "
            "TACACS+: TCP 49, encrypts full packet body, separates auth/authz/acct, used for device administration. "
            "Both use a shared secret for integrity/confidentiality. RADIUS supports VSAs (Vendor Specific Attributes) "
            "for extensibility. TACACS+ supports per-command authorization natively, critical for IOS device management."
        ),
    },
    # ── cd5v3-035 ── Multiple response: IPsec components ─────────────────────
    {
        "id": "cd5v3-035",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "IPsec VPNs",
        "stem": (
            "Select TWO TRUE statements about IPsec protocols and their security services."
        ),
        "options": [
            {
                "id": "a",
                "text": "ESP (Encapsulating Security Payload) provides confidentiality, integrity, authentication, and anti-replay protection.",
                "correct": True,
                "rationale": (
                    "Correct. ESP (IP protocol 50) provides the full suite: encryption (confidentiality), "
                    "HMAC integrity, peer authentication, and a sequence number for anti-replay protection. "
                    "It is the preferred IPsec protocol when data confidentiality is required."
                ),
            },
            {
                "id": "b",
                "text": "AH (Authentication Header) provides confidentiality by encrypting the IP payload.",
                "correct": False,
                "rationale": (
                    "Incorrect. AH (IP protocol 51) provides integrity, authentication, and anti-replay protection "
                    "but does NOT provide confidentiality (no encryption). AH is also incompatible with NAT "
                    "because it includes the outer IP header in its integrity check."
                ),
            },
            {
                "id": "c",
                "text": "IKE Phase 1 establishes the ISAKMP SA used to protect IKE Phase 2 negotiations.",
                "correct": True,
                "rationale": (
                    "Correct. IKE Phase 1 creates a secure, authenticated, encrypted channel (the ISAKMP SA or IKE SA) "
                    "using DH key exchange. This channel is then used to negotiate the IPsec SA parameters (Phase 2). "
                    "Phase 2 would be insecure without the Phase 1 protection."
                ),
            },
            {
                "id": "d",
                "text": "In IPsec transport mode, a new outer IP header is added to hide the original source and destination addresses.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a new outer IP header is the defining characteristic of TUNNEL mode, "
                    "not transport mode. Transport mode preserves the original IP header and only protects "
                    "(encrypts/authenticates) the IP payload."
                ),
            },
        ],
        "explanation": (
            "IPsec protocol summary: AH (protocol 51) = integrity + auth + anti-replay, no encryption, NAT-incompatible. "
            "ESP (protocol 50) = encryption + integrity + auth + anti-replay, NAT-compatible (ESP-UDP encapsulation for NAT-T). "
            "Modes: Tunnel = new outer IP header + full encapsulation (site-to-site VPN). "
            "Transport = original IP header preserved (host-to-host). "
            "IKE creates keying material; Phase 1 = ISAKMP SA (control channel), Phase 2 = IPsec SA (data plane)."
        ),
    },
    # ── cd5v3-036 ── Multiple response: port security configuration ────────────
    {
        "id": "cd5v3-036",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Port security",
        "stem": (
            "Select TWO TRUE statements about sticky MAC address learning on Cisco Catalyst switches."
        ),
        "options": [
            {
                "id": "a",
                "text": "Sticky MAC addresses are stored in the running configuration and can be saved to startup-config to persist across reboots.",
                "correct": True,
                "rationale": (
                    "Correct. When sticky learning is enabled ('switchport port-security mac-address sticky'), "
                    "dynamically learned MACs are converted to static sticky entries and written to the running-config. "
                    "Issuing 'copy running-config startup-config' (or 'write memory') saves them across reboots."
                ),
            },
            {
                "id": "b",
                "text": "Sticky MAC learning requires the 'switchport port-security maximum' to be set to at least 10 before it can be enabled.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no minimum maximum value required to enable sticky learning. "
                    "Sticky learning works with any configured maximum (including the default of 1). "
                    "The maximum only limits how many MACs can be learned."
                ),
            },
            {
                "id": "c",
                "text": "Disabling port security on an interface with sticky MACs removes all sticky MAC entries from the running configuration for that interface.",
                "correct": True,
                "rationale": (
                    "Correct. Issuing 'no switchport port-security' on an interface clears all port security "
                    "configuration for that interface, including sticky MAC entries, from the running configuration. "
                    "This is a key consideration before removing port security from a production port."
                ),
            },
            {
                "id": "d",
                "text": "Sticky MAC addresses are learned only from DHCP ACK messages, not from frame source addresses.",
                "correct": False,
                "rationale": (
                    "Incorrect. Sticky MACs are learned from the source MAC address of frames arriving on the port "
                    "— exactly like normal dynamic MAC learning. DHCP is not involved in sticky MAC learning. "
                    "DHCP snooping is a separate feature."
                ),
            },
        ],
        "explanation": (
            "Sticky MAC learning combines the convenience of dynamic learning with the persistence of static configuration. "
            "As frames arrive, source MACs are learned and written as 'switchport port-security mac-address sticky "
            "<mac> vlan <id>' entries in running-config. To persist: 'write memory'. "
            "To clear without disabling port security: 'clear port-security sticky interface <intf>'. "
            "Disabling port security ('no switchport port-security') removes ALL port security settings including sticky MACs."
        ),
    },
    # ── cd5v3-037 ── Security concepts: vulnerability vs risk vs threat ────────
    {
        "id": "cd5v3-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An organization's web server runs an unpatched version of Apache with a known RCE "
            "vulnerability (CVE-2023-XXXX). The server is internet-facing. No exploit has yet occurred. "
            "A risk assessment rates this as 'Critical'. "
            "Which statement CORRECTLY maps the scenario elements to security terminology?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The unpatched Apache flaw is the vulnerability; remote attackers who could exploit it represent the threat; the likelihood × potential impact of exploitation is the risk.",
                "correct": True,
                "rationale": (
                    "Correct. Vulnerability = the weakness (unpatched CVE). Threat = the agent/event that could "
                    "exploit it (remote attackers). Risk = the combination of threat likelihood and potential impact. "
                    "A critical risk rating reflects high likelihood and severe impact."
                ),
            },
            {
                "id": "b",
                "text": "The CVE is the threat; the internet-facing exposure is the vulnerability; 'Critical' is the exploit.",
                "correct": False,
                "rationale": (
                    "Incorrect. A CVE identifies and describes a specific vulnerability, not a threat. "
                    "The internet-facing exposure is an element that increases risk (attack surface), "
                    "not the vulnerability itself. 'Critical' is a risk rating, not an exploit."
                ),
            },
            {
                "id": "c",
                "text": "The unpatched flaw is the risk; the 'Critical' rating is the vulnerability; remote attackers are the exposure.",
                "correct": False,
                "rationale": (
                    "Incorrect. The unpatched flaw is a vulnerability (a weakness), not a risk. "
                    "The 'Critical' rating describes the level of risk. Exposure refers to the attack surface, "
                    "not the threat actor."
                ),
            },
            {
                "id": "d",
                "text": "Remote attackers are the vulnerability; the unpatched flaw is the exposure; the CVE number is the threat.",
                "correct": False,
                "rationale": (
                    "Incorrect. Attackers are threat agents. The unpatched flaw is the vulnerability. "
                    "A CVE number is simply an identifier for the vulnerability — it is not itself a threat."
                ),
            },
        ],
        "explanation": (
            "Core security terminology: Vulnerability = a weakness in a system (software bug, misconfiguration). "
            "Threat = a potential cause of harm (attacker, natural disaster, malware). "
            "Threat Agent = the entity that exploits a vulnerability (hacker, script kiddie, insider). "
            "Risk = Probability of threat exploiting vulnerability × Impact of successful exploit. "
            "Exploit = the technique or code used to take advantage of a vulnerability. "
            "Mitigation (control) = action that reduces vulnerability, likelihood, or impact."
        ),
    },
    # ── cd5v3-038 ── Security concepts: DoS vs DDoS ───────────────────────────
    {
        "id": "cd5v3-038",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An organization's DNS server receives 50 million UDP packets per second sourced from "
            "thousands of different IP addresses across the globe, overwhelming the server and its "
            "upstream bandwidth. Some source IPs belong to home routers running default credentials "
            "that were compromised months earlier. "
            "Which attack type BEST describes this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Distributed Denial-of-Service (DDoS) using a botnet; mitigated upstream using blackhole routing, scrubbing centers, or anycast-based DDoS mitigation services.",
                "correct": True,
                "rationale": (
                    "Correct. Traffic from thousands of different source IPs (compromised home routers forming a botnet) "
                    "targeting a single victim is a DDoS attack. Mitigations include remotely triggered blackhole "
                    "routing (RTBH), cloud-based scrubbing services (e.g., Cloudflare, Akamai), and BGP anycast."
                ),
            },
            {
                "id": "b",
                "text": "DoS SYN flood from a single attacker; mitigated with TCP SYN cookies on the DNS server.",
                "correct": False,
                "rationale": (
                    "Incorrect. The traffic originates from thousands of different IPs — not a single source. "
                    "This is a distributed attack (DDoS). Also, SYN flood is TCP-specific; the scenario uses UDP. "
                    "TCP SYN cookies would be irrelevant against UDP floods."
                ),
            },
            {
                "id": "c",
                "text": "Smurf attack; mitigated by disabling IP-directed broadcasts on all routers.",
                "correct": False,
                "rationale": (
                    "Incorrect. A Smurf attack uses ICMP echo requests sent to a broadcast address with a spoofed "
                    "victim source IP. The described attack uses UDP traffic directly targeting the DNS server — "
                    "likely a UDP amplification DDoS (potentially DNS reflection), not a Smurf attack."
                ),
            },
            {
                "id": "d",
                "text": "DNS cache poisoning attack; mitigated by enabling DNSSEC on the DNS server.",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS cache poisoning inserts malicious records into a resolver's cache to redirect clients. "
                    "The described attack is volumetric — millions of UDP packets per second causing availability loss — "
                    "not an attempt to corrupt DNS data. This is a DDoS, not a cache poisoning attack."
                ),
            },
        ],
        "explanation": (
            "DoS = single-source attack targeting availability. DDoS = distributed multi-source attack (botnet). "
            "The compromised home routers form a botnet (C2-controlled zombie devices). "
            "UDP-based DDoS types: UDP flood (random ports), DNS amplification (small queries → large responses), "
            "NTP amplification (monlist command), SSDP amplification. "
            "Mitigations: RTBH (null-route at upstream ISP), flowspec BGP policies, rate-limiting at network edge, "
            "scrubbing service. On-premises mitigations alone are ineffective once bandwidth is saturated."
        ),
    },
    # ── cd5v3-039 ── ACL wildcard: /23 summarization ──────────────────────────
    {
        "id": "cd5v3-039",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "An engineer must write a single extended ACL entry that denies all TCP traffic from "
            "the 10.20.10.0/23 subnet to any destination. Which ACL entry is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "access-list 110 deny tcp 10.20.10.0 0.0.1.255 any",
                "correct": True,
                "rationale": (
                    "Correct. A /23 subnet mask is 255.255.254.0. Inverting: 255-254=1 in the third octet, "
                    "255-0=255 in the fourth → wildcard 0.0.1.255. This matches 10.20.10.0–10.20.11.255 (512 hosts), "
                    "exactly the /23 range starting at 10.20.10.0."
                ),
            },
            {
                "id": "b",
                "text": "access-list 110 deny tcp 10.20.10.0 0.0.0.255 any",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.0.255 is the inverse of /24 (255.255.255.0), covering only "
                    "10.20.10.0–10.20.10.255. It does not include the second half of the /23 range "
                    "(10.20.11.0–10.20.11.255)."
                ),
            },
            {
                "id": "c",
                "text": "access-list 110 deny tcp 10.20.10.0 0.0.3.255 any",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.3.255 is the inverse of /22 (255.255.252.0), matching "
                    "10.20.8.0–10.20.11.255 — a /22 block of 1024 addresses, which is twice the intended /23 range "
                    "and includes 10.20.8.x and 10.20.9.x which are not in the intended subnet."
                ),
            },
            {
                "id": "d",
                "text": "access-list 110 deny tcp 10.20.0.0 0.0.1.255 any",
                "correct": False,
                "rationale": (
                    "Incorrect. Although the wildcard mask 0.0.1.255 is correct for a /23, the network address "
                    "10.20.0.0 with this wildcard matches 10.20.0.0–10.20.1.255 — a different /23 block, "
                    "not the intended 10.20.10.0–10.20.11.255."
                ),
            },
        ],
        "explanation": (
            "For 10.20.10.0/23: subnet mask = 255.255.254.0, wildcard = 0.0.1.255. "
            "The /23 block 10.20.10.0/23 spans 10.20.10.0–10.20.11.255 (512 addresses). "
            "Common mistake: using wildcard 0.0.1.255 with the wrong network base address. "
            "Always verify the base address is the actual network address of the /23 block "
            "(the third octet's least-significant bit must be 0 — 10.20.10.x has bit-0=0, so 10.20.10.0 is correct)."
        ),
    },
    # ── cd5v3-040 ── Security program elements: security policy types ─────────
    {
        "id": "cd5v3-040",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security program elements",
        "stem": (
            "A company's acceptable use policy (AUP) prohibits employees from using corporate laptops "
            "for personal social media. An HR manager asks the security team to technically enforce "
            "this policy. Which solution BEST enforces the AUP at the network level for users on the "
            "corporate network?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy a web content filtering proxy or DNS-based filtering service that blocks social media URLs/domains for corporate devices on the internal network.",
                "correct": True,
                "rationale": (
                    "Correct. Web content filtering (URL/category blocking) technically enforces the AUP by "
                    "preventing access to social media sites at the network level. This works for on-network "
                    "devices and can be applied to traffic from corporate endpoints via a proxy or DNS filtering "
                    "service (e.g., Cisco Umbrella, Zscaler)."
                ),
            },
            {
                "id": "b",
                "text": "Configure a standard ACL on the perimeter router to block TCP port 443 to all social media IP addresses.",
                "correct": False,
                "rationale": (
                    "Incorrect. Social media services use dynamic CDN IP addresses that change frequently. "
                    "Maintaining an ACL based on IP addresses is operationally infeasible. Also, a standard ACL "
                    "filters only source IP, not destination — an extended ACL would be needed, and even then "
                    "IP-based blocking for cloud services with thousands of IPs is impractical."
                ),
            },
            {
                "id": "c",
                "text": "Issue a written reminder of the AUP policy to all employees during annual security awareness training.",
                "correct": False,
                "rationale": (
                    "Incorrect. Awareness training (a detective/preventive administrative control) does not technically "
                    "enforce the policy. The question asks for a technical enforcement mechanism. Training alone "
                    "does not block access — it only informs users of the rule."
                ),
            },
            {
                "id": "d",
                "text": "Enable port security on all access switches to limit the MAC addresses allowed per port, restricting unauthorized device usage.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port security limits which physical devices can connect to a switch port based on "
                    "MAC address. It does not inspect or control web traffic destinations. "
                    "It would not prevent an authorized device from accessing social media."
                ),
            },
        ],
        "explanation": (
            "AUP technical enforcement requires Layer 7 (application-layer) controls, not Layer 2–4 controls. "
            "Web content filtering options: (1) Proxy-based (explicit or transparent) URL/category filtering. "
            "(2) DNS-based filtering (e.g., Cisco Umbrella) — block resolution of social media domains. "
            "(3) NGFW/IPS with application-layer inspection (App-ID). "
            "Administrative controls (training, policy) and Layer 2/3 controls (port security, basic ACLs) "
            "cannot enforce application-layer content policies."
        ),
    },
]
