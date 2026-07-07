"""
Cisco CCNA 200-301 — Domain 3: IP Connectivity
Study notes following the exam blueprint objectives.
Original content — not reproduced from any copyrighted source.
"""

NOTES = [
    # ------------------------------------------------------------------
    # 3.1  Routing table components
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "Routing table components",
        "objective": "3.1",
        "video": "Routing Table",
        "study_topics": ["Routing table components"],
        "body": (
            "<p>The IP routing table is the data structure a router consults to decide "
            "where to forward every packet. Understanding each field lets you read "
            "<code>show ip route</code> output confidently on exam day.</p>"
            "<p><strong>Route source codes (left column):</strong></p>"
            "<ul>"
            "<li><strong>C</strong> — directly connected network (an active, up/up interface).</li>"
            "<li><strong>L</strong> — local host route (/32 for IPv4, /128 for IPv6) for the "
            "router's own interface address, auto-installed.</li>"
            "<li><strong>S</strong> — static route configured with <code>ip route</code>.</li>"
            "<li><strong>O</strong> — OSPF-learned route; <strong>O IA</strong> = inter-area, "
            "<strong>O E1/E2</strong> = external.</li>"
            "<li><strong>D</strong> — EIGRP internal; <strong>D EX</strong> = EIGRP external.</li>"
            "<li><strong>R</strong> — RIP; <strong>B</strong> — BGP.</li>"
            "</ul>"
            "<p><strong>Key fields in each routing-table entry:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Field</th><th>Meaning</th></tr>"
            "<tr><td>Network / prefix length</td><td>Destination, e.g. 10.1.0.0/16</td></tr>"
            "<tr><td>[AD/metric]</td><td>Administrative distance / routing metric, e.g. [110/20]</td></tr>"
            "<tr><td>via &lt;next-hop&gt;</td><td>IP address of the next router</td></tr>"
            "<tr><td>Age timer</td><td>How long since the route was last updated</td></tr>"
            "<tr><td>Outbound interface</td><td>Egress interface used to reach next-hop</td></tr>"
            "</table>"
            "<p>A route is installed in the routing table only if the next-hop is reachable and "
            "no route with a lower administrative distance exists for the same prefix. "
            "Equal-cost routes produce multiple entries for the same prefix (ECMP load-sharing).</p>"
        ),
        "key_points": [
            "C = connected, L = local (/32 or /128), S = static, O = OSPF, D = EIGRP, R = RIP, B = BGP.",
            "show ip route displays [AD/metric] in square brackets for every dynamic route.",
            "A directly connected (C) route has AD 0; a local (L) route has AD 0 as well.",
            "ECMP: multiple routes with identical prefix length and metric share traffic.",
            "A route is only placed in the table when the next-hop address is reachable.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.1  Forwarding decision & longest prefix match
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "Forwarding decision & longest prefix match",
        "objective": "3.1",
        "video": "Longest Prefix Match",
        "study_topics": ["Forwarding decision & longest prefix match"],
        "body": (
            "<p>When a packet arrives, the router compares the destination IP against every "
            "prefix in the routing table and selects the <strong>most specific match</strong> — "
            "the entry with the longest (highest-number) prefix length. This rule is called "
            "<em>longest prefix match (LPM)</em> and it takes absolute priority over "
            "administrative distance and metric.</p>"
            "<p><strong>Example routing table:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Prefix</th><th>Next-hop</th></tr>"
            "<tr><td>0.0.0.0/0</td><td>203.0.113.1 (default)</td></tr>"
            "<tr><td>10.0.0.0/8</td><td>10.255.0.1</td></tr>"
            "<tr><td>10.1.0.0/16</td><td>10.1.255.1</td></tr>"
            "<tr><td>10.1.2.0/24</td><td>10.1.2.254</td></tr>"
            "</table>"
            "<p>A packet to <strong>10.1.2.50</strong> matches all four prefixes. LPM selects "
            "<strong>/24</strong> — the longest match — and forwards to 10.1.2.254. "
            "A packet to 10.1.5.1 matches /8 and /16; the /16 wins.</p>"
            "<p><strong>Forwarding decision sequence:</strong></p>"
            "<ol>"
            "<li>Find all matching prefixes in the routing table.</li>"
            "<li>Select the entry with the longest prefix length.</li>"
            "<li>If a tie still exists (same prefix from multiple protocols), use the lower "
            "administrative distance.</li>"
            "<li>If AD is also tied, use the lower metric.</li>"
            "<li>If metric is equal, load-balance across all matching next-hops (ECMP).</li>"
            "</ol>"
            "<p>A default route (0.0.0.0/0) is the shortest possible match and is used only "
            "when no more-specific prefix exists — often called the 'gateway of last resort'.</p>"
        ),
        "key_points": [
            "Longest prefix match (LPM) always wins — it overrides AD and metric.",
            "A /28 beats a /24, which beats a /16, which beats the default /0.",
            "After LPM selects the prefix, AD breaks ties between protocols; metric breaks ties within a protocol.",
            "The default route 0.0.0.0/0 is a catch-all and only used when nothing more specific matches.",
            "ECMP can forward over multiple interfaces when metric and prefix length are equal.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.2  Administrative distance
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "Administrative distance",
        "objective": "3.2",
        "video": "Administrative Distance",
        "study_topics": ["Administrative distance"],
        "body": (
            "<p><strong>Administrative distance (AD)</strong> is a trustworthiness rating "
            "assigned to routing information sources. When two protocols advertise a route "
            "to the <em>same prefix</em>, the router installs only the route with the "
            "<strong>lower AD</strong>. AD values range from 0 (most trusted) to 255 "
            "(never used / unreachable).</p>"
            "<p><strong>Default Cisco AD values (must memorize):</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Source</th><th>AD</th></tr>"
            "<tr><td>Connected interface</td><td>0</td></tr>"
            "<tr><td>Static route</td><td>1</td></tr>"
            "<tr><td>eBGP (external BGP)</td><td>20</td></tr>"
            "<tr><td>EIGRP internal</td><td>90</td></tr>"
            "<tr><td>OSPF</td><td>110</td></tr>"
            "<tr><td>IS-IS</td><td>115</td></tr>"
            "<tr><td>RIP</td><td>120</td></tr>"
            "<tr><td>EIGRP external</td><td>170</td></tr>"
            "<tr><td>iBGP (internal BGP)</td><td>200</td></tr>"
            "<tr><td>Unreachable / unusable</td><td>255</td></tr>"
            "</table>"
            "<p>AD is <em>local</em> to each router — it is never exchanged in routing "
            "updates. A floating static route is simply a static route configured with a "
            "manually raised AD so that a dynamic route takes precedence when available "
            "(see the Floating Static Routes note).</p>"
            "<p>AD only matters when two sources advertise the same prefix length. Once a "
            "specific prefix is selected, <strong>longest prefix match</strong> still "
            "governs which entry is used for an actual packet.</p>"
        ),
        "key_points": [
            "Lower AD = more trusted. Connected=0, Static=1, eBGP=20, EIGRP=90, OSPF=110, RIP=120.",
            "IS-IS=115, EIGRP external=170, iBGP=200. AD 255 means the route is never used.",
            "AD is a local router value; it is NOT advertised to neighbors.",
            "AD only breaks ties between sources advertising the same prefix; LPM takes priority overall.",
            "You can change the AD of a static route manually to create a floating static route.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.3  Static routing
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "Static routing",
        "objective": "3.3",
        "video": "Configuring Static Routes",
        "study_topics": ["Static routing"],
        "body": (
            "<p>A static route is a manually configured routing entry. It has AD 1 (very "
            "trusted) and does not adapt automatically to topology changes, making it "
            "suitable for small networks, stub networks, or as a default route toward an ISP.</p>"
            "<p><strong>Basic syntax:</strong></p>"
            "<pre>ip route &lt;network&gt; &lt;mask&gt; {&lt;next-hop-ip&gt; | &lt;exit-interface&gt; | both}</pre>"
            "<p><strong>Common forms:</strong></p>"
            "<ul>"
            "<li><strong>Next-hop IP only:</strong> <code>ip route 192.168.10.0 255.255.255.0 10.0.0.1</code> — "
            "router must recursively resolve 10.0.0.1 in the routing table before forwarding. "
            "This is the preferred method on point-to-multipoint links.</li>"
            "<li><strong>Exit interface only:</strong> <code>ip route 192.168.10.0 255.255.255.0 Gi0/1</code> — "
            "creates a directly connected (proxy-ARP dependent) entry. Preferred only on "
            "point-to-point links (serial).</li>"
            "<li><strong>Both (fully specified):</strong> <code>ip route 192.168.10.0 255.255.255.0 Gi0/1 10.0.0.1</code> — "
            "no recursive lookup needed; best practice on Ethernet links.</li>"
            "</ul>"
            "<p><strong>Default static route:</strong> <code>ip route 0.0.0.0 0.0.0.0 &lt;next-hop&gt;</code> "
            "— forwards all unmatched packets; often redistributed into a routing protocol with "
            "<code>default-information originate</code>.</p>"
            "<p>Verify with <code>show ip route static</code> and test reachability with "
            "<code>ping</code> and <code>traceroute</code>.</p>"
        ),
        "key_points": [
            "Static route AD = 1; lower than any dynamic protocol.",
            "Next-hop IP is safest on multi-access (Ethernet) links; exit-interface alone only suits point-to-point.",
            "Fully specified static route (interface + next-hop) avoids recursive lookup and proxy-ARP issues.",
            "Default static route: ip route 0.0.0.0 0.0.0.0 <next-hop>.",
            "Use 'default-information originate' to advertise the default route into OSPF.",
            "Verify with: show ip route static | show ip route | ping | traceroute.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.3  Floating static routes
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "Floating static routes",
        "objective": "3.3",
        "video": "Configuring Static Routes",
        "study_topics": ["Floating static routes"],
        "body": (
            "<p>A <strong>floating static route</strong> is a backup static route with its "
            "AD deliberately raised above a dynamic routing protocol so it only appears in "
            "the routing table when the primary (dynamic) route disappears.</p>"
            "<p><strong>How it works:</strong></p>"
            "<ol>"
            "<li>Configure the primary path using a dynamic protocol, e.g. OSPF (AD 110).</li>"
            "<li>Configure a static backup route with an AD higher than 110, e.g. 130:<br>"
            "<code>ip route 192.168.20.0 255.255.255.0 10.0.0.5 130</code></li>"
            "<li>While OSPF is active, the static route 'floats' in the background — it "
            "is in the router's config but <em>not</em> in the routing table.</li>"
            "<li>If the OSPF route is withdrawn (link failure, neighbor goes down), the "
            "floating static route immediately moves into the routing table.</li>"
            "</ol>"
            "<p><strong>AD syntax:</strong> The AD is appended as the last positional "
            "argument in the <code>ip route</code> command.</p>"
            "<pre>ip route 0.0.0.0 0.0.0.0 203.0.113.2 200</pre>"
            "<p>The example above floats below iBGP (AD 200) and all IGPs — it will only "
            "activate if every dynamic route to that prefix disappears. "
            "A floating static route is a simple and effective high-availability technique "
            "that requires no additional routing protocol.</p>"
        ),
        "key_points": [
            "A floating static route has its AD manually raised above the primary dynamic protocol's AD.",
            "It only enters the routing table when the preferred dynamic route is gone.",
            "Syntax: ip route <net> <mask> <next-hop> <AD> — the AD is the last argument.",
            "Common use case: dial backup or secondary ISP link that activates on primary failure.",
            "Does not require a routing protocol; configuration is purely local.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.4  IPv6 static routing
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "IPv6 static routing",
        "objective": "3.4",
        "video": "IPv6 Static Routes",
        "study_topics": ["IPv6 static routing"],
        "body": (
            "<p>IPv6 static routes follow the same logic as IPv4 but use 128-bit addresses "
            "and the <code>ipv6 route</code> command. IPv6 routing must be enabled globally "
            "with <code>ipv6 unicast-routing</code>.</p>"
            "<p><strong>Syntax:</strong></p>"
            "<pre>ipv6 route &lt;prefix/length&gt; {&lt;next-hop-ipv6&gt; | &lt;interface&gt; | both} [AD]</pre>"
            "<p><strong>Examples:</strong></p>"
            "<ul>"
            "<li>Next-hop global unicast: <code>ipv6 route 2001:db8:1::/64 2001:db8:0::1</code></li>"
            "<li>Exit interface (point-to-point only): <code>ipv6 route 2001:db8:1::/64 Serial0/0/0</code></li>"
            "<li>Link-local next-hop (must include exit interface): "
            "<code>ipv6 route 2001:db8:1::/64 Gi0/0 fe80::1</code></li>"
            "<li>Default route: <code>ipv6 route ::/0 &lt;next-hop&gt;</code></li>"
            "</ul>"
            "<p><strong>Link-local next-hops</strong> are very common in IPv6 because "
            "routers often advertise their link-local address (FE80::/10) as the next-hop "
            "in routing updates. When using a link-local address, you <em>must</em> also "
            "specify the outgoing interface, because link-local addresses are not unique "
            "across the whole router — they are only meaningful on a single link.</p>"
            "<p>Verify with <code>show ipv6 route</code> and <code>show ipv6 route static</code>. "
            "Use <code>ping ipv6</code> and <code>traceroute ipv6</code> to test.</p>"
        ),
        "key_points": [
            "Requires: ipv6 unicast-routing on the router globally.",
            "Command: ipv6 route <prefix/length> <next-hop or interface>.",
            "Default IPv6 route: ipv6 route ::/0 <next-hop>.",
            "Link-local (FE80::) next-hop requires the exit interface to be specified.",
            "Verify with: show ipv6 route static | ping ipv6 | traceroute ipv6.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.5  OSPF adjacencies + neighbor state machine  (combined note)
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "OSPF adjacencies and neighbor state machine",
        "objective": "3.5",
        "video": "OSPF Neighbors",
        "study_topics": ["OSPF adjacencies", "OSPF neighbor state machine"],
        "body": (
            "<p>OSPF builds adjacencies between neighboring routers before exchanging "
            "link-state information. The relationship progresses through a defined "
            "<strong>seven-state machine</strong>:</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>State</th><th>What is happening</th></tr>"
            "<tr><td><strong>Down</strong></td><td>No Hellos received from this neighbor; "
            "initial state or the neighbor has been declared dead.</td></tr>"
            "<tr><td><strong>Init</strong></td><td>A Hello has been received from the "
            "neighbor, but this router's own Router-ID is NOT yet listed in that Hello "
            "(one-way communication).</td></tr>"
            "<tr><td><strong>2-Way</strong></td><td>Bidirectional communication confirmed — "
            "each router sees its own RID in the other's Hello. DR/BDR election occurs on "
            "multi-access segments at this point. Non-DR/BDR pairs stop here (DROTHER "
            "relationship).</td></tr>"
            "<tr><td><strong>ExStart</strong></td><td>Master/slave relationship negotiated "
            "using DBD packets; the router with the higher RID becomes master and sets the "
            "initial DBD sequence number.</td></tr>"
            "<tr><td><strong>Exchange</strong></td><td>Routers exchange Database Description "
            "(DBD) packets summarizing their LSDB contents.</td></tr>"
            "<tr><td><strong>Loading</strong></td><td>Routers send Link-State Requests (LSR) "
            "for any LSAs they are missing; neighbor responds with Link-State Updates (LSU) "
            "containing the actual LSAs.</td></tr>"
            "<tr><td><strong>Full</strong></td><td>LSDB is fully synchronized. This is the "
            "only healthy steady-state for a proper OSPF adjacency.</td></tr>"
            "</table>"
            "<p><strong>Adjacency requirements (must match):</strong> same area ID, same "
            "Hello/Dead timers, same area type (stub/NSSA), same subnet, authentication, "
            "and MTU (on some platforms).</p>"
            "<p>On multi-access segments a router forms a Full adjacency only with the DR "
            "and BDR; all other DROTHER–DROTHER pairs stay at 2-Way.</p>"
        ),
        "key_points": [
            "Seven OSPF neighbor states: Down → Init → 2-Way → ExStart → Exchange → Loading → Full.",
            "2-Way: bidirectional confirmed; DR/BDR election happens here on broadcast segments.",
            "ExStart: master/slave negotiated; higher RID wins master role.",
            "Exchange: DBD packets listing LSA headers exchanged.",
            "Loading: missing LSAs fetched via LSR/LSU.",
            "Full: LSDB synchronized — only healthy steady-state for an adjacency.",
            "DROTHER pairs on broadcast networks only reach 2-Way, not Full.",
            "Adjacency requirements: area ID, Hello/Dead timers, area type, subnet, MTU, auth must match.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.5  OSPF DR/BDR election
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "OSPF DR/BDR election",
        "objective": "3.5",
        "video": "OSPF DR and BDR",
        "study_topics": ["OSPF DR/BDR election"],
        "body": (
            "<p>On multi-access segments (e.g., Ethernet broadcast), OSPF reduces the "
            "number of adjacencies by electing a <strong>Designated Router (DR)</strong> "
            "and <strong>Backup Designated Router (BDR)</strong>. All other routers "
            "(DROTHERs) form Full adjacencies only with the DR and BDR, not with each "
            "other. This reduces adjacency count from O(n²) to O(n).</p>"
            "<p><strong>Election rules (two-step, in order):</strong></p>"
            "<ol>"
            "<li><strong>Highest OSPF priority</strong> wins DR; second-highest wins BDR. "
            "Default priority is <strong>1</strong>; range 0–255. "
            "A router with priority <strong>0</strong> is ineligible to become DR or BDR.</li>"
            "<li>If priorities are equal, the router with the <strong>highest Router-ID (RID)</strong> "
            "wins. RID = highest loopback IP; if none, highest active physical interface IP. "
            "Can be set manually with <code>router-id &lt;a.b.c.d&gt;</code>.</li>"
            "</ol>"
            "<p><strong>Non-preemptive:</strong> Once a DR and BDR are elected, they keep "
            "their roles until they fail or OSPF is reset — even if a new router with a higher "
            "priority/RID joins the segment. The new router becomes BDR only; it takes over "
            "as DR only if the current DR fails.</p>"
            "<p>Change interface priority: <code>ip ospf priority &lt;0-255&gt;</code> under "
            "the interface. Use priority 0 to exclude a router from election. "
            "Verify election results with <code>show ip ospf neighbor</code> (look for DR/BDR "
            "in the State column) and <code>show ip ospf interface &lt;int&gt;</code>.</p>"
        ),
        "key_points": [
            "DR and BDR elected on multi-access (broadcast) segments to reduce adjacency count.",
            "Election step 1: highest OSPF interface priority (default 1, range 0-255) wins DR.",
            "Election step 2: tie-break is highest Router-ID.",
            "Priority 0 = ineligible for DR or BDR.",
            "Election is NON-preemptive; a new higher-priority router only becomes BDR, not DR.",
            "DROTHERs form Full adjacency ONLY with DR and BDR; DROTHER–DROTHER pairs stay at 2-Way.",
            "Commands: ip ospf priority <n> | show ip ospf neighbor | show ip ospf interface.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.5  OSPF cost & configuration
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "OSPF cost & configuration",
        "objective": "3.5",
        "video": "OSPF Cost and Configuration",
        "study_topics": ["OSPF cost & configuration"],
        "body": (
            "<p>OSPF uses <strong>cost</strong> as its path metric. The best path is the one "
            "with the lowest cumulative cost from source to destination. Cost is additive — "
            "each outbound interface along the path contributes its cost.</p>"
            "<p><strong>Cost formula:</strong></p>"
            "<pre>Cost = reference bandwidth / interface bandwidth</pre>"
            "<p>Cisco's default reference bandwidth is <strong>100 Mbps (100,000,000 bps)</strong>. "
            "This means Fast Ethernet (100 Mbps) and Gigabit (1 Gbps) both calculate to cost 1 "
            "using the default, which is problematic. Best practice: raise the reference bandwidth "
            "globally on all routers to match the fastest link in your network:</p>"
            "<pre>router ospf 1\n  auto-cost reference-bandwidth 10000</pre>"
            "<p>(Value in Mbps; 10000 = 10 Gbps reference.)</p>"
            "<p><strong>Common default costs:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Interface</th><th>Bandwidth</th><th>Default Cost</th></tr>"
            "<tr><td>Serial (T1)</td><td>1.544 Mbps</td><td>64</td></tr>"
            "<tr><td>Fast Ethernet</td><td>100 Mbps</td><td>1</td></tr>"
            "<tr><td>Gigabit Ethernet</td><td>1000 Mbps</td><td>1</td></tr>"
            "<tr><td>10 Gigabit Ethernet</td><td>10000 Mbps</td><td>1</td></tr>"
            "</table>"
            "<p><strong>Override cost on an interface:</strong> "
            "<code>ip ospf cost &lt;1-65535&gt;</code> — explicit cost always overrides the formula.</p>"
            "<p><strong>Basic OSPFv2 configuration:</strong></p>"
            "<pre>router ospf 1\n  router-id 1.1.1.1\n  network 10.0.0.0 0.0.0.255 area 0</pre>"
            "<p>Alternatively, enable per-interface: "
            "<code>ip ospf 1 area 0</code> under the interface (preferred modern syntax).</p>"
        ),
        "key_points": [
            "OSPF cost = reference bandwidth / interface bandwidth (both in bps).",
            "Default reference bandwidth: 100 Mbps — causes FastEth and GigEth to both equal cost 1.",
            "Fix: auto-cost reference-bandwidth <Mbps> — must be consistent on ALL routers.",
            "Override per-interface: ip ospf cost <value> (takes priority over the formula).",
            "Best path = lowest cumulative cost; costs are summed on outbound interfaces only.",
            "Configure OSPF: router ospf <pid> + network <addr> <wildcard> area <id>.",
            "Modern alternative: ip ospf <pid> area <id> directly under each interface.",
        ],
    },

    # ------------------------------------------------------------------
    # 3.6  First hop redundancy — HSRP / VRRP / GLBP  (combined note)
    # ------------------------------------------------------------------
    {
        "domain": 3,
        "topic": "First hop redundancy protocols (HSRP, VRRP, GLBP)",
        "objective": "3.6",
        "video": "First Hop Redundancy Protocols",
        "study_topics": [
            "First hop redundancy (HSRP/VRRP/GLBP)",
            "First Hop Redundancy Protocols (HSRP, VRRP, GLBP)",
        ],
        "body": (
            "<p>First Hop Redundancy Protocols (FHRPs) present a single <strong>virtual "
            "IP/MAC address</strong> to end hosts so that if the active gateway fails, a "
            "standby router transparently takes over without requiring hosts to change their "
            "default gateway setting.</p>"
            "<p><strong>Comparison of the three protocols:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Feature</th><th>HSRP</th><th>VRRP</th><th>GLBP</th></tr>"
            "<tr><td>Standard</td><td>Cisco proprietary</td><td>Open (RFC 5798)</td><td>Cisco proprietary</td></tr>"
            "<tr><td>Roles</td><td>Active / Standby</td><td>Master / Backup(s)</td><td>AVG + up to 4 AVFs</td></tr>"
            "<tr><td>Virtual MAC</td><td>0000.0C07.ACxx (v1)<br>0000.0C9F.Fxxx (v2)</td>"
            "<td>0000.5E00.01xx</td><td>0007.B4xx.xx00 per AVF</td></tr>"
            "<tr><td>Load balancing</td><td>No (only one active)</td><td>No (only one master)</td>"
            "<td>Yes — multiple AVFs share traffic</td></tr>"
            "<tr><td>Preemption</td><td>Disabled by default</td><td>Enabled by default</td><td>Configurable</td></tr>"
            "<tr><td>Election basis</td><td>Highest priority (default 100)</td>"
            "<td>Highest priority (default 100)</td><td>Highest priority elects AVG</td></tr>"
            "</table>"
            "<p><strong>HSRP details:</strong> Only the active router forwards traffic. "
            "A standby router monitors hellos and takes over if the active fails. "
            "Versions 1 and 2 exist; v2 supports IPv6 and more groups. "
            "Configure: <code>standby &lt;group&gt; ip &lt;vip&gt;</code>; "
            "optionally <code>standby &lt;group&gt; priority &lt;0-255&gt;</code> and "
            "<code>standby &lt;group&gt; preempt</code>.</p>"
            "<p><strong>VRRP details:</strong> The router with the highest priority is the "
            "master; all others are backups. The owner of the actual virtual IP automatically "
            "gets priority 255. Preemption is on by default.</p>"
            "<p><strong>GLBP details:</strong> One Active Virtual Gateway (AVG) answers ARP "
            "requests with different virtual MACs, distributing traffic across up to four "
            "Active Virtual Forwarders (AVFs). This is the only FHRP that provides true "
            "load balancing.</p>"
        ),
        "key_points": [
            "FHRPs provide default-gateway redundancy by sharing a virtual IP and MAC among multiple routers.",
            "HSRP: Cisco-only, Active/Standby, no load balancing, preemption off by default.",
            "VRRP: open standard (RFC 5798), Master/Backup, preemption on by default.",
            "GLBP: Cisco-only, AVG + AVFs, true load balancing across up to 4 forwarders.",
            "HSRP default priority = 100; higher priority wins active/master role.",
            "HSRP virtual MAC: 0000.0C07.ACxx (v1) or 0000.0C9F.Fxxx (v2).",
            "VRRP IP owner gets priority 255 automatically.",
            "Only GLBP load-balances traffic across multiple physical gateways simultaneously.",
        ],
    },
]
