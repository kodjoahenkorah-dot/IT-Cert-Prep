"""Domain 3 — IP Connectivity v3 (Cisco CCNA 200-301).

Third bank of scenario-based, misconception-targeting questions covering
objectives 3.1-3.5. Brand-new scenarios; no paraphrases of v1/v2.
IDs: cd3v3-001 through cd3v3-040.
"""

QUESTIONS = [
    # ------------------------------------------------------------------ 3.1 routing table components
    {
        "id": "cd3v3-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Routing table components",
        "stem": (
            "A router's 'show ip route' output contains the following line:\n"
            "  D EX  172.16.5.0/24 [170/2816000] via 10.1.1.2, GigabitEthernet0/0\n\n"
            "What does the 'D EX' code indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An EIGRP external route — redistributed into EIGRP from another source with a default AD of 170",
                "correct": True,
                "rationale": "Correct. 'D' identifies EIGRP; 'EX' marks an external EIGRP route (redistributed from outside EIGRP). External EIGRP routes have a default administrative distance of 170, higher than internal EIGRP's 90.",
            },
            {
                "id": "b",
                "text": "An OSPF external type-2 route — codes 'D' for DUAL and 'EX' for external",
                "correct": False,
                "rationale": "Incorrect. OSPF external routes are coded 'O E2' or 'O E1'; the 'D' code is EIGRP, not OSPF.",
            },
            {
                "id": "c",
                "text": "A directly connected route that was exported to a routing table",
                "correct": False,
                "rationale": "Incorrect. Directly connected routes use the 'C' code; 'D EX' is specific to EIGRP external.",
            },
            {
                "id": "d",
                "text": "An EIGRP internal route with a metric above 2,000,000",
                "correct": False,
                "rationale": "Incorrect. EIGRP internal routes are coded simply 'D' (AD 90); 'EX' distinguishes external (redistributed) routes with AD 170.",
            },
        ],
        "explanation": (
            "EIGRP route codes: 'D' = EIGRP internal (AD 90), 'D EX' = EIGRP external/redistributed (AD 170). "
            "External routes carry a higher AD to prevent them from accidentally overriding IGP-learned internal routes."
        ),
    },
    {
        "id": "cd3v3-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Routing table components",
        "stem": (
            "A router running OSPFv2 shows:\n"
            "  O IA  192.168.20.0/24 [110/30] via 10.0.0.1, GigabitEthernet0/1\n\n"
            "What does 'O IA' indicate about this route?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is an OSPF inter-area route — learned from a different OSPF area via an ABR",
                "correct": True,
                "rationale": "Correct. 'O IA' stands for OSPF inter-area (IA). It was learned from an Area Border Router (ABR) connecting the local area to the area where 192.168.20.0/24 originates, and is carried in Type 3 Summary LSAs.",
            },
            {
                "id": "b",
                "text": "It is an OSPF intra-area route redistributed internally",
                "correct": False,
                "rationale": "Incorrect. Intra-area OSPF routes are coded 'O' only (no 'IA'); 'O IA' specifically marks inter-area routes summarized by an ABR.",
            },
            {
                "id": "c",
                "text": "It is an OSPF route redistributed from another routing protocol",
                "correct": False,
                "rationale": "Incorrect. Routes redistributed into OSPF are coded 'O E1' or 'O E2' (external); 'O IA' is inter-area, not redistributed.",
            },
            {
                "id": "d",
                "text": "It is an OSPF route learned only via an Ethernet interface",
                "correct": False,
                "rationale": "Incorrect. 'IA' refers to the OSPF area scope (inter-area), not to the interface type through which it was learned.",
            },
        ],
        "explanation": (
            "OSPF route codes: 'O' intra-area (same area), 'O IA' inter-area (via ABR, Type-3 LSA), "
            "'O E1'/'O E2' external (redistributed). Recognising these codes is required for CCNA routing-table interpretation."
        ),
    },
    {
        "id": "cd3v3-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Routing table components",
        "stem": (
            "On Router R1, 'show ip route' shows the following summary line before individual entries:\n"
            "  172.31.0.0/16 is variably subnetted, 4 subnets, 3 masks\n\n"
            "How many distinct prefix lengths are present within the 172.31.0.0/16 block?"
        ),
        "options": [
            {
                "id": "a",
                "text": "3 — the '3 masks' field directly reports the number of distinct prefix lengths",
                "correct": True,
                "rationale": "Correct. The 'variably subnetted' summary line format is '<major-network> is variably subnetted, <N> subnets, <M> masks'. 'M masks' = M distinct prefix lengths (VLSM). Here 3 masks means three different prefix lengths exist.",
            },
            {
                "id": "b",
                "text": "4 — one mask per subnet",
                "correct": False,
                "rationale": "Incorrect. There are 4 subnets total, but only 3 distinct masks, so some subnets share the same prefix length.",
            },
            {
                "id": "c",
                "text": "16 — the /16 classful mask defines the number of mask bits",
                "correct": False,
                "rationale": "Incorrect. The /16 is the classful major network boundary, not the count of distinct subnet masks in use.",
            },
            {
                "id": "d",
                "text": "1 — because the network is subnetted uniformly",
                "correct": False,
                "rationale": "Incorrect. If only one mask were in use the output would not say 'variably subnetted' at all; that phrase specifically indicates multiple (VLSM) masks.",
            },
        ],
        "explanation": (
            "The IOS 'variably subnetted' header reports <subnets> total entries and <masks> distinct prefix lengths for a major network. "
            "Here, 4 subnets use 3 different masks — confirming VLSM is in use and no single fixed-length scheme applies."
        ),
    },
    {
        "id": "cd3v3-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Routing table components",
        "stem": (
            "A new engineer sees this entry and asks you what it means:\n"
            "  S    10.0.0.0/8 [1/0] via 198.51.100.1\n\n"
            "What is the MOST accurate description?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A manually configured static route to the entire Class A block 10.0.0.0/8, with AD 1 and metric 0, forwarded to next-hop 198.51.100.1",
                "correct": True,
                "rationale": "Correct. 'S' = static, /8 = the full Class A range, [1/0] = AD 1 / metric 0 (static default), via 198.51.100.1 = the next-hop address. This is a summary static route covering all of 10.x.x.x.",
            },
            {
                "id": "b",
                "text": "An OSPF route aggregated by an ABR into a /8 summary",
                "correct": False,
                "rationale": "Incorrect. OSPF routes are coded 'O' or 'O IA'; 'S' is unambiguously a static route.",
            },
            {
                "id": "c",
                "text": "A connected route detected on an interface with IP 10.0.0.0/8",
                "correct": False,
                "rationale": "Incorrect. Connected routes use code 'C' and AD 0; this entry has code 'S' and AD 1, both hallmarks of a static route.",
            },
            {
                "id": "d",
                "text": "A route learned from RIP with hop count 0",
                "correct": False,
                "rationale": "Incorrect. RIP routes use code 'R' (not 'S') and RIP's AD is 120 (not 1). The [1/0] bracket confirms this is a static route.",
            },
        ],
        "explanation": (
            "Static route code = 'S', AD = 1. A /8 summary covers all of 10.0.0.0 through 10.255.255.255. "
            "The metric for static routes is 0. More specific (longer-prefix) routes in the table will still override this summary."
        ),
    },
    # ------------------------------------------------------------------ 3.2 forwarding decision / LPM / AD
    {
        "id": "cd3v3-005",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Forwarding decision & longest prefix match",
        "stem": (
            "A router holds these routes:\n"
            "  S    10.10.0.0/16  [1/0]   via 172.16.0.1\n"
            "  O    10.10.10.0/24 [110/5] via 172.16.0.2\n"
            "  D    10.10.10.0/23 [90/2] via 172.16.0.3\n"
            "  S*   0.0.0.0/0    [1/0]   via 172.16.0.9\n\n"
            "A packet arrives destined for 10.10.10.200. Which route is used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "O 10.10.10.0/24 via 172.16.0.2",
                "correct": True,
                "rationale": "Correct. 10.10.10.200 falls in 10.10.10.0/24 (.0-.255), 10.10.10.0/23 (10.10.10.0-10.10.11.255), and 10.10.0.0/16. Among matching routes, the /24 is the longest (most specific) prefix, so it wins regardless of AD. AD 110 vs 90 vs 1 is irrelevant when prefix lengths differ.",
            },
            {
                "id": "b",
                "text": "S 10.10.0.0/16 via 172.16.0.1 (lowest AD=1)",
                "correct": False,
                "rationale": "Incorrect. AD is only compared among routes of the SAME prefix length. The /16 is less specific than the /24 and /23 that also contain .200, so it loses to the longer matches regardless of its AD 1.",
            },
            {
                "id": "c",
                "text": "D 10.10.10.0/23 via 172.16.0.3 (EIGRP lowest AD among the /23 and /24)",
                "correct": False,
                "rationale": "Incorrect. The /24 is longer (more specific) than the /23; both contain .200 but the /24 is preferred by longest-prefix-match. AD is not compared across different prefix lengths.",
            },
            {
                "id": "d",
                "text": "S* 0.0.0.0/0 via 172.16.0.9 (default route always used first)",
                "correct": False,
                "rationale": "Incorrect. The default route is used only when no more specific route matches. Several specific routes match .200, so the default is not used.",
            },
        ],
        "explanation": (
            "Longest-prefix-match applies first: the router finds ALL routes that contain the destination, "
            "then picks the one with the most specific (longest) mask. /24 > /23 > /16 > /0 for .200, so the OSPF /24 wins."
        ),
    },
    {
        "id": "cd3v3-006",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Forwarding decision & longest prefix match",
        "stem": (
            "Router R has:\n"
            "  O    192.168.1.64/26  [110/20] via 10.0.0.1\n"
            "  S    192.168.1.0/24   [1/0]    via 10.0.0.2\n\n"
            "A packet arrives for 192.168.1.100. Which statement is TRUE about the forwarding decision?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The packet is forwarded via 10.0.0.1 because the /26 is more specific than the /24, and .100 is within 192.168.1.64–192.168.1.127",
                "correct": True,
                "rationale": "Correct. 192.168.1.100 is within the /26 range (.64–.127) and also within the /24 (.0–.255). The /26 is the longer prefix and wins despite OSPF's higher AD (110) vs the static's AD (1). LPM always precedes AD comparison.",
            },
            {
                "id": "b",
                "text": "The packet is forwarded via 10.0.0.2 because the static route (AD 1) beats OSPF (AD 110)",
                "correct": False,
                "rationale": "Incorrect. AD is compared only when two routes share the SAME prefix length. Here the /26 and /24 have different lengths; the /26 is more specific and wins by LPM before AD is ever considered.",
            },
            {
                "id": "c",
                "text": "The router load-balances across 10.0.0.1 and 10.0.0.2",
                "correct": False,
                "rationale": "Incorrect. Load balancing applies only to equal-length-prefix routes with the same AD and metric. Different prefix lengths mean the /26 wins outright.",
            },
            {
                "id": "d",
                "text": "The packet is dropped because the two routes overlap",
                "correct": False,
                "rationale": "Incorrect. Overlapping routes are normal and resolved by longest-prefix-match. The /26 is selected and the packet is forwarded, not dropped.",
            },
        ],
        "explanation": (
            "LPM guarantees that /26 beats /24 for 192.168.1.100 regardless of AD. "
            "AD arbitration occurs only when two routes of IDENTICAL prefix length compete for the routing table."
        ),
    },
    {
        "id": "cd3v3-007",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Administrative distance",
        "stem": (
            "Three routers redistribute the same prefix 10.100.0.0/24 into the local router:\n"
            "  - Via EIGRP external (AD 170)\n"
            "  - Via IS-IS (AD 115)\n"
            "  - Via RIP (AD 120)\n\n"
            "Which route is installed in the routing table?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The IS-IS route, because AD 115 is the lowest of the three",
                "correct": True,
                "rationale": "Correct. For the same prefix, the lowest AD wins. IS-IS (115) < RIP (120) < EIGRP external (170), so the IS-IS route is installed.",
            },
            {
                "id": "b",
                "text": "The EIGRP external route, because EIGRP is a Cisco protocol and preferred over standards-based protocols",
                "correct": False,
                "rationale": "Incorrect. Route selection is purely numerical AD; EIGRP external (170) is the LEAST preferred of the three because its AD is highest.",
            },
            {
                "id": "c",
                "text": "The RIP route, because RIP has the simplest metric",
                "correct": False,
                "rationale": "Incorrect. Simplicity of the metric is irrelevant; AD 120 (RIP) is higher than IS-IS's 115, so RIP loses.",
            },
            {
                "id": "d",
                "text": "All three, load-balanced by equal-cost multipath",
                "correct": False,
                "rationale": "Incorrect. ECMP only applies to routes from the same protocol with equal metrics. Different protocols for the same prefix never load-balance; the lowest-AD source wins.",
            },
        ],
        "explanation": (
            "Default ADs: IS-IS 115, RIP 120, EIGRP external 170. "
            "For a single prefix offered by multiple protocols, the router installs only the lowest-AD candidate. IS-IS wins here."
        ),
    },
    {
        "id": "cd3v3-008",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Administrative distance",
        "stem": (
            "An engineer manually sets a static route's administrative distance to 255 with:\n"
            "  ip route 10.200.0.0 255.255.0.0 192.0.2.1 255\n\n"
            "What is the effect of AD 255?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The route is considered unreachable/unusable and is NOT installed in the routing table",
                "correct": True,
                "rationale": "Correct. Administrative distance 255 is the reserved value for 'unreachable' in IOS. A route with AD 255 is explicitly not installed in the routing table, effectively disabling it while keeping the config line present.",
            },
            {
                "id": "b",
                "text": "The route becomes the most preferred of all routes",
                "correct": False,
                "rationale": "Incorrect. Lower AD = more preferred. AD 255 is the WORST possible value (unreachable), not the best.",
            },
            {
                "id": "c",
                "text": "The route floats behind iBGP routes (AD 200)",
                "correct": False,
                "rationale": "Incorrect. AD 255 is above iBGP's 200, so it would nominally lose to iBGP; but AD 255 is the 'unreachable' marker in IOS, meaning the route is never installed at all — it doesn't float, it's simply disabled.",
            },
            {
                "id": "d",
                "text": "The route is installed but treated as a floating backup for all other routes",
                "correct": False,
                "rationale": "Incorrect. AD 255 = not installed. The route cannot serve as a backup because it is never put in the forwarding table.",
            },
        ],
        "explanation": (
            "AD 255 is a reserved sentinel meaning 'not trustworthy/unreachable'. IOS will not install a route with AD 255, "
            "so it effectively disables the static entry without removing it from the configuration."
        ),
    },
    {
        "id": "cd3v3-009",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Administrative distance",
        "stem": (
            "Which TWO statements about administrative distance are TRUE? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "A lower AD value is MORE trusted and preferred over higher AD values for the same prefix",
                "correct": True,
                "rationale": "Correct. AD is an inverse-trust scale: 0 (connected, most trusted) through 255 (unusable). Lowest AD wins when two sources offer the same prefix.",
            },
            {
                "id": "b",
                "text": "AD is compared only between routes of the same prefix length for the same destination",
                "correct": True,
                "rationale": "Correct. Longest-prefix-match is evaluated first; AD only breaks ties among routes with IDENTICAL prefix lengths (i.e., both sources offer the same /24, for example).",
            },
            {
                "id": "c",
                "text": "Administrative distance is used to compare routes within a single routing protocol to choose the best path",
                "correct": False,
                "rationale": "Incorrect. Within a single protocol, metric (not AD) determines the best path. AD distinguishes trustworthiness between different sources/protocols.",
            },
            {
                "id": "d",
                "text": "AD is carried in routing updates and shared between neighbors",
                "correct": False,
                "rationale": "Incorrect. AD is a locally significant value configured on each router; it is not advertised in routing updates between neighbors.",
            },
        ],
        "explanation": (
            "AD is a local preference value used to pick between different route sources (protocols or static vs dynamic). "
            "Lowest AD wins for an equal-length prefix. It is never shared between routers and is not compared across different prefix lengths."
        ),
    },
    # ------------------------------------------------------------------ 3.3 static routing
    {
        "id": "cd3v3-010",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Static routing",
        "stem": (
            "R1's only path to the 10.50.0.0/24 subnet is through R2. "
            "R2's G0/0 IP is 192.168.5.2 and R1's G0/1 is connected to the same /30 segment as R2's G0/0. "
            "Which command on R1 correctly routes packets to 10.50.0.0/24 through R2?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ip route 10.50.0.0 255.255.255.0 192.168.5.2",
                "correct": True,
                "rationale": "Correct. This creates a static route on R1 pointing to the 10.50.0.0/24 destination via next-hop 192.168.5.2 (R2's interface IP on the shared segment).",
            },
            {
                "id": "b",
                "text": "ip route 192.168.5.2 255.255.255.255 10.50.0.0",
                "correct": False,
                "rationale": "Incorrect. The syntax is reversed: the destination (10.50.0.0/24) must be first, followed by the next-hop. This command would create a host route to 192.168.5.2, not route to 10.50.0.0/24.",
            },
            {
                "id": "c",
                "text": "ip route 10.50.0.0 0.0.0.255 192.168.5.2",
                "correct": False,
                "rationale": "Incorrect. Static routes use subnet masks (255.255.255.0 for /24), not wildcard masks (0.0.0.255). Wildcards are for ACLs and OSPF network statements.",
            },
            {
                "id": "d",
                "text": "ip route 10.50.0.0 255.255.255.0 GigabitEthernet0/0",
                "correct": False,
                "rationale": "Incorrect. R1's outgoing interface is G0/1, not G0/0; and using only an exit interface without a next-hop causes ARP for every destination on this Ethernet segment, which is problematic on multi-access links.",
            },
        ],
        "explanation": (
            "Correct IOS static route syntax: 'ip route <dest-network> <subnet-mask> <next-hop-IP>'. "
            "Always verify you have the destination prefix first and the next-hop reachable on a directly connected link."
        ),
    },
    {
        "id": "cd3v3-011",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Static routing",
        "stem": (
            "An engineer configures a fully specified static route:\n"
            "  ip route 172.20.10.0 255.255.255.0 GigabitEthernet0/2 10.0.2.1\n\n"
            "Why is specifying BOTH the exit interface AND the next-hop IP advantageous compared to "
            "specifying only the exit interface on a multi-access segment?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It resolves the next-hop MAC directly without treating every destination as connected, avoiding excessive ARP generation",
                "correct": True,
                "rationale": "Correct. With an exit interface alone on a multi-access network, the router treats all destinations as directly connected and ARPs for each one. Adding a next-hop IP makes the router resolve only one MAC (the next-hop's), eliminating the ARP flood problem.",
            },
            {
                "id": "b",
                "text": "It enables load balancing across both paths automatically",
                "correct": False,
                "rationale": "Incorrect. A single fully specified static route does not create load balancing; that requires multiple equal-cost entries or ECMP.",
            },
            {
                "id": "c",
                "text": "It changes the route's administrative distance from 1 to 0",
                "correct": False,
                "rationale": "Incorrect. Adding both interface and next-hop does not alter the administrative distance; the static AD remains 1 unless explicitly overridden.",
            },
            {
                "id": "d",
                "text": "It makes the route prefer OSPF routes when OSPF reconverges",
                "correct": False,
                "rationale": "Incorrect. A fully specified static route (AD 1) will still be preferred over OSPF (AD 110) for the same prefix unless configured with a higher AD for floating behavior.",
            },
        ],
        "explanation": (
            "On multi-access links, exit-interface-only static routes cause the router to ARP for each forwarded destination. "
            "A fully specified route (interface + next-hop) pins the ARP to just the next-hop IP, preventing this problem. "
            "Best practice is to always include a next-hop on Ethernet segments."
        ),
    },
    {
        "id": "cd3v3-012",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Static routing",
        "stem": (
            "R1 has two equal-cost static routes to 10.99.0.0/24:\n"
            "  ip route 10.99.0.0 255.255.255.0 10.0.1.1\n"
            "  ip route 10.99.0.0 255.255.255.0 10.0.2.1\n\n"
            "By default, how will R1 forward traffic to destinations in 10.99.0.0/24?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Per-destination load balancing (CEF default) — both next-hops are installed and traffic is balanced based on source/destination IP hash",
                "correct": True,
                "rationale": "Correct. With CEF (Cisco Express Forwarding, enabled by default), equal-cost static routes to the same prefix are both installed and traffic is distributed per-flow (source/destination hash), providing per-destination load balancing.",
            },
            {
                "id": "b",
                "text": "Only the first route is used; IOS ignores duplicate static routes to the same prefix",
                "correct": False,
                "rationale": "Incorrect. IOS installs both equal-cost static routes and uses them for load balancing. Neither is ignored.",
            },
            {
                "id": "c",
                "text": "The router uses only 10.0.1.1 because it was configured first",
                "correct": False,
                "rationale": "Incorrect. Configuration order does not determine preference for equal-cost static routes; both are installed simultaneously.",
            },
            {
                "id": "d",
                "text": "The router drops packets because two routes to the same destination conflict",
                "correct": False,
                "rationale": "Incorrect. Multiple equal-cost routes are a valid and deliberate configuration that creates ECMP, not a conflict.",
            },
        ],
        "explanation": (
            "Two static routes with identical destination, mask, and AD are both installed as equal-cost paths. "
            "With CEF (the default), traffic is load-balanced per-flow (source/destination IP pair). "
            "Per-packet load balancing is also possible with process switching but is rarely used."
        ),
    },
    {
        "id": "cd3v3-013",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Floating static routes",
        "stem": (
            "R1 has a primary OSPF-learned default route (AD 110). An engineer configures:\n"
            "  ip route 0.0.0.0 0.0.0.0 10.0.9.1 105\n\n"
            "Is this a valid floating static route backup for the OSPF default? Why or why not?"
        ),
        "options": [
            {
                "id": "a",
                "text": "No — AD 105 is LOWER than OSPF's 110, so this static will always be preferred and used as the primary, never as a backup",
                "correct": True,
                "rationale": "Correct. For a floating static to back up an OSPF route, its AD must be HIGHER than 110. AD 105 < 110 means the static wins and is always active, defeating the backup intent entirely.",
            },
            {
                "id": "b",
                "text": "Yes — AD 105 creates a valid backup because it is less than 255",
                "correct": False,
                "rationale": "Incorrect. 'Less than 255' is not the relevant threshold; the static's AD must be HIGHER than the primary (OSPF, 110) to float. AD 105 is lower, so it would be preferred over OSPF.",
            },
            {
                "id": "c",
                "text": "Yes — the floating static always floats behind OSPF regardless of its AD value",
                "correct": False,
                "rationale": "Incorrect. AD values explicitly determine which route is installed. At AD 105 this static beats OSPF (110) and is always the active route.",
            },
            {
                "id": "d",
                "text": "No — static default routes cannot coexist with OSPF on the same router",
                "correct": False,
                "rationale": "Incorrect. Static and OSPF default routes can absolutely coexist; AD determines which one is installed. The problem here is AD value, not protocol compatibility.",
            },
        ],
        "explanation": (
            "A floating static default must have AD > 110 (e.g., 120–254) to stay out of the routing table while the OSPF default exists. "
            "AD 105 < 110, so the static would be preferred, permanently replacing the OSPF default — not floating behind it."
        ),
    },
    {
        "id": "cd3v3-014",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Floating static routes",
        "stem": (
            "A branch router uses EIGRP (AD 90) to learn route 192.168.100.0/24 over the primary WAN link. "
            "The engineer adds a floating static:\n"
            "  ip route 192.168.100.0 255.255.255.0 10.10.10.1 95\n\n"
            "The primary WAN link fails and EIGRP loses the route. Does the floating static install? "
            "What happens when the WAN recovers?"
        ),
        "options": [
            {
                "id": "a",
                "text": "AD 95 > 90 so the static correctly floats; when WAN recovers and EIGRP re-learns the /24, EIGRP (AD 90) automatically displaces the static again",
                "correct": True,
                "rationale": "Correct. While EIGRP has the /24 (AD 90 < 95), the static is suppressed. When EIGRP loses it, the static installs (AD 95 now wins by default). When EIGRP re-learns the route, its AD 90 beats 95 again, and the static floats out.",
            },
            {
                "id": "b",
                "text": "AD 95 is too high; only AD values below 90 work for floating statics",
                "correct": False,
                "rationale": "Incorrect. The opposite is true: a floating static needs AD HIGHER than the primary to remain inactive while the primary is present. AD 95 > 90 is correct for floating behind EIGRP.",
            },
            {
                "id": "c",
                "text": "The static always stays in the table once installed and does not float back out when EIGRP recovers",
                "correct": False,
                "rationale": "Incorrect. Route selection is dynamic. When EIGRP re-learns the /24 with AD 90, it beats the static's AD 95 and the static is automatically removed from the routing table.",
            },
            {
                "id": "d",
                "text": "A manual 'clear ip route' command is required to remove the static after the WAN recovers",
                "correct": False,
                "rationale": "Incorrect. No manual intervention is needed; IOS automatically re-installs the better-AD EIGRP route when it reappears, displacing the floating static.",
            },
        ],
        "explanation": (
            "Floating static AD must exceed the primary's AD. The router dynamically competes routes: "
            "primary present → static suppressed; primary gone → static installs; primary returns → primary re-wins. "
            "The process is fully automatic with no manual clearing required."
        ),
    },
    {
        "id": "cd3v3-015",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 static routing",
        "stem": (
            "Which of the following is a valid IPv6 static route to the 2001:db8:acad::/48 network "
            "via next-hop 2001:db8:1::1?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ipv6 route 2001:db8:acad::/48 2001:db8:1::1",
                "correct": True,
                "rationale": "Correct. 'ipv6 route <IPv6-prefix>/<prefix-length> <next-hop-IPv6>' is valid IOS syntax for an IPv6 static route. /48 is a valid prefix length and 2001:db8:1::1 is the next-hop.",
            },
            {
                "id": "b",
                "text": "ip route 2001:db8:acad::/48 2001:db8:1::1",
                "correct": False,
                "rationale": "Incorrect. The 'ip route' command is for IPv4 only. IPv6 static routes require 'ipv6 route'.",
            },
            {
                "id": "c",
                "text": "ipv6 route 2001:db8:acad:: 255.255.255.0 2001:db8:1::1",
                "correct": False,
                "rationale": "Incorrect. IPv6 does not use dotted-decimal subnet masks; prefix length notation (e.g., /48) is used exclusively in IPv6 addressing.",
            },
            {
                "id": "d",
                "text": "ipv6 static-route 2001:db8:acad::/48 2001:db8:1::1",
                "correct": False,
                "rationale": "Incorrect. 'ipv6 static-route' is not a valid IOS command; the correct command is 'ipv6 route'.",
            },
        ],
        "explanation": (
            "IPv6 static route syntax: 'ipv6 route <prefix/len> <next-hop-IPv6 | interface [next-hop]>'. "
            "Uses prefix-length notation (not dotted-decimal masks), and requires the 'ipv6 route' command, not 'ip route'."
        ),
    },
    {
        "id": "cd3v3-016",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 static routing",
        "stem": (
            "An engineer configures an IPv6 static route using a link-local next-hop:\n"
            "  ipv6 route 2001:db8:10::/48 fe80::1\n\n"
            "The router rejects the command. What additional parameter is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The exit interface must be specified alongside the link-local address (e.g., ipv6 route 2001:db8:10::/48 GigabitEthernet0/0 fe80::1)",
                "correct": True,
                "rationale": "Correct. Link-local addresses (fe80::/10) are not globally unique — the same address may exist on multiple interfaces. When using a link-local next-hop, IOS requires an exit interface to identify which link's fe80::1 is intended.",
            },
            {
                "id": "b",
                "text": "The route must use a global unicast next-hop; link-local addresses cannot be next-hops",
                "correct": False,
                "rationale": "Incorrect. Link-local addresses ARE valid next-hops for IPv6 static routes, but only when paired with the exit interface to resolve the ambiguity.",
            },
            {
                "id": "c",
                "text": "The administrative distance must be specified explicitly",
                "correct": False,
                "rationale": "Incorrect. AD is optional (defaults to 1); it is not what is missing here. The problem is the unqualified link-local address.",
            },
            {
                "id": "d",
                "text": "'ipv6 unicast-routing' must be enabled globally first",
                "correct": False,
                "rationale": "Incorrect. While 'ipv6 unicast-routing' is needed to route IPv6, the specific error for this command is the ambiguous link-local next-hop needing an exit interface.",
            },
        ],
        "explanation": (
            "Link-local addresses are scoped to a single link. Because the same fe80::1 could exist on different interfaces, "
            "IOS requires an exit interface when a link-local address is used as the next-hop in an IPv6 static route: "
            "'ipv6 route <prefix> <interface> <link-local-next-hop>'."
        ),
    },
    # ------------------------------------------------------------------ 3.4 OSPF
    {
        "id": "cd3v3-017",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "OSPF cost & configuration",
        "stem": (
            "A network administrator raises the OSPF reference bandwidth to 10,000 Mbps (10 Gbps) on all routers "
            "with: 'auto-cost reference-bandwidth 10000'.\n\n"
            "What is the OSPF cost for a 1 Gbps (1000 Mbps) interface with this new reference?"
        ),
        "options": [
            {
                "id": "a",
                "text": "10 (10000 / 1000 = 10)",
                "correct": True,
                "rationale": "Correct. OSPF cost = reference bandwidth / interface bandwidth = 10000 / 1000 = 10. With a 10 Gbps reference, 1 Gbps interfaces now have cost 10, allowing differentiation from 10 Gbps (cost 1).",
            },
            {
                "id": "b",
                "text": "1 (minimum cost floor)",
                "correct": False,
                "rationale": "Incorrect. The cost floor of 1 only applies when the calculation yields a fraction less than 1 (i.e., interface bandwidth > reference bandwidth). Here 10000/1000 = 10, which is above the minimum.",
            },
            {
                "id": "c",
                "text": "1000 (the raw interface bandwidth in Mbps)",
                "correct": False,
                "rationale": "Incorrect. OSPF cost is reference/bandwidth, not the bandwidth value itself. 10000/1000 = 10.",
            },
            {
                "id": "d",
                "text": "100 (the default reference bandwidth divided by 10)",
                "correct": False,
                "rationale": "Incorrect. The default reference (100 Mbps) is no longer in use; the configured reference is 10000 Mbps. The calculation uses the configured value: 10000/1000 = 10.",
            },
        ],
        "explanation": (
            "OSPF cost = reference_bandwidth / interface_bandwidth (minimum 1). "
            "With reference = 10,000 Mbps: 1 Gbps → cost 10, 10 Gbps → cost 1. "
            "This allows the router to differentiate high-speed links that all appeared as cost 1 with the default 100 Mbps reference."
        ),
    },
    {
        "id": "cd3v3-018",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "OSPF cost & configuration",
        "stem": (
            "R1–R2–R3 form a linear OSPF path. Link costs:\n"
            "  R1 G0/0 → R2: cost 4\n"
            "  R2 G0/1 → R3: cost 10\n\n"
            "Separately, R1–R4–R3 also exists:\n"
            "  R1 G0/1 → R4: cost 3\n"
            "  R4 G0/0 → R3: cost 3\n\n"
            "What is the OSPF cost from R1 to R3 via each path, and which path does R1 select?"
        ),
        "options": [
            {
                "id": "a",
                "text": "R1→R2→R3 = 14, R1→R4→R3 = 6; R1 selects R1→R4→R3 as it has the lower cumulative cost",
                "correct": True,
                "rationale": "Correct. OSPF path cost is the sum of outgoing interface costs: R1-R2-R3 = 4+10 = 14; R1-R4-R3 = 3+3 = 6. SPF always selects the path with the lowest cumulative cost, so R1→R4→R3 (cost 6) wins.",
            },
            {
                "id": "b",
                "text": "R1→R2→R3 = 14, R1→R4→R3 = 9; R1 selects R1→R4→R3",
                "correct": False,
                "rationale": "Incorrect. R1→R4→R3 = 3+3 = 6, not 9. Check the addition: each link's cost is the outgoing interface cost on the forwarding router.",
            },
            {
                "id": "c",
                "text": "R1→R2→R3 = 4, R1→R4→R3 = 3; minimum single-link cost is used",
                "correct": False,
                "rationale": "Incorrect. OSPF sums ALL outgoing interface costs along the path; it does not use the lowest single-link cost.",
            },
            {
                "id": "d",
                "text": "Both paths tie at cost 10 because OSPF uses hop count",
                "correct": False,
                "rationale": "Incorrect. OSPF does not use hop count; it uses cumulative interface cost. The paths have different costs (14 vs 6), not equal hop counts.",
            },
        ],
        "explanation": (
            "OSPF Dijkstra (SPF) computes the sum of outgoing link costs from source to destination. "
            "R1→R2→R3: 4+10=14. R1→R4→R3: 3+3=6. The lower-cost path (6) is installed."
        ),
    },
    {
        "id": "cd3v3-019",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OSPF cost & configuration",
        "stem": (
            "An engineer wants to influence OSPF path selection by manually setting the cost of "
            "GigabitEthernet0/0 to 50. Which interface-level command is used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ip ospf cost 50",
                "correct": True,
                "rationale": "Correct. 'ip ospf cost <1-65535>' is the interface-level IOS command that manually sets the OSPF cost for that interface, overriding the auto-calculated value.",
            },
            {
                "id": "b",
                "text": "ospf cost 50 (under router ospf)",
                "correct": False,
                "rationale": "Incorrect. OSPF cost is set per-interface, not under the routing process. The interface command is 'ip ospf cost <value>'.",
            },
            {
                "id": "c",
                "text": "bandwidth 50 (adjusting bandwidth to achieve cost 50 with default reference)",
                "correct": False,
                "rationale": "Incorrect. While changing bandwidth affects the auto-calculated cost, it also affects other protocols and QoS policies. The direct command 'ip ospf cost 50' is the intended approach for OSPF cost tuning.",
            },
            {
                "id": "d",
                "text": "auto-cost reference-bandwidth 50",
                "correct": False,
                "rationale": "Incorrect. 'auto-cost reference-bandwidth' sets the reference used for ALL interfaces in the OSPF process, not a single interface's cost. It would also need to be matched on all OSPF routers.",
            },
        ],
        "explanation": (
            "Manual per-interface OSPF cost: 'ip ospf cost <1–65535>' under the interface. "
            "This overrides the auto-calculation and is the cleanest way to tune individual link costs. "
            "If set, the cost is used directly; auto-calculation via 'reference-bandwidth / interface-bandwidth' is only used when no manual cost is set."
        ),
    },
    {
        "id": "cd3v3-020",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OSPF adjacencies",
        "stem": (
            "R1 and R2 are OSPF neighbors on a broadcast segment. R1 shows the neighbor as FULL/DR, "
            "while R2 shows R1 as FULL/BDR. Which statement best explains these states?"
        ),
        "options": [
            {
                "id": "a",
                "text": "R2 is the DR and R1 is the BDR; each router shows its OWN role in the second field — FULL indicates full adjacency",
                "correct": True,
                "rationale": "Correct. The format is <state>/<role-of-the-LOCAL-router-on-this-segment>. R1 sees neighbor R2 (who is DR) and R1 itself is the BDR — so R1 displays 'FULL/BDR' for R2. R2 sees R1 (who is BDR) and R2 is DR — so R2 displays 'FULL/DR' for R1. Wait — actually the second field is the NEIGHBOR's DR role, not the local role. Let's re-read: FULL/DR means the neighbor IS the DR; FULL/BDR means the neighbor is the BDR. So if R1 shows R2 as FULL/DR: R2 is DR. R2 shows R1 as FULL/BDR: R1 is BDR. Both are fully adjacent (FULL).",
            },
            {
                "id": "b",
                "text": "The states indicate an error — a router cannot be simultaneously FULL with both a DR and a BDR",
                "correct": False,
                "rationale": "Incorrect. On a broadcast segment it is completely normal for a DROTHER or BDR router to be FULL with both the DR and BDR. FULL/DR and FULL/BDR simply mean the adjacency is complete with the router that holds those roles.",
            },
            {
                "id": "c",
                "text": "Both routers are DRs because each reports FULL state",
                "correct": False,
                "rationale": "Incorrect. FULL describes the adjacency state (synchronized LSDBs), not the DR role. The /DR or /BDR suffix describes the neighbor's role on the segment.",
            },
            {
                "id": "d",
                "text": "The FULL/DR state means the router is running as an ABR",
                "correct": False,
                "rationale": "Incorrect. ABR (Area Border Router) is an OSPF topology role (connecting multiple areas), unrelated to the DR/BDR neighbor-state display in 'show ip ospf neighbor'.",
            },
        ],
        "explanation": (
            "In 'show ip ospf neighbor', <state>/<role> describes the adjacency state (FULL = synchronized) and the NEIGHBOR's DR role on the segment. "
            "FULL/DR = neighbor is the DR; FULL/BDR = neighbor is the BDR; FULL/DROTHER = neither DR nor BDR."
        ),
    },
    {
        "id": "cd3v3-021",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "OSPF adjacencies",
        "stem": (
            "Two OSPF routers form adjacency correctly in a lab. In production, they are placed on the same "
            "broadcast segment but fail to exchange LSDBs, stuck in EXCHANGE state. "
            "The engineer checks and finds hello/dead timers match, area IDs match, and no authentication is configured. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An MTU mismatch between the two interfaces",
                "correct": True,
                "rationale": "Correct. OSPF checks interface MTU during the EXCHANGE phase (Database Description packets). If MTUs differ, oversized DBD packets are dropped and the adjacency stalls in EXCHANGE/LOADING. MTU mismatch is the classic cause of this symptom when timers, area, and auth already match.",
            },
            {
                "id": "b",
                "text": "Different OSPF process IDs on each router",
                "correct": False,
                "rationale": "Incorrect. OSPF process IDs are locally significant and do not need to match for neighbors to form an adjacency.",
            },
            {
                "id": "c",
                "text": "Mismatched router IDs",
                "correct": False,
                "rationale": "Incorrect. Router IDs must be unique (not matching); duplicate RIDs would cause OSPF problems but different RIDs are normal and expected.",
            },
            {
                "id": "d",
                "text": "One router has 'passive-interface' configured on its OSPF-facing interface",
                "correct": False,
                "rationale": "Incorrect. A passive interface suppresses hellos, so the adjacency would not even reach 2-WAY — it would never get to EXCHANGE. The scenario says they are in EXCHANGE, so hellos are working.",
            },
        ],
        "explanation": (
            "OSPF adjacency failure in EXCHANGE/LOADING (after hellos succeed and timers match) is a classic MTU mismatch symptom. "
            "Large DBD packets exceed the lower MTU and are silently dropped. "
            "Fix with matching MTUs or 'ip ospf mtu-ignore' as a workaround."
        ),
    },
    {
        "id": "cd3v3-022",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OSPF adjacencies",
        "stem": (
            "When two DROTHER OSPF routers on the same broadcast segment see each other, "
            "what neighbor state do they reach, and why don't they fully synchronize LSDBs with each other?"
        ),
        "options": [
            {
                "id": "a",
                "text": "2-WAY — OSPF design requires DROTHERs to only fully synchronize (FULL) with the DR and BDR, reducing the number of adjacencies on the segment",
                "correct": True,
                "rationale": "Correct. On broadcast segments, DROTHER routers intentionally remain in 2-WAY with other DROTHERs. Full adjacencies are only formed with the DR and BDR. This reduces the n(n-1)/2 adjacency mesh to 2n-3, which is the entire purpose of DR/BDR.",
            },
            {
                "id": "b",
                "text": "FULL — every OSPF router pair must fully synchronize their LSDBs",
                "correct": False,
                "rationale": "Incorrect. Only DROTHER-to-DR and DROTHER-to-BDR adjacencies reach FULL. DROTHER-to-DROTHER adjacencies intentionally stop at 2-WAY.",
            },
            {
                "id": "c",
                "text": "LOADING — they are waiting to receive missing LSAs from each other",
                "correct": False,
                "rationale": "Incorrect. LOADING is a transient state during database exchange; it is not a stable resting state. 2-WAY is the intentional stable state for DROTHER pairs.",
            },
            {
                "id": "d",
                "text": "INIT — they can't move past INIT without matching priorities",
                "correct": False,
                "rationale": "Incorrect. INIT only requires a hello to be received. DROTHER pairs progress to 2-WAY (bidirectional) and deliberately stay there; priority matching is not required for adjacency.",
            },
        ],
        "explanation": (
            "On broadcast segments, DROTHER routers stabilize at 2-WAY with each other. "
            "Full (FULL) adjacencies exist only between each router and the DR/BDR. "
            "This intentional design reduces adjacency count from O(n²) to O(n), scaling OSPF on shared media."
        ),
    },
    {
        "id": "cd3v3-023",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OSPF adjacencies",
        "stem": (
            "An engineer configures OSPFv2 with 'network 10.0.0.0 0.0.0.255 area 0' on R1 and "
            "'network 10.0.0.0 0.0.0.255 area 1' on R2, both on the same /24 Ethernet segment. "
            "What problem occurs?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OSPF adjacency will NOT form because the area IDs don't match on the shared segment",
                "correct": True,
                "rationale": "Correct. OSPF requires both interfaces on the same segment to be in the same area. R1 assigns the interface to area 0, R2 to area 1 — this mismatch prevents adjacency formation.",
            },
            {
                "id": "b",
                "text": "OSPF will form adjacency but the routes will have higher cost",
                "correct": False,
                "rationale": "Incorrect. Area mismatch is a hard requirement; adjacency simply does not form. Cost is irrelevant when adjacency is blocked.",
            },
            {
                "id": "c",
                "text": "Both routers become ABRs automatically",
                "correct": False,
                "rationale": "Incorrect. ABRs are routers physically connected to multiple OSPF areas with different interfaces. Misconfiguring a single shared interface to different areas on different routers creates a misconfiguration, not ABRs.",
            },
            {
                "id": "d",
                "text": "OSPF forms adjacency in area 0 because area 0 takes precedence",
                "correct": False,
                "rationale": "Incorrect. There is no 'area 0 precedence' override; area IDs must explicitly match in hellos. Area mismatch simply blocks adjacency.",
            },
        ],
        "explanation": (
            "OSPF hello packets contain the area ID. If the area IDs in hellos don't match, "
            "the routers will not form an adjacency. Both sides of a link must be configured in the same OSPF area."
        ),
    },
    {
        "id": "cd3v3-024",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "OSPF adjacencies",
        "stem": (
            "Which TWO of the following would prevent an OSPF adjacency from forming between two routers on a broadcast segment? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Different OSPF area IDs configured on the connecting interfaces",
                "correct": True,
                "rationale": "Correct. Area ID must match in hello packets; a mismatch blocks adjacency formation.",
            },
            {
                "id": "b",
                "text": "Mismatched hello timer values (R1 = 10 s, R2 = 30 s)",
                "correct": True,
                "rationale": "Correct. Hello and dead timers must match between OSPF neighbors. A mismatch causes the dead timer to fire before hellos are accepted, preventing stable adjacency.",
            },
            {
                "id": "c",
                "text": "Different OSPF process IDs on each router",
                "correct": False,
                "rationale": "Incorrect. Process IDs are locally significant and do not need to match for neighbors to form an adjacency.",
            },
            {
                "id": "d",
                "text": "Different OSPF router IDs",
                "correct": False,
                "rationale": "Incorrect. Router IDs must be unique (not equal) between OSPF neighbors. Two routers having different RIDs is normal and required.",
            },
        ],
        "explanation": (
            "OSPF adjacency requirements include: same area ID, same subnet/mask, matching hello/dead timers, "
            "matching authentication, matching MTU, and matching stub flags. Process ID and RID need not match; RIDs must be unique."
        ),
    },
    {
        "id": "cd3v3-025",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OSPF DR/BDR election",
        "stem": (
            "Five routers share an OSPF broadcast segment:\n"
            "  R1: priority 5, RID 5.5.5.5\n"
            "  R2: priority 5, RID 4.4.4.4\n"
            "  R3: priority 0, RID 3.3.3.3\n"
            "  R4: priority 0, RID 2.2.2.2\n"
            "  R5: priority 0, RID 1.1.1.1\n\n"
            "Which router becomes the BDR?"
        ),
        "options": [
            {
                "id": "a",
                "text": "R2 (priority 5, RID 4.4.4.4)",
                "correct": True,
                "rationale": "Correct. DR is R1 (highest priority 5, then highest RID 5.5.5.5). BDR is the second-highest eligible router: R2 also has priority 5 but RID 4.4.4.4 (lower than R1's 5.5.5.5). R2 is BDR. Routers with priority 0 are ineligible.",
            },
            {
                "id": "b",
                "text": "R3 (highest RID among priority-0 routers)",
                "correct": False,
                "rationale": "Incorrect. Priority 0 means ineligible for DR and BDR. R3 cannot become BDR regardless of its RID.",
            },
            {
                "id": "c",
                "text": "R1 (DR becomes BDR when priorities are tied)",
                "correct": False,
                "rationale": "Incorrect. R1 is the DR (highest priority + highest RID tie-break). The BDR is the runner-up — R2. One router cannot be both DR and BDR simultaneously.",
            },
            {
                "id": "d",
                "text": "No BDR is elected because three routers have priority 0",
                "correct": False,
                "rationale": "Incorrect. Only priority-0 routers are excluded; there are still two eligible routers (R1, R2) with priority 5. R1 = DR, R2 = BDR.",
            },
        ],
        "explanation": (
            "DR/BDR election: priority-0 routers are completely ineligible. "
            "Among eligible routers, highest priority wins DR; second-highest wins BDR. "
            "Tie in priority is broken by highest RID. Here R1 (priority 5, RID 5.5.5.5) = DR; R2 (priority 5, RID 4.4.4.4) = BDR."
        ),
    },
    {
        "id": "cd3v3-026",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OSPF DR/BDR election",
        "stem": (
            "On a broadcast OSPF segment, routers communicate using two multicast addresses. "
            "A DROTHER router sends an LSU (Link State Update) to the DR and BDR to notify them of a topology change. "
            "Which destination address does the DROTHER use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "224.0.0.6 (AllDRouters) — sent specifically to the DR and BDR",
                "correct": True,
                "rationale": "Correct. DROTHER routers send LSAs and LSUs to 224.0.0.6 (AllDRouters), which is heard only by the DR and BDR. The DR then forwards the LSA to all OSPF routers using 224.0.0.5 (AllSPFRouters).",
            },
            {
                "id": "b",
                "text": "224.0.0.5 (AllSPFRouters) — sent to every OSPF router on the segment",
                "correct": False,
                "rationale": "Incorrect. 224.0.0.5 is used by the DR to flood LSAs to ALL OSPF routers. DROTHERs send updates to 224.0.0.6 (AllDRouters) so only the DR/BDR receive them.",
            },
            {
                "id": "c",
                "text": "The DR's unicast IP address",
                "correct": False,
                "rationale": "Incorrect. OSPF uses multicast on broadcast segments; 224.0.0.6 reaches both DR and BDR simultaneously, which is more efficient than separate unicast.",
            },
            {
                "id": "d",
                "text": "255.255.255.255 (limited broadcast)",
                "correct": False,
                "rationale": "Incorrect. OSPF uses Layer 3 multicast (224.0.0.5/224.0.0.6), not the limited broadcast address.",
            },
        ],
        "explanation": (
            "OSPF multicast addresses: 224.0.0.5 (AllSPFRouters) is used by the DR to distribute LSAs to all OSPF routers. "
            "224.0.0.6 (AllDRouters) is used by DROTHERs to send LSAs to the DR/BDR. "
            "The DR then replicates to all via 224.0.0.5."
        ),
    },
    {
        "id": "cd3v3-027",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OSPF cost & configuration",
        "stem": (
            "An interface running OSPF has 'ip ospf cost 100' configured manually. "
            "The administrator later changes the interface bandwidth with 'bandwidth 1000000' (1 Gbps). "
            "What is the resulting OSPF cost on the interface?"
        ),
        "options": [
            {
                "id": "a",
                "text": "100 — the manually configured cost overrides any auto-calculated value",
                "correct": True,
                "rationale": "Correct. When 'ip ospf cost' is manually set, it takes precedence over the auto-calculated cost (reference/bandwidth). Changing the interface bandwidth does NOT override a manually set OSPF cost.",
            },
            {
                "id": "b",
                "text": "1 — auto-calculated as reference(100 Mbps)/bandwidth(1000 Mbps), rounded up",
                "correct": False,
                "rationale": "Incorrect. The auto-calculation would yield 1, but the manual 'ip ospf cost 100' overrides it. Auto-calculation is only used when no manual cost is configured.",
            },
            {
                "id": "c",
                "text": "The cost cannot be calculated because bandwidth exceeds the reference",
                "correct": False,
                "rationale": "Incorrect. When bandwidth exceeds the reference, the auto-calculated cost is 1 (minimum). But again, a manual cost is already set and takes absolute priority.",
            },
            {
                "id": "d",
                "text": "The cost reverts to the default 1 automatically when bandwidth changes",
                "correct": False,
                "rationale": "Incorrect. Changing the bandwidth statement does not remove or override a manually configured 'ip ospf cost'. The manual setting persists until explicitly removed.",
            },
        ],
        "explanation": (
            "Manual 'ip ospf cost <value>' overrides auto-calculation. "
            "To revert to auto-calculation, use 'no ip ospf cost'. Until then, any bandwidth change is irrelevant to OSPF cost."
        ),
    },
    {
        "id": "cd3v3-028",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "OSPF cost & configuration",
        "stem": (
            "Which TWO commands can be used on a Cisco router to place an interface into OSPF area 0 "
            "without using the 'network' statement under 'router ospf'? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ip ospf 1 area 0 (configured directly on the interface)",
                "correct": True,
                "rationale": "Correct. The per-interface command 'ip ospf <process-id> area <area-id>' is an alternative to 'network' statements and directly assigns an interface to an OSPF area.",
            },
            {
                "id": "b",
                "text": "network 0.0.0.0 255.255.255.255 area 0 (catch-all wildcard under router ospf)",
                "correct": True,
                "rationale": "Correct. Using the all-zeros address with a full wildcard mask 255.255.255.255 matches every interface on the router, placing them all in area 0. This is a valid (if broad) technique to avoid listing individual networks.",
            },
            {
                "id": "c",
                "text": "ospf area 0 (global config command)",
                "correct": False,
                "rationale": "Incorrect. 'ospf area 0' is not a valid IOS command in any configuration mode. Area assignment is done via 'ip ospf' on an interface or 'network' under 'router ospf'.",
            },
            {
                "id": "d",
                "text": "router ospf 1 (with no network statements) automatically includes all interfaces",
                "correct": False,
                "rationale": "Incorrect. Without network statements or per-interface 'ip ospf' commands, 'router ospf 1' alone does not enable OSPF on any interface.",
            },
        ],
        "explanation": (
            "Two methods to enable OSPF on interfaces: (1) 'network <addr> <wildcard> area <n>' under 'router ospf', "
            "or (2) 'ip ospf <pid> area <n>' directly on each interface. "
            "The catch-all 'network 0.0.0.0 255.255.255.255' is a shortcut that matches all active interfaces."
        ),
    },
    # ------------------------------------------------------------------ 3.5 FHRP
    {
        "id": "cd3v3-029",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "First hop redundancy (HSRP/VRRP/GLBP)",
        "stem": (
            "An HSRP group is configured on two routers (R1 and R2) protecting VLAN 10. "
            "R1 has priority 110 and R2 has priority 100. Preemption is NOT enabled. "
            "R1 (the active router) loses power and R2 becomes active. When R1 returns, "
            "what happens to the active role?"
        ),
        "options": [
            {
                "id": "a",
                "text": "R2 remains active because preemption is disabled — R1's higher priority does not automatically reclaim the role",
                "correct": True,
                "rationale": "Correct. Without 'standby <group> preempt' on R1, a recovering router will NOT seize the active role even with higher priority. R2 stays active until it fails or HSRP is manually cleared.",
            },
            {
                "id": "b",
                "text": "R1 immediately reclaims active status because its priority (110) is higher",
                "correct": False,
                "rationale": "Incorrect. HSRP does not automatically preempt without 'standby preempt'. R1 returns to standby role regardless of its higher priority.",
            },
            {
                "id": "c",
                "text": "A new election is triggered and both routers negotiate freshly regardless of preempt",
                "correct": False,
                "rationale": "Incorrect. A fresh election only occurs when the active router fails. When a router rejoins, it defaults to standby if an active already exists and preemption is disabled.",
            },
            {
                "id": "d",
                "text": "R1 and R2 both become active, causing a split-brain condition",
                "correct": False,
                "rationale": "Incorrect. HSRP hellos allow both routers to see each other; R1 sees R2 already active and takes the standby role, not a second active role.",
            },
        ],
        "explanation": (
            "HSRP preemption ('standby <group> preempt') must be explicitly enabled for a returning higher-priority router to reclaim active. "
            "Without it, the current active remains active indefinitely after recovery."
        ),
    },
    {
        "id": "cd3v3-030",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "First hop redundancy (HSRP/VRRP/GLBP)",
        "stem": (
            "Which command configures R1 to participate in HSRP group 10 with virtual IP 192.168.1.254, "
            "priority 120, and enables preemption?"
        ),
        "options": [
            {
                "id": "a",
                "text": "standby 10 ip 192.168.1.254\nstandby 10 priority 120\nstandby 10 preempt",
                "correct": True,
                "rationale": "Correct. HSRP is configured under the interface with 'standby <group> ip <virtual-ip>', 'standby <group> priority <value>', and 'standby <group> preempt'. All three are needed for the described configuration.",
            },
            {
                "id": "b",
                "text": "hsrp group 10 virtual-ip 192.168.1.254 priority 120 preempt",
                "correct": False,
                "rationale": "Incorrect. This is not valid IOS syntax. HSRP uses separate 'standby' commands, not a single 'hsrp group' command with combined options.",
            },
            {
                "id": "c",
                "text": "vrrp 10 ip 192.168.1.254\nvrrp 10 priority 120",
                "correct": False,
                "rationale": "Incorrect. 'vrrp' is VRRP syntax, not HSRP. The question asks for HSRP configuration, which uses the 'standby' keyword.",
            },
            {
                "id": "d",
                "text": "standby 10 ip 192.168.1.254\nstandby 10 priority 120\n(preemption is on by default)",
                "correct": False,
                "rationale": "Incorrect. HSRP preemption is NOT on by default. It must be explicitly enabled with 'standby <group> preempt'.",
            },
        ],
        "explanation": (
            "HSRP interface commands: 'standby <grp> ip <VIP>' sets the virtual IP, "
            "'standby <grp> priority <n>' sets the election priority, "
            "and 'standby <grp> preempt' (not default) allows a higher-priority router to take over an existing active."
        ),
    },
    {
        "id": "cd3v3-031",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "First hop redundancy (HSRP/VRRP/GLBP)",
        "stem": (
            "In VRRP, the router that owns the virtual IP address (i.e., the virtual IP is one of its real interface addresses) "
            "has what default behavior regarding priority?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The IP owner automatically has priority 255 and is always the master, overriding any configured priority",
                "correct": True,
                "rationale": "Correct. VRRP gives the IP address owner priority 255 (the highest possible), making it always the master for that group. This is a key difference from HSRP, where the virtual IP is typically NOT one of the router's real addresses.",
            },
            {
                "id": "b",
                "text": "The IP owner has priority 100 (the default) just like every other VRRP router",
                "correct": False,
                "rationale": "Incorrect. VRRP explicitly elevates the IP owner to priority 255, not the default 100. This ensures the IP owner is always master.",
            },
            {
                "id": "c",
                "text": "The IP owner cannot participate in VRRP because owning the virtual IP creates a conflict",
                "correct": False,
                "rationale": "Incorrect. VRRP explicitly allows (and prefers) the IP owner; in fact the virtual IP in VRRP is often a real interface address on one of the routers.",
            },
            {
                "id": "d",
                "text": "The IP owner has the lowest priority and acts as the backup by default",
                "correct": False,
                "rationale": "Incorrect. This is backwards: the IP owner has the highest priority (255) and is the master, not the backup.",
            },
        ],
        "explanation": (
            "VRRP priority 255 is reserved for the router that owns the virtual IP address (the virtual IP matches one of its real interface IPs). "
            "This router is always the master. In HSRP, the virtual IP is typically a distinct address not owned by any router."
        ),
    },
    {
        "id": "cd3v3-032",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "First hop redundancy (HSRP/VRRP/GLBP)",
        "stem": (
            "A network uses GLBP with four routers in the same group. A host ARPs for the virtual gateway IP. "
            "What makes GLBP's ARP reply different from HSRP's?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The GLBP AVG assigns a different virtual MAC address from its pool to each ARP reply, directing different hosts to different AVFs for load balancing",
                "correct": True,
                "rationale": "Correct. In GLBP, the Active Virtual Gateway (AVG) answers all ARP requests for the VIP but responds with different virtual MAC addresses (one per Active Virtual Forwarder, up to 4). Each MAC is answered by a different router, distributing outbound traffic.",
            },
            {
                "id": "b",
                "text": "GLBP sends the real MAC of the active router, just like HSRP",
                "correct": False,
                "rationale": "Incorrect. Both GLBP and HSRP use virtual MACs (not real interface MACs) in ARP replies; the difference is GLBP rotates among multiple virtual MACs to spread load across routers.",
            },
            {
                "id": "c",
                "text": "GLBP returns multiple MAC addresses in a single ARP reply",
                "correct": False,
                "rationale": "Incorrect. Each ARP reply contains one MAC address, but successive ARP replies from different hosts may get different virtual MACs (round-robin or weighted), directing them to different AVFs.",
            },
            {
                "id": "d",
                "text": "GLBP returns the virtual IP as the gateway MAC in the ARP reply",
                "correct": False,
                "rationale": "Incorrect. A MAC address is a Layer 2 address; ARP returns a MAC, not an IP. GLBP returns one of its pool of virtual MACs (e.g., 0007.b4xx.xxxx format).",
            },
        ],
        "explanation": (
            "GLBP's AVG serves as the single ARP responder for the VIP but assigns different virtual MACs to different hosts, "
            "pointing them to different AVFs. This achieves actual per-host load balancing with a single virtual IP — "
            "something HSRP and VRRP (single forwarder per group) cannot do natively."
        ),
    },
    {
        "id": "cd3v3-033",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "First hop redundancy (HSRP/VRRP/GLBP)",
        "stem": (
            "Which TWO statements correctly describe differences between HSRPv1 and HSRPv2? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "HSRPv2 supports up to 4096 groups (0–4095) while HSRPv1 supports only 256 groups (0–255)",
                "correct": True,
                "rationale": "Correct. HSRPv1 supports group numbers 0–255 (256 groups). HSRPv2 extends this to 0–4095 (4096 groups), aligning group numbers with VLAN IDs for easier management.",
            },
            {
                "id": "b",
                "text": "HSRPv2 uses IPv6-style multicast addresses while HSRPv1 uses 224.0.0.2",
                "correct": True,
                "rationale": "Correct. HSRPv1 uses 224.0.0.2 for hellos. HSRPv2 uses 224.0.0.102 for IPv4 and ff02::66 for IPv6 HSRP. The different multicast addresses also mean v1 and v2 groups are incompatible on the same segment.",
            },
            {
                "id": "c",
                "text": "HSRPv1 supports load balancing across forwarders; HSRPv2 requires GLBP for load balancing",
                "correct": False,
                "rationale": "Incorrect. Neither HSRPv1 nor HSRPv2 performs per-host load balancing within a single group; both are active/standby. Load balancing via HSRP requires multiple groups with different active routers.",
            },
            {
                "id": "d",
                "text": "HSRPv2 is an open IEEE standard while HSRPv1 is Cisco-proprietary",
                "correct": False,
                "rationale": "Incorrect. Both HSRPv1 and HSRPv2 are Cisco-proprietary. VRRP is the open-standard equivalent.",
            },
        ],
        "explanation": (
            "HSRPv2 improvements over v1: group number range expanded to 0–4095 (matching VLAN IDs), "
            "uses 224.0.0.102 multicast (IPv4) instead of 224.0.0.2, "
            "and supports millisecond timer granularity. Both versions remain Cisco-proprietary."
        ),
    },
    {
        "id": "cd3v3-034",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "First hop redundancy (HSRP/VRRP/GLBP)",
        "stem": (
            "An HSRP active router is configured with 'standby 1 track GigabitEthernet0/1 30'. "
            "What happens if G0/1 goes down?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router's HSRP priority is decremented by 30; if the result falls below the standby's priority (and preempt is set), the standby becomes active",
                "correct": True,
                "rationale": "Correct. Object/interface tracking decrements the HSRP priority by the specified decrement (30) when the tracked interface fails. If the decrement causes the priority to fall below the standby's, and the standby has preempt enabled, a failover occurs.",
            },
            {
                "id": "b",
                "text": "The router is immediately removed from the HSRP group",
                "correct": False,
                "rationale": "Incorrect. Interface tracking only adjusts the priority; the router remains in the HSRP group. It becomes a candidate to lose the active role depending on priorities.",
            },
            {
                "id": "c",
                "text": "The HSRP group is dissolved and must be manually re-configured",
                "correct": False,
                "rationale": "Incorrect. Interface tracking is a graceful mechanism that adjusts priority; the group continues and no reconfiguration is needed.",
            },
            {
                "id": "d",
                "text": "G0/1 going down has no effect unless G0/1 is the HSRP tracking interface itself",
                "correct": False,
                "rationale": "Incorrect. The command explicitly tracks G0/1; if G0/1 fails, the priority decrements by 30 as configured.",
            },
        ],
        "explanation": (
            "HSRP interface tracking allows a router to reduce its priority if an upstream or critical interface fails. "
            "Syntax: 'standby <grp> track <interface> <decrement>'. "
            "Combined with preempt on the standby router, this achieves automatic failover when the active loses connectivity."
        ),
    },
    # ------------------------------------------------------------------ mix of topics for depth
    {
        "id": "cd3v3-035",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Forwarding decision & longest prefix match",
        "stem": (
            "A router's table shows ONLY:\n"
            "  C   10.1.1.0/30  [0/0]  GigabitEthernet0/0\n"
            "  L   10.1.1.1/32  [0/0]  GigabitEthernet0/0\n"
            "  S*  0.0.0.0/0    [1/0]  via 10.1.1.2\n\n"
            "A packet arrives destined for 10.1.1.1. Which route is matched and what is the outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The /32 local route (L) is matched; the router processes the packet locally (it is addressed to the router itself)",
                "correct": True,
                "rationale": "Correct. 10.1.1.1/32 is the router's own interface address (L = local). When a packet is destined for the router's own IP, the /32 host route is matched (longest prefix, most specific), and the packet is delivered to the router's local processes, not forwarded.",
            },
            {
                "id": "b",
                "text": "The /30 connected route (C) is matched and the packet is forwarded out G0/0",
                "correct": False,
                "rationale": "Incorrect. While the /30 also contains .1, the /32 is more specific. The /32 match causes the router to accept the packet for local processing, not forward it.",
            },
            {
                "id": "c",
                "text": "The default route (S*) is used because 10.1.1.1 is not a routable destination",
                "correct": False,
                "rationale": "Incorrect. The default is used only when no more specific match exists. Both the /30 and /32 match; the /32 wins by LPM.",
            },
            {
                "id": "d",
                "text": "The packet is dropped because a host-route and a network-route cannot coexist for the same address",
                "correct": False,
                "rationale": "Incorrect. /32 (L) and /30 (C) coexist in the table; IOS installs both automatically for every configured interface. They do not conflict.",
            },
        ],
        "explanation": (
            "A local /32 route (L) represents the router's own interface IP. "
            "When traffic is addressed to the router itself, the /32 is the longest-matching route and the packet is handled locally. "
            "This is how the router distinguishes 'traffic for me' from 'traffic I forward'."
        ),
    },
    {
        "id": "cd3v3-036",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Routing table components",
        "stem": (
            "On a Cisco router, what is the administrative distance of a route that is directly connected "
            "(interface up, IP configured)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "0 — directly connected routes are considered completely trustworthy",
                "correct": True,
                "rationale": "Correct. A connected route has AD 0, the best possible value. The router verifies the link directly, so no external trust is needed. A route with AD 0 is never displaced by any other source.",
            },
            {
                "id": "b",
                "text": "1 — same as a static route",
                "correct": False,
                "rationale": "Incorrect. Static routes have AD 1; directly connected routes have AD 0, making them even more preferred than statics.",
            },
            {
                "id": "c",
                "text": "90 — same as EIGRP internal",
                "correct": False,
                "rationale": "Incorrect. EIGRP internal is AD 90. Directly connected routes bypass all routing-protocol trust levels with AD 0.",
            },
            {
                "id": "d",
                "text": "Connected routes have no administrative distance",
                "correct": False,
                "rationale": "Incorrect. All routes have an AD in IOS. Connected routes have AD 0 explicitly, which is why they are always the most preferred for any prefix they match.",
            },
        ],
        "explanation": (
            "AD scale (lower = more preferred): Connected 0, Static 1, eBGP 20, EIGRP internal 90, OSPF 110, IS-IS 115, RIP 120, EIGRP external 170, iBGP 200, unusable 255. "
            "Connected (AD 0) is always the most preferred source."
        ),
    },
    {
        "id": "cd3v3-037",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Static routing",
        "stem": (
            "An engineer wants to verify that a newly added static route is in the routing table and active. "
            "Which command most directly shows this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "show ip route static",
                "correct": True,
                "rationale": "Correct. 'show ip route static' filters the routing table to display only static routes, showing all currently installed static routes with their AD, metric, and next-hop.",
            },
            {
                "id": "b",
                "text": "show running-config | include ip route",
                "correct": False,
                "rationale": "Incorrect. This shows the static route configuration, but a route can be configured yet not installed (e.g., if the next-hop is unreachable or AD is 255). The routing table (not running-config) confirms a route is actually active.",
            },
            {
                "id": "c",
                "text": "show ip interface brief",
                "correct": False,
                "rationale": "Incorrect. 'show ip interface brief' shows interface status and IP addresses, not the routing table entries.",
            },
            {
                "id": "d",
                "text": "debug ip routing",
                "correct": False,
                "rationale": "Incorrect. 'debug ip routing' shows routing table changes in real time and is not appropriate for simply verifying a static route is currently installed; it produces excessive output in production.",
            },
        ],
        "explanation": (
            "To verify installed static routes: 'show ip route static' shows only static entries from the active routing table. "
            "Always verify in the routing table (not running-config) because a configured static route may not install if the next-hop is unreachable."
        ),
    },
    {
        "id": "cd3v3-038",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "OSPF DR/BDR election",
        "stem": (
            "An engineer wants to ensure Router R1 NEVER becomes the DR or BDR on any OSPF broadcast segment "
            "without disabling OSPF on R1's interfaces. Which command on R1 achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ip ospf priority 0 (configured on each OSPF-enabled interface of R1)",
                "correct": True,
                "rationale": "Correct. Setting OSPF interface priority to 0 permanently disqualifies the router from becoming DR or BDR on that segment. The router still forms adjacencies and participates in OSPF; it just never wins DR/BDR election.",
            },
            {
                "id": "b",
                "text": "ospf dr none (under router ospf)",
                "correct": False,
                "rationale": "Incorrect. 'ospf dr none' is not a valid IOS command. DR exclusion is done with 'ip ospf priority 0' per-interface.",
            },
            {
                "id": "c",
                "text": "passive-interface default (under router ospf)",
                "correct": False,
                "rationale": "Incorrect. 'passive-interface default' suppresses hellos on all interfaces, which prevents adjacency formation entirely — far more than just excluding DR eligibility.",
            },
            {
                "id": "d",
                "text": "router-id 0.0.0.0 (forces the lowest RID and loses all elections)",
                "correct": False,
                "rationale": "Incorrect. RID 0.0.0.0 is not a valid OSPF router-id. Even if it were, DR election uses priority first; only when priorities are equal does RID break ties — a priority-5 router with RID 0.0.0.0 could still become DR over a priority-1 router.",
            },
        ],
        "explanation": (
            "'ip ospf priority 0' on an interface removes that router from DR/BDR candidacy on the connected segment. "
            "It still forms FULL adjacencies with the DR/BDR and participates in OSPF normally — just as a DROTHER."
        ),
    },
    {
        "id": "cd3v3-039",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 static routing",
        "stem": (
            "R1 has IPv6 enabled and 'ipv6 unicast-routing' configured. An engineer adds:\n"
            "  ipv6 route 2001:db8::/32 Null0\n\n"
            "What is the purpose of this route?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is a summary discard route — any packet matching 2001:db8::/32 but not a more specific route is dropped at Null0, preventing routing loops from a less specific default",
                "correct": True,
                "rationale": "Correct. Pointing a summary route to Null0 is a common practice when summarizing address blocks. More specific routes within the block are forwarded normally; traffic that matches only the summary (no more-specific route) hits Null0 and is discarded, preventing it from matching a default route and looping.",
            },
            {
                "id": "b",
                "text": "It disables IPv6 routing for all 2001:db8:: addresses",
                "correct": False,
                "rationale": "Incorrect. More specific routes within 2001:db8::/32 still work normally via LPM. Only traffic that has NO more specific match falls to this Null0 route.",
            },
            {
                "id": "c",
                "text": "It creates a default IPv6 route, because /32 is the IPv6 default prefix",
                "correct": False,
                "rationale": "Incorrect. The IPv6 default route prefix is ::/0 (all zeros, prefix length 0), not /32. A 2001:db8::/32 route is a specific summary, not the default.",
            },
            {
                "id": "d",
                "text": "It causes all IPv6 traffic to loop through the router infinitely",
                "correct": False,
                "rationale": "Incorrect. Null0 immediately discards matching packets (without an ICMP reply unless configured otherwise). No looping occurs; traffic is silently dropped.",
            },
        ],
        "explanation": (
            "A Null0 static route (also called a discard or black-hole route) prevents routing loops when summarizing prefixes. "
            "More-specific routes within the summary forward normally via LPM. "
            "Only traffic matching the summary but no more-specific route is dropped at Null0."
        ),
    },
    {
        "id": "cd3v3-040",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Forwarding decision & longest prefix match",
        "stem": (
            "A router's table contains:\n"
            "  S    10.0.0.0/8    [1/0]  via 10.99.0.1\n"
            "  O    10.1.0.0/16   [110/5] via 10.99.0.2\n"
            "  D    10.1.1.0/24   [90/3]  via 10.99.0.3\n"
            "  S*   0.0.0.0/0    [1/0]  via 10.99.0.9\n\n"
            "Which TWO statements are TRUE about forwarding a packet to 10.1.1.50? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The packet is forwarded via 10.99.0.3 because the EIGRP /24 route is the longest prefix match",
                "correct": True,
                "rationale": "Correct. 10.1.1.50 is in 10.1.1.0/24, 10.1.0.0/16, 10.0.0.0/8, and 0.0.0.0/0. The /24 is the longest (most specific) match, so the EIGRP route via 10.99.0.3 is selected regardless of AD.",
            },
            {
                "id": "b",
                "text": "The static /8 route (AD 1) is NOT used despite its lower AD because the /24 is a longer prefix match",
                "correct": True,
                "rationale": "Correct. AD is only compared between routes of identical prefix length. The /8 and /24 are different lengths; the /24 wins by LPM before AD is ever considered.",
            },
            {
                "id": "c",
                "text": "The packet is forwarded via 10.99.0.1 because the static route has the lowest AD of 1",
                "correct": False,
                "rationale": "Incorrect. AD does not override prefix-length specificity. The /8 (AD 1) loses to the /24 (AD 90) because longest-prefix-match is applied first.",
            },
            {
                "id": "d",
                "text": "The default route via 10.99.0.9 is used as a tiebreaker when multiple routes match",
                "correct": False,
                "rationale": "Incorrect. The default route is only used when NO more specific route matches. Multiple specific routes exist here; the most specific (/24) is used and the default is irrelevant.",
            },
        ],
        "explanation": (
            "For 10.1.1.50: four routes match (/24, /16, /8, /0). LPM selects the /24. "
            "AD is not consulted across different prefix lengths — the /24 wins regardless of its AD (90) vs the /8's AD (1). "
            "The default route (0.0.0.0/0) is never used when more-specific routes exist."
        ),
    },
]
