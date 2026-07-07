QUESTIONS = [
    # ── cd4v3-001 ── NAT/PAT ────────────────────────────────────────────────
    {
        "id": "cd4v3-001",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "A router has the following NAT configuration:\n"
            "  ip nat pool CORP_POOL 203.0.113.10 203.0.113.15 netmask 255.255.255.248\n"
            "  ip nat inside source list 1 pool CORP_POOL\n"
            "  access-list 1 permit 10.0.0.0 0.0.0.255\n\n"
            "Thirty hosts on the 10.0.0.0/24 subnet simultaneously open TCP sessions to the Internet. "
            "What happens to the 25th through 30th sessions when all six pool addresses are already in use "
            "and 'overload' is NOT configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router drops the packets; new sessions are not translated until an existing NAT entry times out and frees a pool address",
                "correct": True,
                "rationale": (
                    "Correct. Without 'overload', dynamic NAT performs one-to-one address mapping. The pool "
                    "contains six addresses (.10–.15), so only six simultaneous inside-to-outside translations "
                    "can exist. When the pool is exhausted, the router drops packets from additional hosts "
                    "and logs a NAT translation failure. No new sessions are established until an existing "
                    "entry ages out (default TCP timeout 86400 s)."
                ),
            },
            {
                "id": "b",
                "text": "The router automatically enables PAT on the pool's last address to accommodate the overflow sessions",
                "correct": False,
                "rationale": (
                    "Incorrect. Without the 'overload' keyword, Cisco IOS does not automatically fall back "
                    "to PAT. Overload must be explicitly configured. Pool exhaustion causes drops, not "
                    "automatic PAT escalation."
                ),
            },
            {
                "id": "c",
                "text": "The router round-robins a sixth address to all remaining sessions, multiplexing them on the same IP",
                "correct": False,
                "rationale": (
                    "Incorrect. Round-robin or multiplexing behaviour requires PAT (overload). Basic dynamic "
                    "NAT allocates each session a distinct IP address from the pool; once exhausted, "
                    "further sessions are dropped, not multiplexed."
                ),
            },
            {
                "id": "d",
                "text": "The router translates the additional sessions using the interface IP of the outside interface as a fallback",
                "correct": False,
                "rationale": (
                    "Incorrect. Using the outside interface IP as a fallback is the behaviour of "
                    "'ip nat inside source list … interface … overload'. Without 'overload', there is no "
                    "such fallback — excess sessions are simply dropped."
                ),
            },
        ],
        "explanation": (
            "Dynamic NAT (without overload) maps each inside local address to a unique inside global address "
            "from the pool. The pool size limits the maximum number of simultaneous translated sessions. "
            "When the pool is exhausted, packets are dropped and a %IP_NAT-3-NO_ADDRESS_AVAILABLE syslog "
            "message is generated. Adding the 'overload' keyword switches to PAT, allowing thousands of "
            "concurrent sessions to share a single public IP via unique port numbers."
        ),
    },
    # ── cd4v3-002 ── NAT/PAT ────────────────────────────────────────────────
    {
        "id": "cd4v3-002",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "An engineer issues 'show ip nat translations' and observes entries like:\n"
            "  Pro  Inside global      Inside local        Outside local      Outside global\n"
            "  ---  203.0.113.5        10.1.1.20           ---                ---\n\n"
            "There are NO port numbers in any column. Which type of NAT is operating, and what does "
            "the absence of port numbers indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Static NAT or dynamic NAT without overload; the one-to-one mapping contains no port information because PAT is not in use",
                "correct": True,
                "rationale": (
                    "Correct. When port numbers are absent from the 'show ip nat translations' output, "
                    "the entry is either a static NAT entry (one-to-one, permanent) or a dynamic NAT "
                    "entry (one-to-one, temporary). PAT (overload) always shows port numbers in the "
                    "inside global column. The three-dash (---) in outside columns further indicates "
                    "this is a session-independent mapping, typical of static NAT."
                ),
            },
            {
                "id": "b",
                "text": "PAT is operating; the port numbers are hidden by default and must be revealed with 'show ip nat translations verbose'",
                "correct": False,
                "rationale": (
                    "Incorrect. PAT entries always display port numbers in the standard 'show ip nat "
                    "translations' output. There is no hidden mode; absence of ports definitively "
                    "indicates one-to-one NAT, not PAT."
                ),
            },
            {
                "id": "c",
                "text": "NAT overload is operating on ICMP traffic; ICMP uses query IDs instead of ports which are suppressed in the display",
                "correct": False,
                "rationale": (
                    "Incorrect. While ICMP PAT entries do use ICMP query IDs in place of port numbers, "
                    "they still appear in the translation table with identifiers displayed. An empty "
                    "outside column (---) indicates a static or dynamic one-to-one mapping with no active "
                    "session, not an ICMP PAT quirk."
                ),
            },
            {
                "id": "d",
                "text": "This is an outside NAT entry translating the source address of incoming packets from the Internet",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip nat outside source' entries would show addresses in the outside columns "
                    "and a different translation direction. The entry shown has an inside local and inside "
                    "global, indicating inside-source NAT."
                ),
            },
        ],
        "explanation": (
            "The 'show ip nat translations' output distinguishes NAT types by whether port numbers appear: "
            "static/dynamic one-to-one NAT shows address-only entries; PAT shows address:port pairs. "
            "Dashes (---) in the outside columns indicate no active session is associated with the entry "
            "(common for static NAT mappings that are always present). Static entries have no timeout; "
            "dynamic entries expire per the NAT translation timeout."
        ),
    },
    # ── cd4v3-003 ── NAT/PAT ────────────────────────────────────────────────
    {
        "id": "cd4v3-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "NAT/PAT",
        "stem": (
            "A branch router uses PAT to share a single public IP (198.51.100.1) for all outbound traffic. "
            "An internal host at 172.16.5.5 opens an HTTP session to 93.184.216.34:80 using source port 49152. "
            "A second host at 172.16.5.6 happens to open an HTTP session to the same destination using "
            "the same source port 49152. How does PAT distinguish the two return flows?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PAT assigns a unique inside global port to each translation; both sessions appear as 198.51.100.1 but with different source ports, so return traffic is demultiplexed by port number",
                "correct": True,
                "rationale": (
                    "Correct. This is the core mechanism of PAT. When two inside hosts use the same "
                    "source port, the router assigns distinct inside global ports — e.g., 198.51.100.1:49152 "
                    "for the first host and 198.51.100.1:49153 for the second. The NAT table maps each "
                    "inside global port back to the correct inside local address:port. Return traffic "
                    "arrives with the destination port matching the inside global entry, and the router "
                    "knows exactly which private host to forward it to."
                ),
            },
            {
                "id": "b",
                "text": "PAT cannot handle port collisions; the second session is dropped and the second host must retry with a different source port",
                "correct": False,
                "rationale": (
                    "Incorrect. PAT is specifically designed to handle port collisions. The router "
                    "automatically reassigns an available port from its range (1024–65535) when a "
                    "collision occurs. Sessions are not dropped due to port conflicts."
                ),
            },
            {
                "id": "c",
                "text": "PAT uses DSCP markings to differentiate the two flows because source ports are identical",
                "correct": False,
                "rationale": (
                    "Incorrect. DSCP is a QoS marking in the IP header and has nothing to do with NAT "
                    "demultiplexing. PAT operates entirely on IP addresses and Layer 4 port numbers."
                ),
            },
            {
                "id": "d",
                "text": "PAT allocates a unique public IP address from a secondary pool to the second host when a port conflict is detected",
                "correct": False,
                "rationale": (
                    "Incorrect. PAT is designed to operate with a single public IP address. It resolves "
                    "port conflicts by re-using the same public IP with different port numbers, not by "
                    "allocating additional public IP addresses."
                ),
            },
        ],
        "explanation": (
            "PAT (Port Address Translation / NAT overload) maintains a 5-tuple translation table: "
            "protocol, inside local IP, inside local port, inside global IP, inside global port. "
            "When port conflicts arise between inside hosts, the router selects an unused port for "
            "the inside global entry. Return traffic is matched by destination IP+port in the NAT "
            "table. PAT can support ~65,000 concurrent sessions per public IP address."
        ),
    },
    # ── cd4v3-004 ── NTP ────────────────────────────────────────────────────
    {
        "id": "cd4v3-004",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTP",
        "stem": (
            "A network engineer runs 'show ntp associations' on router R3 and sees:\n"
            "      address         ref clock     st  when  poll reach  delay  offset  disp\n"
            "  *~  10.0.0.1        .GPS.          1   64   128  377    1.2    -0.34   0.5\n"
            "   ~  10.0.0.2        10.0.0.1       2   45   128  377    2.1     0.12   0.8\n\n"
            "What does the asterisk (*) before the first entry indicate, and what is R3's stratum?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The asterisk identifies 10.0.0.1 as the currently selected (synchronized) NTP peer; R3 is stratum 2",
                "correct": True,
                "rationale": (
                    "Correct. In 'show ntp associations', the asterisk (*) marks the currently selected "
                    "synchronization source. 10.0.0.1 is a stratum 1 server (ref clock .GPS.), so R3 "
                    "synchronizes to stratum 1 and therefore becomes stratum 2 (one hop from the source). "
                    "The tilde (~) indicates a configured peer/server."
                ),
            },
            {
                "id": "b",
                "text": "The asterisk identifies 10.0.0.1 as a preferred but not yet synchronized NTP candidate; R3 stratum is unknown until synchronization completes",
                "correct": False,
                "rationale": (
                    "Incorrect. An asterisk in NTP associations output specifically means the source is "
                    "currently selected and synchronized. A '+' indicates a candidate not yet selected. "
                    "An 'x' indicates a falseticker (unreliable source)."
                ),
            },
            {
                "id": "c",
                "text": "The asterisk means R3 is acting as the NTP master for 10.0.0.1; R3 is stratum 1",
                "correct": False,
                "rationale": (
                    "Incorrect. The asterisk marks the upstream source R3 is synchronized to, not a "
                    "downstream client. R3 references 10.0.0.1 (stratum 1), making R3 stratum 2."
                ),
            },
            {
                "id": "d",
                "text": "The asterisk marks 10.0.0.1 as a falseticker that R3 has rejected; R3 actually uses 10.0.0.2 as its time source and is stratum 3",
                "correct": False,
                "rationale": (
                    "Incorrect. Falsetickers are marked with 'x' in Cisco NTP output, not '*'. "
                    "The asterisk denotes the selected and trusted time source. R3 is using 10.0.0.1, "
                    "the stratum 1 server."
                ),
            },
        ],
        "explanation": (
            "'show ntp associations' symbols: * = current synchronization source; + = candidate peer; "
            "~ = configured (statically); x = falseticker (discarded); # = too distant. "
            "R3's stratum = upstream stratum + 1. Upstream (10.0.0.1) is stratum 1 → R3 is stratum 2. "
            "The 'reach' field (octal 377 = binary 11111111) means all 8 recent polls were successful. "
            "'offset' is the time difference in milliseconds between R3 and the reference."
        ),
    },
    # ── cd4v3-005 ── NTP ────────────────────────────────────────────────────
    {
        "id": "cd4v3-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTP",
        "stem": (
            "A Cisco router is configured as a local NTP master with the command 'ntp master 7'. "
            "The organization's WAN link to the upstream NTP stratum-2 server later comes back up. "
            "Which behavior will the router exhibit regarding time synchronization?"
        ),
        "options": [
            {
                "id": "a",
                "text": "If the router also has 'ntp server <upstream>' configured, it will prefer the external stratum-2 source over its own stratum-7 local clock",
                "correct": True,
                "rationale": (
                    "Correct. NTP always prefers the source with the lowest stratum. 'ntp master 7' makes "
                    "the router's local clock a stratum-7 source. When a stratum-2 external server becomes "
                    "reachable (via 'ntp server'), NTP selects the better (lower stratum) source. The router "
                    "will synchronize to the external server and serve its clients at stratum 3, discarding "
                    "the local master configuration as the active source."
                ),
            },
            {
                "id": "b",
                "text": "The router will continue using its internal clock at stratum 7 because 'ntp master' takes precedence over 'ntp server'",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ntp master' does not take precedence over an external NTP server. NTP "
                    "selection algorithm prefers lower stratum. Stratum 2 < stratum 7, so the external "
                    "server wins the election when it becomes reachable."
                ),
            },
            {
                "id": "c",
                "text": "The router advertises itself to clients as stratum 8 because 'ntp master 7' adds 1 hop",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ntp master 7' means the router's own reference clock is at stratum 7. "
                    "The router itself is stratum 7, and its NTP clients would be stratum 8. The router "
                    "does not add 1 to the configured value for its own stratum advertisement."
                ),
            },
            {
                "id": "d",
                "text": "The router rejects the external stratum-2 server because it is already synchronized at a higher stratum",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP does not reject lower-stratum (better) sources. The algorithm actively "
                    "seeks the lowest reachable stratum. A stratum-7 local clock is inferior to a "
                    "stratum-2 external server; the external server will be selected."
                ),
            },
        ],
        "explanation": (
            "'ntp master <stratum>' configures a Cisco router as an authoritative NTP source using its "
            "internal clock. This is typically used as a fallback when no external NTP is available. "
            "The configured stratum value (1-15) tells clients how far the router is from a reference clock. "
            "When a better (lower stratum) external source is configured with 'ntp server', NTP's best-source "
            "selection algorithm will choose the external server, making the local master a standby. "
            "Verify active source with 'show ntp status' (reference IP and stratum)."
        ),
    },
    # ── cd4v3-006 ── DHCP & DNS roles ───────────────────────────────────────
    {
        "id": "cd4v3-006",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A network engineer captures DHCP traffic and observes the following exchange sequence "
            "from a client booting for the first time on the network:\n"
            "  1. Client → Broadcast: UDP src port 68, dst port 67\n"
            "  2. Server → Broadcast: UDP src port 67, dst port 68\n"
            "  3. Client → Broadcast: UDP src port 68, dst port 67\n"
            "  4. Server → Broadcast: UDP src port 67, dst port 68\n\n"
            "Which DHCP message type corresponds to message 3 in this sequence, and why is it sent as a broadcast?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP Request (DHCPREQUEST); broadcast because the client has not yet been assigned an IP and must also notify other DHCP servers that their offers were not selected",
                "correct": True,
                "rationale": (
                    "Correct. The DORA sequence is: Discover (1) → Offer (2) → Request (3) → Acknowledge (4). "
                    "The DHCPREQUEST (message 3) is broadcast for two reasons: (1) the client does not yet "
                    "have a confirmed IP address and cannot send unicast; (2) other DHCP servers that sent "
                    "offers see the broadcast and know their offers were declined, releasing the offered "
                    "addresses back to their pools. The client identifies the chosen server using DHCP "
                    "option 54 (Server Identifier)."
                ),
            },
            {
                "id": "b",
                "text": "DHCP Discover (DHCPDISCOVER); broadcast because the client is looking for any available DHCP server",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCPDISCOVER is message 1, not message 3. Message 3 in the DORA sequence "
                    "is always DHCPREQUEST, sent after the client receives one or more DHCPOFFER messages."
                ),
            },
            {
                "id": "c",
                "text": "DHCP Acknowledge (DHCPACK); broadcast because the server must inform all clients simultaneously",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCPACK is message 4, sent by the SERVER, not the client. Message 3 is "
                    "sent by the client (source port 68) — this identifies it as a client-originated message, "
                    "which is DHCPREQUEST."
                ),
            },
            {
                "id": "d",
                "text": "DHCP Inform (DHCPINFORM); broadcast to update other hosts in the subnet of the new address assignment",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCPINFORM is a special message sent by a client that already has an IP "
                    "address (e.g., statically assigned) and wants DHCP server configuration parameters "
                    "only. It is not part of the normal DORA sequence."
                ),
            },
        ],
        "explanation": (
            "DHCP DORA sequence: Discover → Offer → Request → Acknowledge. "
            "All four messages are broadcasts during initial address acquisition because the client has no IP. "
            "DHCPREQUEST serves a dual purpose: it confirms the selected offer to the winning server AND "
            "implicitly declines offers from all other servers (they observe the broadcast and see a "
            "Server Identifier in option 54 that is not their own). "
            "After receiving DHCPACK, the client performs a gratuitous ARP to check for address conflicts "
            "before fully committing to the assigned address."
        ),
    },
    # ── cd4v3-007 ── DHCP & DNS roles ───────────────────────────────────────
    {
        "id": "cd4v3-007",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A host resolves 'internal.corp.local' to 10.20.30.40 using the corporate DNS server. "
            "An hour later the same host tries to reach the same name but gets 'host not found'. "
            "The DNS server still has the record. Which DNS-related mechanism is the MOST likely cause "
            "of the failure on the host?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The DNS record's TTL expired in the host's local resolver cache and a new query to the DNS server failed due to a network outage or misconfiguration",
                "correct": True,
                "rationale": (
                    "Correct. DNS records have a TTL (Time To Live) that controls how long they are cached "
                    "by resolvers and clients. When the TTL expires, the cached record is discarded and a "
                    "new query must be sent. If the subsequent query fails (e.g., DNS server unreachable, "
                    "UDP port 53 blocked, wrong DNS server configured), the host cannot resolve the name "
                    "even though the record exists on the server. 'Host not found' with a valid server "
                    "record points to a connectivity or configuration issue on re-query."
                ),
            },
            {
                "id": "b",
                "text": "The DNS server automatically removes A records after 60 minutes as a security feature to prevent stale entries",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS servers do not automatically delete A records on a 60-minute schedule. "
                    "Records persist until manually removed or until dynamic DNS lease expiry. The TTL "
                    "controls cache lifetime on clients/resolvers, not the record's lifetime on the server."
                ),
            },
            {
                "id": "c",
                "text": "The host's ARP cache expired, preventing it from reaching the DNS server by MAC address",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP cache expiry causes a new ARP request to be sent; it does not result "
                    "in a 'host not found' DNS error. ARP re-resolution is transparent to the application "
                    "layer and happens automatically."
                ),
            },
            {
                "id": "d",
                "text": "DHCP renewed the host's IP address and reset the DNS server configuration to a public resolver that cannot resolve internal names",
                "correct": False,
                "rationale": (
                    "Incorrect. While DHCP renewal can theoretically overwrite DNS settings, this is "
                    "typically not the cause of a one-time resolution failure an hour after the first "
                    "success. The question asks for the MOST LIKELY DNS mechanism — TTL expiry combined "
                    "with a query failure is the most direct DNS-layer explanation."
                ),
            },
        ],
        "explanation": (
            "DNS TTL (Time To Live) is a field in each resource record controlling how long downstream "
            "resolvers and clients cache the record. Short TTLs (seconds to minutes) mean frequent "
            "re-queries; long TTLs reduce DNS traffic but slow propagation of record changes. "
            "When a cached entry expires, the client issues a fresh recursive query. If that query "
            "fails (server unreachable, NXDOMAIN, or timeout), the client receives a resolution error "
            "even if the record is valid on the authoritative server. Tools: 'ipconfig /displaydns' "
            "(Windows), 'nscd -g' (Linux) to view resolver cache."
        ),
    },
    # ── cd4v3-008 ── SNMP ───────────────────────────────────────────────────
    {
        "id": "cd4v3-008",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SNMP",
        "stem": (
            "A network administrator configures the following on a Cisco router:\n"
            "  snmp-server community READONLY ro\n"
            "  snmp-server community READWRITE rw\n"
            "  snmp-server host 10.1.1.100 version 2c READONLY\n\n"
            "An NMS at 10.1.1.100 attempts an SNMP Set operation using community string READWRITE "
            "to change an interface description. Which statement is TRUE?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Set operation succeeds because the READWRITE community string has rw (read-write) permission, regardless of which community is used in the snmp-server host statement",
                "correct": True,
                "rationale": (
                    "Correct. The 'snmp-server host' statement configures which community string (and thus "
                    "which permissions) is used for TRAP notifications sent from the router to the NMS. "
                    "It does NOT restrict which community strings the NMS can use when sending GET/SET "
                    "queries to the router. The NMS can use any valid community string the router knows "
                    "about. Since READWRITE is defined with 'rw', the Set operation is authorized."
                ),
            },
            {
                "id": "b",
                "text": "The Set operation fails because the snmp-server host statement binds 10.1.1.100 exclusively to the READONLY community",
                "correct": False,
                "rationale": (
                    "Incorrect. 'snmp-server host' defines the trap destination and the community string "
                    "used for traps sent TO that host. It does not restrict which community strings the "
                    "host (NMS) can use when initiating SNMP queries to the router."
                ),
            },
            {
                "id": "c",
                "text": "The Set operation fails because SNMPv2c does not support write operations; only SNMPv3 allows configuration changes",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv2c supports Set operations for write access just as SNMPv1 does. "
                    "The key difference between SNMPv2c and SNMPv3 is security (authentication/encryption), "
                    "not the availability of Set operations."
                ),
            },
            {
                "id": "d",
                "text": "The Set operation succeeds only if the NMS source IP matches the ACL bound to the READWRITE community",
                "correct": False,
                "rationale": (
                    "Incorrect. The configuration shown does not associate an ACL with the READWRITE "
                    "community (no ACL number follows 'rw'). An ACL would restrict access if configured "
                    "as 'snmp-server community READWRITE rw <acl-number>', but without one, all source "
                    "IPs are permitted for that community."
                ),
            },
        ],
        "explanation": (
            "'snmp-server host <ip> version <v> <community>' configures the TRAP destination — it tells "
            "the router where to send unsolicited notifications and which community to use in those traps. "
            "It does NOT create an access restriction preventing the NMS from using other community strings "
            "for Get/Set operations. To restrict which hosts can query the device, use "
            "'snmp-server community <string> [ro|rw] <acl>' with an ACL defining permitted source IPs. "
            "Read-only (ro) communities permit Get/GetNext/GetBulk only; read-write (rw) also permit Set."
        ),
    },
    # ── cd4v3-009 ── SNMP ───────────────────────────────────────────────────
    {
        "id": "cd4v3-009",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SNMP",
        "stem": (
            "A network operations team receives an SNMP trap from a router but cannot correlate it with "
            "the managed device because the trap source IP is the outgoing interface IP (which changes "
            "based on routing). The team wants all SNMP traps to originate from the router's loopback0 "
            "address (10.255.255.1). Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "snmp-server trap-source Loopback0",
                "correct": True,
                "rationale": (
                    "Correct. 'snmp-server trap-source <interface>' sets the source IP address used in "
                    "SNMP trap packets to the IP configured on the specified interface. Using Loopback0 "
                    "ensures a stable, consistent source IP regardless of which physical interface the "
                    "trap packet actually exits through. This is a best practice for NMS correlation."
                ),
            },
            {
                "id": "b",
                "text": "snmp-server source-interface Loopback0",
                "correct": False,
                "rationale": (
                    "Incorrect. 'snmp-server source-interface' is not a valid Cisco IOS SNMP command. "
                    "The correct syntax is 'snmp-server trap-source <interface>'. Confusing this with "
                    "other source-interface commands (e.g., for NTP or Syslog) is a common mistake."
                ),
            },
            {
                "id": "c",
                "text": "ip route 0.0.0.0 0.0.0.0 Loopback0",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a default route via Loopback0 would not change the source IP of "
                    "SNMP traps — it would only affect routing decisions. The source IP is determined by "
                    "the interface the packet exits on (or an explicit trap-source configuration)."
                ),
            },
            {
                "id": "d",
                "text": "snmp-server host 10.255.255.1 traps version 2c PUBLIC",
                "correct": False,
                "rationale": (
                    "Incorrect. This command adds a trap destination at 10.255.255.1, not a source. "
                    "The router's NMS IP is separate from the router's own loopback. This would send "
                    "traps TO 10.255.255.1, not FROM it."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS commands to control source addressing for management protocols: "
            "'snmp-server trap-source <intf>' — SNMP traps; "
            "'logging source-interface <intf>' — Syslog; "
            "'ntp source <intf>' — NTP; "
            "'ip radius source-interface <intf>' — RADIUS. "
            "Using Loopback interfaces as management sources provides stability (loopbacks are always "
            "up as long as the router is operational) and simplifies NMS configuration, ACLs, and "
            "device correlation in management tools."
        ),
    },
    # ── cd4v3-010 ── Syslog severity levels ─────────────────────────────────
    {
        "id": "cd4v3-010",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "A Cisco router generates this syslog message:\n"
            "  %SYS-2-MALLOCFAIL: Memory allocation of 65536 bytes failed from 0x...\n\n"
            "Based on the syslog message format, which severity level does this message represent, "
            "and what is its name?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Severity 2 — Critical",
                "correct": True,
                "rationale": (
                    "Correct. In the Cisco syslog message format %FACILITY-SEVERITY-MNEMONIC, the number "
                    "between the facility (SYS) and the mnemonic (MALLOCFAIL) is the severity level. "
                    "The number 2 corresponds to 'Critical' — indicating a critical condition that requires "
                    "immediate attention. Memory allocation failures at the OS level are critical because "
                    "they can cause processes to crash."
                ),
            },
            {
                "id": "b",
                "text": "Severity 2 — Alert",
                "correct": False,
                "rationale": (
                    "Incorrect. Alert is severity level 1, not 2. The eight syslog severity levels are: "
                    "0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, 5=Notice, 6=Informational, "
                    "7=Debugging. The '-2-' in the message format unambiguously means Critical."
                ),
            },
            {
                "id": "c",
                "text": "Severity 2 — Error",
                "correct": False,
                "rationale": (
                    "Incorrect. Error is severity level 3, not 2. Critical (2) is more severe than "
                    "Error (3). The lower the number, the more severe the condition."
                ),
            },
            {
                "id": "d",
                "text": "Severity 2 — Warning",
                "correct": False,
                "rationale": (
                    "Incorrect. Warning is severity level 4. The message clearly contains '-2-', "
                    "which maps to Critical in the syslog severity scale."
                ),
            },
        ],
        "explanation": (
            "Cisco syslog message format: %FACILITY-SEVERITY-MNEMONIC: description text. "
            "Severity levels 0–7: Emergency (0), Alert (1), Critical (2), Error (3), Warning (4), "
            "Notice (5), Informational (6), Debugging (7). Mnemonic: 'Every Awesome Cisco Engineer "
            "Will Need Ice-cream Daily'. Lower numbers = more severe. %SYS-2-MALLOCFAIL is a Critical "
            "(2) message indicating a memory allocation failure in the IOS operating system."
        ),
    },
    # ── cd4v3-011 ── Syslog severity levels ─────────────────────────────────
    {
        "id": "cd4v3-011",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "An engineer wants to configure a router to send syslog messages to a remote server "
            "at 10.10.10.200, but ONLY warnings, errors, critical alerts, and emergencies — "
            "not informational or debugging messages. Which command set achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "logging host 10.10.10.200\nlogging trap warnings",
                "correct": True,
                "rationale": (
                    "Correct. 'logging host 10.10.10.200' specifies the remote syslog server. "
                    "'logging trap warnings' (or equivalently 'logging trap 4') sets the severity "
                    "threshold for messages forwarded to the syslog server to level 4 (Warning), "
                    "which means levels 0 (Emergency) through 4 (Warning) are forwarded. "
                    "Levels 5 (Notice) through 7 (Debugging) are suppressed."
                ),
            },
            {
                "id": "b",
                "text": "logging host 10.10.10.200\nlogging trap notifications",
                "correct": False,
                "rationale": (
                    "Incorrect. 'notifications' is severity level 5. Setting the trap level to 5 would "
                    "also forward Notice-level (5) messages to the server, which exceeds the requirement. "
                    "The correct level is 'warnings' (4) to exclude notices and above."
                ),
            },
            {
                "id": "c",
                "text": "logging host 10.10.10.200\nlogging trap errors",
                "correct": False,
                "rationale": (
                    "Incorrect. 'errors' is severity level 3. Setting the trap level to 3 would suppress "
                    "Warning (4) messages, which the requirement specifies should be included. The correct "
                    "level is 'warnings' (4) to include warnings as well as higher severity messages."
                ),
            },
            {
                "id": "d",
                "text": "logging 10.10.10.200\nlogging trap 4 7",
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging trap' takes a single severity level as its argument, not a range. "
                    "There is no 'logging trap 4 7' syntax. The correct command is 'logging trap 4' "
                    "or 'logging trap warnings'. The 'logging' command (without 'host') is also not "
                    "the correct syntax for specifying a remote syslog server."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS syslog configuration for a remote server: "
            "(1) 'logging host <ip>' — designates the syslog server; "
            "(2) 'logging trap <level>' — sets the minimum severity forwarded (levels 0 through N are sent). "
            "Named levels: emergencies(0), alerts(1), critical(2), errors(3), warnings(4), "
            "notifications(5), informational(6), debugging(7). "
            "Separate commands for other destinations: 'logging console <level>' (console), "
            "'logging buffered <level>' (RAM buffer). All thresholds are independent."
        ),
    },
    # ── cd4v3-012 ── Syslog severity levels ─────────────────────────────────
    {
        "id": "cd4v3-012",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Syslog severity levels",
        "stem": (
            "A Cisco router is configured with:\n"
            "  logging buffered 7\n"
            "  logging console 5\n"
            "  logging trap 3\n"
            "  logging host 172.16.0.50\n\n"
            "The router generates a %LINK-3-UPDOWN error message. Which logging destinations "
            "will display or receive this message? (Select the BEST answer.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The RAM buffer, the console, and the remote syslog server will all receive the message",
                "correct": True,
                "rationale": (
                    "Correct. The message is severity 3 (Error). "
                    "'logging buffered 7' captures levels 0–7, so severity 3 is stored in the RAM buffer. "
                    "'logging console 5' captures levels 0–5, so severity 3 (< 5) is displayed on console. "
                    "'logging trap 3' captures levels 0–3, so severity 3 is forwarded to 172.16.0.50. "
                    "All three destinations have thresholds at or above level 3."
                ),
            },
            {
                "id": "b",
                "text": "Only the RAM buffer will receive the message because the console threshold is 5 and the trap threshold is 3, excluding severity 3",
                "correct": False,
                "rationale": (
                    "Incorrect. A threshold of N means levels 0 through N are captured. Both console (0–5) "
                    "and syslog trap (0–3) include severity 3. All three destinations receive this message."
                ),
            },
            {
                "id": "c",
                "text": "Only the remote syslog server will receive the message because 'logging trap 3' is the most restrictive filter",
                "correct": False,
                "rationale": (
                    "Incorrect. Each logging destination is independent. The most restrictive filter "
                    "('logging trap 3') limits what goes to the syslog server, but does not affect what "
                    "goes to the console or buffer. All three destinations capture severity 3 given their "
                    "respective thresholds."
                ),
            },
            {
                "id": "d",
                "text": "The message appears only on the console and in the RAM buffer; 'logging trap 3' excludes severity 3 messages from the syslog server",
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging trap 3' means the trap threshold is severity 3, so all messages "
                    "from severity 0 up to AND INCLUDING severity 3 are forwarded to the syslog server. "
                    "Severity 3 is not excluded — it is at the threshold boundary and is included."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS logging thresholds are inclusive upper bounds: 'logging X' sends levels 0 through X. "
            "For a severity-3 message with these thresholds: "
            "buffered=7 → 0–7 captured → YES; "
            "console=5 → 0–5 captured → YES (3 ≤ 5); "
            "trap=3 → 0–3 captured → YES (3 ≤ 3). "
            "All three destinations receive the message. A message is excluded only when its severity "
            "number is GREATER than the configured threshold (e.g., a severity-4 Warning would not "
            "be sent to the trap server configured at level 3)."
        ),
    },
    # ── cd4v3-013 ── DHCP relay (ip helper-address) ──────────────────────────
    {
        "id": "cd4v3-013",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP relay (ip helper-address)",
        "stem": (
            "A router is configured as a DHCP relay agent with 'ip helper-address 10.0.0.5' on its "
            "Gi0/0 interface (IP: 172.16.10.1/24). The DHCP server at 10.0.0.5 has a pool for "
            "172.16.10.0/24. After the relay is configured, clients still do not receive addresses. "
            "A packet capture shows the relayed DISCOVER arriving at 10.0.0.5 with giaddr 172.16.10.1. "
            "The server has no exclusions. Which is the MOST likely cause of the failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The DHCP server does not have a route back to 172.16.10.0/24; DHCP Offer packets cannot be delivered to the relay agent",
                "correct": True,
                "rationale": (
                    "Correct. The DHCP server unicasts the DHCPOFFER to the giaddr (172.16.10.1 — the relay "
                    "agent). If the server lacks a route to 172.16.10.0/24, the Offer is dropped in transit "
                    "and the relay agent never receives it. The client does not receive an offer. This is a "
                    "classic, easily overlooked issue: the server must be able to route back to every subnet "
                    "it serves, typically via a static route or routing protocol pointing to the relay agent's "
                    "IP or a next-hop toward the clients."
                ),
            },
            {
                "id": "b",
                "text": "The 'ip helper-address' command must be applied on the interface facing the DHCP server, not the client-facing interface",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip helper-address' must be on the interface facing the CLIENTS (where "
                    "broadcasts arrive). The configuration shown (on Gi0/0, which connects to the 172.16.10.0 "
                    "subnet) is correct. Moving it to the server-facing interface would break relay."
                ),
            },
            {
                "id": "c",
                "text": "The DHCP Discover is being dropped because 'ip helper-address' only relays UDP port 69 (TFTP) by default",
                "correct": False,
                "rationale": (
                    "Incorrect. By default, 'ip helper-address' relays several UDP services including "
                    "DHCP/BOOTP (ports 67/68), TFTP (69), DNS (53), TACACS (49), time (37), NetBIOS "
                    "name service (137), and NetBIOS datagram (138). DHCP is included by default."
                ),
            },
            {
                "id": "d",
                "text": "The giaddr field must match the DHCP server IP, not the relay agent interface IP",
                "correct": False,
                "rationale": (
                    "Incorrect. The giaddr (Gateway IP Address) field is set by the relay agent to its own "
                    "interface IP (172.16.10.1 in this case). The DHCP server uses giaddr to select the "
                    "correct address pool and to unicast the reply to the relay agent. The giaddr should "
                    "NOT be the DHCP server's IP."
                ),
            },
        ],
        "explanation": (
            "DHCP relay troubleshooting checklist: "
            "(1) 'ip helper-address' on correct (client-facing) interface; "
            "(2) DHCP server has pool matching giaddr subnet; "
            "(3) DHCP server has a RETURN ROUTE to the giaddr subnet — the most commonly missed step; "
            "(4) No ACL blocking UDP 67/68 between relay and server; "
            "(5) 'service dhcp' not disabled on the relay router. "
            "The server unicasts DHCPOFFER to giaddr — if routing fails in either direction, the "
            "exchange breaks silently."
        ),
    },
    # ── cd4v3-014 ── DHCP relay (ip helper-address) ──────────────────────────
    {
        "id": "cd4v3-014",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP relay (ip helper-address)",
        "stem": (
            "A Cisco IOS router is both a DHCP server and a DHCP relay agent. The router has:\n"
            "  interface Vlan30\n"
            "   ip address 192.168.30.1 255.255.255.0\n"
            "   ip helper-address 192.168.30.1\n\n"
            "A network engineer notices this configuration and raises a concern. "
            "Which statement BEST describes the issue?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configuring ip helper-address pointing to the router's own interface causes the relay to loop; the router should rely on its local DHCP server pool without a helper-address",
                "correct": True,
                "rationale": (
                    "Correct. When 'ip helper-address' is set to the router's own interface IP, the relayed "
                    "DHCP Discover is sent as a unicast back to the router itself. Depending on the IOS "
                    "version, this either causes a loop, gets dropped, or creates unexpected behavior. "
                    "If the router is the DHCP server for VLAN 30, the helper-address is unnecessary — "
                    "IOS will match the local pool based on the incoming interface subnet automatically. "
                    "The helper-address is only needed when the DHCP server is on a DIFFERENT router/subnet."
                ),
            },
            {
                "id": "b",
                "text": "The helper-address should point to the broadcast address (192.168.30.255) to reach the local DHCP server",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip helper-address' must point to a unicast IP address of the DHCP server. "
                    "Using a broadcast address as the helper target is not valid and would not forward "
                    "DHCP traffic to a specific server."
                ),
            },
            {
                "id": "c",
                "text": "The ip helper-address is on the wrong interface; it should be on the interface facing the DHCP server, not the client VLAN",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip helper-address' is always placed on the client-facing interface. "
                    "The concern here is not about which interface it's on, but that the helper is "
                    "pointing to the router's own address unnecessarily."
                ),
            },
            {
                "id": "d",
                "text": "This configuration is valid; 'ip helper-address' pointing to self causes IOS to use the fastest path to the local DHCP server pool",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no IOS feature that uses a self-referential helper-address as "
                    "an optimized local shortcut. The correct approach is to have no helper-address on "
                    "an interface when the router itself is the DHCP server for that subnet."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS DHCP server operation: when a DHCP Discover arrives on an interface, the router "
            "first checks if it has a local DHCP pool matching that interface's subnet (without any relay). "
            "No 'ip helper-address' is needed for locally served subnets. 'ip helper-address' is required "
            "only when the DHCP server is on a remote subnet. Configuring helper-address pointing to the "
            "local interface creates unnecessary complexity and potential loop conditions. "
            "Remove 'ip helper-address 192.168.30.1' and ensure the pool is correctly configured."
        ),
    },
    # ── cd4v3-015 ── QoS ────────────────────────────────────────────────────
    {
        "id": "cd4v3-015",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "A network engineer is configuring QoS on a WAN interface using MQC (Modular QoS CLI). "
            "The policy-map has three classes: VOICE (priority 512), VIDEO (bandwidth 2048), "
            "and DATA (bandwidth 1024). The WAN interface is 10 Mbps. "
            "An excess of voice traffic beyond 512 kbps arrives. What happens to voice packets "
            "that exceed the LLQ (Low Latency Queue) configured rate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Voice packets exceeding 512 kbps are dropped by the LLQ policer, even if the link has spare capacity",
                "correct": True,
                "rationale": (
                    "Correct. The 'priority' command in Cisco MQC creates an LLQ (Low Latency Queue) with "
                    "an implicit policer at the specified rate. Packets that exceed the priority bandwidth "
                    "are dropped regardless of whether other queues are idle or whether link capacity is "
                    "available. This protects other traffic classes from being starved by bursty voice "
                    "streams. The rate acts as both a guarantee and a cap."
                ),
            },
            {
                "id": "b",
                "text": "Voice packets exceeding 512 kbps are queued in a secondary buffer and transmitted when the link becomes less congested",
                "correct": False,
                "rationale": (
                    "Incorrect. LLQ does not buffer excess traffic. The 'priority' command combines strict "
                    "priority scheduling with policing — excess traffic is dropped immediately. There is no "
                    "secondary queue for overflow voice packets."
                ),
            },
            {
                "id": "c",
                "text": "Voice packets exceeding 512 kbps are re-marked to DSCP 0 (Best Effort) and placed in the default class queue",
                "correct": False,
                "rationale": (
                    "Incorrect. LLQ policing drops excess packets; it does not re-mark and re-queue them. "
                    "Re-marking (e.g., DSCP policing with 'exceed-action dscp-transmit') is a separate "
                    "policy action not associated with the 'priority' command."
                ),
            },
            {
                "id": "d",
                "text": "The LLQ automatically borrows bandwidth from the VIDEO and DATA classes to accommodate excess voice traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. Bandwidth borrowing applies to CBWFQ 'bandwidth' classes (which can use "
                    "idle capacity above their minimum guarantee), not to LLQ 'priority' classes. "
                    "The priority class has a hard ceiling enforced by the built-in policer."
                ),
            },
        ],
        "explanation": (
            "LLQ (Low Latency Queue) = CBWFQ + strict priority + implicit policer. "
            "Configured with 'priority <kbps>' in a policy-map class. "
            "Behaviour: (1) strict priority scheduling — LLQ traffic dequeues before all other classes; "
            "(2) built-in policer at the specified rate — excess packets are DROPPED. "
            "This prevents LLQ traffic from monopolizing the link at the cost of other classes. "
            "For voice (constant-rate, latency-sensitive), the rate equals the expected voice bandwidth. "
            "Contrast with 'bandwidth' (CBWFQ): guarantees a minimum, allows borrowing idle capacity, "
            "no built-in policer."
        ),
    },
    # ── cd4v3-016 ── QoS ────────────────────────────────────────────────────
    {
        "id": "cd4v3-016",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "A QoS policy classifies traffic by DSCP value at the distribution layer and re-marks "
            "untrusted traffic at the access layer. An access switch port connects to a PC (not an "
            "IP phone). The access switch is configured with:\n"
            "  mls qos trust cos\n"
            "  no mls qos trust dscp\n\n"
            "The PC sends packets marked DSCP EF (46). What DSCP value will the packet have when "
            "it reaches the distribution switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DSCP 0 (Best Effort), because the switch trusts CoS not DSCP; since the PC does not set an 802.1Q CoS value, the switch maps CoS 0 to DSCP 0",
                "correct": True,
                "rationale": (
                    "Correct. 'mls qos trust cos' trusts the CoS (802.1p) value in the 802.1Q header, "
                    "not the IP DSCP. Since the PC connects to an untagged access port, its frames "
                    "have no 802.1Q tag and thus no CoS value — the switch assigns CoS 0. "
                    "The switch then derives DSCP from the CoS-to-DSCP map; CoS 0 → DSCP 0. "
                    "The original DSCP EF (46) in the IP header is overwritten with DSCP 0. "
                    "This prevents untrusted endpoints from self-marking premium traffic."
                ),
            },
            {
                "id": "b",
                "text": "DSCP EF (46), because once a packet is marked EF it cannot be overwritten by a switch",
                "correct": False,
                "rationale": (
                    "Incorrect. DSCP markings in the IP ToS/DSCP field can be overwritten by any device "
                    "that processes QoS policy. 'mls qos trust cos' explicitly ignores the DSCP value "
                    "and derives QoS treatment from CoS instead, which can result in DSCP being re-marked."
                ),
            },
            {
                "id": "c",
                "text": "DSCP EF (46), because 'no mls qos trust dscp' only prevents the switch from trusting the DSCP but still preserves the original marking in the packet",
                "correct": False,
                "rationale": (
                    "Incorrect. When 'mls qos trust cos' is active and a CoS value maps to a different "
                    "DSCP, the switch rewrites the DSCP in the packet. The original DSCP EF is not "
                    "preserved — it is overwritten based on the CoS-to-DSCP mapping."
                ),
            },
            {
                "id": "d",
                "text": "CoS 5, because the switch converts DSCP EF (46) to CoS 5 using the default DSCP-to-CoS map",
                "correct": False,
                "rationale": (
                    "Incorrect. CoS is a Layer 2 field in the 802.1Q header. Conversions between DSCP "
                    "and CoS occur in different directions depending on trust configuration. The question "
                    "asks for the DSCP value at the next switch — with 'trust cos' and no 802.1Q tag, "
                    "the effective CoS is 0, which maps to DSCP 0."
                ),
            },
        ],
        "explanation": (
            "QoS trust on Cisco Catalyst switches: "
            "'mls qos trust dscp' — honor IP DSCP, use DSCP for internal QoS label; "
            "'mls qos trust cos' — honor 802.1p CoS, use CoS-to-DSCP map to derive DSCP; "
            "'mls qos trust device cisco-phone' — conditionally trust CoS only from an authenticated phone. "
            "Without trust, the switch defaults to DSCP 0 for all traffic. "
            "Access ports for PCs should NOT trust DSCP or CoS to prevent endpoints from self-marking "
            "traffic with premium DSCP values to steal bandwidth."
        ),
    },
    # ── cd4v3-017 ── SSH remote access ──────────────────────────────────────
    {
        "id": "cd4v3-017",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SSH remote access",
        "stem": (
            "An engineer is verifying SSH on a Cisco router and runs 'show ip ssh'. The output includes:\n"
            "  SSH Enabled - version 1.99\n"
            "  Authentication timeout: 120 secs; Authentication retries: 3\n\n"
            "What does 'version 1.99' mean, and what command would restrict the router to SSHv2 only?"
        ),
        "options": [
            {
                "id": "a",
                "text": "'Version 1.99' means the router accepts both SSHv1 and SSHv2 connections; 'ip ssh version 2' restricts it to SSHv2 only",
                "correct": True,
                "rationale": (
                    "Correct. SSH version 1.99 is a compatibility string indicating the router accepts "
                    "both SSHv1 and SSHv2 client connections. This is the default when RSA keys exist "
                    "but 'ip ssh version' has not been explicitly set. 'ip ssh version 2' restricts "
                    "the server to SSHv2 exclusively, refusing SSHv1 negotiation and improving security "
                    "(SSHv1 has known vulnerabilities including man-in-the-middle susceptibility)."
                ),
            },
            {
                "id": "b",
                "text": "'Version 1.99' is an IOS internal version code indicating the SSH daemon is running firmware release 1.99; no command change is needed",
                "correct": False,
                "rationale": (
                    "Incorrect. SSH 1.99 is a standard SSH protocol version string (defined in RFC 4253 "
                    "transition guidance) meaning backward-compatible with both versions. It is not an "
                    "IOS firmware version number."
                ),
            },
            {
                "id": "c",
                "text": "'Version 1.99' means only SSHv1 is supported; 'ip ssh version 2' upgrades to SSHv2",
                "correct": False,
                "rationale": (
                    "Incorrect. Version 1.99 indicates BOTH SSHv1 and SSHv2 are accepted, not SSHv1 only. "
                    "If only SSHv1 were supported, the output would show 'version 1.0' or 'version 1'."
                ),
            },
            {
                "id": "d",
                "text": "'Version 1.99' is a deprecated state; the router must be reloaded to apply 'ip ssh version 2'",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip ssh version 2' takes effect immediately without a reload. "
                    "SSH version 1.99 is not a deprecated state — it is normal IOS behavior when "
                    "version is not explicitly constrained."
                ),
            },
        ],
        "explanation": (
            "SSH protocol version negotiation: 'SSH-1.99-...' in the protocol banner means the server "
            "accepts both SSHv1 and SSHv2 (defined in RFC 4253 section 5.1 for backward compatibility). "
            "Cisco IOS default after RSA key generation: version 1.99 (both accepted). "
            "'ip ssh version 1' — accept SSHv1 only (insecure, not recommended); "
            "'ip ssh version 2' — accept SSHv2 only (recommended for production). "
            "Verify: 'show ip ssh' shows the active version and authentication parameters. "
            "Additional hardening: reduce 'ip ssh time-out' (default 120s) and 'ip ssh authentication-retries'."
        ),
    },
    # ── cd4v3-018 ── SSH remote access ──────────────────────────────────────
    {
        "id": "cd4v3-018",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SSH remote access",
        "stem": (
            "A network administrator has configured SSH on a router but wants to ensure that only the "
            "management workstation at 192.168.100.50 can SSH to the VTY lines. The router's loopback "
            "address is 10.255.0.1 and its management interface is 10.1.0.1. "
            "Which configuration BEST restricts SSH access to only 192.168.100.50?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ip access-list standard MGMT-ONLY\n"
                    " permit host 192.168.100.50\n"
                    "line vty 0 4\n"
                    " access-class MGMT-ONLY in"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'access-class <acl> in' applied to VTY lines restricts inbound connections "
                    "to only source IPs permitted by the ACL. The standard ACL 'MGMT-ONLY' permits only "
                    "192.168.100.50; an implicit deny blocks all other IPs. This is the correct and "
                    "purpose-built mechanism for restricting management access to specific hosts."
                ),
            },
            {
                "id": "b",
                "text": (
                    "ip access-list extended MGMT-ONLY\n"
                    " permit tcp host 192.168.100.50 host 10.1.0.1 eq 22\n"
                    "(applied with 'ip access-group MGMT-ONLY in' on the management interface)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While an inbound ACL on the interface blocks SSH from unauthorized sources "
                    "destined to 10.1.0.1, it does not protect access via the loopback or other interfaces. "
                    "An engineer could still SSH to 10.255.0.1 from an unauthorized host if routing allows "
                    "it. The 'access-class' on VTY lines is more comprehensive — it applies regardless of "
                    "which interface the SSH packet arrives on."
                ),
            },
            {
                "id": "c",
                "text": (
                    "ip ssh source-interface 192.168.100.50"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip ssh source-interface' sets the source interface the router uses when "
                    "initiating outbound SSH connections to other devices. It has no effect on restricting "
                    "inbound SSH sessions to the router's VTY lines."
                ),
            },
            {
                "id": "d",
                "text": (
                    "line vty 0 4\n"
                    " transport input ssh\n"
                    " login local\n"
                    " ip verify source"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip verify source' is a feature that validates source IPs against DHCP "
                    "snooping bindings to prevent IP spoofing on access ports — it is not a VTY access "
                    "restriction command. It is not applicable to restricting SSH management access."
                ),
            },
        ],
        "explanation": (
            "Restricting VTY (SSH/Telnet) access to specific source IPs requires the 'access-class' command "
            "on the vty lines, referencing a standard ACL. Unlike 'ip access-group' on an interface "
            "(which filters by ingress/egress interface), 'access-class in' checks the SOURCE IP of the "
            "management session regardless of which physical interface the packet arrived on. "
            "This protects all management access paths simultaneously. "
            "Best practice: combine 'transport input ssh', 'login local'/'aaa authentication', "
            "and 'access-class <acl> in' on all VTY lines."
        ),
    },
    # ── cd4v3-019 ── TFTP/FTP ───────────────────────────────────────────────
    {
        "id": "cd4v3-019",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TFTP/FTP",
        "stem": (
            "An engineer is copying an IOS image from a router's flash to a remote server using FTP. "
            "The router's FTP credentials are configured with:\n"
            "  ip ftp username netadmin\n"
            "  ip ftp password Cisco123\n\n"
            "The engineer then runs:\n"
            "  copy flash:c1100-universalk9.bin ftp://10.5.0.20/backups/c1100.bin\n\n"
            "The transfer fails with 'Permission denied'. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The FTP server at 10.5.0.20 does not have write permissions for the 'netadmin' user in the /backups/ directory",
                "correct": True,
                "rationale": (
                    "Correct. FTP 'Permission denied' errors indicate the server rejected the file write. "
                    "The router's IOS FTP client successfully authenticated (credentials are configured) "
                    "but the FTP server denied the STOR command because the 'netadmin' account does not "
                    "have write permission to the /backups/ directory. This is a server-side permission "
                    "issue, not a router configuration error."
                ),
            },
            {
                "id": "b",
                "text": "FTP is passive mode by default on Cisco IOS; the server firewall blocks the data channel TCP connection from the server to the router",
                "correct": False,
                "rationale": (
                    "Incorrect. If the data channel were blocked, the error would typically be a "
                    "connection timeout or 'connection refused', not 'Permission denied'. "
                    "A 'Permission denied' FTP response (code 550) specifically indicates an authorization "
                    "failure at the server, not a network connectivity issue."
                ),
            },
            {
                "id": "c",
                "text": "The 'ip ftp username' and 'ip ftp password' commands are not valid for file transfers initiated with 'copy flash: ftp:'",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip ftp username' and 'ip ftp password' are exactly the commands used to "
                    "set FTP credentials for Cisco IOS 'copy' commands. They apply to all FTP operations "
                    "including 'copy flash: ftp:'."
                ),
            },
            {
                "id": "d",
                "text": "FTP cannot be used to send files from flash; 'copy flash: ftp:' is only supported for copying from FTP to flash",
                "correct": False,
                "rationale": (
                    "Incorrect. 'copy flash: ftp:' is a valid Cisco IOS command to upload a file FROM "
                    "flash TO an FTP server. IOS supports bidirectional FTP file transfers."
                ),
            },
        ],
        "explanation": (
            "FTP server response codes: 550 = 'Permission denied' (authorization failure for the operation); "
            "530 = 'Not logged in' (authentication failure); 425 = 'Can't open data connection' (firewall/NAT). "
            "When 'Permission denied' appears after a successful FTP connection, the issue is server-side "
            "authorization — the authenticated user lacks write permission to the target directory. "
            "On Cisco IOS, FTP client credentials are set globally with 'ip ftp username/password'. "
            "Verify with 'debug ip ftp' to trace the FTP command exchange."
        ),
    },
    # ── cd4v3-020 ── TFTP/FTP ───────────────────────────────────────────────
    {
        "id": "cd4v3-020",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TFTP/FTP",
        "stem": (
            "A technician wants to copy a new IOS image from a TFTP server (192.168.1.50) to a router's "
            "flash. The router has limited RAM. Which statement correctly describes TFTP behavior "
            "that the technician should be aware of before initiating the transfer?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TFTP writes the file directly to flash without buffering in RAM; large files can be copied safely regardless of available RAM",
                "correct": False,
                "rationale": (
                    "Incorrect. On many Cisco platforms, IOS must load the TFTP-received image into RAM "
                    "before writing it to flash. If available RAM is less than the image size, the copy "
                    "may fail partway through. This is a known concern for IOS upgrades on lower-end "
                    "platforms with limited RAM."
                ),
            },
            {
                "id": "b",
                "text": "TFTP uses UDP and has no built-in error detection; a corrupt flash write cannot be detected after the transfer completes",
                "correct": False,
                "rationale": (
                    "Incorrect. While TFTP uses UDP and relies on block-level acknowledgments rather than "
                    "TCP's stream reliability, Cisco IOS verifies the MD5 checksum of the downloaded image "
                    "after the transfer. A corrupt transfer is detected by the checksum verification step, "
                    "not left undetected."
                ),
            },
            {
                "id": "c",
                "text": "TFTP transfers use UDP port 69 for the initial request, then negotiate a random UDP port pair for data transfer; firewalls between the router and TFTP server must permit these dynamic ports",
                "correct": True,
                "rationale": (
                    "Correct. TFTP uses a well-known port (UDP 69) for the initial Read Request (RRQ) or "
                    "Write Request (WRQ). After the server receives the request, it selects a random "
                    "ephemeral UDP port (a TID — Transfer Identifier) for the data exchange; the client "
                    "also uses a random source port. Stateful firewalls handle this automatically, but "
                    "stateless ACLs must permit UDP traffic with dynamic ports or use broad UDP rules "
                    "between the router and TFTP server."
                ),
            },
            {
                "id": "d",
                "text": "TFTP requires the router to authenticate with a username and password before the transfer begins",
                "correct": False,
                "rationale": (
                    "Incorrect. TFTP has no authentication mechanism whatsoever. Authentication is a "
                    "feature of FTP and SCP, not TFTP. The lack of authentication is one of the primary "
                    "security limitations of TFTP, which is why it should only be used in trusted networks."
                ),
            },
        ],
        "explanation": (
            "TFTP (RFC 1350) protocol details: "
            "- Initial request on UDP port 69 (well-known); subsequent data on random ephemeral UDP ports (TIDs). "
            "- No authentication, no encryption — suitable only for trusted network segments. "
            "- Block size default 512 bytes; RFC 2348 extends to 65464 bytes for large file efficiency. "
            "- ACK-per-block reliability (lock-step); not a streaming protocol. "
            "For IOS image copies, verify: sufficient flash space ('show flash'), sufficient free RAM on "
            "platforms that buffer in RAM, reachability to TFTP server, and firewall rules permitting "
            "dynamic UDP ports."
        ),
    },
    # ── cd4v3-021 ── NAT/PAT ────────────────────────────────────────────────
    {
        "id": "cd4v3-021",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "An engineer wants to verify that PAT is working correctly. They run 'debug ip nat' and "
            "observe:\n"
            "  NAT*: s=10.1.1.5->203.0.113.1, d=8.8.8.8 [1234]\n"
            "  NAT*: s=8.8.8.8, d=203.0.113.1->10.1.1.5 [1234]\n\n"
            "In the first line, what does the arrow '->' between the source addresses indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The source address was translated FROM 10.1.1.5 (inside local) TO 203.0.113.1 (inside global) as the packet exits toward the destination 8.8.8.8",
                "correct": True,
                "rationale": (
                    "Correct. In 'debug ip nat' output, the '->' arrow between addresses indicates a "
                    "translation. 's=10.1.1.5->203.0.113.1' means the source IP was changed from the "
                    "inside local (10.1.1.5) to the inside global (203.0.113.1). The asterisk (*) indicates "
                    "fast-switched (CEF/fast-path) NAT. The number in brackets [1234] is the IP packet ID."
                ),
            },
            {
                "id": "b",
                "text": "The packet is being routed FROM 10.1.1.5 TO 203.0.113.1; no translation has occurred yet",
                "correct": False,
                "rationale": (
                    "Incorrect. In NAT debug output, '->' specifically indicates that a translation "
                    "occurred — the address before the arrow is the pre-translation value and the address "
                    "after is the post-translation value. The debug message would not use '->' to indicate "
                    "simple routing."
                ),
            },
            {
                "id": "c",
                "text": "10.1.1.5 is the inside global and 203.0.113.1 is the inside local; the arrow shows the reverse translation direction",
                "correct": False,
                "rationale": (
                    "Incorrect. In standard PAT/NAT, 10.1.1.x addresses are private (inside local) and "
                    "203.0.113.x addresses are public (inside global). The debug confirms outbound "
                    "translation: private → public. The second debug line shows the reverse: return "
                    "traffic is translated back from public (203.0.113.1) to private (10.1.1.5)."
                ),
            },
            {
                "id": "d",
                "text": "The router is performing destination NAT; 10.1.1.5 is the original destination and 203.0.113.1 is the new destination",
                "correct": False,
                "rationale": (
                    "Incorrect. The 's=' prefix indicates this is a SOURCE address translation. "
                    "Destination NAT would appear as 'd=x.x.x.x->y.y.y.y' in the debug output."
                ),
            },
        ],
        "explanation": (
            "'debug ip nat' output format: s=<src_before>-><src_after>, d=<dst_before>-><dst_after> [id]. "
            "Arrow (->) between addresses = translation occurred. "
            "Outbound (inside→outside): s=inside_local->inside_global, d=outside_global. "
            "Return (outside→inside): s=outside_global, d=inside_global->inside_local. "
            "The asterisk (*) denotes fast-path processing. "
            "Use 'debug ip nat detailed' for port numbers (useful for PAT verification)."
        ),
    },
    # ── cd4v3-022 ── DHCP & DNS roles ───────────────────────────────────────
    {
        "id": "cd4v3-022",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A DHCP server is configured with a lease time of 8 hours. A host receives an IP address "
            "at 8:00 AM. At what time will the host FIRST attempt to renew the lease, and which "
            "DHCP message type does it use for this renewal?"
        ),
        "options": [
            {
                "id": "a",
                "text": "At 12:00 PM (50% of lease time = 4 hours after assignment); the host sends a unicast DHCPREQUEST directly to the DHCP server",
                "correct": True,
                "rationale": (
                    "Correct. RFC 2131 defines the T1 renewal timer as 50% of the lease time. For an "
                    "8-hour lease, T1 = 4 hours, so the first renewal attempt is at 8:00 AM + 4 hours = "
                    "12:00 PM. The host sends a unicast DHCPREQUEST (not a Discover) directly to the "
                    "original DHCP server's unicast IP. The DHCP server responds with a DHCPACK extending "
                    "the lease."
                ),
            },
            {
                "id": "b",
                "text": "At 2:00 PM (75% of lease time = 6 hours after assignment); the host sends a broadcast DHCPDISCOVER to find any available server",
                "correct": False,
                "rationale": (
                    "Incorrect. The 75% mark (T2 = 6 hours, at 2:00 PM) is the REBINDING timer — when the "
                    "host gives up on the original server and broadcasts a DHCPREQUEST to any server. "
                    "The first renewal attempt (T1 = 50%) is at 12:00 PM using unicast to the original server."
                ),
            },
            {
                "id": "c",
                "text": "At 3:59 PM (just before lease expiry at 4:00 PM); the host sends a DHCPRELEASE and starts a new DORA sequence",
                "correct": False,
                "rationale": (
                    "Incorrect. An 8-hour lease expires at 4:00 AM the next day, not 4:00 PM. Also, "
                    "DHCP clients attempt renewal well before expiry (at T1 and T2). The T3 expiry causes "
                    "the address to be released and a new DORA sequence to begin, but this only happens "
                    "if both T1 and T2 renewal attempts fail."
                ),
            },
            {
                "id": "d",
                "text": "At 8:00 PM (100% of lease time); the host broadcasts a DHCPDISCOVER to re-acquire an address",
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting until 100% (lease expiry) to renew means the host loses its IP "
                    "address and must restart with DHCPDISCOVER. Normal DHCP operation renews at T1 (50%) "
                    "with unicast and at T2 (87.5%) with broadcast, well before lease expiry."
                ),
            },
        ],
        "explanation": (
            "DHCP lease renewal timers (RFC 2131): "
            "T1 = 0.5 × lease time (50%) — unicast DHCPREQUEST to original server; "
            "T2 = 0.875 × lease time (87.5%) — broadcast DHCPREQUEST to any server (rebinding); "
            "T3 = lease time (100%) — lease expires; host reverts to DHCPDISCOVER. "
            "For an 8-hour lease: T1=4h (12:00 PM), T2=7h (3:00 PM), expiry=8h (4:00 AM next day). "
            "Renewal uses DHCPREQUEST (not Discover), preserving the existing IP. "
            "ACK extends the lease; NAK forces a new DORA sequence."
        ),
    },
    # ── cd4v3-023 ── SNMP ───────────────────────────────────────────────────
    {
        "id": "cd4v3-023",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SNMP",
        "stem": (
            "A network engineer configures SNMPv3 on a Cisco router with the following:\n"
            "  snmp-server group NETOPS v3 priv\n"
            "  snmp-server user NMSUSER NETOPS v3 auth sha Aut#Pass1 priv aes 128 Prv#Pass2\n\n"
            "The NMS attempts a query using 'authNoPriv' security level. What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The query is rejected; the group NETOPS requires 'priv' security level and the NMS must use authPriv (authentication + encryption)",
                "correct": True,
                "rationale": (
                    "Correct. The SNMPv3 group 'NETOPS' is configured with 'v3 priv', meaning the minimum "
                    "security level for group members is authPriv (authentication AND privacy/encryption). "
                    "A query from NMSUSER using only authNoPriv (authentication without encryption) does not "
                    "meet the group's security requirement and will be rejected with an authorization error. "
                    "The group security level is enforced on all users in that group."
                ),
            },
            {
                "id": "b",
                "text": "The query succeeds; 'priv' in the group definition is a maximum, not a minimum — lower security levels are also accepted",
                "correct": False,
                "rationale": (
                    "Incorrect. The security level specified in 'snmp-server group' is a MINIMUM requirement, "
                    "not a maximum. If the group requires 'priv', then every member must use authPriv. "
                    "Using a lower security level (authNoPriv or noAuthNoPriv) is rejected."
                ),
            },
            {
                "id": "c",
                "text": "The query succeeds but the response is sent unencrypted because the NMS did not request privacy",
                "correct": False,
                "rationale": (
                    "Incorrect. The group enforces authPriv. The router does not selectively drop encryption "
                    "to accommodate lower-security queries from group members — the query is rejected outright "
                    "if the security level doesn't match the group requirement."
                ),
            },
            {
                "id": "d",
                "text": "The query is rejected because SNMPv3 requires SHA authentication, and authNoPriv uses MD5",
                "correct": False,
                "rationale": (
                    "Incorrect. The rejection is due to the security level mismatch (authNoPriv vs. required "
                    "authPriv), not due to the hash algorithm. SNMPv3 supports both MD5 and SHA for "
                    "authentication regardless of the security level."
                ),
            },
        ],
        "explanation": (
            "SNMPv3 security levels (ascending order): "
            "noAuthNoPriv — no authentication, no encryption; "
            "authNoPriv — HMAC authentication (MD5 or SHA), no encryption; "
            "authPriv — HMAC authentication + DES/3DES/AES encryption. "
            "The 'snmp-server group' security level sets the MINIMUM required level for that group. "
            "Users sending queries at a lower level than required are denied. "
            "On Cisco IOS, configure: 'snmp-server group <name> v3 {noauth|auth|priv}' and "
            "'snmp-server user <name> <group> v3 [auth <alg> <pass>] [priv <alg> <pass>]'."
        ),
    },
    # ── cd4v3-024 ── NTP ────────────────────────────────────────────────────
    {
        "id": "cd4v3-024",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "NTP",
        "stem": (
            "An engineer configures NTP authentication on a router:\n"
            "  ntp authenticate\n"
            "  ntp authentication-key 1 md5 NTPsecret!\n"
            "  ntp trusted-key 1\n"
            "  ntp server 10.0.0.1\n\n"
            "The upstream NTP server at 10.0.0.1 is NOT configured with NTP authentication. "
            "The router shows 'Clock is unsynchronized' in 'show ntp status'. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router requires authenticated NTP responses (ntp trusted-key 1); since 10.0.0.1 sends unauthenticated responses, the router rejects them and remains unsynchronized",
                "correct": True,
                "rationale": (
                    "Correct. When 'ntp authenticate' and 'ntp trusted-key' are configured, the router "
                    "will only accept time from servers whose NTP packets contain a valid, trusted key. "
                    "The server at 10.0.0.1 sends standard NTP without a key — the router's authentication "
                    "check fails, the server is marked as untrusted, and the clock does not synchronize. "
                    "Both sides must have matching authentication keys for NTP auth to succeed."
                ),
            },
            {
                "id": "b",
                "text": "NTP authentication requires RSA keys; MD5 is not a valid algorithm for NTP on Cisco IOS",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS NTP authentication uses MD5 keyed hash (symmetric key), not RSA. "
                    "RSA is used by SSH, not NTP. 'ntp authentication-key <id> md5 <key>' is the correct "
                    "and only supported NTP authentication syntax on standard Cisco IOS."
                ),
            },
            {
                "id": "c",
                "text": "The router needs 'ntp server 10.0.0.1 key 1' to associate the key with the server; without it, authentication is not applied to that server's traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. While 'ntp server <ip> key <id>' is the correct command to associate a key "
                    "with a specific server and would be required for full NTP authentication, the question "
                    "states the server itself does not use authentication. Even with 'key 1' added, the "
                    "server's unsigned responses would still fail authentication. The root issue is the "
                    "server not being configured for NTP auth."
                ),
            },
            {
                "id": "d",
                "text": "NTP authentication conflicts with NTP server configuration; 'ntp server' and 'ntp authenticate' cannot coexist on the same device",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ntp authenticate' and 'ntp server' are designed to be used together. "
                    "Authentication enhances the security of client-server NTP relationships. They do not "
                    "conflict; both can and should be configured simultaneously in secure environments."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS NTP authentication requires matching configuration on BOTH the client and server: "
            "Client: 'ntp authenticate', 'ntp authentication-key <id> md5 <key>', 'ntp trusted-key <id>', "
            "'ntp server <ip> key <id>'. "
            "Server: same key ID and key value, also configured with 'ntp authenticate'. "
            "If only one side is configured for authentication, NTP responses fail the integrity check "
            "and the client remains unsynchronized. "
            "'show ntp associations detail' reveals authentication status per peer (showing 'authenticated' "
            "or 'not authenticated' next to each configured server)."
        ),
    },
    # ── cd4v3-025 ── QoS ────────────────────────────────────────────────────
    {
        "id": "cd4v3-025",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "A network engineer is asked to explain the difference between DSCP AF21 and DSCP AF23. "
            "A colleague states 'they are in the same AF class so they are treated identically.' "
            "Which statement BEST corrects this misconception?"
        ),
        "options": [
            {
                "id": "a",
                "text": "AF21 and AF23 are in the same Assured Forwarding class (Class 2) but have different drop precedences; AF23 has the highest drop probability within AF2 and is dropped first during congestion",
                "correct": True,
                "rationale": (
                    "Correct. Assured Forwarding PHBs are encoded as AFxy where x = class (1-4) and "
                    "y = drop precedence (1=low, 2=medium, 3=high). AF21, AF22, AF23 are all in AF class 2 "
                    "(same queue and bandwidth allocation). During congestion, WRED drops packets using "
                    "drop precedence: AF23 > AF22 > AF21. Traffic marked AF23 is sacrificed first to "
                    "protect AF21 traffic within the same class."
                ),
            },
            {
                "id": "b",
                "text": "AF21 and AF23 are in different AF classes; AF21 is class 2 and AF23 is class 3, so they compete for different bandwidth allocations",
                "correct": False,
                "rationale": (
                    "Incorrect. The first digit in AFxy is the class number. AF21 and AF23 both have "
                    "x=2 → both are in AF class 2. AF23's '3' refers to drop precedence (high), "
                    "not a different class. AF31 and AF32 would be in class 3."
                ),
            },
            {
                "id": "c",
                "text": "AF21 and AF23 are indeed treated identically; the drop precedence suffix is informational only and not used by Cisco switches",
                "correct": False,
                "rationale": (
                    "Incorrect. Drop precedence is actively used by WRED (Weighted Random Early Detection) "
                    "to set different drop thresholds for different precedence levels within the same AF class. "
                    "Cisco QoS implementations honor drop precedence when WRED is configured."
                ),
            },
            {
                "id": "d",
                "text": "AF23 gets more bandwidth than AF21 because a higher DSCP number indicates higher priority",
                "correct": False,
                "rationale": (
                    "Incorrect. A higher DSCP number does not inherently mean higher priority or more "
                    "bandwidth. Within an AF class, higher drop precedence (higher third digit) means "
                    "the traffic is MORE likely to be dropped, not given more bandwidth. Class is the "
                    "primary determinant of bandwidth allocation."
                ),
            },
        ],
        "explanation": (
            "DSCP Assured Forwarding (AF) PHB: AFxy where x=class (1–4), y=drop precedence (1=low, 2=med, 3=high). "
            "DSCP values: AF11=10, AF12=12, AF13=14; AF21=18, AF22=20, AF23=22; "
            "AF31=26, AF32=28, AF33=30; AF41=34, AF42=36, AF43=38. "
            "All traffic in the same class (e.g., AF2x) shares the same minimum bandwidth queue. "
            "WRED drops higher-precedence (y=3) traffic first during congestion to protect lower-precedence "
            "(y=1) traffic. This allows service providers to offer tiered service within a class."
        ),
    },
    # ── cd4v3-026 ── DHCP relay (ip helper-address) ──────────────────────────
    {
        "id": "cd4v3-026",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP relay (ip helper-address)",
        "stem": (
            "By default, 'ip helper-address' on a Cisco router forwards several UDP broadcast services "
            "in addition to DHCP. An engineer wants to restrict the relay to forward ONLY DHCP traffic "
            "(UDP ports 67 and 68) and stop forwarding DNS (port 53), TFTP (port 69), and NetBIOS "
            "broadcasts. Which command accomplishes this restriction?"
        ),
        "options": [
            {
                "id": "a",
                "text": "no ip forward-protocol udp 53\nno ip forward-protocol udp 69\nno ip forward-protocol udp 137\nno ip forward-protocol udp 138",
                "correct": True,
                "rationale": (
                    "Correct. 'ip helper-address' by default forwards eight UDP services: 37 (time), "
                    "49 (TACACS), 53 (DNS), 67 (BOOTP/DHCP client), 68 (BOOTP/DHCP server), 69 (TFTP), "
                    "137 (NetBIOS name), 138 (NetBIOS datagram). To restrict to DHCP only, remove the "
                    "other services using 'no ip forward-protocol udp <port>'. Ports 67 and 68 are "
                    "enabled by default and do not need to be explicitly added."
                ),
            },
            {
                "id": "b",
                "text": "ip helper-address 10.0.0.5 dhcp-only",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'dhcp-only' keyword for the 'ip helper-address' command. "
                    "The forwarded protocols are controlled globally with 'ip forward-protocol udp <port>'."
                ),
            },
            {
                "id": "c",
                "text": "ip helper-address 10.0.0.5 67 68",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'ip helper-address' command takes only an IP address (and optionally "
                    "a redundancy group) as arguments. Port numbers are not specified in the command itself; "
                    "they are managed globally with 'ip forward-protocol udp'."
                ),
            },
            {
                "id": "d",
                "text": "access-list 100 permit udp any any eq 67\naccess-list 100 permit udp any any eq 68\nip helper-address 10.0.0.5 access-class 100",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'access-class' option for 'ip helper-address'. Protocol "
                    "filtering for the helper is controlled through 'ip forward-protocol udp' commands, "
                    "not through ACLs applied to the helper-address command."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS default UDP forwarded services under 'ip helper-address': "
            "37 (Time), 49 (TACACS), 53 (DNS), 67 (DHCP/BOOTP server), 68 (DHCP/BOOTP client), "
            "69 (TFTP), 137 (NetBIOS name service), 138 (NetBIOS datagram service). "
            "To add a service: 'ip forward-protocol udp <port>'. "
            "To remove a service: 'no ip forward-protocol udp <port>'. "
            "To restrict to DHCP only: remove DNS(53), TFTP(69), NetBIOS(137,138), TACACS(49), Time(37). "
            "Verify: 'show ip forward-protocol' lists all enabled forwarded protocols."
        ),
    },
    # ── cd4v3-027 ── multiple_response: NAT/PAT + DHCP & DNS roles ──────────
    {
        "id": "cd4v3-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "Select TWO statements that are TRUE about static NAT on Cisco IOS routers."
        ),
        "options": [
            {
                "id": "a",
                "text": "A static NAT entry persists in the NAT table indefinitely and is not subject to the NAT translation timeout",
                "correct": True,
                "rationale": (
                    "Correct. Unlike dynamic NAT entries that age out after an idle timeout, static NAT "
                    "mappings are permanent — they remain in the translation table until explicitly removed "
                    "with 'no ip nat inside source static' or 'clear ip nat translation'. This is necessary "
                    "for servers that must always be reachable from outside."
                ),
            },
            {
                "id": "b",
                "text": "Static NAT allows multiple inside hosts to share a single public IP using port multiplexing",
                "correct": False,
                "rationale": (
                    "Incorrect. Port multiplexing describes PAT (overload), not static NAT. Static NAT "
                    "performs a one-to-one mapping between a single inside local address and a single "
                    "inside global address. Each host requires its own unique public IP."
                ),
            },
            {
                "id": "c",
                "text": "Static NAT enables unsolicited inbound connections from the Internet to reach an inside host because the mapping exists before any session is initiated",
                "correct": True,
                "rationale": (
                    "Correct. Because the static mapping is permanent and bidirectional, external hosts can "
                    "initiate connections to the inside global IP and the NAT router will translate them to "
                    "the inside local IP. This is why static NAT (not PAT) is used to publish internal "
                    "servers to the Internet."
                ),
            },
            {
                "id": "d",
                "text": "Static NAT requires the 'ip nat inside source static' command followed by 'ip nat translation timeout 0' to prevent expiration",
                "correct": False,
                "rationale": (
                    "Incorrect. Static NAT entries created with 'ip nat inside source static' are inherently "
                    "permanent. 'ip nat translation timeout 0' is not needed and is not a valid concept for "
                    "static entries. The timeout command applies only to dynamic NAT/PAT entries."
                ),
            },
        ],
        "explanation": (
            "Static NAT key characteristics: permanent one-to-one address mapping, bidirectional — allows "
            "both outbound (inside→outside) and inbound (outside→inside) sessions, no timeout, "
            "requires a dedicated public IP per mapped inside host. "
            "Used for publishing internal servers (web, mail, DNS) to the Internet. "
            "Command: 'ip nat inside source static <inside-local> <inside-global>'. "
            "For server port-forwarding (one public IP, multiple servers): static port NAT — "
            "'ip nat inside source static tcp <inside-local> <port> <inside-global> <port>'."
        ),
    },
    # ── cd4v3-028 ── multiple_response: Syslog severity levels ──────────────
    {
        "id": "cd4v3-028",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "A router is configured with 'logging trap informational'. "
            "Select TWO severity levels whose messages WILL be forwarded to the syslog server."
        ),
        "options": [
            {
                "id": "a",
                "text": "Severity 3 (Error)",
                "correct": True,
                "rationale": (
                    "Correct. 'logging trap informational' sets the threshold to severity 6. All messages "
                    "from severity 0 (Emergency) through severity 6 (Informational) are forwarded. "
                    "Severity 3 (Error) is within this range (3 ≤ 6) and will be sent to the syslog server."
                ),
            },
            {
                "id": "b",
                "text": "Severity 7 (Debugging)",
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging trap informational' (level 6) does NOT include severity 7 "
                    "(Debugging). Level 7 has a higher number than the threshold of 6, meaning it is "
                    "less severe than the threshold and is suppressed."
                ),
            },
            {
                "id": "c",
                "text": "Severity 5 (Notice/Notification)",
                "correct": True,
                "rationale": (
                    "Correct. Severity 5 (Notice) is within the range 0–6 set by 'logging trap "
                    "informational'. Messages at severity 5 are forwarded to the syslog server."
                ),
            },
            {
                "id": "d",
                "text": "Severity 8 (Verbose)",
                "correct": False,
                "rationale": (
                    "Incorrect. Syslog severity levels are defined only from 0 to 7 in RFC 5424 and "
                    "Cisco IOS. There is no severity level 8. This is a distractor testing knowledge "
                    "of the severity range boundary."
                ),
            },
        ],
        "explanation": (
            "Syslog severity levels 0–7 only: Emergency(0), Alert(1), Critical(2), Error(3), "
            "Warning(4), Notice(5), Informational(6), Debugging(7). "
            "'logging trap informational' = 'logging trap 6' = forward levels 0 through 6. "
            "Level 7 (Debugging) is excluded unless threshold is set to 7 with 'logging trap debugging'. "
            "Debugging-level logging generates extremely high message volumes and should not be enabled "
            "to remote syslog servers in production environments without filtering."
        ),
    },
    # ── cd4v3-029 ── multiple_response: SSH remote access + TFTP/FTP ────────
    {
        "id": "cd4v3-029",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SSH remote access",
        "stem": (
            "Select TWO prerequisites that MUST be configured on a Cisco IOS router before "
            "SSH can be enabled and functional."
        ),
        "options": [
            {
                "id": "a",
                "text": "A hostname other than the default 'Router' must be set with the 'hostname' command",
                "correct": True,
                "rationale": (
                    "Correct. RSA key generation uses the format 'hostname.domain-name' as the key label. "
                    "A meaningful hostname (not the default 'Router') is required. If the hostname is 'Router', "
                    "the key is generated as 'Router.domain-name', which is technically functional but "
                    "violates best practice. More critically, if the hostname is missing or default, the key "
                    "label is ambiguous, and some IOS versions refuse to generate SSH keys."
                ),
            },
            {
                "id": "b",
                "text": "An RSA key pair must be generated with 'crypto key generate rsa'",
                "correct": True,
                "rationale": (
                    "Correct. SSH uses RSA asymmetric encryption for the key exchange phase of the "
                    "handshake. Without RSA keys, the router cannot establish the SSH session. "
                    "'crypto key generate rsa modulus 2048' is required before SSH becomes functional. "
                    "SSHv2 requires a minimum of 768 bits; 2048 bits is recommended."
                ),
            },
            {
                "id": "c",
                "text": "A username with privilege level 15 must be created in the local database",
                "correct": False,
                "rationale": (
                    "Incorrect. SSH itself does not require a privilege-15 user to function. Any local "
                    "username with any privilege level can authenticate via SSH. Privilege level 15 "
                    "provides enable-level access but is not a prerequisite for the SSH protocol itself. "
                    "Some users may be privilege 1 for restricted access."
                ),
            },
            {
                "id": "d",
                "text": "The 'service ssh' command must be enabled globally",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'service ssh' command in Cisco IOS. SSH is enabled automatically "
                    "once RSA keys are generated. The relevant commands are 'crypto key generate rsa' and "
                    "optionally 'ip ssh version 2'. Compare this with 'service dhcp', which does exist "
                    "and controls the DHCP server."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS SSH prerequisites: "
            "(1) 'hostname <name>' — non-default hostname (used in RSA key label); "
            "(2) 'ip domain-name <name>' — required for RSA key generation label; "
            "(3) 'crypto key generate rsa modulus 2048' — generates the key pair that enables SSH; "
            "(4) 'ip ssh version 2' — optional but recommended to restrict to SSHv2; "
            "(5) VTY lines: 'transport input ssh' and 'login local' (or AAA). "
            "Once RSA keys exist, SSH is active. Verify: 'show ip ssh', 'show crypto key mypubkey rsa'."
        ),
    },
    # ── cd4v3-030 ── multiple_response: DHCP & DNS roles ────────────────────
    {
        "id": "cd4v3-030",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "Select TWO statements that are TRUE about the DHCP DORA process and address conflict detection."
        ),
        "options": [
            {
                "id": "a",
                "text": "A DHCP server performs a ping (ICMP echo) to the address it is about to offer, to check whether the address is already in use before sending DHCPOFFER",
                "correct": True,
                "rationale": (
                    "Correct. By default, Cisco IOS DHCP server pings an address before offering it. "
                    "If the ping receives a reply, the server marks the address as a conflict, adds it to "
                    "the conflict database ('show ip dhcp conflict'), skips that address, and tries the next "
                    "one in the pool. This is configurable with 'ip dhcp ping packets <count>' and "
                    "'ip dhcp ping timeout <ms>'. This prevents offering addresses already used by "
                    "statically configured hosts."
                ),
            },
            {
                "id": "b",
                "text": "After receiving DHCPACK, the client sends a gratuitous ARP to verify that no other host on the segment is using the assigned IP address",
                "correct": True,
                "rationale": (
                    "Correct. RFC 2131 recommends that DHCP clients issue a gratuitous ARP (ARP probe) "
                    "for the offered IP address after receiving DHCPACK. If another host responds to the "
                    "ARP, the client sends DHCPDECLINE to the server (informing it of a conflict) and "
                    "restarts the DORA process. The server then records the declined address as a conflict."
                ),
            },
            {
                "id": "c",
                "text": "The DHCP client always sends DHCPREQUEST as a unicast to the IP address specified in the DHCPOFFER's Server Identifier option",
                "correct": False,
                "rationale": (
                    "Incorrect. During initial address acquisition (first-time DORA), the DHCPREQUEST is "
                    "sent as a BROADCAST (the client has not yet committed to the address). The unicast "
                    "DHCPREQUEST is used during lease RENEWAL (T1 timer) when the client already has an "
                    "IP and sends directly to the original server."
                ),
            },
            {
                "id": "d",
                "text": "DHCPNAK (negative acknowledgment) is sent by the client to reject an unsuitable offer from the server",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCPNAK is sent by the SERVER to the client, not the other way around. "
                    "The server sends DHCPNAK when it cannot fulfill a DHCPREQUEST (e.g., the requested "
                    "address is no longer available or the client is on the wrong subnet). "
                    "The client rejects an unsuitable address by sending DHCPDECLINE, not DHCPNAK."
                ),
            },
        ],
        "explanation": (
            "DHCP conflict detection mechanisms: "
            "Server-side: ICMP ping before offering (configurable on Cisco IOS). "
            "Client-side: gratuitous ARP probe after receiving DHCPACK; if conflict detected → DHCPDECLINE. "
            "DHCP message types summary: "
            "DHCPDISCOVER (client broadcast, find server); DHCPOFFER (server unicast/broadcast, offer IP); "
            "DHCPREQUEST (client broadcast during DORA, or unicast during renewal); "
            "DHCPACK (server confirms assignment); DHCPNAK (server denies request); "
            "DHCPDECLINE (client rejects offered IP — conflict detected); "
            "DHCPRELEASE (client voluntarily releases IP); DHCPINFORM (client requests config, has IP)."
        ),
    },
]
