"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file G.

37 scenario-driven questions (33 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 3 in
``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Architecture trade-offs (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A logistics company's route-optimization engine currently runs on "
            "a single very large on-premises server. As demand grows, the "
            "architecture team is deciding between vertically scaling "
            "(replacing the server with an even larger one) and horizontally "
            "scaling (distributing the workload across many smaller, "
            "redundant servers behind a load balancer). Which trade-off BEST "
            "justifies choosing the horizontal (scale-out) approach from a "
            "security and availability standpoint?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Horizontal scaling eliminates the single point of "
                    "failure of one large server, but requires additional "
                    "engineering effort to manage state consistency and "
                    "synchronization across nodes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Distributing load across many redundant nodes "
                    "removes the single-server failure point, at the cost of "
                    "the added complexity of keeping state consistent across "
                    "those nodes — the classic scale-out trade-off."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Vertical scaling is inherently more resilient because a "
                    "single larger server can never experience hardware "
                    "failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Any single server, regardless of size, remains "
                    "a single point of failure; hardware failure is always "
                    "possible."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Horizontal scaling reduces the attack surface because "
                    "there is only one system administrators must patch and "
                    "harden"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The opposite is true — horizontal scaling adds "
                    "more hosts that each must be patched and hardened, "
                    "increasing the attack surface, not reducing it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Vertical scaling allows the application to continue "
                    "serving requests uninterrupted while the single server "
                    "is taken offline for the upgrade"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Upgrading a single vertically scaled server "
                    "typically requires downtime to swap or expand hardware, "
                    "unlike a horizontally scaled pool where individual nodes "
                    "can be replaced without interrupting service."
                ),
            },
        ],
        "explanation": (
            "Scale-out (horizontal) architectures trade added state-"
            "synchronization complexity for the elimination of a single-"
            "server failure point and the ability to perform rolling "
            "maintenance without downtime, while scale-up (vertical) "
            "architectures keep things simple but remain a single point of "
            "failure requiring downtime to upgrade."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company keeps its primary customer database, containing "
            "regulated financial records, on dedicated on-premises servers to "
            "satisfy a data residency requirement. During its month-end "
            "reporting period, the web front-end experiences a tenfold "
            "increase in traffic, so the company temporarily provisions "
            "additional web servers in a public cloud provider to absorb the "
            "spike, then decommissions them afterward. Which cloud "
            "architecture concept does this scenario BEST describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hybrid cloud with cloud bursting",
                "correct": True,
                "rationale": (
                    "Correct. Keeping regulated data on-premises while "
                    "temporarily bursting overflow web capacity into a public "
                    "cloud provider during a demand spike is the textbook "
                    "definition of hybrid cloud with cloud bursting."
                ),
            },
            {
                "id": "b",
                "text": "Community cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. A community cloud is shared infrastructure "
                    "used by multiple organizations with common concerns; "
                    "nothing in this scenario describes shared tenancy among "
                    "peer organizations."
                ),
            },
            {
                "id": "c",
                "text": "Multi-cloud redundancy",
                "correct": False,
                "rationale": (
                    "Incorrect. Multi-cloud redundancy means actively running "
                    "workloads across two or more providers to survive an "
                    "outage, not temporarily bursting capacity to one "
                    "provider while the core system stays on-premises."
                ),
            },
            {
                "id": "d",
                "text": "Software as a Service (SaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. The company is provisioning its own web "
                    "servers, not consuming a third-party vendor's finished "
                    "software application."
                ),
            },
        ],
        "explanation": (
            "Hybrid cloud architectures let an organization keep regulated "
            "or sensitive workloads on-premises while dynamically bursting "
            "elastic, less-sensitive workloads into a public cloud to handle "
            "temporary demand spikes."
        ),
    },
    {
        "id": "nd3g-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company's employees use a SaaS email platform. An employee "
            "grants a malicious third-party OAuth application broad read/send "
            "permissions to their mailbox after clicking a phishing link. The "
            "SaaS provider's infrastructure, patching, and platform-level "
            "security were never compromised. Under the shared responsibility "
            "model, whose responsibility was it to prevent this incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer organization, because monitoring and "
                    "restricting third-party application permissions granted "
                    "within a SaaS platform is a customer-side responsibility, "
                    "not the provider's"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In SaaS, the provider secures the underlying "
                    "platform and infrastructure, but governance over user "
                    "behavior, identity, and third-party app authorizations "
                    "within that platform remains the customer's "
                    "responsibility."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The SaaS provider, because it is solely responsible for "
                    "the security of all data and configurations within its "
                    "platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Even in SaaS, where the provider carries the "
                    "largest share of responsibility, the customer still owns "
                    "identity, access, and data governance decisions such as "
                    "which third-party apps to authorize."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Neither party, because OAuth application consent "
                    "phishing is not addressed by the shared responsibility "
                    "model"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Identity and access governance, including "
                    "third-party application consent, is explicitly a "
                    "customer responsibility under the shared responsibility "
                    "model."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The third-party application developer exclusively, since "
                    "the provider and customer share no responsibility once "
                    "an external app is involved"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The shared responsibility model does not "
                    "transfer all obligation to an external developer; the "
                    "customer remains responsible for what it authorizes "
                    "within its own tenant."
                ),
            },
        ],
        "explanation": (
            "Even in the most provider-managed cloud service model (SaaS), "
            "the customer retains responsibility for identity governance, "
            "access decisions, and data within its tenant — including which "
            "third-party OAuth applications employees are permitted to "
            "authorize."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A nuclear power facility needs to send real-time turbine "
            "telemetry from its isolated OT/SCADA network to a corporate "
            "historian database on the IT network for analytics, but "
            "engineers must guarantee that it is physically impossible for "
            "any traffic, malware, or command to travel from the IT network "
            "back into the OT network. Which control BEST satisfies this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A unidirectional security gateway (data diode)",
                "correct": True,
                "rationale": (
                    "Correct. A data diode enforces one-way data flow at the "
                    "hardware level, making reverse traffic physically "
                    "impossible rather than merely blocked by policy — "
                    "exactly what the physical-impossibility requirement "
                    "calls for."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A stateful firewall configured with a deny-all inbound "
                    "rule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A firewall rule is a software policy that can "
                    "be misconfigured, bypassed, or defeated by a "
                    "vulnerability; it does not make reverse traffic "
                    "physically impossible."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A site-to-site IPSec VPN tunnel between the OT and IT "
                    "networks"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN tunnel is bidirectional by design and "
                    "would actually create a path for traffic to flow back "
                    "into the OT network, the opposite of what is required."
                ),
            },
            {
                "id": "d",
                "text": (
                    "An air-gapped network with a manual sneakernet USB "
                    "transfer process"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A sneakernet process cannot deliver "
                    "real-time telemetry as the scenario requires, and "
                    "introduces its own removable-media risk."
                ),
            },
        ],
        "explanation": (
            "Data diodes (unidirectional gateways) are the standard OT/ICS "
            "control for guaranteeing one-way data flow out of a safety- or "
            "reliability-critical control network when even a software "
            "firewall's policy-based enforcement is not considered "
            "sufficient assurance."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IoT security",
        "stem": (
            "Thousands of a vendor's internet-connected security cameras "
            "were recruited into a massive botnet after attackers scanned the "
            "internet for devices still using the factory-default Telnet "
            "administrative credentials, then used them to launch a "
            "distributed denial-of-service attack. Which combination of "
            "controls would have BEST prevented these specific cameras from "
            "being compromised?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Forcing a unique credential change during initial setup "
                    "and placing the cameras on an isolated network segment "
                    "with no direct internet exposure"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Eliminating default credentials removes the "
                    "exact weakness the attackers scanned for, and isolating "
                    "the cameras from direct internet reachability removes "
                    "the exposure that let attackers find and reach them in "
                    "the first place."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increasing the video resolution and frame rate "
                    "encryption strength used by the cameras"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Video stream quality or encryption has no "
                    "bearing on whether the administrative Telnet interface "
                    "still accepts default credentials."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Relying on the cameras' built-in motion-detection AI to "
                    "flag unauthorized access attempts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Motion detection analyzes video content, not "
                    "network authentication attempts, and provides no "
                    "prevention against credential-based compromise."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configuring the cameras to auto-update firmware directly "
                    "from the internet without administrator review"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Unreviewed automatic updates do not address "
                    "the default-credential weakness or direct internet "
                    "exposure, and blindly trusting vendor push updates "
                    "introduces its own supply-chain risk."
                ),
            },
        ],
        "explanation": (
            "Mirai-style IoT botnets are built almost entirely by scanning "
            "for devices still using factory-default credentials and reaching "
            "them directly over the internet; changing default credentials "
            "and isolating IoT devices on a segmented network defeats both "
            "prerequisites."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A platform team's CI/CD pipeline currently builds container "
            "images and pushes them straight to the production registry with "
            "no automated check for known-vulnerable packages. Which control "
            "would MOST effectively catch vulnerable dependencies before they "
            "ever reach production?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Integrating an automated container image vulnerability "
                    "scanner as a required, blocking stage in the CI/CD build "
                    "pipeline"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Scanning images for known-vulnerable packages "
                    "as a blocking build-pipeline stage catches the problem "
                    "before an image can ever reach the production registry, "
                    "shifting the check left."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Running a vulnerability scanner against the live "
                    "production containers once per quarter"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Quarterly scanning after deployment finds "
                    "vulnerabilities only after they are already running in "
                    "production, and leaves long gaps between checks."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Requiring developers to manually document which "
                    "third-party packages they used in each image"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Manual documentation does not detect known "
                    "vulnerabilities and is purely administrative record-"
                    "keeping."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enabling verbose application logging inside each "
                    "container to record runtime errors"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Runtime error logging captures application "
                    "behavior, not known vulnerabilities in the packages "
                    "baked into the image."
                ),
            },
        ],
        "explanation": (
            "Automated image scanning integrated as a blocking CI/CD stage "
            "is the standard 'shift-left' control for catching known-"
            "vulnerable dependencies before a container image is ever "
            "pushed to a production registry."
        ),
    },
    {
        "id": "nd3g-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A platform engineering team is hardening its container runtime "
            "configuration. Which TWO practices genuinely reduce the risk of "
            "a container-to-host breakout? (Select TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Run application containers as an unprivileged, non-root "
                    "user inside the container"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Running as a non-root user limits what an "
                    "attacker who gains code execution inside the container "
                    "can do, reducing the impact of a potential breakout."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Use minimal, purpose-built base images (such as "
                    "distroless images) that exclude shells and package "
                    "managers not needed at runtime"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Minimal images remove the tools an attacker "
                    "would otherwise use to pivot, escalate, or persist after "
                    "gaining initial access, shrinking the container's "
                    "attack surface."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Launch all containers with the --privileged flag so they "
                    "can access host devices if ever needed later"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Privileged mode grants near-complete access "
                    "to host devices and kernel capabilities, dramatically "
                    "increasing — not reducing — the risk of a breakout."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Mount the host's container engine socket into every "
                    "application container so they can manage sibling "
                    "containers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Exposing the container engine's control "
                    "socket inside a container is a well-known escape vector "
                    "that effectively grants root-equivalent control of the "
                    "host."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Share a single root-level service account across all "
                    "containers to simplify credential management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A shared root-level credential violates least "
                    "privilege and means a single compromised container "
                    "exposes credentials usable against every other "
                    "container."
                ),
            },
        ],
        "explanation": (
            "Reducing container breakout risk relies on least-privilege "
            "runtime settings — non-root execution and minimal images that "
            "remove unneeded tools — while privileged flags, exposed engine "
            "sockets, and shared root credentials all actively increase "
            "breakout and blast-radius risk."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A developer hardcodes a third-party payment API key directly "
            "into a serverless function's source code, which is then "
            "committed to a company Git repository that includes several "
            "external contributor collaborators. Which change BEST "
            "remediates this exposure while preserving the function's "
            "ability to authenticate at runtime?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove the hardcoded key from the code and repository "
                    "history, and retrieve it at runtime from a managed "
                    "secrets manager/vault"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Purging the key from the repository (including "
                    "history) and retrieving it at runtime from a secrets "
                    "manager keeps the credential out of source control while "
                    "still letting the function authenticate when it runs."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Base64-encode the API key before committing it to the "
                    "repository"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Base64 encoding is not encryption and is "
                    "trivially reversible by anyone who finds the encoded "
                    "value; it provides no real protection."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rename the repository file containing the key so it is "
                    "harder for contributors to locate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is security through obscurity — the key "
                    "remains fully exposed to anyone with repository access "
                    "and in the commit history."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rotate the key on the same schedule as all other "
                    "unrelated credentials, without changing where it is "
                    "stored"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rotating on a fixed schedule without removing "
                    "the key from the shared repository does not fix the "
                    "underlying exposure — a new key would simply be exposed "
                    "again at the next commit."
                ),
            },
        ],
        "explanation": (
            "Secrets should never be committed to source control, even in "
            "serverless environments; the correct remediation is to remove "
            "the credential from the repository and its history entirely and "
            "have the function retrieve it at runtime from a managed secrets "
            "manager."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "A security architect is selecting a hypervisor platform for a "
            "new server virtualization initiative that will host many "
            "security-sensitive, mutually isolated workloads. One option runs "
            "directly on the physical hardware; the other runs as an "
            "application on top of a general-purpose host operating system. "
            "From a security standpoint, which BEST explains why the bare-"
            "metal (Type 1) hypervisor is generally preferred for this use "
            "case?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It removes the host operating system as an additional "
                    "layer that could be independently compromised, reducing "
                    "the overall attack surface between guest VMs and the "
                    "hardware"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A Type 1 hypervisor runs directly on hardware, "
                    "eliminating a general-purpose host OS as a separate, "
                    "independently exploitable layer that a Type 2 "
                    "hypervisor depends on."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It allows guest VMs to directly share the same kernel as "
                    "the host OS for better performance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Sharing a kernel describes containerization, "
                    "not virtualization, and sharing a kernel would actually "
                    "reduce isolation between workloads rather than improve "
                    "security."
                ),
            },
            {
                "id": "c",
                "text": "It eliminates the need to ever patch the hypervisor itself",
                "correct": False,
                "rationale": (
                    "Incorrect. Type 1 hypervisors still ship vulnerabilities "
                    "and require ongoing patching just like any other "
                    "software."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It permits guest operating systems to bypass the "
                    "hypervisor entirely for direct hardware access"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bypassing the hypervisor would defeat the "
                    "purpose of virtualization and isolation between guest "
                    "VMs, not strengthen security."
                ),
            },
        ],
        "explanation": (
            "Type 1 (bare-metal) hypervisors are generally preferred for "
            "security-sensitive multi-tenant workloads because they remove "
            "the extra attack surface of a general-purpose host OS that a "
            "Type 2 (hosted) hypervisor depends on."
        ),
    },
    {
        "id": "nd3g-010",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "An attacker who has already compromised one tenant's virtual "
            "machine on a multi-tenant hosting platform exploits an unpatched "
            "vulnerability in the hypervisor to gain code execution on the "
            "underlying host, from which they can access and manipulate "
            "other tenants' VMs. What is this attack technique called, and "
            "what is the PRIMARY mitigation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "VM escape; promptly and consistently patching the "
                    "hypervisor to close known vulnerabilities"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Breaking out of a guest VM to reach the "
                    "hypervisor/host is called VM escape, and the primary "
                    "mitigation is timely hypervisor patching to close the "
                    "vulnerabilities that make escape possible."
                ),
            },
            {
                "id": "b",
                "text": (
                    "VLAN hopping; disabling dynamic trunking protocol on "
                    "physical switches"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN hopping is a Layer 2 network attack "
                    "against switch trunking behavior, not a hypervisor "
                    "vulnerability exploited from within a guest VM."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Session hijacking; enforcing shorter web session timeout "
                    "values"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Session hijacking targets authenticated web "
                    "sessions; nothing in the scenario involves stealing a "
                    "session token."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Privilege escalation via SQL injection; parameterizing "
                    "all database queries"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. No database or SQL injection is described; "
                    "the attacker pivoted from a guest VM to the hypervisor, "
                    "not through an application query."
                ),
            },
        ],
        "explanation": (
            "VM escape is the attack of breaking out of a guest VM's "
            "isolation to reach the hypervisor or host, typically by "
            "exploiting an unpatched hypervisor vulnerability; keeping the "
            "hypervisor consistently patched is the primary mitigation."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A vulnerability assessment finds that every Windows server in an "
            "environment still has SMBv1 and the Print Spooler service "
            "enabled by default, even though no legitimate business "
            "application requires either. Both have well-known, actively "
            "exploited remote code execution vulnerabilities. What is the "
            "MOST effective attack-surface-reduction action?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Disable SMBv1 and the Print Spooler service on all "
                    "servers that do not explicitly require them for a "
                    "documented business function"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing unneeded, historically exploited "
                    "services entirely is the definition of attack surface "
                    "reduction — there is nothing left for an attacker to "
                    "exploit if the service is not running at all."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Leave both services enabled but increase the frequency "
                    "of vulnerability scans to detect exploitation attempts "
                    "sooner"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent scanning improves detection "
                    "after the fact but does not remove the exposed service, "
                    "so the attack surface itself is unchanged."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy a signature-based antivirus update on each server "
                    "without changing the services that are running"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus signatures address known malware "
                    "payloads, not the exposed, unnecessary services "
                    "themselves that provide the initial entry point."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Restrict SMBv1 and Print Spooler access to the local "
                    "administrator account only, while keeping both services "
                    "running for all other accounts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Both services remain remotely reachable and "
                    "exploitable regardless of which account restrictions are "
                    "applied; the vulnerable service itself is still exposed."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means removing unneeded services and "
            "software entirely rather than layering detection or account "
            "restrictions on top of a still-exposed, historically exploited "
            "service."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management workflow",
        "stem": (
            "A database schema change was approved by the change advisory "
            "board and implemented during the scheduled maintenance window. "
            "When the change caused unexpected application errors, the team "
            "spent six additional hours improvising a manual recovery because "
            "the original change request did not specify how to reverse the "
            "change. Which element of the change management process was "
            "missing, and would have MOST reduced the outage duration?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A documented backout/rollback plan specifying the exact "
                    "steps to revert the change if it fails"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A pre-approved backout plan lets the team "
                    "revert immediately when a change fails, instead of "
                    "improvising recovery steps under pressure — exactly the "
                    "missing piece described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A second approval signature from a more senior manager "
                    "on the change advisory board"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An additional approval signature affects "
                    "whether the change was authorized, not how quickly it "
                    "can be reversed once it fails."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A longer scheduled maintenance window to allow more time "
                    "for the original change"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More time for the forward change does not "
                    "provide a defined recovery path once the change has "
                    "already failed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A stricter change-freeze policy prohibiting any changes "
                    "during month-end"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A change freeze restricts when changes may "
                    "occur; it has no bearing on how this specific approved "
                    "change could have been reversed once implemented."
                ),
            },
        ],
        "explanation": (
            "Every change request should include a documented backout/"
            "rollback plan so that, if the change fails, the team can revert "
            "quickly using pre-approved steps rather than improvising "
            "recovery during an active outage."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Failure modes",
        "stem": (
            "A company's outbound email data loss prevention (DLP) gateway "
            "inspects every message for sensitive data patterns before it "
            "leaves the network. When the DLP inspection engine becomes "
            "unreachable due to a software fault, the gateway is currently "
            "configured to allow all outbound email to pass without "
            "inspection so that business communication is not delayed. A "
            "security review recommends changing this behavior so that "
            "outbound mail is held or blocked entirely whenever the "
            "inspection engine is unavailable, even though this may delay "
            "some legitimate email. Which change is being recommended?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Changing the DLP gateway's failure mode from fail-open "
                    "to fail-closed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Currently the gateway fails open (passes "
                    "traffic uninspected on failure); the recommendation to "
                    "hold or block mail instead when inspection is "
                    "unavailable is the definition of switching to "
                    "fail-closed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Changing the DLP gateway's failure mode from fail-closed "
                    "to fail-open"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the actual direction of the "
                    "change described — the gateway is currently fail-open "
                    "and is being changed to fail-closed, not the other way "
                    "around."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replacing the DLP gateway with an intrusion prevention "
                    "system operating in fail-open mode"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This introduces an unrelated device and the "
                    "wrong failure behavior; the scenario describes changing "
                    "how the existing DLP gateway behaves on failure, not "
                    "replacing it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configuring the DLP gateway for active-active high "
                    "availability with two inspection engines"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding redundant inspection engines reduces "
                    "the likelihood of a failure occurring, but the scenario "
                    "specifically describes changing what the gateway does "
                    "when a failure does occur, which is a failure-mode "
                    "change, not a redundancy change."
                ),
            },
        ],
        "explanation": (
            "Fail-open lets traffic pass uninspected during a failure, "
            "prioritizing availability; fail-closed blocks traffic during a "
            "failure, prioritizing confidentiality/data-loss prevention over "
            "availability — the correct choice depends on which risk the "
            "organization is less willing to accept."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A retailer is deploying a new web application firewall (WAF) in "
            "front of its checkout page for the first time. To avoid "
            "inadvertently blocking legitimate customer transactions due to "
            "untuned rules, the security team initially configures the WAF to "
            "log and alert on traffic that matches attack signatures without "
            "blocking any requests. Which BEST describes this deployment "
            "approach and its purpose?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Detection/monitoring mode, used to tune rules and reduce "
                    "false positives before enabling blocking (prevention) "
                    "mode in production"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Running a new WAF in log-only/detection mode "
                    "first lets the team observe and tune rules against real "
                    "traffic before switching to active blocking, minimizing "
                    "the risk of blocking legitimate checkout transactions."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fail-open mode, used to guarantee the WAF never impacts "
                    "application availability under any circumstance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open describes what happens when the "
                    "device itself fails or becomes unreachable, not an "
                    "intentional detection-only deployment stage while the "
                    "device is functioning normally."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Passive reconnaissance mode, used to fingerprint the "
                    "checkout application's technology stack"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Passive reconnaissance describes an "
                    "attacker's information-gathering technique, not a WAF "
                    "deployment mode."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Bridge mode, used to make the WAF invisible at Layer 2 "
                    "so it cannot be detected by attackers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bridge/transparent mode describes a network "
                    "deployment topology, not whether the device is "
                    "detecting-only or actively blocking traffic."
                ),
            },
        ],
        "explanation": (
            "New WAF and IPS deployments are commonly rolled out in a log-"
            "only detection mode first so rules can be tuned against real "
            "production traffic, minimizing false positives before switching "
            "to active blocking."
        ),
    },
    {
        "id": "nd3g-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A company wants a firewall capable of distinguishing between "
            "different applications that share the same destination port 443 "
            "(for example, allowing a specific SaaS collaboration tool's chat "
            "feature while blocking its file-upload feature) and applying "
            "different policies to each. A traditional stateful packet-"
            "filtering firewall, which only evaluates source/destination IP, "
            "port, and connection state, cannot make this distinction. Which "
            "capability must the replacement firewall provide?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Layer 7 application-aware inspection, as found in a "
                    "next-generation firewall (NGFW)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Distinguishing specific applications and "
                    "features sharing the same port requires Layer 7 "
                    "application-layer visibility, which is the defining "
                    "capability of an NGFW."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Larger stateful connection tables to track more "
                    "simultaneous sessions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A bigger connection table increases scale, "
                    "not application-layer visibility; it still cannot "
                    "distinguish one application's features from another's on "
                    "the same port."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Network address translation (NAT) to hide internal IP "
                    "addresses on port 443 traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NAT addresses IP exposure, not application "
                    "differentiation, and does not help the firewall tell "
                    "different port-443 applications apart."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Support for a greater number of static port-forwarding "
                    "rules"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More port-forwarding rules still only "
                    "operate on IP and port, providing no application-layer "
                    "awareness."
                ),
            },
        ],
        "explanation": (
            "Only Layer 7 application-aware inspection, the hallmark "
            "capability of an NGFW, can distinguish between different "
            "applications or application features that share the same "
            "destination port."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "An application team needs incoming web requests routed based on "
            "URL path — requests to /api/* must go to a pool of application "
            "servers, while requests to /images/* must go to a separate pool "
            "of static-content servers — with session persistence maintained "
            "per user. A basic Layer 4 load balancer, which only distributes "
            "connections based on IP address and port, cannot make this "
            "distinction. What capability is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Layer 7 (application-layer) load balancing with "
                    "content-based routing rules"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Only a Layer 7 load balancer can inspect the "
                    "HTTP request itself, including the URL path, to route "
                    "requests to different backend pools accordingly."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Round-robin DNS resolution across all servers in both "
                    "pools"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DNS round-robin has no visibility into HTTP "
                    "request content and simply rotates IP addresses "
                    "returned to clients, unable to distinguish URL paths."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Network address translation performed at the perimeter "
                    "firewall"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates addresses; it does not inspect "
                    "or route based on application-layer content such as a "
                    "URL path."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A larger connection table on the existing Layer 4 load "
                    "balancer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Increasing scale on a Layer 4 device does not "
                    "add the application-layer content awareness needed to "
                    "route based on URL path."
                ),
            },
        ],
        "explanation": (
            "Routing decisions based on HTTP content such as URL path "
            "require a Layer 7 (application-layer) load balancer, since a "
            "Layer 4 device only has visibility into IP and port information."
        ),
    },
    {
        "id": "nd3g-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company wants to automatically verify that a laptop has "
            "current antivirus signatures and all critical OS patches "
            "installed BEFORE it is granted access to the internal LAN, and "
            "to redirect any non-compliant device to an isolated remediation "
            "network instead. Which technology BEST provides this "
            "capability?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Network Access Control (NAC) with device posture/health "
                    "assessment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. NAC evaluates a connecting device's compliance "
                    "posture — patch level, antivirus status, and more — "
                    "before admission, and can quarantine non-compliant "
                    "devices to a remediation VLAN."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A stateful perimeter firewall applying source-IP-based "
                    "rules"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A perimeter firewall filters traffic by "
                    "address and port; it does not assess an endpoint's "
                    "patch level or antivirus status before granting LAN "
                    "access."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A reverse proxy performing TLS termination for internal "
                    "web applications"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A reverse proxy handles web traffic "
                    "termination and forwarding; it plays no role in "
                    "assessing device health before network admission."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A security information and event management (SIEM) "
                    "platform correlating log alerts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A SIEM detects and correlates events after "
                    "they occur; it does not gate whether a device is "
                    "admitted to the network in the first place."
                ),
            },
        ],
        "explanation": (
            "Network Access Control (NAC) is purpose-built to assess a "
            "connecting device's security posture — patch level, antivirus "
            "status, and configuration — before granting or restricting "
            "network access."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "A company currently authenticates 802.1X wired and wireless "
            "clients using PEAP-MSCHAPv2, which tunnels a username/password "
            "exchange inside a server-authenticated TLS tunnel. A security "
            "assessment notes that if an attacker can trick a client into "
            "connecting to a rogue access point and get the client to "
            "complete the inner authentication, the captured MSCHAPv2 "
            "exchange may be vulnerable to offline cracking. Which EAP method "
            "would BEST eliminate this specific risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "EAP-TLS, which requires mutual certificate-based "
                    "authentication for both client and server and never "
                    "transmits a crackable password exchange"
                ),
                "correct": True,
                "rationale": (
                    "Correct. EAP-TLS requires the client to also present a "
                    "certificate, so there is no password exchange to steal "
                    "or crack, and a rogue AP cannot successfully impersonate "
                    "the legitimate server without the private key."
                ),
            },
            {
                "id": "b",
                "text": (
                    "EAP-MD5, which uses a simpler challenge-response hash "
                    "for authentication"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. EAP-MD5 is a weaker, one-way authentication "
                    "method with no mutual authentication or protection "
                    "against offline attacks — it does not solve the "
                    "described risk."
                ),
            },
            {
                "id": "c",
                "text": "LEAP, Cisco's legacy lightweight EAP protocol",
                "correct": False,
                "rationale": (
                    "Incorrect. LEAP is well known to be vulnerable to "
                    "offline dictionary attacks, arguably making the risk "
                    "worse rather than better."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Open authentication with a shared network passphrase for "
                    "all users"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This removes per-user authentication and "
                    "802.1X entirely, providing far weaker security than the "
                    "PEAP configuration already in place."
                ),
            },
        ],
        "explanation": (
            "EAP-TLS eliminates password-based authentication exchanges "
            "entirely by requiring mutual certificate-based authentication, "
            "removing the credential-capture risk inherent to password-based "
            "EAP methods like PEAP-MSCHAPv2 when a client connects to a rogue "
            "access point."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "All of a company's application servers sit on a single flat "
            "VLAN for operational simplicity. To stop an attacker who "
            "compromises one server from pivoting laterally to any other "
            "server on that same VLAN, the security team implements "
            "software-defined policies that enforce a per-workload allow-list "
            "of exactly which other individual hosts and ports each server "
            "may communicate with, independent of the underlying physical or "
            "VLAN topology. What is this approach called?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Microsegmentation",
                "correct": True,
                "rationale": (
                    "Correct. Microsegmentation enforces granular, software-"
                    "defined, per-workload communication policies that "
                    "restrict lateral movement even between hosts on the "
                    "same VLAN or physical segment."
                ),
            },
            {
                "id": "b",
                "text": "VLAN hopping prevention",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN hopping prevention addresses an attack "
                    "that abuses trunk negotiation to cross VLAN boundaries; "
                    "it does not describe enforcing per-workload policy "
                    "within a single VLAN."
                ),
            },
            {
                "id": "c",
                "text": "Network address translation",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates addresses between networks; "
                    "it does not enforce host-to-host communication policy "
                    "within a flat segment."
                ),
            },
            {
                "id": "d",
                "text": "Spanning Tree Protocol (STP) hardening",
                "correct": False,
                "rationale": (
                    "Incorrect. STP hardening prevents Layer 2 switching "
                    "loops and related attacks; it has no role in enforcing "
                    "per-workload lateral-movement policy."
                ),
            },
        ],
        "explanation": (
            "Microsegmentation applies fine-grained, software-defined "
            "security policies at the individual workload level, restricting "
            "lateral movement even among hosts that share the same VLAN or "
            "physical network segment."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A site-to-site VPN between two branch offices currently "
            "authenticates using a single pre-shared key (PSK) that is "
            "manually configured on both VPN gateways and has been unchanged "
            "since installation. A security review notes that if this PSK is "
            "ever disclosed, an attacker could impersonate either gateway. "
            "Which change would MOST improve the strength of the VPN's "
            "authentication?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace the shared PSK with certificate-based "
                    "authentication (e.g., IKEv2 with X.509 certificates) "
                    "issued individually to each gateway"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Certificate-based authentication gives each "
                    "gateway its own private key rather than a single shared "
                    "secret, so compromise of one gateway's certificate does "
                    "not automatically let an attacker impersonate the other."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the length of the existing pre-shared key from "
                    "16 to 24 characters"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A longer PSK is still a single secret shared "
                    "by both gateways — if it is ever disclosed, the same "
                    "impersonation risk remains regardless of its length."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Switch the VPN from IPSec to a GRE tunnel for simpler "
                    "configuration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GRE alone provides no encryption or "
                    "authentication and would weaken, not strengthen, the "
                    "VPN's security."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rotate the same pre-shared key every 90 days going "
                    "forward"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Periodic rotation shrinks the exposure window "
                    "somewhat but does not eliminate the fundamental risk of "
                    "a single secret shared by both parties."
                ),
            },
        ],
        "explanation": (
            "Certificate-based authentication replaces a single shared "
            "secret with individually issued key pairs per gateway, so the "
            "compromise of one gateway's credentials does not automatically "
            "compromise the other's identity — a meaningful strength "
            "improvement over PSK authentication."
        ),
    },
    {
        "id": "nd3g-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A company requires that if a remote employee's VPN client "
            "connection drops unexpectedly while the employee is working from "
            "a coffee shop's public Wi-Fi, the laptop must immediately stop "
            "sending or receiving any network traffic outside the encrypted "
            "tunnel until the VPN reconnects, rather than silently falling "
            "back to the unencrypted local network. Which VPN client feature "
            "enforces this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A kill switch",
                "correct": True,
                "rationale": (
                    "Correct. A VPN kill switch blocks all network traffic "
                    "outside the tunnel the moment the VPN connection drops, "
                    "preventing any silent fallback to an unencrypted "
                    "network."
                ),
            },
            {
                "id": "b",
                "text": "Split tunneling",
                "correct": False,
                "rationale": (
                    "Incorrect. Split tunneling intentionally routes only "
                    "some traffic through the VPN and lets other traffic "
                    "travel outside it — the opposite of blocking all "
                    "non-tunneled traffic."
                ),
            },
            {
                "id": "c",
                "text": "Perfect forward secrecy",
                "correct": False,
                "rationale": (
                    "Incorrect. Perfect forward secrecy protects past "
                    "session keys from being derived if a long-term key is "
                    "later compromised; it has nothing to do with behavior "
                    "when the connection drops."
                ),
            },
            {
                "id": "d",
                "text": "Always-on DNS-over-HTTPS",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS-over-HTTPS protects the privacy of DNS "
                    "queries specifically; it does not block all other "
                    "outside-tunnel traffic when the VPN connection drops."
                ),
            },
        ],
        "explanation": (
            "A VPN kill switch is the client feature that blocks all "
            "network traffic the instant the VPN tunnel drops, preventing "
            "sensitive traffic from silently falling back to an untrusted "
            "local network such as public Wi-Fi."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A company is redesigning remote access under Zero Trust "
            "principles. Which TWO of the following design choices are "
            "consistent with a genuine Zero Trust implementation? (Select "
            "TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A policy enforcement point brokers and authorizes every "
                    "individual application access request, rather than "
                    "granting broad network access after a single login"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Per-request, per-application authorization "
                    "through a policy enforcement point is a core Zero Trust "
                    "mechanism, replacing broad network-level trust after a "
                    "single login."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Device posture and user risk signals are continuously "
                    "reassessed throughout a session, and access can be "
                    "revoked mid-session if signals change"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuous verification throughout a session, "
                    "not just at initial login, is a foundational Zero Trust "
                    "principle — trust is never permanent."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Once a user authenticates successfully with MFA, they "
                    "retain standing access to the entire internal network "
                    "for the rest of the day"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Granting standing, broad access after one "
                    "authentication event describes implicit trust and "
                    "castle-and-moat design, the opposite of Zero Trust."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Users connecting from inside the corporate office "
                    "building are automatically granted greater trust than "
                    "remote users, since the office network is considered "
                    "secure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Zero Trust explicitly rejects granting trust "
                    "based on network location; every request must be "
                    "verified regardless of where it originates."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Access decisions rely solely on VLAN-based network "
                    "segmentation, without evaluating identity or device "
                    "signals per request"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Network segmentation alone, without identity "
                    "and context evaluation for each request, does not meet "
                    "the Zero Trust standard of continuous, identity-centric "
                    "verification."
                ),
            },
        ],
        "explanation": (
            "Zero Trust requires per-request authorization through a policy "
            "enforcement point and continuous reassessment of trust "
            "throughout a session — it explicitly rejects standing access, "
            "location-based trust, and segmentation-only controls that skip "
            "identity and context evaluation."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-023",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Data classification",
        "stem": (
            "An insurance company's data classification policy defines "
            "Public, Internal, Confidential, and Restricted labels. Its "
            "proprietary actuarial pricing model — a set of formulas that "
            "gives it a significant competitive advantage — contains no "
            "personally identifiable information and is not subject to any "
            "specific data-privacy regulation. A junior analyst argues it "
            "should be labeled Internal because 'it isn't regulated data.' "
            "Which classification is MOST appropriate, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restricted (or Confidential, per the policy's naming), "
                    "because classification should be driven by the business "
                    "impact of unauthorized disclosure, not solely by whether "
                    "a regulation specifically covers the data"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Data classification is driven by the potential "
                    "harm from disclosure — here, severe competitive damage "
                    "— not only by whether a named regulation applies to "
                    "that specific data type."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Internal, because only data subject to a specific named "
                    "regulation (such as PCI DSS or HIPAA) can be classified "
                    "above the Internal level"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Regulatory coverage is one factor among "
                    "several in classification decisions, not the sole "
                    "requirement for an elevated classification level."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Public, because the model is not personally identifiable "
                    "and therefore carries no confidentiality requirement"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Confidentiality requirements are driven by "
                    "business and competitive harm from disclosure, not only "
                    "by whether the data is personally identifiable."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The classification cannot be determined without first "
                    "consulting external regulators"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Internal business-impact assessment, not "
                    "regulator consultation, is what determines "
                    "classification for proprietary trade-secret data that "
                    "carries no specific regulatory obligation."
                ),
            },
        ],
        "explanation": (
            "Classification decisions must consider the business impact of "
            "unauthorized disclosure — including competitive and financial "
            "harm — not just whether a specific regulation names the data "
            "type; unregulated trade secrets can still warrant an "
            "organization's highest confidentiality label."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-024",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A regulated financial firm moving data to a public cloud "
            "provider is contractually required to ensure that the cloud "
            "provider itself can never decrypt the firm's data, even though "
            "the provider's infrastructure performs the encryption "
            "operations. The firm must retain exclusive, revocable control "
            "over the encryption keys. Which approach BEST satisfies this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Bring Your Own Key (BYOK) / customer-managed keys held "
                    "in an external key management system the firm controls, "
                    "rather than provider-managed keys"
                ),
                "correct": True,
                "rationale": (
                    "Correct. BYOK/customer-managed keys let the firm retain "
                    "exclusive control and revocation authority over the "
                    "keys, so the provider cannot decrypt the data without "
                    "the firm's key being made available."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Provider-managed encryption keys stored and rotated "
                    "automatically within the cloud platform's default key "
                    "management service"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. With provider-managed keys, the provider "
                    "retains access to the keys, directly contradicting the "
                    "requirement that the provider never be able to decrypt "
                    "the data."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Client-side hashing of the data using SHA-256 instead of "
                    "encryption"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is one-way and irreversible; it would "
                    "make the data unusable for legitimate purposes and does "
                    "not equate to encryption key control."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enabling the cloud provider's default in-transit TLS "
                    "encryption for all API calls to the storage service"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data only while it is moving "
                    "across the network; it does not address who controls "
                    "the keys used to encrypt the data at rest."
                ),
            },
        ],
        "explanation": (
            "BYOK / customer-managed key arrangements let an organization "
            "retain exclusive, revocable control over its encryption keys "
            "even when the underlying encryption operations are performed by "
            "a cloud provider, ensuring the provider itself cannot decrypt "
            "the data without the customer's key."
        ),
    },
    {
        "id": "nd3g-025",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A hospital must send a file containing patient records to an "
            "external auditor. The security team wants to (1) keep the "
            "contents confidential in case the file is intercepted or "
            "misdirected, and (2) allow the auditor to verify the file was "
            "not altered in transit. Which TWO actions together satisfy both "
            "goals? (Select TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Encrypt the file with a strong algorithm before sending "
                    "it, independent of any transport-layer encryption "
                    "already used by the delivery channel"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Encrypting the file itself protects its "
                    "contents even if it is intercepted, misdirected, or "
                    "lands on an intermediate server outside the original "
                    "transport channel."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Generate a cryptographic hash (or digital signature) of "
                    "the file and provide it to the auditor through a "
                    "separate channel to verify integrity upon receipt"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A hash or signature delivered out-of-band lets "
                    "the auditor confirm the received file matches the "
                    "original and was not altered in transit."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rely solely on the email provider's TLS connection to "
                    "protect the message in transit"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects only the transport hop and "
                    "provides no protection once the file lands on an "
                    "intermediate server, and it provides no way to verify "
                    "the file's integrity afterward."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rename the file with a non-descriptive filename before "
                    "sending it"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Renaming a file is security through "
                    "obscurity and provides no real confidentiality or "
                    "integrity assurance."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Compress the file into a password-less ZIP archive to "
                    "reduce its size"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Compression without a strong password or "
                    "encryption provides no confidentiality and no integrity "
                    "verification."
                ),
            },
        ],
        "explanation": (
            "Confidentiality and integrity for a sensitive file transfer "
            "require two distinct controls: encrypting the file itself "
            "(independent of the transport channel) and providing a hash or "
            "signature through a separate channel so the recipient can "
            "verify the file was not altered."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-026",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data states",
        "stem": (
            "A company's checkout microservice calls an internal payment-"
            "authorization microservice over plain HTTP, sending the "
            "customer's full card number in the request body. Developers "
            "justify this by noting that both services run on the internal "
            "data center network, which they consider trusted. A penetration "
            "tester captures this traffic using a compromised host elsewhere "
            "on the same internal network. Which data-protection principle "
            "was violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data in transit must be encrypted (e.g., via mTLS) "
                    "regardless of whether the network is internal, since "
                    "internal hosts cannot be implicitly trusted"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The card number was exposed while actively "
                    "moving across the network between services — data in "
                    "transit — and internal network location does not "
                    "justify skipping encryption, as the compromised host "
                    "demonstrates."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Data at rest must be encrypted using full-disk "
                    "encryption on both microservice hosts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The exposure occurred on the network during "
                    "transmission between services, not from data stored on "
                    "disk."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data in use must be protected using a hardware security "
                    "module during processing"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The card number was captured on the network "
                    "wire between two services, not while being processed in "
                    "memory on a single host."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Data must be tokenized before it is ever generated by "
                    "the checkout service"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization is one possible mitigation, but "
                    "the core principle violated in this scenario is the "
                    "failure to encrypt data actively moving across the "
                    "network — a data-in-transit failure."
                ),
            },
        ],
        "explanation": (
            "Data in transit must be encrypted regardless of whether the "
            "network segment is considered 'internal' or 'trusted' — a "
            "principle central to both defense-in-depth and Zero Trust, "
            "since any host on that network could be compromised and used to "
            "capture unencrypted traffic."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-027",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Tokenization and masking",
        "stem": (
            "An insurance company's live production claims database stores "
            "full Social Security numbers. Adjusters need to see full values, "
            "but call-center representatives querying that SAME live "
            "database in real time must see only masked values, based on "
            "their role — without the company creating and maintaining a "
            "separate, duplicated database. Which technique BEST meets this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Dynamic data masking applied at query time based on the "
                    "requesting user's role"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Dynamic data masking evaluates the requesting "
                    "user's role at query time against the live production "
                    "database, returning masked or unmasked values without "
                    "requiring a separate copy of the data."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Static data masking applied to a nightly export used to "
                    "refresh a test/development environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking creates a separate, sanitized "
                    "copy of the data for non-production use; it does not "
                    "provide real-time, role-based masking of the live "
                    "production database itself."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Full-disk encryption of the production database volume"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Full-disk encryption protects data at rest "
                    "from disk theft; it does not selectively mask values "
                    "shown to different roles during live queries."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Irreversible one-way hashing of the SSN column for all "
                    "users"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing every value irreversibly would also "
                    "prevent adjusters from ever seeing the full SSN they "
                    "legitimately need for their role."
                ),
            },
        ],
        "explanation": (
            "Dynamic data masking is applied at query time against the live "
            "production database itself, showing full or masked values based "
            "on the requesting user's role, unlike static masking which "
            "creates a separate sanitized copy for non-production purposes."
        ),
    },
    {
        "id": "nd3g-028",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A law firm must submit a document containing clients' Social "
            "Security numbers as a public court exhibit. The numbers must be "
            "permanently and irreversibly removed from the version filed "
            "publicly — not simply hidden from view or partially displayed "
            "— so that no process can recover them from the filed document. "
            "Which technique is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Redaction",
                "correct": True,
                "rationale": (
                    "Correct. Redaction permanently removes the sensitive "
                    "content from the document itself, satisfying the "
                    "requirement that no process can recover the values from "
                    "the filed exhibit."
                ),
            },
            {
                "id": "b",
                "text": "Masking",
                "correct": False,
                "rationale": (
                    "Incorrect. Masking typically displays a partial value, "
                    "such as the last four digits, and may remain reversible "
                    "for authorized users elsewhere — it does not guarantee "
                    "permanent removal from the filed document."
                ),
            },
            {
                "id": "c",
                "text": "Tokenization",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization replaces the value with a token "
                    "but preserves a reversible mapping stored elsewhere, "
                    "which does not satisfy a requirement for irreversible "
                    "public disclosure."
                ),
            },
            {
                "id": "d",
                "text": "Data minimization",
                "correct": False,
                "rationale": (
                    "Incorrect. Data minimization limits what data is "
                    "collected or retained in the first place; it does not "
                    "describe permanently removing a value already present "
                    "in an existing document."
                ),
            },
        ],
        "explanation": (
            "Redaction is the technique for permanently and irreversibly "
            "removing sensitive content from a specific document, unlike "
            "masking or tokenization, both of which typically preserve the "
            "original value or a reversible mapping to it elsewhere."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-029",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A video production studio performs a full backup every Sunday "
            "night. For the remaining six nights of the week, administrators "
            "are choosing between differential backups (each capturing all "
            "changes since the last full backup) and incremental backups "
            "(each capturing only changes since the previous backup of any "
            "type). The studio's top priority is minimizing the number of "
            "backup sets that must be restored after a Friday failure, even "
            "if that means more storage is consumed over the week. Which "
            "backup strategy should it choose, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Differential backups, because restoring requires only "
                    "the last full backup plus the single most recent "
                    "differential — fewer sets than an incremental chain"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A differential restore needs only the full "
                    "backup and the latest differential, while an "
                    "incremental restore requires the full backup plus every "
                    "incremental since — more sets to apply, which directly "
                    "conflicts with the studio's stated priority."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Incremental backups, because each incremental backup is "
                    "smaller and therefore faster to restore than a "
                    "differential backup"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Individual incremental backups are smaller, "
                    "but a Friday restore requires the full backup plus every "
                    "incremental in the chain since Sunday — more sets "
                    "overall than the differential approach."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Incremental backups, because they eliminate the need for "
                    "a weekly full backup entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Both differential and incremental strategies "
                    "still require a periodic full backup as their baseline; "
                    "neither eliminates it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Differential backups, because they consume less storage "
                    "over the week than incremental backups"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Differential backups grow larger each day as "
                    "they re-capture all changes since the full backup, "
                    "consuming more cumulative storage over the week than "
                    "incrementals, not less."
                ),
            },
        ],
        "explanation": (
            "Differential backups trade higher storage consumption over the "
            "week for a faster, simpler restore requiring only the full "
            "backup plus the latest differential, while incremental backups "
            "save storage but require restoring the full backup plus every "
            "incremental since — the opposite trade-off."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-030",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "A securities exchange's trading platform requires that the "
            "complete loss of an entire data center — not just a single "
            "server or component — result in zero reduction of available "
            "processing capacity at the surviving site. An N+1 redundancy "
            "model, which adds only one extra unit of capacity beyond what is "
            "needed, would not satisfy this requirement if that spare "
            "capacity is concentrated in the same data center that is lost. "
            "Which redundancy model is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "2N redundancy, in which capacity is fully duplicated "
                    "across two independent data centers, each able to "
                    "independently handle 100% of the load"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 2N redundancy fully duplicates capacity across "
                    "two independent sites, so losing either site entirely "
                    "still leaves 100% of required capacity available at the "
                    "surviving site."
                ),
            },
            {
                "id": "b",
                "text": (
                    "N+1 redundancy, provided the single spare unit is a "
                    "faster server than the others"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. However powerful the single spare unit is, it "
                    "still fails to preserve capacity if the entire data "
                    "center containing both the primary units and the spare "
                    "is lost."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Active-passive failover within a single data center "
                    "using a hot standby server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This does not protect against loss of the "
                    "entire site, since both the active and standby servers "
                    "reside in the same facility."
                ),
            },
            {
                "id": "d",
                "text": (
                    "N+1 redundancy, provided the spare unit is tested "
                    "quarterly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Testing frequency does not change the fact "
                    "that a single spare unit within the same site cannot "
                    "survive total loss of that site."
                ),
            },
        ],
        "explanation": (
            "2N redundancy fully duplicates capacity across two independent "
            "sites so that the complete loss of one site still leaves 100% "
            "of required capacity available, unlike N+1, which typically "
            "concentrates its single spare unit within one site and cannot "
            "survive that site's total loss."
        ),
    },
    {
        "id": "nd3g-031",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "A company operates a two-node failover cluster split across two "
            "data centers. When the network link between the two data "
            "centers fails, both nodes lose contact with each other but each "
            "can still independently reach a small third-site server "
            "dedicated to arbitration. Administrators configure this third-"
            "site server so that whichever node can still communicate with "
            "it is allowed to become active, while the other is fenced off. "
            "What is this third-site server called, and what problem does it "
            "solve?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A witness (quorum) node; it prevents split-brain by "
                    "giving the cluster a tie-breaking vote when the two main "
                    "nodes cannot see each other"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A witness/quorum node breaks the tie during a "
                    "network partition so only one node becomes active, "
                    "preventing the split-brain condition where both nodes "
                    "believe they are primary."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A jump server; it provides administrators a hardened "
                    "point of access to manage both cluster nodes remotely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A jump server controls administrative access "
                    "paths; it plays no role in cluster failover arbitration "
                    "during a network partition."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A honeypot; it lures an attacker away from the "
                    "production cluster nodes during a network partition"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A honeypot is a deception tool for attacker "
                    "detection, unrelated to breaking a cluster's tie during "
                    "a partition."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A load balancer; it distributes client traffic evenly "
                    "between the two data centers during normal operation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes traffic during "
                    "normal operation, but the server described exists "
                    "solely to break a communication tie during a partition, "
                    "not to route client requests."
                ),
            },
        ],
        "explanation": (
            "A witness (quorum) node gives a two-node cluster a tie-breaking "
            "vote during a network partition, preventing the split-brain "
            "condition in which both isolated nodes attempt to act as the "
            "active primary simultaneously."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-032",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multi-cloud and platform diversity",
        "stem": (
            "A company deliberately builds its applications as containerized "
            "workloads orchestrated with Kubernetes and avoids using any "
            "cloud provider's proprietary managed services or vendor-"
            "specific APIs wherever an open-standard alternative exists. "
            "Leadership states this is intentional so that, if needed, "
            "workloads can be migrated to a different cloud provider with "
            "minimal rework. What architectural goal does this design choice "
            "PRIMARILY achieve?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Workload portability, reducing vendor lock-in by "
                    "minimizing dependence on any single provider's "
                    "proprietary services"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Standardizing on open, portable technologies "
                    "and avoiding proprietary vendor APIs is precisely how "
                    "organizations preserve the ability to move workloads "
                    "between providers, minimizing lock-in."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Elimination of all single points of failure, since "
                    "Kubernetes automatically replicates workloads across "
                    "multiple cloud providers simultaneously"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A Kubernetes cluster typically still runs "
                    "within one provider at a time; portability is not the "
                    "same as active, simultaneous multi-provider redundancy."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Regulatory data residency compliance, since "
                    "containerized workloads are automatically exempt from "
                    "cross-border data transfer restrictions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Containerization has no inherent effect on "
                    "where data is physically stored or on data residency "
                    "obligations."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Reduced attack surface, since avoiding proprietary cloud "
                    "services eliminates the need for any identity and access "
                    "management configuration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Identity and access management is still "
                    "required regardless of whether the workload uses "
                    "proprietary or open-standard services."
                ),
            },
        ],
        "explanation": (
            "Deliberately avoiding proprietary vendor APIs in favor of open, "
            "portable standards such as Kubernetes preserves an "
            "organization's ability to migrate workloads between cloud "
            "providers with minimal rework, directly reducing vendor lock-in."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-033",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Power resilience",
        "stem": (
            "A data center currently receives all utility power through a "
            "single feed from one electrical substation. Redundant UPS units "
            "and a backup generator protect against outages once power is "
            "lost, but a security review notes that a failure upstream at the "
            "single substation itself would still interrupt the facility's "
            "normal utility power, forcing an immediate transition to backup "
            "power. Which additional measure would MOST directly address "
            "this specific upstream single point of failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Contracting for a second utility feed from a physically "
                    "separate substation, routed to independent power "
                    "distribution paths within the facility"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A second, physically independent utility feed "
                    "from a different substation directly removes the single "
                    "upstream point of failure that a UPS and generator only "
                    "compensate for after the fact."
                ),
            },
            {
                "id": "b",
                "text": "Increasing the runtime capacity of the existing UPS batteries",
                "correct": False,
                "rationale": (
                    "Incorrect. A larger UPS extends how long the facility "
                    "can run on battery after an outage, but it does not "
                    "address the underlying single-substation dependency "
                    "itself."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Adding a second diesel generator identical to the first "
                    "at the same facility"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Backup generation only activates after "
                    "utility power has already been lost; it does not "
                    "address the single substation feed that caused the "
                    "outage in the first place."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Scheduling more frequent load testing of the existing "
                    "generator"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent testing validates generator "
                    "readiness but does not add a second, independent source "
                    "of primary utility power."
                ),
            },
        ],
        "explanation": (
            "Diverse utility feeds from physically separate substations "
            "address the upstream single point of failure directly, while "
            "UPS and generator capacity only mitigate the consequences after "
            "utility power has already been lost."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-034",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "Two credit unions with similar core-banking infrastructure sign "
            "an agreement to host each other's operations temporarily during "
            "a disaster, at minimal ongoing cost since neither pays to "
            "maintain a dedicated standby facility. A risk assessment raises "
            "a concern specific to this type of arrangement. Which of the "
            "following is the MOST significant inherent drawback of a "
            "reciprocal/mutual aid recovery agreement compared to a "
            "dedicated hot or warm site?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "There is no guarantee the partner will have available "
                    "capacity when needed, particularly since a regional "
                    "disaster (such as a hurricane or widespread power "
                    "outage) may affect both organizations simultaneously"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Reciprocal agreements depend on the partner "
                    "having spare capacity precisely when it is needed, and "
                    "many disasters are regional events that could impair "
                    "both organizations at the same time."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Reciprocal agreements are always more expensive than "
                    "maintaining a dedicated hot site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the actual cost trade-off; "
                    "reciprocal agreements are typically chosen specifically "
                    "because they are far cheaper than maintaining a "
                    "dedicated hot site."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Reciprocal agreements cannot legally be documented in a "
                    "formal, signed agreement between the two organizations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reciprocal arrangements are commonly "
                    "formalized in a written agreement; the real drawback is "
                    "capacity/availability risk, not any legal barrier to "
                    "documentation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Reciprocal agreements guarantee a near-zero recovery "
                    "time objective equivalent to a hot site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reciprocal arrangements generally offer "
                    "weaker, less immediate recovery capability than a "
                    "dedicated hot site, not an equivalent RTO."
                ),
            },
        ],
        "explanation": (
            "The core weakness of reciprocal/mutual aid recovery agreements "
            "is that they provide no binding guarantee of available capacity "
            "when needed, and regional disasters can plausibly impact both "
            "partner organizations at the same time, undermining the "
            "arrangement's reliability."
        ),
    },
    {
        "id": "nd3g-035",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "An insurance company can tolerate up to 48 hours of application "
            "downtime (its recovery time objective) but cannot lose more than "
            "one hour of transaction data (its recovery point objective) in a "
            "disaster. The DR team selects a warm site, believing that "
            "meeting the 48-hour RTO also automatically satisfies the 1-hour "
            "RPO. Why is this assumption INCORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Site type (cold/warm/hot) primarily determines how "
                    "quickly operations can resume, while RPO depends on the "
                    "data replication frequency to that site, which must be "
                    "separately designed to be near-continuous to achieve a "
                    "1-hour target"
                ),
                "correct": True,
                "rationale": (
                    "Correct. RTO and RPO are independent metrics — choosing "
                    "a site type addresses how fast recovery can begin, but "
                    "meeting a specific RPO requires deliberately designing "
                    "the data replication schedule to that site, which is "
                    "not automatic."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A warm site by definition already replicates data "
                    "continuously in real time, so the RPO requirement is "
                    "automatically satisfied once the RTO is met"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A warm site does not guarantee any specific "
                    "replication frequency by definition — this is exactly "
                    "the false assumption the scenario describes as "
                    "incorrect."
                ),
            },
            {
                "id": "c",
                "text": (
                    "RTO and RPO always have identical numeric values by "
                    "industry standard, so a 48-hour RTO implies a 48-hour "
                    "RPO, not a 1-hour RPO"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RTO and RPO measure different things and are "
                    "independently defined based on business requirements; "
                    "there is no standard that ties them to identical "
                    "values."
                ),
            },
            {
                "id": "d",
                "text": (
                    "RPO applies only to cold sites, so it is irrelevant once "
                    "a warm site has been selected"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RPO applies to any recovery strategy "
                    "regardless of site type, since it addresses acceptable "
                    "data loss, not site classification."
                ),
            },
        ],
        "explanation": (
            "RTO and RPO are independent objectives: site type (cold, warm, "
            "hot) primarily governs how quickly the business can resume "
            "operations, while RPO is governed by how frequently data is "
            "replicated to that site — a separate design decision that must "
            "be deliberately engineered to meet a tight RPO target."
        ),
    },
    # ------------------------------------------------------------------ #
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-036",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Resilience testing",
        "stem": (
            "A compliance auditor is evaluating an organization's disaster "
            "recovery testing program, which includes a discussion-based "
            "walkthrough and a live technical failover exercise. Which TWO "
            "statements correctly distinguish these two types of resilience "
            "testing? (Select TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A tabletop/structured walkthrough is discussion-based, "
                    "low-cost, and does not involve actually operating or "
                    "disrupting any production system"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tabletop exercises are purely discussion-based "
                    "and never touch live systems, making them the lowest-"
                    "cost, lowest-risk form of resilience testing."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A full-interruption (live failover) test provides the "
                    "highest level of assurance that the DR site actually "
                    "works, but carries real risk of a production outage if "
                    "the failover itself fails"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A full-interruption test actually cuts over "
                    "production to the DR site, providing the strongest "
                    "validation available, but with genuine risk to "
                    "production availability if something goes wrong."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A tabletop exercise requires physically failing over "
                    "live production traffic to the DR site while "
                    "participants discuss the results afterward"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a full-interruption test, not "
                    "a tabletop exercise, which is purely discussion-based "
                    "and involves no live technical execution at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A parallel test is functionally identical to a full-"
                    "interruption test because both completely cut over 100% "
                    "of production traffic to the DR site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A parallel test processes real transactions "
                    "at the DR site while the primary site continues "
                    "operating normally; only a full-interruption test "
                    "actually cuts over production."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Structured walkthroughs require the DR site to process "
                    "live customer transactions in order to be considered "
                    "valid"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a parallel or full-"
                    "interruption test; a structured walkthrough involves no "
                    "live technical execution at either site."
                ),
            },
        ],
        "explanation": (
            "Resilience testing methods range from purely discussion-based "
            "tabletop exercises, which carry no operational risk, up to "
            "full-interruption tests, which actually cut production over to "
            "the DR site and provide the strongest assurance at the highest "
            "operational risk — parallel tests sit in between by processing "
            "live data at the DR site without cutting over the primary."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3g-037",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "Two government agencies want to document a mutual intent to "
            "informally share cyber threat intelligence indicators with each "
            "other on a best-effort basis. Neither agency wants to create "
            "legally binding service commitments, financial obligations, or a "
            "formal partnership structure — only a written record of shared "
            "goals and general expectations. Which agreement type is MOST "
            "appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memorandum of Understanding (MOU)",
                "correct": True,
                "rationale": (
                    "Correct. An MOU documents mutual intent and general, "
                    "non-binding expectations between parties — exactly what "
                    "the two agencies want without creating enforceable "
                    "service or financial commitments."
                ),
            },
            {
                "id": "b",
                "text": "Service Level Agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines specific, measurable, and "
                    "typically enforceable service performance commitments, "
                    "which the agencies explicitly want to avoid."
                ),
            },
            {
                "id": "c",
                "text": "Business Partnership Agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formally and often legally defines a "
                    "joint business partnership's structure and financial "
                    "responsibilities, a far more formal arrangement than "
                    "what is described."
                ),
            },
            {
                "id": "d",
                "text": "Non-disclosure Agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects confidential information from "
                    "disclosure but does not document mutual intent or "
                    "general collaborative goals between the parties."
                ),
            },
        ],
        "explanation": (
            "A Memorandum of Understanding is the appropriate document for "
            "recording mutual intent and general, non-binding expectations "
            "between organizations, unlike the enforceable commitments of an "
            "SLA or BPA or the narrow confidentiality scope of an NDA."
        ),
    },
]
