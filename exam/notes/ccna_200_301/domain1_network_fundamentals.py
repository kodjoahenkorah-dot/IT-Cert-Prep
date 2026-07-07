"""Domain 1 — Network Fundamentals study notes (Cisco CCNA 200-301).

Covers objectives 1.1-1.13 (~20 % of the exam).
Each entry in NOTES ties to one or more question study_topic labels so the
quiz engine can surface the right reading after a missed question.
"""

NOTES = [
    # ------------------------------------------------------------------ 1.1
    {
        "domain": 1,
        "topic": "Network components",
        "objective": "1.1",
        "video": "Network Components",
        "study_topics": ["Network components"],
        "body": (
            "<p>A modern network is built from a layered set of devices, each "
            "operating at a specific OSI layer and serving a distinct role.</p>"
            "<ul>"
            "<li><strong>Hub (Layer 1):</strong> A simple signal repeater that "
            "floods incoming electrical signals out every other port. All ports "
            "share one collision domain and one broadcast domain — obsolete "
            "today but still a CCNA exam concept.</li>"
            "<li><strong>Switch (Layer 2):</strong> Forwards Ethernet frames "
            "based on destination MAC addresses. Each port is its own collision "
            "domain. Switches build a MAC address table by learning source MACs "
            "from incoming frames.</li>"
            "<li><strong>Multilayer / Layer 3 Switch:</strong> Combines L2 "
            "switching with L3 inter-VLAN routing in hardware ASICs, giving "
            "wire-speed routing. Optimised for LAN; lacks the rich WAN interface "
            "support of a traditional router.</li>"
            "<li><strong>Router (Layer 3):</strong> Forwards packets between "
            "networks using IP addresses and a routing table. Separates both "
            "collision and broadcast domains. Supports diverse WAN interfaces "
            "(serial, DSL, cable, etc.) and advanced features.</li>"
            "<li><strong>Firewall:</strong> Enforces security policy by "
            "inspecting traffic (L3-L7). Next-generation firewalls (NGFW) add "
            "application visibility, IPS, URL filtering, and user identity.</li>"
            "<li><strong>Wireless LAN Controller (WLC):</strong> Centralises "
            "management of lightweight APs in the split-MAC architecture — "
            "handles RF management, roaming, channel/power assignment, and "
            "security policy. APs retain only real-time 802.11 MAC functions.</li>"
            "<li><strong>Access Point (AP):</strong> Provides the wireless "
            "radio interface. Autonomous APs operate independently; lightweight "
            "APs rely on a WLC for management.</li>"
            "<li><strong>PoE Switch / PoE Injector:</strong> Delivers power "
            "over Ethernet copper pairs. Standards: 802.3af (PoE) ~15.4 W, "
            "802.3at (PoE+) ~30 W, 802.3bt (PoE++) up to ~90 W per port.</li>"
            "<li><strong>Cisco DNA Center:</strong> Centralised intent-based "
            "networking controller for design, provisioning, policy, and "
            "assurance across campus fabrics.</li>"
            "</ul>"
            "<p>Knowing which device operates at which OSI layer and what "
            "traffic it can forward or filter is essential for the exam.</p>"
        ),
        "key_points": [
            "Hubs are Layer 1 repeaters — one collision domain for all ports.",
            "Switches are Layer 2 — each port is its own collision domain.",
            "Routers are Layer 3 — separate both collision and broadcast domains.",
            "Layer 3 switches do inter-VLAN routing in hardware ASICs but lack broad WAN support.",
            "WLC centralises lightweight AP management (RF, roaming, policy) via split-MAC.",
            "PoE standards: 802.3af ~15.4 W, 802.3at ~30 W, 802.3bt up to ~90 W.",
            "Cisco DNA Center is the intent-based networking management/controller platform.",
        ],
    },
    # ------------------------------------------------------------------ 1.2
    {
        "domain": 1,
        "topic": "Network topologies",
        "objective": "1.2",
        "video": "Network Topologies",
        "study_topics": ["Network topologies"],
        "body": (
            "<p>Network topology describes how devices are physically or "
            "logically connected and how traffic flows between them.</p>"
            "<p><strong>Common physical topologies:</strong></p>"
            "<ul>"
            "<li><strong>Star:</strong> All endpoints connect to a central "
            "switch or hub. Most common for modern Ethernet LANs. Single point "
            "of failure at the centre.</li>"
            "<li><strong>Bus:</strong> All devices share a single cable "
            "segment. Legacy coaxial Ethernet (10BASE2/5). Any break stops the "
            "entire network.</li>"
            "<li><strong>Ring:</strong> Devices connected in a closed loop. "
            "Used in SONET/SDH WANs and legacy Token Ring (IEEE 802.5).</li>"
            "<li><strong>Mesh / Full mesh:</strong> Every device connects "
            "directly to every other device. Maximises redundancy; scales "
            "poorly (n(n-1)/2 links).</li>"
            "<li><strong>Partial mesh:</strong> Selected devices have multiple "
            "connections; balances redundancy with cost.</li>"
            "<li><strong>Point-to-point:</strong> A dedicated link between "
            "exactly two devices — e.g., WAN serial links, PPP connections.</li>"
            "</ul>"
            "<p><strong>Enterprise architectural models:</strong></p>"
            "<ul>"
            "<li><strong>Three-tier campus (access / distribution / core):</strong> "
            "<em>Access</em> — connects end devices, provides PoE and port security. "
            "<em>Distribution</em> — aggregates access switches, inter-VLAN routing, "
            "ACLs, and route summarisation. "
            "<em>Core</em> — high-speed backbone, no policy/filtering, pure fast "
            "transit between distribution blocks.</li>"
            "<li><strong>Two-tier (collapsed core):</strong> Distribution and "
            "core merged into one layer; common in smaller campuses.</li>"
            "<li><strong>Spine-Leaf (data centre):</strong> Every leaf switch "
            "connects to every spine switch; no leaf-to-leaf links. Any "
            "server-to-server path crosses exactly one spine, giving predictable "
            "equal-cost latency. Uses L3 ECMP instead of STP-blocked links.</li>"
            "<li><strong>SOHO:</strong> Small office / home office — typically "
            "one integrated device combining router, switch, wireless AP, "
            "DHCP server, and NAT/firewall.</li>"
            "<li><strong>WAN topologies:</strong> Hub-and-spoke (branch sites "
            "connect to a central hub), full mesh, partial mesh, point-to-point "
            "leased lines.</li>"
            "</ul>"
        ),
        "key_points": [
            "Three-tier campus: access (endpoint ports) → distribution (policy/routing) → core (fast backbone).",
            "Spine-leaf: every leaf to every spine, equal-cost one-hop east-west latency.",
            "Spine-leaf uses ECMP, not STP — all links active.",
            "SOHO = single integrated device (router + switch + AP + NAT).",
            "Full mesh maximises redundancy; partial mesh balances redundancy vs cost.",
            "Distribution layer is where ACLs, inter-VLAN routing, and summarisation live.",
        ],
    },
    # ------------------------------------------------------------------ 1.3
    {
        "domain": 1,
        "topic": "Cabling & interfaces",
        "objective": "1.3",
        "video": "Cabling and Interfaces",
        "study_topics": ["Cabling & interfaces"],
        "body": (
            "<p>Choosing the right medium and connector is fundamental to "
            "building a functional network.</p>"
            "<p><strong>Copper twisted-pair (UTP):</strong></p>"
            "<ul>"
            "<li>Max segment length 100 m for all Ethernet speeds up to 10 Gbps "
            "(Cat 6a).</li>"
            "<li><strong>Straight-through:</strong> T568B on both ends — connects "
            "unlike devices (PC to switch, switch to router).</li>"
            "<li><strong>Crossover:</strong> T568A one end, T568B the other — "
            "connects like devices (PC-to-PC, switch-to-switch) when Auto-MDIX "
            "is absent. Modern devices with Auto-MDIX detect and correct "
            "automatically.</li>"
            "<li><strong>Rollover (console):</strong> Pins reversed end-to-end; "
            "used for out-of-band management via the console port.</li>"
            "</ul>"
            "<p><strong>Optical fibre:</strong></p>"
            "<ul>"
            "<li><strong>Multimode (MMF):</strong> Larger core (50 or 62.5 µm), "
            "LED or VCSEL light source. Cost-effective for short distances. "
            "10 Gbps reaches ~400 m on OM4. Connectors: LC, SC, ST.</li>"
            "<li><strong>Single-mode (SMF):</strong> Narrow core (~9 µm), laser "
            "light. Supports tens of kilometres — the choice for inter-building "
            "or WAN links. Higher transceiver cost than MMF.</li>"
            "</ul>"
            "<p><strong>Transceiver form factors (Cisco context):</strong></p>"
            "<ul>"
            "<li><strong>SFP (mini-GBIC):</strong> 1 Gbps — supports copper or "
            "fibre.</li>"
            "<li><strong>SFP+:</strong> 10 Gbps.</li>"
            "<li><strong>QSFP / QSFP+:</strong> 40 / 100 Gbps — four lanes "
            "combined.</li>"
            "</ul>"
            "<p><strong>Serial / WAN interfaces:</strong> Legacy point-to-point "
            "WAN links use EIA/TIA-232, V.35, or similar serial connectors with "
            "DCE/DTE roles. The DCE end provides the clock signal "
            "(<code>clock rate</code> on Cisco labs).</p>"
            "<p><strong>PoE reminder:</strong> 802.3af (~15.4 W), 802.3at / "
            "PoE+ (~30 W), 802.3bt / PoE++ (~60-90 W).</p>"
        ),
        "key_points": [
            "UTP copper max segment = 100 m regardless of speed (up to Cat 6a / 10G).",
            "Straight-through: unlike devices (PC↔switch, switch↔router).",
            "Crossover: like devices (PC↔PC, switch↔switch) — Auto-MDIX removes the need.",
            "Rollover / console cable: management access via console port.",
            "Multimode fibre: short reach, VCSEL/LED, larger core, lower cost.",
            "Single-mode fibre: long reach (tens of km), laser, narrow core, higher cost.",
            "SFP = 1G, SFP+ = 10G, QSFP+ = 40G — hot-swappable transceiver modules.",
            "Serial DCE side sets clock rate in Cisco lab environments.",
        ],
    },
    # ------------------------------------------------------------------ 1.4
    {
        "domain": 1,
        "topic": "Interface and cable troubleshooting",
        "objective": "1.4",
        "video": "Troubleshooting Interfaces and Cables",
        "study_topics": ["Interface/cable troubleshooting"],
        "body": (
            "<p>Reading interface status and counters is the first step when "
            "diagnosing connectivity problems.</p>"
            "<p><strong>Interface status matrix (<code>show interfaces</code>):</strong></p>"
            "<table>"
            "<tr><th>Layer 1</th><th>Layer 2</th><th>Meaning</th></tr>"
            "<tr><td>up</td><td>up</td><td>Normal, fully operational</td></tr>"
            "<tr><td>up</td><td>down</td><td>L1 good; L2 failing — keepalive or "
            "encapsulation mismatch</td></tr>"
            "<tr><td>down</td><td>down</td><td>L1 failure — unplugged cable, "
            "broken port, speed mismatch preventing link</td></tr>"
            "<tr><td>administratively down</td><td>down</td><td>Interface "
            "manually shut down (<code>shutdown</code> command)</td></tr>"
            "</table>"
            "<p><strong>Key counters and their causes:</strong></p>"
            "<ul>"
            "<li><strong>CRC / Input errors:</strong> Corrupt frames — usually "
            "a bad cable, damaged connector, or EMI.</li>"
            "<li><strong>Runts:</strong> Frames shorter than 64 bytes — often "
            "collisions or a bad NIC.</li>"
            "<li><strong>Giants:</strong> Frames longer than the MTU — jumbo "
            "frame mismatch or a misconfigured MTU.</li>"
            "<li><strong>Collisions:</strong> Normal on a half-duplex link; "
            "should be zero on a full-duplex link.</li>"
            "<li><strong>Late collisions:</strong> Collisions detected after "
            "the first 64 bytes (the slot time window). The classic symptom of "
            "a <em>duplex mismatch</em> — one side full-duplex, the other "
            "half-duplex. Also occurs when a cable is too long.</li>"
            "<li><strong>Input drops / overruns:</strong> Ingress rate exceeds "
            "interface or buffer capacity.</li>"
            "</ul>"
            "<p><strong>Duplex and speed mismatches:</strong></p>"
            "<ul>"
            "<li>Both sides should auto-negotiate, or both should be manually "
            "hardcoded to the same speed and duplex.</li>"
            "<li>Hardcoding one side but leaving the other on auto leads to a "
            "duplex mismatch (auto side defaults to half-duplex when it cannot "
            "negotiate), causing late collisions and degraded throughput.</li>"
            "</ul>"
            "<p><strong>Useful Cisco IOS commands:</strong></p>"
            "<ul>"
            "<li><code>show interfaces GigabitEthernet0/1</code> — full "
            "counters and status.</li>"
            "<li><code>show interfaces status</code> — summary table of all "
            "ports, speed, duplex, VLAN.</li>"
            "<li><code>show ip interface brief</code> — quick IP/status view.</li>"
            "</ul>"
        ),
        "key_points": [
            "Up/Up = normal. Up/Down = L2 problem (keepalive/encapsulation). Down/Down = L1 problem.",
            "Administratively down = manual 'shutdown' applied.",
            "Late collisions = duplex mismatch (half vs full-duplex) or cable too long.",
            "CRC errors = bad cable, damaged connector, EMI.",
            "Runts < 64 bytes; Giants > MTU — both indicate physical or config issues.",
            "Never hard-code only one side of a link; either set both or let both auto-negotiate.",
            "Use 'show interfaces' counters to pinpoint the layer and nature of the fault.",
        ],
    },
    # ------------------------------------------------------------------ 1.5
    {
        "domain": 1,
        "topic": "TCP vs UDP and well-known port numbers",
        "objective": "1.5",
        "video": "TCP and UDP",
        "study_topics": ["TCP vs UDP", "TCP/UDP well-known port numbers"],
        "body": (
            "<p>TCP and UDP are the two primary Layer 4 transport protocols, "
            "each suited to different application needs.</p>"
            "<p><strong>TCP (Transmission Control Protocol):</strong></p>"
            "<ul>"
            "<li>Connection-oriented: establishes a session with the "
            "<strong>three-way handshake</strong> — SYN → SYN-ACK → ACK.</li>"
            "<li>Reliable: acknowledges segments; retransmits lost ones.</li>"
            "<li>In-order delivery: sequences segments and reorders at the "
            "receiver.</li>"
            "<li>Flow control: <em>sliding window</em> — receiver advertises "
            "how much buffer space it has; sender limits outstanding "
            "unacknowledged data.</li>"
            "<li>Congestion control: reduces send rate when the network is "
            "congested.</li>"
            "<li>Connection teardown: FIN / FIN-ACK / ACK (or RST for abrupt "
            "close).</li>"
            "<li>Higher overhead — suitable for file transfers, web, email.</li>"
            "</ul>"
            "<p><strong>UDP (User Datagram Protocol):</strong></p>"
            "<ul>"
            "<li>Connectionless: no handshake, no session state.</li>"
            "<li>No reliability, no ordering, no retransmission.</li>"
            "<li>Low overhead and latency — suitable for real-time voice/video, "
            "DNS queries, DHCP, TFTP, SNMP.</li>"
            "<li>Applications provide their own error handling if needed "
            "(e.g., RTP for voice).</li>"
            "</ul>"
            "<p><strong>Well-known port numbers (0–1023):</strong></p>"
            "<table>"
            "<tr><th>Port</th><th>Protocol</th><th>Transport</th></tr>"
            "<tr><td>20</td><td>FTP data</td><td>TCP</td></tr>"
            "<tr><td>21</td><td>FTP control</td><td>TCP</td></tr>"
            "<tr><td>22</td><td>SSH</td><td>TCP</td></tr>"
            "<tr><td>23</td><td>Telnet</td><td>TCP</td></tr>"
            "<tr><td>25</td><td>SMTP</td><td>TCP</td></tr>"
            "<tr><td>53</td><td>DNS</td><td>TCP &amp; UDP</td></tr>"
            "<tr><td>67</td><td>DHCP server</td><td>UDP</td></tr>"
            "<tr><td>68</td><td>DHCP client</td><td>UDP</td></tr>"
            "<tr><td>69</td><td>TFTP</td><td>UDP</td></tr>"
            "<tr><td>80</td><td>HTTP</td><td>TCP</td></tr>"
            "<tr><td>110</td><td>POP3</td><td>TCP</td></tr>"
            "<tr><td>143</td><td>IMAP</td><td>TCP</td></tr>"
            "<tr><td>161</td><td>SNMP (agent)</td><td>UDP</td></tr>"
            "<tr><td>162</td><td>SNMP trap</td><td>UDP</td></tr>"
            "<tr><td>443</td><td>HTTPS</td><td>TCP</td></tr>"
            "<tr><td>514</td><td>Syslog</td><td>UDP</td></tr>"
            "<tr><td>1812/1813</td><td>RADIUS auth/accounting</td><td>UDP</td></tr>"
            "</table>"
            "<p>Both TCP and UDP share port numbers as a multiplexing mechanism "
            "to direct traffic to the correct application process.</p>"
        ),
        "key_points": [
            "TCP: connection-oriented, reliable, ordered, flow-controlled — higher overhead.",
            "UDP: connectionless, no reliability/ordering — lower latency, best for real-time.",
            "TCP three-way handshake: SYN → SYN-ACK → ACK.",
            "TCP teardown: FIN → FIN-ACK → ACK (or RST for abrupt close).",
            "TCP sliding window provides flow control between sender and receiver.",
            "FTP 20/21, SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, TFTP 69.",
            "HTTP 80, HTTPS 443, POP3 110, IMAP 143, SNMP 161/162, Syslog 514.",
            "DNS uses both UDP (queries) and TCP (zone transfers / large responses).",
        ],
    },
    # ------------------------------------------------------------------ 1.6
    {
        "domain": 1,
        "topic": "IPv4 subnetting",
        "objective": "1.6",
        "video": "Subnetting",
        "study_topics": ["IPv4 subnetting"],
        "body": (
            "<p>IPv4 subnetting divides a classful or CIDR address block into "
            "smaller, more manageable networks.</p>"
            "<p><strong>Key formula:</strong> Usable hosts = 2<sup>h</sup> − 2, "
            "where <em>h</em> is the number of host bits (32 − prefix length). "
            "Subtract 2 for the network address and the directed broadcast.</p>"
            "<p><strong>Common prefix reference table:</strong></p>"
            "<table>"
            "<tr><th>Prefix</th><th>Subnet mask</th><th>Block size</th>"
            "<th>Usable hosts</th></tr>"
            "<tr><td>/24</td><td>255.255.255.0</td><td>256</td><td>254</td></tr>"
            "<tr><td>/25</td><td>255.255.255.128</td><td>128</td><td>126</td></tr>"
            "<tr><td>/26</td><td>255.255.255.192</td><td>64</td><td>62</td></tr>"
            "<tr><td>/27</td><td>255.255.255.224</td><td>32</td><td>30</td></tr>"
            "<tr><td>/28</td><td>255.255.255.240</td><td>16</td><td>14</td></tr>"
            "<tr><td>/29</td><td>255.255.255.248</td><td>8</td><td>6</td></tr>"
            "<tr><td>/30</td><td>255.255.255.252</td><td>4</td><td>2</td></tr>"
            "</table>"
            "<p><strong>Block-size method (fast subnetting):</strong></p>"
            "<p>Block size = 256 − <em>interesting octet value of the mask</em>. "
            "Subnets begin at multiples of the block size.</p>"
            "<p><em>Worked example:</em> Host <code>192.168.10.200/26</code></p>"
            "<ol>"
            "<li>/26 mask = 255.255.255.<strong>192</strong>. "
            "Block size = 256 − 192 = <strong>64</strong>.</li>"
            "<li>Subnet boundaries in the last octet: 0, 64, 128, <strong>192</strong>, 256.</li>"
            "<li>200 falls between 192 and 256, so the subnet is "
            "<strong>192.168.10.192/26</strong>.</li>"
            "<li>Broadcast = next boundary − 1 = 256 − 1 = <strong>.255</strong>.</li>"
            "<li>Usable range: <strong>.193 – .254</strong> (62 hosts).</li>"
            "</ol>"
            "<p><strong>VLSM</strong> (Variable Length Subnet Masking) lets "
            "different subnets within the same major network use different "
            "prefix lengths — assign /30s to point-to-point WAN links (2 usable "
            "hosts) and larger blocks to LAN segments.</p>"
            "<p><strong>Route summarisation:</strong> Find the common bits "
            "shared by all networks to be summarised; the prefix length equals "
            "the number of shared bits.</p>"
        ),
        "key_points": [
            "Usable hosts = 2^(32 - prefix) - 2.",
            "Block size = 256 - mask value of the interesting octet.",
            "Subnet boundaries are multiples of the block size.",
            "Broadcast = next subnet boundary - 1.",
            "/30 = 2 usable hosts — standard for point-to-point WAN links.",
            "/26 = 62 hosts, /27 = 30, /28 = 14, /29 = 6.",
            "VLSM assigns different mask lengths to different segments — efficient address use.",
            "Summarise by finding the common high-order bits across all child networks.",
        ],
    },
    # ------------------------------------------------------------------ 1.7
    {
        "domain": 1,
        "topic": "Private addressing and NAT",
        "objective": "1.7",
        "video": "Private Addressing and NAT",
        "study_topics": ["Private addressing & NAT"],
        "body": (
            "<p>RFC 1918 reserves three private address ranges for use inside "
            "organisations. These addresses are not routed on the public "
            "internet, so NAT (Network Address Translation) is needed for "
            "internet access.</p>"
            "<p><strong>RFC 1918 private ranges:</strong></p>"
            "<table>"
            "<tr><th>Range</th><th>CIDR prefix</th><th>Former class</th></tr>"
            "<tr><td>10.0.0.0 – 10.255.255.255</td><td>10.0.0.0/8</td>"
            "<td>Class A</td></tr>"
            "<tr><td>172.16.0.0 – 172.31.255.255</td><td>172.16.0.0/12</td>"
            "<td>Class B</td></tr>"
            "<tr><td>192.168.0.0 – 192.168.255.255</td><td>192.168.0.0/16</td>"
            "<td>Class C</td></tr>"
            "</table>"
            "<p><strong>Other reserved / special-use ranges to know:</strong></p>"
            "<ul>"
            "<li><strong>127.0.0.0/8</strong> — loopback (127.0.0.1 most common).</li>"
            "<li><strong>169.254.0.0/16</strong> — APIPA / link-local; "
            "auto-assigned by Windows/macOS when DHCP fails.</li>"
            "<li><strong>0.0.0.0/0</strong> — default route (all networks).</li>"
            "<li><strong>255.255.255.255</strong> — limited broadcast "
            "(not forwarded by routers).</li>"
            "</ul>"
            "<p><strong>NAT types:</strong></p>"
            "<ul>"
            "<li><strong>Static NAT:</strong> One-to-one permanent mapping of "
            "a private address to a public address. Used for servers that must "
            "be reachable from outside.</li>"
            "<li><strong>Dynamic NAT:</strong> Maps a private address to an "
            "address from a pool of public addresses. Still one-to-one at any "
            "given moment.</li>"
            "<li><strong>PAT / NAT Overload (most common):</strong> Many-to-one "
            "— multiple private hosts share a single public IP, differentiated "
            "by TCP/UDP port numbers. This is how SOHO routers provide internet "
            "access to many devices simultaneously.</li>"
            "</ul>"
            "<p>NAT provides <em>address translation only</em> — it does not "
            "encrypt traffic. DHCP handles address assignment; encryption is "
            "IPsec or TLS.</p>"
        ),
        "key_points": [
            "RFC 1918 private ranges: 10/8, 172.16/12 (172.16–172.31), 192.168/16.",
            "Private addresses are not routable on the public internet — require NAT.",
            "APIPA 169.254.0.0/16 is assigned when DHCP fails — not RFC 1918.",
            "Static NAT = one-to-one permanent mapping (for servers).",
            "Dynamic NAT = one-to-one from a pool (no guarantee of same address).",
            "PAT / NAT Overload = many-to-one using port numbers — most common in SOHO.",
            "NAT does NOT encrypt traffic and is NOT a substitute for a firewall.",
        ],
    },
    # ------------------------------------------------------------------ 1.8
    {
        "domain": 1,
        "topic": "IPv6 addressing",
        "objective": "1.8",
        "video": "IPv6 Addressing",
        "study_topics": ["IPv6 addressing"],
        "body": (
            "<p>IPv6 uses 128-bit addresses written as eight groups of four "
            "hexadecimal digits separated by colons, e.g.: "
            "<code>2001:0db8:0000:0000:0000:ff00:0042:8329</code></p>"
            "<p><strong>Compression rules:</strong></p>"
            "<ol>"
            "<li>Drop leading zeros within each hextet: "
            "<code>0db8 → db8</code>, <code>0042 → 42</code>.</li>"
            "<li>Replace one (and only one) contiguous run of all-zero hextets "
            "with <code>::</code>: <code>0000:0000:0000 → ::</code>.</li>"
            "</ol>"
            "<p>Applying both rules: "
            "<code>2001:db8::ff00:42:8329</code></p>"
            "<p><strong>Interface identifier and EUI-64:</strong></p>"
            "<p>For a /64 prefix, the 64-bit interface ID can be auto-generated "
            "from the 48-bit MAC address using modified EUI-64:</p>"
            "<ol>"
            "<li>Split the MAC into two 24-bit halves.</li>"
            "<li>Insert <code>FF:FE</code> between them.</li>"
            "<li>Invert the 7th bit (U/L bit) of the first byte: e.g., "
            "<code>00</code> (0000 0000) → <code>02</code> (0000 0010).</li>"
            "</ol>"
            "<p><em>Example:</em> MAC <code>00:1A:2B:3C:4D:5E</code> → "
            "<code>021A:2BFF:FE3C:4D5E</code></p>"
            "<p><strong>Address assignment methods:</strong></p>"
            "<ul>"
            "<li><strong>Static manual</strong> — administrator configured.</li>"
            "<li><strong>SLAAC</strong> (Stateless Address Autoconfiguration) — "
            "host combines the /64 prefix from a Router Advertisement with a "
            "self-generated interface ID (EUI-64 or random).</li>"
            "<li><strong>DHCPv6</strong> (stateful) — server assigns full "
            "address and prefix, similar to DHCPv4.</li>"
            "<li><strong>Stateless DHCPv6</strong> — SLAAC for the address, "
            "DHCPv6 only for additional options like DNS servers.</li>"
            "</ul>"
            "<p>IPv6 eliminates broadcasts; ARP is replaced by "
            "<strong>NDP</strong> (Neighbor Discovery Protocol) using ICMPv6 "
            "messages (Router Solicitation, Router Advertisement, Neighbor "
            "Solicitation, Neighbor Advertisement).</p>"
        ),
        "key_points": [
            "IPv6 = 128 bits, eight 16-bit hextets in hex, separated by colons.",
            "Drop leading zeros in each hextet; replace one all-zero run with '::'.",
            "EUI-64: split MAC, insert FFFE, flip 7th bit of first byte.",
            "SLAAC: host builds address from RA prefix + self-generated interface ID.",
            "DHCPv6 stateful: server assigns full address; stateless: SLAAC address + DHCPv6 options.",
            "IPv6 has no broadcast; NDP (ICMPv6) replaces ARP.",
            "Every IPv6 interface auto-generates a link-local address (fe80::/10).",
        ],
    },
    # ------------------------------------------------------------------ 1.9
    {
        "domain": 1,
        "topic": "IPv6 address types and classification",
        "objective": "1.9",
        "video": "IPv6 Address Types",
        "study_topics": ["IPv6 address types", "IPv6 address type classification"],
        "body": (
            "<p>IPv6 defines several address types, each serving a distinct "
            "routing scope and purpose.</p>"
            "<p><strong>Unicast types:</strong></p>"
            "<table>"
            "<tr><th>Type</th><th>Prefix</th><th>Scope / Use</th></tr>"
            "<tr><td>Global Unicast (GUA)</td><td>2000::/3</td>"
            "<td>Globally routable (internet), analogous to public IPv4. "
            "Currently assigned from <code>2001::</code> range.</td></tr>"
            "<tr><td>Link-local</td><td>fe80::/10</td>"
            "<td>Auto-configured on every interface; on-link only, never "
            "forwarded by a router. Required for NDP and routing protocol "
            "neighbour relationships.</td></tr>"
            "<tr><td>Unique Local (ULA)</td><td>fc00::/7 (fdXX:…)</td>"
            "<td>Roughly equivalent to RFC 1918 private addresses; routable "
            "within an organisation but not on the public internet. The "
            "<code>fd00::/8</code> sub-range (L bit = 1) is the locally "
            "assigned portion used in practice.</td></tr>"
            "<tr><td>Loopback</td><td>::1/128</td>"
            "<td>Equivalent to 127.0.0.1; used to test the local IP stack.</td>"
            "</tr>"
            "<tr><td>Unspecified</td><td>::/128</td>"
            "<td>Source address when a host has no address yet (e.g., during "
            "DAD).</td></tr>"
            "</table>"
            "<p><strong>Multicast (ff00::/8):</strong> One-to-many delivery; "
            "IPv6 replaces all IPv4 broadcast with targeted multicast.</p>"
            "<ul>"
            "<li><code>ff02::1</code> — All nodes on the link.</li>"
            "<li><code>ff02::2</code> — All routers on the link.</li>"
            "<li><code>ff02::5 / ::6</code> — OSPFv3 routers.</li>"
            "<li><code>ff02::9</code> — RIPng routers.</li>"
            "<li><code>ff02::a</code> — EIGRP routers.</li>"
            "<li><strong>Solicited-node multicast:</strong> "
            "<code>ff02::1:ff00:0/104</code> + last 24 bits of unicast address; "
            "used by NDP for efficient address resolution.</li>"
            "</ul>"
            "<p><strong>Anycast:</strong> One address assigned to multiple "
            "interfaces; packets are delivered to the topologically nearest "
            "interface. Used for load distribution (e.g., DNS anycast).</p>"
            "<p><strong>No broadcast in IPv6</strong> — that function is "
            "handled by targeted multicast groups.</p>"
        ),
        "key_points": [
            "Global unicast (GUA): 2000::/3 — globally routable, like a public IPv4 address.",
            "Link-local: fe80::/10 — auto-configured, on-link only, never routed.",
            "Unique local (ULA): fc00::/7 (fd prefix in practice) — private, like RFC 1918.",
            "Loopback: ::1/128 — equivalent to 127.0.0.1.",
            "Multicast: ff00::/8 — ff02::1 all-nodes, ff02::2 all-routers.",
            "Anycast: same address on multiple devices; routed to nearest instance.",
            "IPv6 has NO broadcast — multicast replaces all broadcast functions.",
            "Every interface MUST have a link-local address to participate in IPv6.",
        ],
    },
    # ------------------------------------------------------------------ 1.10
    {
        "domain": 1,
        "topic": "Client IP verification",
        "objective": "1.10",
        "video": "Verifying IP on Client Devices",
        "study_topics": ["Client IP verification"],
        "body": (
            "<p>Verifying a client's IP configuration is the first step in "
            "troubleshooting connectivity from the endpoint.</p>"
            "<p><strong>Windows:</strong></p>"
            "<ul>"
            "<li><code>ipconfig</code> — shows IP address, subnet mask, and "
            "default gateway for each adapter.</li>"
            "<li><code>ipconfig /all</code> — adds MAC address, DNS servers, "
            "DHCP server, lease times, and IPv6 details.</li>"
            "<li><code>ipconfig /release</code> — releases the DHCP lease.</li>"
            "<li><code>ipconfig /renew</code> — requests a new DHCP lease.</li>"
            "<li><code>ipconfig /flushdns</code> — clears the DNS resolver "
            "cache.</li>"
            "</ul>"
            "<p><strong>Linux / macOS:</strong></p>"
            "<ul>"
            "<li><code>ip address show</code> (or <code>ip addr</code>) — "
            "modern Linux; shows IP and MAC per interface.</li>"
            "<li><code>ifconfig</code> — legacy command; still common on "
            "macOS.</li>"
            "<li><code>cat /etc/resolv.conf</code> — DNS server settings on "
            "Linux.</li>"
            "<li><code>networksetup -getinfo &lt;interface&gt;</code> — macOS "
            "IP details.</li>"
            "</ul>"
            "<p><strong>Cisco IOS:</strong></p>"
            "<ul>"
            "<li><code>show ip interface brief</code> — quick status and IP "
            "for all interfaces.</li>"
            "<li><code>show interfaces</code> — detailed counters and "
            "status.</li>"
            "<li><code>show ip route</code> — routing table.</li>"
            "</ul>"
            "<p><strong>APIPA indicator:</strong> A Windows client with address "
            "<code>169.254.x.x</code> and no default gateway has failed to "
            "obtain a DHCP lease. Investigate the NIC, cable, switch port, "
            "VLAN tagging, and DHCP server reachability.</p>"
            "<p><strong>Common verification tests:</strong> "
            "<code>ping 127.0.0.1</code> (loopback — IP stack), "
            "<code>ping &lt;default gateway&gt;</code> (local network), "
            "<code>ping 8.8.8.8</code> (internet by IP), "
            "<code>ping google.com</code> (DNS resolution).</p>"
        ),
        "key_points": [
            "Windows: 'ipconfig /all' shows IP, mask, gateway, MAC, DNS, DHCP server.",
            "Linux: 'ip addr' (modern) or 'ifconfig' (legacy) for interface details.",
            "Cisco IOS: 'show ip interface brief' for quick status; 'show interfaces' for counters.",
            "APIPA address 169.254.x.x = DHCP failure; no gateway means the host is isolated.",
            "Ping sequence: loopback → default gateway → remote IP → DNS name.",
            "'ipconfig /release' and '/renew' forces a new DHCP exchange on Windows.",
            "'ipconfig /flushdns' clears the local DNS cache — useful for name-resolution problems.",
        ],
    },
    # ------------------------------------------------------------------ 1.11
    {
        "domain": 1,
        "topic": "Wireless principles",
        "objective": "1.11",
        "video": "Wireless Principles",
        "study_topics": ["Wireless principles"],
        "body": (
            "<p>Wireless LANs (WLANs) are defined by the IEEE 802.11 standard "
            "family. Understanding RF behaviour, channels, and 802.11 "
            "amendments is essential for the CCNA exam.</p>"
            "<p><strong>802.11 amendments and speeds:</strong></p>"
            "<table>"
            "<tr><th>Amendment</th><th>Band</th><th>Max speed (approx)</th>"
            "<th>Common name</th></tr>"
            "<tr><td>802.11a</td><td>5 GHz</td><td>54 Mbps</td><td>—</td></tr>"
            "<tr><td>802.11b</td><td>2.4 GHz</td><td>11 Mbps</td><td>Wi-Fi 1</td></tr>"
            "<tr><td>802.11g</td><td>2.4 GHz</td><td>54 Mbps</td><td>Wi-Fi 3</td></tr>"
            "<tr><td>802.11n</td><td>2.4 &amp; 5 GHz</td><td>600 Mbps</td>"
            "<td>Wi-Fi 4</td></tr>"
            "<tr><td>802.11ac</td><td>5 GHz</td><td>~3.5 Gbps</td>"
            "<td>Wi-Fi 5</td></tr>"
            "<tr><td>802.11ax</td><td>2.4, 5, 6 GHz</td><td>~9.6 Gbps</td>"
            "<td>Wi-Fi 6/6E</td></tr>"
            "</table>"
            "<p><strong>Channels and interference:</strong></p>"
            "<ul>"
            "<li>2.4 GHz: 14 channels spaced 5 MHz apart, each ~22 MHz wide. "
            "Only <strong>channels 1, 6, and 11</strong> are non-overlapping in "
            "North America. Assign adjacent APs to different non-overlapping "
            "channels to prevent co-channel or adjacent-channel interference.</li>"
            "<li>5 GHz: Many more non-overlapping 20 MHz channels — much less "
            "congestion. Less range than 2.4 GHz.</li>"
            "</ul>"
            "<p><strong>CSMA/CA:</strong> Wi-Fi is a <em>half-duplex, "
            "shared medium</em>. Stations use Carrier Sense Multiple Access "
            "with Collision Avoidance: listen before transmitting, then add a "
            "random back-off if the medium is busy. All clients on the same AP "
            "and channel share airtime; more clients = less per-client "
            "throughput.</p>"
            "<p><strong>Key WLAN terminology:</strong></p>"
            "<ul>"
            "<li><strong>SSID:</strong> The network name broadcast in beacon "
            "frames; identifies the WLAN to clients.</li>"
            "<li><strong>BSS / BSSID:</strong> Basic Service Set; one AP and "
            "its associated clients. BSSID = AP's MAC address for the radio.</li>"
            "<li><strong>ESS:</strong> Extended Service Set — multiple APs "
            "sharing the same SSID; enables seamless roaming.</li>"
            "<li><strong>Cell:</strong> The coverage area of a single AP.</li>"
            "<li><strong>WPA2 / WPA3:</strong> Current encryption and "
            "authentication standards. WPA2 uses AES-CCMP; WPA3 adds SAE for "
            "stronger password-based auth.</li>"
            "</ul>"
        ),
        "key_points": [
            "2.4 GHz non-overlapping channels (North America): 1, 6, 11.",
            "5 GHz offers many more non-overlapping channels — less congestion.",
            "Wi-Fi is half-duplex and shared medium — CSMA/CA used to avoid collisions.",
            "SSID = network name; BSSID = AP radio MAC address.",
            "ESS = multiple APs with same SSID enabling seamless roaming.",
            "WPA2 uses AES-CCMP; WPA3 uses SAE for improved authentication.",
            "More clients on one AP = less per-client airtime and throughput.",
            "802.11n = Wi-Fi 4, 802.11ac = Wi-Fi 5, 802.11ax = Wi-Fi 6.",
        ],
    },
    # ------------------------------------------------------------------ 1.12
    {
        "domain": 1,
        "topic": "Virtualization and containers",
        "objective": "1.12",
        "video": "Virtualization and Containers",
        "study_topics": ["Virtualization & containers"],
        "body": (
            "<p>Virtualisation abstracts physical hardware or operating systems "
            "to run multiple isolated workloads on shared infrastructure.</p>"
            "<p><strong>Virtual Machines (VMs):</strong></p>"
            "<ul>"
            "<li>A <em>hypervisor</em> presents virtualised hardware to each "
            "guest OS.</li>"
            "<li><strong>Type 1 (bare-metal) hypervisor:</strong> Runs directly "
            "on hardware — e.g., VMware ESXi, Microsoft Hyper-V, KVM. Better "
            "performance.</li>"
            "<li><strong>Type 2 (hosted) hypervisor:</strong> Runs as an "
            "application on a host OS — e.g., VMware Workstation, VirtualBox. "
            "Easier for desktops/labs.</li>"
            "<li>Each VM includes a full guest OS, making them larger and slower "
            "to boot than containers.</li>"
            "</ul>"
            "<p><strong>Containers:</strong></p>"
            "<ul>"
            "<li>Virtualise at the OS level — containers share the host kernel "
            "and package only the application and its dependencies.</li>"
            "<li>Much lighter than VMs: smaller image size, sub-second start "
            "times.</li>"
            "<li>Less isolation than VMs (shared kernel is a larger attack "
            "surface).</li>"
            "<li>Docker is the most common container runtime; Kubernetes "
            "orchestrates containers at scale.</li>"
            "</ul>"
            "<table>"
            "<tr><th></th><th>VM</th><th>Container</th></tr>"
            "<tr><td>Isolation</td><td>Full OS isolation</td>"
            "<td>Process isolation (shared kernel)</td></tr>"
            "<tr><td>Size</td><td>GBs</td><td>MBs</td></tr>"
            "<tr><td>Boot time</td><td>Seconds–minutes</td><td>Milliseconds</td></tr>"
            "<tr><td>Overhead</td><td>Higher</td><td>Lower</td></tr>"
            "</table>"
            "<p><strong>Network virtualisation concepts:</strong></p>"
            "<ul>"
            "<li><strong>VRF (Virtual Routing and Forwarding):</strong> Creates "
            "multiple independent routing tables on one physical router, "
            "isolating customer or department routes even with overlapping "
            "address space. Analogous to VLANs but at Layer 3.</li>"
            "<li><strong>VLAN:</strong> Layer 2 segmentation — one switch "
            "carries multiple broadcast domains via 802.1Q tagging.</li>"
            "<li><strong>SDN (Software-Defined Networking):</strong> Separates "
            "the control plane (routing decisions) from the data plane "
            "(forwarding). A centralised controller manages the network via "
            "open APIs (e.g., OpenFlow, Cisco DNA Center using RESTCONF/NETCONF)."
            "</li>"
            "</ul>"
        ),
        "key_points": [
            "Type 1 hypervisor: runs on bare metal (ESXi, Hyper-V, KVM) — best performance.",
            "Type 2 hypervisor: runs on a host OS (Workstation, VirtualBox) — best for labs.",
            "VMs = full guest OS per instance; containers = shared kernel + app dependencies.",
            "Containers are lighter, start faster, but offer less isolation than VMs.",
            "VRF = multiple independent L3 routing tables on one router (L3 equivalent of VLANs).",
            "SDN separates control plane from data plane; controller manages forwarding via APIs.",
            "Docker runs containers; Kubernetes orchestrates them at scale.",
        ],
    },
    # ------------------------------------------------------------------ 1.13
    {
        "domain": 1,
        "topic": "Switching concepts and MAC address table",
        "objective": "1.13",
        "video": "Switching Concepts",
        "study_topics": ["Switching concepts / MAC table"],
        "body": (
            "<p>Understanding how a Layer 2 switch learns and forwards frames "
            "is foundational for troubleshooting and VLAN design.</p>"
            "<p><strong>MAC address table operations:</strong></p>"
            "<ol>"
            "<li><strong>Learn:</strong> When a frame arrives, the switch reads "
            "the <em>source</em> MAC address and records the MAC → ingress port "
            "mapping in the Content-Addressable Memory (CAM) table, along with "
            "a VLAN tag and timestamp.</li>"
            "<li><strong>Forward (known unicast):</strong> If the "
            "<em>destination</em> MAC is in the table, the frame is sent only "
            "to the recorded port.</li>"
            "<li><strong>Flood (unknown unicast / broadcast / unknown multicast):"
            "</strong> If the destination MAC is not in the table, the switch "
            "floods the frame out all ports in the same VLAN except the ingress "
            "port.</li>"
            "<li><strong>Age out:</strong> Entries that are not refreshed within "
            "the aging timer (default <strong>300 seconds</strong> on Cisco) "
            "are removed, keeping the table current as devices move.</li>"
            "</ol>"
            "<p><strong>Useful IOS commands:</strong></p>"
            "<ul>"
            "<li><code>show mac address-table</code> — view all learned "
            "entries.</li>"
            "<li><code>show mac address-table dynamic</code> — only dynamic "
            "entries.</li>"
            "<li><code>show mac address-table aging-time</code> — current "
            "aging timer value.</li>"
            "<li><code>clear mac address-table dynamic</code> — flush all "
            "dynamic entries.</li>"
            "</ul>"
            "<p><strong>Frame types and handling:</strong></p>"
            "<table>"
            "<tr><th>Frame type</th><th>Destination MAC</th>"
            "<th>Switch action</th></tr>"
            "<tr><td>Known unicast</td><td>In MAC table</td>"
            "<td>Forward to specific port</td></tr>"
            "<tr><td>Unknown unicast</td><td>NOT in MAC table</td>"
            "<td>Flood within VLAN</td></tr>"
            "<tr><td>Broadcast</td><td>FF:FF:FF:FF:FF:FF</td>"
            "<td>Flood within VLAN</td></tr>"
            "<tr><td>Multicast</td><td>01:xx:xx:xx:xx:xx</td>"
            "<td>Flood (or controlled with IGMP snooping)</td></tr>"
            "</table>"
            "<p><strong>VLANs:</strong> A VLAN is a logical broadcast domain "
            "on one or more switches. Frames within a VLAN stay within that "
            "VLAN; routing is required to move traffic between VLANs. 802.1Q "
            "trunks carry traffic for multiple VLANs over a single link using "
            "a 4-byte tag inserted into the Ethernet frame header.</p>"
        ),
        "key_points": [
            "Switches LEARN from the SOURCE MAC of incoming frames.",
            "Switches FORWARD based on the DESTINATION MAC.",
            "Unknown unicast, broadcast, and unregistered multicast = flood within VLAN.",
            "Default MAC aging time on Cisco switches = 300 seconds (5 minutes).",
            "Static entries never age out; only dynamic (learned) entries expire.",
            "Each VLAN is its own broadcast domain; inter-VLAN traffic requires routing.",
            "802.1Q trunk: a 4-byte VLAN tag added to frames allows multi-VLAN transport on one link.",
            "'show mac address-table' displays current MAC-to-port mappings.",
        ],
    },
    # ------------------------------------------------------------------ OSI
    {
        "domain": 1,
        "topic": "OSI model layers, PDUs, and representative protocols",
        "objective": "1.1",
        "video": "OSI Model",
        "study_topics": ["OSI model layers, PDUs, and representative protocols"],
        "body": (
            "<p>The OSI (Open Systems Interconnection) model is a seven-layer "
            "reference framework for understanding and troubleshooting network "
            "communication. Data passes down the layers on the sender and back "
            "up on the receiver; each layer adds (or removes) its own header "
            "to produce a protocol data unit (PDU).</p>"
            "<table>"
            "<tr><th>#</th><th>Layer</th><th>PDU</th>"
            "<th>Representative protocols / devices</th></tr>"
            "<tr><td>7</td><td>Application</td><td>Data</td>"
            "<td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP, SNMP, SSH, Telnet</td></tr>"
            "<tr><td>6</td><td>Presentation</td><td>Data</td>"
            "<td>TLS/SSL encryption, JPEG/MPEG encoding, ASCII/Unicode</td></tr>"
            "<tr><td>5</td><td>Session</td><td>Data</td>"
            "<td>NetBIOS, RPC, SIP session management</td></tr>"
            "<tr><td>4</td><td>Transport</td><td>Segment (TCP) / Datagram (UDP)"
            "</td><td>TCP, UDP — port numbers, reliability, flow control</td>"
            "</tr>"
            "<tr><td>3</td><td>Network</td><td>Packet</td>"
            "<td>IPv4, IPv6, ICMP, OSPF, EIGRP — routers operate here</td></tr>"
            "<tr><td>2</td><td>Data Link</td><td>Frame</td>"
            "<td>Ethernet (802.3), Wi-Fi (802.11), PPP, 802.1Q VLAN tags — "
            "switches and bridges</td></tr>"
            "<tr><td>1</td><td>Physical</td><td>Bits</td>"
            "<td>Copper, fibre, radio, hubs, repeaters, cables, connectors</td>"
            "</tr>"
            "</table>"
            "<p><strong>Encapsulation summary:</strong> Application data → "
            "TCP/UDP segment (L4) → IP packet (L3) → Ethernet frame (L2) → "
            "electrical/light/radio bits (L1). At each layer the relevant "
            "header (and at L2 also a trailer/FCS) is added.</p>"
            "<p><strong>Mnemonic (top to bottom):</strong> "
            "<em>All People Seem To Need Data Processing</em> "
            "(Application, Presentation, Session, Transport, Network, "
            "Data Link, Physical).</p>"
            "<p><strong>Troubleshooting with OSI:</strong> Start at Layer 1 "
            "(is the cable plugged in?) and work up. The interface status "
            "output maps directly: L1 = physical state, L2 = line protocol.</p>"
            "<p><strong>TCP/IP model comparison:</strong> The 4-layer TCP/IP "
            "model maps as: Application (OSI 5-7), Transport (OSI 4), "
            "Internet (OSI 3), Network Access (OSI 1-2).</p>"
        ),
        "key_points": [
            "OSI Layer 1 Physical: bits, cables, hubs — PDU = Bits.",
            "OSI Layer 2 Data Link: frames, MAC addresses, switches — PDU = Frame.",
            "OSI Layer 3 Network: packets, IP addresses, routers — PDU = Packet.",
            "OSI Layer 4 Transport: segments/datagrams, TCP/UDP, ports — PDU = Segment.",
            "Layers 5/6/7 (Session, Presentation, Application) = Data.",
            "Encapsulation: data → segment → packet → frame → bits (sender); reverse at receiver.",
            "Mnemonic top-down: All People Seem To Need Data Processing.",
            "TCP/IP model: Application, Transport, Internet, Network Access (4 layers).",
        ],
    },
]
