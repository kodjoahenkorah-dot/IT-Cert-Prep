"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file C.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 3 in
``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Architecture trade-offs (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A game studio is deciding how to provision server capacity for a new "
            "multiplayer title's launch. Owning enough on-premises hardware to "
            "handle the worst-case concurrent-player spike expected on launch day "
            "would sit largely idle for the rest of the year, and the studio's "
            "small infrastructure team would be solely responsible for every "
            "hardware failure and firmware patch on that equipment. Which "
            "trade-off BEST justifies provisioning the launch-day burst capacity "
            "in the public cloud instead of on-premises?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cloud provisioning transfers the risk and operational burden "
                    "of hardware failures and firmware patching to the provider "
                    "and scales elastically to match demand, in exchange for "
                    "ongoing usage-based cost instead of a large upfront capital "
                    "purchase"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the classic risk-transference and "
                    "elasticity trade-off: the provider absorbs hardware failure/"
                    "patching risk and the studio pays only for capacity it "
                    "actually uses, avoiding idle capital investment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "On-premises hardware provides better elasticity, since the "
                    "studio's own team can provision new servers faster than a "
                    "cloud provider's API"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the actual trade-off — cloud "
                    "infrastructure offers rapid, on-demand elasticity through "
                    "provider APIs; provisioning new physical servers in-house is "
                    "comparatively slow."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Moving launch-day capacity to the cloud eliminates the "
                    "studio's security responsibilities entirely, since the "
                    "provider assumes full accountability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Under the shared responsibility model, the "
                    "studio still retains security responsibilities (e.g., "
                    "application configuration, access control) in the cloud; "
                    "using cloud capacity does not eliminate all accountability."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Provisioning on-premises hardware transfers financial and "
                    "operational risk to a third party, reducing the studio's "
                    "liability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the opposite of what happens "
                    "on-premises — owning the hardware keeps all financial and "
                    "operational risk with the studio itself; it is the cloud "
                    "option that transfers this risk to the provider."
                ),
            },
        ],
        "explanation": (
            "Choosing cloud burst capacity over on-premises hardware for a "
            "temporary, unpredictable spike is a textbook risk-transference and "
            "elasticity trade-off: the provider absorbs hardware and patching "
            "risk in exchange for ongoing usage-based cost rather than a large "
            "idle capital investment."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A three-person startup wants to deploy its own custom-written "
            "application code and business logic but has no staff to manage "
            "servers, operating systems, or runtime environments. The team needs "
            "a platform that runs their custom code while completely eliminating "
            "OS and runtime patching responsibility. Which cloud service model "
            "BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Platform as a Service (PaaS)",
                "correct": True,
                "rationale": (
                    "Correct. PaaS lets the customer deploy and run its own "
                    "custom application code while the provider fully manages "
                    "the underlying OS, runtime, and infrastructure — exactly "
                    "matching the need to deploy custom code without any OS/"
                    "runtime management burden."
                ),
            },
            {
                "id": "b",
                "text": "Software as a Service (SaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. SaaS delivers a complete, pre-built application "
                    "with no ability to deploy custom code or business logic, "
                    "which conflicts with the startup's requirement to run its "
                    "own application."
                ),
            },
            {
                "id": "c",
                "text": "Infrastructure as a Service (IaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. IaaS still leaves the customer responsible for "
                    "managing the guest OS, patching, and runtime environment — "
                    "burdens the startup explicitly wants to avoid given it has "
                    "no staff to handle them."
                ),
            },
            {
                "id": "d",
                "text": "Community cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a deployment model based on who "
                    "shares the environment, not a service model, and does not "
                    "by itself resolve who manages the OS and runtime."
                ),
            },
        ],
        "explanation": (
            "PaaS is the only model that both allows deployment of custom "
            "application code and removes OS/runtime management responsibility "
            "from the customer, unlike SaaS (no custom code) or IaaS (customer "
            "still manages the OS)."
        ),
    },
    {
        "id": "nd3c-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A manufacturer's on-premises analytics servers are sized for "
            "average daily telemetry processing. A month-end batch job requires "
            "roughly five times normal compute for about 18 hours; the data "
            "involved is non-sensitive aggregate telemetry already approved for "
            "public cloud processing. Purchasing enough on-premises hardware to "
            "cover this monthly peak would sit idle the rest of the month. Which "
            "architecture BEST addresses this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cloud bursting — temporarily extend the workload to public "
                    "cloud compute during the periodic demand spike while "
                    "keeping normal daily operations on-premises"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cloud bursting is designed precisely for this "
                    "pattern: temporary, predictable spikes are offloaded to "
                    "elastic public cloud capacity, avoiding idle on-premises "
                    "hardware sized for a rare peak."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fully migrate all analytics workloads to the public cloud, "
                    "retiring the on-premises servers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Normal daily processing already runs fine on "
                    "the existing on-premises servers; a full migration is an "
                    "unnecessarily disruptive and costly response to a narrow, "
                    "once-a-month capacity gap."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Permanently expand on-premises hardware capacity to handle "
                    "the month-end peak at all times"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly the capital waste the scenario "
                    "describes — the extra capacity would sit idle roughly 29 "
                    "days out of every month."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Let the month-end batch job run over a longer period on "
                    "the existing on-premises hardware without any additional "
                    "capacity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores the stated business need for the "
                    "batch job to complete at the required 18-hour, 5x-capacity "
                    "level, rather than actually solving the capacity gap."
                ),
            },
        ],
        "explanation": (
            "Cloud bursting is the standard hybrid-cloud pattern for handling "
            "short, predictable demand spikes by temporarily extending to "
            "elastic public cloud capacity, avoiding both idle on-premises "
            "overprovisioning and an unnecessary full migration."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A hospital's bedside infusion pump runs a proprietary real-time "
            "operating system on FDA-cleared hardware. The manufacturer states "
            "that any software modification — including installing a security "
            "agent — voids the device's regulatory clearance and could alter its "
            "life-critical timing behavior. A vulnerability scan finds the "
            "pump's network stack has a known flaw. Which control is MOST "
            "appropriate given these constraints?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Isolate the pump on a dedicated, tightly filtered network "
                    "segment and monitor it with an out-of-band, passive "
                    "OT-aware sensor that observes traffic without sending any "
                    "commands to the device"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Passive, out-of-band monitoring combined with "
                    "network segmentation reduces exposure and provides "
                    "detection without modifying the device's software or "
                    "interfering with its life-critical real-time behavior, "
                    "respecting the FDA clearance constraint."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Install a lightweight endpoint detection and response "
                    "(EDR) agent directly on the pump to actively block "
                    "exploitation attempts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Installing any software agent on the device "
                    "would modify it, voiding its regulatory clearance and "
                    "risking interference with its real-time timing guarantees "
                    "— exactly what the constraint prohibits."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Apply the vendor's general-purpose OS security patch "
                    "immediately, bypassing the FDA recertification process to "
                    "close the flaw faster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bypassing required regulatory recertification "
                    "on a life-critical medical device risks unpredictable, "
                    "unsafe behavior and is not appropriate regardless of "
                    "urgency."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Migrate the pump's control software to a virtualized "
                    "instance running in the hospital's data center for "
                    "centralized patch management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A bedside infusion pump's control logic must "
                    "run locally in real time at the point of care; virtualizing "
                    "it introduces unacceptable latency and availability risk "
                    "for a life-critical function."
                ),
            },
        ],
        "explanation": (
            "For regulatory-locked, unpatchable embedded medical devices, "
            "network segmentation combined with passive, non-intrusive "
            "monitoring is the standard compensating control, since active "
            "agents, unauthorized patching, or migration are unsafe or "
            "infeasible."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IoT security",
        "stem": (
            "A commercial property manager deploys internet-connected smart "
            "door locks that receive firmware updates automatically from the "
            "manufacturer's cloud service. A security review finds the locks "
            "will install any firmware file pushed to them without verifying "
            "its origin, and update traffic travels over the same network "
            "segment used for guest Wi-Fi. Which change BEST reduces the risk "
            "of a malicious firmware update being installed on the locks?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure the locks to accept only cryptographically "
                    "signed firmware verified against the manufacturer's public "
                    "key, and move update traffic to an isolated management "
                    "VLAN separate from guest Wi-Fi"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Signature verification prevents installation of "
                    "unauthorized or tampered firmware, and network isolation "
                    "from guest Wi-Fi removes a low-trust segment as an avenue "
                    "for intercepting or spoofing update traffic — directly "
                    "addressing both identified gaps."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Permanently disable all firmware updates so the locks can "
                    "never receive a malicious file"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This also blocks legitimate security patches "
                    "indefinitely, leaving known vulnerabilities in the current "
                    "firmware unfixed forever — trading one risk for a worse "
                    "one."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require building staff to physically inspect each lock "
                    "monthly for signs of tampering"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical inspection does not scale across many "
                    "locks and cannot detect a remotely delivered malicious "
                    "firmware update, which is the actual risk identified."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rotate the administrative password on each lock's mobile "
                    "app on a quarterly schedule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Password rotation addresses credential-based "
                    "access risk, not the firmware integrity and network-"
                    "isolation gaps that allow an unauthorized firmware push."
                ),
            },
        ],
        "explanation": (
            "Signed-firmware verification paired with network isolation of "
            "update traffic is the standard control for securing IoT devices "
            "against malicious firmware, directly closing the integrity and "
            "exposure gaps identified rather than disabling updates or relying "
            "on non-scalable manual checks."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A SaaS platform runs containers from many mutually untrusted "
            "customers on shared hosts using the default container runtime, "
            "which shares the host kernel with every container. The security "
            "team wants stronger isolation between tenant containers and the "
            "host kernel than the default runtime provides, without the cost "
            "and overhead of giving each tenant a dedicated virtual machine. "
            "Which approach BEST meets this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Use a sandboxed container runtime (e.g., a gVisor- or "
                    "Kata Containers-style microVM/user-space kernel) that "
                    "intercepts and isolates system calls between each "
                    "container and the host kernel"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Sandboxed runtimes insert an additional isolation "
                    "layer between the container and the host kernel, "
                    "meaningfully reducing kernel-level attack surface between "
                    "tenants without the full overhead of dedicating a separate "
                    "VM to each one."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Continue using the default container runtime but add a "
                    "web application firewall in front of each container"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF filters application-layer HTTP traffic; "
                    "it does nothing to isolate a container's system calls "
                    "from the shared host kernel, which is the actual risk "
                    "described."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Assign each tenant's containers to a dedicated physical "
                    "host with no other tenants present"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This does provide strong isolation, but it "
                    "reintroduces the per-tenant hardware cost and overhead the "
                    "requirement explicitly says to avoid."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Run all tenant containers under a single shared "
                    "root-privileged process to simplify resource management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Running containers with shared root privileges "
                    "weakens isolation further and increases the impact of any "
                    "single container compromise — the opposite of the stated "
                    "goal."
                ),
            },
        ],
        "explanation": (
            "Sandboxed/microVM container runtimes are purpose-built to add a "
            "kernel isolation layer between mutually untrusted containers and "
            "the host without the cost of dedicated per-tenant hardware, unlike "
            "WAFs, which address a different traffic layer, or dedicated hosts, "
            "which are cost-prohibitive at scale."
        ),
    },
    {
        "id": "nd3c-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Microservices and containerization",
        "stem": (
            "Operations engineers routinely SSH into running production "
            "containers to install packages and apply hotfixes directly. When "
            "containers restart or are rescheduled by the orchestrator, they "
            "revert to the original container image, silently losing every "
            "hotfix that was applied this way and reintroducing previously "
            "fixed issues. Which practice BEST resolves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Treat containers as immutable: rebuild the container "
                    "image with the fix included and redeploy it, rather than "
                    "modifying a running container in place"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Immutable infrastructure ensures every deployed "
                    "instance is built from a versioned, reproducible image, so "
                    "fixes persist across restarts and rescheduling instead of "
                    "being silently lost — directly resolving the described "
                    "drift."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the orchestrator's container restart threshold so "
                    "containers are rescheduled less frequently"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This only delays when the drift is lost, rather "
                    "than fixing the underlying practice of patching running "
                    "containers in place; the fix will still disappear "
                    "eventually."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Grant engineers persistent root SSH access to all "
                    "production containers to make future hotfixes faster to "
                    "apply"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This formalizes and expands the very practice "
                    "causing the problem, increasing both configuration drift "
                    "risk and the attack surface of production containers."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Store a manual log of every hotfix applied via SSH so it "
                    "can be reapplied after each restart"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This treats the symptom rather than the cause, "
                    "requiring ongoing manual reapplication instead of making "
                    "the fix a permanent part of the deployed artifact."
                ),
            },
        ],
        "explanation": (
            "Immutable infrastructure — rebuilding and redeploying versioned "
            "images rather than patching running containers in place — is the "
            "standard container practice that prevents configuration drift and "
            "silent loss of fixes across restarts."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A serverless function accepts a user-supplied URL and fetches its "
            "content on the function's behalf to generate a link preview. A "
            "penetration test shows that submitting the cloud provider's "
            "internal metadata service address as the 'URL' causes the "
            "function to return the temporary credentials assigned to its "
            "execution role. Which combination of controls BEST mitigates this "
            "specific server-side request forgery (SSRF) risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require the token-bound (session-oriented) version of the "
                    "instance/function metadata service that rejects simple "
                    "unauthenticated requests, and restrict the function's "
                    "outbound network calls to an explicit allowlist of "
                    "external domains"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A session-oriented metadata service (such as a "
                    "token-required version) prevents a simple crafted request "
                    "from retrieving credentials, and an egress allowlist stops "
                    "the function from ever being able to reach the internal "
                    "metadata address at all, closing both layers of this SSRF "
                    "path."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the function's memory allocation so it can "
                    "validate URLs more thoroughly before fetching them"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Memory allocation has no bearing on SSRF risk; "
                    "the vulnerability is about unrestricted outbound requests "
                    "and metadata service access, not compute resources."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rotate the function's execution role credentials on a "
                    "weekly schedule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rotating credentials on a schedule does not "
                    "prevent an attacker from retrieving and using the "
                    "currently valid credentials via the same SSRF path before "
                    "the next rotation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the function's execution timeout to allow the "
                    "URL fetch to complete without errors"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Execution timeout is unrelated to which "
                    "destinations the function is permitted to reach and does "
                    "nothing to prevent SSRF to the internal metadata service."
                ),
            },
        ],
        "explanation": (
            "Mitigating SSRF against cloud metadata services requires both "
            "hardening the metadata service itself against simple "
            "unauthenticated requests and restricting the function's outbound "
            "network reach — resource, timeout, and rotation settings do not "
            "address the actual request-forgery path."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "A cloud hosting provider's multi-tenant virtualization platform "
            "has two findings from a security assessment: (1) a single "
            "tenant's runaway workload can consume enough shared CPU and I/O "
            "capacity to degrade performance for every other VM on the same "
            "host, and (2) the hypervisor management interface has several "
            "legacy virtual devices and remote management services enabled "
            "that no current workload uses. Which TWO changes would MOST "
            "directly remediate these two specific findings, respectively? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure resource reservations, limits, and shares "
                    "(quality-of-service controls) on each VM to cap how much "
                    "shared CPU/I/O capacity any single tenant can consume"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Enforcing per-VM resource limits directly "
                    "prevents a single runaway workload from starving other "
                    "tenants of shared capacity — remediating the first "
                    "finding."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Disable unused legacy virtual devices and unnecessary "
                    "hypervisor management services/interfaces to reduce the "
                    "hypervisor's attack surface"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing unused virtual devices and management "
                    "services directly shrinks the exposed hypervisor attack "
                    "surface described in the second finding."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the host's memory and CPU overcommit ratios to "
                    "allow more VMs to be packed per host"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Increasing overcommit ratios worsens resource "
                    "contention risk between tenants rather than addressing "
                    "the noisy-neighbor finding, and it does not touch the "
                    "hypervisor attack-surface finding at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Convert all physical servers in the fleet to virtual "
                    "machines (P2V) to standardize the environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. P2V conversion is a migration activity "
                    "unrelated to either resource contention between existing "
                    "tenants or reducing the hypervisor's exposed management "
                    "surface."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Enable nested virtualization on every host so customers "
                    "can run their own hypervisors inside their VMs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Nested virtualization adds functionality and "
                    "attack surface rather than reducing it, and does not "
                    "address resource contention between tenants."
                ),
            },
        ],
        "explanation": (
            "Per-VM resource QoS controls directly stop one tenant's workload "
            "from starving others, while disabling unused hypervisor devices "
            "and management services directly shrinks the exposed management "
            "attack surface — overcommit ratios, P2V conversion, and nested "
            "virtualization address neither finding."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-010",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "An external vulnerability scan of a company's internet-facing IP "
            "range finds: RDP (port 3389) open directly to the internet on "
            "three servers, an SNMP service still responding using the default "
            "'public' community string, and a VPN gateway provisioned for a "
            "vendor project that ended eight months ago still actively "
            "accepting connections. Which action MOST directly reduces the "
            "attack surface exposed by these findings?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove direct internet access to RDP by routing it "
                    "through a VPN or jump host, change or disable the default "
                    "SNMP community string, and decommission the unused VPN "
                    "gateway"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Each action eliminates or closes an unnecessary "
                    "internet-facing entry point entirely, which is the "
                    "definition of reducing attack surface, rather than adding "
                    "monitoring or authentication around exposure that remains "
                    "open."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy an intrusion detection system to monitor traffic "
                    "to all three exposed services without changing their "
                    "configuration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Monitoring can help detect misuse of these "
                    "exposed services but does not eliminate any of the "
                    "unnecessary internet-facing entry points themselves."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require multifactor authentication for RDP logins while "
                    "leaving RDP reachable directly from the internet"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding authentication strengthens access "
                    "control to a service that remains exposed, but it does "
                    "not remove the internet-facing exposure itself, and RDP "
                    "remains a frequent target for exploitation independent of "
                    "login credentials."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enable verbose logging on the SNMP service so future "
                    "misuse attempts are recorded"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Logging documents activity after the fact but "
                    "does not close the default-credential exposure or reduce "
                    "the number of unnecessary services reachable from the "
                    "internet."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means eliminating unnecessary exposed "
            "services and stale infrastructure entirely — closing "
            "internet-facing RDP, fixing the default SNMP credential, and "
            "decommissioning the unused VPN gateway — not merely monitoring or "
            "authenticating in front of exposure that remains."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management workflow",
        "stem": (
            "A change advisory board approved and scheduled a database schema "
            "migration. During implementation the migration caused unexpected "
            "application errors, and because the change request did not "
            "include a documented rollback procedure, engineers spent six "
            "hours manually reverse-engineering the previous schema to restore "
            "service. Which change management element, if enforced as a "
            "mandatory part of every change request, would have MOST reduced "
            "this recovery time?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A documented and pre-tested rollback/backout plan "
                    "required as part of every change request before approval"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A tested, documented rollback plan lets the team "
                    "revert quickly to the known-good prior state as soon as a "
                    "change causes problems, directly addressing the six-hour "
                    "manual reconstruction described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A more diverse set of voting members on the change "
                    "advisory board"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Board composition affects the quality of the "
                    "approval decision, but it does not provide the team with "
                    "a faster path to recovery once a problem occurs during "
                    "implementation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Scheduling all changes only during pre-approved "
                    "maintenance windows"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Maintenance windows control when a change "
                    "occurs, not how quickly the team can recover if the "
                    "change fails, which is the specific gap described."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Requiring every change ticket to be digitally signed by "
                    "the requester"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Digital signatures verify who requested a "
                    "change; they have no effect on the team's ability to "
                    "reverse a change that has already caused an outage."
                ),
            },
        ],
        "explanation": (
            "A mandatory, pre-tested rollback/backout plan is the change "
            "management element specifically designed to enable rapid recovery "
            "when an approved change causes unexpected problems, unlike board "
            "composition, scheduling windows, or ticket signing, which address "
            "different aspects of the process."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "A chemical plant's safety instrumented system (SIS) network "
            "firewall sits between the control network and the actuators that "
            "open and close critical process valves. Policy states that no "
            "unauthorized or unverified command may ever reach an actuator, "
            "even if that means halting remote monitoring capability, because "
            "an uncommanded or unauthorized actuation could cause a "
            "life-safety incident. How should this firewall's failure mode be "
            "configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Fail-closed, blocking all command traffic to the "
                    "actuators if the firewall fails"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Fail-closed ensures that if the firewall fails, "
                    "no unauthorized or unverified commands can reach the "
                    "actuators, matching the stated priority that preventing "
                    "uncommanded actuation outweighs the loss of remote "
                    "monitoring."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fail-open, allowing command traffic to continue passing "
                    "if the firewall fails, to preserve remote monitoring "
                    "visibility"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open would allow unauthenticated or "
                    "unverified commands to reach the actuators during a "
                    "device failure, directly violating the stated "
                    "zero-tolerance policy for unauthorized actuation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Active-active clustering of two firewalls to eliminate "
                    "any single point of failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a high-availability design choice, not "
                    "a failure-mode setting, and does not by itself define how "
                    "a single device should behave if it fails."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Passive/tap mode so the firewall only monitors actuator "
                    "traffic without ever blocking it"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Passive monitoring removes the device's "
                    "ability to block unauthorized commands at all times, not "
                    "just during a failure, which contradicts the requirement "
                    "to prevent unauthorized actuation."
                ),
            },
        ],
        "explanation": (
            "When preventing unauthorized or unverified commands outweighs "
            "the value of continuous monitoring, an inline control protecting "
            "life-safety actuators should be configured fail-closed, the "
            "opposite priority from availability-focused systems."
        ),
    },
    {
        "id": "nd3c-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Failure modes",
        "stem": (
            "A public weather-data API gateway calls an internal "
            "authentication service to check for premium-tier rate limits "
            "before serving requests. The underlying weather data itself is "
            "free, public, non-sensitive information. During an outage of the "
            "authentication service, should the gateway fail-open or "
            "fail-closed, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Fail-open, continuing to serve the public, non-sensitive "
                    "data at the default free-tier rate limit, since "
                    "availability of non-sensitive public data outweighs the "
                    "risk of temporarily unenforced premium rate limits"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the data is public and non-sensitive, "
                    "the risk of briefly under-enforcing rate limits is low, "
                    "while blocking all requests would needlessly deny access "
                    "to information that carries no confidentiality or "
                    "integrity risk — fail-open is the appropriate choice "
                    "here."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fail-closed, blocking all API requests until the "
                    "authentication service is restored, to guarantee rate "
                    "limits are always enforced"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking access to public, non-sensitive data "
                    "entirely to protect a rate-limiting function is a "
                    "disproportionate response; the data itself carries no "
                    "confidentiality risk that would justify halting "
                    "availability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Fail-open, but only for requests originating from the "
                    "company's own internal network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This restricts fail-open behavior based on "
                    "network origin for reasons unrelated to the scenario, "
                    "unnecessarily limiting availability of already-public "
                    "data with no confidentiality benefit."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Fail-closed for read requests but fail-open for write "
                    "requests"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This scenario describes a read-only public "
                    "data API with no write operations; this distinction is "
                    "not applicable and does not address the actual "
                    "availability-versus-rate-limit trade-off described."
                ),
            },
        ],
        "explanation": (
            "For a public, non-sensitive data service, fail-open is "
            "appropriate when the dependency being lost (rate-limit "
            "enforcement) carries far less risk than denying availability "
            "altogether — the opposite priority from a system protecting "
            "confidential or life-safety functions."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A company's forward proxy performs TLS decryption and inspection "
            "on all outbound HTTPS traffic to scan for malware and data "
            "exfiltration. After deployment, a partner-integrated mobile app "
            "that uses certificate pinning begins failing to connect, because "
            "the proxy's re-signed certificate does not match the certificate "
            "the app expects. Which change BEST resolves this while preserving "
            "TLS inspection for all other outbound traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Add an explicit bypass/exemption rule on the proxy for "
                    "the pinned app's specific destination domain(s), allowing "
                    "that traffic to pass through without decryption while all "
                    "other outbound HTTPS continues to be inspected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A targeted bypass rule resolves the pinning "
                    "conflict for only the affected destination while leaving "
                    "TLS inspection intact for everything else, matching both "
                    "goals in the requirement."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Disable TLS inspection on the proxy for all outbound "
                    "traffic company-wide"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a disproportionate response that "
                    "eliminates inspection of all other outbound HTTPS traffic "
                    "to fix a conflict affecting only one specific pinned app."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Instruct users to manually install and trust the proxy's "
                    "certificate authority on their mobile devices"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate pinning checks the exact "
                    "certificate or public key the app expects, bypassing the "
                    "device's general trust store entirely, so installing the "
                    "proxy's CA certificate does not resolve a pinning "
                    "failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Replace the partner's mobile app with a browser-based "
                    "alternative to avoid certificate pinning"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a technical fix under the "
                    "security team's control and depends on a decision by the "
                    "partner and the business, rather than resolving the proxy "
                    "configuration conflict directly."
                ),
            },
        ],
        "explanation": (
            "Certificate pinning conflicts with TLS-decrypting proxies are "
            "resolved with a targeted bypass/exemption for the specific "
            "pinned destination, preserving inspection everywhere else, rather "
            "than disabling inspection broadly or attempting device-level "
            "trust changes that pinning specifically defeats."
        ),
    },
    {
        "id": "nd3c-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A security team notices employees using a peer-to-peer "
            "file-sharing application that dynamically negotiates random, "
            "non-standard ports to evade the perimeter stateful firewall's "
            "port-based blocking rules. Which upgrade would MOST effectively "
            "allow the team to block this application regardless of which "
            "port it uses?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy a next-generation firewall (NGFW) with "
                    "application identification (Layer 7 awareness) to detect "
                    "and block the application by its traffic signature rather "
                    "than by port number"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Application identification inspects traffic "
                    "content and behavior to recognize the specific "
                    "application regardless of the port it uses, directly "
                    "solving the port-hopping evasion problem a stateful "
                    "firewall cannot address."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Continually add new explicit deny rules for each "
                    "additional port as it is discovered in use"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a reactive approach that the "
                    "application will continue to evade simply by negotiating "
                    "yet another port, since the firewall is still filtering "
                    "by port number rather than application identity."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the stateful firewall's connection table size "
                    "to track more simultaneous sessions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Connection table size affects how many "
                    "sessions the firewall can track, not its ability to "
                    "identify which application is generating a given "
                    "session."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Extend the firewall's session keepalive timeout to hold "
                    "connections open longer for analysis"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Keepalive timeout controls how long idle "
                    "sessions remain open; it has no bearing on the firewall's "
                    "ability to identify the application generating the "
                    "traffic."
                ),
            },
        ],
        "explanation": (
            "Only Layer 7 application identification, a defining NGFW "
            "capability, can recognize and block an application by its "
            "traffic signature independent of the specific port it "
            "negotiates — port-based rules and stateful tracking cannot keep "
            "pace with dynamic port evasion."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company is deploying threat-detection sensors for the first "
            "time and wants to observe and tune detection rules for 90 days "
            "before allowing the system to automatically block any traffic, to "
            "avoid disrupting production traffic with false positives during "
            "that tuning period. Which deployment approach BEST satisfies this "
            "need for the initial 90 days?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy the sensor out-of-band via a network tap or SPAN "
                    "port as a passive intrusion detection system (IDS) that "
                    "alerts but does not block, then transition to an inline "
                    "intrusion prevention system (IPS) after the tuning period"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A passive, out-of-band IDS deployment observes "
                    "and generates alerts on traffic without ever being "
                    "positioned to block it, exactly matching the requirement "
                    "to tune detection safely before any automatic blocking "
                    "begins."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy the sensor inline immediately in blocking (IPS) "
                    "mode with all default signatures enabled"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Immediately enabling inline blocking with "
                    "untuned default signatures risks exactly the kind of "
                    "false-positive-driven production disruption the "
                    "requirement is trying to avoid."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy the sensor inline but configure it to fail-open if "
                    "it becomes overloaded"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is still an inline, actively blocking "
                    "deployment during the tuning window and does not address "
                    "the stated need to observe traffic without any risk of "
                    "blocking production flow."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Deploy the sensor inline in blocking mode, but only "
                    "during off-peak overnight hours"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This still actively blocks live traffic during "
                    "the stated tuning period, just on a schedule, rather than "
                    "using a genuinely passive, alert-only deployment as "
                    "required."
                ),
            },
        ],
        "explanation": (
            "A passive, out-of-band IDS deployment (via tap or SPAN) is the "
            "standard way to observe and tune detection without any risk of "
            "blocking legitimate traffic, before later transitioning to an "
            "inline, actively blocking IPS once confidence in the tuning is "
            "established."
        ),
    },
    {
        "id": "nd3c-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Network appliances",
        "stem": (
            "A SOC currently has almost no visibility into internal network "
            "activity: it cannot copy traffic to its sensors without affecting "
            "production packet flow, and it cannot see inside encrypted "
            "outbound sessions at all. Leadership wants two additions: (1) a "
            "way to copy 100% of traffic to sensors without impacting "
            "production traffic flow, and (2) a way to inspect the contents "
            "of outbound HTTPS sessions for malware and data exfiltration. "
            "Which TWO appliances, respectively, satisfy these two needs? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A dedicated network TAP (test access point), which "
                    "passively copies all traffic at the physical layer "
                    "independent of production switch load"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A TAP is purpose-built to duplicate 100% of "
                    "traffic for monitoring without ever affecting the "
                    "production traffic flow it copies — satisfying the first "
                    "need."
                ),
            },
            {
                "id": "b",
                "text": (
                    "An SSL/TLS-decrypting forward proxy, which decrypts, "
                    "inspects, and re-encrypts outbound HTTPS sessions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A decrypting forward proxy is purpose-built to "
                    "expose the contents of encrypted outbound sessions to "
                    "inspection tools before re-encrypting and forwarding the "
                    "traffic — satisfying the second need."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A load balancer, distributing traffic across multiple "
                    "backend servers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer's purpose is traffic "
                    "distribution for availability and performance; it neither "
                    "passively copies traffic for monitoring nor decrypts "
                    "sessions for inspection."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A web application firewall (WAF), protecting a "
                    "public-facing web application from inbound attacks"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF inspects inbound requests to a specific "
                    "web application; it does not provide general visibility "
                    "into outbound internal traffic or passive full-traffic "
                    "copying."
                ),
            },
            {
                "id": "e",
                "text": (
                    "A NAT gateway, translating internal private addresses to "
                    "public addresses for outbound connections"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A NAT gateway only translates addresses; it "
                    "provides no traffic-copying or content-inspection "
                    "capability."
                ),
            },
        ],
        "explanation": (
            "A network TAP provides lossless, non-intrusive full traffic "
            "copying, while a decrypting forward proxy exposes encrypted "
            "session contents to inspection — together closing both "
            "visibility gaps, unlike load balancers, WAFs, or NAT gateways, "
            "which serve unrelated purposes."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "An employee connects an unauthorized personal wireless router to "
            "an office wall jack. The device begins answering DHCP requests "
            "from other users on the segment, handing out an "
            "attacker-controlled default gateway address and enabling "
            "on-path interception of their traffic. Which switch-level "
            "control is BEST suited to prevent this specific attack going "
            "forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "DHCP snooping, configured to trust only the switch ports "
                    "connected to the legitimate DHCP server and to drop DHCP "
                    "server responses (offers) arriving from any other port"
                ),
                "correct": True,
                "rationale": (
                    "Correct. DHCP snooping is specifically designed to "
                    "distinguish trusted DHCP server ports from untrusted "
                    "access ports and discard rogue DHCP server traffic, "
                    "directly preventing an unauthorized device from handing "
                    "out a malicious gateway address."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Port security limiting each access port to a small, "
                    "fixed number of learned MAC addresses"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MAC address limiting controls how many "
                    "devices can use a port; it does not evaluate or block the "
                    "content of DHCP traffic, so a single rogue router within "
                    "the allowed MAC count would still be able to answer DHCP "
                    "requests."
                ),
            },
            {
                "id": "c",
                "text": "802.1X port-based authentication using EAP-TLS certificates",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X authenticates a device's identity "
                    "before granting network access, but it does not inspect "
                    "or filter DHCP server traffic from a device that has "
                    "already been granted access to the port."
                ),
            },
            {
                "id": "d",
                "text": (
                    "STP BPDU Guard, disabling a port that receives "
                    "unexpected spanning-tree bridge protocol data units"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. BPDU Guard protects against Layer 2 topology "
                    "loops caused by unauthorized switches; it does not detect "
                    "or block rogue DHCP server responses, which is an "
                    "unrelated attack type."
                ),
            },
        ],
        "explanation": (
            "DHCP snooping is the switch feature purpose-built to distinguish "
            "legitimate DHCP server traffic from rogue DHCP responses, "
            "directly stopping this specific attack — unlike MAC limiting, "
            "802.1X authentication, or BPDU Guard, which address different "
            "threats."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A cloud-native web tier runs in an auto-scaling group where "
            "instances are constantly created and terminated, each receiving "
            "a new, unpredictable IP address. Traditional IP-address-based "
            "firewall rules become outdated within minutes and cannot "
            "reliably enforce which services this tier is allowed to talk to. "
            "Which segmentation approach BEST solves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Software-defined micro-segmentation policies based on "
                    "workload identity or resource tags that follow each "
                    "instance regardless of its assigned IP address, "
                    "dynamically enforced by the SDN or cloud-native firewall"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tag- or identity-based policies bind enforcement "
                    "to what the workload is, not what IP address it happens "
                    "to hold at a given moment, so the policy remains accurate "
                    "even as instances are constantly recycled with new "
                    "addresses."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Static IP-address-based firewall rules, manually updated "
                    "each time an instance is created or terminated"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly the unsustainable, "
                    "constantly-outdated approach the scenario describes as "
                    "the current problem, and it does not scale with "
                    "instances churning within minutes."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A single flat network with no segmentation, relying only "
                    "on the application's own authentication logic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Removing network segmentation entirely "
                    "eliminates a layer of defense and does not solve the "
                    "underlying problem of enforcing policy against a moving "
                    "target of IP addresses — it simply gives up on "
                    "network-level controls."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DNS-based access control, allowing traffic only from "
                    "hostnames that resolve at policy-creation time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static DNS-resolved rules face the same "
                    "staleness problem as static IP rules once addresses "
                    "behind those hostnames change with instance churn, and "
                    "DNS resolution can also be manipulated or cached "
                    "inconsistently."
                ),
            },
        ],
        "explanation": (
            "Tag- or identity-based micro-segmentation is the standard SDN "
            "pattern for enforcing policy against ephemeral, "
            "constantly-changing IP addresses in auto-scaling environments, "
            "unlike static IP or DNS-based rules, which cannot keep pace with "
            "the churn."
        ),
    },
    {
        "id": "nd3c-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A company uses VXLAN overlay tunnels to stretch a single "
            "tenant's Layer 2 segment between two data centers, with the "
            "underlying VXLAN traffic transiting a shared provider's MPLS "
            "network between sites. A security review notes that VXLAN "
            "encapsulation provides logical segmentation but does not encrypt "
            "the payload, so tenant traffic crosses the shared provider "
            "network in cleartext. Which control BEST addresses this specific "
            "gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Encrypt the underlying links carrying the VXLAN traffic "
                    "using MACsec (Layer 2) or an IPSec tunnel over the "
                    "underlay, in addition to the existing VXLAN segmentation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because VXLAN itself only provides logical "
                    "segmentation and encapsulation, not encryption, adding "
                    "MACsec or IPSec on the underlying transport is required "
                    "to actually encrypt the tenant traffic as it crosses the "
                    "shared provider network."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Add more VXLAN network identifiers (VNIs) to further "
                    "segment the tenant's traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding more VNIs only creates additional "
                    "logical segments; it still does nothing to encrypt the "
                    "payload data crossing the shared provider network, which "
                    "is the actual gap identified."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the VXLAN tunnel's maximum transmission unit "
                    "(MTU) to reduce fragmentation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MTU size affects packet fragmentation and "
                    "performance, not confidentiality; it has no bearing on "
                    "whether the payload is encrypted."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Migrate from VXLAN to traditional 802.1Q VLAN trunking "
                    "between the two sites"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Traditional VLAN trunking does not natively "
                    "span separate data centers over an IP/MPLS underlay the "
                    "way VXLAN does, and it would provide no encryption "
                    "either, failing to solve the stated problem while also "
                    "removing the overlay capability the design relies on."
                ),
            },
        ],
        "explanation": (
            "VXLAN provides logical segmentation, not confidentiality; when "
            "its traffic crosses an untrusted or shared underlay network, an "
            "additional encryption control such as MACsec or IPSec on the "
            "underlying links is required to protect the payload in transit."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A company wants its VPN and TLS sessions configured so that if "
            "an attacker records encrypted traffic today and later steals the "
            "server's long-term private key, the attacker still cannot "
            "decrypt any of the previously captured sessions. Which "
            "cryptographic configuration BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Use ephemeral Diffie-Hellman key exchange (DHE or "
                    "ECDHE) to negotiate a unique session key for each "
                    "session, providing perfect forward secrecy"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ephemeral key exchange generates a new, "
                    "temporary session key for every session that is never "
                    "derived solely from the long-term private key, so a "
                    "future compromise of that key cannot be used to decrypt "
                    "previously captured sessions — the definition of perfect "
                    "forward secrecy."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Use static RSA key exchange, where the session key is "
                    "encrypted using the server's long-term public key"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. With static RSA key exchange, every session "
                    "key is protected only by the same long-term private key; "
                    "compromising that key later lets an attacker decrypt any "
                    "previously recorded session, which is exactly the risk "
                    "the requirement wants to avoid."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the RSA key size used for the server's "
                    "long-term certificate from 2048 to 4096 bits"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A larger long-term key makes that key itself "
                    "harder to brute-force, but it does not change the fact "
                    "that, under static key exchange, compromising it "
                    "retroactively exposes all past sessions — it does not "
                    "provide forward secrecy."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Extend the TLS session resumption ticket lifetime so "
                    "fewer full handshakes are required"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Longer resumption ticket lifetimes reduce "
                    "handshake overhead but have no bearing on whether past "
                    "session traffic can be decrypted after a future key "
                    "compromise."
                ),
            },
        ],
        "explanation": (
            "Perfect forward secrecy specifically requires ephemeral key "
            "exchange (DHE/ECDHE) so that session keys are never solely "
            "derivable from the long-term private key, unlike static RSA key "
            "exchange, larger key sizes, or session ticket lifetime settings, "
            "none of which prevent retroactive decryption."
        ),
    },
    {
        "id": "nd3c-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A utility company's battery-powered field sensors need VPN "
            "connectivity back to a central collector over intermittent "
            "cellular links. The sensors have very limited CPU and battery "
            "capacity, and the connection frequently drops and must reconnect "
            "quickly without a costly full renegotiation each time. Which VPN "
            "approach is MOST appropriate for these resource-constrained, "
            "intermittently connected devices?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A lightweight, modern VPN protocol (such as a "
                    "WireGuard-style implementation) using a small, efficient "
                    "cryptographic codebase designed for fast reconnection and "
                    "minimal CPU/battery overhead"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Lightweight modern VPN protocols are "
                    "specifically designed with a minimal codebase and "
                    "efficient cryptographic handshake for fast reconnection "
                    "with low CPU and battery impact — matching the sensors' "
                    "constraints exactly."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A full IPSec/IKEv2 stack with the complete standard "
                    "cipher suite negotiation process"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IPSec's full negotiation and larger protocol "
                    "stack impose more CPU and reconnection overhead than the "
                    "constrained battery-powered sensors can efficiently "
                    "sustain across frequent intermittent reconnects."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A browser-based clientless SSL VPN portal requiring "
                    "manual user login for each session"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Clientless portal-based VPNs are designed for "
                    "interactive human users logging in through a browser, not "
                    "for unattended, automated field sensors reconnecting "
                    "without user interaction."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A GRE tunnel without any encryption to minimize "
                    "processing overhead"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While GRE alone has minimal overhead, it "
                    "provides no encryption at all, failing to protect the "
                    "confidentiality of the sensor data — a VPN requirement "
                    "the scenario clearly implies."
                ),
            },
        ],
        "explanation": (
            "Lightweight, modern VPN protocols built for a small "
            "cryptographic footprint and fast reconnection are the "
            "appropriate choice for resource- and battery-constrained field "
            "devices on intermittent links, unlike heavier IPSec negotiation, "
            "human-interactive clientless portals, or unencrypted GRE "
            "tunnels."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "As part of a Zero Trust redesign, a security architect finds "
            "that database administrators hold standing, always-on elevated "
            "privileges to production systems, regardless of whether they are "
            "actively performing maintenance. Which change BEST aligns this "
            "access model with Zero Trust principles?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace standing privileges with just-in-time (JIT), "
                    "time-bound privilege elevation that must be requested and "
                    "approved for each specific task, automatically expiring "
                    "afterward"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Zero Trust rejects implicit, standing trust in "
                    "favor of granting the minimum necessary access only when "
                    "and for as long as it is needed; just-in-time elevation "
                    "directly replaces always-on privilege with per-task, "
                    "time-bound access."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Require the DBAs to use a stronger password policy for "
                    "their existing standing administrative accounts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Strengthening passwords improves credential "
                    "security but does nothing to reduce the underlying "
                    "problem of privileges being granted at all times "
                    "regardless of need, which is what Zero Trust's "
                    "least-privilege principle targets."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Consolidate all DBA accounts into a single shared "
                    "administrative account to simplify access reviews"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A shared account both increases standing "
                    "access exposure and destroys individual accountability, "
                    "directly contradicting Zero Trust's requirements for "
                    "continuous, per-identity verification."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Grant DBAs standing access to a broader set of systems "
                    "so they do not need to request access repeatedly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This expands, rather than reduces, always-on "
                    "standing privilege — the opposite of the least-privilege, "
                    "minimize-implicit-trust direction a Zero Trust redesign "
                    "requires."
                ),
            },
        ],
        "explanation": (
            "Zero Trust replaces implicit, standing trust with "
            "least-privilege, just-in-time access granted only for the "
            "duration a task requires, unlike password strengthening, account "
            "consolidation, or broadening standing access, none of which "
            "reduce persistent privilege exposure."
        ),
    },
    {
        "id": "nd3c-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "Remote employees currently connect via VPN to a central data "
            "center hub, and all of their internet-bound traffic — including "
            "everyday SaaS traffic like email and collaboration tools — is "
            "backhauled through the hub's security stack before reaching the "
            "internet, adding significant latency. Which architecture change, "
            "consistent with SASE principles, would BEST reduce this latency "
            "while still enforcing consistent security policy?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Adopt a SASE model that enforces security policy via "
                    "cloud-delivered security service edge (SSE) functions "
                    "close to each user's location, enabling local internet "
                    "breakout without backhauling through the central data "
                    "center hub"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SASE's cloud-delivered security functions apply "
                    "consistent policy near the user's point of access, "
                    "eliminating the need to route traffic back through a "
                    "central hub and directly reducing the latency caused by "
                    "that backhaul (a 'trombone' routing pattern)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the bandwidth of the MPLS circuits connecting "
                    "each branch to the central data center hub"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More bandwidth can relieve congestion but does "
                    "not eliminate the fundamental latency penalty of routing "
                    "every packet through a distant central hub before it "
                    "reaches the internet."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Continue routing all traffic through the central VPN "
                    "hub, but disable security inspection to speed up "
                    "processing"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This removes security enforcement to gain "
                    "speed rather than fixing the routing inefficiency, "
                    "undermining the stated requirement to maintain consistent "
                    "security policy."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure a split-tunnel VPN that sends all traffic, "
                    "including SaaS traffic, directly to the internet with no "
                    "inspection at all"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Sending traffic to the internet with no "
                    "inspection at all improves latency but abandons "
                    "consistent security policy enforcement entirely, failing "
                    "half of the stated requirement."
                ),
            },
        ],
        "explanation": (
            "SASE's distributed, cloud-delivered security service edge "
            "removes the need to backhaul all traffic through a central hub, "
            "cutting latency while still applying consistent policy — unlike "
            "simply adding bandwidth, disabling inspection, or removing "
            "inspection through an uninspected split tunnel."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-025",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification",
        "stem": (
            "A defense contractor classifies data using the labels Public, "
            "Sensitive, Proprietary, and Export-Controlled. A set of "
            "engineering drawings describes a component subject to U.S. "
            "export control regulations (ITAR); disclosing the drawings to "
            "non-U.S. persons without a government license is a federal "
            "offense, regardless of how commercially sensitive the drawings "
            "are otherwise. Which classification should these drawings "
            "receive?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Export-Controlled",
                "correct": True,
                "rationale": (
                    "Correct. Export-Controlled is the classification "
                    "specifically reserved for data subject to legal export "
                    "restrictions like ITAR, where disclosure to unauthorized "
                    "foreign persons carries regulatory and criminal "
                    "consequences beyond ordinary business sensitivity."
                ),
            },
            {
                "id": "b",
                "text": "Proprietary",
                "correct": False,
                "rationale": (
                    "Incorrect. Proprietary typically denotes business-"
                    "sensitive trade secrets protected for competitive "
                    "reasons; it does not capture the distinct legal "
                    "export-licensing restrictions that apply to "
                    "ITAR-controlled technical data."
                ),
            },
            {
                "id": "c",
                "text": "Sensitive",
                "correct": False,
                "rationale": (
                    "Incorrect. Sensitive data warrants general protection "
                    "from unauthorized internal or external disclosure, but "
                    "this label does not address the specific legal "
                    "export-control licensing requirement that governs who "
                    "may even view this data based on nationality."
                ),
            },
            {
                "id": "d",
                "text": "Public",
                "correct": False,
                "rationale": (
                    "Incorrect. Public data carries no disclosure "
                    "restriction, which is the opposite of data whose "
                    "unauthorized disclosure to a foreign person is a federal "
                    "offense."
                ),
            },
        ],
        "explanation": (
            "When a classification scheme includes a label specifically for "
            "legally export-restricted data, technical data subject to "
            "regulations like ITAR belongs at that classification rather than "
            "a general sensitivity or proprietary-business label, since the "
            "controlling risk is legal/regulatory export licensing rather "
            "than ordinary competitive sensitivity."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-026",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "An application's customer-support screen only ever needs to "
            "display the last four digits of a customer's Social Security "
            "number to verify identity, and no other part of the application "
            "ever uses the full number after initial account verification at "
            "signup. Currently, the full SSN is stored indefinitely in the "
            "customer database. Which change provides the STRONGEST reduction "
            "in risk from a future database breach?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Apply data minimization: stop retaining the full SSN "
                    "after initial verification, storing only the last four "
                    "digits (or a token) needed for ongoing support use"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since the full value is never actually needed "
                    "after initial verification, not retaining it at all "
                    "eliminates the risk of its exposure in a future breach "
                    "entirely — a stronger reduction than any control that "
                    "merely protects data that continues to be stored."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Encrypt the full SSN column with AES-256 using a key "
                    "stored in the same application server's configuration "
                    "file"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This still retains the full SSN indefinitely, "
                    "and storing the encryption key alongside the encrypted "
                    "data on the same server means a server compromise can "
                    "expose both — a materially weaker reduction in risk than "
                    "simply not retaining the data at all."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Apply dynamic masking so support agents see only the "
                    "last four digits on screen, while the full SSN remains "
                    "stored in the database"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This controls what agents see, but the full "
                    "SSN is still retained in the database and remains fully "
                    "exposed in the event of a database breach, since masking "
                    "is a display-layer control, not a data-retention "
                    "control."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Move the SSN column to a separate database table with "
                    "stricter access permissions, while still storing the "
                    "full value indefinitely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reduces who can query the value under "
                    "normal operations, but the full SSN is still retained "
                    "and would still be exposed if that separate table itself "
                    "were ever breached."
                ),
            },
        ],
        "explanation": (
            "Data minimization — not retaining data that is never actually "
            "needed — provides the strongest risk reduction because data "
            "that was never stored cannot be exposed in a breach, unlike "
            "encryption, masking, or access segregation, which all still "
            "leave the full value present somewhere to be compromised."
        ),
    },
    {
        "id": "nd3c-027",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Data protection methods",
        "stem": (
            "A design firm regularly emails proprietary CAD files to "
            "external contractors. Once a file leaves the firm's network, "
            "the firm has no way to prevent the recipient from forwarding it, "
            "printing it, or continuing to open it after the contract ends. "
            "Which control BEST gives the firm persistent control over the "
            "file's use even after it has left the corporate network?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Information/digital rights management (IRM/DRM) that "
                    "embeds usage controls — such as restrictions on "
                    "printing, forwarding, and an expiration date — directly "
                    "into the file itself"
                ),
                "correct": True,
                "rationale": (
                    "Correct. IRM/DRM protections travel with the file and "
                    "continue to be enforced by the reader/viewer application "
                    "wherever the file goes, giving the firm persistent "
                    "control over printing, forwarding, and expiration even "
                    "after the file leaves the network — exactly the gap "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Encrypt the email in transit using TLS between the "
                    "firm's mail server and the contractor's mail server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TLS only protects the email while it is being "
                    "transmitted between mail servers; it provides no "
                    "ongoing control over the file once it has been delivered "
                    "and decrypted at the recipient's end."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Apply full-disk encryption on the firm's own laptops "
                    "that create the CAD files"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Full-disk encryption protects data at rest on "
                    "the firm's own devices; it has no effect on a file that "
                    "has already been emailed out and now resides on the "
                    "external contractor's systems."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure the email gateway's data loss prevention (DLP) "
                    "policy to block all outbound emails containing CAD file "
                    "attachments"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking these attachments entirely would "
                    "prevent the firm from being able to legitimately share "
                    "files with contractors at all, failing to support the "
                    "described ongoing business need for external "
                    "collaboration."
                ),
            },
        ],
        "explanation": (
            "IRM/DRM is the control designed specifically to persist usage "
            "restrictions with a file after it leaves the organization's "
            "network and passes to external recipients, unlike transport "
            "encryption, at-rest device encryption, or an outright DLP block, "
            "none of which provide ongoing post-delivery control."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-028",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Data states",
        "stem": (
            "A cloud object storage bucket is configured for cross-region "
            "replication: every night, an automated background process "
            "silently copies newly written objects from the primary region "
            "to a bucket in a second region over the cloud provider's "
            "internal backbone network, with no user or application ever "
            "directly requesting the copy. While an object is actively being "
            "copied by this replication process between regions, which data "
            "state applies to it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data in transit, because the object is actively moving "
                    "across a network between two locations, even though the "
                    "copy is an automated background process rather than a "
                    "user-initiated interactive session"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Data in transit refers to any data actively "
                    "traversing a network, regardless of whether a human user "
                    "or interactive session triggered the movement; an "
                    "automated backbone replication copy is still network "
                    "transmission and must be protected accordingly (e.g., "
                    "with encryption in transit)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Data at rest, because the object already existed in a "
                    "stored bucket before replication began"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While the object was at rest before and will "
                    "be at rest again after replication completes, the state "
                    "during the actual copy operation is defined by its being "
                    "actively transmitted across the network, not by its "
                    "stored state before or after."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data in use, because the replication engine is actively "
                    "processing the object"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data in use specifically refers to data being "
                    "actively processed in memory by an application (e.g., "
                    "decrypted for computation), not data simply being copied "
                    "byte-for-byte across a network connection."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No defined data state applies, since the replication is "
                    "automated rather than user-initiated"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data state classifications (at rest, in "
                    "transit, in use) apply based on what is technically "
                    "happening to the data, not on whether a human user "
                    "initiated the action; automated processes are not "
                    "exempt from these classifications."
                ),
            },
        ],
        "explanation": (
            "Data in transit describes any data actively moving across a "
            "network — including automated, non-interactive processes like "
            "cross-region replication — distinguishing it from data at rest "
            "(stored, not moving) and data in use (actively processed in "
            "memory)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-029",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A retailer wants to reduce the number of internal systems "
            "subject to PCI DSS audit scope. Its order-management and "
            "loyalty-lookup systems need a consistent, referenceable value to "
            "detect duplicate transactions and match loyalty accounts to "
            "purchases, but neither system needs to ever see, store, or "
            "process the customer's actual primary account number (PAN). "
            "Which technique BEST reduces PCI scope for these downstream "
            "systems while still supporting their referencing needs?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tokenization: replace the PAN with a token in the "
                    "order-management and loyalty systems, keeping the "
                    "reversible mapping to the real PAN isolated in a "
                    "separate, narrowly scoped token vault"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the downstream systems only ever store "
                    "and reference the token — never the actual PAN — they "
                    "fall outside PCI DSS cardholder data scope, while the "
                    "token remains consistent and referenceable for "
                    "duplicate-detection and loyalty matching, satisfying "
                    "both goals."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Static masking of the PAN in each system, replacing it "
                    "with a randomly generated, non-consistent substitute "
                    "value"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking is typically applied "
                    "irreversibly and does not guarantee the same masked "
                    "output every time for the same input across separate "
                    "systems, undermining the requirement for a consistent, "
                    "referenceable value used to detect duplicates and match "
                    "accounts."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Column-level encryption of the PAN, storing the "
                    "encrypted value directly in the order-management and "
                    "loyalty databases"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Storing any form of the actual PAN — even "
                    "encrypted — within these systems generally keeps them "
                    "inside PCI DSS scope, since the systems still house "
                    "cardholder data rather than a fully de-scoped surrogate "
                    "value."
                ),
            },
            {
                "id": "d",
                "text": (
                    "One-way hashing of the PAN using SHA-256 before storing "
                    "it in each system"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While hashing can be irreversible, PCI DSS "
                    "still generally treats a hashed PAN as sensitive "
                    "cardholder data subject to compliance requirements "
                    "unless implemented under specific approved conditions, "
                    "and a bare hash does not reduce scope the way "
                    "vault-isolated tokenization does."
                ),
            },
        ],
        "explanation": (
            "Tokenization is the standard technique for reducing PCI DSS "
            "audit scope: it removes the actual PAN from downstream systems "
            "entirely while still providing a consistent, referenceable "
            "surrogate value, unlike masking (inconsistent), raw encryption "
            "(PAN still present), or bare hashing (still treated as "
            "sensitive)."
        ),
    },
    {
        "id": "nd3c-030",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A mobile banking app's engineering team is implementing two "
            "separate protections: (1) the stored bank account number is "
            "replaced with a random, non-mathematically-derived surrogate "
            "value that only the back-end settlement vault can map back to "
            "the real account number for authorized processing, and (2) "
            "customer support agents viewing the account in their internal "
            "tool see only a partial, on-screen view of the account number "
            "(e.g., ****4821), while the complete number remains stored "
            "securely server-side. Which TWO techniques are being described, "
            "respectively? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tokenization, using a vault-based mapping to allow "
                    "authorized recovery of the original account number for "
                    "settlement processing"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Replacing the account number with a random "
                    "surrogate value that a vault can map back to the "
                    "original for authorized processing is the definition of "
                    "vault-based tokenization — matching the first "
                    "protection."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Dynamic data masking, displaying only a partial view of "
                    "the account number to the support agent while the full "
                    "value remains protected server-side"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Showing only a partial, on-screen "
                    "representation of a value while the complete value stays "
                    "protected elsewhere is the definition of dynamic masking "
                    "— matching the second protection."
                ),
            },
            {
                "id": "c",
                "text": "One-way hashing of the account number",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is irreversible by design, so it "
                    "could never support the vault's authorized recovery of "
                    "the original account number described in the first "
                    "protection."
                ),
            },
            {
                "id": "d",
                "text": "Static data masking of the account number",
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking permanently and irreversibly "
                    "replaces a value for non-production or display use; it "
                    "does not describe a reversible, vault-based value used "
                    "for live settlement processing, nor a partial on-screen "
                    "reveal to a live support agent."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Column-level encryption with the key distributed "
                    "directly to the support agent's application"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Distributing the decryption key to the "
                    "support tool would let it decrypt and display the "
                    "complete account number, contradicting the requirement "
                    "that agents see only a partial value."
                ),
            },
        ],
        "explanation": (
            "Vault-based tokenization supports authorized recovery of the "
            "original value for back-end processing, while dynamic masking "
            "controls how much of a value is revealed on screen to a given "
            "user role — distinct techniques from irreversible hashing, "
            "non-reversible static masking, or key-distributed encryption."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-031",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A company has performed nightly automated backups for several "
            "years, and the backup software reports every job as completed "
            "successfully. During an actual ransomware recovery, the team "
            "discovers that a significant portion of the backup files are "
            "corrupted and cannot be restored, because the backups were never "
            "actually tested with a full restore. Which practice would have "
            "MOST reliably prevented this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Regularly performing full restore tests of backup data "
                    "to an isolated environment to verify that backups are "
                    "actually recoverable, not just that the backup job "
                    "reported success"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A job reporting 'success' only confirms the "
                    "backup process ran without error; only an actual restore "
                    "test verifies the resulting data is genuinely usable, "
                    "which is the gap that led to the failed recovery."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increasing the frequency of backups from nightly to "
                    "hourly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent backups would only produce more "
                    "frequent copies of data that might still be silently "
                    "corrupted; frequency does nothing to verify the "
                    "recoverability of the backups themselves."
                ),
            },
            {
                "id": "c",
                "text": "Encrypting all backup files with AES-256",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption protects the confidentiality of "
                    "backup data if stolen, but it has no bearing on whether "
                    "the underlying backed-up data is intact and restorable."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Adding more backup storage capacity to retain a longer "
                    "history of backup versions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Retaining more historical versions does not "
                    "address whether any individual backup is actually "
                    "restorable; without testing, additional untested "
                    "versions could be equally corrupted."
                ),
            },
        ],
        "explanation": (
            "Only regular, full restore testing verifies that backups are "
            "genuinely recoverable — a successful backup job status, "
            "encryption, added frequency, or extra retained history all fail "
            "to catch silent corruption the way an actual restore test does."
        ),
    },
    {
        "id": "nd3c-032",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backups and replication",
        "stem": (
            "An e-commerce company currently replicates its transaction "
            "database to a disaster recovery site using hourly snapshots. "
            "Leadership now mandates that, in a worst-case failure, no more "
            "than 5 minutes of transactions can ever be lost. The network "
            "link to the DR site has ample spare bandwidth to support a more "
            "frequent replication method. Which change BEST meets the new "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace hourly snapshots with continuous transaction log "
                    "shipping (or continuous data protection) to the DR site, "
                    "replicating changes as they occur rather than on a fixed "
                    "hourly interval"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuous log shipping or CDP replicates "
                    "changes on an ongoing, near-real-time basis rather than "
                    "a fixed hourly interval, closing the recovery point gap "
                    "down to a small, bounded window well within the "
                    "required 5 minutes."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the snapshot interval to every 30 minutes "
                    "instead of every hour"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Even a 30-minute snapshot interval still "
                    "permits up to 30 minutes of potential data loss, far "
                    "exceeding the mandated 5-minute maximum."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Switch to synchronous replication for every transaction, "
                    "guaranteeing a zero-second recovery point regardless of "
                    "latency impact"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While this would technically satisfy the "
                    "RPO, synchronous replication was not what the "
                    "requirement called for (a bounded RPO of 5 minutes, not "
                    "zero), and it introduces unnecessary commit latency for "
                    "a requirement that continuous log shipping can already "
                    "satisfy without that added performance cost."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Keep hourly snapshots, but retain them for a longer "
                    "period of time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Retention duration determines how far back in "
                    "history backups are kept; it does nothing to reduce the "
                    "amount of data that could be lost between the most "
                    "recent snapshot and a failure."
                ),
            },
        ],
        "explanation": (
            "Continuous log shipping or CDP is the appropriate step up from "
            "periodic snapshots to meet a tight, bounded RPO like 5 minutes, "
            "without the added commit-latency cost of full synchronous "
            "replication, which would over-deliver on a requirement that "
            "isn't actually zero."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-033",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "A company's application cluster requires three nodes to handle "
            "normal peak load. The operations team regularly takes one node "
            "offline at a time for scheduled patching, and leadership "
            "requires that the service remain fully available at full "
            "capacity even if an unplanned node failure occurs while a node "
            "is already offline for that scheduled maintenance. Which "
            "redundancy level should the cluster be provisioned with?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "N+2 redundancy — five total nodes, two more than the "
                    "three required for peak load — so a scheduled "
                    "maintenance node and one additional unplanned failure "
                    "can both be absorbed simultaneously without losing "
                    "capacity"
                ),
                "correct": True,
                "rationale": (
                    "Correct. N+2 provisions enough spare capacity to cover "
                    "both a planned maintenance node being offline and a "
                    "simultaneous unplanned failure, keeping the required "
                    "three nodes' worth of capacity available in both "
                    "situations at once."
                ),
            },
            {
                "id": "b",
                "text": (
                    "N+1 redundancy — four total nodes, one more than the "
                    "three required for peak load"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. N+1 only covers a single node being "
                    "unavailable at a time; once one node is offline for "
                    "scheduled maintenance, the remaining three nodes provide "
                    "exactly the minimum required capacity, leaving no buffer "
                    "for an additional unplanned failure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Active-passive clustering with a single standby node "
                    "held in reserve"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single standby node functions similarly to "
                    "N+1 in this three-node-minimum scenario — it covers one "
                    "absence, not the combination of a maintenance node and a "
                    "simultaneous unplanned failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No additional redundancy beyond the three nodes "
                    "required for peak load, relying on rapid manual "
                    "provisioning if a failure occurs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This provides no buffer at all for even a "
                    "single node outage, let alone the combined "
                    "scheduled-maintenance-plus-unplanned-failure scenario "
                    "the requirement describes, and manual provisioning "
                    "introduces unacceptable delay."
                ),
            },
        ],
        "explanation": (
            "N+2 redundancy is the level required when the design must "
            "tolerate both a planned absence (e.g., maintenance) and an "
            "additional unplanned failure occurring at the same time without "
            "losing required capacity, unlike N+1, which only covers a "
            "single absence."
        ),
    },
    {
        "id": "nd3c-034",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "High availability",
        "stem": (
            "A three-tier web application currently has two single points of "
            "failure identified in an architecture review: (1) a single load "
            "balancer appliance sits in front of the web tier with no "
            "standby, and (2) each application server connects to the shared "
            "storage array through a single host bus adapter (HBA) and a "
            "single fabric switch, so a failed cable, HBA, or switch isolates "
            "that server from storage. Which TWO changes would MOST directly "
            "eliminate these two specific single points of failure, "
            "respectively? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy a redundant, clustered pair of load balancers "
                    "(e.g., using VRRP or a similar protocol to share a "
                    "floating virtual IP) instead of a single appliance"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A clustered load balancer pair with a floating "
                    "virtual IP eliminates the single-appliance failure point "
                    "by allowing a standby unit to take over the shared IP "
                    "automatically — directly remediating the first finding."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Configure multipath I/O with redundant HBAs and "
                    "connections through separate fabric switches from each "
                    "application server to the storage array"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Multipath storage connectivity through "
                    "independent HBAs and switches ensures that a single "
                    "cable, HBA, or switch failure does not isolate a server "
                    "from storage — directly remediating the second finding."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the single load balancer's CPU and memory "
                    "allocation to handle more traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Vertically scaling the existing single "
                    "appliance improves its capacity but does not eliminate "
                    "it as a single point of failure — if that one appliance "
                    "fails entirely, the web tier is still unreachable."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Add more application servers behind the existing single "
                    "load balancer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Additional application servers improve "
                    "web-tier redundancy, but the load balancer in front of "
                    "them remains a single point of failure regardless of how "
                    "many servers sit behind it."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Increase the frequency of database backups to the "
                    "storage array"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent backups improve recovery point "
                    "objectives for data loss scenarios, but they do nothing "
                    "to address either the load balancer or the storage "
                    "connectivity single points of failure described."
                ),
            },
        ],
        "explanation": (
            "A clustered load balancer pair removes the single-appliance "
            "failure point at the web tier, while multipath storage "
            "connectivity removes the single-HBA/switch failure point at the "
            "storage layer — vertical scaling, adding more web servers "
            "behind the same load balancer, or more frequent backups address "
            "neither finding."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-035",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multi-cloud and platform diversity",
        "stem": (
            "A retailer's storefront went fully offline for six hours when "
            "its single content delivery network (CDN) provider suffered a "
            "global outage, even though the retailer's origin servers "
            "remained up and healthy the entire time. Which architecture "
            "change BEST addresses this specific single point of failure "
            "going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Adopt a multi-CDN configuration, routing traffic across "
                    "two independent CDN providers with automatic failover "
                    "between them"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since the outage was specific to the single CDN "
                    "layer rather than the origin servers, adding a second, "
                    "independent CDN provider with automatic failover "
                    "directly removes that single point of failure at the "
                    "layer where the actual outage occurred."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Add more origin servers behind the existing single CDN "
                    "provider"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The origin servers were never the problem — "
                    "they remained healthy throughout the outage — so adding "
                    "more of them does nothing to address a failure at the "
                    "CDN layer."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Negotiate a larger, higher-tier contract with the same "
                    "single CDN provider"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Remaining with a single provider, even under "
                    "a larger contract, still leaves the storefront fully "
                    "dependent on that one provider's availability, "
                    "reproducing the same single point of failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rely solely on client-side browser caching to keep the "
                    "site available during future outages"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Client-side caching only helps returning "
                    "visitors with previously cached content already in their "
                    "browser; it does not provide availability for new "
                    "visitors or dynamic content during a CDN-wide outage."
                ),
            },
        ],
        "explanation": (
            "A multi-CDN strategy, spanning independent providers with "
            "automatic failover, directly addresses a single point of "
            "failure at the CDN layer, unlike adding origin capacity, a "
            "larger contract with the same provider, or client-side caching, "
            "none of which resolve provider-wide unavailability."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-036",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Power resilience",
        "stem": (
            "A company's critical server racks currently draw power from a "
            "single UPS and a single power distribution unit (PDU) per rack. "
            "Leadership requires that a single UPS module or PDU failure — "
            "including during scheduled maintenance on one power path — never "
            "interrupts power to these racks. Which power redundancy "
            "topology BEST meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "2N redundancy, with each server equipped with dual power "
                    "supplies fed by two completely independent UPS and PDU "
                    "paths, either of which can carry the full load alone"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 2N provisions two fully independent, parallel "
                    "power paths, each capable of carrying the entire load on "
                    "its own, so a failure or planned maintenance on either "
                    "UPS or PDU path leaves the other fully able to power the "
                    "racks without interruption."
                ),
            },
            {
                "id": "b",
                "text": (
                    "N+1 redundancy, with a single shared spare UPS module "
                    "available to take over if the primary UPS fails"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. N+1 covers a single UPS module failure, but "
                    "because it does not provision a fully independent second "
                    "PDU/distribution path, an issue on the shared "
                    "distribution path — or maintenance on it — can still "
                    "interrupt power, unlike true 2N."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A single UPS sized with extra battery capacity to extend "
                    "runtime"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Extra battery capacity extends how long a "
                    "single UPS can run, but it does not add a second, "
                    "independent path; a failure of that single UPS or its "
                    "PDU would still interrupt power entirely."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A single generator without any UPS, sized to cover "
                    "extended outages"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Without a UPS, there would be a power "
                    "interruption during the time it takes the generator to "
                    "start and stabilize, and a single generator/PDU path "
                    "still leaves no redundancy for a failure or maintenance "
                    "on that one path."
                ),
            },
        ],
        "explanation": (
            "2N redundancy is the topology that provides two fully "
            "independent power paths, each able to carry the full load "
            "alone, meeting a requirement that a failure or planned "
            "maintenance on either single path never interrupts power — a "
            "bar that N+1, extended single-UPS runtime, or a single "
            "generator path cannot clear."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-037",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "A global trading platform requires an effectively near-zero "
            "recovery time objective: any outage at the primary site must be "
            "invisible to end users, with traffic automatically shifting to "
            "a fully synchronized secondary environment within seconds. The "
            "organization has budget approval for whatever level of "
            "redundancy this requires. Which recovery site type BEST meets "
            "this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A hot site — a fully redundant, continuously "
                    "synchronized active environment (or active-active "
                    "multi-region deployment) ready for immediate, automatic "
                    "failover"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A hot site is the only recovery site type that "
                    "keeps a fully synchronized, ready environment running "
                    "continuously, enabling the seconds-scale, automatic "
                    "failover the near-zero RTO requirement demands."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A warm site, with infrastructure pre-installed and data "
                    "updated periodically, requiring some final configuration "
                    "before cutover"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A warm site's periodic data updates and need "
                    "for final configuration before cutover introduce delay "
                    "far beyond a seconds-scale RTO, failing this specific "
                    "requirement even though it is a reasonable fit for less "
                    "time-sensitive systems."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A cold site, with basic facility and connectivity but no "
                    "pre-installed hardware or data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Provisioning hardware and restoring data from "
                    "scratch at a cold site takes far longer than seconds, "
                    "making this option entirely unsuitable for a near-zero "
                    "RTO requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A reciprocal agreement with a partner organization to "
                    "use their facility during an outage"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reciprocal agreements involve significant "
                    "setup time, capacity uncertainty, and configuration work "
                    "during an actual event, none of which can deliver an "
                    "automatic, seconds-scale failover."
                ),
            },
        ],
        "explanation": (
            "Only a hot site (or equivalent active-active multi-region "
            "deployment) provides the continuously synchronized, ready-to-go "
            "environment needed for a near-zero RTO with automatic failover; "
            "warm, cold, and reciprocal options all involve recovery delay "
            "that a budget-unconstrained, seconds-scale requirement cannot "
            "tolerate."
        ),
    },
    {
        "id": "nd3c-038",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "A regional retailer operates a single distribution center and "
            "has a very limited disaster recovery budget. It has no existing "
            "secondary facility anywhere and does not want to commit in "
            "advance to a fixed second location that might not even be near "
            "wherever a future disaster actually strikes. After a disaster, "
            "the retailer needs temporary on-site IT capability restored at "
            "whatever location becomes available. Which recovery site "
            "approach BEST fits these constraints?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Contract for a mobile recovery site — a self-contained "
                    "trailer or transportable unit with servers, network "
                    "equipment, and workstations that can be deployed to "
                    "whichever location is needed after a disaster"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A mobile recovery site provides temporary IT "
                    "capability without committing to any fixed second "
                    "location in advance, and it can be deployed wherever it "
                    "is actually needed after a disaster — directly matching "
                    "both the budget and location-flexibility constraints."
                ),
            },
            {
                "id": "b",
                "text": "A cold site at a specific, pre-selected fixed location",
                "correct": False,
                "rationale": (
                    "Incorrect. A cold site requires committing to a "
                    "specific fixed location in advance, which the retailer "
                    "explicitly wants to avoid since a future disaster's "
                    "actual impact area is unknown."
                ),
            },
            {
                "id": "c",
                "text": "A hot site maintained continuously at a fixed location",
                "correct": False,
                "rationale": (
                    "Incorrect. A hot site is the most expensive recovery "
                    "option and also requires committing to a fixed location, "
                    "conflicting with both the limited budget and the desire "
                    "for location flexibility."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A reciprocal agreement with a partner organization's "
                    "existing data center"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A reciprocal agreement depends on a partner "
                    "organization with compatible infrastructure already "
                    "being available and willing, which is not established "
                    "as an option here, and does not offer the same "
                    "flexible, deploy-anywhere capability as a mobile unit."
                ),
            },
        ],
        "explanation": (
            "A mobile recovery site is the standard low commitment, "
            "location-flexible option for an organization that cannot "
            "predict where a future disaster will strike and cannot afford a "
            "fixed hot or warm site, unlike a cold site or hot site, both of "
            "which require pre-committing to a specific location."
        ),
    },
    # ------------------------------------------------------------------ #
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-039",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Resilience testing",
        "stem": (
            "A DR team wants to validate the technical accuracy of its "
            "ransomware runbook by actually executing the documented "
            "recovery steps — including running the real detection, "
            "isolation, and restoration scripts — against an isolated, "
            "non-production clone of the environment, injecting a simulated "
            "ransomware event into that clone. Live production systems and "
            "users are never touched during this exercise. Which type of "
            "resilience test is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Simulation test",
                "correct": True,
                "rationale": (
                    "Correct. A simulation test technically injects a mock "
                    "incident and executes the actual recovery procedures "
                    "against an isolated, non-production environment, "
                    "validating technical accuracy without touching live "
                    "production — exactly matching this description."
                ),
            },
            {
                "id": "b",
                "text": "Tabletop exercise",
                "correct": False,
                "rationale": (
                    "Incorrect. A tabletop exercise is a purely "
                    "discussion-based walkthrough of roles and responses; it "
                    "does not involve actually executing technical recovery "
                    "scripts against any environment, isolated or otherwise."
                ),
            },
            {
                "id": "c",
                "text": "Full interruption (live failover) test",
                "correct": False,
                "rationale": (
                    "Incorrect. A full interruption test actually shuts down "
                    "live production systems and cuts real traffic over to "
                    "the DR environment, which contradicts the scenario's "
                    "explicit statement that live production systems are "
                    "never touched."
                ),
            },
            {
                "id": "d",
                "text": "Parallel processing test",
                "correct": False,
                "rationale": (
                    "Incorrect. A parallel test runs the DR environment "
                    "alongside live production processing real production "
                    "data concurrently for comparison; this scenario instead "
                    "describes an isolated clone environment with an "
                    "injected mock event, not concurrent live production "
                    "processing."
                ),
            },
        ],
        "explanation": (
            "A simulation test is defined by technically executing recovery "
            "procedures against an isolated, non-production copy of the "
            "environment with an injected mock incident — distinct from the "
            "purely verbal tabletop exercise, the live-cutover full "
            "interruption test, or the concurrent-live-processing parallel "
            "test."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3c-040",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "A company plans to engage a consulting firm for multiple "
            "projects over the next three years. It wants a single "
            "overarching contract establishing payment terms, liability, and "
            "confidentiality obligations up front, so that each new project "
            "can be quickly authorized through a short project-specific work "
            "order rather than renegotiating full legal terms every time. "
            "Which agreement type BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A master service agreement (MSA), under which individual "
                    "statements of work (SOWs) are issued for each new "
                    "project"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An MSA is designed precisely for this pattern: "
                    "it establishes overarching legal, payment, and liability "
                    "terms once, allowing each subsequent project to be "
                    "quickly authorized through a brief SOW without "
                    "renegotiating the full contract."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A memorandum of understanding (MOU) describing the "
                    "general intent to collaborate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is typically a non-binding statement "
                    "of mutual intent; it lacks the binding legal, payment, "
                    "and liability terms the company needs established up "
                    "front for a multi-year, multi-project engagement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A service level agreement (SLA) defining uptime and "
                    "performance metrics"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines measurable performance and "
                    "response-time commitments for a specific service; it "
                    "does not establish the overarching contractual, "
                    "payment, and liability framework needed to govern "
                    "multiple future projects."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A separate, fully negotiated individual contract drafted "
                    "from scratch for each new project"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly the repeated renegotiation "
                    "the company is trying to avoid, contradicting the "
                    "stated goal of quickly authorizing new projects without "
                    "redoing full legal terms each time."
                ),
            },
        ],
        "explanation": (
            "A master service agreement paired with per-project statements "
            "of work is the standard structure for establishing overarching "
            "legal terms once and then quickly authorizing repeated future "
            "engagements, unlike a non-binding MOU, a narrowly scoped SLA, "
            "or renegotiating a full contract every time."
        ),
    },
]
