"""
Cisco CCNA 200-301 — Domain 6: Automation and Programmability
Question bank (22 questions).
"""

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # 6.1 / 6.2  Traditional vs controller-based / automation impact
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-001",
        "domain": 6,
        "objective": "6.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation impact",
        "stem": (
            "A network administrator is evaluating the impact of moving from "
            "traditional CLI-based management to a fully automated, "
            "controller-based network. Which statement BEST describes a key "
            "operational difference introduced by automation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Automation eliminates the need for any human oversight "
                    "because the controller handles all failure scenarios "
                    "autonomously."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation reduces manual effort but does not "
                    "eliminate human oversight; engineers still design policies, "
                    "monitor outcomes, and respond to events the controller "
                    "cannot resolve."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Automation enables consistent, repeatable configuration "
                    "changes across hundreds of devices simultaneously, reducing "
                    "human error caused by manual CLI entry."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A primary benefit of automation is that the same "
                    "intent-based or script-driven change is applied uniformly "
                    "across all devices at once, removing the per-device "
                    "copy-paste error risk inherent in CLI management."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Automation requires that all devices use the same "
                    "hardware vendor so that the controller API is standardized."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Many modern SDN controllers support multi-vendor "
                    "environments through abstraction layers and standard APIs "
                    "(e.g., NETCONF/YANG, REST), so same-vendor hardware is not "
                    "a requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Automation replaces the data plane entirely, meaning packets "
                    "are forwarded by the controller rather than network devices."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation (and SDN) centralizes the control "
                    "plane logic but the data plane — actual packet forwarding — "
                    "remains distributed on the network devices."
                ),
            },
        ],
        "explanation": (
            "Automation's most immediate operational benefit is consistency and "
            "speed: a single template or API call can configure thousands of "
            "devices identically, preventing configuration drift and human error. "
            "The data plane still resides on the devices, and human engineers "
            "remain responsible for policy design and exception handling."
        ),
    },
    {
        "id": "cd6-002",
        "domain": 6,
        "objective": "6.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Traditional vs controller-based",
        "stem": (
            "In a traditional campus network, a network engineer must log in to "
            "each switch individually to change a VLAN. In a controller-based "
            "network, the engineer makes the change once in the controller UI and "
            "it propagates automatically. Which additional characteristic "
            "DISTINGUISHES controller-based networking from the traditional model?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Controller-based networks require every device to maintain "
                    "a full copy of the network topology, whereas traditional "
                    "networks do not."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In traditional networks each device runs "
                    "distributed protocols (STP, OSPF) and DOES build topology "
                    "tables. Controller-based networks typically centralize "
                    "topology knowledge in the controller."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Traditional networks use distributed control planes on each "
                    "device, while controller-based networks centralize control "
                    "plane logic and program devices via southbound APIs."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the defining architectural difference. "
                    "Traditional networks have each device run its own routing/"
                    "switching protocol (distributed control plane). "
                    "Controller-based SDN moves that logic to a centralized "
                    "controller that pushes forwarding decisions to devices via "
                    "southbound interfaces such as OpenFlow or NETCONF."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Controller-based networks eliminate Layer 2 switching and "
                    "rely exclusively on Layer 3 routing for all forwarding."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Controller-based networks support both Layer 2 "
                    "and Layer 3 forwarding; centralization of the control plane "
                    "does not mandate a specific forwarding layer."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Traditional networks support QoS policies, whereas "
                    "controller-based networks cannot enforce QoS because the "
                    "data plane is fully abstracted."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Controller-based networks can enforce QoS; "
                    "the controller can program QoS markings and queuing policies "
                    "on devices through southbound APIs."
                ),
            },
        ],
        "explanation": (
            "The hallmark distinction between traditional and controller-based "
            "networks is the location of the control plane. Traditional networks "
            "are fully distributed — each router/switch independently runs IGPs, "
            "STP, etc. Controller-based (SDN) networks centralize that logic, "
            "using southbound APIs (OpenFlow, NETCONF, REST) to program "
            "forwarding tables on network devices."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.3  SDN architecture — overlay/underlay/fabric, NBI/SBI
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-003",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN architecture (control/data plane)",
        "stem": (
            "An SDN controller receives a routing-policy update from an "
            "orchestration application and then programs the forwarding tables of "
            "all edge routers. Which two interfaces are used for each of these "
            "communications, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Southbound interface (SBI) from the application to the "
                    "controller; northbound interface (NBI) from the controller "
                    "to the routers."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The directions are reversed. Applications sit "
                    "above the controller and communicate via the NBI. Routers "
                    "sit below the controller and are programmed via the SBI."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Northbound interface (NBI) from the application to the "
                    "controller; southbound interface (SBI) from the controller "
                    "to the routers."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Applications (orchestrators, OSS/BSS, analytics) "
                    "talk to the SDN controller via the northbound API. The "
                    "controller then uses southbound interfaces (OpenFlow, "
                    "NETCONF, RESTCONF, BGP-LS) to program the data-plane "
                    "devices."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Eastbound interface from the application to the controller; "
                    "westbound interface from the controller to the routers."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. East/Westbound interfaces describe communication "
                    "between peer SDN controllers, not between a controller and "
                    "applications or devices."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Northbound interface (NBI) from the application to the "
                    "controller; management plane interface from the controller "
                    "to the routers."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The 'management plane interface' is not the "
                    "correct SDN term for this path. The standard term for "
                    "controller-to-device programming is the southbound interface "
                    "(SBI)."
                ),
            },
        ],
        "explanation": (
            "In an SDN architecture: Northbound Interface (NBI) — between "
            "applications/orchestrators and the controller, typically REST-based. "
            "Southbound Interface (SBI) — between the controller and the network "
            "devices (data plane), using protocols such as OpenFlow, NETCONF, "
            "RESTCONF, or gRPC. East/Westbound — between peer controllers."
        ),
    },
    {
        "id": "cd6-004",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SDN architecture (overlay/underlay/fabric)",
        "stem": (
            "In Cisco SD-Access, VXLAN tunnels carry segmented traffic between "
            "fabric edge nodes while the underlying physical routed network "
            "provides IP reachability. What are these two network layers called, "
            "respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Underlay and overlay.",
                "correct": False,
                "rationale": (
                    "Incorrect. The order is wrong. VXLAN tunnels ARE the "
                    "overlay; the physical IP network is the underlay. The "
                    "question lists VXLAN first, so the correct answer pairs "
                    "'overlay' with VXLAN and 'underlay' with the physical "
                    "network — which is the opposite of this choice."
                ),
            },
            {
                "id": "b",
                "text": "Overlay and underlay.",
                "correct": True,
                "rationale": (
                    "Correct. VXLAN tunnels form the overlay — a virtualized "
                    "logical network on top of the physical infrastructure. The "
                    "physical routed network that provides IP reachability between "
                    "fabric nodes is the underlay. Together they comprise the "
                    "SD-Access fabric."
                ),
            },
            {
                "id": "c",
                "text": "Data plane and control plane.",
                "correct": False,
                "rationale": (
                    "Incorrect. Data plane and control plane describe functional "
                    "separation within a single device or SDN architecture, not "
                    "the physical vs. logical network layer distinction described "
                    "in the question."
                ),
            },
            {
                "id": "d",
                "text": "Fabric and spine.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Fabric' refers to the entire SD-Access solution, "
                    "and 'spine' is a physical tier in a leaf-spine topology — "
                    "neither maps to the VXLAN tunnel layer vs. physical IP "
                    "transport distinction."
                ),
            },
        ],
        "explanation": (
            "SD-Access uses a two-layer model. The underlay is the physical IP "
            "network (routed access using IS-IS or OSPF) that provides "
            "reachability between fabric nodes. The overlay is built with VXLAN "
            "tunnels and LISP control plane, carrying segmented virtual networks "
            "(VNs) across the fabric. Cisco DNA Center orchestrates both layers."
        ),
    },
    {
        "id": "cd6-005",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Northbound/southbound APIs",
        "stem": (
            "A developer writes a Python script that calls a Cisco DNA Center "
            "REST API to retrieve a list of all network devices. From an SDN "
            "architecture perspective, which interface does this API call traverse?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Southbound interface, because the script is requesting "
                    "device data from below the controller."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The southbound interface connects the controller "
                    "to the network devices, not to external applications or "
                    "scripts. The script is an application sitting above the "
                    "controller."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Northbound interface, because the script is an application "
                    "consuming the controller's REST API from above."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Northbound APIs expose the controller's capabilities "
                    "to applications and orchestration systems. A Python script "
                    "calling Cisco DNA Center REST APIs is using the northbound "
                    "interface to consume network services and data."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Eastbound interface, because Python scripts use an "
                    "inter-controller messaging bus."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. East/westbound interfaces are used for "
                    "controller-to-controller federation, not for "
                    "application-to-controller communication."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Management plane interface, because SNMP and REST both "
                    "belong to the management plane."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While REST is often used for management, the "
                    "formal SDN architecture term for the application-to-controller "
                    "API path is northbound interface (NBI), not 'management "
                    "plane interface'."
                ),
            },
        ],
        "explanation": (
            "The NBI (northbound interface) exposes the controller's "
            "capabilities northward to applications, scripts, and orchestrators "
            "via REST, gRPC, or other APIs. The SBI (southbound interface) goes "
            "south to program the actual network devices (routers, switches) using "
            "protocols like NETCONF, OpenFlow, or CLI over SSH. Any Python/"
            "application interacting with DNA Center's API is using the NBI."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.4  Cisco DNA Center
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-006",
        "domain": 6,
        "objective": "6.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cisco DNA Center",
        "stem": (
            "A campus network currently uses traditional per-device CLI "
            "management for 300 switches. The network team is migrating to "
            "Cisco DNA Center. Which capability does Cisco DNA Center provide "
            "that traditional CLI management does NOT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The ability to configure individual interface IP addresses "
                    "on each switch."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Configuring individual interface IP addresses is "
                    "equally possible via CLI on each switch. This is not a "
                    "distinguishing DNA Center capability."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Intent-based policy deployment that translates business "
                    "intent into network configurations and automatically "
                    "provisions all devices consistently."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DNA Center's core value is intent-based networking: "
                    "an administrator defines a business or security policy (e.g., "
                    "group-based access), and DNA Center translates that intent "
                    "into device-specific configurations and provisions all "
                    "devices simultaneously — something traditional per-device "
                    "CLI cannot do."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Support for VLANs and spanning tree on Cisco Catalyst "
                    "switches."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN and STP support is a fundamental feature of "
                    "Catalyst switches managed traditionally via CLI. It is not a "
                    "capability unique to DNA Center."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The ability to run Cisco IOS software on network devices."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IOS runs on the device hardware regardless of "
                    "how the device is managed. DNA Center does not provide or "
                    "replace IOS."
                ),
            },
        ],
        "explanation": (
            "Cisco DNA Center is an intent-based networking controller. Unlike "
            "traditional CLI management (where an engineer manually logs in to "
            "each device), DNA Center allows administrators to define network "
            "intent (policies, segmentation, QoS) in a central UI, and the "
            "platform automatically translates and provisions those policies "
            "across all fabric devices. It also provides network assurance, "
            "analytics, and telemetry not available in CLI-only management."
        ),
    },
    {
        "id": "cd6-007",
        "domain": 6,
        "objective": "6.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cisco DNA Center",
        "stem": (
            "A network engineer is comparing Cisco DNA Center device management "
            "to traditional campus device management. Which statement is TRUE "
            "about how Cisco DNA Center manages devices differently?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "DNA Center communicates with devices exclusively using "
                    "SNMPv2c, the same as traditional network management systems."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DNA Center uses modern southbound protocols "
                    "including NETCONF/YANG, SSH, and telemetry streams. While "
                    "it can interact with SNMP for legacy devices, SNMPv2c is "
                    "not its primary or exclusive protocol."
                ),
            },
            {
                "id": "b",
                "text": (
                    "DNA Center uses a REST-based northbound API allowing "
                    "external systems and scripts to programmatically retrieve "
                    "inventory, topology, and push configurations."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A key difference is that DNA Center exposes a "
                    "documented REST API (northbound) so that external "
                    "orchestration, ITSM systems, or custom scripts can "
                    "query device inventory and push changes — something a "
                    "traditional NMS or CLI-only environment does not provide "
                    "in a structured, programmable way."
                ),
            },
            {
                "id": "c",
                "text": (
                    "In DNA Center, each device retains its own independent "
                    "control plane with no influence from the controller."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SD-Access (managed by DNA Center) moves "
                    "segmentation and policy logic to a centralized control "
                    "plane, using LISP for the control plane and VXLAN for the "
                    "data plane. Devices do not act fully independently."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DNA Center requires the network to be converted to a "
                    "full OpenFlow SDN architecture before any device can be "
                    "managed."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DNA Center does not require OpenFlow. It supports "
                    "traditional Cisco IOS/IOS-XE devices for basic management "
                    "and uses NETCONF/YANG and proprietary protocols for advanced "
                    "SD-Access features."
                ),
            },
        ],
        "explanation": (
            "Cisco DNA Center differentiates itself through programmability: "
            "its northbound REST API allows IT automation pipelines to interact "
            "with the controller, and its southbound protocols (NETCONF, SSH, "
            "telemetry) are modern alternatives to SNMP polling. Traditional "
            "campus management relies on per-device CLI or basic SNMP NMS, "
            "lacking this programmatic abstraction layer."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.5  REST APIs — HTTP verbs, CRUD, status codes, statelessness
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-008",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A network automation script needs to CREATE a new VLAN object via "
            "a REST API call to a network controller. The VLAN does not yet "
            "exist. Which HTTP method and expected success status code is "
            "CORRECT for this operation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "GET with status 200 OK.",
                "correct": False,
                "rationale": (
                    "Incorrect. GET retrieves an existing resource and returns "
                    "200 on success. It does not create resources."
                ),
            },
            {
                "id": "b",
                "text": "PUT with status 200 OK.",
                "correct": False,
                "rationale": (
                    "Incorrect. PUT updates or replaces an existing resource "
                    "(idempotent). While some implementations allow PUT to create "
                    "a resource when the URI is known, the canonical HTTP method "
                    "for creation is POST, which returns 201 Created."
                ),
            },
            {
                "id": "c",
                "text": "POST with status 201 Created.",
                "correct": True,
                "rationale": (
                    "Correct. POST is the HTTP method for creating a new "
                    "resource on a server. The standard success response when a "
                    "resource is newly created is HTTP 201 Created, optionally "
                    "with a Location header pointing to the new resource's URI."
                ),
            },
            {
                "id": "d",
                "text": "PATCH with status 204 No Content.",
                "correct": False,
                "rationale": (
                    "Incorrect. PATCH partially modifies an existing resource. "
                    "204 No Content indicates success with no response body, "
                    "typical of DELETE or some PUT/PATCH operations, not "
                    "resource creation."
                ),
            },
        ],
        "explanation": (
            "REST CRUD-to-HTTP mapping: Create=POST (201), Read=GET (200), "
            "Update(full)=PUT (200/204), Update(partial)=PATCH (200/204), "
            "Delete=DELETE (200/204). For creation, POST returns 201 Created "
            "with a Location header referencing the new resource URI. This is "
            "a commonly tested CCNA automation topic."
        ),
    },
    {
        "id": "cd6-009",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A REST API client sends a request to update only the description "
            "field of an existing BGP neighbor object without replacing the "
            "entire object. Which HTTP method is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "PUT, because it replaces the entire resource at the "
                    "specified URI."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. PUT replaces the entire resource body. Sending "
                    "only the description field with PUT would overwrite all "
                    "other fields with missing/null values, which is not the "
                    "desired partial update."
                ),
            },
            {
                "id": "b",
                "text": (
                    "PATCH, because it applies a partial modification to an "
                    "existing resource."
                ),
                "correct": True,
                "rationale": (
                    "Correct. PATCH is explicitly designed for partial resource "
                    "updates. The client sends only the fields to be changed, "
                    "and the server merges the changes with the existing resource "
                    "state — preserving fields that were not included in the "
                    "request."
                ),
            },
            {
                "id": "c",
                "text": (
                    "POST, because it is the most flexible HTTP method for "
                    "sending data to the server."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. POST creates new resources. Using POST to modify "
                    "part of an existing resource is non-standard and most REST "
                    "APIs would not handle it as a partial update."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DELETE followed by POST, to remove the old object and "
                    "re-create it with the new description."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DELETE + POST is destructive and could cause a "
                    "brief outage of the BGP neighbor. PATCH achieves the same "
                    "partial update atomically without deleting the resource."
                ),
            },
        ],
        "explanation": (
            "HTTP methods for resource modification: PUT replaces the entire "
            "resource (idempotent); PATCH applies a partial update (also should "
            "be idempotent per RFC 5789, though implementations vary). When "
            "only a subset of fields needs to change, PATCH is the correct "
            "choice. POST is for creation; DELETE removes resources."
        ),
    },
    {
        "id": "cd6-010",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A network automation script calls a Cisco DNA Center REST API and "
            "receives the following HTTP response:\n\n"
            "    HTTP/1.1 401 Unauthorized\n"
            "    Content-Type: application/json\n\n"
            "    {\"response\": \"No Authentication Header\", \"version\": \"1.0\"}\n\n"
            "What does this status code indicate, and what should the script "
            "do FIRST to resolve it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The resource was not found; the script should verify the "
                    "API endpoint URL."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP 404 Not Found indicates the resource does "
                    "not exist. HTTP 401 Unauthorized specifically means "
                    "authentication credentials are missing or invalid."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The authenticated user lacks permission for the resource; "
                    "the script should request elevated privileges from an "
                    "administrator."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP 403 Forbidden indicates the client is "
                    "authenticated but lacks authorization for the resource. "
                    "HTTP 401 specifically means authentication itself failed "
                    "or is absent."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Authentication credentials are missing or invalid; the "
                    "script should first obtain a valid token by calling the "
                    "DNA Center authentication API and include it as a Bearer "
                    "token in subsequent requests."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 401 Unauthorized means the server could not "
                    "authenticate the request. For Cisco DNA Center, the typical "
                    "fix is to call POST /dna/system/api/v1/auth/token with "
                    "Basic Auth credentials to receive a JWT token, then include "
                    "that token in subsequent API calls using the "
                    "'X-Auth-Token' header."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The server encountered an internal error; the script should "
                    "retry the request after a delay."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP 5xx codes (e.g., 500 Internal Server Error) "
                    "indicate server-side errors that may be resolved by retrying. "
                    "HTTP 401 is a client-side authentication failure requiring "
                    "the client to supply valid credentials."
                ),
            },
        ],
        "explanation": (
            "Key REST HTTP status codes: 200 OK, 201 Created, 400 Bad Request "
            "(malformed syntax), 401 Unauthorized (authentication failure), "
            "403 Forbidden (authenticated but no permission), 404 Not Found, "
            "500 Internal Server Error. For Cisco DNA Center, 401 means the "
            "X-Auth-Token header is missing or expired — the script must "
            "re-authenticate via the /auth/token endpoint first."
        ),
    },
    {
        "id": "cd6-011",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (statelessness/data encoding)",
        "stem": (
            "A REST API is described as stateless. Which behavior does this "
            "characteristic REQUIRE of the client?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The client must establish a persistent TCP session so the "
                    "server can track context across API calls."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Statelessness means the opposite: the server "
                    "does NOT track session state between requests. A persistent "
                    "TCP connection (HTTP keep-alive) is a transport optimization "
                    "and does not imply server-side session state."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Each API request must contain all information the server "
                    "needs to process it — including authentication credentials "
                    "or tokens — because the server stores no client session "
                    "state between requests."
                ),
                "correct": True,
                "rationale": (
                    "Correct. REST statelessness (a core REST constraint) means "
                    "every request from client to server must be self-contained. "
                    "The server never stores session state between calls, so the "
                    "client must include auth tokens, parameters, and context "
                    "in every individual request."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The client must cache all responses locally and never "
                    "request the same resource twice."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Caching is a separate REST constraint "
                    "(cacheable responses). Statelessness refers to the server "
                    "not storing client session state, not to client-side caching "
                    "behavior."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The client must use XML encoding for all request bodies "
                    "because JSON encoding carries inherent state information."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Statelessness has nothing to do with data "
                    "encoding format. REST APIs commonly use JSON (or XML), and "
                    "neither format inherently carries session state."
                ),
            },
        ],
        "explanation": (
            "REST statelessness is one of the six architectural constraints "
            "defined by Roy Fielding. It requires that every HTTP request be "
            "self-contained — the server cannot depend on context from a "
            "previous request. This means tokens, resource identifiers, and all "
            "required parameters must be included in every call. This design "
            "improves scalability because any server instance can handle any "
            "request without session affinity."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.5  REST status codes — extra scenario
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-012",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A script sends the following REST API request to a network "
            "controller:\n\n"
            "    POST /api/v1/vlans HTTP/1.1\n"
            "    Content-Type: application/json\n"
            "    X-Auth-Token: abc123\n\n"
            "    {\"vlan_id\": \"abc\", \"name\": \"Engineering\"}\n\n"
            "The server returns HTTP 400. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The authentication token 'abc123' has expired."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An expired or invalid token would produce HTTP "
                    "401 Unauthorized, not 400 Bad Request."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The request body contains invalid data — 'vlan_id' has a "
                    "string value 'abc' instead of a numeric VLAN ID, causing "
                    "the server to reject the malformed request."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 400 Bad Request means the server could not "
                    "process the request due to a client-side error in the "
                    "request syntax or data. VLAN IDs must be integers (1–4094), "
                    "so passing the string 'abc' is syntactically or semantically "
                    "invalid, causing the server to return 400."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The server does not have a VLAN with that name in its "
                    "database, so it returns a not-found error."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A missing resource returns HTTP 404 Not Found. "
                    "Since this is a POST to CREATE a new VLAN, a 404 would "
                    "mean the endpoint itself doesn't exist. HTTP 400 indicates "
                    "a problem with the request data, not a missing resource."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The server encountered an unhandled exception while "
                    "processing the request."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Unhandled server-side exceptions return HTTP 500 "
                    "Internal Server Error. HTTP 400 is a client-side error "
                    "indicating the request was malformed."
                ),
            },
        ],
        "explanation": (
            "HTTP 400 Bad Request indicates the server cannot process the "
            "request because of a client error — malformed JSON, wrong data "
            "types, missing required fields, or invalid parameter values. In "
            "this scenario, vlan_id should be an integer, not the string 'abc'. "
            "Know the full set: 200 (OK), 201 (Created), 400 (Bad Request / "
            "client error), 401 (Unauthorized / no/bad auth), 403 (Forbidden / "
            "authenticated but not allowed), 404 (Not Found), 500 (Internal "
            "Server Error)."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.6  Configuration management — Ansible, Puppet, Chef
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-013",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "A network team wants a configuration-management tool that requires "
            "NO software agent installed on the managed network devices and "
            "pushes configuration to them over SSH. Which tool BEST fits this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Ansible",
                "correct": True,
                "rationale": (
                    "Correct. Ansible is agentless and uses a push model, "
                    "connecting to devices over SSH (or APIs) from a control "
                    "node without requiring an agent on each device — ideal for "
                    "network gear that cannot run agents."
                ),
            },
            {
                "id": "b",
                "text": "Puppet",
                "correct": False,
                "rationale": (
                    "Incorrect. Puppet is traditionally agent-based and "
                    "pull-based: managed nodes run a Puppet agent that pulls "
                    "configuration from the Puppet master, contradicting the "
                    "no-agent requirement."
                ),
            },
            {
                "id": "c",
                "text": "Chef",
                "correct": False,
                "rationale": (
                    "Incorrect. Chef is also traditionally agent-based and "
                    "pull-based, using a Chef client on each node that pulls "
                    "'recipes' from the Chef server."
                ),
            },
            {
                "id": "d",
                "text": "SNMPv3",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP is a monitoring/management protocol, not "
                    "a configuration-management framework like Ansible, "
                    "Puppet, or Chef."
                ),
            },
        ],
        "explanation": (
            "Ansible = agentless, push model, over SSH/APIs. Puppet and Chef "
            "are traditionally agent-based and pull model (the managed node "
            "pulls config from a master/server). Knowing agent vs. agentless "
            "and push vs. pull is a core CCNA automation distinction."
        ),
    },
    {
        "id": "cd6-014",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "An engineer applies the same Ansible playbook to configure NTP "
            "on 50 routers three times in a row without any changes. After the "
            "third run, the NTP configuration on all routers is identical to "
            "what it was after the first run, with no duplicate entries or "
            "errors. Which configuration-management property does this "
            "demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Convergence — the network eventually reaches the desired "
                    "state after multiple passes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Convergence refers to routing protocol stability, "
                    "not the configuration-management property of producing the "
                    "same result on repeated application."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Idempotency — applying the same configuration operation "
                    "multiple times produces the same result as applying it once."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Idempotency means that running the same playbook "
                    "or configuration task multiple times has the same effect as "
                    "running it once — no duplicate entries are added, no errors "
                    "are introduced. Ansible tasks are designed to be idempotent "
                    "by checking current state before making changes."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Atomicity — all configuration changes succeed or none of "
                    "them are applied."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Atomicity describes all-or-nothing transaction "
                    "behavior. The scenario describes repeated application "
                    "producing the same result, which is idempotency, not "
                    "atomicity."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Agentlessness — the tool does not require software on "
                    "the managed nodes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Agentlessness describes the communication model "
                    "(no client software required), not the property of repeated "
                    "runs producing consistent results."
                ),
            },
        ],
        "explanation": (
            "Idempotency is a critical property of configuration-management "
            "tools like Ansible, Puppet, and Chef. An idempotent operation "
            "produces the same outcome regardless of how many times it is "
            "executed. For example, an Ansible task to 'ensure NTP server "
            "192.0.2.1 is configured' will add it if missing but will not "
            "add a duplicate if it is already present."
        ),
    },
    {
        "id": "cd6-015",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "A team is choosing between Puppet and Ansible for large-scale "
            "network device configuration. They are concerned about scalability "
            "and want managed devices to proactively fetch their configuration "
            "on a schedule. Which statement CORRECTLY describes the model that "
            "meets this requirement, and which tool provides it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Push model — Ansible pushes configurations to all devices "
                    "simultaneously on a schedule defined in the control node."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While Ansible can be scheduled, it uses a push "
                    "model where the control node initiates connections and "
                    "pushes configs. The team's requirement for devices to "
                    "'proactively fetch' config describes a pull model."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Pull model — Puppet agents installed on devices periodically "
                    "check in with the Puppet master and pull the desired-state "
                    "catalog."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Puppet uses a pull model: each managed node runs "
                    "a Puppet agent that contacts the Puppet master (Puppet "
                    "Server) on a regular interval (default every 30 minutes), "
                    "downloads a compiled catalog of the desired state, and "
                    "enforces it locally. This is the defining pull-based, "
                    "agent-based behavior of Puppet."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Pull model — Ansible agents installed on devices pull "
                    "playbooks from the Ansible Tower server on a schedule."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible does NOT use agents. Even with Ansible "
                    "Tower/AWX scheduling, the control node pushes configs; "
                    "the managed devices do not pull."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Push model — Chef cookbooks are pushed from the Chef "
                    "workstation to the Chef server, and the Chef server then "
                    "proactively pushes them to nodes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Chef also uses a pull model: Chef clients "
                    "(agents) on managed nodes pull cookbooks from the Chef "
                    "server. The Chef server does not push to clients."
                ),
            },
        ],
        "explanation": (
            "Push vs. Pull: Ansible = agentless PUSH (control node initiates). "
            "Puppet = agent-based PULL (agent on node polls master every ~30 min). "
            "Chef = agent-based PULL (Chef client on node pulls from Chef server). "
            "For devices that must proactively fetch their config on a schedule, "
            "Puppet's (or Chef's) pull model is the match."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.7  JSON — syntax, data types, valid vs. invalid
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-016",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "JSON data format",
        "stem": (
            "Examine the following data snippet:\n\n"
            "    {\n"
            "        \"hostname\": \"SW1\",\n"
            "        \"vlan_id\": 10,\n"
            "        \"active\": true,\n"
            "        \"description\": null,\n"
            "        \"interfaces\": [\"Gi0/0\", \"Gi0/1\"]\n"
            "    }\n\n"
            "Which statement CORRECTLY identifies the data types present?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "\"hostname\" is a string, \"vlan_id\" is a string because "
                    "all values in JSON must be quoted, \"active\" is a boolean, "
                    "\"description\" is null, and \"interfaces\" is an array."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON numbers are NOT quoted. 'vlan_id: 10' is a "
                    "valid JSON number (integer). Only string values require "
                    "double quotes in JSON."
                ),
            },
            {
                "id": "b",
                "text": (
                    "\"hostname\" is a string, \"vlan_id\" is a number, "
                    "\"active\" is a boolean, \"description\" is null, and "
                    "\"interfaces\" is an array."
                ),
                "correct": True,
                "rationale": (
                    "Correct. JSON supports six data types: string (double-quoted "
                    "text), number (integer or float, unquoted), boolean (true or "
                    "false, lowercase, unquoted), null (lowercase, unquoted), "
                    "object ({}), and array ([]). Each field in the snippet maps "
                    "to exactly one of these types."
                ),
            },
            {
                "id": "c",
                "text": (
                    "\"hostname\" is a string, \"vlan_id\" is an integer object, "
                    "\"active\" is a string because it is a keyword, "
                    "\"description\" is an empty string, and \"interfaces\" is "
                    "a tuple."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON has no 'integer object' or 'tuple' types. "
                    "'true' is a JSON boolean, not a string. 'null' is the null "
                    "type, not an empty string. Arrays in JSON use [] syntax."
                ),
            },
            {
                "id": "d",
                "text": (
                    "\"hostname\" is a string, \"vlan_id\" is a number, "
                    "\"active\" is a string because booleans in JSON must be "
                    "quoted as \"true\", \"description\" is null, and "
                    "\"interfaces\" is an object."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON booleans are the literal unquoted values "
                    "'true' or 'false' (lowercase). Quoting them as \"true\" "
                    "would make them strings, not booleans. Also, [] is an array, "
                    "not an object ({})."
                ),
            },
        ],
        "explanation": (
            "JSON (RFC 8259) defines exactly six value types: string (double "
            "quotes required), number (no quotes, integer or floating point), "
            "boolean (lowercase true/false, no quotes), null (lowercase, no "
            "quotes), object ({} — unordered key/value pairs), and array ([] — "
            "ordered list). Confusing quoted strings with unquoted numbers/"
            "booleans is a frequent exam trap."
        ),
    },
    {
        "id": "cd6-017",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "JSON data format",
        "stem": (
            "Which of the following is INVALID JSON and would cause a parser "
            "error?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "{\"port\": 443, \"tls\": true, \"cipher\": null}"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect (this IS valid JSON). The object has three "
                    "key/value pairs with a number, boolean, and null — all "
                    "valid JSON types using correct syntax."
                ),
            },
            {
                "id": "b",
                "text": (
                    "{\"vlans\": [10, 20, 30]}"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect (this IS valid JSON). An object containing an "
                    "array of numbers is well-formed JSON."
                ),
            },
            {
                "id": "c",
                "text": (
                    "{hostname: \"R1\", \"ip\": \"10.0.0.1\"}"
                ),
                "correct": True,
                "rationale": (
                    "Correct — this IS invalid JSON. JSON requires all object "
                    "keys to be strings enclosed in double quotes. The key "
                    "'hostname' is unquoted, which violates the JSON specification "
                    "and causes a parse error. Valid JSON would be: "
                    "{\"hostname\": \"R1\", \"ip\": \"10.0.0.1\"}"
                ),
            },
            {
                "id": "d",
                "text": (
                    "{\"active\": false, \"count\": 0}"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect (this IS valid JSON). 'false' is a valid JSON "
                    "boolean and 0 is a valid JSON number. The syntax is correct."
                ),
            },
        ],
        "explanation": (
            "A critical JSON rule: ALL object keys MUST be double-quoted strings. "
            "This distinguishes JSON from JavaScript object literal syntax (which "
            "allows unquoted keys). Other common JSON invalidity triggers: single "
            "quotes instead of double quotes, trailing commas, unquoted string "
            "values, and using 'True'/'False'/'None' (Python) instead of "
            "'true'/'false'/'null'."
        ),
    },
    {
        "id": "cd6-018",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "JSON data format",
        "stem": (
            "A network script parses the following JSON response from a "
            "controller API:\n\n"
            "    {\n"
            "        \"devices\": [\n"
            "            {\"id\": 1, \"name\": \"R1\", \"reachable\": true},\n"
            "            {\"id\": 2, \"name\": \"R2\", \"reachable\": false}\n"
            "        ],\n"
            "        \"total\": 2\n"
            "    }\n\n"
            "The script needs to access the name of the SECOND device. "
            "Using Python-style dot/bracket notation, which reference is "
            "CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "data[\"devices\"][2][\"name\"]",
                "correct": False,
                "rationale": (
                    "Incorrect. JSON arrays (and Python lists) are zero-indexed. "
                    "Index 2 would refer to a third element, which does not "
                    "exist in this two-element array, resulting in an IndexError."
                ),
            },
            {
                "id": "b",
                "text": "data[\"devices\"][1][\"name\"]",
                "correct": True,
                "rationale": (
                    "Correct. After parsing, 'data[\"devices\"]' is a Python "
                    "list. The second device is at index 1 (zero-based). "
                    "data[\"devices\"][1][\"name\"] returns \"R2\"."
                ),
            },
            {
                "id": "c",
                "text": "data.devices[2].name",
                "correct": False,
                "rationale": (
                    "Incorrect. Python's json.loads() returns a dictionary, not "
                    "an object with dot-notation attribute access. Dot notation "
                    "would raise an AttributeError. Additionally, index 2 is "
                    "out of range."
                ),
            },
            {
                "id": "d",
                "text": "data[\"devices\"][\"R2\"][\"name\"]",
                "correct": False,
                "rationale": (
                    "Incorrect. 'devices' is a JSON array (Python list), not a "
                    "dictionary. Accessing it with string key \"R2\" would raise "
                    "a TypeError. Lists are accessed by integer index."
                ),
            },
        ],
        "explanation": (
            "JSON arrays are ordered and zero-indexed when parsed into Python "
            "lists via json.loads(). The first element is index 0, second is "
            "index 1, etc. JSON objects become Python dictionaries accessed "
            "with string keys. Dot notation (data.devices) is not valid for "
            "Python dicts — it requires bracket notation (data[\"devices\"])."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multiple-response questions (3 total)
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-019",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "Select TWO characteristics that are TRUE of Ansible when used for "
            "network device configuration management."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ansible is agentless — it does not require software to be "
                    "installed on managed network devices."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ansible connects to devices using SSH (or APIs) "
                    "from a central control node; no Ansible agent software "
                    "runs on the managed devices."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Ansible uses a pull model in which each device fetches its "
                    "playbook from the Ansible master on a schedule."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible uses a PUSH model. The control node "
                    "initiates connections and pushes configurations to managed "
                    "devices. Puppet and Chef use pull models."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Ansible playbooks are written in YAML and describe the "
                    "desired state of the device configuration."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ansible uses YAML-formatted playbooks. Playbooks "
                    "define tasks that describe the desired end-state, making "
                    "them human-readable and declarative in nature."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ansible requires a Ruby runtime environment on each managed "
                    "network device to execute automation tasks."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ruby runtime is a requirement for Chef (which "
                    "uses Chef client written in Ruby). Ansible is agentless and "
                    "requires no runtime on managed devices."
                ),
            },
        ],
        "explanation": (
            "Ansible's two signature characteristics for network automation: "
            "(1) Agentless — no client software needed on devices, uses SSH/APIs; "
            "(2) YAML-based playbooks describing desired state. Chef uses Ruby, "
            "Puppet uses its own DSL. Ansible and Puppet/Chef are commonly "
            "contrasted on the CCNA exam."
        ),
    },
    {
        "id": "cd6-020",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "Select TWO HTTP methods that are considered IDEMPOTENT according "
            "to the HTTP specification — meaning that making the same request "
            "multiple times produces the same server state as making it once."
        ),
        "options": [
            {
                "id": "a",
                "text": "POST",
                "correct": False,
                "rationale": (
                    "Incorrect. POST is NOT idempotent. Sending the same POST "
                    "request multiple times typically creates multiple resources "
                    "(e.g., multiple VLAN entries), changing server state each "
                    "time."
                ),
            },
            {
                "id": "b",
                "text": "GET",
                "correct": True,
                "rationale": (
                    "Correct. GET is idempotent (and also safe). Retrieving the "
                    "same resource multiple times always returns the same data "
                    "without modifying server state."
                ),
            },
            {
                "id": "c",
                "text": "PUT",
                "correct": True,
                "rationale": (
                    "Correct. PUT is idempotent. Sending the same PUT request "
                    "multiple times replaces the resource with the same data "
                    "each time, resulting in an identical server state after "
                    "each call."
                ),
            },
            {
                "id": "d",
                "text": "DELETE",
                "correct": False,
                "rationale": (
                    "Incorrect in the context of this question. While DELETE is "
                    "technically idempotent per RFC 7231 (deleting an already "
                    "deleted resource returns 404 but the state is the same), "
                    "GET and PUT are the clearer and more commonly cited examples. "
                    "Note: if the exam asks about safe AND idempotent, GET is the "
                    "best answer; PUT is idempotent but not safe."
                ),
            },
        ],
        "explanation": (
            "HTTP idempotency (RFC 7231): Safe and idempotent: GET, HEAD. "
            "Idempotent but not safe: PUT, DELETE. Not idempotent: POST, PATCH. "
            "PUT is idempotent because the same full replacement applied twice "
            "leaves the resource in the same state. POST is not idempotent "
            "because each call may create a new resource."
        ),
    },
    {
        "id": "cd6-021",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SDN architecture (control/data plane)",
        "stem": (
            "Select TWO statements that CORRECTLY describe the separation of "
            "the control plane and data plane in an SDN architecture."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The data plane is responsible for forwarding packets based "
                    "on entries in FIB/CAM tables, and it resides on the "
                    "network devices."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The data plane (forwarding plane) performs the "
                    "actual packet forwarding using the Forwarding Information "
                    "Base (FIB) or CAM/TCAM tables on switches and routers. "
                    "It remains distributed on the physical hardware in SDN."
                ),
            },
            {
                "id": "b",
                "text": (
                    "In SDN, the control plane is removed from all network "
                    "devices and centralized in the SDN controller, which uses "
                    "southbound APIs to program the data plane on each device."
                ),
                "correct": True,
                "rationale": (
                    "Correct. SDN's defining characteristic is the separation "
                    "and centralization of the control plane. The controller "
                    "makes all routing/switching decisions and pushes forwarding "
                    "rules to devices via southbound protocols (OpenFlow, "
                    "NETCONF, etc.)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The SDN controller resides in the data plane because it "
                    "processes transit packets at line rate."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The SDN controller is part of the control plane, "
                    "not the data plane. It does not forward transit user traffic. "
                    "Packet forwarding at line rate is the data plane function "
                    "performed by ASICs in network devices."
                ),
            },
            {
                "id": "d",
                "text": (
                    "SDN eliminates the need for any forwarding tables on network "
                    "devices because the controller forwards all packets on behalf "
                    "of the devices."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SDN does not eliminate forwarding tables. The "
                    "controller programs the forwarding tables (flow tables in "
                    "OpenFlow, FIB in traditional SDN). Network devices still "
                    "forward packets locally using those tables."
                ),
            },
        ],
        "explanation": (
            "In SDN, the control plane (routing decisions, topology calculation, "
            "policy) is centralized in the controller. The data plane (packet "
            "forwarding based on installed flow/FIB entries) remains on the "
            "physical network devices. The controller uses southbound APIs "
            "(e.g., OpenFlow, NETCONF) to program the data plane. This "
            "separation enables centralized policy management and network "
            "programmability."
        ),
    },
    # ------------------------------------------------------------------ #
    # Additional coverage questions
    # ------------------------------------------------------------------ #
    {
        "id": "cd6-022",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Northbound/southbound APIs",
        "stem": (
            "A network architect is designing an SDN solution and must choose "
            "a southbound interface (SBI) protocol for programming forwarding "
            "tables on Cisco IOS-XE devices. Which protocol is a Cisco-supported "
            "SBI that uses a model-driven approach based on YANG data models "
            "over a secure transport?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "OpenFlow — the original SDN southbound protocol developed "
                    "by the Open Networking Foundation."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OpenFlow is a valid SBI protocol but it is not "
                    "the primary SBI used by Cisco IOS-XE devices with DNA Center. "
                    "Cisco primarily uses NETCONF/YANG and RESTCONF for "
                    "model-driven programmability on IOS-XE."
                ),
            },
            {
                "id": "b",
                "text": (
                    "NETCONF — a network management protocol that uses YANG data "
                    "models and operates over SSH (TCP 830) to configure and "
                    "retrieve device state."
                ),
                "correct": True,
                "rationale": (
                    "Correct. NETCONF (RFC 6241) is a model-driven SBI protocol "
                    "supported on Cisco IOS-XE. It uses YANG data models to "
                    "describe configuration and state, transports messages as XML "
                    "over SSH (port 830), and supports candidate/running/startup "
                    "datastores. DNA Center uses NETCONF as its primary southbound "
                    "protocol for SD-Access fabric devices."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SNMPv3 — an industry-standard protocol that supports both "
                    "device configuration and monitoring over UDP."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv3 provides authentication and encryption for "
                    "SNMP but is primarily a monitoring protocol. Its SET "
                    "operations for configuration are limited and it does not "
                    "use YANG data models. NETCONF is the modern model-driven "
                    "alternative."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Telnet — a legacy protocol used for CLI-based southbound "
                    "device configuration in SDN deployments."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Telnet is an unencrypted legacy CLI protocol, "
                    "not a modern model-driven SBI. It does not use YANG data "
                    "models and is not suitable for programmatic SDN southbound "
                    "communication."
                ),
            },
        ],
        "explanation": (
            "Cisco's model-driven programmability stack: NETCONF (SSH/port 830, "
            "XML encoding, YANG models) and RESTCONF (HTTPS, JSON or XML, YANG "
            "models) are the primary SBI protocols for IOS-XE. DNA Center uses "
            "NETCONF/YANG as its southbound interface for SD-Access. OpenFlow is "
            "an open-standard SBI used in academic/open SDN environments but is "
            "less prevalent in enterprise Cisco deployments."
        ),
    },
]
