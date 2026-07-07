"""
CCNA 200-301 Domain 6: Automation and Programmability
Study notes for exam preparation.
"""

NOTES = [
    {
        "domain": 6,
        "topic": "Automation Impact on Network Management",
        "objective": "6.1",
        "video": "Network Automation",
        "study_topics": ["Automation impact"],
        "body": (
            "<p>Network automation transforms how engineers configure, monitor, and manage "
            "infrastructure by replacing repetitive manual tasks with programmatic processes. "
            "Instead of logging into each device individually and applying changes by hand, "
            "automation tools can push configurations to hundreds of devices simultaneously, "
            "reducing human error and saving significant time.</p>"
            "<p><strong>Key benefits of automation:</strong></p>"
            "<ul>"
            "<li><strong>Consistency:</strong> Every device receives the exact same configuration, "
            "eliminating typos and partial changes that cause outages.</li>"
            "<li><strong>Speed:</strong> Tasks that once took days (e.g., rolling out ACLs across "
            "1,000 switches) complete in minutes.</li>"
            "<li><strong>Scalability:</strong> Adding new devices to an automation workflow requires "
            "minimal incremental effort.</li>"
            "<li><strong>Auditability:</strong> Version-controlled configuration files create a "
            "clear history of every change, supporting compliance and troubleshooting.</li>"
            "<li><strong>Self-healing:</strong> Automated monitoring can detect and remediate faults "
            "without human intervention.</li>"
            "</ul>"
            "<p><strong>Challenges to consider:</strong></p>"
            "<ul>"
            "<li>Initial investment in learning scripting languages (Python) and tooling.</li>"
            "<li>Risk of large-scale misconfiguration if automation scripts contain bugs—test in a "
            "lab environment first.</li>"
            "<li>Legacy devices may lack APIs, requiring screen-scraping or older protocols.</li>"
            "</ul>"
            "<p>For the CCNA exam, understand that automation reduces OpEx, improves accuracy, and "
            "enables intent-based networking where the engineer declares <em>what</em> the network "
            "should do, not <em>how</em> to configure each device.</p>"
        ),
        "key_points": [
            "Automation replaces repetitive CLI tasks with programmatic, repeatable processes.",
            "Benefits include consistency, speed, scalability, auditability, and self-healing.",
            "Reduces operational expenditure (OpEx) and human error.",
            "Test automation scripts in a lab before deploying to production.",
            "Enables intent-based networking—declare desired state, not device-by-device steps.",
        ],
    },
    {
        "domain": 6,
        "topic": "Traditional vs Controller-Based Networking",
        "objective": "6.2",
        "video": "Controller-Based Networking",
        "study_topics": [
            "Traditional vs controller-based",
            "Network automation and controller-based architecture concepts",
        ],
        "body": (
            "<p><strong>Traditional (distributed) networking</strong> places both the control plane "
            "and data plane on every individual device. Each router or switch independently runs "
            "routing protocols (OSPF, BGP), makes its own forwarding decisions, and requires "
            "separate CLI-based configuration. This model is well-understood but scales poorly: "
            "any policy change must be replicated to every device manually.</p>"
            "<p><strong>Controller-based networking</strong> centralises the control plane into a "
            "software controller. Network devices (switches, routers, APs) retain the data plane "
            "but defer forwarding decisions to the controller. The controller has a global view of "
            "the entire topology and can compute optimal paths, enforce policies, and push "
            "configurations programmatically via southbound APIs.</p>"
            "<p><strong>Comparison:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Aspect</th><th>Traditional</th><th>Controller-Based</th></tr>"
            "<tr><td>Control plane</td><td>Distributed (per device)</td><td>Centralised (controller)</td></tr>"
            "<tr><td>Configuration</td><td>CLI per device</td><td>Controller API / GUI</td></tr>"
            "<tr><td>Scalability</td><td>Difficult at scale</td><td>Scales via abstraction</td></tr>"
            "<tr><td>Visibility</td><td>Device-by-device</td><td>Topology-wide</td></tr>"
            "<tr><td>Automation</td><td>Scripts + SSH</td><td>Native REST/NETCONF APIs</td></tr>"
            "</table>"
            "<p>Controller-based architectures underpin modern SD-WAN, SD-Access, and cloud-managed "
            "wireless systems. Cisco DNA Center is Cisco's enterprise controller for SD-Access. "
            "The shift to controller-based models is the foundation of network automation because "
            "the controller exposes standard APIs that scripts and orchestration tools can call.</p>"
        ),
        "key_points": [
            "Traditional networking: control and data planes co-located on every device.",
            "Controller-based: centralised control plane; devices handle only data-plane forwarding.",
            "Controller provides global topology view, enabling policy-consistent automation.",
            "Cisco DNA Center is the primary controller for enterprise SD-Access deployments.",
            "Controller exposes northbound APIs (to apps) and southbound APIs (to devices).",
        ],
    },
    {
        "domain": 6,
        "topic": "SDN Architecture: Control/Data Planes and Overlay/Underlay/Fabric",
        "objective": "6.3",
        "video": "SDN Architecture",
        "study_topics": [
            "SDN architecture (control/data plane)",
            "SDN architecture (overlay/underlay/fabric)",
        ],
        "body": (
            "<p><strong>Software-Defined Networking (SDN)</strong> separates the network into "
            "distinct functional planes:</p>"
            "<ul>"
            "<li><strong>Data plane (forwarding plane):</strong> The part of the device that actually "
            "moves packets—ASIC-based packet switching, applying ACLs, QoS markings. Operates in "
            "hardware at line rate.</li>"
            "<li><strong>Control plane:</strong> The 'brain' that decides <em>how</em> to forward "
            "packets—running routing protocols, building FIBs/CAMs. In SDN this logic is lifted out "
            "of devices and centralised in a controller.</li>"
            "<li><strong>Management plane:</strong> Out-of-band management—SSH, SNMP, NETCONF—used "
            "to configure and monitor devices. Not involved in forwarding decisions.</li>"
            "</ul>"
            "<p><strong>Overlay / Underlay / Fabric:</strong></p>"
            "<ul>"
            "<li><strong>Underlay:</strong> The physical IP transport network (routers, switches, "
            "cables). It provides reachability between all nodes. Can be OSPF or IS-IS routed. "
            "Optimised for simplicity and high availability.</li>"
            "<li><strong>Overlay:</strong> A virtual network tunnelled on top of the underlay. "
            "Uses encapsulation protocols such as VXLAN, GRE, or IPsec to carry tenant traffic "
            "independent of the underlay topology. Provides segmentation and policy enforcement.</li>"
            "<li><strong>Fabric:</strong> The combination of underlay + overlay + the controller "
            "that manages them—the entire system working together. In Cisco SD-Access, the fabric "
            "uses VXLAN over an IP underlay managed by Cisco DNA Center.</li>"
            "</ul>"
            "<p>Decoupling overlay from underlay means you can change the physical topology without "
            "re-addressing virtual networks, and you can move workloads without changing policies.</p>"
        ),
        "key_points": [
            "Data plane: hardware forwarding of packets; control plane: routing/switching logic.",
            "SDN moves the control plane to a centralised controller.",
            "Management plane handles device configuration and monitoring (SSH, SNMP, NETCONF).",
            "Underlay: physical IP transport network providing node reachability.",
            "Overlay: virtual network (VXLAN, GRE) tunnelled over the underlay for tenant isolation.",
            "Fabric = underlay + overlay + controller working as an integrated system.",
        ],
    },
    {
        "domain": 6,
        "topic": "Northbound and Southbound APIs",
        "objective": "6.3",
        "video": "Northbound and Southbound APIs",
        "study_topics": ["Northbound/southbound APIs"],
        "body": (
            "<p>SDN controllers sit between the applications that request network services and the "
            "devices that implement them. Two sets of APIs facilitate this communication:</p>"
            "<p><strong>Northbound Interface (NBI):</strong></p>"
            "<ul>"
            "<li>Connects the controller <em>upward</em> to business applications, orchestration "
            "platforms, and network management systems (NMS).</li>"
            "<li>Typically REST-based (HTTP/HTTPS + JSON/XML), enabling any application that can "
            "make HTTP calls to programme the network.</li>"
            "<li>Abstracts low-level device details—an app requests 'create a VPN between sites A "
            "and B' without specifying which commands to run on which router.</li>"
            "<li>Examples: Cisco DNA Center REST API, OpenDaylight REST NBI.</li>"
            "</ul>"
            "<p><strong>Southbound Interface (SBI):</strong></p>"
            "<ul>"
            "<li>Connects the controller <em>downward</em> to network devices (switches, routers, "
            "APs, firewalls).</li>"
            "<li>Carries the actual configuration and forwarding instructions to devices.</li>"
            "<li>Common SBI protocols: <strong>OpenFlow</strong> (open standard, installs flow "
            "entries), <strong>NETCONF</strong> (IETF standard, XML over SSH), "
            "<strong>RESTCONF</strong> (REST-like NETCONF), <strong>OpFlex</strong> (Cisco ACI), "
            "<strong>gRPC/gNMI</strong> (telemetry and config).</li>"
            "<li>Also includes traditional protocols used in hybrid mode: SSH, SNMP.</li>"
            "</ul>"
            "<p>Think of the controller as a translator: applications speak REST (NBI) and devices "
            "speak NETCONF/OpenFlow (SBI). The controller bridges the abstraction gap.</p>"
        ),
        "key_points": [
            "Northbound API (NBI): controller to applications—typically REST/JSON.",
            "Southbound API (SBI): controller to network devices—OpenFlow, NETCONF, RESTCONF, gRPC.",
            "NBI abstracts device complexity so apps can request intent, not commands.",
            "SBI translates controller intent into device-specific configuration.",
            "Common Cisco SBIs: NETCONF (XML/SSH), RESTCONF (HTTP/JSON), OpFlex (ACI).",
        ],
    },
    {
        "domain": 6,
        "topic": "Cisco DNA Center",
        "objective": "6.4",
        "video": "Cisco DNA Center",
        "study_topics": ["Cisco DNA Center"],
        "body": (
            "<p><strong>Cisco DNA Center (Cisco Digital Network Architecture Center)</strong> is "
            "Cisco's centralised network controller and management platform for enterprise "
            "campus and branch networks. It is the controller layer in Cisco SD-Access.</p>"
            "<p><strong>Core functions:</strong></p>"
            "<ul>"
            "<li><strong>Design:</strong> Define network hierarchy (sites, buildings, floors), "
            "IP address pools, wireless SSIDs, and templates.</li>"
            "<li><strong>Policy:</strong> Create group-based access policies using scalable group "
            "tags (SGTs) without touching individual device ACLs.</li>"
            "<li><strong>Provision:</strong> Zero-touch provisioning (ZTP)—devices auto-register, "
            "download configs, and join the fabric automatically.</li>"
            "<li><strong>Assurance:</strong> Real-time analytics using telemetry data to verify "
            "network health, detect issues, and provide root-cause analysis.</li>"
            "</ul>"
            "<p><strong>SD-Access fabric roles:</strong></p>"
            "<ul>"
            "<li><strong>Control plane node:</strong> Runs LISP map-server/resolver; maps endpoint "
            "IDs (MAC/IP) to routing locators (RLOCs).</li>"
            "<li><strong>Border node:</strong> Connects the SD-Access fabric to external networks "
            "(WAN, internet, data centre).</li>"
            "<li><strong>Edge node:</strong> Access layer switch where endpoints connect; performs "
            "VXLAN encapsulation.</li>"
            "</ul>"
            "<p>Cisco DNA Center exposes a <strong>REST API</strong> (northbound) so that external "
            "scripts and orchestration tools can automate design, policy, and provisioning tasks. "
            "It communicates with fabric devices via NETCONF/RESTCONF and traditional CLI "
            "(southbound).</p>"
        ),
        "key_points": [
            "DNA Center is Cisco's SDN controller for enterprise SD-Access deployments.",
            "Four pillars: Design, Policy, Provision (ZTP), and Assurance.",
            "SD-Access uses VXLAN overlay with LISP control plane managed by DNA Center.",
            "Fabric roles: control plane node, border node, edge node.",
            "Exposes a northbound REST API for integration with external automation tools.",
        ],
    },
    {
        "domain": 6,
        "topic": "REST APIs: HTTP Methods, CRUD, Statelessness, and Data Encoding",
        "objective": "6.5",
        "video": "REST APIs",
        "study_topics": [
            "REST APIs (HTTP verbs/CRUD)",
            "REST API HTTP methods mapped to CRUD operations",
            "REST APIs (statelessness/data encoding)",
        ],
        "body": (
            "<p><strong>REST (Representational State Transfer)</strong> is an architectural style "
            "for web APIs built on top of HTTP. RESTful APIs expose resources via URIs and use "
            "standard HTTP methods to perform operations on those resources.</p>"
            "<p><strong>CRUD to HTTP verb mapping:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>CRUD Operation</th><th>HTTP Verb</th><th>Description</th></tr>"
            "<tr><td>Create</td><td>POST</td><td>Submit new resource data to the server</td></tr>"
            "<tr><td>Read</td><td>GET</td><td>Retrieve a resource or list of resources</td></tr>"
            "<tr><td>Update (full)</td><td>PUT</td><td>Replace an existing resource entirely</td></tr>"
            "<tr><td>Update (partial)</td><td>PATCH</td><td>Modify specific fields of a resource</td></tr>"
            "<tr><td>Delete</td><td>DELETE</td><td>Remove a resource from the server</td></tr>"
            "</table>"
            "<p><strong>Common HTTP status codes:</strong></p>"
            "<ul>"
            "<li><strong>200 OK</strong> – Request succeeded (GET, PUT, PATCH, DELETE).</li>"
            "<li><strong>201 Created</strong> – New resource created successfully (POST).</li>"
            "<li><strong>400 Bad Request</strong> – Malformed request syntax or invalid data.</li>"
            "<li><strong>401 Unauthorized</strong> – Authentication required or failed.</li>"
            "<li><strong>403 Forbidden</strong> – Authenticated but not authorised for this resource.</li>"
            "<li><strong>404 Not Found</strong> – Requested resource does not exist.</li>"
            "<li><strong>500 Internal Server Error</strong> – Server-side failure.</li>"
            "</ul>"
            "<p><strong>Statelessness:</strong> Each HTTP request from a client to a REST API must "
            "contain all information needed to process it. The server stores no session state "
            "between requests. Authentication credentials (API key, token) are sent with every "
            "call. This simplifies scalability—any server instance can handle any request.</p>"
            "<p><strong>Data encoding:</strong> REST APIs typically exchange data as "
            "<strong>JSON</strong> (most common, human-readable) or <strong>XML</strong>. The "
            "<code>Content-Type: application/json</code> and <code>Accept: application/json</code> "
            "HTTP headers tell the server and client what format to use. Cisco DNA Center, "
            "RESTCONF, and most modern network APIs default to JSON.</p>"
        ),
        "key_points": [
            "POST=Create, GET=Read, PUT=Update (full), PATCH=Update (partial), DELETE=Delete.",
            "200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Server Error.",
            "REST is stateless: every request is self-contained; no server-side session.",
            "Authentication token or API key must be included in each request header.",
            "Data encoded as JSON (default) or XML; declared via Content-Type/Accept headers.",
            "Resources identified by URIs; HTTP verbs define the action on those resources.",
        ],
    },
    {
        "domain": 6,
        "topic": "Configuration Management Tools: Ansible, Puppet, and Chef",
        "objective": "6.6",
        "video": "Configuration Management",
        "study_topics": ["Configuration management (Ansible/Puppet/Chef)"],
        "body": (
            "<p>Configuration management tools automate the deployment and enforcement of device "
            "and server configurations at scale. Three tools appear on the CCNA exam:</p>"
            "<p><strong>Ansible</strong></p>"
            "<ul>"
            "<li><strong>Agentless:</strong> No software installed on managed devices; connects "
            "via SSH (Linux/network) or WinRM (Windows).</li>"
            "<li><strong>Push model:</strong> The Ansible control node pushes configs to devices "
            "when a playbook is executed.</li>"
            "<li><strong>Language:</strong> YAML playbooks; human-readable, low barrier to entry.</li>"
            "<li><strong>Idempotent:</strong> Running the same playbook multiple times produces "
            "the same result—no unintended changes on subsequent runs.</li>"
            "<li>Most popular choice for network automation due to its agentless simplicity and "
            "extensive Cisco module library (cisco.ios, cisco.nxos).</li>"
            "</ul>"
            "<p><strong>Puppet</strong></p>"
            "<ul>"
            "<li><strong>Agent-based:</strong> A Puppet agent runs on each managed node and "
            "periodically checks in with the Puppet master server.</li>"
            "<li><strong>Pull model:</strong> Agents pull the desired-state catalog from the "
            "master (default every 30 minutes) and apply any necessary changes.</li>"
            "<li><strong>Language:</strong> Puppet DSL (declarative) or Ruby.</li>"
            "<li>Strong at enforcing configuration drift correction over time.</li>"
            "</ul>"
            "<p><strong>Chef</strong></p>"
            "<ul>"
            "<li><strong>Agent-based:</strong> Chef client runs on each node and pulls from the "
            "Chef server.</li>"
            "<li><strong>Pull model:</strong> Similar to Puppet; node runs chef-client to converge "
            "to desired state.</li>"
            "<li><strong>Language:</strong> Ruby-based DSL ('recipes' and 'cookbooks').</li>"
            "<li>Highly flexible but steeper learning curve than Ansible.</li>"
            "</ul>"
            "<p><strong>Quick comparison:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Tool</th><th>Agent</th><th>Model</th><th>Language</th></tr>"
            "<tr><td>Ansible</td><td>Agentless</td><td>Push</td><td>YAML</td></tr>"
            "<tr><td>Puppet</td><td>Agent-based</td><td>Pull</td><td>Puppet DSL</td></tr>"
            "<tr><td>Chef</td><td>Agent-based</td><td>Pull</td><td>Ruby DSL</td></tr>"
            "</table>"
        ),
        "key_points": [
            "Ansible: agentless, push model, YAML playbooks—most common for network automation.",
            "Puppet: agent-based, pull model, Puppet DSL; enforces state every ~30 minutes.",
            "Chef: agent-based, pull model, Ruby DSL (recipes/cookbooks); steepest learning curve.",
            "All three tools are idempotent—repeated runs converge to desired state safely.",
            "Ansible connects via SSH; Puppet and Chef require an agent daemon on each managed node.",
        ],
    },
    {
        "domain": 6,
        "topic": "JSON Data Format and Data Types",
        "objective": "6.7",
        "video": "JSON",
        "study_topics": [
            "JSON data format",
            "JSON data types",
        ],
        "body": (
            "<p><strong>JSON (JavaScript Object Notation)</strong> is a lightweight, text-based "
            "data interchange format widely used in REST APIs, including those from Cisco DNA "
            "Center and RESTCONF. It is human-readable and easy for programs to parse.</p>"
            "<p><strong>JSON structural elements:</strong></p>"
            "<ul>"
            "<li><strong>Object <code>{}</code>:</strong> An unordered collection of key/value "
            "pairs. Keys must be strings enclosed in double quotes. "
            "Example: <code>{\"hostname\": \"R1\", \"version\": 17}</code></li>"
            "<li><strong>Array <code>[]</code>:</strong> An ordered list of values. "
            "Example: <code>[\"Gi0/0\", \"Gi0/1\", \"Gi0/2\"]</code></li>"
            "<li><strong>Nested structures:</strong> Objects can contain arrays and vice versa, "
            "enabling complex hierarchical data.</li>"
            "</ul>"
            "<p><strong>JSON data types:</strong></p>"
            "<ul>"
            "<li><strong>String:</strong> Text in double quotes — <code>\"enabled\"</code></li>"
            "<li><strong>Number:</strong> Integer or floating-point, no quotes — <code>1000</code>, "
            "<code>99.5</code></li>"
            "<li><strong>Boolean:</strong> Lowercase <code>true</code> or <code>false</code></li>"
            "<li><strong>Null:</strong> Represents an absent value — <code>null</code></li>"
            "<li><strong>Object:</strong> <code>{}</code></li>"
            "<li><strong>Array:</strong> <code>[]</code></li>"
            "</ul>"
            "<p><strong>Valid JSON example (network device):</strong></p>"
            "<pre><code>"
            "{\n"
            "  \"device\": {\n"
            "    \"hostname\": \"SW1\",\n"
            "    \"model\": \"C9300\",\n"
            "    \"managed\": true,\n"
            "    \"uptime_days\": 42,\n"
            "    \"interfaces\": [\"Gi1/0/1\", \"Gi1/0/2\"],\n"
            "    \"description\": null\n"
            "  }\n"
            "}"
            "</code></pre>"
            "<p><strong>JSON rules:</strong> Keys are always strings (double-quoted). Strings use "
            "double quotes only (not single). Trailing commas are not allowed. JSON has no "
            "comments. Whitespace (spaces, tabs, newlines) is insignificant outside of strings.</p>"
        ),
        "key_points": [
            "JSON uses objects {} (key/value pairs) and arrays [] (ordered lists).",
            "Six data types: string, number, boolean, null, object, array.",
            "Strings must use double quotes; booleans are lowercase true/false.",
            "No trailing commas, no comments, no single-quoted strings in valid JSON.",
            "JSON is the default encoding for Cisco DNA Center REST API and RESTCONF.",
            "Nested objects and arrays represent hierarchical network configuration data.",
        ],
    },
]
