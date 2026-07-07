"""
Cisco CCNA 200-301 — Domain 6: Automation and Programmability
Question bank v3b (20 questions).
"""

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # 6.1  Automation impact
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-001",
        "domain": 6,
        "objective": "6.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation impact",
        "stem": (
            "A service provider uses Python scripts to automatically provision "
            "new customer VRFs on 80 PE routers simultaneously. Before "
            "automation, a single engineer took three hours to manually "
            "configure each VRF per customer request, one router at a time. "
            "After automation, all 80 routers are provisioned in under four "
            "minutes. A senior architect argues the MOST important operational "
            "improvement is NOT the speed gain. Which benefit does the "
            "architect MOST likely mean?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The scripts eliminate all BGP routing errors because "
                    "automation fixes protocol-level convergence issues."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation scripts configure devices but do not "
                    "alter BGP protocol behavior or fix convergence issues caused "
                    "by topology or timer misconfiguration."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Every router receives an identical, validated VRF "
                    "configuration derived from the same template, preventing "
                    "the subtle per-device mismatches that accumulate with "
                    "manual work and cause hard-to-diagnose service outages."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Configuration consistency is the deeper operational "
                    "value: when 80 routers are configured by the same script "
                    "from the same validated template, subtle differences — wrong "
                    "route-distinguisher, missing export community — that human "
                    "operators introduce when copy-pasting are eliminated. These "
                    "mismatches are a leading cause of customer-facing incidents."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Automation permanently prevents any human from modifying "
                    "VRF configurations via CLI after they are created."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation tools configure devices but do not "
                    "inherently lock out CLI access. Preventing manual CLI "
                    "changes requires separate AAA policy enforcement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The script reduces bandwidth consumption on the management "
                    "network compared to individual SSH sessions."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While scripted SSH sessions may be slightly more "
                    "efficient than interactive sessions, management bandwidth "
                    "is not a meaningful operational benefit compared to "
                    "consistency and error reduction."
                ),
            },
        ],
        "explanation": (
            "Beyond speed, automation's primary operational benefit is "
            "consistency and correctness: every device receives the exact same "
            "configuration from a single validated source of truth. This "
            "eliminates configuration drift, copy-paste errors, and the "
            "subtle per-device variation that accumulates in large manual "
            "environments. Consistency is harder to quantify than speed but "
            "more impactful for long-term reliability."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.2  Traditional vs controller-based
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-002",
        "domain": 6,
        "objective": "6.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Traditional vs controller-based",
        "stem": (
            "A financial institution runs a traditional campus network where "
            "every switch has its own independent Spanning Tree and HSRP "
            "configuration managed via CLI. The CISO wants a solution that "
            "provides a single pane of glass to enforce security group "
            "microsegmentation policy across all switches without writing "
            "per-device ACLs. Which architectural model BEST addresses "
            "this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Continue with traditional CLI management but add a "
                    "RADIUS server to centralize authentication for each "
                    "SSH login."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Centralizing SSH authentication does not "
                    "provide microsegmentation policy management. Per-device "
                    "ACLs would still need to be written and deployed "
                    "manually on each switch."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy a controller-based architecture (e.g., Cisco "
                    "SD-Access with DNA Center) that centralizes policy "
                    "definition and automatically translates security group "
                    "policies into device-specific configurations via "
                    "southbound APIs."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Controller-based architectures like SD-Access "
                    "with DNA Center allow administrators to define security "
                    "group-based policy once in the controller, which "
                    "automatically generates and pushes the corresponding "
                    "configuration to all devices — eliminating the need for "
                    "per-device ACL management."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Upgrade all switches to the latest IOS version, which "
                    "includes a built-in microsegmentation agent."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IOS software upgrades provide new features "
                    "but do not provide a single pane of glass for centralized "
                    "policy definition and deployment. Each device would still "
                    "require individual configuration."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Replace all switches with firewalls that enforce "
                    "microsegmentation at every port."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Replacing all switches with firewalls is "
                    "architecturally impractical and does not address the "
                    "single-pane-of-glass policy management requirement. "
                    "Each firewall would still require individual policy "
                    "configuration."
                ),
            },
        ],
        "explanation": (
            "The fundamental advantage of controller-based over traditional "
            "networking is policy abstraction and central enforcement: intent "
            "is defined once and the controller translates it into device-level "
            "configuration. For microsegmentation (security group tagging and "
            "policy), SD-Access with DNA Center is specifically designed to "
            "replace thousands of per-device ACLs with group-based policy "
            "managed from a single interface."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.3  SDN architecture — control/data plane
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-003",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN architecture (control/data plane)",
        "stem": (
            "In a traditional three-tier campus network, a core switch "
            "runs OSPF and builds its own routing table autonomously. In "
            "an SDN architecture, an equivalent core switch has its OSPF "
            "process removed and instead receives forwarding entries "
            "programmed by a centralized controller. Which statement "
            "CORRECTLY describes the impact on the switch's planes?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The switch loses both its control plane and data plane; "
                    "all forwarding is now handled by the controller."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In SDN the data plane (actual packet "
                    "forwarding based on programmed entries) remains on the "
                    "network device. Only the control plane logic is moved "
                    "to the controller."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The switch retains its data plane (packet forwarding "
                    "using controller-programmed FIB/flow entries) but "
                    "relinquishes its autonomous control plane (route "
                    "calculation), which now resides in the SDN controller."
                ),
                "correct": True,
                "rationale": (
                    "Correct. SDN decouples control from forwarding: the "
                    "control plane (routing decisions, topology calculation) "
                    "moves to the controller. The data plane (forwarding "
                    "packets at line rate based on installed entries) stays "
                    "on the switch hardware. This is the defining SDN "
                    "architectural change."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The switch retains both control and data planes, but "
                    "the controller provides a backup control plane that "
                    "activates only during failures."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In a pure SDN model the device's control "
                    "plane is removed entirely and delegated to the "
                    "controller, not retained as primary with a controller "
                    "backup."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The switch loses its data plane; the management plane "
                    "is enhanced to handle all packet forwarding."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The management plane (SNMP, SSH, logging) "
                    "is a separate function for device configuration and "
                    "monitoring. SDN does not relocate data-plane forwarding "
                    "to the management plane."
                ),
            },
        ],
        "explanation": (
            "SDN architecture separates the three planes: "
            "Control plane (routing decisions, topology) → centralized in "
            "the SDN controller. "
            "Data plane (packet forwarding based on FIB/flow tables) → "
            "remains distributed on network devices. "
            "Management plane (SSH, SNMP, logging) → remains on devices. "
            "The controller programs the data plane via southbound APIs "
            "(OpenFlow flow-mods, NETCONF, etc.)."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.3  SDN architecture — overlay/underlay/fabric
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-004",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SDN architecture (overlay/underlay/fabric)",
        "stem": (
            "A network architect is designing a new data center fabric using "
            "VXLAN BGP EVPN. The physical spine-leaf switches use IS-IS for "
            "IP reachability between loopback addresses. Tenant virtual "
            "machines communicate through VXLAN-encapsulated frames that "
            "traverse the physical network. An intern asks: 'If the IS-IS "
            "underlay goes down between two leaf nodes, what happens to the "
            "VXLAN overlay traffic between tenants on those leaves?' "
            "Which answer is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The VXLAN overlay continues to forward tenant traffic "
                    "because the overlay is independent of the underlay."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The overlay is dependent on the underlay for "
                    "IP reachability between tunnel endpoints (VTEPs). If "
                    "IS-IS loses the path between two leaf loopbacks, the "
                    "VXLAN tunnel between those VTEPs loses its transport "
                    "path and overlay traffic is disrupted."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The VXLAN overlay traffic between tenants on those two "
                    "leaf nodes is also disrupted because VXLAN tunnels rely "
                    "on the underlay IP reachability between VTEP loopbacks "
                    "to transport encapsulated frames."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The overlay depends on the underlay: VXLAN "
                    "encapsulates frames in UDP/IP packets destined for the "
                    "remote VTEP's IP address (loopback). If IS-IS cannot "
                    "provide a path between the VTEP IPs, the VXLAN tunnel "
                    "has no transport and overlay traffic fails. The overlay "
                    "abstracts the topology but is not independent of it."
                ),
            },
            {
                "id": "c",
                "text": (
                    "VXLAN automatically reroutes the overlay traffic using "
                    "LISP mapping lookups when the primary underlay path fails."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. LISP is used in SD-Access as the overlay "
                    "control plane for endpoint mapping, not as a failover "
                    "mechanism for VXLAN BGP EVPN data-center fabrics. "
                    "Rerouting is handled by IS-IS convergence in the "
                    "underlay, not LISP."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The BGP EVPN control plane reroutes tenant traffic "
                    "through the management network when the underlay fails."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. BGP EVPN is the overlay control plane for "
                    "MAC/IP advertisement; it does not reroute traffic through "
                    "the management network. Management and data planes are "
                    "separate, and the management network is not a data "
                    "forwarding path."
                ),
            },
        ],
        "explanation": (
            "Overlay/underlay dependency: the overlay (VXLAN) provides "
            "logical abstraction but is carried by the underlay (IS-IS/OSPF "
            "routed IP fabric). VXLAN packets are outer-IP/UDP encapsulated "
            "to VTEP loopback addresses — if IS-IS cannot route between those "
            "loopbacks, no outer-IP path exists and the VXLAN tunnel drops. "
            "The underlay must be resilient (ECMP, fast IS-IS timers) to "
            "minimize overlay impact during failures."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.3  Northbound/southbound APIs
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-005",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Northbound/southbound APIs",
        "stem": (
            "Two Cisco DNA Center clusters, one managing the campus network "
            "and one managing the data center, must share topology and "
            "policy information to coordinate end-to-end path computation. "
            "Which SDN interface type describes communication BETWEEN "
            "these two controllers?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Northbound interface — because the campus controller "
                    "is above the data center controller in the hierarchy."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Northbound interfaces connect a controller "
                    "to applications or orchestration systems above it. Two "
                    "peer controllers at the same level communicate via "
                    "east/westbound interfaces."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Southbound interface — because controllers communicate "
                    "with each other using device-programming protocols "
                    "like NETCONF."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Southbound interfaces connect a controller "
                    "downward to network devices. Controller-to-controller "
                    "communication at the same tier is the east/westbound "
                    "interface."
                ),
            },
            {
                "id": "c",
                "text": (
                    "East/westbound interface — because this describes "
                    "horizontal communication between peer controllers "
                    "at the same architectural level."
                ),
                "correct": True,
                "rationale": (
                    "Correct. East/westbound interfaces (also called "
                    "lateral or inter-controller interfaces) describe "
                    "communication between peer SDN controllers. When two "
                    "controllers of equal standing share state, policy, or "
                    "topology, they use east/westbound APIs. This is distinct "
                    "from northbound (controller to application) and "
                    "southbound (controller to device)."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Management plane interface — because DNS Center uses "
                    "SNMP to exchange topology data with peer controllers."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'Management plane interface' is not the "
                    "standard SDN term for inter-controller communication, "
                    "and DNA Center does not use SNMP for controller-to-"
                    "controller topology exchange."
                ),
            },
        ],
        "explanation": (
            "SDN interface summary: "
            "NBI (northbound) = controller ↑ applications/orchestrators. "
            "SBI (southbound) = controller ↓ network devices. "
            "East/westbound = controller ↔ peer controllers (horizontal). "
            "When two controllers at the same layer need to share state, "
            "routes, or policies, the east/westbound interface is used. "
            "Examples: BGP-LS between controllers, proprietary REST APIs "
            "between controller clusters."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.4  Cisco DNA Center
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-006",
        "domain": 6,
        "objective": "6.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cisco DNA Center",
        "stem": (
            "After deploying Cisco DNA Center, a network engineer notices "
            "that the assurance dashboard shows a Catalyst 9200 switch with "
            "a 'Fair' health score, flagging high CPU utilization and "
            "multiple interface errors. Without DNA Center, how would the "
            "engineer typically have discovered these issues?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The issues would have been reported automatically by "
                    "the switch via OSPF LSA flooding to all routers in "
                    "the network."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OSPF LSA flooding conveys topology and "
                    "reachability information, not device health metrics "
                    "like CPU utilization or interface error counters."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The engineer would have had to manually SSH to each "
                    "switch and run 'show processes cpu' and 'show interfaces' "
                    "commands, or rely on users reporting symptoms — detecting "
                    "the problem reactively rather than proactively."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Without a controller's assurance plane, "
                    "identifying health issues requires either reactive "
                    "response (user complaints) or periodic manual "
                    "CLI checks on individual devices. DNA Center's "
                    "continuous telemetry collection and scoring surface "
                    "problems proactively that would otherwise go undetected "
                    "until they cause outages."
                ),
            },
            {
                "id": "c",
                "text": (
                    "STP topology change notifications (TCNs) would have "
                    "alerted the NMS to the high CPU and interface errors."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. STP TCNs notify of topology changes (port "
                    "state transitions), not CPU or interface error conditions. "
                    "Different mechanisms collect different types of device "
                    "health data."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The switch would have automatically emailed the "
                    "network team using its built-in alert engine."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco Catalyst switches do not have a built-in "
                    "email alert engine for health thresholds. Syslog and SNMP "
                    "traps can alert on specific events if configured, but "
                    "the proactive health scoring and assurance view requires "
                    "a platform like DNA Center."
                ),
            },
        ],
        "explanation": (
            "Cisco DNA Center Network Assurance continuously collects "
            "telemetry (streaming, SNMP, syslog) from all managed devices, "
            "correlates it, and produces device and client health scores. "
            "This proactive visibility replaces reactive, per-device CLI "
            "investigation. Without it, engineers detect problems only when "
            "users report issues or during scheduled manual audits — hours "
            "or days after problems begin."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.5  REST APIs — CRUD/HTTP verbs
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-007",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A network automation script successfully creates a prefix-list "
            "object on a controller using POST. The script is later updated "
            "to add three new permit entries to the SAME prefix-list object "
            "while keeping all existing entries intact. The prefix-list URI "
            "is /api/v1/prefix-lists/PL-CORP. Which HTTP method should the "
            "updated script use, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "POST to /api/v1/prefix-lists/PL-CORP, because POST "
                    "is always used when sending data to the server."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. POST to an existing resource URI creates "
                    "a subordinate resource or may result in a duplicate "
                    "or error. POST is for creating new resources, not "
                    "modifying existing ones. It would not 'add entries' "
                    "to an existing prefix-list."
                ),
            },
            {
                "id": "b",
                "text": (
                    "PUT to /api/v1/prefix-lists/PL-CORP with the complete "
                    "updated prefix-list (all old entries plus three new ones) "
                    "in the body, because PUT replaces the entire resource."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. PUT would work if the script sends the "
                    "full updated list, but the question says 'add three "
                    "new entries while keeping existing entries intact' — "
                    "implying a partial update. PATCH is the correct choice "
                    "for partial modification without requiring the full "
                    "resource representation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "PATCH to /api/v1/prefix-lists/PL-CORP with only the "
                    "three new permit entries in the body, because PATCH "
                    "applies a partial modification to the existing resource "
                    "without replacing the entire object."
                ),
                "correct": True,
                "rationale": (
                    "Correct. PATCH is designed for partial updates: the "
                    "client sends only the fields or entries to add/change, "
                    "and the server merges them with the existing resource. "
                    "This preserves the existing prefix-list entries while "
                    "adding the new ones, without requiring the client to "
                    "retrieve and re-send the entire list."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DELETE /api/v1/prefix-lists/PL-CORP followed by POST "
                    "with the full updated prefix-list, to ensure all entries "
                    "are applied consistently."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DELETE + POST is a two-step, non-atomic "
                    "operation that briefly removes the prefix-list, "
                    "potentially impacting routing policy between the two "
                    "operations. PATCH achieves the same result atomically "
                    "without any service disruption."
                ),
            },
        ],
        "explanation": (
            "HTTP method selection: "
            "POST = create a new resource (response 201). "
            "PUT = replace entire resource (idempotent). "
            "PATCH = partial update, merge changes with existing resource. "
            "DELETE = remove resource. "
            "When the requirement is 'add to existing without replacing,' "
            "PATCH is the correct answer. The key differentiator from PUT "
            "is that PATCH does not require the complete resource "
            "representation — only the delta."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.5  REST APIs — HTTP status codes
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-008",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A Python script calls a controller REST API to retrieve "
            "interface statistics:\n\n"
            "    GET /api/v2/devices/R1/interfaces/Gi0/0/stats\n"
            "    X-Auth-Token: valid_token_here\n\n"
            "The API returns HTTP 404. A junior engineer suggests the token "
            "has expired. The senior engineer disagrees. Which response "
            "BEST explains the senior engineer's position?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The senior engineer is wrong — HTTP 404 is always "
                    "caused by an expired or revoked authentication token."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An expired or invalid token returns HTTP "
                    "401 Unauthorized. HTTP 404 specifically means the "
                    "server could not find a resource at the requested URI, "
                    "which is unrelated to token validity."
                ),
            },
            {
                "id": "b",
                "text": (
                    "HTTP 404 Not Found means the server could not locate "
                    "the resource — either device R1 is not in the "
                    "controller's inventory, interface Gi0/0 does not exist, "
                    "or the URI path is incorrect. The fix is to verify the "
                    "device name, interface ID, and URI path — not to "
                    "re-authenticate."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 404 is a client-side error meaning 'resource "
                    "not found at this URI.' Possible causes: wrong device ID "
                    "(R1 not onboarded in controller), wrong interface format "
                    "(Gi0/0 vs GigabitEthernet0/0), or URI typo. An expired "
                    "token would return 401. The senior engineer is correct "
                    "that re-authentication will not resolve a 404."
                ),
            },
            {
                "id": "c",
                "text": (
                    "HTTP 404 means the server is temporarily overloaded; "
                    "the script should wait and retry automatically."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Server overload returns HTTP 503 Service "
                    "Unavailable or 429 Too Many Requests. HTTP 404 is "
                    "a permanent client-side error for a missing resource, "
                    "not a transient server load issue."
                ),
            },
            {
                "id": "d",
                "text": (
                    "HTTP 404 means the client lacks write permission for "
                    "the statistics endpoint; the fix is to request admin "
                    "privileges."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Permission issues return HTTP 403 Forbidden. "
                    "HTTP 404 means the resource was not found, regardless "
                    "of the user's privilege level."
                ),
            },
        ],
        "explanation": (
            "REST HTTP status code reference: "
            "200 OK — success (GET/PUT/PATCH/DELETE with body). "
            "201 Created — resource created (POST). "
            "204 No Content — success, no body (DELETE/PUT/PATCH). "
            "400 Bad Request — malformed request syntax or invalid data. "
            "401 Unauthorized — missing or invalid authentication. "
            "403 Forbidden — authenticated but lacks permission. "
            "404 Not Found — resource does not exist at URI. "
            "500 Internal Server Error — server-side failure. "
            "Distinguishing 401/403/404 is a common exam question."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.5  REST APIs — statelessness/data encoding
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-009",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (statelessness/data encoding)",
        "stem": (
            "A network automation platform makes 500 concurrent REST API "
            "calls to a controller cluster with three load-balanced nodes. "
            "Each API call includes an X-Auth-Token header. A developer "
            "asks why the application must include the token in every "
            "single request rather than relying on the cluster to remember "
            "the session after the first authenticated call. Which REST "
            "property BEST explains the requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Uniform interface — every resource must be accessed "
                    "through a consistent URI structure."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The uniform interface constraint defines how "
                    "resources are identified and manipulated via URIs and "
                    "standard methods, not why each request must carry auth "
                    "credentials independently."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Statelessness — because each REST request must be "
                    "self-contained with all context needed for the server "
                    "to process it, no server node in the cluster stores "
                    "client session state between calls, so each call must "
                    "independently authenticate."
                ),
                "correct": True,
                "rationale": (
                    "Correct. REST statelessness requires every request to "
                    "be self-contained. In a load-balanced cluster, any node "
                    "may handle any request; if session state were required, "
                    "the client would need affinity to a single node. By "
                    "including the token in every request, any cluster node "
                    "can independently validate it — this is exactly why "
                    "statelessness is a REST architectural requirement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Cacheability — the token header ensures that responses "
                    "are properly cached by intermediary proxies."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cacheability is a separate REST constraint "
                    "governing whether responses may be cached. The token "
                    "in every request is a consequence of statelessness, "
                    "not cacheability."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Layered system — the cluster uses multiple network "
                    "layers, so each layer needs its own authentication."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The layered system REST constraint allows "
                    "intermediaries (proxies, gateways) between client and "
                    "server. It does not explain why each HTTP request must "
                    "carry authentication credentials."
                ),
            },
        ],
        "explanation": (
            "REST statelessness is the architectural constraint that makes "
            "horizontal scaling possible: no server-side session means any "
            "cluster node can process any request without needing prior "
            "context. The client carries all state (token, resource ID, "
            "request parameters) in every request. This is why JWT bearer "
            "tokens, API keys, or Basic Auth headers must be included in "
            "every REST call — the server treats each call as a brand-new, "
            "independent interaction."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.6  Configuration management — Ansible / Puppet / Chef
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-010",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "An Ansible control node runs a playbook targeting 200 Cisco "
            "IOS-XE switches in the inventory file. The playbook configures "
            "a standard set of SNMP community strings. After the playbook "
            "completes, an engineer manually removes the SNMP configuration "
            "from 10 of the switches via CLI. What happens the NEXT TIME "
            "the same Ansible playbook is executed?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ansible skips all 200 switches because it ran "
                    "successfully once and assumes nothing has changed."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible does not assume prior run results "
                    "are still valid. On each run it connects to each host "
                    "and checks current state against desired state."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Ansible detects that 10 switches are missing the SNMP "
                    "configuration, applies the desired state to those 10 "
                    "(reporting 'changed'), and reports 'ok' for the other "
                    "190 switches where the configuration is already present."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ansible's check-then-act pattern (idempotency) "
                    "means each task compares current device state to desired "
                    "state. On the 10 modified switches, SNMP strings are "
                    "missing, so Ansible applies them (task = 'changed'). "
                    "On the 190 unchanged switches, the state matches, so "
                    "no action is taken (task = 'ok'). This is exactly the "
                    "configuration drift remediation capability of Ansible."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Ansible re-applies the SNMP configuration to all 200 "
                    "switches regardless of their current state, duplicating "
                    "the community strings on the 190 already-configured "
                    "switches."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible IOS modules check existing state "
                    "before applying changes. If the desired SNMP community "
                    "is already present, the task reports 'ok' and does "
                    "not duplicate entries."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ansible fails with an error because the inventory now "
                    "differs from the last-run state stored in the "
                    "Ansible database."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible does not maintain a persistent "
                    "database of previous device states between runs. Each "
                    "run independently connects to devices and checks current "
                    "state in real time."
                ),
            },
        ],
        "explanation": (
            "Ansible's drift remediation in practice: each playbook run "
            "connects to every host in inventory, checks current state, "
            "and applies only the changes needed to reach desired state. "
            "Hosts with correct config → 'ok'. Hosts drifted from desired "
            "state → 'changed' (correction applied). This is idempotent "
            "operation and desired-state enforcement — the two most "
            "operationally important Ansible properties for network "
            "management at scale."
        ),
    },
    {
        "id": "cd6v3b-011",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "A network automation team is comparing Ansible, Puppet, and "
            "Chef for managing Cisco IOS-XE routers. They specifically need "
            "a tool where the MANAGED DEVICE initiates the configuration "
            "check-in process — not the management server. Which tool and "
            "model matches this requirement, and what is the agent component "
            "on the managed device called?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ansible — the Ansible agent on each router polls the "
                    "Ansible Tower server every 30 minutes for new playbooks."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible is agentless — there is no Ansible "
                    "agent on managed devices. Even with Ansible Tower/AWX, "
                    "the Tower server pushes jobs to a remote execution "
                    "node; managed devices do not poll."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Puppet — the Puppet agent on each managed device "
                    "periodically initiates a connection to the Puppet "
                    "master, requests its catalog, and enforces the "
                    "desired state locally."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Puppet uses a pull model: the Puppet agent "
                    "(installed on each managed node) initiates a TLS "
                    "connection to the Puppet master on a schedule (default "
                    "every 30 minutes), authenticates with a certificate, "
                    "requests its compiled catalog, and runs the resources "
                    "locally. This is device-initiated check-in."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Chef — the Chef server pushes run-lists to a Chef "
                    "push-job agent on each router, which then executes "
                    "the cookbook locally."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Chef's primary model is also pull-based "
                    "(chef-client on node pulls from Chef server), but the "
                    "question asks specifically which tool uses device-"
                    "initiated check-in with an agent. Both Puppet and Chef "
                    "fit, but Puppet is the canonical CCNA answer. The Chef "
                    "push-job model described is a specific add-on, not the "
                    "primary architecture."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ansible — the Ansible callback plugin on each router "
                    "calls back to the Ansible control node to pull its "
                    "configuration task list."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible callback plugins are output hooks "
                    "on the control node (for logging, notifications), not "
                    "agents on managed devices. Ansible remains agentless "
                    "and push-based."
                ),
            },
        ],
        "explanation": (
            "Push vs. pull for CCNA: "
            "Ansible = agentless, push (control node initiates). "
            "Puppet = agent-based, pull (Puppet agent on node initiates "
            "check-in with master every ~30 min, default). "
            "Chef = agent-based (chef-client), pull (client initiates "
            "check-in with Chef server). "
            "When the requirement is 'device initiates the check-in,' "
            "Puppet (or Chef) with their pull model is the answer. "
            "The agent component is called the 'Puppet agent' in Puppet."
        ),
    },
    {
        "id": "cd6v3b-012",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "A DevOps engineer writes an Ansible playbook that uses the "
            "cisco.ios.ios_config module to push interface descriptions "
            "to 50 routers. The playbook runs without errors but the "
            "engineer notices the task reports 'changed' on every router "
            "on every run, even after the first successful run. Which "
            "explanation BEST accounts for this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ansible always reports 'changed' for network device "
                    "tasks because network modules cannot check device state."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Many Ansible network modules (including "
                    "cisco.ios.ios_config with check_running option) can "
                    "compare desired vs. current state. Consistently "
                    "reporting 'changed' usually indicates a specific "
                    "configuration or module parameter issue."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The ios_config module is likely being used without "
                    "the 'save_when' or comparison parameters, causing it "
                    "to push changes without checking if they already exist "
                    "— or the descriptions include dynamic content (e.g., "
                    "timestamps) that differs on each run."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ansible's ios_config module behavior depends "
                    "on how it is invoked. If used in a way that does not "
                    "compare existing running config to desired config "
                    "(or if the config contains dynamic values like "
                    "timestamps), the module may report 'changed' on every "
                    "run. True idempotency requires the module to detect "
                    "that the current state already matches — which may "
                    "require proper use of 'lines' vs 'src', or the "
                    "match parameter."
                ),
            },
            {
                "id": "c",
                "text": (
                    "This is expected behavior — Ansible is designed to "
                    "always report 'changed' for configuration tasks as "
                    "a safety indicator."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible is designed to be idempotent and "
                    "report 'ok' when no change is needed. Consistently "
                    "reporting 'changed' on re-runs of the same playbook "
                    "indicates an idempotency issue that should be "
                    "investigated and fixed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The routers are reverting the descriptions after each "
                    "Ansible run because OSPF LSA updates overwrite "
                    "interface descriptions."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OSPF does not modify interface descriptions. "
                    "Interface descriptions are local configuration stored "
                    "in running-config, not affected by routing protocol "
                    "operations."
                ),
            },
        ],
        "explanation": (
            "Ansible idempotency for Cisco IOS requires careful module "
            "usage. The cisco.ios.ios_config module supports state "
            "comparison but must be used correctly. If the module cannot "
            "detect that the config is already present (e.g., using raw "
            "config blocks without running-config comparison, or dynamic "
            "values in the config), it will always push and report 'changed.' "
            "Best practice: use higher-level resource modules (ios_interfaces, "
            "etc.) which are inherently idempotent, rather than raw "
            "ios_config where possible."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.7  JSON data format
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-013",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "JSON data format",
        "stem": (
            "A Python script receives the following JSON string from a "
            "REST API and attempts to parse it with json.loads():\n\n"
            "    {\n"
            "        'hostname': 'SW2',\n"
            "        'vlan_id': 20,\n"
            "        'active': True\n"
            "    }\n\n"
            "The script raises a json.JSONDecodeError. What are the TWO "
            "JSON syntax violations in this string?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The keys use single quotes instead of double quotes, "
                    "and 'True' is capitalized (Python boolean) instead "
                    "of lowercase 'true' (JSON boolean)."
                ),
                "correct": True,
                "rationale": (
                    "Correct. JSON requires double quotes for all strings "
                    "(keys and string values). Single-quoted keys/values "
                    "are JavaScript-style object literals, not valid JSON. "
                    "Additionally, JSON booleans must be lowercase 'true' "
                    "or 'false'; Python's capitalized 'True'/'False' are "
                    "not valid JSON and will cause a JSONDecodeError."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The vlan_id value is a number instead of a string, "
                    "and the object is missing a trailing comma after "
                    "the last key-value pair."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON fully supports unquoted numbers — "
                    "20 is a valid JSON number value. Trailing commas are "
                    "NOT required (and are actually invalid in strict JSON). "
                    "Neither of these is the cause of the decode error."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The object has no 'type' key identifying the data "
                    "schema, and 'active' should be a string 'yes' or 'no' "
                    "instead of a boolean."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON has no requirement for a 'type' or "
                    "schema key. Boolean values are valid JSON; the problem "
                    "is capitalization ('True' vs 'true'), not the use of "
                    "booleans."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The vlan_id value should be quoted as '\"20\"' because "
                    "JSON requires all values to be strings, and 'active' "
                    "should use null instead of True."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON does NOT require all values to be "
                    "strings; numbers, booleans, and null are all valid "
                    "JSON value types. The problem is the single-quote "
                    "and capitalized-boolean violations, not numeric values."
                ),
            },
        ],
        "explanation": (
            "Two classic JSON syntax traps when writing Python dicts "
            "as JSON: "
            "(1) Single quotes are Python string syntax — JSON requires "
            "double quotes for all keys and string values. "
            "(2) Python boolean literals are True/False (capital first "
            "letter) — JSON boolean literals are true/false (all "
            "lowercase). Similarly, Python None becomes JSON null. "
            "json.loads() will raise JSONDecodeError for either violation."
        ),
    },
    {
        "id": "cd6v3b-014",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "JSON data format",
        "stem": (
            "Examine the following JSON structure returned by a network "
            "controller API:\n\n"
            "    {\n"
            "        \"fabric\": {\n"
            "            \"sites\": [\n"
            "                {\"name\": \"HQ\", \"edge_count\": 4},\n"
            "                {\"name\": \"Branch1\", \"edge_count\": 2}\n"
            "            ],\n"
            "            \"version\": 3\n"
            "        }\n"
            "    }\n\n"
            "A Python script (after json.loads()) needs to retrieve the "
            "edge_count value for 'Branch1'. Which expression is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "data[\"fabric\"][\"sites\"][\"Branch1\"][\"edge_count\"]",
                "correct": False,
                "rationale": (
                    "Incorrect. 'sites' is a JSON array (Python list), "
                    "not a dictionary. Lists are indexed by integer position, "
                    "not by string keys. Accessing data[\"fabric\"][\"sites\"]"
                    "[\"Branch1\"] raises a TypeError."
                ),
            },
            {
                "id": "b",
                "text": "data[\"fabric\"][\"sites\"][1][\"edge_count\"]",
                "correct": True,
                "rationale": (
                    "Correct. After json.loads(), 'data[\"fabric\"]' is a "
                    "dict. 'data[\"fabric\"][\"sites\"]' is a list (0-indexed). "
                    "Branch1 is the second element → index 1. "
                    "'data[\"fabric\"][\"sites\"][1][\"edge_count\"]' returns 2."
                ),
            },
            {
                "id": "c",
                "text": "data.fabric.sites[1].edge_count",
                "correct": False,
                "rationale": (
                    "Incorrect. Python dicts returned by json.loads() do "
                    "not support dot-notation attribute access. Accessing "
                    "data.fabric raises AttributeError. Bracket notation "
                    "is required: data[\"fabric\"][\"sites\"][1][\"edge_count\"]."
                ),
            },
            {
                "id": "d",
                "text": "data[\"fabric\"][\"sites\"][2][\"edge_count\"]",
                "correct": False,
                "rationale": (
                    "Incorrect. Python (and JSON) lists are zero-indexed. "
                    "Index 0 = HQ, index 1 = Branch1. Index 2 does not "
                    "exist in this two-element list and would raise "
                    "an IndexError."
                ),
            },
        ],
        "explanation": (
            "JSON navigation in Python: objects become dicts (use string "
            "keys), arrays become lists (use integer indexes, zero-based). "
            "Nested access chains brackets: dict key → list index → dict "
            "key. Dot notation does NOT work for Python dicts from "
            "json.loads(). The trap options here test: string-key access "
            "on a list (TypeError), dot notation (AttributeError), and "
            "off-by-one index error (IndexError)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multiple-response questions (~3)
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3b-015",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "Select TWO statements that are TRUE about REST API design "
            "and HTTP methods as they apply to network automation."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A GET request is safe and idempotent — it retrieves "
                    "resource state without modifying it, and repeating "
                    "it produces the same result each time."
                ),
                "correct": True,
                "rationale": (
                    "Correct. GET is defined as both safe (no side effects "
                    "on server state) and idempotent (identical requests "
                    "return identical results). It is used for the Read "
                    "operation in CRUD."
                ),
            },
            {
                "id": "b",
                "text": (
                    "POST is idempotent because sending the same POST "
                    "request twice will always produce exactly one new "
                    "resource, not two."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. POST is NOT idempotent per RFC 7231. "
                    "Sending the same POST request twice typically creates "
                    "two separate resources (e.g., two VLAN entries with "
                    "the same data). This is a common exam misconception."
                ),
            },
            {
                "id": "c",
                "text": (
                    "DELETE is idempotent — deleting a resource that has "
                    "already been deleted results in HTTP 404, but the "
                    "final server state (resource absent) is the same as "
                    "after the first successful delete."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DELETE is idempotent by definition (RFC 7231): "
                    "the first DELETE removes the resource (returns 200/204); "
                    "a second DELETE finds nothing to remove (returns 404), "
                    "but the state of the server — resource is absent — is "
                    "identical. The effect is the same regardless of how "
                    "many times DELETE is called."
                ),
            },
            {
                "id": "d",
                "text": (
                    "PATCH is always safer than PUT for modifying resources "
                    "because PATCH cannot accidentally delete existing "
                    "fields, while PUT can."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While PATCH applies partial updates and "
                    "PUT replaces the entire resource, neither is inherently "
                    "'safer' in all contexts. PUT is appropriate when you "
                    "intentionally want to replace the full resource. PATCH "
                    "implementations vary — a poorly implemented PATCH could "
                    "also cause data loss. 'Safer' is context-dependent, "
                    "not a specification guarantee."
                ),
            },
        ],
        "explanation": (
            "HTTP idempotency/safety (RFC 7231): "
            "Safe AND idempotent: GET, HEAD. "
            "Idempotent but NOT safe: PUT, DELETE. "
            "Neither safe nor idempotent: POST, PATCH. "
            "DELETE is idempotent because the end-state (resource absent) "
            "is identical whether called once or ten times, even though "
            "subsequent calls return 404 instead of 200/204. POST is the "
            "classic non-idempotent method — each call may create a new "
            "resource."
        ),
    },
    {
        "id": "cd6v3b-016",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "Select TWO characteristics that differentiate Puppet from "
            "Ansible for network device configuration management."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Puppet requires an agent installed on each managed "
                    "device, whereas Ansible is agentless and connects "
                    "via SSH or APIs."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the fundamental architectural "
                    "difference: Puppet = agent-based (Puppet agent must "
                    "run on managed nodes). Ansible = agentless (no software "
                    "on managed devices; control node uses SSH/API)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Puppet uses a pull model where managed nodes initiate "
                    "check-ins with the Puppet master, whereas Ansible "
                    "uses a push model where the control node initiates "
                    "connections to managed devices."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Puppet = pull (agent on node polls master). "
                    "Ansible = push (control node initiates SSH to devices). "
                    "This push/pull distinction is a core CCNA exam topic."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both Puppet and Ansible use YAML-formatted playbooks "
                    "to describe desired configuration state."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible uses YAML playbooks. Puppet uses "
                    "its own declarative DSL in manifest files (.pp), "
                    "not YAML. Chef uses a Ruby-based DSL in cookbooks."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ansible can only manage Cisco devices, whereas Puppet "
                    "supports multi-vendor environments."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Both Ansible and Puppet support multi-vendor "
                    "environments. Ansible has modules for Cisco, Juniper, "
                    "Arista, and many other vendors. Ansible is not "
                    "Cisco-only."
                ),
            },
        ],
        "explanation": (
            "Puppet vs. Ansible for CCNA: "
            "Puppet: agent-based, pull model, Puppet DSL manifests, "
            "TLS/certificate authentication, suitable for large-scale "
            "compliance enforcement where nodes check in on schedule. "
            "Ansible: agentless, push model, YAML playbooks, SSH-based, "
            "simpler to deploy for network devices that cannot run agents. "
            "Both support desired-state configuration and idempotency."
        ),
    },
]
