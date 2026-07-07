QUESTIONS = [
    {
        "id": "cd4-001",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "A router is configured with the following commands:\n"
            "  ip nat inside source list 10 interface GigabitEthernet0/1 overload\n"
            "  access-list 10 permit 192.168.1.0 0.0.0.255\n"
            "Host 192.168.1.10 sends a packet to 8.8.8.8. After NAT translation, which address pair "
            "correctly describes the inside local and inside global addresses?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Inside local: 192.168.1.10; Inside global: the IP assigned to GigabitEthernet0/1",
                "correct": True,
                "rationale": (
                    "Correct. The inside local is the private address of the host as seen from inside the network "
                    "(192.168.1.10). The inside global is the public-facing address the packet is translated to — "
                    "in PAT/overload mode this is the IP of the exit interface (GigabitEthernet0/1), with a unique "
                    "source port to differentiate sessions."
                ),
            },
            {
                "id": "b",
                "text": "Inside local: the IP assigned to GigabitEthernet0/1; Inside global: 192.168.1.10",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the definitions. The inside local is always the private host address; "
                    "the inside global is the translated (public) address seen outside the network."
                ),
            },
            {
                "id": "c",
                "text": "Inside local: 192.168.1.10; Inside global: 8.8.8.8",
                "correct": False,
                "rationale": (
                    "Incorrect. 8.8.8.8 is the destination (outside global address), not the inside global. "
                    "The inside global is the translated source address, not the destination."
                ),
            },
            {
                "id": "d",
                "text": "Inside local: 8.8.8.8; Inside global: 192.168.1.10",
                "correct": False,
                "rationale": (
                    "Incorrect. 8.8.8.8 is the outside global address (the public destination). "
                    "The inside local/global terminology applies to the originating host, not the destination."
                ),
            },
        ],
        "explanation": (
            "NAT terminology: Inside local = private address of internal host as seen from inside; "
            "Inside global = public address used to represent that host outside (post-translation); "
            "Outside global = address of the remote destination. PAT (overload) maps many inside local "
            "addresses to a single inside global address by multiplexing TCP/UDP port numbers."
        ),
    },
    {
        "id": "cd4-002",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "A network administrator issues 'show ip nat translations' and sees:\n"
            "  Pro  Inside global       Inside local        Outside local       Outside global\n"
            "  tcp  203.0.113.1:1025    10.1.1.5:1025       172.16.0.1:80       172.16.0.1:80\n\n"
            "Which statement about this translation entry is TRUE?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The inside host at 10.1.1.5 is communicating with 172.16.0.1 using PAT; 203.0.113.1 is the public-facing address",
                "correct": True,
                "rationale": (
                    "Correct. The entry shows a TCP PAT translation: 10.1.1.5:1025 (inside local) is translated "
                    "to 203.0.113.1:1025 (inside global) for communication with 172.16.0.1:80. The presence of "
                    "port numbers in the Inside global column confirms PAT (overload) is in use."
                ),
            },
            {
                "id": "b",
                "text": "This is a static NAT entry because the port numbers on both sides are identical (1025)",
                "correct": False,
                "rationale": (
                    "Incorrect. Matching port numbers do not indicate static NAT. Static NAT maps an inside local "
                    "address to a fixed inside global address without port translation. The presence of port numbers "
                    "in the global column is the hallmark of PAT regardless of whether the port numbers happen to match."
                ),
            },
            {
                "id": "c",
                "text": "172.16.0.1 is the inside local address of a second internal host",
                "correct": False,
                "rationale": (
                    "Incorrect. 172.16.0.1 appears in the Outside local and Outside global columns, indicating "
                    "it is the remote destination (outside) address, not an internal host."
                ),
            },
            {
                "id": "d",
                "text": "The translation will persist indefinitely because it is a TCP entry",
                "correct": False,
                "rationale": (
                    "Incorrect. Dynamic NAT/PAT translations have configurable timeouts (default 24 hours for TCP "
                    "extended translations). They are not permanent; only static NAT entries persist indefinitely "
                    "unless explicitly removed."
                ),
            },
        ],
        "explanation": (
            "'show ip nat translations' output columns: Inside global (public translated address:port), "
            "Inside local (private host address:port), Outside local (destination as seen from inside), "
            "Outside global (real destination address). Port numbers in the Inside global column confirm PAT. "
            "Dynamic entries age out per configured timeouts."
        ),
    },
    {
        "id": "cd4-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "NAT/PAT",
        "stem": (
            "An engineer needs to allow an internal web server at 10.10.10.50 to be reachable from the Internet "
            "on public IP 203.0.113.100. The router's outside interface already uses 203.0.113.1/30. "
            "Which configuration correctly implements static NAT for this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ip nat inside source static 10.10.10.50 203.0.113.100\n"
                    "(applied with 'ip nat inside' on the LAN interface and 'ip nat outside' on the WAN interface)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Static NAT maps a single inside local address (10.10.10.50) one-to-one to a fixed "
                    "inside global address (203.0.113.100). The 'ip nat inside' and 'ip nat outside' interface "
                    "designations are mandatory for NAT to function; without them the router cannot determine "
                    "translation direction."
                ),
            },
            {
                "id": "b",
                "text": (
                    "ip nat inside source list 1 pool WEB overload\n"
                    "ip nat pool WEB 203.0.113.100 203.0.113.100 netmask 255.255.255.252"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Using 'overload' with a pool of one address creates PAT, which translates "
                    "outbound sessions from many hosts. It would not allow unsolicited inbound connections "
                    "from the Internet to reach 10.10.10.50."
                ),
            },
            {
                "id": "c",
                "text": "ip nat outside source static 10.10.10.50 203.0.113.100",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip nat outside source static' translates outside (source) addresses, which is "
                    "used in a different, less common scenario. The correct command for mapping an inside private "
                    "address to a public IP is 'ip nat inside source static'."
                ),
            },
            {
                "id": "d",
                "text": "ip nat inside source static tcp 10.10.10.50 80 203.0.113.1 80",
                "correct": False,
                "rationale": (
                    "Incorrect. This command creates a static port-forwarding NAT entry using the router's own "
                    "outside interface IP (203.0.113.1), not the dedicated public IP 203.0.113.100 assigned to "
                    "the server. It also only forwards TCP port 80, not all protocols."
                ),
            },
        ],
        "explanation": (
            "Static NAT provides a permanent one-to-one mapping between an inside local and inside global address. "
            "Both interface-direction commands ('ip nat inside' / 'ip nat outside') must be applied. "
            "PAT/overload is appropriate for many-to-one outbound translation but cannot handle arbitrary inbound "
            "sessions without additional static or port-forwarding entries."
        ),
    },
    {
        "id": "cd4-004",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTP",
        "stem": (
            "A Cisco router shows the following output:\n"
            "  R1# show ntp status\n"
            "  Clock is synchronized, stratum 3, reference is 10.0.0.1\n\n"
            "What can be concluded from this output?"
        ),
        "options": [
            {
                "id": "a",
                "text": "R1 is synchronized to 10.0.0.1, which is a stratum 2 NTP server, and R1 itself is stratum 3",
                "correct": True,
                "rationale": (
                    "Correct. A device's stratum is always one greater than its upstream NTP reference. "
                    "If R1 is stratum 3 and references 10.0.0.1, then 10.0.0.1 must be stratum 2. "
                    "'Clock is synchronized' confirms R1 has successfully synchronized."
                ),
            },
            {
                "id": "b",
                "text": "R1 is a stratum 3 NTP master and 10.0.0.1 is a downstream client",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'reference is 10.0.0.1' field identifies the upstream server R1 is "
                    "synchronized to, not a downstream client. Downstream clients are not shown in 'show ntp status'."
                ),
            },
            {
                "id": "c",
                "text": "R1 is unsynchronized because stratum 3 exceeds the maximum useful stratum of 2",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP stratum values run from 1 (directly connected to a reference clock) to 15 "
                    "(the practical limit). Stratum 16 means unsynchronized. Stratum 3 is perfectly valid and "
                    "common in enterprise networks."
                ),
            },
            {
                "id": "d",
                "text": "R1 will advertise itself as stratum 2 to any NTP clients that query it",
                "correct": False,
                "rationale": (
                    "Incorrect. R1 will advertise stratum 3 to its own clients; they will then be stratum 4. "
                    "Each hop adds 1 to the stratum value."
                ),
            },
        ],
        "explanation": (
            "NTP stratum indicates distance from the reference clock source. Stratum 1 is directly attached to "
            "an authoritative clock (GPS, atomic). Each NTP hop adds 1. A router synchronized to a stratum N "
            "server becomes stratum N+1 to its own clients. Stratum 16 = unsynchronized. The 'reference' field "
            "in 'show ntp status' identifies the upstream time source."
        ),
    },
    {
        "id": "cd4-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTP",
        "stem": (
            "An engineer wants Router R2 to use Router R1 (10.1.1.1) as its NTP server. R2 should also act as "
            "an NTP server for downstream devices at stratum 5. Which configuration on R2 achieves both goals?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ntp server 10.1.1.1\n(R2 will automatically serve time to clients at its own stratum level)",
                "correct": True,
                "rationale": (
                    "Correct. Configuring 'ntp server 10.1.1.1' causes R2 to synchronize to R1. Once synchronized, "
                    "R2 automatically acts as an NTP server for any downstream devices that query it — no additional "
                    "command is needed to enable the server function. R2's stratum will be R1's stratum + 1; if R1 "
                    "is stratum 4, R2 becomes stratum 5 automatically."
                ),
            },
            {
                "id": "b",
                "text": "ntp server 10.1.1.1\nntp master 5",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ntp master 5' makes R2 an authoritative NTP source that will serve time even if "
                    "it loses synchronization with R1, using its own internal clock at stratum 5. This is typically "
                    "used as a fallback/last-resort, not as a normal client-server setup. It can also cause the "
                    "router to override synchronized time with its local clock in some failure scenarios, which "
                    "is undesirable here."
                ),
            },
            {
                "id": "c",
                "text": "ntp peer 10.1.1.1\nntp broadcast client",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ntp peer' establishes a symmetric active association (both devices can sync "
                    "to each other), which is not required here. 'ntp broadcast client' configures R2 to accept "
                    "NTP broadcasts, a passive mode unrelated to the unicast client requirement."
                ),
            },
            {
                "id": "d",
                "text": "ntp authenticate\nntp trusted-key 1\nntp server 10.1.1.1 key 1",
                "correct": False,
                "rationale": (
                    "Incorrect. These commands configure NTP authentication, which is a security enhancement. "
                    "While valid in a secure environment, they require matching configuration on R1 (defining "
                    "key 1 with the same password). Without the corresponding key on R1, R2 will fail to "
                    "synchronize. Authentication is not required by the question."
                ),
            },
        ],
        "explanation": (
            "On Cisco IOS, 'ntp server <ip>' is sufficient to make a router both an NTP client (syncing upstream) "
            "and an NTP server (responding to downstream queries). 'ntp master' is used to designate a router as "
            "an authoritative stratum source independent of external synchronization — useful as a fallback but "
            "not needed for normal client/server operation. NTP authentication (MD5) adds security but requires "
            "matching keys on both endpoints."
        ),
    },
    {
        "id": "cd4-006",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A host on VLAN 10 (subnet 192.168.10.0/24) sends a DHCP Discover message. The DHCP server "
            "is on a different subnet (10.0.0.0/24). The Layer 3 switch acting as the default gateway for "
            "VLAN 10 has the following configuration on its VLAN 10 interface:\n"
            "  interface Vlan10\n"
            "   ip address 192.168.10.1 255.255.255.0\n"
            "   ip helper-address 10.0.0.10\n\n"
            "Which statement correctly describes what happens to the DHCP Discover packet?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The switch converts the broadcast DHCP Discover to a unicast UDP packet sourced from "
                    "192.168.10.1 and forwards it to 10.0.0.10"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The 'ip helper-address' command (DHCP relay agent, RFC 3046) intercepts the "
                    "broadcast DHCP Discover on the ingress interface, changes the destination from "
                    "255.255.255.255 to the configured helper address (10.0.0.10), sets the source to the "
                    "relay agent's interface IP (192.168.10.1), and forwards it as a unicast packet. The "
                    "giaddr field is populated with 192.168.10.1 so the DHCP server knows which scope to use."
                ),
            },
            {
                "id": "b",
                "text": "The switch floods the broadcast out all interfaces, including the uplink toward 10.0.0.10",
                "correct": False,
                "rationale": (
                    "Incorrect. Without ip helper-address, a router/L3 switch drops broadcasts and does not "
                    "forward them between subnets. The ip helper-address specifically converts the broadcast "
                    "to a directed unicast — it does not simply flood it."
                ),
            },
            {
                "id": "c",
                "text": "The switch drops the packet because DHCP broadcasts cannot cross Layer 3 boundaries",
                "correct": False,
                "rationale": (
                    "Incorrect. While it is true that broadcasts do not normally cross Layer 3 boundaries, "
                    "the 'ip helper-address' command exists specifically to overcome this limitation by "
                    "acting as a relay agent."
                ),
            },
            {
                "id": "d",
                "text": "The DHCP Discover is forwarded as a broadcast to all interfaces in all VLANs on the switch",
                "correct": False,
                "rationale": (
                    "Incorrect. Broadcasts are contained within their VLAN/broadcast domain. The relay agent "
                    "converts the broadcast to a unicast destined specifically for the configured helper "
                    "address, not to all VLANs."
                ),
            },
        ],
        "explanation": (
            "DHCP relay (ip helper-address) solves the problem of DHCP broadcasts not crossing router boundaries. "
            "The relay agent (router or L3 switch) intercepts the broadcast Discover, inserts its own interface "
            "IP into the GIADDR (gateway IP address) field, changes the destination to the DHCP server's IP, "
            "and forwards it as unicast UDP port 67. The DHCP server uses GIADDR to select the correct address "
            "pool. The reply is unicast back to the relay agent, which then forwards it to the client."
        ),
    },
    {
        "id": "cd4-007",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A DNS server receives a query for 'www.example.com'. It does not have the record in cache "
            "and is configured as a recursive resolver. Which sequence of steps does it perform?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Query a root name server → receive referral to .com TLD server → query .com TLD server → "
                    "receive referral to example.com authoritative server → query authoritative server → "
                    "return the A record to the client"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Recursive DNS resolution follows the DNS hierarchy: root servers → TLD servers "
                    "(.com, .org, etc.) → authoritative name servers for the domain. The recursive resolver "
                    "performs all these steps on behalf of the client and caches results per their TTL."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Return a 'name not found' error immediately since it lacks the record"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A recursive resolver does not return an error just because the record is not "
                    "in cache. It performs full iterative resolution through the DNS hierarchy to find the answer."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Forward the query directly to the example.com authoritative server since the TLD is known"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A resolver without a cached referral cannot know the authoritative server for "
                    "example.com without first querying the TLD. The process must start at the root (or a "
                    "cached TLD referral) to discover the authoritative server address."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Send the query to the client's configured gateway and let it resolve the name"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DNS resolution is performed by the DNS server, not delegated back to the "
                    "client's gateway. The recursive resolver handles the full resolution process independently."
                ),
            },
        ],
        "explanation": (
            "DNS uses a hierarchical tree: root zone (.) → top-level domain (.com) → second-level domain (example.com). "
            "A recursive resolver queries root servers for a referral to the TLD server, then the TLD server for "
            "a referral to the authoritative server, then the authoritative server for the final answer. Results "
            "are cached per TTL to reduce future query load. Clients send queries to recursive resolvers; "
            "recursive resolvers perform the iterative lookups."
        ),
    },
    {
        "id": "cd4-008",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SNMP",
        "stem": (
            "A network engineer is evaluating SNMPv2c versus SNMPv3 for monitoring a healthcare network "
            "that must comply with data privacy regulations. Which statement BEST explains why SNMPv3 "
            "is preferred in this environment?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SNMPv3 supports authentication (MD5/SHA) and encryption (DES/AES) via its authPriv "
                    "security level, preventing eavesdropping and data tampering; SNMPv2c transmits "
                    "community strings and data in plaintext"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SNMPv3 introduces the User Security Model (USM) with three security levels: "
                    "noAuthNoPriv (no authentication, no encryption), authNoPriv (authentication only), and "
                    "authPriv (authentication + encryption). SNMPv2c uses community strings transmitted in "
                    "cleartext, making it unsuitable for regulated environments."
                ),
            },
            {
                "id": "b",
                "text": (
                    "SNMPv3 is preferred because it uses TCP instead of UDP, ensuring reliable delivery "
                    "of management data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Both SNMPv2c and SNMPv3 use UDP (port 161 for get/set operations, 162 for "
                    "traps/informs). The primary advantage of SNMPv3 is security (authentication and "
                    "encryption), not transport reliability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SNMPv3 eliminates the need for a MIB because it uses XML-encoded data, "
                    "making it more suitable for compliance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv3 still uses MIBs (Management Information Bases) with OID-based "
                    "data structures. It does not use XML. The security improvements — not data format "
                    "changes — are the reason for its adoption in regulated environments."
                ),
            },
            {
                "id": "d",
                "text": (
                    "SNMPv3 supports a higher number of MIB objects than SNMPv2c, enabling more "
                    "comprehensive monitoring"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The number of MIB objects is not determined by the SNMP version but by "
                    "what the managed device implements. SNMPv3 does not inherently support more MIB objects "
                    "than SNMPv2c."
                ),
            },
        ],
        "explanation": (
            "SNMPv1/v2c use community strings (read-only / read-write) that are transmitted in plaintext — "
            "a significant security vulnerability. SNMPv3 adds the User Security Model (USM) supporting "
            "HMAC-MD5/HMAC-SHA authentication and DES/3DES/AES encryption. The 'authPriv' level provides "
            "both. SNMPv3 also introduces the View-based Access Control Model (VACM) for fine-grained "
            "access control. In environments with data privacy requirements, SNMPv3 authPriv is mandatory."
        ),
    },
    {
        "id": "cd4-009",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SNMP",
        "stem": (
            "A network management system (NMS) needs to be alerted immediately when a router interface "
            "goes down, without the NMS having to continuously poll the device. Which SNMP mechanism "
            "should be configured, and on which UDP port does the NMS receive these messages?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SNMP traps sent from the agent to the NMS on UDP port 162",
                "correct": True,
                "rationale": (
                    "Correct. SNMP traps are unsolicited notifications sent by the agent (router) to the "
                    "NMS when significant events occur (e.g., interface down, linkDown trap). The NMS "
                    "listens for traps on UDP port 162. This eliminates the need for constant polling."
                ),
            },
            {
                "id": "b",
                "text": "SNMP Get-Request sent from the NMS to the agent on UDP port 161",
                "correct": False,
                "rationale": (
                    "Incorrect. Get-Request is a poll-based mechanism where the NMS initiates the query "
                    "to the agent on UDP 161. This requires the NMS to continuously poll, which is exactly "
                    "what the question wants to avoid."
                ),
            },
            {
                "id": "c",
                "text": "SNMP Set-Request sent from the NMS to the agent on UDP port 161",
                "correct": False,
                "rationale": (
                    "Incorrect. Set-Request is used to configure (write) values on managed devices, "
                    "not to receive event notifications. It is initiated by the NMS, not the agent."
                ),
            },
            {
                "id": "d",
                "text": "SNMP traps sent from the NMS to the agent on UDP port 161",
                "correct": False,
                "rationale": (
                    "Incorrect. Traps are sent BY the agent TO the NMS, not the other way around. "
                    "Additionally, traps are received by the NMS on UDP 162, not 161. Port 161 is used "
                    "for SNMP queries (Get, GetNext, Set)."
                ),
            },
        ],
        "explanation": (
            "SNMP uses UDP port 161 for management queries (Get, GetNext, GetBulk, Set) initiated by the NMS, "
            "and UDP port 162 for traps and informs sent by managed devices (agents) to the NMS. Traps are "
            "unreliable (no acknowledgment); Informs (SNMPv2c/v3) add reliability by requiring acknowledgment "
            "from the NMS. For immediate event notification without polling, configure SNMP traps on the "
            "agent with 'snmp-server host <NMS-IP> traps <community>'."
        ),
    },
    {
        "id": "cd4-010",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "A network engineer configures 'logging trap 4' on a router. Which messages will the router send to the syslog server?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Messages of severity 0 through 4 (emergency, alert, critical, error, warning)",
                "correct": True,
                "rationale": (
                    "Correct. 'logging trap 4' sets the severity threshold to 4 (warning); the router sends "
                    "all messages from severity 0 (emergency) up to and including 4. Lower numbers are more "
                    "severe, and the device logs that level and everything more severe."
                ),
            },
            {
                "id": "b",
                "text": "Only messages of severity exactly 4 (warning)",
                "correct": False,
                "rationale": (
                    "Incorrect. The trap level is a threshold, not an exact match; it includes all severities "
                    "numerically lower (more severe) than the configured level too."
                ),
            },
            {
                "id": "c",
                "text": "Messages of severity 4 through 7 (warning through debugging)",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the direction; higher numbers (5 notification, 6 informational, "
                    "7 debugging) are LESS severe and are excluded when the threshold is 4."
                ),
            },
            {
                "id": "d",
                "text": "All messages, since 4 enables full logging",
                "correct": False,
                "rationale": (
                    "Incorrect. Level 4 excludes severities 5-7; only level 7 (debugging) would include all messages."
                ),
            },
        ],
        "explanation": (
            "Syslog severities run 0-7: Emergency, Alert, Critical, Error, Warning, Notification, Informational, "
            "Debugging (mnemonic 'Every Awesome Cisco Engineer Will Need Ice-cream Daily'). Lower = more severe. "
            "A configured trap level sends that level and all more-severe (lower-numbered) messages."
        ),
    },
    {
        "id": "cd4-011",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Syslog severity levels",
        "stem": (
            "A router generates the following syslog message:\n"
            "  %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to down\n\n"
            "An engineer sees this message only in the console but not in the syslog server logs. "
            "The syslog server is reachable and 'logging host 10.0.0.50' is configured. "
            "Which is the MOST LIKELY cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The 'logging trap' level on the router is set to a value lower than 5 (e.g., 'logging trap 3'), "
                    "so severity 5 notifications are not forwarded to the syslog server"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The syslog message has severity 5 (notice/notification) as indicated by the '-5-' "
                    "in the message format. If 'logging trap' is configured to 3 (critical) or less, only "
                    "severities 0-3 are forwarded to the syslog host. Severity 5 would be suppressed. "
                    "The console sees it because console logging may have a higher (less restrictive) threshold."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The syslog message is severity 5 (notification), and syslog only forwards severity 0-2 by default"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Cisco IOS default logging trap level is 6 (informational), not 2. "
                    "By default, all messages through severity 6 are forwarded to syslog hosts."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The message contains facility LINEPROTO which is blocked by default on remote syslog destinations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS does not selectively block specific facilities from remote logging "
                    "by default. All facilities are forwarded equally; filtering is done by severity level, "
                    "not facility name."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Console logging is enabled with 'logging console 7' which overrides syslog and captures all messages locally"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Console logging and syslog server logging are independent; one does not "
                    "override the other. Each destination has its own threshold configured independently "
                    "('logging console', 'logging trap', 'logging buffered')."
                ),
            },
        ],
        "explanation": (
            "Cisco syslog message format: %FACILITY-SEVERITY-MNEMONIC: description. The severity digit "
            "(-5- in this case) identifies the level. Cisco IOS maintains separate logging thresholds for "
            "console ('logging console'), internal buffer ('logging buffered'), and remote syslog "
            "('logging trap'). Each can be set independently. Default 'logging trap' is 6 (informational); "
            "if lowered below 5, notification-level messages are suppressed from the syslog server."
        ),
    },
    {
        "id": "cd4-012",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP relay (ip helper-address)",
        "stem": (
            "A Cisco router is configured as a DHCP server for the 10.10.20.0/24 subnet:\n"
            "  ip dhcp pool VLAN20\n"
            "   network 10.10.20.0 255.255.255.0\n"
            "   default-router 10.10.20.1\n"
            "   dns-server 8.8.8.8\n"
            "  ip dhcp excluded-address 10.10.20.1 10.10.20.10\n\n"
            "Clients on VLAN 20 are not receiving IP addresses. The VLAN 20 interface on the router is "
            "configured with IP 10.10.20.1/24 and is up/up. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The excluded-address range (10.10.20.1-10.10.20.10) includes the gateway address, which prevents the pool from functioning",
                "correct": False,
                "rationale": (
                    "Incorrect. Including the gateway address in the excluded range is correct practice — "
                    "you exclude addresses already assigned statically so the DHCP server does not hand them "
                    "out. This does not break the pool; it just means addresses .1 through .10 will not be "
                    "dynamically assigned. Addresses .11 through .254 remain available."
                ),
            },
            {
                "id": "b",
                "text": "The 'ip dhcp pool' name 'VLAN20' does not match the interface name and therefore the pool is not bound to that interface",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP pool names do not need to match interface names. The pool is associated "
                    "with a subnet via the 'network' statement, not by the pool name. The router selects the "
                    "pool based on the subnet from which the DHCP request arrives."
                ),
            },
            {
                "id": "c",
                "text": "The router requires 'service dhcp' to be enabled; if it was disabled with 'no service dhcp', the router will not respond to DHCP requests",
                "correct": True,
                "rationale": (
                    "Correct. 'service dhcp' is enabled by default on Cisco IOS, but if an administrator "
                    "has issued 'no service dhcp', the router will silently discard all DHCP discover and "
                    "request messages, including those arriving on directly connected interfaces. This is "
                    "a common misconfiguration that prevents clients from obtaining addresses despite a "
                    "correctly configured pool."
                ),
            },
            {
                "id": "d",
                "text": "The dns-server statement must reference an internal server; external DNS addresses like 8.8.8.8 are rejected",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS DHCP pools accept any valid IP address for dns-server, including "
                    "public addresses like 8.8.8.8. There is no validation that restricts DNS server "
                    "addresses to internal ranges."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS enables DHCP service by default ('service dhcp'). If disabled with 'no service dhcp', "
            "the router drops all DHCP messages. Other common DHCP server issues: pool network statement "
            "must match the interface subnet, addresses not excluded that are statically assigned elsewhere "
            "cause conflicts, and 'ip dhcp excluded-address' must be configured before the pool. Always "
            "verify with 'show ip dhcp binding', 'show ip dhcp pool', and 'show ip dhcp conflict'."
        ),
    },
    {
        "id": "cd4-013",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP relay (ip helper-address)",
        "stem": (
            "A multilayer switch has VLAN interfaces for VLAN 10 (172.16.10.1/24) and VLAN 20 "
            "(172.16.20.1/24). A single DHCP server at 10.0.0.1 serves both VLANs. "
            "An engineer configures 'ip helper-address 10.0.0.1' under the VLAN 10 interface only. "
            "Clients in VLAN 10 get addresses; clients in VLAN 20 do not. What must the engineer do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Add 'ip helper-address 10.0.0.1' under the VLAN 20 interface (interface Vlan20)",
                "correct": True,
                "rationale": (
                    "Correct. The 'ip helper-address' command is an interface-level command and must be "
                    "configured on each interface (SVI) that needs DHCP relay. Since VLAN 20 clients "
                    "send broadcasts to the VLAN 20 SVI (172.16.20.1) and there is no helper-address "
                    "configured there, those broadcasts are dropped and never relayed to the DHCP server."
                ),
            },
            {
                "id": "b",
                "text": "Configure a second DHCP server specifically for VLAN 20",
                "correct": False,
                "rationale": (
                    "Incorrect. A single DHCP server can serve multiple subnets as long as relay agents "
                    "are configured correctly on each SVI. Adding a second DHCP server is unnecessary "
                    "and increases management overhead."
                ),
            },
            {
                "id": "c",
                "text": "Add 'ip helper-address 10.0.0.1' under the physical uplink interface toward the DHCP server",
                "correct": False,
                "rationale": (
                    "Incorrect. The helper-address must be placed on the interface facing the DHCP clients "
                    "(the SVI where broadcasts arrive), not on the uplink toward the server. Placing it "
                    "on the uplink would not intercept client broadcasts."
                ),
            },
            {
                "id": "d",
                "text": "Configure 'ip dhcp relay information option' globally to enable relay for all VLANs automatically",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip dhcp relay information option' enables DHCP Option 82 (relay agent "
                    "information) insertion, which adds circuit-ID and remote-ID to relayed packets. "
                    "It does not automatically configure relay on all VLANs — each SVI still requires "
                    "its own 'ip helper-address' command."
                ),
            },
        ],
        "explanation": (
            "'ip helper-address' is an interface-level command; it must be configured on each Layer 3 "
            "interface (SVI or physical) that receives DHCP broadcasts from clients needing relay. "
            "The relay agent populates the GIADDR field with the interface's own IP address, which the "
            "DHCP server uses to select the correct address pool. Multiple helper-address statements "
            "can be configured on a single interface to forward to multiple DHCP servers."
        ),
    },
    {
        "id": "cd4-014",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "A network engineer is designing QoS for VoIP traffic. The organization uses DSCP EF (Expedited "
            "Forwarding) marking for voice RTP streams. At the trust boundary (the access switch port "
            "connecting IP phones), which QoS behavior is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure 'mls qos trust dscp' on the switchport to trust DSCP markings from the IP phone, "
                    "and enable a strict-priority queue to ensure EF traffic receives low latency and low jitter"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The trust boundary is the point where the network begins to trust QoS markings. "
                    "IP phones mark voice RTP with DSCP EF (46), which maps to PHB Expedited Forwarding — "
                    "a strict-priority queue guaranteeing low latency, low jitter, and low packet loss. "
                    "'mls qos trust dscp' tells the switch to honor the DSCP value in the IP header rather "
                    "than overwriting it with a default value."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Mark all traffic from the phone port with DSCP 0 (Best Effort) and rely on per-hop behavior "
                    "deeper in the network to reclassify voice traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Marking traffic as DSCP 0 (Best Effort / BE) removes QoS differentiation. "
                    "Reclassifying traffic deeper in the network (after the access layer) is both operationally "
                    "complex and defeats the purpose of the trust boundary — the phone already marks traffic "
                    "correctly, so the switch should trust and preserve those markings."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Use DSCP AF41 (Assured Forwarding class 4, low drop) for voice because EF is reserved "
                    "for network control traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DSCP EF (46) is specifically defined for low-latency, low-jitter, low-loss "
                    "traffic such as VoIP (RFC 3246). AF41 provides assured forwarding with lower drop "
                    "preference but does not guarantee the strict latency bounds needed for voice. "
                    "Network control traffic typically uses CS6 (DSCP 48) or CS7 (DSCP 56)."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure traffic shaping on the access port to limit VoIP to 64 kbps, "
                    "ensuring fair bandwidth allocation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Shaping introduces queuing delay and jitter, which is harmful to real-time "
                    "voice traffic. VoIP requires a strict-priority queue, not a shaper. Policing (dropping "
                    "excess) might be used to protect against misbehaving endpoints, but shaping voice is "
                    "counter-productive."
                ),
            },
        ],
        "explanation": (
            "QoS trust boundaries define where the network begins honoring endpoint QoS markings. "
            "DSCP EF (46, binary 101110) is the Per-Hop Behavior for voice RTP: strict priority queue, "
            "<150ms one-way delay, <30ms jitter, <1% packet loss per ITU G.114. 'mls qos trust dscp' "
            "preserves IP phone markings at the access layer. Without trust, switches overwrite DSCP to "
            "0 (default). The trust boundary should be as close to the endpoint as possible — typically "
            "the access switch port where the phone connects."
        ),
    },
    {
        "id": "cd4-015",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "An ISP applies a traffic contract to a customer's WAN circuit: committed rate 10 Mbps, "
            "burst allowed to 15 Mbps for short intervals. Traffic exceeding the burst is dropped at "
            "the ISP edge. The customer's router also has a QoS policy on the WAN interface. "
            "Which QoS mechanism on the CUSTOMER router would BEST prevent packet loss from ISP policing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Traffic shaping on the customer's outbound WAN interface, configured to shape to the "
                    "committed rate (10 Mbps), buffering bursts rather than sending them to the ISP"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Shaping delays (buffers) traffic that exceeds the configured rate, smoothing "
                    "bursts and preventing them from reaching the ISP where they would be policed (dropped). "
                    "By shaping to 10 Mbps at the customer edge, traffic arrives at the ISP within the "
                    "contracted rate, avoiding drops. Shaping introduces delay but prevents loss."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Traffic policing on the customer's outbound WAN interface, configured to drop traffic "
                    "above 10 Mbps before it reaches the ISP"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Policing also prevents ISP drops by discarding excess traffic at the "
                    "customer edge, but it does so by dropping packets rather than buffering them. "
                    "Shaping is preferred when the goal is to prevent loss while still delivering as "
                    "much data as possible within the contracted rate."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Weighted Fair Queuing (WFQ) on the WAN interface to ensure equal bandwidth distribution "
                    "among all flows"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. WFQ is a queuing/scheduling algorithm that provides fair bandwidth allocation "
                    "among flows. It does not limit the aggregate rate sent to the ISP and therefore does "
                    "not prevent ISP policing drops when the total traffic exceeds 10 Mbps."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Class-Based Weighted Fair Queuing (CBWFQ) with a guaranteed bandwidth of 10 Mbps "
                    "for all traffic classes combined"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CBWFQ allocates minimum bandwidth guarantees to traffic classes and manages "
                    "congestion within the router's interface queue, but it does not rate-limit the total "
                    "output to 10 Mbps. Traffic can still burst above 10 Mbps and be policed by the ISP."
                ),
            },
        ],
        "explanation": (
            "Policing vs. Shaping: Policing drops or re-marks packets that exceed the configured rate — "
            "it does not buffer. Shaping buffers excess packets in a queue and releases them at the "
            "configured rate, smoothing bursts. When an ISP applies policing to enforce a CIR (committed "
            "information rate), configuring shaping at the customer edge to match the CIR prevents the "
            "ISP from seeing bursts. This trades latency (queuing delay from shaping) for packet loss "
            "avoidance (no ISP policing drops)."
        ),
    },
    {
        "id": "cd4-016",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SSH remote access",
        "stem": (
            "An engineer attempts to SSH into a Cisco router but receives the error: "
            "'SSH: no matching cipher found.' The router is running IOS 15.x. "
            "Which configuration is MOST likely missing or misconfigured on the router?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router has not generated RSA keys ('crypto key generate rsa'), which are required before SSH can negotiate encryption parameters",
                "correct": True,
                "rationale": (
                    "Correct. SSH on Cisco IOS requires RSA keys to be generated before the SSH server "
                    "can function. Without RSA keys, the SSH daemon cannot complete key exchange and "
                    "cipher negotiation will fail. The error 'no matching cipher found' can manifest "
                    "when the server cannot participate in negotiation at all. RSA key size should be "
                    "at least 1024 bits (2048 recommended for SSHv2)."
                ),
            },
            {
                "id": "b",
                "text": "The vty lines are configured with 'transport input telnet' instead of 'transport input ssh'",
                "correct": False,
                "rationale": (
                    "Incorrect. If vty lines only allow Telnet, the client would receive a connection "
                    "refused or the session would fall back to Telnet negotiation — not an SSH cipher "
                    "negotiation error. The cipher error occurs during SSH protocol negotiation, "
                    "suggesting the SSH daemon is active but cannot complete the handshake."
                ),
            },
            {
                "id": "c",
                "text": "The 'ip domain-name' command is missing, so the router cannot generate a hostname-based SSH identity",
                "correct": False,
                "rationale": (
                    "Incorrect. While 'ip domain-name' is required before generating RSA keys (the key "
                    "label uses hostname.domain-name), its absence prevents key generation, not cipher "
                    "negotiation. The question states the error is about cipher matching, implying keys "
                    "may exist but negotiation fails — the root cause is still missing/unusable RSA keys."
                ),
            },
            {
                "id": "d",
                "text": "The 'ip ssh version 2' command has not been configured, defaulting to SSHv1 which lacks cipher support",
                "correct": False,
                "rationale": (
                    "Incorrect. SSHv1 does support encryption ciphers (3DES, Blowfish). The 'no matching "
                    "cipher' error is more fundamental — it indicates the server cannot participate in "
                    "the handshake at all, pointing to missing RSA keys rather than a version mismatch."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS SSH server prerequisites: (1) hostname set (not 'Router'), (2) 'ip domain-name' "
            "configured, (3) RSA keys generated with 'crypto key generate rsa modulus 2048', "
            "(4) 'ip ssh version 2' recommended, (5) VTY lines configured with 'transport input ssh' "
            "and 'login local' (or AAA). Without RSA keys, SSH cannot function regardless of other "
            "settings. Verify with 'show ip ssh' and 'show crypto key mypubkey rsa'."
        ),
    },
    {
        "id": "cd4-017",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SSH remote access",
        "stem": (
            "An engineer is hardening SSH access on a Cisco IOS router. Which combination of commands "
            "BEST restricts remote management to SSHv2 only and enforces local database authentication "
            "on VTY lines 0 through 4?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ip ssh version 2\n"
                    "line vty 0 4\n"
                    " transport input ssh\n"
                    " login local"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'ip ssh version 2' globally restricts SSH to version 2 only (disabling SSHv1). "
                    "'transport input ssh' prevents Telnet connections on VTY lines. 'login local' requires "
                    "authentication against the local username database. Together these three commands "
                    "enforce encrypted SSHv2-only access with local credential validation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "ip ssh version 2\n"
                    "line vty 0 4\n"
                    " transport input all\n"
                    " login local"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'transport input all' allows both Telnet and SSH connections. "
                    "Telnet transmits credentials in plaintext, which violates the security hardening "
                    "requirement. Only 'transport input ssh' should be used."
                ),
            },
            {
                "id": "c",
                "text": (
                    "ip ssh version 2\n"
                    "line vty 0 4\n"
                    " transport input ssh\n"
                    " no login"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'no login' disables authentication on VTY lines entirely, allowing any "
                    "user to connect without credentials. This is a critical security misconfiguration "
                    "regardless of transport protocol restrictions."
                ),
            },
            {
                "id": "d",
                "text": (
                    "crypto key generate rsa modulus 2048\n"
                    "line vty 0 4\n"
                    " transport input ssh\n"
                    " login local"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While generating RSA keys is a prerequisite, this configuration is missing "
                    "'ip ssh version 2'. Without it, both SSHv1 and SSHv2 may be accepted depending on "
                    "the IOS version's default, which does not enforce strict SSHv2-only access."
                ),
            },
        ],
        "explanation": (
            "SSH hardening on Cisco IOS requires: 'ip ssh version 2' (restrict to SSHv2), "
            "'transport input ssh' on VTY lines (block Telnet), 'login local' (require username/password "
            "from local database). Prerequisites: valid hostname, domain name, and RSA keys. "
            "Additional hardening: 'ip ssh time-out', 'ip ssh authentication-retries', "
            "access-class on VTY lines to restrict source IPs, and strong enable/local passwords."
        ),
    },
    {
        "id": "cd4-018",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TFTP/FTP",
        "stem": (
            "An engineer needs to back up a Cisco router's running configuration to a TFTP server at "
            "192.168.1.100. Which command accomplishes this task?"
        ),
        "options": [
            {
                "id": "a",
                "text": "copy running-config tftp://192.168.1.100/router-backup.cfg",
                "correct": True,
                "rationale": (
                    "Correct. 'copy running-config tftp:' initiates a TFTP upload of the running "
                    "configuration to the specified TFTP server. The URL format "
                    "'tftp://server/filename' specifies the destination. TFTP uses UDP port 69 and "
                    "does not require authentication, making it suitable for simple file transfers "
                    "within a trusted network."
                ),
            },
            {
                "id": "b",
                "text": "copy tftp://192.168.1.100/router-backup.cfg running-config",
                "correct": False,
                "rationale": (
                    "Incorrect. This command copies FROM the TFTP server TO the running configuration "
                    "(a restore operation), which is the reverse of what is needed. "
                    "The syntax is 'copy <source> <destination>'."
                ),
            },
            {
                "id": "c",
                "text": "write network 192.168.1.100",
                "correct": False,
                "rationale": (
                    "Incorrect. 'write network' is a legacy command used in older IOS versions to save "
                    "configuration via TFTP, but it is deprecated in modern IOS. The current best practice "
                    "is 'copy running-config tftp:'. Additionally, the syntax shown is incomplete."
                ),
            },
            {
                "id": "d",
                "text": "archive config tftp://192.168.1.100/router-backup.cfg",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'archive' command on Cisco IOS is used to configure automatic "
                    "configuration archiving (with 'archive path', 'archive time-period', etc.), "
                    "not to initiate a one-time TFTP backup. There is no 'archive config tftp://' syntax."
                ),
            },
        ],
        "explanation": (
            "TFTP (Trivial File Transfer Protocol) uses UDP port 69, provides no authentication or "
            "encryption, and is used for simple file transfers in trusted environments. Cisco IOS uses "
            "TFTP to copy IOS images, configuration files, and other files. Syntax: "
            "'copy <source> <destination>' where source/destination can be running-config, startup-config, "
            "tftp:, flash:, etc. FTP (port 21) provides authentication and is preferred when security "
            "is needed; configure with 'ip ftp username' and 'ip ftp password'."
        ),
    },
    {
        "id": "cd4-019",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TFTP/FTP",
        "stem": (
            "A network engineer needs to upgrade the IOS image on a router. The new image file is 45 MB. "
            "The engineer has access to both a TFTP server and an FTP server. Which statement BEST "
            "describes the difference between using TFTP versus FTP for this transfer?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "TFTP uses UDP and has no authentication or built-in error recovery beyond block acknowledgments; "
                    "FTP uses TCP with authentication, supports larger files reliably, and is preferred for "
                    "large IOS image transfers"
                ),
                "correct": True,
                "rationale": (
                    "Correct. TFTP uses UDP (no guaranteed delivery, no authentication) and historically had "
                    "a 32 MB file size limitation (though modern implementations extend this with larger block "
                    "sizes). FTP uses TCP (reliable delivery via retransmission), supports authentication "
                    "(username/password), and handles large files reliably. For a 45 MB image, FTP is the "
                    "more reliable and secure choice."
                ),
            },
            {
                "id": "b",
                "text": (
                    "TFTP is preferred over FTP for IOS upgrades because TFTP uses TCP, ensuring reliable "
                    "transfer of large binary files"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TFTP uses UDP, not TCP. FTP uses TCP. TFTP is not preferred for large "
                    "binary transfers precisely because it lacks TCP's reliability and error recovery "
                    "mechanisms and has file size limitations."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both TFTP and FTP provide equivalent security through community strings; the choice "
                    "depends only on server availability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Community strings are an SNMP concept, not related to TFTP or FTP. "
                    "TFTP has no authentication; FTP uses username/password. They are not equivalent "
                    "in security."
                ),
            },
            {
                "id": "d",
                "text": (
                    "FTP requires the router to initiate a control connection on TCP port 69, while "
                    "TFTP uses TCP port 21 for file data transfer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The port numbers are reversed. TFTP uses UDP port 69. FTP uses TCP "
                    "port 21 for the control connection and TCP port 20 (active mode) or a negotiated "
                    "port (passive mode) for data transfer."
                ),
            },
        ],
        "explanation": (
            "TFTP (RFC 1350): UDP port 69, no authentication, no encryption, block-based transfer with "
            "ACK per block, original 32 MB limit (TFTP option extensions in RFC 2348 support larger files). "
            "Suited for simple transfers in trusted networks (e.g., DHCP PXE boot, small config files). "
            "FTP (RFC 959): TCP ports 21 (control) and 20/dynamic (data), username/password auth, supports "
            "large files reliably. For IOS images, Cisco also supports SCP (Secure Copy Protocol) which "
            "uses SSH for encrypted transfers. Configure FTP on IOS with 'ip ftp username' and 'ip ftp password'."
        ),
    },
    {
        "id": "cd4-020",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "A network engineer reviews a QoS policy and sees that video conferencing traffic is marked "
            "DSCP AF41. The policy places AF41 traffic in a Bandwidth queue with 30% guaranteed bandwidth. "
            "An executive complains that video quality degrades during peak hours. Which change would "
            "BEST improve video conferencing quality?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Re-mark video conferencing to DSCP EF and place it in a strict Low Latency Queue (LLQ) "
                    "with a bandwidth limit (e.g., 'priority 10000')"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While EF/LLQ does provide strict priority treatment, re-marking video as EF "
                    "is not a best practice — EF is specifically recommended for voice (small, constant "
                    "rate flows). Video conferencing produces variable-rate traffic that can starve other "
                    "queues in an LLQ if not bandwidth-limited, and the 'priority' command requires "
                    "a bandwidth limit to prevent starvation, but it introduces risk of drops when "
                    "video bursts above the limit."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the guaranteed bandwidth allocation for the AF41 class and configure a "
                    "WRED (Weighted Random Early Detection) drop policy to manage congestion before "
                    "tail-drop occurs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. For interactive video (AF4x class), increasing the minimum guaranteed "
                    "bandwidth ensures sufficient capacity during peak hours. Adding WRED specifically "
                    "tuned to AF41 (lower drop threshold) provides active queue management — "
                    "WRED drops packets early before queue overflow, signaling TCP sources to back off "
                    "while preserving video flows. This is the RFC 4594 recommendation for video "
                    "conferencing: AF41 with WRED, not EF/LLQ."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Move video conferencing to DSCP CS1 (Class Selector 1) to separate it from "
                    "other Assured Forwarding classes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CS1 (DSCP 8) is defined for 'scavenger' or low-priority background "
                    "traffic (e.g., peer-to-peer). Reclassifying video to CS1 would give it lower "
                    "priority than best-effort traffic (CS0/DSCP 0), severely degrading quality."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure policing on the video class to enforce a hard cap of exactly 30% of link "
                    "bandwidth, dropping all packets above the rate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Policing the video class to 30% of bandwidth with hard drops would "
                    "worsen quality during periods when video genuinely needs more bandwidth. "
                    "Policing causes packet loss and retransmission (for TCP flows) or visible "
                    "degradation (for UDP-based video). The goal is to guarantee minimum bandwidth "
                    "and manage congestion gracefully, not to impose a strict cap."
                ),
            },
        ],
        "explanation": (
            "RFC 4594 QoS design guidelines: Voice RTP → DSCP EF (strict priority, small constant rate); "
            "Interactive video conferencing → DSCP AF41 (assured forwarding, variable rate, WRED); "
            "Streaming video → DSCP AF31; Bulk data → DSCP AF11; Scavenger → DSCP CS1. "
            "WRED performs probabilistic early discard based on average queue depth, preventing "
            "TCP global synchronization and tail-drop. For video, WRED is tuned to the AF class "
            "drop precedence (AF41 > AF42 > AF43 drop probability order)."
        ),
    },
    {
        "id": "cd4-021",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "Select TWO statements that are TRUE about Cisco IOS syslog configuration and behavior."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Severity level 0 (Emergency) is the most severe syslog level; severity level 7 (Debugging) "
                    "is the least severe and generates the highest volume of messages"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Syslog severity 0 (Emergency) = most critical, system unusable. "
                    "Severity 7 (Debugging) = least critical, highest volume, used for troubleshooting. "
                    "The mnemonic is Every Awesome Cisco Engineer Will Need Ice-cream Daily "
                    "(Emergency=0, Alert=1, Critical=2, Error=3, Warning=4, Notice=5, Informational=6, Debugging=7)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The 'logging buffered' command stores syslog messages in NVRAM so they persist across reloads"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging buffered' stores messages in RAM (the internal log buffer), "
                    "not NVRAM. The buffer is cleared on reload. To view buffered logs: 'show logging'. "
                    "For persistent logging across reloads, an external syslog server is required."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Each syslog message includes a facility code and a severity level in its header, "
                    "allowing the syslog server to filter and route messages appropriately"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Syslog messages (RFC 5424 / RFC 3164) include a PRIVAL field encoding both "
                    "facility (0-23) and severity (0-7). Cisco IOS syslog messages embed facility and "
                    "severity in the message format (%FACILITY-SEVERITY-MNEMONIC). Syslog servers use "
                    "these fields to categorize, filter, and alert on messages."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configuring 'logging console 7' and 'logging trap 3' on the same router sends all "
                    "messages (0-7) to both the console and the syslog server equally"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Console and trap (remote syslog) logging thresholds are independent. "
                    "'logging console 7' sends levels 0-7 to the console; 'logging trap 3' sends only "
                    "levels 0-3 to the syslog server. They have different effective message sets."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS syslog destinations: console (logging console), VTY (logging monitor), "
            "internal buffer (logging buffered), and remote server (logging host / logging trap). "
            "Each has an independent severity threshold. Buffered logs are in RAM and lost on reload. "
            "Syslog message format: %FACILITY-SEVERITY-MNEMONIC: message text. "
            "Severity 0-7: Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debugging."
        ),
    },
    {
        "id": "cd4-022",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "SNMP",
        "stem": (
            "A network administrator is configuring SNMPv3 on a Cisco router. Select TWO statements "
            "that correctly describe SNMPv3 security features compared to SNMPv2c."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SNMPv3 with the 'authPriv' security level provides both message authentication "
                    "(using HMAC-MD5 or HMAC-SHA) and encryption (using DES or AES), "
                    "preventing both tampering and eavesdropping"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SNMPv3 defines three security levels: noAuthNoPriv (no security), "
                    "authNoPriv (authentication only with HMAC), and authPriv (authentication + "
                    "encryption). authPriv uses HMAC-MD5 or HMAC-SHA for integrity and DES, 3DES, "
                    "or AES for confidentiality. SNMPv2c provides none of these — community strings "
                    "and PDU content are transmitted in cleartext."
                ),
            },
            {
                "id": "b",
                "text": (
                    "SNMPv3 replaces community strings with named user accounts, each associated with "
                    "a security level and optional authentication/privacy credentials"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SNMPv3 introduces the User-based Security Model (USM). Instead of "
                    "community strings, access is controlled by user accounts defined with "
                    "'snmp-server user <name> <group> v3 auth <alg> <pass> priv <alg> <pass>'. "
                    "Each user belongs to an SNMPv3 group with an associated security level and VACM "
                    "view, providing granular access control."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SNMPv3 uses TCP port 162 for all management operations to ensure reliable delivery, "
                    "whereas SNMPv2c uses UDP"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv3 still uses UDP, just like SNMPv1 and SNMPv2c. Port 161 is used "
                    "for SNMP queries (GET, SET) and port 162 for notifications (traps, informs). "
                    "SNMPv3 does not change the transport protocol."
                ),
            },
            {
                "id": "d",
                "text": (
                    "SNMPv3 eliminates the concept of MIBs and OIDs, replacing them with a "
                    "YANG/NETCONF data model for improved interoperability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv3 retains MIBs and OIDs for data modeling. YANG and NETCONF are "
                    "separate network management protocols (model-driven programmability) that are "
                    "unrelated to SNMP version. SNMPv3 is an enhancement of the SNMP framework, "
                    "not a replacement of its data modeling approach."
                ),
            },
        ],
        "explanation": (
            "SNMPv3 key improvements over SNMPv2c: (1) User Security Model (USM) — named users replace "
            "community strings; (2) authPriv security level — HMAC authentication + AES/DES encryption; "
            "(3) View-based Access Control Model (VACM) — restricts which MIB objects each user can access; "
            "(4) Message timeliness protection — prevents replay attacks. SNMPv3 configuration on Cisco IOS: "
            "'snmp-server group', 'snmp-server user', 'snmp-server host ... version 3 priv'. "
            "Transport remains UDP 161/162."
        ),
    },
]
