QUESTIONS = [
    # ------------------------------------------------------------------ cd4v2-001
    {
        "id": "cd4v2-001",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "A company has one public IP address (203.0.113.5) assigned to its router's GigabitEthernet0/0 "
            "(WAN) interface. One hundred internal hosts share this single address for Internet access using "
            "PAT. After 10 minutes, 'show ip nat translations' shows zero entries for a host that was "
            "actively browsing just moments ago. Which is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The dynamic PAT translation for that host timed out due to inactivity; "
                    "the default UDP NAT timeout is 300 seconds and TCP is 86400 seconds"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The default TCP NAT translation timeout is 86400 seconds (24 hours), "
                    "far longer than 10 minutes. The default UDP NAT timeout is 300 seconds (5 minutes). "
                    "If the host stopped generating traffic, a UDP session could expire in 5 minutes, "
                    "but an active TCP session would persist far longer. This answer partially confuses the timeouts."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The translation was removed because PAT only maintains entries while traffic is actively "
                    "flowing; an idle TCP connection's entry is aged out after the default 60-second "
                    "half-open (FIN-wait) timeout if a TCP teardown was detected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cisco IOS PAT translation entries are dynamic and maintained per-session. "
                    "When a TCP session completes its FIN/RST exchange, IOS detects the teardown and "
                    "removes the translation entry quickly (default tcp-fin-rst timeout is 60 seconds). "
                    "If browsing stopped and the TCP connections closed normally, those translations "
                    "would be removed upon FIN detection, leaving no entries visible in 'show ip nat translations'."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The PAT table reached its maximum of 64,511 concurrent entries and flushed the oldest "
                    "entries to make room for new sessions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While Cisco IOS does have PAT port limits per inside-global address "
                    "(approximately 64,000 port translations), with only 100 hosts this limit is unlikely "
                    "to be reached. The scenario describes zero entries for a specific host, "
                    "not a global table flush."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Static NAT entries take precedence over PAT entries; since a static NAT entry exists "
                    "for 203.0.113.5, the dynamic PAT entry was overwritten"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a PAT overload configuration. Static NAT entries "
                    "do coexist with dynamic PAT, but they do not overwrite or delete dynamic entries. "
                    "A static entry for the outside interface IP (203.0.113.5) would conflict with "
                    "the PAT overload configuration, but that would prevent PAT from functioning entirely, "
                    "not remove individual host entries."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS PAT tracks per-session state. TCP translations expire after detected session teardown "
            "(FIN/RST timeout, default 60 s) or after the tcp-established timeout (86400 s by default). "
            "UDP translations expire after the udp-timeout (default 300 s). ICMP translations expire after "
            "the icmp-timeout (default 60 s). After browsing ceases and connections close, TCP translations "
            "are removed upon FIN/RST detection, yielding an empty translation table. Adjust timeouts with "
            "'ip nat translation tcp-fin-rst <seconds>' etc."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-002
    {
        "id": "cd4v2-002",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NAT/PAT",
        "stem": (
            "An engineer configures the following commands on a border router:\n"
            "  ip nat pool OUTSIDE_POOL 203.0.113.10 203.0.113.20 netmask 255.255.255.0\n"
            "  ip nat inside source list PRIV_HOSTS pool OUTSIDE_POOL\n"
            "  ip access-list standard PRIV_HOSTS\n"
            "   permit 10.0.0.0 0.255.255.255\n\n"
            "After deploying, only the first few hosts obtain translations; subsequent hosts receive "
            "no Internet access. What is MOST likely the cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The NAT pool is exhausted; with only 11 public IPs in the pool and no 'overload' "
                    "keyword, each internal host consumes one public IP — once the 11 are in use, "
                    "new translation requests fail"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Dynamic NAT without 'overload' performs one-to-one address translation. "
                    "The pool 203.0.113.10–203.0.113.20 contains 11 addresses. The 12th and subsequent "
                    "hosts will find no available pool addresses and their translation requests will be "
                    "dropped. Adding 'overload' to the nat inside source command would enable PAT, "
                    "allowing all hosts to share the pool via port multiplexing."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The access list permits an overly broad range; the router rejects NAT for "
                    "addresses outside 10.0.0.0/24 because the wildcard mask is too wide"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The wildcard mask 0.255.255.255 correctly matches the entire 10.0.0.0/8 "
                    "range (all RFC 1918 10.x.x.x addresses). The broad ACL is not the problem; "
                    "Cisco IOS uses it only to identify which traffic to translate, and matching "
                    "10.x.x.x sources is intentional. The pool exhaustion is the actual issue."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Dynamic NAT requires 'ip nat inside' on every host's interface; "
                    "hosts without this command are not translated"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip nat inside' / 'ip nat outside' are configured on the router's "
                    "interfaces (LAN-facing and WAN-facing), not on hosts. The router interfaces "
                    "identify traffic direction for NAT, regardless of how many hosts exist behind them."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The netmask 255.255.255.0 in the pool definition must match the WAN interface subnet; "
                    "if the WAN interface uses a /30, the pool netmask causes an IOS error"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The netmask in 'ip nat pool' defines the subnet of the pool addresses, "
                    "not the WAN interface subnet. It does not need to match the WAN interface mask. "
                    "IOS uses this to verify pool addresses are within the stated subnet — "
                    "203.0.113.10–203.0.113.20 are all within 203.0.113.0/24, so this is valid."
                ),
            },
        ],
        "explanation": (
            "Dynamic NAT (without overload) maps each inside host to a unique pool address one-to-one. "
            "Pool size determines the maximum concurrent translated hosts. When the pool is exhausted, "
            "new hosts cannot be translated until an existing translation times out. Adding 'overload' "
            "converts the configuration to PAT (many-to-few), allowing all hosts to share pool addresses "
            "via unique port numbers. Verify pool utilization with 'show ip nat translations' and "
            "'show ip nat statistics'."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-003
    {
        "id": "cd4v2-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "NAT/PAT",
        "stem": (
            "An engineer needs to allow external SSH access (TCP 22) to an internal server at 192.168.50.100 "
            "via the router's single public IP 198.51.100.1. Simultaneously, PAT must continue to provide "
            "Internet access for all other internal hosts. Which configuration correctly achieves BOTH goals "
            "without breaking existing PAT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ip nat inside source static 192.168.50.100 198.51.100.1\n"
                    "ip nat inside source list 10 interface GigabitEthernet0/1 overload"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Configuring a full static NAT (all protocols) for 192.168.50.100 to the "
                    "same IP used by PAT overload creates a conflict. The static entry would capture all "
                    "traffic to/from 198.51.100.1 for that host, and outbound PAT for other hosts might "
                    "conflict. Full static NAT to the PAT interface IP is not a supported design."
                ),
            },
            {
                "id": "b",
                "text": (
                    "ip nat inside source static tcp 192.168.50.100 22 198.51.100.1 22\n"
                    "ip nat inside source list 10 interface GigabitEthernet0/1 overload"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A port-specific static NAT entry (static TCP port forwarding) maps only "
                    "TCP port 22 destined for 198.51.100.1 to the internal server at 192.168.50.100:22. "
                    "This coexists with the PAT overload statement because it is protocol- and port-specific. "
                    "Inbound SSH reaches the server; outbound PAT continues to work for other traffic. "
                    "Cisco IOS evaluates static entries before dynamic PAT entries."
                ),
            },
            {
                "id": "c",
                "text": (
                    "ip nat outside source static 198.51.100.1 192.168.50.100\n"
                    "ip nat inside source list 10 interface GigabitEthernet0/1 overload"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip nat outside source static' translates the SOURCE address of packets "
                    "originating from the outside (i.e., translates 198.51.100.1 to 192.168.50.100 as "
                    "the packet enters the router from outside). This does not forward inbound SSH "
                    "to the server; it is used in different, unusual scenarios involving outside address translation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "ip nat inside destination static 198.51.100.1 22 192.168.50.100 22\n"
                    "ip nat inside source list 10 interface GigabitEthernet0/1 overload"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip nat inside destination' is not a standard Cisco IOS NAT command for "
                    "port forwarding. The correct command for static port forwarding is "
                    "'ip nat inside source static tcp <inside-local> <port> <inside-global> <port>'. "
                    "The syntax in this option is invalid."
                ),
            },
        ],
        "explanation": (
            "Port-forwarding static NAT ('ip nat inside source static tcp/udp <inside-ip> <inside-port> "
            "<outside-ip> <outside-port>') creates a protocol-specific static entry that coexists with "
            "dynamic PAT. Cisco IOS checks static entries first. Only matching TCP port 22 traffic is "
            "forwarded to the server; all other outbound traffic uses PAT overload as normal. "
            "This is a common design for hosting services on a single public IP shared with PAT."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-004
    {
        "id": "cd4v2-004",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTP",
        "stem": (
            "A network engineer issues 'show ntp associations' on Router R3 and observes:\n"
            "  address         ref clock    st  when  poll  reach  delay  offset  disp\n"
            "  *~10.0.0.1      .GPS.         1   15    64   377    1.2    -0.5    0.8\n"
            "   ~10.0.0.2      10.0.0.1      2   22    64   377    2.1    -1.1    1.2\n\n"
            "What does the asterisk (*) next to 10.0.0.1 indicate, and what is R3's stratum?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The asterisk means 10.0.0.1 is the currently selected synchronization source; "
                    "R3's stratum is 2 because 10.0.0.1 is stratum 1"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In 'show ntp associations', the asterisk (*) marks the peer that the "
                    "local device has selected as its best (current) time source — the one it is "
                    "actively synchronized to. 10.0.0.1 shows stratum 1 (ref clock .GPS.), so R3 "
                    "synchronizes to a stratum-1 source and therefore R3 becomes stratum 2. "
                    "The tilde (~) prefix indicates a configured server."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The asterisk means 10.0.0.1 is an NTP master configured with 'ntp master'; "
                    "R3's stratum is 1 because it references a GPS source"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The asterisk in 'show ntp associations' marks the currently selected "
                    "synchronization peer, not an 'ntp master' configuration. R3's own stratum is "
                    "one greater than its selected source (stratum 1 + 1 = stratum 2). R3 does not "
                    "directly reference GPS."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The asterisk indicates that 10.0.0.1 is unreachable; reach value 377 shows "
                    "100% packet loss and R3 is unsynchronized (stratum 16)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A reach value of 377 (octal) is the best possible value, meaning "
                    "the last 8 NTP polls all received responses (all bits set in the 8-bit shift "
                    "register). This indicates full reachability, not packet loss. The asterisk "
                    "confirms successful synchronization, not failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The asterisk means 10.0.0.1 is a backup source; R3 prefers 10.0.0.2 as its "
                    "primary and is stratum 3"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The asterisk marks the currently ACTIVE (selected) synchronization "
                    "source — the peer with the best quality metrics (lowest stratum, lowest offset, "
                    "best reachability). R3 selected 10.0.0.1 over 10.0.0.2 because it is stratum 1 "
                    "versus stratum 2, making 10.0.0.1 the primary, not a backup."
                ),
            },
        ],
        "explanation": (
            "'show ntp associations' symbols: * = selected synchronization source (current peer), "
            "+ = candidate peer, ~ = configured server, # = distance exceeds maximum. "
            "The 'reach' column is an octal representation of the last 8 poll results; 377 (octal) "
            "= 11111111 binary = 100% success. The 'st' column is the peer's stratum. "
            "The local device's own stratum = selected peer's stratum + 1. "
            "R3 selects the best peer via the NTP clock selection algorithm (lowest stratum, "
            "smallest offset/jitter, best reachability)."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-005
    {
        "id": "cd4v2-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTP",
        "stem": (
            "An engineer wants to configure NTP authentication on Router R1 so that R1 only "
            "synchronizes to a trusted NTP server at 192.168.1.1. Which set of commands on R1 is "
            "CORRECT and COMPLETE for authenticated NTP synchronization?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ntp authenticate\n"
                    "ntp authentication-key 1 md5 SecretKey\n"
                    "ntp trusted-key 1\n"
                    "ntp server 192.168.1.1 key 1"
                ),
                "correct": True,
                "rationale": (
                    "Correct. NTP authentication requires four steps: (1) enable authentication "
                    "globally with 'ntp authenticate', (2) define the key and algorithm with "
                    "'ntp authentication-key <id> md5 <password>', (3) mark the key as trusted "
                    "with 'ntp trusted-key <id>', and (4) reference the key when specifying the "
                    "server with 'ntp server <ip> key <id>'. All four steps are required; "
                    "missing any one causes authentication to fail silently or the association "
                    "to fail entirely."
                ),
            },
            {
                "id": "b",
                "text": (
                    "ntp authentication-key 1 md5 SecretKey\n"
                    "ntp server 192.168.1.1 key 1"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This configuration is missing both 'ntp authenticate' (which globally "
                    "enables NTP authentication enforcement) and 'ntp trusted-key 1' (which designates "
                    "key 1 as acceptable). Without 'ntp authenticate', IOS may still synchronize without "
                    "verifying authentication. Without 'ntp trusted-key', the key is defined but not "
                    "designated as trusted, causing authentication to fail."
                ),
            },
            {
                "id": "c",
                "text": (
                    "ntp authenticate\n"
                    "ntp authentication-key 1 sha256 SecretKey\n"
                    "ntp server 192.168.1.1"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The 'ntp server' command does not reference the key ('key 1' is missing), "
                    "so IOS will not use authentication when polling 192.168.1.1. Additionally, "
                    "'ntp trusted-key' is absent. Cisco IOS NTP authentication uses MD5; "
                    "SHA256 may not be supported in all IOS versions for NTP authentication."
                ),
            },
            {
                "id": "d",
                "text": (
                    "ntp trusted-key 1\n"
                    "ntp server 192.168.1.1 key 1 prefer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This configuration is missing 'ntp authenticate' and "
                    "'ntp authentication-key 1 md5 <password>'. Without defining the key content, "
                    "IOS cannot perform HMAC-MD5 calculation. 'ntp trusted-key' alone without the "
                    "key definition references a non-existent key."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS NTP authentication (MD5) requires all four commands: "
            "'ntp authenticate' (enables enforcement), 'ntp authentication-key <id> md5 <secret>' "
            "(defines the key), 'ntp trusted-key <id>' (marks it as acceptable), and "
            "'ntp server <ip> key <id>' (associates the key with the server). "
            "The matching authentication-key and trusted-key must also be configured on the NTP server. "
            "Authentication prevents synchronization to rogue NTP sources."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-006
    {
        "id": "cd4v2-006",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A host on a corporate network has the following IP configuration:\n"
            "  IP address:      172.16.5.100\n"
            "  Subnet mask:     255.255.255.0\n"
            "  Default gateway: 172.16.5.1\n"
            "  DNS server:      10.1.1.53\n\n"
            "The host can ping 8.8.8.8 successfully but cannot reach 'intranet.corp.local' "
            "or 'www.google.com' by name. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The default gateway 172.16.5.1 is blocking DNS traffic on UDP port 53"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. If the gateway were blocking UDP 53, DNS queries would fail for all "
                    "names. However, the key fact is that pinging 8.8.8.8 by IP address works, "
                    "confirming routing is functional. The issue is specifically name resolution, "
                    "not routing or gateway filtering."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The DNS server at 10.1.1.53 is unreachable or not responding; "
                    "the host cannot resolve any hostnames because DNS queries to 10.1.1.53 are failing"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The host can reach 8.8.8.8 by IP (routing works), but name resolution "
                    "fails for both internal and external names. This points to a DNS server problem — "
                    "either 10.1.1.53 is unreachable from 172.16.5.0/24, the DNS service is down, "
                    "or a firewall is blocking UDP/TCP 53 to 10.1.1.53. Since BOTH internal and "
                    "external lookups fail, the common component is the DNS server itself."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The host is missing a search domain (DNS suffix) for 'corp.local'; "
                    "www.google.com fails because it is an external FQDN not in the local zone"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A missing DNS search domain would affect short-name resolution "
                    "(e.g., 'intranet' without '.corp.local') but would not prevent resolution of "
                    "FQDNs like 'intranet.corp.local' or 'www.google.com'. Since both FQDNs fail, "
                    "the problem is not a missing search domain."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The host has a split-brain DNS issue; the internal DNS server 10.1.1.53 can "
                    "only resolve internal names, so 'www.google.com' must use a forwarder"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Split-brain (split-horizon) DNS is where internal and external views "
                    "of a name differ. Even with a split-brain design, the internal DNS server "
                    "typically forwards unknown queries to an external resolver. This would explain "
                    "external name failure only if the forwarder is misconfigured, but the scenario "
                    "describes complete DNS failure (both names), suggesting the DNS server is entirely unreachable."
                ),
            },
        ],
        "explanation": (
            "Troubleshooting name resolution: confirm IP connectivity first (ping by IP succeeds here). "
            "If ALL name lookups fail (internal and external), the DNS server is the common failure point. "
            "Verify: (1) DNS server is reachable (ping 10.1.1.53), (2) DNS service is running, "
            "(3) no ACL blocks UDP/TCP 53. If only external names fail and internal succeed, "
            "check DNS forwarder configuration. If only short names fail, check DNS search suffix. "
            "Use 'nslookup' or 'ping www.google.com' to differentiate connectivity vs. DNS issues."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-007
    {
        "id": "cd4v2-007",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "During DHCP DORA, a client sends a DHCP Discover. The DHCP server responds with an Offer "
            "containing IP 10.10.1.50/24, gateway 10.10.1.1, and lease time 8 hours. The client then "
            "sends a DHCP Request. Which statement about the DHCP Request message is TRUE?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The DHCP Request is a unicast message sent directly to the server that made the "
                    "Offer, since the client already knows the server's IP address from the Offer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The DHCP Request (the third step in DORA) is sent as a broadcast "
                    "(destination 255.255.255.255), not unicast. The client does this intentionally "
                    "so that ALL DHCP servers that sent Offers are notified. Servers whose Offers "
                    "were not selected can then return their offered addresses to their pools. "
                    "The client has not yet been assigned an IP to use for unicast sourcing."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The DHCP Request is broadcast so that all DHCP servers on the segment are notified "
                    "of which Offer was accepted; the selected server's IP appears in the 'server identifier' "
                    "option (Option 54)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The DHCP Request in the initial lease process is a broadcast so multiple "
                    "DHCP servers (all of which may have sent Offers) are informed of the client's choice. "
                    "DHCP Option 54 (server identifier) contains the IP of the chosen DHCP server. "
                    "Servers that were not selected see their IP is absent from Option 54 and withdraw "
                    "their Offer, returning the address to the available pool."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The DHCP Request message includes the client's new IP (10.10.1.50) as the "
                    "source IP address in the IP header, confirming acceptance of the offered address"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. At the Request stage, the client has not yet been officially granted "
                    "the IP address. The IP header source remains 0.0.0.0 (client does not yet own "
                    "the address). The offered IP (10.10.1.50) appears in the 'requested IP address' "
                    "option (DHCP Option 50) within the DHCP payload, not in the IP header."
                ),
            },
            {
                "id": "d",
                "text": (
                    "After receiving the Offer, the client immediately applies the offered IP to its "
                    "interface and sends the Request as a unicast to test reachability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The client does not apply the offered IP until it receives the "
                    "Acknowledgment (ACK) — the fourth and final step of DORA. Applying the IP "
                    "before the ACK would risk address conflicts if the server rejects the request "
                    "or if multiple servers sent conflicting offers."
                ),
            },
        ],
        "explanation": (
            "DHCP DORA process: (1) Discover — client broadcasts from 0.0.0.0 to 255.255.255.255; "
            "(2) Offer — server unicasts/broadcasts an available IP to the client (by MAC address); "
            "(3) Request — client BROADCASTS to accept one Offer and notify all other servers "
            "(Option 54 identifies the selected server); "
            "(4) Acknowledge — selected server unicasts/broadcasts the final lease confirmation. "
            "The client applies the IP only after receiving the ACK. "
            "Lease renewal (at T1 = 50% of lease time) uses unicast directly to the server."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-008
    {
        "id": "cd4v2-008",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A Cisco router is configured as a DHCP server. An administrator issues "
            "'show ip dhcp conflict' and sees an entry for 10.1.1.25. What does this indicate, "
            "and what administrative action should be taken?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "10.1.1.25 was offered to a client but the client did not send a DHCP Request; "
                    "the address is automatically re-added to the pool after the lease timeout"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An address that was offered but not requested does not appear in "
                    "the conflict table — it simply returns to the pool when the offer expires. "
                    "The conflict table specifically records addresses that the DHCP server detected "
                    "as already in use (via ping or gratuitous ARP probe) before assignment, "
                    "or that returned a DHCP Decline from a client."
                ),
            },
            {
                "id": "b",
                "text": (
                    "10.1.1.25 was detected as already in use (via ping or client DHCP Decline) and "
                    "has been withdrawn from the pool; the administrator must issue "
                    "'clear ip dhcp conflict 10.1.1.25' after resolving the conflict to return "
                    "it to the pool"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cisco IOS DHCP server pings addresses before offering them (conflict "
                    "detection). If a ping response is received, the address is marked as conflicted "
                    "and placed in the conflict log — it will not be offered again. A client can also "
                    "send a DHCP Decline if it detects via ARP that the offered address is in use. "
                    "The administrator must resolve the conflict (remove/reconfigure the static device "
                    "using that IP) and then 'clear ip dhcp conflict 10.1.1.25' to return it to the pool."
                ),
            },
            {
                "id": "c",
                "text": (
                    "10.1.1.25 is currently leased to a client and will be listed here until the "
                    "lease expires; 'show ip dhcp binding' shows the same entries as 'show ip dhcp conflict'"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Active leases appear in 'show ip dhcp binding', not in "
                    "'show ip dhcp conflict'. The conflict table is separate and contains only "
                    "addresses flagged as conflicted (in use by a non-DHCP device), "
                    "preventing them from being offered to DHCP clients."
                ),
            },
            {
                "id": "d",
                "text": (
                    "10.1.1.25 was excluded with 'ip dhcp excluded-address' and the conflict table "
                    "mirrors the exclusion list for reference"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Excluded addresses (configured with 'ip dhcp excluded-address') are "
                    "never offered and do not appear in the conflict table. The conflict table records "
                    "addresses that were in the pool but were detected in use, causing the DHCP server "
                    "to withdraw them from future offers."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS DHCP conflict detection: before offering an address, the server sends ICMP pings. "
            "If a response is received, the address is logged in the conflict table and withheld from the pool. "
            "Clients send DHCP Decline (with Option 50 = conflicting IP) when they detect an ARP conflict "
            "after receiving an Offer. Both mechanisms populate 'show ip dhcp conflict'. "
            "Conflicts must be manually cleared with 'clear ip dhcp conflict {<ip> | *}' after the "
            "underlying IP conflict is resolved. Avoid conflicts by using 'ip dhcp excluded-address' "
            "for all statically assigned addresses."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-009
    {
        "id": "cd4v2-009",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SNMP",
        "stem": (
            "A network engineer configures the following on a Cisco router:\n"
            "  snmp-server community PUBLIC ro\n"
            "  snmp-server community PRIVATE rw\n"
            "  snmp-server host 10.5.5.5 version 2c PUBLIC\n\n"
            "The NMS at 10.5.5.5 can read MIB values but cannot modify interface descriptions via SNMP. "
            "Which change would allow the NMS to make SNMP Set operations?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Change the 'snmp-server host' statement to use the PRIVATE community: "
                    "snmp-server host 10.5.5.5 version 2c PRIVATE"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The 'snmp-server host' statement defines the destination for "
                    "unsolicited notifications (traps/informs) sent from the router to the NMS — "
                    "it does not control what community string the NMS uses when sending Set requests "
                    "TO the router. Changing the trap destination community does not enable Set operations."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The NMS must use the 'PRIVATE' read-write community string when sending "
                    "SNMP Set requests; no router configuration change is needed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The router already has a read-write community 'PRIVATE' configured. "
                    "The NMS needs to use this RW community string in its SNMP Set PDUs directed "
                    "to the router on UDP port 161. The 'PUBLIC' community is read-only (ro) and "
                    "rejects Set operations. The fix is on the NMS side — configure it to use "
                    "'PRIVATE' for write operations."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add 'snmp-server enable traps snmp set' to the router to enable Set trap notifications"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'snmp-server enable traps' controls which events generate notifications "
                    "(traps) sent from the device. It has no effect on whether the SNMP agent accepts "
                    "or rejects Set requests. The issue is the community string permissions, not trap configuration."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Replace the SNMPv2c communities with SNMPv3 users; SNMPv2c read-write communities "
                    "are deprecated and not functional on modern IOS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv2c read-write communities are fully functional on Cisco IOS. "
                    "While SNMPv3 is the security best practice, SNMPv2c RW communities work "
                    "and the correct diagnosis here is that the NMS is using the wrong (read-only) "
                    "community for Set operations, not that RW communities are broken."
                ),
            },
        ],
        "explanation": (
            "SNMPv2c uses community strings as a form of access control. Read-only (ro) communities "
            "permit Get, GetNext, and GetBulk operations but reject Set operations (the agent returns "
            "a 'noAccess' or 'readOnly' error). Read-write (rw) communities allow all operations "
            "including Set. The NMS must use the correct community string in each PDU. "
            "The 'snmp-server host' line controls outbound notifications from the router to the NMS "
            "(traps/informs) and does not affect inbound Get/Set operation authentication."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-010
    {
        "id": "cd4v2-010",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SNMP",
        "stem": (
            "An NMS requires confirmation that SNMP notifications were received by the management station. "
            "SNMP traps are currently configured but the operations team reports occasional missed "
            "notifications. Which SNMP feature should be configured to ensure reliable notification delivery, "
            "and on which SNMP version(s) is it available?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SNMP Informs, available in SNMPv2c and SNMPv3; the NMS sends an acknowledgment "
                    "to the agent, and the agent retransmits if no acknowledgment is received"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Unlike traps (fire-and-forget, no acknowledgment), SNMP Informs "
                    "require the receiving NMS to send an acknowledgment (InformResponse PDU). "
                    "If the agent does not receive an acknowledgment within a timeout period, "
                    "it retransmits the Inform. Informs are available in SNMPv2c and SNMPv3, "
                    "but NOT in SNMPv1. Configure with: 'snmp-server host <ip> informs version 2c <community>'."
                ),
            },
            {
                "id": "b",
                "text": (
                    "SNMP Informs, available only in SNMPv3 with authPriv security; SNMPv2c traps "
                    "can be made reliable by switching to TCP transport"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP Informs are available in both SNMPv2c and SNMPv3, not "
                    "exclusively in SNMPv3. Additionally, SNMP does not use TCP — it uses UDP "
                    "for all versions. There is no TCP transport option for standard SNMP."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SNMP bulk transfers, which retransmit all MIB data if a trap is missed; "
                    "configure with 'snmp-server enable bulk-transfer'"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GetBulk is an NMS-initiated operation to efficiently retrieve "
                    "large tables by reducing the number of round trips. It is not related to "
                    "notification reliability. There is no 'snmp-server enable bulk-transfer' command "
                    "for trap retransmission."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the SNMP trap queue size on the router with 'snmp-server trap-source' "
                    "to buffer and retransmit missed traps automatically"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'snmp-server trap-source' specifies which interface IP to use "
                    "as the source address of SNMP traps — it does not control queue size or "
                    "retransmission. Standard SNMP traps have no built-in retransmission mechanism. "
                    "Only SNMP Informs provide acknowledged, retransmittable notifications."
                ),
            },
        ],
        "explanation": (
            "SNMP notification types: Traps (SNMPv1/v2c/v3) — UDP, unacknowledged, no retransmit; "
            "Informs (SNMPv2c/v3) — UDP, acknowledged by NMS (InformResponse), retransmitted if no ACK. "
            "Informs consume more router resources (must store notification until ACK received). "
            "Configure Informs on Cisco IOS: 'snmp-server host <ip> informs version 2c <community>' or "
            "'snmp-server host <ip> informs version 3 priv <username>'. "
            "Note: Informs are NOT available in SNMPv1."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-011
    {
        "id": "cd4v2-011",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "A Cisco router generates this syslog message:\n"
            "  %SYS-2-MALLOCFAIL: Memory allocation of 65536 bytes failed from 0x...\n\n"
            "Which severity level is this message, what is its name, and which logging destination "
            "threshold would cause this message to be SUPPRESSED from reaching the syslog server?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Severity 2 (Critical); the message is suppressed if 'logging trap 1' is configured "
                    "because level 1 (Alert) excludes level 2 and above"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The '-2-' in '%SYS-2-MALLOCFAIL' indicates severity 2, which is 'Critical'. "
                    "Syslog thresholds work inclusively downward: 'logging trap 1' sends only levels "
                    "0 (Emergency) and 1 (Alert) to the syslog server. Severity 2 (Critical) has a "
                    "higher number and is excluded when the threshold is set to 1. "
                    "This is a serious message indicating a memory allocation failure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Severity 2 (Critical); the message is suppressed if 'logging trap 3' is configured "
                    "because level 3 (Error) is less severe than Critical"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging trap 3' sets the threshold to severity 3 (Error). Since "
                    "severity 2 (Critical) is numerically lower (more severe) than 3, it WOULD be "
                    "sent to the syslog server, not suppressed. Suppression requires a threshold "
                    "numerically LOWER than the message severity (e.g., threshold 1 suppresses level 2)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Severity 2 (Warning); it would be suppressed by 'logging trap 4' "
                    "because warning messages are level 4 and below"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Severity 2 is Critical, not Warning. Warning is severity 4. "
                    "The message format encodes the severity numerically in the facility-severity-mnemonic "
                    "string. 'logging trap 4' sends levels 0-4 to the syslog server, so severity 2 "
                    "would be INCLUDED, not suppressed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Severity 2 (Alert); 'logging trap 0' would suppress it because only "
                    "Emergency messages pass threshold 0"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Severity 2 is Critical (Alert is severity 1). 'logging trap 0' sends "
                    "only Emergency (level 0) to the syslog server, so level 2 would indeed be "
                    "suppressed — but the severity name is wrong. The correct name for severity 2 is Critical."
                ),
            },
        ],
        "explanation": (
            "Syslog severity levels: 0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, "
            "5=Notice (Notification), 6=Informational, 7=Debugging. "
            "The severity is encoded in the syslog message header as '-N-'. "
            "%SYS-2-MALLOCFAIL: facility=SYS, severity=2 (Critical), mnemonic=MALLOCFAIL. "
            "A memory allocation failure is a critical condition that may lead to process crashes or "
            "service interruption. 'logging trap N' forwards messages with severity <= N to the syslog server."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-012
    {
        "id": "cd4v2-012",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "An engineer needs to configure a router to send syslog messages to an external server "
            "at 172.20.0.10 using a non-default source interface and severity level 'notifications'. "
            "Which combination of commands achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "logging host 172.20.0.10\n"
                    "logging trap notifications\n"
                    "logging source-interface Loopback0"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'logging host 172.20.0.10' specifies the syslog server destination. "
                    "'logging trap notifications' (or 'logging trap 5') sets the severity threshold "
                    "to level 5 (Notifications/Notice), sending messages of severity 0-5. "
                    "'logging source-interface Loopback0' ensures all syslog packets use the "
                    "Loopback0 IP as the source, making the source consistent even if physical "
                    "interfaces change."
                ),
            },
            {
                "id": "b",
                "text": (
                    "logging 172.20.0.10\n"
                    "logging level 5\n"
                    "logging interface Loopback0"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While 'logging 172.20.0.10' is an older alias for 'logging host', "
                    "the commands 'logging level 5' and 'logging interface Loopback0' are not valid "
                    "Cisco IOS syntax. The correct commands are 'logging trap 5' (or 'logging trap notifications') "
                    "and 'logging source-interface Loopback0'."
                ),
            },
            {
                "id": "c",
                "text": (
                    "logging host 172.20.0.10\n"
                    "logging trap 6\n"
                    "logging source-interface Loopback0"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging trap 6' sets the threshold to Informational (level 6), "
                    "which sends levels 0-6 — more messages than 'notifications' (levels 0-5). "
                    "The question specifically requires severity level 'notifications' (level 5, "
                    "not 6). This configuration over-delivers by one severity level."
                ),
            },
            {
                "id": "d",
                "text": (
                    "logging server 172.20.0.10 severity notifications\n"
                    "logging origin-id Loopback0"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging server' is not a standard Cisco IOS command; the correct "
                    "command is 'logging host'. 'logging origin-id' adds an origin identifier to "
                    "syslog messages but does not specify the source interface IP. These are not "
                    "valid IOS commands for this purpose."
                ),
            },
        ],
        "explanation": (
            "Syslog configuration on Cisco IOS: "
            "'logging host <ip>' — destination syslog server; "
            "'logging trap <level|name>' — severity threshold for remote syslog (level 5 = notifications/notice); "
            "'logging source-interface <intf>' — ensures a consistent source IP for syslog packets. "
            "Severity names: emergencies(0), alerts(1), critical(2), errors(3), warnings(4), "
            "notifications(5), informational(6), debugging(7). "
            "Using a Loopback as source interface is best practice for stability."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-013
    {
        "id": "cd4v2-013",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP relay (ip helper-address)",
        "stem": (
            "A router configured as DHCP relay ('ip helper-address') is forwarding client Discover "
            "messages to the DHCP server. The DHCP server's 'debug ip dhcp server packet' output "
            "shows it receiving Discovers with GIADDR = 0.0.0.0 instead of the relay agent's "
            "interface IP. As a result, the server cannot determine which pool to use. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The 'ip helper-address' command is configured on the wrong interface — "
                    "it was placed on the WAN-facing (outside) interface instead of the "
                    "LAN-facing (inside) interface where client broadcasts arrive"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The 'ip helper-address' must be on the interface where DHCP client "
                    "broadcasts are received (the LAN or SVI interface). When the relay agent "
                    "intercepts a broadcast Discover, it populates the GIADDR field with the "
                    "IP address of THAT interface before forwarding to the server. If the command "
                    "is on the wrong interface, the router does not intercept client broadcasts, "
                    "and if they somehow reach the server (e.g., in a one-segment scenario), "
                    "GIADDR remains 0.0.0.0."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The DHCP server requires 'ip dhcp relay giaddr fill' to be configured globally "
                    "to populate the GIADDR field"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'ip dhcp relay giaddr fill' command in Cisco IOS. "
                    "The relay agent (router with ip helper-address) automatically populates "
                    "GIADDR with the ingress interface IP — this is fundamental DHCP relay behavior "
                    "per RFC 2131 and requires no additional configuration."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The DHCP client must be configured to include its subnet information in the "
                    "Discover so the server can select the correct pool regardless of GIADDR"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP clients send minimal information in the Discover — they do not "
                    "know their subnet (that is what they are trying to obtain). The server relies "
                    "on GIADDR from the relay agent to identify the client subnet and select the "
                    "appropriate pool. Clients do not supply subnet information independently."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The 'ip forward-protocol udp 67' command is missing; without it, "
                    "GIADDR is not set by the relay agent"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip forward-protocol udp 67' was used with the older 'ip helper-address' "
                    "behavior to enable forwarding of specific UDP protocols, but modern IOS includes "
                    "UDP 67 (DHCP) in the default helper-address forwarding list. 'ip forward-protocol' "
                    "does not control GIADDR population."
                ),
            },
        ],
        "explanation": (
            "The GIADDR (Gateway IP Address) field in DHCP is populated by the relay agent with the "
            "IP address of the interface on which the DHCP broadcast was received. The DHCP server "
            "uses GIADDR to identify the client's subnet and select the matching address pool. "
            "If GIADDR = 0.0.0.0, the relay agent did not process the packet (it was not on the "
            "correct interface). 'ip helper-address' must be on the LAN-facing interface, not the uplink. "
            "Verify with: 'show running-config interface <int>' to confirm helper placement."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-014
    {
        "id": "cd4v2-014",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP relay (ip helper-address)",
        "stem": (
            "By default, Cisco IOS 'ip helper-address' forwards not only DHCP (UDP 67/68) but also "
            "several other UDP services. An engineer wants to restrict the relay to ONLY DHCP traffic "
            "and prevent TFTP (UDP 69) and other services from being relayed. Which approach achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Use 'no ip forward-protocol udp 69' (and for each non-DHCP service port) to remove "
                    "those ports from the default helper-address forwarding list, leaving only UDP 67/68"
                ),
                "correct": True,
                "rationale": (
                    "Correct. By default, 'ip helper-address' relays the following UDP ports: "
                    "37 (time), 49 (TACACS), 53 (DNS), 67 (DHCP/BOOTP server), 68 (DHCP/BOOTP client), "
                    "69 (TFTP), 137 (NetBIOS name), 138 (NetBIOS datagram). To restrict relaying to "
                    "DHCP only, the engineer must issue 'no ip forward-protocol udp' for each non-DHCP "
                    "port in the default list (e.g., 'no ip forward-protocol udp 69', "
                    "'no ip forward-protocol udp 53', etc.)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Replace 'ip helper-address' with 'ip dhcp relay address' to restrict relay to DHCP only"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip dhcp relay address' is not a standard Cisco IOS command. "
                    "The only mechanism for controlling which UDP protocols are relayed via "
                    "ip helper-address is through 'ip forward-protocol udp' and 'no ip forward-protocol udp'."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Apply an ACL to the helper interface blocking UDP ports other than 67/68; "
                    "the helper-address will only relay traffic permitted by the ACL"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. ACLs can block traffic from entering or leaving an interface, but they "
                    "operate before the helper-address relay decision. Blocking UDP ports with an ACL "
                    "would prevent those packets from being forwarded at all (including locally), "
                    "not just from being relayed. The proper mechanism is 'no ip forward-protocol udp <port>'."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure 'ip helper-address 10.0.0.1 dhcp-only' on the interface; "
                    "this restricts the relay to DHCP broadcasts exclusively"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'dhcp-only' keyword for 'ip helper-address' in Cisco IOS. "
                    "The ip helper-address command does not support protocol filtering via keywords. "
                    "Protocol filtering is controlled globally via 'no ip forward-protocol udp <port>'."
                ),
            },
        ],
        "explanation": (
            "Default UDP ports relayed by 'ip helper-address': 37, 49, 53, 67, 68, 69, 137, 138. "
            "To restrict to DHCP only, remove unneeded ports with 'no ip forward-protocol udp <port>' "
            "globally for each port except 67 and 68. This is a security best practice to prevent "
            "unintended relay of DNS, TFTP, NetBIOS, and other broadcasts across subnet boundaries. "
            "After changes, verify with 'show running-config | include forward-protocol'."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-015
    {
        "id": "cd4v2-015",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "An engineer is implementing QoS on a WAN interface and must classify traffic into three "
            "classes: VoIP (DSCP EF), business-critical applications (DSCP AF31), and everything else "
            "(default class). The policy must guarantee 30% bandwidth for business-critical and place "
            "VoIP in a strict-priority queue. Which MQC (Modular QoS CLI) policy-map structure is "
            "MOST correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "policy-map WAN-OUT\n"
                    " class VOIP\n"
                    "  priority percent 20\n"
                    " class BUSINESS\n"
                    "  bandwidth percent 30\n"
                    " class class-default\n"
                    "  fair-queue"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'priority percent 20' places VoIP in the strict low-latency queue (LLQ) "
                    "with 20% of bandwidth as the policer ceiling — traffic above this rate is dropped "
                    "during congestion. 'bandwidth percent 30' guarantees 30% minimum bandwidth for "
                    "business-critical traffic during congestion. 'class-default' with 'fair-queue' "
                    "(WFQ) provides equitable distribution for remaining traffic. "
                    "This matches the correct MQC LLQ+CBWFQ structure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "policy-map WAN-OUT\n"
                    " class VOIP\n"
                    "  bandwidth percent 20\n"
                    " class BUSINESS\n"
                    "  priority percent 30\n"
                    " class class-default\n"
                    "  queue-limit 64"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the treatment: VoIP gets 'bandwidth' (guaranteed but not "
                    "strict-priority), and the business class gets 'priority' (LLQ strict priority). "
                    "VoIP requires 'priority' (LLQ) for low latency and jitter; 'bandwidth' only "
                    "guarantees a minimum share during congestion without strict queuing priority."
                ),
            },
            {
                "id": "c",
                "text": (
                    "policy-map WAN-OUT\n"
                    " class VOIP\n"
                    "  priority percent 20\n"
                    " class BUSINESS\n"
                    "  priority percent 30\n"
                    " class class-default\n"
                    "  bandwidth percent 50"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Configuring two 'priority' classes is not valid in Cisco MQC — only "
                    "one class in a policy-map may use 'priority' (LLQ). Multiple 'priority' statements "
                    "in the same policy-map are rejected by IOS. Business applications should use "
                    "'bandwidth', not 'priority'."
                ),
            },
            {
                "id": "d",
                "text": (
                    "policy-map WAN-OUT\n"
                    " class VOIP\n"
                    "  police rate percent 20\n"
                    " class BUSINESS\n"
                    "  bandwidth percent 30\n"
                    " class class-default\n"
                    "  fair-queue"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'police rate percent 20' is a policing action (drops excess traffic) "
                    "not a queuing/scheduling action. Policing VoIP drops packets above 20% rate, "
                    "causing packet loss and jitter — the opposite of what VoIP needs. "
                    "VoIP requires the LLQ 'priority' command for strict scheduling priority, "
                    "not a policer."
                ),
            },
        ],
        "explanation": (
            "Cisco MQC LLQ + CBWFQ structure: one class uses 'priority [percent/kbps]' for LLQ "
            "(strict priority, acts as a policer ceiling during congestion); other classes use "
            "'bandwidth [percent/kbps]' for guaranteed minimum rates (CBWFQ); class-default handles "
            "remaining traffic. Only ONE 'priority' class is allowed per policy-map. "
            "LLQ is ideal for real-time traffic (VoIP); CBWFQ for guaranteed-rate traffic; "
            "WFQ/FIFO/WRED for best-effort. Apply with 'service-policy output WAN-OUT' on the interface."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-016
    {
        "id": "cd4v2-016",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "QoS (classification/marking/queuing)",
        "stem": (
            "A QoS policy classifies all HTTP/HTTPS traffic (TCP 80/443) as DSCP AF21. "
            "An engineer observes that large file downloads are causing congestion and impacting "
            "interactive web sessions. Both are marked AF21. Which QoS technique addresses this "
            "problem by distinguishing large bulk flows from interactive sessions WITHOUT reclassifying traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "WRED (Weighted Random Early Detection) tuned to preferentially drop packets "
                    "from long-lived (large) TCP flows during congestion by exploiting TCP's "
                    "congestion avoidance mechanisms"
                ),
                "correct": True,
                "rationale": (
                    "Correct. WRED drops packets probabilistically as queues fill, triggering TCP's "
                    "congestion avoidance in the affected flows. Large bulk TCP flows have larger "
                    "congestion windows and thus receive more drops, causing them to slow down more "
                    "than short interactive flows. WRED also prevents tail-drop global synchronization "
                    "(where ALL TCP flows back off simultaneously), allowing interactive sessions "
                    "to continue at adequate rates without requiring separate classification."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Configure traffic policing on AF21 to limit all HTTP/HTTPS to 1 Mbps, "
                    "ensuring no single flow dominates the link"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Policing to 1 Mbps would drop packets from both bulk and interactive "
                    "sessions equally, potentially breaking both. A hard 1 Mbps cap per-flow is not "
                    "practical and does not distinguish large from small flows without per-flow policing, "
                    "which is not what the question asks."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enable PQ (Priority Queuing) for the AF21 class to give it strict-priority "
                    "service over all other traffic, reducing congestion effects"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Priority Queuing (PQ) is an older mechanism replaced by LLQ in MQC. "
                    "More importantly, giving ALL HTTP traffic strict priority (including bulk downloads) "
                    "over other traffic would increase congestion for other classes, not solve the "
                    "intra-class congestion problem between bulk and interactive HTTP sessions."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure FIFO queuing for the AF21 class; FIFO naturally favors interactive "
                    "sessions because they send smaller packets that transit the queue faster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. FIFO processes packets in arrival order regardless of flow size. "
                    "Large bulk flows that fill the queue with back-to-back packets will delay "
                    "interactive packets waiting behind them. FIFO does not provide any differential "
                    "treatment between large and small flows within the same class."
                ),
            },
        ],
        "explanation": (
            "WRED (Weighted Random Early Detection) provides active queue management by probabilistically "
            "dropping packets before the queue is full. TCP flows respond to drops by reducing their "
            "congestion window (cwnd), slowing their sending rate. Large bulk flows are more affected "
            "because they sustain higher cwnd values and encounter more drops as queue depth increases. "
            "WRED prevents TCP global synchronization (a tail-drop failure mode where all flows "
            "simultaneously reduce rates). For DSCP-based WRED, configure per-DSCP minimum threshold, "
            "maximum threshold, and mark probability in the policy-map class."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-017
    {
        "id": "cd4v2-017",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SSH remote access",
        "stem": (
            "A network administrator configures SSH on a new router with these commands:\n"
            "  hostname R1\n"
            "  ip domain-name corp.local\n"
            "  crypto key generate rsa modulus 1024\n"
            "  ip ssh version 2\n"
            "  line vty 0 4\n"
            "   transport input ssh\n"
            "   login local\n"
            "  username admin privilege 15 secret Cisco123!\n\n"
            "An SSH client connects and authenticates successfully but is immediately disconnected "
            "without reaching the exec prompt. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The RSA key size (1024 bits) is below the SSHv2 minimum of 2048 bits; "
                    "the session is rejected after authentication"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SSHv2 on Cisco IOS requires a minimum RSA key size of 768 bits "
                    "(768-4096 supported; 2048 recommended). 1024-bit keys work with SSHv2. "
                    "A key-size issue would prevent connection establishment, not disconnect after "
                    "successful authentication."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The VTY lines are missing an 'exec-timeout' value; without it, "
                    "IOS immediately terminates the session"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The default exec-timeout is 10 minutes (600 seconds). "
                    "A missing or zero exec-timeout does not cause immediate disconnection after "
                    "authentication — in fact, 'exec-timeout 0 0' means never time out. "
                    "Immediate post-authentication disconnect has a different root cause."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The 'aaa new-model' command is configured and the default AAA authentication list "
                    "is not defined, causing authorization to fail after authentication succeeds"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. If 'aaa new-model' were enabled with no authentication list, the "
                    "result would typically be authentication failure (not post-authentication "
                    "disconnect). The scenario shows authentication succeeds, pointing to a "
                    "different issue."
                ),
            },
            {
                "id": "d",
                "text": (
                    "There is no exec process on the VTY lines; either 'no exec' is configured or "
                    "the exec shell has not been enabled for privilege 15, causing the session to "
                    "close immediately after authentication"
                ),
                "correct": True,
                "rationale": (
                    "Correct. If 'no exec' is configured under the VTY line, IOS terminates the "
                    "session immediately after the user authenticates — no exec shell is spawned. "
                    "This is a common misconfiguration. Another scenario: if privilege 15 users "
                    "are directed straight to 'access-class' that denies them, or if 'autocommand "
                    "logout' is configured, the session closes immediately. The most exam-relevant "
                    "cause is 'no exec' under the vty line, which prevents any interactive shell "
                    "from starting."
                ),
            },
        ],
        "explanation": (
            "After successful SSH authentication, IOS spawns an exec process for interactive management. "
            "If 'no exec' is configured under the VTY line (e.g., for lines used only for outbound "
            "connections or console server applications), IOS disconnects immediately after login. "
            "Other causes of immediate post-auth disconnect: 'autocommand logout', access-class "
            "restrictions, or authorization failure if aaa is configured. "
            "Verify with: 'show line vty 0 4' and 'show running-config | section line vty'. "
            "The fix is to ensure VTY lines have exec enabled (default) and no conflicting commands."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-018
    {
        "id": "cd4v2-018",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SSH remote access",
        "stem": (
            "An engineer wants to limit SSH access to a router's management interface "
            "(Management0) to only hosts in the 10.100.0.0/24 subnet. The router already has "
            "SSH configured with local authentication. Which additional configuration achieves this restriction?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ip access-list standard MGT-ACCESS\n"
                    " permit 10.100.0.0 0.0.0.255\n"
                    "line vty 0 4\n"
                    " access-class MGT-ACCESS in"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'access-class <acl> in' on VTY lines restricts incoming connections "
                    "to sources permitted by the ACL. Hosts outside 10.100.0.0/24 will be "
                    "refused at the VTY line before authentication is attempted. "
                    "This is the correct mechanism for VTY source-IP restriction on Cisco IOS. "
                    "The standard ACL matches source IPs only, which is appropriate for this use case."
                ),
            },
            {
                "id": "b",
                "text": (
                    "interface Management0\n"
                    " ip access-group MGT-ACCESS in"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Applying an inbound ACL on the Management0 interface would filter "
                    "ALL traffic entering that interface, not just SSH. This would also block "
                    "legitimate SNMP, ICMP (ping), NTP, and other management protocols. "
                    "The VTY 'access-class' command is the correct method for restricting "
                    "specifically which hosts can open VTY (SSH/Telnet) sessions."
                ),
            },
            {
                "id": "c",
                "text": (
                    "ip ssh source-interface Management0\n"
                    "ip ssh restrict source 10.100.0.0 0.0.0.255"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip ssh source-interface' specifies the source interface for "
                    "outbound SSH connections initiated BY the router (not inbound). "
                    "'ip ssh restrict source' is not a valid Cisco IOS command. "
                    "Source restriction for inbound SSH requires 'access-class' on VTY lines."
                ),
            },
            {
                "id": "d",
                "text": (
                    "crypto key generate rsa modulus 2048\n"
                    "ip ssh maxstartups 3\n"
                    "ip ssh source-interface Management0"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip ssh maxstartups' limits the number of concurrent unauthenticated "
                    "SSH sessions (DoS protection), not the source IP range. 'ip ssh source-interface' "
                    "controls the source IP for outbound SSH only. Neither command restricts inbound "
                    "SSH connections to specific source subnets."
                ),
            },
        ],
        "explanation": (
            "'access-class <acl-name|number> in' on VTY lines applies source IP filtering to "
            "incoming management connections (SSH and Telnet). Only hosts matching the ACL's "
            "permit entries can establish VTY sessions. The ACL should use standard IP (source "
            "address only) for simplicity. Extended ACLs can also be used to restrict by source "
            "AND destination. This is the primary Cisco IOS mechanism for restricting remote "
            "management access by IP address, complementing authentication controls."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-019
    {
        "id": "cd4v2-019",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TFTP/FTP",
        "stem": (
            "A network engineer issues the following command on a Cisco router:\n"
            "  copy ftp://admin:Cisco123@192.168.10.50/ios-15.7.bin flash:\n\n"
            "Which statement correctly describes the behavior and security implications of this transfer?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "FTP transfers the file over TCP with credentials and file data encrypted by default, "
                    "making it more secure than SCP for IOS image transfers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Standard FTP (RFC 959) transmits credentials (username and password) "
                    "and file data in PLAINTEXT over TCP. FTP is NOT encrypted. SCP (Secure Copy "
                    "Protocol) uses SSH for encryption and is far more secure than FTP for transferring "
                    "sensitive files such as IOS images and configuration files."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The credentials (admin:Cisco123) are transmitted in plaintext over TCP port 21 "
                    "for the control channel; the file data traverses a separate data connection "
                    "on TCP port 20 or a negotiated port, also unencrypted"
                ),
                "correct": True,
                "rationale": (
                    "Correct. FTP uses TCP port 21 for the control channel (commands including "
                    "USER and PASS sent in clear text) and TCP port 20 (active mode) or a negotiated "
                    "ephemeral port (passive mode) for file data — also unencrypted. "
                    "The entire transfer, including credentials, is visible to anyone with network access. "
                    "For sensitive environments, SCP ('copy scp://...') is preferred."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The command fails because Cisco IOS requires FTP credentials to be configured "
                    "separately with 'ip ftp username' and 'ip ftp password'; inline URL credentials "
                    "are not supported"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS supports inline FTP credentials in the URL syntax "
                    "('ftp://user:password@server/file'). This is a valid alternative to using "
                    "'ip ftp username' and 'ip ftp password' global commands. Both methods work; "
                    "inline credentials in the command take precedence over globally configured ones."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The file is downloaded over UDP port 69 because Cisco IOS internally converts "
                    "FTP requests to TFTP for efficiency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS does not convert FTP to TFTP. FTP uses TCP (ports 21 and 20/dynamic); "
                    "TFTP uses UDP port 69. They are completely separate protocols. "
                    "An FTP copy command uses FTP regardless of any TFTP server availability."
                ),
            },
        ],
        "explanation": (
            "FTP (RFC 959) uses TCP with a two-channel design: control (TCP 21) for commands and "
            "data (TCP 20 active / ephemeral passive) for file transfer. All traffic including "
            "credentials is cleartext. Cisco IOS FTP client commands: "
            "'copy ftp://[user:pass@]server/file <destination>' or configure globally with "
            "'ip ftp username <name>' and 'ip ftp password <pass>'. "
            "For secure transfers: SCP (SSH-based, encrypted) is preferred. "
            "Configure SCP server on IOS: 'ip scp server enable'. "
            "Client: 'copy scp://user@server/file flash:'."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-020
    {
        "id": "cd4v2-020",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TFTP/FTP",
        "stem": (
            "A network operations center must transfer a 200 KB router configuration file to a remote "
            "branch router across an unreliable WAN link with occasional packet loss. The NOC has both "
            "TFTP and FTP servers available. Which protocol is more appropriate for this transfer, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "TFTP, because its block-based ACK mechanism retransmits individual 512-byte "
                    "blocks on packet loss, making it resilient on lossy links"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While TFTP does have a per-block ACK mechanism with retransmission "
                    "(using a lockstep stop-and-wait protocol), its UDP-based transport and lack "
                    "of flow control make it less efficient on lossy WAN links compared to FTP's "
                    "TCP transport. TFTP stop-and-wait ACKs become extremely slow on high-latency "
                    "links. Additionally, TFTP lacks authentication, which is a concern for "
                    "transferring configuration files."
                ),
            },
            {
                "id": "b",
                "text": (
                    "FTP, because it uses TCP's reliable delivery with flow control and error recovery, "
                    "handles packet loss through retransmission transparently, and supports "
                    "authentication for configuration file security"
                ),
                "correct": True,
                "rationale": (
                    "Correct. FTP's TCP transport provides reliable, in-order delivery with automatic "
                    "retransmission, flow control (TCP window), and congestion control. On a lossy WAN, "
                    "TCP retransmits lost segments without application intervention, ensuring the "
                    "complete file arrives. FTP also provides username/password authentication, "
                    "protecting configuration files from unauthorized access. For 200 KB over "
                    "unreliable WAN, FTP's TCP reliability and authentication make it the better choice."
                ),
            },
            {
                "id": "c",
                "text": (
                    "TFTP, because it requires less overhead than FTP (no authentication handshake), "
                    "making it faster on bandwidth-constrained WAN links"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While TFTP does have lower overhead (no authentication), on a lossy "
                    "link the savings are negated by retransmissions, lockstep ACKs causing "
                    "pipeline stalls, and potential timeouts. FTP's TCP window-based flow control "
                    "is far more efficient on lossy links. Lower overhead does not equal better "
                    "performance when reliability is the primary concern."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither; only SCP should be used for configuration file transfers because "
                    "TFTP and FTP are prohibited by the CCNA security framework"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The CCNA 200-301 exam covers TFTP and FTP as valid file transfer "
                    "protocols for network device management. SCP is a more secure option but is "
                    "not the only acceptable protocol. The question asks about the better choice "
                    "between TFTP and FTP given the specific constraints, not whether alternatives exist."
                ),
            },
        ],
        "explanation": (
            "TFTP vs FTP for WAN transfers: TFTP uses UDP with stop-and-wait ACKs per 512-byte block, "
            "making it slow on high-latency or lossy links. On a 100ms RTT link, TFTP throughput for "
            "a 200KB file (390 blocks) = 390 round trips × 100ms = ~39 seconds minimum, ignoring loss. "
            "FTP uses TCP sliding window, achieving much higher throughput. FTP also provides "
            "authentication (username/password) and is more suitable for sensitive files over "
            "untrusted paths. For the most secure option, use SCP (encrypted via SSH)."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-021
    {
        "id": "cd4v2-021",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "NAT/PAT",
        "stem": (
            "A network engineer issues 'debug ip nat' and observes:\n"
            "  NAT: s=10.0.0.5->203.0.113.1, d=8.8.8.8 [1000]\n"
            "  NAT*: s=8.8.8.8, d=203.0.113.1->10.0.0.5 [1000]\n\n"
            "The asterisk (*) in the second debug line indicates what condition?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The asterisk indicates the packet was fast-switched (CEF or fast-path) and "
                    "the NAT translation was performed in the fast-switching path without "
                    "process switching"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In 'debug ip nat' output, an asterisk (*) on the translation line "
                    "indicates the packet was processed in the fast-switching or CEF (Cisco Express "
                    "Forwarding) path rather than the process-switching path. The first line (no "
                    "asterisk) is typically process-switched (slower, used for the first packet that "
                    "creates the translation entry). Subsequent packets in the same flow use fast-switching. "
                    "This is a common CCNA exam topic for interpreting NAT debug output."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The asterisk indicates the translation entry was created as a static NAT "
                    "entry and is not subject to aging or timeout"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The asterisk in 'debug ip nat' output is related to the switching "
                    "path (fast-switched vs. process-switched), not the entry type (static vs. dynamic). "
                    "Static NAT entries do not generate a different debug symbol."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The asterisk marks the return traffic (outside-to-inside direction), "
                    "distinguishing it from outbound translations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The debug output shows translation in both directions, and the "
                    "direction (inside-to-outside vs. outside-to-inside) is indicated by the "
                    "arrow notation (s->d) and the address ordering, not by the asterisk. "
                    "The asterisk denotes the switching path."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The asterisk means the translation created a new entry in the NAT table; "
                    "subsequent packets do not generate debug output"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A new translation table entry creation would be indicated on the "
                    "first (non-asterisked) line representing the process-switched initial packet. "
                    "The asterisk on subsequent lines indicates fast-switched packets, not new "
                    "table entries."
                ),
            },
        ],
        "explanation": (
            "'debug ip nat' output format: 'NAT: s=<src>-><translated>, d=<dst> [id]' for "
            "process-switched packets; 'NAT*: ...' (with asterisk) for fast-switched/CEF-switched packets. "
            "The first packet in a new flow is typically process-switched (creates the translation entry); "
            "subsequent packets in the same flow are fast-switched. In production, most packets show "
            "the asterisk. 'debug ip nat detailed' shows additional information including ACL matches "
            "and pool allocation. Use 'no debug all' or 'undebug all' to stop debug output."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-022
    {
        "id": "cd4v2-022",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "An engineer is reviewing Cisco IOS syslog behavior. Select TWO statements that are "
            "TRUE about the syslog message format and severity system."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A Cisco IOS syslog message with format '%OSPF-5-ADJCHG: ...' has severity 5 "
                    "(Notification/Notice), which is LESS severe than severity 4 (Warning)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In syslog, lower numbers are MORE severe (0=Emergency is worst). "
                    "Severity 5 (Notice/Notification) is less severe (lower priority) than "
                    "severity 4 (Warning). The format %FACILITY-SEVERITY-MNEMONIC encodes the "
                    "numeric severity directly. %OSPF-5-ADJCHG indicates an OSPF neighbor state "
                    "change at severity 5."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The command 'logging buffered 64000 debugging' stores syslog messages in a "
                    "64,000-byte RAM buffer at severity 7 threshold, capturing all messages "
                    "including debug; these messages survive a router reload"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'logging buffered' stores messages in RAM (volatile memory). "
                    "The buffer is cleared when the router reloads — messages do NOT persist "
                    "across reboots. To preserve logs across reloads, an external syslog server "
                    "is required ('logging host <ip>')."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The Cisco IOS syslog message format includes three elements before the colon: "
                    "facility name, severity level, and mnemonic (e.g., %LINK-3-UPDOWN: ...)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The Cisco IOS syslog message format is: "
                    "%FACILITY-SEVERITY-MNEMONIC: message text. "
                    "Facility identifies the subsystem (e.g., LINK, OSPF, SYS), severity is the "
                    "numeric level (0-7), and mnemonic is a short code identifying the specific event. "
                    "Understanding this format is essential for reading and filtering log output."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Setting 'logging console debugging' automatically enables syslog forwarding "
                    "to all configured syslog hosts at the debugging level as well"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Console logging ('logging console') and remote syslog logging "
                    "('logging trap' / 'logging host') are completely independent with separate "
                    "severity thresholds. Setting the console level to debugging does not affect "
                    "the trap level for remote syslog servers. Each destination must be configured "
                    "independently."
                ),
            },
        ],
        "explanation": (
            "Cisco IOS syslog message format: %FACILITY-SEVERITY-MNEMONIC: description. "
            "Severity 0-7 (lower = more severe): Emergency, Alert, Critical, Error, Warning, "
            "Notice, Informational, Debugging. Independent logging destinations: "
            "console (logging console <level>), internal buffer (logging buffered <size> <level>), "
            "remote syslog server (logging host <ip> + logging trap <level>), "
            "VTY sessions (logging monitor <level>, requires 'terminal monitor' per session). "
            "Only 'logging host' sends logs off-device; all others use volatile RAM or console only."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-023
    {
        "id": "cd4v2-023",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "NTP",
        "stem": (
            "An engineer is troubleshooting NTP synchronization on a Cisco router. "
            "Select TWO conditions that would cause 'show ntp status' to display "
            "'Clock is unsynchronized, stratum 16'."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The router cannot reach any configured NTP server (all servers are unreachable "
                    "or not responding to NTP queries)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When a router cannot successfully synchronize with any configured "
                    "NTP peer or server, it declares itself unsynchronized at stratum 16. "
                    "Stratum 16 is the NTP designation for 'unsynchronized' or 'invalid' — "
                    "any device receiving stratum 16 time should not use it as a reference."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The router is configured with 'ntp master 3' and has no upstream NTP server "
                    "configured; it uses its own internal clock as the time source"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ntp master 3' makes the router an authoritative NTP source at "
                    "stratum 3, using its own internal clock. In this case, 'show ntp status' "
                    "would show 'Clock is synchronized, stratum 3, reference is 127.127.7.1' "
                    "(the local clock pseudo-reference). It would NOT show stratum 16 unsynchronized — "
                    "that is the purpose of 'ntp master': to keep the router synchronized using "
                    "its own clock when no external source is available."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The router's NTP authentication is enabled ('ntp authenticate') but the "
                    "configured NTP server uses a different key, causing authentication to fail "
                    "and the association to be rejected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When NTP authentication is enabled and the key mismatch causes "
                    "authentication failure, the NTP association is rejected — the router "
                    "treats the server as untrusted and cannot synchronize. With no valid "
                    "synchronization source, the router becomes stratum 16 unsynchronized. "
                    "Key mismatches appear as failed authentication in 'debug ntp events'."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The router's stratum is 8, which exceeds the recommended maximum usable "
                    "stratum of 7; IOS automatically declares the clock unsynchronized"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no IOS rule that automatically marks stratum 8 or "
                    "higher as unsynchronized. Stratum values 1-15 are all valid operational "
                    "strata. Only stratum 16 is the designated 'unsynchronized' value. "
                    "Stratum 8 is uncommon but perfectly valid — NTP clients would use it "
                    "and become stratum 9."
                ),
            },
        ],
        "explanation": (
            "NTP stratum 16 = unsynchronized / clock not reliable. Causes: "
            "(1) No reachable NTP server — all configured peers/servers fail to respond or "
            "are themselves unsynchronized (stratum 16). "
            "(2) NTP authentication failure — key mismatch prevents association. "
            "(3) Clock offset too large — if the offset exceeds the 'panic threshold' (128 ms by default "
            "in reference NTP implementations; Cisco IOS also has limits), IOS may refuse to step the clock. "
            "'ntp master' prevents stratum 16 by providing a local reference. "
            "Verify NTP: 'show ntp status', 'show ntp associations detail', 'debug ntp events'."
        ),
    },
    # ------------------------------------------------------------------ cd4v2-024
    {
        "id": "cd4v2-024",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP & DNS roles",
        "stem": (
            "A DHCP client obtained a lease with a lease time of 8 hours. After 4 hours, the client "
            "attempts to renew its lease (T1 timer). The DHCP server does not respond to the renewal "
            "request. What happens at T2 (6 hours into the lease), and what is the client's behavior "
            "if the lease expires without a successful renewal?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "At T2 (75% of lease = 6 hours), the client broadcasts a DHCP Request to ANY "
                    "available DHCP server; if no server responds before lease expiration, "
                    "the client stops using the IP address and sends a new DHCP Discover"
                ),
                "correct": True,
                "rationale": (
                    "Correct. DHCP lease renewal behavior: T1 (50% of lease = 4 hours) — client "
                    "unicasts a DHCP Request to the original server. If no response, T2 (87.5% "
                    "per RFC 2131, or 75% in common implementations = 6 hours for an 8-hour lease) "
                    "— client BROADCASTS a DHCP Request to any DHCP server (rebinding state). "
                    "If the lease expires with no acknowledgment, the client MUST stop using the "
                    "IP address immediately and restart the full DORA process with a new Discover. "
                    "It cannot continue using an expired lease."
                ),
            },
            {
                "id": "b",
                "text": (
                    "At T2, the client continues using the IP address and retries renewal every "
                    "60 seconds until the lease expires; after expiration, the client retains the "
                    "IP address for an additional grace period of 1 hour"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no grace period after DHCP lease expiration per RFC 2131. "
                    "When a lease expires without renewal, the client MUST immediately cease using "
                    "the IP address. Continuing to use an expired address would constitute an "
                    "unauthorized address assignment and could cause network conflicts."
                ),
            },
            {
                "id": "c",
                "text": (
                    "At T2, the client switches to APIPA (169.254.x.x) addressing as a fallback "
                    "while continuing renewal attempts; APIPA allows local-subnet communication "
                    "during the DHCP outage"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. APIPA (Automatic Private IP Addressing, 169.254.0.0/16) is used "
                    "when a client cannot obtain a DHCP lease at all during initial discovery — "
                    "not as a fallback during lease renewal. During the renewal window (T1 to "
                    "lease expiration), the client continues using the current IP. APIPA is "
                    "not automatically applied mid-lease."
                ),
            },
            {
                "id": "d",
                "text": (
                    "At T2, the client sends a DHCP Release to free the address, then immediately "
                    "enters the rebinding state and requests the same IP from any available server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP Release is a voluntary message sent when a client explicitly "
                    "releases its address (e.g., when shutting down or changing networks). "
                    "During the T2 rebinding state, the client does NOT send a Release — it sends "
                    "a DHCP Request (broadcast) to renew the same IP with any server. "
                    "Sending a Release would free the address before obtaining a renewal, "
                    "risking address loss."
                ),
            },
        ],
        "explanation": (
            "DHCP lease timers (RFC 2131): "
            "T1 = 50% of lease time (renewal timer) — client unicasts DHCP Request to original server. "
            "T2 = 87.5% of lease time (rebinding timer) — client broadcasts DHCP Request to any server. "
            "Note: Cisco DHCP server defaults T2 to 75% (configurable). "
            "Lease expiration: client MUST stop using the IP and restart DORA from the beginning. "
            "During renewal, the client requests the SAME IP address (Option 50). "
            "A server may grant the same IP or offer a different one. "
            "View lease timers: 'ipconfig /all' (Windows) or 'show dhcp lease' on Cisco devices."
        ),
    },
]
