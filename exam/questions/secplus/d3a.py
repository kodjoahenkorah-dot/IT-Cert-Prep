"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file A.

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
        "id": "nd3a-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A multinational retailer is redesigning its point-of-sale architecture "
            "and must choose between a centralized model, in which every store sends "
            "transactions to a single regional data center for processing, and a "
            "decentralized model, in which local edge servers at each store process "
            "transactions independently and synchronize with headquarters later. "
            "Which trade-off BEST justifies choosing the decentralized (edge) model?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Local edge processing lets stores keep accepting transactions "
                    "during a WAN outage, improving availability at the cost of "
                    "eventual-consistency complexity between sites"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Decentralized/edge architectures trade some data "
                    "consistency and synchronization complexity for local "
                    "responsiveness and continued availability when the link to "
                    "headquarters is down — exactly the scenario described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Centralizing all processing in one data center reduces the "
                    "attack surface by eliminating distributed endpoints"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a genuine advantage of the centralized "
                    "model, not the decentralized one, so it cannot justify "
                    "choosing decentralization."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Decentralized edge nodes are cheaper to patch because updates "
                    "only need to be pushed to a single location"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The opposite is true: patching is simpler and "
                    "cheaper in a centralized model where there is one location to "
                    "update, not many distributed edge nodes."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Centralized architecture provides better responsiveness "
                    "because all transaction logic executes locally at each store"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the decentralized model, not the "
                    "centralized one — in a centralized design, transactions must "
                    "round-trip to the regional data center rather than executing "
                    "locally."
                ),
            },
        ],
        "explanation": (
            "Centralized vs. decentralized architecture is a classic availability/"
            "responsiveness-versus-consistency trade-off: centralization simplifies "
            "patching and shrinks the attack surface, while decentralization "
            "preserves local availability and responsiveness during connectivity "
            "loss at the cost of synchronization complexity."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A healthcare organization is moving out of its own data center. An "
            "auditor requires that the organization retain the ability to apply "
            "its own OS-level hardening and control the exact timing of patches to "
            "the guest operating system, while still eliminating the burden of "
            "managing physical servers and hypervisors. Which cloud service model "
            "BEST meets both requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Infrastructure as a Service (IaaS)",
                "correct": True,
                "rationale": (
                    "Correct. In IaaS, the provider manages the physical hardware, "
                    "hypervisor, and network, while the customer retains full "
                    "control over the guest OS and above — including patch timing "
                    "and hardening standards."
                ),
            },
            {
                "id": "b",
                "text": "Platform as a Service (PaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. PaaS reduces management burden further by having "
                    "the provider manage the OS and runtime, which conflicts with "
                    "the requirement that the organization control its own OS "
                    "patch schedule."
                ),
            },
            {
                "id": "c",
                "text": "Software as a Service (SaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. SaaS gives the customer no control over the "
                    "underlying OS at all; the provider manages the entire stack "
                    "including the application."
                ),
            },
            {
                "id": "d",
                "text": "Community cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a deployment model (who shares the "
                    "cloud environment), not a service model, and does not by "
                    "itself address who manages hardware versus OS patching."
                ),
            },
        ],
        "explanation": (
            "IaaS is the only service model that both removes physical hardware "
            "management from the customer and leaves OS-level control — including "
            "patch timing — in the customer's hands."
        ),
    },
    {
        "id": "nd3a-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company discovers that an object storage bucket in its IaaS "
            "environment was configured with public read access, exposing customer "
            "records. The cloud provider confirms that its physical data centers, "
            "hypervisor, and network fabric were never compromised. Under the "
            "shared responsibility model, who is accountable for this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer, because configuring access controls on data "
                    "stored in the cloud is a customer responsibility in every "
                    "service model"
                ),
                "correct": True,
                "rationale": (
                    "Correct. \"Security of the cloud\" (physical infrastructure, "
                    "hypervisor) is the provider's job, but \"security in the "
                    "cloud\" — including access control configuration on data the "
                    "customer stores — remains the customer's responsibility "
                    "regardless of service model."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The cloud provider, because providers are solely responsible "
                    "for all security in an IaaS environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IaaS does shift more infrastructure responsibility "
                    "to the provider than PaaS or SaaS, but it never makes the "
                    "provider solely responsible for all security — data access "
                    "configuration is always retained by the customer."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider and customer share equal, joint accountability "
                    "through a combined security operations center"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The shared responsibility model divides distinct "
                    "layers of accountability rather than making both parties "
                    "jointly liable for the same misconfiguration through a "
                    "combined SOC."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither party, because publicly accessible storage is an "
                    "unavoidable inherent risk of using IaaS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bucket permissions are a configurable control, not "
                    "an unavoidable risk, and someone is always accountable for "
                    "setting them correctly."
                ),
            },
        ],
        "explanation": (
            "The shared responsibility model draws a clear line: providers secure "
            "the underlying cloud infrastructure, while customers are always "
            "responsible for configuring access to their own data, regardless of "
            "service model."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A power utility's SCADA controller runs an embedded, real-time OS on "
            "hardware from a vendor that requires lengthy recertification testing "
            "before any patch can be applied. Taking the turbine controller offline "
            "for patch testing would cause a longer, costlier outage than the risk "
            "the patch addresses. Which compensating control is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Isolate the controller on a segmented OT network protected by "
                    "a unidirectional gateway or tightly controlled firewall rules, "
                    "limiting exposure without altering the controller itself"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When patching an embedded/ICS device isn't feasible "
                    "on a reasonable timeline, network isolation and strict "
                    "boundary controls are the standard compensating control that "
                    "reduces risk without touching the constrained device."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Apply the vendor patch immediately without recertification to "
                    "close the vulnerability as quickly as possible"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bypassing vendor recertification on safety-critical "
                    "ICS hardware risks unpredictable control-loop behavior and "
                    "could itself cause an outage or unsafe condition."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Install a modern EDR agent directly on the embedded "
                    "controller to monitor and block malicious activity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Resource-constrained real-time embedded controllers "
                    "typically cannot support standard EDR agents without risking "
                    "the timing guarantees the control process depends on."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Migrate the control logic to a cloud-hosted virtual machine "
                    "for easier centralized patch management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Real-time turbine control cannot tolerate the "
                    "latency and availability risk of depending on a remote cloud "
                    "connection; this would introduce new failure modes rather "
                    "than reduce risk."
                ),
            },
        ],
        "explanation": (
            "For legacy or unpatchable ICS/SCADA and embedded devices, network "
            "segmentation and boundary controls (e.g., unidirectional gateways) are "
            "the standard compensating control, since direct patching, host agents, "
            "or cloud migration are often infeasible or unsafe."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IoT security",
        "stem": (
            "An enterprise deploys several hundred low-cost smart HVAC sensors "
            "that ship with weak default credentials and lack the CPU and memory "
            "to run standard security agents. Which control BEST mitigates the "
            "risk these devices pose without exceeding their hardware capabilities?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Place the sensors on an isolated network segment with ACLs "
                    "restricting traffic to only the specific management protocols "
                    "and destinations they require"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Network-level segmentation and restrictive ACLs "
                    "contain resource-constrained IoT devices without requiring "
                    "any additional processing power on the devices themselves."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Install host-based antivirus software on each sensor to "
                    "detect malicious firmware modifications"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. These constrained IoT devices typically lack the "
                    "CPU, memory, and OS support needed to run host-based "
                    "antivirus agents."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enforce a 90-day password rotation policy through each "
                    "device's individual administrative panel"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rotating default credentials is a good first step "
                    "but, done manually per device across hundreds of sensors, it "
                    "does not scale and provides far weaker containment than "
                    "network segmentation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Assign each sensor a public IP address so it can be reached "
                    "directly by a centralized cloud management dashboard"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Exposing weakly secured IoT devices directly to "
                    "the internet significantly increases their attack surface "
                    "rather than reducing it."
                ),
            },
        ],
        "explanation": (
            "For resource-constrained IoT devices that cannot run traditional "
            "security agents, network segmentation with restrictive ACLs is the "
            "most scalable and effective control."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A security team wants to reduce the blast radius if an attacker "
            "achieves code execution inside a single containerized microservice "
            "through a code-injection flaw. Which control provides the strongest "
            "containment for this specific scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Run each container as a non-root user with a read-only root "
                    "filesystem, combined with kernel namespace and cgroup "
                    "isolation limiting what the process can access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Least-privilege container execution combined with "
                    "kernel-level isolation directly limits what an attacker who "
                    "gains code execution inside one container can do to the host "
                    "or other containers."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy all microservices inside a single shared container to "
                    "simplify inter-service calls"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Consolidating services into one container "
                    "eliminates isolation entirely, meaning a single compromise "
                    "would affect every service at once — the opposite of "
                    "reducing blast radius."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Place an API gateway in front of the microservices to "
                    "authenticate external requests"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An API gateway helps secure north-south traffic "
                    "entering the environment but does nothing to limit what a "
                    "container can do once code execution is achieved inside it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Use a shared base image across all microservices to ensure "
                    "consistent patch levels"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Shared base images help patch consistency, but "
                    "they do not limit an attacker's ability to act within a "
                    "compromised container and can even widen the shared "
                    "vulnerability surface if a flaw exists in that base image."
                ),
            },
        ],
        "explanation": (
            "Reducing container blast radius requires least-privilege execution "
            "and kernel-level isolation controls, not perimeter authentication or "
            "image-consistency practices, which address different problems."
        ),
    },
    {
        "id": "nd3a-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A penetration test of a Kubernetes-orchestrated microservices "
            "platform found containers running with privileged security contexts "
            "and unrestricted pod-to-pod network communication across namespaces. "
            "Which TWO controls would MOST directly remediate these two specific "
            "findings? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Enforce a non-root, least-privilege pod security context that "
                    "disallows privileged containers"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This directly remediates the finding of containers "
                    "running with privileged security contexts."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Implement Kubernetes network policies to restrict pod-to-pod "
                    "traffic to only the paths each service requires "
                    "(microsegmentation)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This directly remediates the finding of "
                    "unrestricted pod-to-pod communication by enforcing "
                    "least-privilege east-west traffic rules."
                ),
            },
            {
                "id": "c",
                "text": "Enable container image vulnerability scanning in the CI/CD pipeline",
                "correct": False,
                "rationale": (
                    "Incorrect. Image scanning is a valuable supply-chain control "
                    "for catching known vulnerabilities before deployment, but it "
                    "does not address privileged security contexts or "
                    "unrestricted pod-to-pod traffic that already exist at "
                    "runtime."
                ),
            },
            {
                "id": "d",
                "text": "Deploy a web application firewall (WAF) in front of the ingress controller",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF filters malicious external (north-south) "
                    "web traffic reaching the cluster; it has no effect on "
                    "container privilege levels or internal pod-to-pod traffic."
                ),
            },
            {
                "id": "e",
                "text": "Increase the replica count of each pod to improve redundancy",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding replicas improves availability, not the "
                    "security posture of privilege levels or network "
                    "segmentation."
                ),
            },
        ],
        "explanation": (
            "Least-privilege security contexts and Kubernetes network policies "
            "map directly to the two findings — excessive container privilege and "
            "unrestricted lateral pod communication — while scanning, WAFs, and "
            "replica counts address different, unrelated concerns."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A development team stores database credentials as plaintext "
            "environment variables in each serverless function's configuration. "
            "Which change would BEST improve the security of this design without "
            "sacrificing the operational benefits of the serverless model?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Retrieve the credentials at runtime from a managed secrets "
                    "manager or vault using the function's execution role"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Pulling secrets from a managed secrets manager at "
                    "runtime removes plaintext credentials from configuration "
                    "while preserving the serverless model's lack of infrastructure "
                    "to manage."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Migrate the workload to persistent IaaS virtual machines so "
                    "credentials can be stored in an encrypted local file"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This abandons the serverless model's operational "
                    "benefits (no server management, automatic scaling) that the "
                    "requirement explicitly says to preserve."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Hardcode the credentials directly into the function's "
                    "source code so they are version-controlled"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hardcoding secrets into source code is worse than "
                    "environment variables, as it also exposes them to anyone "
                    "with repository access and version history."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the function's execution timeout to allow more time "
                    "for encrypted credential negotiation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Execution timeout is unrelated to how credentials "
                    "are stored or retrieved and does nothing to secure them."
                ),
            },
        ],
        "explanation": (
            "A managed secrets manager accessed via the function's execution "
            "role/identity is the standard pattern for securing serverless "
            "credentials without reintroducing server management overhead."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "A hosting provider runs many mutually untrusted customer workloads "
            "on shared physical servers and wants to minimize the attack surface "
            "available for a guest-to-host escape. Which approach is MOST "
            "appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Use bare-metal Type 1 hypervisors running directly on the "
                    "hardware rather than hosted on a general-purpose OS"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A Type 1 hypervisor runs directly on hardware with a "
                    "minimal, purpose-built code base, reducing the attack surface "
                    "compared to a hypervisor hosted on top of a full "
                    "general-purpose operating system."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Use a Type 2 hosted hypervisor running on top of a "
                    "general-purpose host operating system for easier management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A Type 2 hypervisor adds the entire underlying "
                    "host OS as additional attack surface, making it less "
                    "appropriate than bare-metal Type 1 for a multi-tenant "
                    "hosting environment."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replace virtualization with containerization for all "
                    "customer workloads to achieve stronger isolation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Containers share the host kernel, which generally "
                    "provides weaker isolation between mutually untrusted tenants "
                    "than separate virtual machines with their own kernels — the "
                    "opposite of what is needed here."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Dedicate a single physical host to each virtual machine to "
                    "eliminate hypervisor risk entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This defeats the cost and resource-utilization "
                    "purpose of virtualization and is not a scalable answer for a "
                    "hosting provider serving many tenants."
                ),
            },
        ],
        "explanation": (
            "Bare-metal Type 1 hypervisors minimize the code base exposed between "
            "tenants and are the standard choice for multi-tenant hosting where "
            "guest-to-host escape risk must be minimized."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-010",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A vulnerability assessment finds that a production server is running "
            "FTP, Telnet, and a default web administration console, none of which "
            "are used by the application it hosts. Which action MOST directly "
            "reduces the server's attack surface?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable the unused FTP, Telnet, and admin console services",
                "correct": True,
                "rationale": (
                    "Correct. Removing or disabling unnecessary running services "
                    "eliminates the exposed entry points entirely, which is the "
                    "definition of reducing attack surface."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy an intrusion detection system (IDS) to monitor "
                    "traffic to these services"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Monitoring can detect misuse of the exposed "
                    "services but does not reduce the number of exposed services "
                    "themselves."
                ),
            },
            {
                "id": "c",
                "text": "Deploy a web application firewall (WAF) in front of the server",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF filters HTTP(S) application traffic; it does "
                    "nothing to protect insecure protocols like FTP and Telnet "
                    "that don't route through it."
                ),
            },
            {
                "id": "d",
                "text": "Require multifactor authentication for the admin console",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding MFA strengthens access control to a "
                    "service that remains exposed, but it does not shrink the "
                    "attack surface by removing unneeded exposed services."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means eliminating unnecessary exposed "
            "services and entry points, not merely monitoring or adding "
            "authentication in front of them."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management workflow",
        "stem": (
            "At 2 a.m., a network engineer pushes a firewall rule change directly "
            "to production to resolve a business-critical outage, without waiting "
            "for change advisory board (CAB) approval. Which statement BEST "
            "describes the correct change management process for this situation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An emergency change process should be followed, allowing the "
                    "fix to proceed immediately with documentation and formal "
                    "approval obtained retroactively along with a post-"
                    "implementation review"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Formal change management frameworks include an "
                    "emergency change procedure precisely for situations like this "
                    "— allowing urgent fixes while still requiring documentation "
                    "and after-the-fact review/approval."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Production changes should never occur outside standard "
                    "business hours, regardless of business impact"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Emergency outages must be addressed whenever they "
                    "occur; refusing to act until business hours would prolong an "
                    "active, business-critical outage unnecessarily."
                ),
            },
            {
                "id": "c",
                "text": (
                    "All changes require CAB pre-approval with no exceptions, so "
                    "the engineer should have waited until the next scheduled CAB "
                    "meeting before making the change"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting for a routine CAB meeting during an active "
                    "critical outage would leave the business down far longer "
                    "than necessary; emergency change processes exist to avoid "
                    "exactly this delay."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A rollback plan is unnecessary for emergency changes since "
                    "speed is the priority"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A rollback plan remains a required element of "
                    "change management even during emergencies, precisely because "
                    "urgent changes carry higher risk of unintended side effects."
                ),
            },
        ],
        "explanation": (
            "Mature change management processes include a defined emergency-"
            "change path that allows urgent fixes to proceed with retroactive "
            "documentation, approval, and review, rather than either bypassing "
            "governance entirely or delaying critical fixes for routine approval."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "An inline intrusion prevention system (IPS) sits in front of a "
            "hospital's electronic health records system used during emergency "
            "care. Policy states that availability of clinical systems during a "
            "life-safety event outweighs the risk of a brief security gap. How "
            "should the IPS's failure mode be configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fail-open, allowing traffic to continue passing if the device fails",
                "correct": True,
                "rationale": (
                    "Correct. Fail-open preserves availability by letting traffic "
                    "pass through if the inline device fails, matching the stated "
                    "priority of clinical availability over a temporary security "
                    "gap."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fail-closed, blocking all traffic if the device fails to "
                    "guarantee no malicious traffic passes uninspected"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-closed is the right choice when confidentiality "
                    "or integrity outweighs availability, but here it would block "
                    "clinical traffic during a device failure, contradicting the "
                    "stated life-safety priority."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Active-active load balancing across two IPS appliances to "
                    "eliminate any single point of failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a high-availability design choice, not a "
                    "failure-mode setting, and does not by itself answer how a "
                    "single device should behave if it fails."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure the device in passive/tap mode so it never affects "
                    "traffic flow"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Switching to passive monitoring removes the "
                    "device's ability to actively prevent threats inline, changing "
                    "its entire deployment posture rather than simply defining its "
                    "failure behavior while remaining an active, inline control."
                ),
            },
        ],
        "explanation": (
            "When availability is prioritized over the risk of a brief security "
            "gap, an inline device should be configured to fail-open rather than "
            "fail-closed."
        ),
    },
    {
        "id": "nd3a-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Failure modes",
        "stem": (
            "A brokerage firm's compliance policy states that no unencrypted PII "
            "may leave the network under any circumstance, even if enforcing this "
            "requires halting trading operations. An inline data loss prevention "
            "(DLP) appliance inspects all outbound traffic. Which combination of "
            "device placement and failure mode BEST supports this policy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Inline (active) placement with a fail-closed configuration",
                "correct": True,
                "rationale": (
                    "Correct. Inline placement allows the DLP appliance to "
                    "actively block traffic, and fail-closed ensures that if the "
                    "device fails, traffic stops rather than passing uninspected "
                    "— matching a policy that prioritizes data protection over "
                    "availability."
                ),
            },
            {
                "id": "b",
                "text": "Inline (active) placement with a fail-open configuration",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open would allow unencrypted PII to leave "
                    "the network uninspected if the appliance fails, directly "
                    "violating the stated zero-tolerance policy."
                ),
            },
            {
                "id": "c",
                "text": "Passive (tap/monitor) placement with a fail-closed configuration",
                "correct": False,
                "rationale": (
                    "Incorrect. A passive tap only receives a copy of traffic and "
                    "cannot block anything, so \"fail-closed\" is not meaningful "
                    "in this placement — traffic still flows regardless of the "
                    "appliance's state, which does not satisfy a strict "
                    "prevention requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Passive placement with an out-of-band alerting workflow to "
                    "the security operations center"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This enables detection and alerting after data "
                    "has already left the network, but does not prevent the "
                    "leak, failing to meet the policy's strict prevention "
                    "requirement."
                ),
            },
        ],
        "explanation": (
            "Strict data-loss-prevention requirements call for inline (active) "
            "placement so the device can block traffic, combined with a "
            "fail-closed configuration so a device failure halts traffic rather "
            "than allowing an uninspected leak."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "An e-commerce company's perimeter next-generation firewall (NGFW) "
            "already provides network-layer filtering. The security team now "
            "wants a dedicated appliance placed specifically in front of the "
            "public web application to detect and block SQL injection and "
            "cross-site scripting attempts targeting it. Which appliance should "
            "be added?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Web application firewall (WAF)",
                "correct": True,
                "rationale": (
                    "Correct. A WAF is purpose-built to inspect HTTP(S) requests "
                    "for application-layer attacks like SQL injection and XSS, "
                    "complementing broader network-layer filtering already done "
                    "by the NGFW."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The existing NGFW, with additional signature updates applied"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While NGFWs offer some application awareness, a "
                    "WAF is the purpose-built appliance for deep inspection of "
                    "web request payloads against OWASP Top 10-style attacks, "
                    "making it the more precise answer for this specific need."
                ),
            },
            {
                "id": "c",
                "text": "Forward proxy server",
                "correct": False,
                "rationale": (
                    "Incorrect. A forward proxy controls and filters outbound "
                    "requests from internal clients to the internet; it does not "
                    "protect an inbound-facing public web application."
                ),
            },
            {
                "id": "d",
                "text": "Stateful packet-filtering firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. A stateful firewall filters based on Layer 3/4 "
                    "information (IP, port, connection state) and cannot inspect "
                    "application-layer payloads for SQL injection or XSS "
                    "patterns."
                ),
            },
        ],
        "explanation": (
            "A WAF is specifically designed to inspect and block application-"
            "layer web attacks, complementing rather than duplicating the "
            "network-layer filtering already handled by an NGFW."
        ),
    },
    {
        "id": "nd3a-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A company is opening a dozen small branch offices, each with fewer "
            "than 15 employees and a limited IT budget. Each site needs firewall, "
            "antivirus, content filtering, and basic IPS functionality "
            "consolidated to minimize hardware cost and management overhead. "
            "Which solution is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A unified threat management (UTM) appliance at each branch",
                "correct": True,
                "rationale": (
                    "Correct. UTM appliances consolidate firewall, antivirus, "
                    "content filtering, and IPS into a single low-cost device, "
                    "which matches the small branch office's budget and "
                    "simplicity requirements."
                ),
            },
            {
                "id": "b",
                "text": (
                    "An enterprise-grade NGFW cluster with dedicated IPS blades "
                    "at each branch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This provides strong capability but is heavily "
                    "over-engineered and cost-prohibitive for a 15-person branch "
                    "office, violating the stated budget constraint."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Separate best-of-breed firewall, antivirus server, and IPS "
                    "sensor deployed individually at each site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Deploying and managing multiple separate devices "
                    "at each small branch increases cost and administrative "
                    "overhead, directly conflicting with the requirement to "
                    "minimize both."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rely solely on a cloud-delivered SASE platform with no "
                    "on-premises hardware at any branch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SASE is a valid strategic alternative for "
                    "distributed branch security, but the requirement here "
                    "specifically calls for a single consolidated on-premises "
                    "appliance at each site, which describes a UTM rather than a "
                    "hardware-free cloud-native rollout."
                ),
            },
        ],
        "explanation": (
            "UTM appliances are purpose-built to consolidate multiple security "
            "functions into one low-cost, easy-to-manage device, making them the "
            "standard fit for small branch offices with limited budget and staff."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "Administrators need every SSH and RDP management connection into a "
            "segmented production management VLAN to pass through a single "
            "hardened, monitored host that logs all administrative sessions for "
            "audit purposes. Which appliance BEST fulfills this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Jump server (bastion host)",
                "correct": True,
                "rationale": (
                    "Correct. A jump server is specifically designed as the "
                    "single hardened, audited chokepoint through which "
                    "administrators reach systems in a restricted segment."
                ),
            },
            {
                "id": "b",
                "text": "Load balancer",
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes application traffic "
                    "across servers; it is not designed to broker or log "
                    "administrative shell/RDP sessions."
                ),
            },
            {
                "id": "c",
                "text": "Reverse proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A reverse proxy mediates and terminates web "
                    "traffic to backend application servers; it is not built for "
                    "brokering and auditing general administrative sessions like "
                    "SSH or RDP."
                ),
            },
            {
                "id": "d",
                "text": "VPN concentrator",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN concentrator provides an encrypted remote "
                    "access tunnel into the network, but it does not itself act "
                    "as the single audited hop that all internal administrative "
                    "sessions must pass through."
                ),
            },
        ],
        "explanation": (
            "A jump server (bastion host) is the appliance purpose-built to serve "
            "as the sole, hardened, and logged chokepoint for administrative "
            "access into a segmented environment."
        ),
    },
    {
        "id": "nd3a-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network appliances",
        "stem": (
            "An inline network sensor was configured to actively drop packets "
            "matching intrusion signatures. After deployment, a load balancer "
            "began marking healthy backend web servers as unhealthy because a "
            "signature falsely matched legitimate health-check traffic, which the "
            "sensor blocked in real time. Which change addresses this immediate "
            "operational issue while preserving threat detection capability?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tune or add an explicit allow rule for the health-check flow "
                    "on the sensor, or temporarily switch that segment to "
                    "detection-only mode until the signature is tuned"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Surgically tuning the false-positive signature or "
                    "carving out an exception for the specific legitimate flow "
                    "resolves the operational impact while keeping active "
                    "prevention in place for all other traffic."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the load balancer's health check failure threshold "
                    "so brief blocks no longer remove the server from rotation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This masks the symptom without fixing the "
                    "underlying false-positive block, and could also delay "
                    "detection of genuine server health problems."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Disable the sensor entirely to eliminate any further false "
                    "positives"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This removes all intrusion prevention capability "
                    "network-wide to solve a narrow, specific false-positive "
                    "issue — a disproportionate response."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Move the sensor from an inline placement to a permanent "
                    "tap/monitor-only span port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This does stop the false blocking, but it "
                    "permanently forfeits active, real-time prevention for all "
                    "traffic network-wide rather than surgically tuning or "
                    "exempting only the specific affected flow."
                ),
            },
        ],
        "explanation": (
            "The precise fix for a false-positive-driven blocking issue is to "
            "tune the offending signature or exempt the specific legitimate flow, "
            "preserving active prevention everywhere else rather than disabling "
            "or de-tuning protection network-wide."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "A company wants only corporate-managed laptops presenting a valid "
            "device certificate to gain full network access from wired conference "
            "room ports; unrecognized devices should be automatically placed on a "
            "restricted guest VLAN. Which control BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "802.1X port-based network access control using EAP-TLS "
                    "certificate authentication, with dynamic VLAN assignment "
                    "based on device identity/compliance"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 802.1X with EAP-TLS authenticates the device via "
                    "its certificate before granting access and can dynamically "
                    "assign the appropriate VLAN based on the result, exactly "
                    "matching this requirement."
                ),
            },
            {
                "id": "b",
                "text": "Static MAC address filtering configured on each switch port",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC addresses can be spoofed, and static "
                    "MAC filtering does not tie access to certificate-based "
                    "identity or support dynamic, compliance-based VLAN "
                    "assignment at scale."
                ),
            },
            {
                "id": "c",
                "text": "Administratively disabling all unused switch ports",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a good general attack-surface reduction "
                    "practice, but it does not provide conditional, identity-based "
                    "access control for the active conference room ports that "
                    "must remain enabled for use."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Port mirroring (SPAN) configured on the conference room "
                    "switch ports to monitor connected devices"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Port mirroring only copies traffic for monitoring "
                    "purposes; it does not authenticate devices or control "
                    "network access."
                ),
            },
        ],
        "explanation": (
            "802.1X with certificate-based EAP-TLS authentication and dynamic "
            "VLAN assignment is the standard control for granting differentiated, "
            "identity-based network access at the switch port."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A cloud provider must be able to programmatically create, modify, "
            "and tear down isolated tenant network segments across thousands of "
            "physical switches within seconds via API calls, without manually "
            "touching each device's configuration. Which architecture enables "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Software-defined networking (SDN) with a centralized "
                    "controller that separates the control plane from the data "
                    "plane"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SDN centralizes network control logic in a "
                    "controller that programmatically configures the data plane "
                    "across many devices, enabling rapid, API-driven segmentation "
                    "changes at scale."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Traditional VLAN trunking configured manually on each "
                    "physical switch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly the manual, per-device "
                    "configuration approach the provider is trying to avoid."
                ),
            },
            {
                "id": "c",
                "text": "Physically air-gapped networks dedicated to each tenant",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical air gaps provide strong isolation but "
                    "are not scalable, rapid, or programmatic — building separate "
                    "physical infrastructure per tenant is cost-prohibitive at "
                    "this scale."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A single flat network relying only on host-based firewalls "
                    "on each tenant VM"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This provides no true network-level tenant "
                    "isolation and relies entirely on endpoint controls, which "
                    "does not meet the requirement for rapid, centrally managed "
                    "segmentation."
                ),
            },
        ],
        "explanation": (
            "SDN's separation of the control plane from the data plane, managed "
            "through a centralized, API-driven controller, is what enables rapid, "
            "programmatic, large-scale network segmentation."
        ),
    },
    {
        "id": "nd3a-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "An organization has segmented its data center into VLANs by "
            "department (Finance, HR, Engineering). After an attacker compromised "
            "one host inside the Engineering VLAN, they moved laterally to every "
            "other host in that same VLAN unimpeded. Which architecture change "
            "would BEST limit this lateral movement going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Implement micro-segmentation with software-defined policies "
                    "enforcing least-privilege communication between individual "
                    "workloads, regardless of VLAN membership"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Micro-segmentation enforces least-privilege, "
                    "workload-to-workload policies that limit lateral movement "
                    "even between hosts on the same VLAN, directly addressing the "
                    "gap that traditional department-level VLANs left open."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Create additional VLANs to further subdivide Engineering by "
                    "team"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reduces the blast radius somewhat, but hosts "
                    "within each new sub-VLAN can still move laterally among "
                    "themselves unimpeded — it lacks the workload-level "
                    "granularity of micro-segmentation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy a next-generation firewall with deep packet "
                    "inspection at the network perimeter"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A perimeter NGFW inspects north-south traffic "
                    "entering and leaving the network; it does not address "
                    "east-west lateral movement occurring entirely within the "
                    "internal Engineering VLAN."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Move all Engineering workloads onto a single dedicated "
                    "physical network isolated from the rest of the enterprise"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This isolates Engineering from other "
                    "departments but does not solve the lateral movement problem "
                    "among hosts within Engineering itself, and is an extreme, "
                    "operationally costly measure."
                ),
            },
        ],
        "explanation": (
            "Micro-segmentation enforces least-privilege policies at the "
            "individual workload level, closing the lateral-movement gap that "
            "coarse VLAN-based segmentation leaves within a single segment."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "Two corporate data centers must exchange traffic securely across "
            "the public internet, with the entire original IP packet — including "
            "headers — encapsulated and encrypted so internal addressing is "
            "hidden from the transit network. Which configuration is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "IPSec in tunnel mode",
                "correct": True,
                "rationale": (
                    "Correct. Tunnel mode encrypts and encapsulates the entire "
                    "original IP packet, including headers, inside a new packet "
                    "— the standard configuration for site-to-site VPNs across "
                    "an untrusted network."
                ),
            },
            {
                "id": "b",
                "text": "IPSec in transport mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Transport mode encrypts only the payload and "
                    "leaves the original IP header exposed; it is typically used "
                    "for host-to-host communication within a trusted network, not "
                    "site-to-site tunnels over the internet."
                ),
            },
            {
                "id": "c",
                "text": "A TLS 1.3 connection established at the application layer",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS operates at a different layer and secures "
                    "individual application sessions; it is not the mechanism "
                    "used to encapsulate and encrypt whole IP packets for a "
                    "network-to-network site tunnel."
                ),
            },
            {
                "id": "d",
                "text": "A GRE tunnel without IPSec encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. GRE alone provides encapsulation and routing but "
                    "no encryption, so it does not provide the confidentiality "
                    "this requirement calls for."
                ),
            },
        ],
        "explanation": (
            "IPSec tunnel mode is required whenever the entire original IP "
            "packet, including its header, must be encapsulated and encrypted for "
            "transit across an untrusted network, as in a site-to-site VPN."
        ),
    },
    {
        "id": "nd3a-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "Remote employees connect via VPN client to reach internal file "
            "shares. Security policy requires that ALL of a remote user's "
            "internet-bound traffic — not just corporate traffic — be inspected "
            "by the on-premises secure web gateway for data loss prevention. "
            "Which VPN configuration satisfies this requirement, and what is its "
            "primary trade-off?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Full tunnel VPN, routing all traffic including general "
                    "internet browsing through the corporate network for "
                    "inspection, at the cost of increased latency and corporate "
                    "bandwidth/appliance load"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Only a full tunnel routes all of a remote user's "
                    "traffic through corporate infrastructure for inspection, "
                    "satisfying the policy — at the cost of added latency and "
                    "load on corporate bandwidth and security appliances."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Split tunnel VPN, routing only corporate-destined traffic "
                    "through the tunnel while general internet traffic exits "
                    "locally to preserve bandwidth"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Split tunneling leaves general internet traffic "
                    "uninspected by the corporate gateway, directly violating the "
                    "requirement that ALL internet-bound traffic be inspected."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Clientless SSL VPN restricted to browser-based access to "
                    "internal web portals only"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This limits access to specific internal web "
                    "applications and does not capture or route the user's "
                    "general internet-bound traffic for inspection at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Site-to-site IPSec VPN between the employee's home router "
                    "and the corporate gateway"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Site-to-site VPNs connect networks, not "
                    "individual remote users, and are impractical to provision "
                    "for each employee's home connection."
                ),
            },
        ],
        "explanation": (
            "Only a full tunnel configuration routes all remote user traffic "
            "through the corporate secure web gateway for inspection, trading "
            "added latency and appliance load for complete visibility — the "
            "opposite trade-off of a split tunnel."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "In a Zero Trust architecture, a user's access request to a "
            "sensitive application is evaluated in real time against identity, "
            "device posture, and contextual risk signals before a decision is "
            "rendered and enforced. Which two Zero Trust components are "
            "respectively responsible for making that decision and enforcing it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The policy decision point (PDP) makes the decision; the "
                    "policy enforcement point (PEP) enforces it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Per the NIST SP 800-207 Zero Trust model, the "
                    "policy decision point evaluates signals and renders the "
                    "access decision, while the policy enforcement point carries "
                    "out (enforces) that decision on the connection."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The policy enforcement point (PEP) makes the decision; the "
                    "policy decision point (PDP) enforces it"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the actual roles — the PDP decides "
                    "and the PEP enforces, not the other way around."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The control plane enforces access while the data plane "
                    "evaluates trust signals and renders decisions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is also reversed: the control plane is where "
                    "policy decisions are made, while the data plane carries and "
                    "enforces traffic handling based on those decisions."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A single unified policy engine performs both evaluation and "
                    "enforcement, eliminating the need to separate these "
                    "functions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Zero Trust architecture explicitly separates the "
                    "decision function from the enforcement function rather than "
                    "combining them into one component."
                ),
            },
        ],
        "explanation": (
            "Zero Trust architecture separates decision-making (policy decision "
            "point) from enforcement (policy enforcement point), evaluating "
            "identity, device, and contextual signals before granting or denying "
            "access on every request."
        ),
    },
    {
        "id": "nd3a-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "An organization wants to consolidate its branch office networking "
            "and security stack into a single cloud-delivered service that "
            "combines wide-area connectivity with security functions for users "
            "regardless of location. Which TWO technologies are core components "
            "typically converged within a SASE (Secure Access Service Edge) "
            "architecture? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "SD-WAN",
                "correct": True,
                "rationale": (
                    "Correct. SD-WAN provides the software-defined wide-area "
                    "connectivity layer that SASE converges with cloud-delivered "
                    "security services."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Security service edge functions such as ZTNA, secure web "
                    "gateway (SWG), and CASB"
                ),
                "correct": True,
                "rationale": (
                    "Correct. These cloud-delivered security functions are "
                    "converged with networking in a SASE architecture to secure "
                    "users regardless of location."
                ),
            },
            {
                "id": "c",
                "text": "A dedicated physical MPLS circuit terminating at each branch",
                "correct": False,
                "rationale": (
                    "Incorrect. SASE is specifically intended to reduce reliance "
                    "on costly, inflexible dedicated MPLS circuits in favor of "
                    "internet-based SD-WAN transport, not to add more of them."
                ),
            },
            {
                "id": "d",
                "text": "An on-premises hardware HSM cluster for key management",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware security modules are a separate "
                    "cryptographic key-management category and are not a core "
                    "component of the SASE convergence model."
                ),
            },
            {
                "id": "e",
                "text": "A physically air-gapped backup network segment",
                "correct": False,
                "rationale": (
                    "Incorrect. Air-gapping is a physical segmentation strategy "
                    "unrelated to the cloud-delivered networking-and-security "
                    "convergence that defines SASE."
                ),
            },
        ],
        "explanation": (
            "SASE converges SD-WAN connectivity with a suite of cloud-delivered "
            "security service edge functions (ZTNA, SWG, CASB, FWaaS), replacing "
            "dedicated circuits and on-premises point solutions rather than "
            "adding to them."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-025",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification",
        "stem": (
            "A private hospital system classifies data using the labels Public, "
            "Internal, Confidential, and Restricted. Patient PHI records — whose "
            "unauthorized disclosure would trigger regulatory fines, patient "
            "harm, and reputational damage, and which only a small, named group "
            "of clinicians may access on a strict need-to-know basis — should "
            "receive which classification?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Restricted",
                "correct": True,
                "rationale": (
                    "Correct. Restricted is reserved for the organization's most "
                    "tightly controlled data, limited to a narrow, named group of "
                    "individuals on strict need-to-know — matching the PHI "
                    "handling requirements described."
                ),
            },
            {
                "id": "b",
                "text": "Confidential",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidential is serious enough for many sensitive "
                    "business records, but this scheme reserves an even stricter "
                    "\"Restricted\" tier specifically for data limited to a "
                    "narrow, named group — a tighter control than the broader "
                    "business need-to-know that Confidential typically allows."
                ),
            },
            {
                "id": "c",
                "text": "Internal",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal data is meant for general employee use "
                    "and is far too permissive a label for regulated PHI with "
                    "strict access limitations."
                ),
            },
            {
                "id": "d",
                "text": "Public",
                "correct": False,
                "rationale": (
                    "Incorrect. Public data carries no disclosure risk at all, "
                    "which is the opposite of PHI subject to regulatory "
                    "protection."
                ),
            },
        ],
        "explanation": (
            "When an organization's classification scheme includes a tier "
            "explicitly reserved for the narrowest, named-individual, need-to-"
            "know access, regulated data like PHI with severe harm/legal impact "
            "belongs at that highest (Restricted) tier."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-026",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A QA team needs a test data set derived from production customer "
            "records. Developers must never be able to recover the real values, "
            "but the substitute data must preserve the original format (length "
            "and character types) so that application logic under test continues "
            "to function correctly. Which method BEST satisfies both "
            "requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Static data masking that generates realistic, format-"
                    "preserving substitute values with no way to reverse them to "
                    "the originals"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Static masking permanently replaces production "
                    "values with realistic, correctly formatted substitutes and "
                    "provides no mechanism to recover the originals, matching "
                    "both requirements exactly."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Encrypt the columns with AES-256 and give developers a "
                    "shared decryption key so the data can be reversed if needed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Providing developers a decryption key means they "
                    "can still recover the real customer data, violating the "
                    "requirement that they must never access the original values."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Tokenize each value, mapping it in a secure vault that the "
                    "production application can later detokenize"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization is designed for cases where a "
                    "production system needs to detokenize values later for a "
                    "business transaction; maintaining a reversible vault mapping "
                    "introduces unnecessary risk for one-way test data that never "
                    "needs to be reversed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Hash each field with SHA-256 so the same input always "
                    "produces the same output"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is one-way and non-reversible, but it "
                    "does not preserve the original format — a hashed 16-digit "
                    "card number no longer looks like one — breaking application "
                    "logic that depends on realistic, correctly formatted values."
                ),
            },
        ],
        "explanation": (
            "Static data masking is the method purpose-built to produce "
            "irreversible, format-preserving substitute data for non-production "
            "environments like QA and development."
        ),
    },
    {
        "id": "nd3a-027",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Data protection methods",
        "stem": (
            "A company must protect a database column containing customers' full "
            "payment card numbers so that (1) the original card number can be "
            "recovered later by the payment processor when needed for a refund, "
            "and (2) if the database file itself is stolen, the numbers remain "
            "unreadable without a separate key or vault the attacker did not "
            "obtain. Which TWO controls, used together, satisfy BOTH "
            "requirements? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Format-preserving tokenization, replacing the card number "
                    "with a token and storing the mapping in a separate, "
                    "access-controlled token vault"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tokenization allows the original value to be "
                    "recovered later (via the vault) for legitimate business use "
                    "like refunds, while the token itself reveals nothing about "
                    "the original value if the database is stolen without the "
                    "vault."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Column-level AES encryption (or transparent database "
                    "encryption) protecting the data at rest, with keys stored in "
                    "a separate KMS/HSM"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Encryption allows authorized recovery of the "
                    "original value using the key, while ensuring the data is "
                    "unreadable if the database file is stolen without also "
                    "compromising the separately stored key."
                ),
            },
            {
                "id": "c",
                "text": "One-way hashing of the card number",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is irreversible by design, so the "
                    "original card number could never be recovered for a refund, "
                    "failing the first requirement."
                ),
            },
            {
                "id": "d",
                "text": "Static data masking of the column",
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking is meant to permanently and "
                    "irreversibly obscure values for display or non-production "
                    "use; it is not designed to let an authorized process later "
                    "recover the original card number."
                ),
            },
            {
                "id": "e",
                "text": "Labeling the column \"Restricted\" in the data classification scheme",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification labeling documents handling "
                    "requirements but provides no actual cryptographic or "
                    "structural protection of the data itself."
                ),
            },
        ],
        "explanation": (
            "Tokenization and encryption are both reversible-by-design "
            "protections that can satisfy an authorized-recovery requirement "
            "while still protecting stolen data, unlike hashing or masking, which "
            "are intentionally irreversible."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-028",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data states",
        "stem": (
            "Malware on a point-of-sale terminal scrapes credit card numbers "
            "directly from RAM immediately after they are decrypted for "
            "processing, despite the data being encrypted both in transit and at "
            "rest. Which data state is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data in use",
                "correct": True,
                "rationale": (
                    "Correct. Data being actively processed in memory — after "
                    "decryption but before re-encryption or transmission — is "
                    "\"data in use,\" and this is the state RAM-scraping malware "
                    "exploits."
                ),
            },
            {
                "id": "b",
                "text": "Data at rest",
                "correct": False,
                "rationale": (
                    "Incorrect. Data at rest describes stored data, such as on "
                    "disk, which the scenario already states is encrypted and "
                    "not the target of this attack."
                ),
            },
            {
                "id": "c",
                "text": "Data in transit",
                "correct": False,
                "rationale": (
                    "Incorrect. Data in transit describes data moving across a "
                    "network, which the scenario already states is encrypted and "
                    "not what is being scraped from RAM."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Data in motion, since RAM is a volatile, constantly "
                    "changing medium"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. \"Data in motion\" is essentially synonymous with "
                    "data in transit across a network, not a reference to "
                    "memory's volatility; data actively being processed in memory "
                    "is properly termed data in use."
                ),
            },
        ],
        "explanation": (
            "Data in use refers to data actively being processed in memory, "
            "which is unencrypted at that moment even when it is protected at "
            "rest and in transit — the exact gap RAM-scraping malware targets."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-029",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "Call center representatives need to see only the last four digits "
            "of a customer's card number to verify identity during a call, and "
            "must never see the full card number. Which technique BEST satisfies "
            "this display requirement with the least operational complexity?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Dynamic data masking that displays only the last four "
                    "digits of the card number in the call center application "
                    "while the full value remains stored server-side"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Dynamic masking directly and simply satisfies the "
                    "partial-display need, showing only the last four digits "
                    "while keeping the full value protected and stored "
                    "server-side."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Tokenization, replacing the card number with a randomly "
                    "generated token before it is ever displayed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A token on its own does not preserve the "
                    "recognizable last-four-digit format the representative "
                    "needs; achieving a partial reveal would require an "
                    "additional detokenization step, making it more complex than "
                    "simple masking for this specific display need."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Field-level encryption, with the call center application "
                    "decrypting the full value on screen for verification"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Decrypting and fully displaying the card number "
                    "exposes the entire value to the representative, which "
                    "directly violates the requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Truncation at the database layer, permanently storing only "
                    "the last four digits"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Permanently discarding the rest of the card "
                    "number destroys its availability for other legitimate "
                    "business needs, such as processing or refunds — an "
                    "irreversible loss beyond what this display-only requirement "
                    "calls for."
                ),
            },
        ],
        "explanation": (
            "Dynamic data masking is designed precisely for controlling how much "
            "of a sensitive value is displayed to a given user role, while the "
            "full value remains intact and protected elsewhere."
        ),
    },
    {
        "id": "nd3a-030",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A payment processor's tokenization system generates tokens using a "
            "simple, unsalted sequential counter, with the mapping table stored "
            "on the same server as the token vault application itself. Which "
            "weakness MOST undermines the security benefit of tokenization in "
            "this design?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The token vault (mapping table) is not adequately isolated "
                    "from systems that can access it, so compromising that one "
                    "system reverses every token back to its original card "
                    "number"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tokenization's security depends entirely on "
                    "keeping the vault mapping tokens to original values "
                    "isolated and tightly access-controlled; co-locating it with "
                    "the vault application removes that isolation and creates a "
                    "single point of total compromise."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Tokenization inherently provides weaker protection than "
                    "masking regardless of implementation, since masking is "
                    "unrecoverable while tokens can always be reversed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This overgeneralizes: tokenization's security "
                    "depends on how well the vault is protected, not on an "
                    "inherent weakness compared to masking, and the two "
                    "techniques serve different requirements (recoverable versus "
                    "irreversible)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Sequential, unsalted token values allow attackers to "
                    "perform frequency analysis and directly guess the "
                    "underlying card numbers from the token values themselves"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Unlike weak hashing, tokens are typically "
                    "arbitrary surrogate values assigned via table lookup rather "
                    "than derived mathematically from the input, so analyzing "
                    "the token values alone does not reveal the original card "
                    "numbers; the real risk here is vault exposure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "PCI DSS prohibits the use of tokenization for cardholder "
                    "data entirely, requiring encryption instead"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is factually false — PCI DSS explicitly "
                    "recognizes tokenization as an acceptable control that can "
                    "reduce compliance scope for cardholder data."
                ),
            },
        ],
        "explanation": (
            "Tokenization's security rests entirely on strict isolation and "
            "access control of the token vault mapping; failing to isolate that "
            "vault — not the token generation method or an inherent weakness "
            "versus masking — is what undermines this design."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-031",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A company performs a full backup every Sunday. It needs the fastest "
            "possible restore time in the event of a Thursday failure, and can "
            "accept only a moderate increase in daily backup storage and time "
            "compared to the alternative. Which backup strategy should be used "
            "for the remaining six days of the week?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Differential backups each day, capturing all changes since "
                    "the last full backup"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Restoring from a differential backup requires only "
                    "the last full backup plus the single most recent "
                    "differential, giving faster restores than incremental chains "
                    "while adding only a moderate daily storage/time cost."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Incremental backups each day, capturing only changes since "
                    "the previous backup"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Incremental backups use less storage and time "
                    "daily, but restoring requires the full backup plus every "
                    "incremental since, making restores slower — the opposite of "
                    "the stated priority."
                ),
            },
            {
                "id": "c",
                "text": "A second full backup performed every day in addition to Sunday's",
                "correct": False,
                "rationale": (
                    "Incorrect. While daily fulls would restore fastest, they far "
                    "exceed the \"moderate increase\" in storage and backup time "
                    "the requirement allows, making this the most resource-"
                    "intensive option rather than a moderate one."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Continuous data protection (CDP), journaling every "
                    "transaction in real time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CDP offers very fine-grained recovery points but "
                    "introduces a level of infrastructure complexity and resource "
                    "demand beyond the \"moderate increase\" the scenario calls "
                    "for, when a simpler daily strategy meets the stated need."
                ),
            },
        ],
        "explanation": (
            "Differential backups strike the balance the scenario calls for: "
            "faster restores than incrementals, at only a moderate storage/time "
            "cost compared to running additional full backups or continuous "
            "journaling."
        ),
    },
    {
        "id": "nd3a-032",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backups and replication",
        "stem": (
            "A bank replicates its transaction database between a primary data "
            "center and a secondary site 500 miles away. Regulation mandates a "
            "recovery point objective (RPO) of zero — no data loss is acceptable "
            "— even though this may occasionally slow transaction commit times "
            "due to distance-induced latency. Which replication method should be "
            "used?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Synchronous replication, writing to both sites before "
                    "acknowledging a transaction as committed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Synchronous replication only confirms a transaction "
                    "once it is written at both sites, guaranteeing zero data "
                    "loss (RPO of zero) at the cost of added commit latency — "
                    "exactly the trade-off the mandate accepts."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Asynchronous replication, acknowledging the transaction "
                    "locally and forwarding it to the secondary site shortly "
                    "after to avoid latency-driven performance impact"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Asynchronous replication permits a small window "
                    "of unreplicated data that could be lost in a failure, "
                    "violating the mandated zero-data-loss requirement — this is "
                    "the trade-off the scenario says must be avoided."
                ),
            },
            {
                "id": "c",
                "text": "Snapshot-based replication taken every 15 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. This allows up to 15 minutes of data loss between "
                    "snapshots, far exceeding an RPO of zero."
                ),
            },
            {
                "id": "d",
                "text": "Journaling-based log shipping replicated once per hour in batch",
                "correct": False,
                "rationale": (
                    "Incorrect. Hourly batch shipping creates a large potential "
                    "data-loss window, which does not satisfy a zero RPO "
                    "requirement."
                ),
            },
        ],
        "explanation": (
            "A zero RPO mandate requires synchronous replication, which confirms "
            "writes at both sites before committing, trading transaction latency "
            "for guaranteed zero data loss."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-033",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "An application cluster must use all provisioned server capacity to "
            "handle normal daily load, with no idle standby resources, while "
            "still automatically continuing operations without service "
            "interruption if one node fails. Which HA cluster configuration "
            "should be used?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Active-active clustering, with all nodes actively processing "
                    "load-balanced traffic and absorbing a failed node's share "
                    "instantly"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Active-active clustering uses every node to serve "
                    "traffic during normal operation, with the remaining nodes "
                    "absorbing load if one fails — matching both the "
                    "full-utilization and no-interruption requirements."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Active-passive clustering, with a fully provisioned standby "
                    "node sitting idle until a failover event occurs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Active-passive guarantees failover but leaves "
                    "standby capacity unused during normal operations, violating "
                    "the requirement to utilize all provisioned capacity."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Cold site standby, with a secondary node powered off until "
                    "manually activated during a failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Manual activation introduces significant delay, "
                    "which directly contradicts the requirement for automatic "
                    "continuation without service interruption."
                ),
            },
            {
                "id": "d",
                "text": (
                    "N+1 redundancy with a single dedicated spare node reserved "
                    "above normal capacity needs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reserving a spare node above what daily load "
                    "requires still leaves capacity idle during normal "
                    "operations, violating the full-utilization requirement."
                ),
            },
        ],
        "explanation": (
            "Active-active clustering is the only configuration that both fully "
            "utilizes all provisioned capacity under normal load and provides "
            "seamless, automatic failover if a node fails."
        ),
    },
    {
        "id": "nd3a-034",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "High availability",
        "stem": (
            "A load balancer distributes requests round-robin across three "
            "active, healthy web servers. Users report their shopping carts are "
            "randomly emptied mid-session even though no failover event has "
            "occurred and all servers remain healthy. Which load balancer "
            "configuration change would BEST resolve this while preserving the "
            "benefits of active-active high availability?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Enable session persistence (sticky sessions), or migrate "
                    "session state to a shared centralized store accessible by "
                    "all nodes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The root cause is that session/cart state is not "
                    "shared or pinned across nodes; enabling sticky sessions or "
                    "centralizing session storage keeps a user's requests "
                    "consistent with their cart data while still load balancing "
                    "across all active servers."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Switch to an active-passive configuration so only one "
                    "server ever serves live traffic at a time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the active-active load "
                    "distribution and capacity benefit entirely to solve what is "
                    "actually a session-state design problem, not a capacity or "
                    "failover problem."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Reduce the load balancer's health check interval so "
                    "unhealthy servers are detected and removed faster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. All servers are reported healthy; the issue is "
                    "unrelated to health check timing and is instead caused by a "
                    "lack of session affinity or shared state."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure round-robin with weighted server priority based "
                    "on CPU load"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Weighting distribution by CPU load is a "
                    "performance-tuning change that does nothing to address the "
                    "actual root cause: session state not being shared or "
                    "pinned across nodes."
                ),
            },
        ],
        "explanation": (
            "Randomly losing session/cart data across an active-active pool "
            "points to missing session persistence or shared session state, "
            "which sticky sessions or centralized session storage resolve "
            "without sacrificing active-active load distribution."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-035",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multi-cloud and platform diversity",
        "stem": (
            "A business wants to avoid vendor lock-in and reduce the risk that a "
            "single cloud provider's outage takes down its entire service. It is "
            "willing to accept the added operational complexity of managing two "
            "different providers' APIs and tooling. Which strategy BEST achieves "
            "this, and what is its primary trade-off?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Multi-cloud deployment across two independent cloud "
                    "providers, trading increased operational and tooling "
                    "complexity for provider-outage resilience and reduced "
                    "vendor lock-in"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Multi-cloud is the only option that spreads risk "
                    "across truly independent providers, directly addressing "
                    "both vendor lock-in and provider-wide outage risk, at the "
                    "accepted cost of managing multiple platforms."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploying across multiple availability zones within a "
                    "single provider's region, trading minimal added complexity "
                    "for protection against zone or provider-wide outages"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Multiple AZs protect against a single zone "
                    "failure but not a full provider-wide platform outage, and "
                    "remain entirely dependent on one vendor — failing to reduce "
                    "vendor lock-in as required."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploying across multiple regions within a single cloud "
                    "provider, trading data sovereignty and latency "
                    "considerations for protection against a single region "
                    "failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This improves regional resilience but still "
                    "relies on one provider, so it does nothing to reduce the "
                    "vendor lock-in risk explicitly stated as a goal."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Using a single provider's hybrid cloud, connecting "
                    "on-premises infrastructure to that provider's public cloud"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The public cloud portion remains tied to a "
                    "single vendor, so this does not address cross-provider "
                    "vendor lock-in risk."
                ),
            },
        ],
        "explanation": (
            "Only a true multi-cloud strategy, spanning independent providers, "
            "reduces both vendor lock-in and the risk of a single provider's "
            "outage taking down the service, at the cost of added tooling and "
            "operational complexity."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-036",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Power resilience",
        "stem": (
            "A data center's utility power fails during a storm. The facility "
            "must bridge the gap between the outage and generator startup "
            "without any interruption to running servers, and must also be able "
            "to keep running for an extended, unpredictable duration if the "
            "storm knocks out utility power for days. Which combination of "
            "controls addresses BOTH needs?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An uninterruptible power supply (UPS) for instantaneous, "
                    "gap-free power during the brief transition, paired with a "
                    "fuel-resupplied generator for extended runtime"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The UPS bridges the immediate gap with zero "
                    "interruption while the generator starts, and the generator "
                    "then provides sustained power for as long as fuel can be "
                    "resupplied — covering both the instant-transition and "
                    "extended-outage requirements."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A dual-supply/redundant power feed from two separate "
                    "utility substations, without a generator or UPS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A regional storm can affect both utility feeds "
                    "simultaneously, and this option provides no protection "
                    "against a total utility outage of unpredictable duration."
                ),
            },
            {
                "id": "c",
                "text": "A generator alone, sized for extended runtime, without a UPS",
                "correct": False,
                "rationale": (
                    "Incorrect. Generators take time to start and stabilize, so "
                    "without a UPS, servers would still experience a power "
                    "interruption during that startup gap."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A UPS alone, sized with additional battery capacity for "
                    "several hours"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Battery capacity is finite and cannot sustain the "
                    "facility for a multi-day outage the way a fuel-resupplied "
                    "generator can, failing the extended-runtime requirement."
                ),
            },
        ],
        "explanation": (
            "A UPS provides the instantaneous, gap-free bridge power a "
            "generator cannot supply during its startup delay, while the "
            "generator provides the sustained runtime a UPS's finite battery "
            "cannot — together covering both requirements."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-037",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "An organization has a recovery time objective (RTO) of 4 hours and "
            "a moderate budget that cannot support a fully mirrored, real-time-"
            "synchronized duplicate data center, but also cannot tolerate the "
            "days-long recovery time of building a bare facility from scratch. "
            "Which recovery site type BEST matches these constraints?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Warm site, with facility, hardware, and connectivity already "
                    "in place and periodically updated data, requiring some final "
                    "configuration and data sync before cutover"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A warm site's pre-installed infrastructure with "
                    "periodic data updates can realistically achieve a 4-hour "
                    "RTO at a moderate cost, between the extremes of hot and "
                    "cold sites."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Hot site, fully redundant and continuously synchronized, "
                    "ready for immediate failover"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A hot site would easily meet the 4-hour RTO, but "
                    "it is the most expensive recovery site option, exceeding the "
                    "stated moderate-budget constraint."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Cold site, with basic facility, power, and connectivity but "
                    "no pre-installed hardware or data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Procuring hardware and restoring data from "
                    "scratch takes far longer than 4 hours, failing the RTO "
                    "requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Reciprocal agreement with a partner organization to use "
                    "their data center space during a disaster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While often low-cost, reciprocal agreements "
                    "introduce significant uncertainty around capacity "
                    "contention, reliability, and configuration readiness, none "
                    "of which is guaranteed to meet a firm 4-hour RTO."
                ),
            },
        ],
        "explanation": (
            "A warm site occupies the middle ground between a hot site's cost "
            "and a cold site's slow recovery, making it the standard fit for a "
            "moderate RTO and moderate budget."
        ),
    },
    {
        "id": "nd3a-038",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "A company's primary data center is in a coastal, hurricane-prone "
            "region. Leadership wants a disaster recovery site far enough away "
            "to avoid being affected by the same hurricane or regional power "
            "grid failure, but the CFO is concerned about the added network "
            "latency and data sovereignty/legal implications of selecting a site "
            "in a different country. Which approach BEST balances these "
            "concerns?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Select a geographically dispersed DR site in a different "
                    "inland region within the same country, far enough to avoid "
                    "shared weather and grid risk while avoiding cross-border "
                    "data sovereignty issues"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An inland site in a different region provides "
                    "sufficient geographic dispersion from a coastal hurricane "
                    "and its regional grid, while staying within the same "
                    "country avoids the cross-border legal and data sovereignty "
                    "concerns the CFO raised."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Select a DR site in the nearest adjacent city to minimize "
                    "replication latency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A nearby city is likely within the same "
                    "hurricane and regional power grid impact zone, defeating "
                    "the purpose of geographic dispersion."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Select a DR site on a different continent to maximize "
                    "distance and disaster independence"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While this maximizes disaster independence, it "
                    "ignores the CFO's explicitly stated concern about "
                    "cross-border data sovereignty and legal implications."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Co-locate the DR site in the same building on a separate "
                    "floor with independent power feeds"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The same building remains vulnerable to the same "
                    "regional hurricane or citywide grid failure, so this is not "
                    "true geographic dispersion."
                ),
            },
        ],
        "explanation": (
            "Choosing an inland site in a different region of the same country "
            "provides real geographic dispersion from a regional disaster while "
            "avoiding the added latency and legal complexity of a cross-border "
            "DR site."
        ),
    },
    # ------------------------------------------------------------------ #
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-039",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Resilience testing",
        "stem": (
            "A disaster recovery program includes two distinct validation "
            "activities: (1) stakeholders sit in a conference room and verbally "
            "walk through their roles during a hypothetical ransomware outbreak "
            "without touching any live systems, and (2) the DR team actually "
            "shuts down the primary production database and confirms the "
            "secondary site fully takes over live traffic. Which TWO resilience "
            "testing types are being described, respectively? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tabletop exercise",
                "correct": True,
                "rationale": (
                    "Correct. A tabletop exercise is a discussion-based "
                    "walkthrough of roles and responses to a hypothetical "
                    "incident, without touching any live systems — matching "
                    "activity 1."
                ),
            },
            {
                "id": "b",
                "text": "Full failover (live) test",
                "correct": True,
                "rationale": (
                    "Correct. A full failover test actually shifts live "
                    "production traffic to the secondary site to validate real "
                    "cutover — matching activity 2."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Parallel processing test, where the DR site processes "
                    "production data alongside the primary without cutting over"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A parallel test validates the DR environment's "
                    "output without ever cutting live traffic over to it, which "
                    "does not match activity 2's description of the secondary "
                    "site fully taking over live traffic."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Simulation test, where a mock incident is technically "
                    "injected into an isolated, non-production copy of the "
                    "environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A simulation test involves technical injection "
                    "into an isolated environment, which matches neither the "
                    "purely verbal, systems-untouched nature of activity 1 nor "
                    "the live production cutover described in activity 2."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Checklist review, where teams individually confirm document "
                    "currency without group discussion"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A checklist review is a passive, individual "
                    "document check, lacking the collaborative group walkthrough "
                    "and discussion described in activity 1."
                ),
            },
        ],
        "explanation": (
            "Tabletop exercises validate plans through discussion alone, while "
            "full failover tests validate the actual mechanics of a live cutover "
            "— distinct from parallel tests, simulations, or passive checklist "
            "reviews, which describe different levels of technical rigor."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3a-040",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "Two companies are co-investing in and jointly building a shared "
            "data center facility. They need an agreement that formally and "
            "legally defines ownership percentages and financial responsibilities "
            "of this joint venture. Which agreement type BEST fulfills this "
            "need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Business partnership agreement (BPA)",
                "correct": True,
                "rationale": (
                    "Correct. A BPA is the legally binding agreement that "
                    "formally defines the terms of a business partnership, "
                    "including ownership stakes and financial responsibilities "
                    "of a joint venture like this shared facility."
                ),
            },
            {
                "id": "b",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines measurable performance and "
                    "uptime commitments for a service; it does not establish "
                    "joint ownership or financial partnership terms."
                ),
            },
            {
                "id": "c",
                "text": "Memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents mutual intent and general goals "
                    "between parties, but it is typically non-binding and less "
                    "formal than what is needed to legally define binding "
                    "ownership and financial responsibilities of a joint venture."
                ),
            },
            {
                "id": "d",
                "text": "Non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA only protects confidential information "
                    "exchanged between parties and does not address ownership or "
                    "financial structure."
                ),
            },
        ],
        "explanation": (
            "A business partnership agreement is the legally binding document "
            "purpose-built to define ownership stakes and financial "
            "responsibilities in a joint venture, unlike the weaker, non-binding "
            "MOU or the narrowly scoped SLA and NDA."
        ),
    },
]
