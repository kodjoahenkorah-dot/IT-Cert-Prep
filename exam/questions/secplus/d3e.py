"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file E.

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
        "id": "nd3e-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A platform team is redesigning server provisioning. Under the "
            "current model, administrators patch and reconfigure long-lived "
            "servers in place, and configuration drift has caused several "
            "outages when a 'fixed' setting silently reverted. The team is "
            "considering an immutable-infrastructure model instead, where "
            "servers are never modified after deployment and any change is "
            "delivered by building and deploying an entirely new image. Which "
            "statement BEST justifies adopting the immutable model from a "
            "security standpoint?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Immutable infrastructure eliminates configuration drift and "
                    "undocumented changes because every deployed instance "
                    "originates from the same tested, version-controlled image, "
                    "at the cost of requiring a full redeploy for even minor "
                    "changes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because instances are never patched in place, "
                    "every running server is provably identical to a known, "
                    "version-controlled image, closing the drift-based gap that "
                    "caused the outages — the trade-off is that even a small "
                    "change requires building and redeploying a whole new image "
                    "rather than a quick in-place tweak."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Immutable infrastructure allows administrators to apply "
                    "emergency hotfixes directly to running production servers "
                    "faster than the mutable model"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The immutable model specifically forbids "
                    "modifying running servers; a fix must be built into a new "
                    "image and redeployed, which is generally slower than an "
                    "in-place hotfix, not faster."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Immutable infrastructure guarantees that a compromised "
                    "server cannot be replaced by an attacker with a malicious "
                    "image"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Immutability describes how servers are updated, "
                    "not who is authorized to build or deploy images; without a "
                    "secured build pipeline an attacker could still inject a "
                    "malicious image into the deployment process."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Immutable infrastructure removes the need for a "
                    "version-controlled image repository since every server "
                    "state is unique"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Immutable infrastructure depends on a "
                    "version-controlled image repository as its single source "
                    "of truth; it does not make server state unique — quite the "
                    "opposite, every instance from a given image is identical."
                ),
            },
        ],
        "explanation": (
            "Immutable infrastructure trades deployment speed and flexibility "
            "for configuration consistency: because no server is ever modified "
            "after launch, drift and undocumented 'temporary' changes that "
            "erode a known-good baseline are structurally eliminated."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company migrates a fleet of virtual machines to an "
            "infrastructure-as-a-service (IaaS) provider. Six months later, an "
            "audit finds the guest operating systems have never received a "
            "single security patch. The operations team explains they assumed "
            "the cloud provider handled OS patching as part of the service, "
            "the same way it handles the physical hosts and hypervisor. Which "
            "statement BEST describes the flaw in that assumption?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Under the IaaS shared responsibility model, the provider "
                    "secures the physical facility, hardware, and hypervisor, "
                    "but the customer remains responsible for patching the "
                    "guest OS, middleware, and applications running on it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. IaaS shifts responsibility for physical security "
                    "and the virtualization layer to the provider, but "
                    "everything above the hypervisor — guest OS patching, "
                    "runtime, and application-level security — remains the "
                    "customer's obligation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider is responsible for guest OS patching in any "
                    "cloud deployment model, so the operations team's "
                    "assumption was correct and the finding is a false positive"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Provider responsibility for the guest OS "
                    "increases only in higher-abstraction models such as PaaS "
                    "and SaaS; in IaaS the guest OS is squarely the customer's "
                    "responsibility, so the finding is accurate."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Shared responsibility only applies to data encryption, not "
                    "to operating system patching"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The shared responsibility model spans every "
                    "layer of the stack — physical, virtualization, OS, "
                    "middleware, application, and data — not just encryption."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Because the VMs run on the provider's hardware, the "
                    "customer has no ability to patch the guest OS even if it "
                    "wanted to"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In IaaS the customer has full administrative "
                    "access to the guest OS and is both able and obligated to "
                    "patch it; the provider only manages layers below the "
                    "hypervisor."
                ),
            },
        ],
        "explanation": (
            "IaaS moves physical and hypervisor security to the provider but "
            "leaves guest OS, middleware, application, and data security with "
            "the customer — a boundary that shifts further toward the "
            "provider only as the service model moves toward PaaS and SaaS."
        ),
    },
    {
        "id": "nd3e-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A retailer runs its order-processing platform on-premises "
            "year-round because its data governance policy requires customer "
            "order data to remain in company-owned data centers. During the "
            "holiday shopping season, transaction volume spikes to 15 times "
            "normal, far exceeding on-premises capacity. Which cloud "
            "architecture approach BEST lets the retailer handle the seasonal "
            "spike without abandoning its data governance requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cloud bursting, in which stateless front-end processing "
                    "temporarily scales into a public cloud during demand "
                    "spikes while the governed order data stays in the "
                    "on-premises environment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cloud bursting lets the on-premises environment "
                    "remain the primary, governed home for sensitive data "
                    "while elastic, typically stateless capacity in the public "
                    "cloud absorbs short-term demand spikes — satisfying both "
                    "the data residency policy and the scalability need."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fully migrating order processing to a public cloud "
                    "provider so elastic scaling is always available"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A full migration to public cloud would move "
                    "customer order data outside company-owned data centers, "
                    "directly violating the stated governance requirement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploying a community cloud shared with other retailers "
                    "to spread the cost of extra capacity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A community cloud is shared infrastructure "
                    "among organizations with common concerns, not a mechanism "
                    "for elastic overflow, and it still would not keep the "
                    "governed data on company-owned hardware."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Overprovisioning the on-premises data center year-round to "
                    "match peak holiday capacity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This meets the data residency requirement but "
                    "is the most capital-inefficient option, leaving 15x "
                    "capacity idle for most of the year instead of leveraging "
                    "elastic architecture."
                ),
            },
        ],
        "explanation": (
            "Cloud bursting is the hybrid-cloud pattern purpose-built for "
            "exactly this trade-off: keep sensitive, governed data on "
            "dedicated infrastructure while temporarily borrowing public "
            "cloud elasticity for demand spikes."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A natural-gas pipeline operator's SCADA controllers run firmware "
            "that the manufacturer certifies for safety compliance; any "
            "modification, including a security patch, voids the certification "
            "and requires an expensive, months-long recertification process. "
            "The controllers therefore cannot be patched. Which THREE "
            "compensating controls are MOST appropriate to reduce risk to the "
            "unpatched SCADA network? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Isolate the SCADA network from the corporate IT network "
                    "and the internet using dedicated firewalls and strict "
                    "segmentation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Network isolation prevents an attacker who "
                    "compromises the corporate network — or the internet at "
                    "large — from ever reaching the unpatched controllers, "
                    "compensating for the inability to patch them directly."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy a unidirectional security gateway (data diode) so "
                    "telemetry can flow out to monitoring systems but no "
                    "traffic can flow back into the control network"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A data diode enforces one-way communication at "
                    "the hardware level, letting operators monitor the "
                    "unpatched controllers from the IT side without exposing "
                    "an inbound attack path into the control network."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy application allowlisting on any general-purpose "
                    "computers acting as human-machine interfaces (HMIs) so "
                    "only approved control software can execute"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Allowlisting on the HMI workstations prevents "
                    "malware or unauthorized code from executing on the "
                    "systems that interact with the unpatchable controllers, "
                    "reducing the practical attack surface without touching "
                    "the certified firmware."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Expose the controllers' management interfaces directly to "
                    "the internet so the vendor can provide remote patch "
                    "support"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The controllers cannot be patched at all "
                    "without voiding certification, and exposing management "
                    "interfaces to the internet would massively increase risk "
                    "with no compensating benefit."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Disable logging on the control network to reduce "
                    "processing load on the legacy hardware"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling logging removes the visibility "
                    "needed to detect compromise of an unpatchable environment "
                    "and is the opposite of a compensating control."
                ),
            },
        ],
        "explanation": (
            "When a device cannot be patched due to certification or vendor "
            "constraints, security relies on compensating controls — network "
            "isolation, one-way data flow via a data diode, and allowlisting "
            "on adjacent general-purpose systems — rather than remediating "
            "the device itself."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IoT security",
        "stem": (
            "A vending machine operator deploys 2,000 internet-connected "
            "vending machines that use embedded cellular modems to report "
            "inventory and process payments. A security review finds every "
            "machine ships with the same default administrative password and "
            "all machines are addressable from the general corporate network "
            "alongside employee workstations and servers. Which mitigation "
            "BEST reduces risk from this deployment?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Change default credentials on every machine and place all "
                    "vending machines on an isolated network segment that can "
                    "only reach the specific management server they require"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Eliminating default credentials removes the "
                    "easiest compromise path, and segmenting the machines away "
                    "from the corporate network limits what an attacker who "
                    "still compromises a machine can reach — combining "
                    "credential hygiene with containment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Leave the default credentials in place since the machines "
                    "are physically located in public areas and are not "
                    "considered high-value targets"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical location has no bearing on network "
                    "risk; a compromised vending machine on a flat corporate "
                    "network is still a pivot point into servers and "
                    "workstations."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Change default credentials on every machine, but keep "
                    "them on the flat corporate network to simplify "
                    "troubleshooting"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fixing credentials addresses only half the "
                    "problem; leaving the devices on the flat network still "
                    "lets a compromised machine reach sensitive corporate "
                    "systems directly."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disable the cellular modems and require all inventory and "
                    "payment reporting to be entered manually"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the connectivity feature the "
                    "business relies on entirely rather than securing it, and "
                    "is disproportionate compared to fixing credentials and "
                    "segmenting the network."
                ),
            },
        ],
        "explanation": (
            "IoT risk reduction generally requires two complementary steps: "
            "eliminating weak default credentials and containing the devices "
            "on an isolated segment so that a compromise of one low-trust "
            "device cannot reach high-value corporate systems."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A container image build process uses a Dockerfile ENV "
            "instruction to embed a database password so the application can "
            "connect at startup. A security review runs `docker history` on "
            "the published image and recovers the plaintext password from an "
            "intermediate image layer, even though the final running "
            "container's environment variable was later overwritten. Which "
            "remediation BEST addresses the root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove the credential from the image entirely and inject "
                    "it at runtime from an external secrets manager or "
                    "orchestrator-managed secret store"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because every layer of a container image is "
                    "immutable and inspectable, any secret ever written into a "
                    "layer — even one later overwritten — remains recoverable; "
                    "the only fix is to never bake the secret into the image "
                    "and instead inject it at runtime from a dedicated secrets "
                    "manager."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Overwrite the environment variable with a placeholder "
                    "value in a later Dockerfile instruction before publishing "
                    "the image"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly what the affected image "
                    "already did, and `docker history` still recovered the "
                    "original secret from the earlier layer — overwriting a "
                    "value in a later layer does not remove it from the "
                    "layers beneath."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Compress the final image to reduce its size before "
                    "publishing it to the registry"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Compression changes the image's storage "
                    "footprint, not its layer history; the plaintext secret "
                    "remains recoverable from the layer metadata regardless of "
                    "compression."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Restrict `docker history` so only administrators can run "
                    "it against published images"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting who can inspect the image does not "
                    "remove the secret from the layer, and anyone with pull "
                    "access to the registry can still extract the layers and "
                    "recover the credential directly."
                ),
            },
        ],
        "explanation": (
            "Container image layers are immutable and remain part of the "
            "published artifact forever; secrets must never be written into "
            "any layer during the build and should instead be injected at "
            "container runtime from an external secrets manager."
        ),
    },
    {
        "id": "nd3e-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A company's CI/CD pipeline builds container images and pushes "
            "them directly to the production registry with no intermediate "
            "checks. A post-deployment audit finds several running images "
            "contain base-layer libraries with critical, publicly disclosed "
            "CVEs that predate the images' build dates by over a year. Which "
            "change to the pipeline BEST prevents this from recurring?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Add an automated image vulnerability scanning stage that "
                    "runs after build and blocks the push to the production "
                    "registry if critical CVEs are found"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A scanning gate integrated into the pipeline "
                    "catches known-vulnerable base images and dependencies "
                    "before they ever reach the production registry, shifting "
                    "detection left instead of relying on a manual audit after "
                    "the fact."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Schedule a quarterly manual review of all images already "
                    "running in production"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A quarterly manual review is reactive and slow "
                    "compared to an automated pre-deployment gate, and it "
                    "would still allow vulnerable images to run in production "
                    "for months at a time."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Configure the container runtime to automatically restart "
                    "any container that crashes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automatic restart addresses availability after "
                    "a failure, not the presence of known-vulnerable software "
                    "in the image being deployed in the first place."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the size of the CI/CD build server so images "
                    "compile faster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Build performance is unrelated to whether "
                    "known-vulnerable libraries are present in the resulting "
                    "image; this does not address the security gap at all."
                ),
            },
        ],
        "explanation": (
            "Integrating automated vulnerability scanning as a blocking gate "
            "in the CI/CD pipeline is the standard shift-left control for "
            "catching known-vulnerable base images and dependencies before "
            "they reach production."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A development team believes that because a function-as-a-service "
            "platform manages the underlying servers and runtime patching, "
            "their serverless functions are inherently free of unpatched "
            "software risk. An incident later reveals that an attacker "
            "exploited a known, year-old vulnerability in a third-party "
            "logging library bundled inside the function's own deployment "
            "package. Which statement BEST explains the security gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "In the serverless shared responsibility model, the "
                    "provider patches the underlying OS and runtime, but the "
                    "customer remains responsible for the dependencies and "
                    "libraries bundled into their own function code"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Serverless computing shifts infrastructure and "
                    "runtime patching to the provider, but application-level "
                    "code — including any third-party libraries the developer "
                    "bundles into the deployment package — remains squarely "
                    "the customer's responsibility to keep updated."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider is responsible for scanning and patching "
                    "every third-party library bundled inside customer "
                    "function code"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Providers manage the execution environment, "
                    "not the contents of a customer's own deployment package; "
                    "libraries the developer chooses to bundle are outside the "
                    "provider's responsibility."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Serverless functions cannot be exploited through "
                    "vulnerable bundled libraries because each invocation runs "
                    "in a freshly provisioned, ephemeral environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ephemeral execution limits persistence between "
                    "invocations but does nothing to prevent a vulnerable "
                    "library from being exploited during a single invocation, "
                    "as this incident demonstrates."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The finding indicates a misconfigured execution role "
                    "with excessive permissions, not a vulnerable dependency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The described root cause is a known "
                    "vulnerability in a bundled third-party library, which is "
                    "a dependency management issue, not an IAM permissions "
                    "issue."
                ),
            },
        ],
        "explanation": (
            "Serverless computing does not eliminate the customer's "
            "responsibility for application-level dependencies; the provider "
            "patches the platform, but code and libraries the developer "
            "bundles into the function must still be scanned and updated by "
            "the customer."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "A hosting provider's hypervisor management console (used to "
            "create, modify, and delete any customer's virtual machines) is "
            "reachable on the same network segment as guest VM production "
            "traffic. A penetration test shows that a compromised, low-value "
            "customer VM can reach the management console's login page. "
            "Which architectural change BEST reduces the risk this finding "
            "represents?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Move the hypervisor management interface onto a "
                    "dedicated, isolated out-of-band management network that "
                    "guest VM traffic cannot reach"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Isolating the management plane onto a separate "
                    "network removes the path from any compromised guest VM "
                    "to the console that controls every VM on the host, "
                    "directly closing the escalation path the pentest found."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Require a stronger password policy on the hypervisor "
                    "management console login page"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stronger password reduces brute-force risk "
                    "but does nothing to remove the fundamental exposure of a "
                    "privileged management interface to a network segment "
                    "reachable by low-trust, potentially compromised guest "
                    "VMs."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enable live migration so VMs can be moved between hosts "
                    "without downtime"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Live migration is an availability feature and "
                    "is unrelated to restricting network reachability of the "
                    "hypervisor management plane; it does not address the "
                    "exposure identified."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the memory and CPU reservation on the "
                    "management console VM"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting resource reservations affects "
                    "performance, not network exposure, and has no bearing on "
                    "whether a compromised guest VM can reach the management "
                    "plane."
                ),
            },
        ],
        "explanation": (
            "Because the hypervisor management plane can control every VM on "
            "a host, it must be isolated on a dedicated out-of-band "
            "management network unreachable from guest VM production "
            "traffic — placing it on a shared segment turns any compromised "
            "guest into a potential path to full host compromise."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-010",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A software asset inventory finds that a standard corporate "
            "laptop image includes roughly 200 applications, most bundled "
            "years ago as part of a vendor software suite. Interviews confirm "
            "fewer than 20 of these applications are actually used by any "
            "employee, yet all 200 remain installed fleet-wide and receive no "
            "consistent patch tracking. Which action BEST reduces the "
            "endpoint attack surface here?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Uninstall the applications that are not in active use and "
                    "build a new baseline image containing only required "
                    "software"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing unused software eliminates the "
                    "unpatched, untracked applications entirely rather than "
                    "trying to manage risk in software nobody needs — fewer "
                    "installed applications means fewer potential "
                    "vulnerabilities to track and exploit."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Leave all 200 applications installed but require the "
                    "vendor suite license to be renewed annually"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. License renewal has no bearing on whether the "
                    "unused applications are patched or how they enlarge the "
                    "attack surface; the applications remain installed and "
                    "unmanaged."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy endpoint detection and response (EDR) agents to "
                    "monitor the 200 installed applications for suspicious "
                    "behavior"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Monitoring for exploitation after the fact "
                    "does not reduce the number of unnecessary attack "
                    "surfaces present; removing unused software is a more "
                    "direct and preventive fix."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Move patch management responsibility for all 200 "
                    "applications to end users"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Delegating patching of unnecessary software to "
                    "end users does not remove the attack surface and is "
                    "unlikely to be executed consistently, leaving the "
                    "underlying risk unaddressed."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means removing unnecessary software, "
            "services, and features rather than trying to secure or monitor "
            "them in place — every unused application left installed is an "
            "unpatched liability with no corresponding business benefit."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management workflow",
        "stem": (
            "Using the emergency change process, an administrator applies a "
            "critical zero-day patch to a production database server outside "
            "the normal change advisory board (CAB) cycle. The patch breaks "
            "compatibility with a reporting application, causing a six-hour "
            "outage, because no one had documented how to revert the change "
            "and the administrator had to reconstruct the rollback steps "
            "under pressure. Which change management element would have BEST "
            "prevented the extended outage?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Requiring a documented backout/rollback plan as a "
                    "mandatory part of the emergency change record, even when "
                    "the CAB's standard advance-approval cycle is bypassed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A documented backout plan lets the team revert "
                    "a failed change immediately regardless of how urgently it "
                    "was approved; the outage was prolonged specifically "
                    "because no rollback procedure existed, not because the "
                    "patch itself was applied under emergency process."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Eliminating the emergency change process entirely so all "
                    "changes must go through the standard CAB cycle"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Removing the emergency process would have "
                    "delayed a critical zero-day patch, increasing exposure "
                    "time; the emergency path itself was appropriate, the "
                    "missing rollback plan was the actual gap."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Requiring two administrators to approve every emergency "
                    "change before it is applied"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Additional approvers might slow down applying "
                    "an urgent patch but would not have provided a way to "
                    "quickly revert the change once it broke the reporting "
                    "application."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Restricting emergency changes to business hours only"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting the timing of emergency changes "
                    "does not address the absence of a rollback plan and could "
                    "delay urgent patching of a zero-day, increasing risk "
                    "rather than reducing outage impact."
                ),
            },
        ],
        "explanation": (
            "Even under an expedited emergency change process, a documented "
            "backout plan is a core change management requirement — it is "
            "what allows a failed change to be reverted quickly instead of "
            "reconstructed under pressure during an active outage."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "A company's remote-access VPN concentrator authenticates users "
            "against a central RADIUS server. Security policy states that if "
            "the RADIUS server becomes unreachable, the VPN concentrator must "
            "deny all new connection attempts rather than granting access "
            "through any local fallback method. Which configuration BEST "
            "implements this policy?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure the VPN concentrator to fail closed on "
                    "authentication server unavailability, denying all new "
                    "connections until RADIUS service is restored"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Failing closed means the control defaults to "
                    "denying access when it cannot verify identity, which "
                    "exactly matches the stated policy of accepting an "
                    "availability impact rather than allowing unauthenticated "
                    "or weakly authenticated access."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Configure the VPN concentrator to fail open on "
                    "authentication server unavailability, granting access to "
                    "any user who attempts to connect"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fail open grants access without verifying "
                    "identity when RADIUS is unreachable — the direct opposite "
                    "of the stated policy, which explicitly requires denying "
                    "access under that condition."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Configure the VPN concentrator to fall back to a locally "
                    "cached list of usernames and passwords when RADIUS is "
                    "unreachable"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A local fallback still grants access through "
                    "an alternate method during the outage, which the policy "
                    "explicitly rules out; it is not equivalent to denying all "
                    "new connections."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure the VPN concentrator to queue connection "
                    "attempts and automatically retry RADIUS indefinitely "
                    "without ever denying or granting access"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Indefinitely queuing connections without a "
                    "defined deny behavior does not implement the explicit "
                    "policy requirement to deny all new connections when "
                    "RADIUS is unreachable."
                ),
            },
        ],
        "explanation": (
            "Fail-closed authentication is the correct choice whenever a "
            "policy prioritizes preventing unauthenticated access over "
            "maintaining availability during an outage of the identity "
            "verification service."
        ),
    },
    {
        "id": "nd3e-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Failure modes",
        "stem": (
            "A bank's VPN gateway validates client certificates using OCSP "
            "(Online Certificate Status Protocol) to confirm a certificate has "
            "not been revoked. Leadership requires that a revoked client "
            "certificate must never be able to establish a connection, even "
            "if that means legitimate users are temporarily locked out during "
            "an OCSP responder outage. Which OCSP configuration BEST meets "
            "this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Hard-fail (fail closed) OCSP checking, which blocks the "
                    "TLS handshake whenever the revocation status cannot be "
                    "confirmed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Hard-fail OCSP blocks any connection whose "
                    "revocation status cannot be positively confirmed, which "
                    "is the only configuration that guarantees a revoked (or "
                    "unverifiable) certificate can never authenticate — "
                    "exactly matching leadership's stated priority over "
                    "availability."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Soft-fail (fail open) OCSP checking, which allows the "
                    "connection to proceed if the OCSP responder cannot be "
                    "reached"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Soft-fail permits the handshake to complete "
                    "when the responder is unreachable, which means an "
                    "attacker who blocks OCSP traffic could get a revoked "
                    "certificate accepted — the opposite of the requirement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Disable revocation checking entirely to avoid any impact "
                    "from OCSP responder outages"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling revocation checking means a revoked "
                    "certificate would always be accepted, which directly "
                    "violates the requirement that revoked certificates must "
                    "never authenticate."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Switch from OCSP to a certificate revocation list (CRL) "
                    "that is downloaded once a year"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A CRL refreshed only annually would leave a "
                    "certificate revoked mid-year treated as valid for up to "
                    "twelve months, failing to meet a requirement that revoked "
                    "certificates must never be accepted."
                ),
            },
        ],
        "explanation": (
            "When a requirement explicitly prioritizes preventing revoked "
            "credentials from being accepted over maintaining availability, "
            "hard-fail (fail-closed) revocation checking is the correct "
            "choice, even though it accepts the risk of legitimate lockouts "
            "during a responder outage."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A border router uses stateless access control lists to filter "
            "traffic. For every internal host allowed to initiate an outbound "
            "connection, administrators must manually write a matching rule "
            "permitting the corresponding inbound return traffic, since the "
            "device does not track connection state. The rule base has grown "
            "to thousands of entries and administrators frequently create "
            "gaps that either block legitimate return traffic or leave overly "
            "broad inbound ports open. Which change BEST addresses this "
            "problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace the stateless device with a stateful firewall "
                    "that automatically tracks connection state and permits "
                    "return traffic for established sessions without a "
                    "separate explicit rule"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A stateful firewall maintains a connection "
                    "table and automatically allows return traffic that "
                    "matches an already-permitted outbound session, "
                    "eliminating the need to manually pair inbound and "
                    "outbound rules and closing the class of errors "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Add more stateless rules with narrower port ranges to "
                    "reduce the size of each individual gap"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Narrower port ranges may shrink individual "
                    "rule gaps but do not address the root cause — the device "
                    "still cannot track connection state — and rule sprawl "
                    "and manual pairing errors would continue."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Remove all inbound rules so that no return traffic is "
                    "ever permitted"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This would break every legitimate outbound "
                    "connection's return traffic, causing a total connectivity "
                    "failure rather than solving the rule-management problem."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Sort the existing stateless rules alphabetically by "
                    "destination IP address to make them easier to read"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reordering rules for readability does not "
                    "change the fundamental fact that the device is stateless "
                    "and requires manually paired rules for every "
                    "conversation; the structural problem remains."
                ),
            },
        ],
        "explanation": (
            "Stateless filtering requires an explicit rule for both "
            "directions of every allowed conversation and does not scale "
            "safely; a stateful firewall automatically permits return "
            "traffic for connections it has already approved, removing this "
            "entire category of manual-pairing error."
        ),
    },
    {
        "id": "nd3e-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A security architect is designing firewall zones for a new "
            "three-tier e-commerce application (web, application, and "
            "database tiers) that will be internet-facing. Which THREE "
            "practices are MOST appropriate for the firewall architecture? "
            "(Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Place the internet-facing web tier in a screened subnet "
                    "(DMZ) that is separate from the internal corporate "
                    "network"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A screened subnet isolates the internet-facing "
                    "tier so that if it is compromised, the attacker does not "
                    "land directly inside the internal network — a "
                    "foundational firewall zone design principle."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Configure the firewall rules protecting the database tier "
                    "to permit inbound traffic only from the specific "
                    "application-tier hosts on the required database port"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Restricting the database tier's inbound rules "
                    "to only the application tier on the necessary port "
                    "enforces least privilege between zones, so compromising "
                    "the web tier alone does not grant direct database "
                    "access."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy a web application firewall (WAF) in front of the "
                    "internet-facing web tier to inspect HTTP/HTTPS "
                    "application-layer traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A WAF adds application-layer inspection "
                    "specifically tuned for web attacks (such as SQL "
                    "injection and cross-site scripting) that a standard "
                    "network firewall's port- and protocol-based rules would "
                    "not catch."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Allow the database tier direct outbound internet access "
                    "so it can retrieve its own patches"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Giving the most sensitive tier direct internet "
                    "access creates an unnecessary exfiltration and "
                    "command-and-control path; patches should be retrieved "
                    "through a controlled, mediated update process instead."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Disable logging on the internal firewall between the "
                    "application and database tiers to maximize throughput"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling logging removes the visibility "
                    "needed to detect lateral movement between tiers, which "
                    "is precisely where an attacker who compromises the web "
                    "tier would attempt to pivot next."
                ),
            },
        ],
        "explanation": (
            "Sound firewall zone architecture for a multi-tier application "
            "combines a screened subnet for the internet-facing tier, "
            "least-privilege rules restricting each tier to only what the "
            "next tier requires, and application-layer inspection (a WAF) "
            "for internet-facing web traffic."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company deploys a forward proxy that requires each client "
            "browser to be manually configured with the proxy's address and "
            "port before web traffic is inspected and filtered. A review "
            "finds that unmanaged contractor laptops and BYOD mobile devices, "
            "which are never configured with the proxy settings, browse the "
            "internet completely uninspected. Which change BEST closes this "
            "gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace or supplement the explicit proxy with a "
                    "transparent (inline) proxy that intercepts all outbound "
                    "web traffic at the network layer regardless of client "
                    "configuration"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A transparent proxy sits inline in the network "
                    "path and redirects traffic for inspection without "
                    "requiring any client-side configuration, so unmanaged and "
                    "BYOD devices are inspected the same as managed corporate "
                    "laptops."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Distribute a document instructing contractors and BYOD "
                    "users to manually configure their own proxy settings"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Relying on unmanaged users to voluntarily "
                    "configure proxy settings is unenforceable and would "
                    "leave devices that skip the step — accidentally or "
                    "intentionally — uninspected, which is the exact gap "
                    "found."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the proxy server's memory allocation to improve "
                    "throughput for managed devices"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Performance tuning for already-configured "
                    "managed devices does nothing to bring unmanaged and BYOD "
                    "devices, which never used the proxy at all, under "
                    "inspection."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disable internet access entirely for all managed "
                    "corporate laptops to force everyone onto the same "
                    "network path"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling internet access for managed devices "
                    "does not affect unmanaged or BYOD devices, which are the "
                    "actual source of the uninspected traffic, and would "
                    "disrupt legitimate business use."
                ),
            },
        ],
        "explanation": (
            "An explicit proxy only inspects traffic from clients that are "
            "specifically configured to use it; a transparent, inline proxy "
            "intercepts traffic at the network layer so inspection applies "
            "uniformly regardless of device management state or client "
            "configuration."
        ),
    },
    {
        "id": "nd3e-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company's DNS filtering appliance blocks resolution of known "
            "malicious and policy-violating domains for all internal clients. "
            "Security analysts notice that a growing number of workstations "
            "are resolving blocked domains anyway, because their browsers "
            "have been updated to use DNS over HTTPS (DoH) with a hardcoded "
            "public third-party resolver, bypassing the internal DNS "
            "infrastructure entirely. Which control BEST restores visibility "
            "and enforcement over these lookups?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Block outbound connections to known public DoH resolver "
                    "IP addresses and domains at the firewall, forcing "
                    "clients to fall back to the internal, filtered DNS "
                    "resolver"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Blocking the encrypted DoH channel to external "
                    "resolvers at the network boundary removes the bypass "
                    "path, forcing DNS queries back through the internal "
                    "resolver where the filtering appliance can enforce "
                    "policy."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the DNS filtering appliance's block list update "
                    "frequency from daily to hourly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A faster block list update does not address "
                    "the actual problem — the queries are bypassing the "
                    "internal DNS resolver entirely via DoH, so the internal "
                    "appliance never sees them regardless of list freshness."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Disable the internal DNS resolver so all clients are "
                    "forced to use public resolvers directly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This would eliminate internal DNS filtering "
                    "for every client, not just the ones already bypassing it, "
                    "making the security posture worse rather than better."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Require all internal clients to use IPv6 instead of IPv4 "
                    "for DNS resolution"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The IP version used for transport has no "
                    "bearing on whether DNS queries are encapsulated in DoH "
                    "and sent to an external resolver, so this does not "
                    "address the bypass."
                ),
            },
        ],
        "explanation": (
            "DNS over HTTPS encrypts DNS queries and can hardcode a public "
            "resolver, bypassing internal DNS security controls entirely; "
            "the standard mitigation is to block outbound traffic to known "
            "public DoH resolvers at the firewall so lookups are forced back "
            "through the filtered internal resolver."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "A company enforces 802.1X port-based authentication on every "
            "wired switch port, requiring a valid certificate-based "
            "supplicant before a device is granted network access. Several "
            "network printers on the floor cannot run an 802.1X supplicant at "
            "all, and administrators need them to still reach the print "
            "server on a restricted VLAN without disabling 802.1X on their "
            "switch ports. Which feature BEST accommodates the printers "
            "without weakening the overall port security posture?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "MAC authentication bypass (MAB), which authenticates the "
                    "printer by its MAC address against a known-device list "
                    "and places it into a restricted VLAN if it cannot "
                    "perform 802.1X"
                ),
                "correct": True,
                "rationale": (
                    "Correct. MAB is designed exactly for devices that cannot "
                    "run an 802.1X supplicant — it authenticates by MAC "
                    "address as a fallback and can assign the device to a "
                    "restricted VLAN, preserving port-level enforcement "
                    "without disabling 802.1X."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Disable 802.1X on the switch ports connected to the "
                    "printers and leave them open"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling port security entirely for those "
                    "ports removes any authentication control, letting anyone "
                    "who plugs into that jack — printer or not — gain "
                    "unauthenticated network access."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Install a self-signed 802.1X supplicant certificate "
                    "directly on the switch itself"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The supplicant must run on the connecting "
                    "device (the printer) to authenticate that device; "
                    "installing a certificate on the switch does not give the "
                    "printer 802.1X capability it does not have."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Physically relocate the printers to a separate building "
                    "with no network connectivity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Removing network connectivity defeats the "
                    "printers' required function of reaching the print "
                    "server, and is a disproportionate response compared to "
                    "using MAB."
                ),
            },
        ],
        "explanation": (
            "MAC authentication bypass provides a controlled fallback "
            "authentication path for devices incapable of 802.1X, letting "
            "administrators grant them limited, VLAN-restricted access "
            "without disabling port-based authentication on the switch "
            "entirely."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "In a software-defined data center, a single centralized SDN "
            "controller programs the flow tables for every switch in the "
            "fabric. A security assessment notes that any attacker who "
            "compromises the controller could reprogram traffic forwarding "
            "and segmentation policy across the entire data center at once. "
            "Which control BEST addresses this specific risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Isolate and harden the SDN control plane on a dedicated "
                    "management network with strict role-based access control "
                    "and multifactor authentication for controller "
                    "administrators"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the SDN controller can reprogram "
                    "forwarding and segmentation for the entire fabric, "
                    "isolating and hardening the control plane with strict "
                    "access controls directly reduces the likelihood and "
                    "impact of the exact single-point-of-compromise risk the "
                    "assessment identified."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the number of physical switches in the fabric to "
                    "add redundancy"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding more switches increases forwarding "
                    "capacity and redundancy for individual link or switch "
                    "failure, but every switch still takes its flow-table "
                    "instructions from the same central controller, so "
                    "controller compromise still affects them all."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Configure each switch to accept flow-table updates from "
                    "any controller on the network to avoid a single point of "
                    "failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Accepting flow-table updates from any "
                    "controller would let an attacker stand up a rogue "
                    "controller and reprogram the fabric even more easily, "
                    "making the risk worse rather than better."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Migrate from an overlay-based SDN fabric to VLANs "
                    "configured manually on each switch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Abandoning SDN eliminates its operational "
                    "benefits and does not directly address securing a "
                    "centralized control plane; the assessment's concern is "
                    "about protecting the controller, not about removing SDN "
                    "itself."
                ),
            },
        ],
        "explanation": (
            "SDN's centralized control plane is powerful precisely because "
            "one controller governs the whole fabric — which also makes it a "
            "high-value target; the mitigation is to isolate and strictly "
            "control administrative access to that controller, not to add "
            "unrelated switch redundancy or weaken controller trust "
            "boundaries further."
        ),
    },
    {
        "id": "nd3e-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "In a software-defined data center, workloads are frequently "
            "migrated between hosts and subnets by the orchestration platform "
            "based on capacity. Traditional VLAN-based segmentation rules, "
            "which are tied to a workload's IP address and subnet, must be "
            "manually rewritten every time a workload moves, and mistakes "
            "have repeatedly left newly migrated workloads temporarily "
            "unprotected. Which segmentation approach BEST solves this "
            "problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Identity- or tag-based micro-segmentation, in which "
                    "security policy is bound to the workload's identity or "
                    "metadata tags and automatically follows it regardless of "
                    "which host, subnet, or IP address it moves to"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tag- or identity-based micro-segmentation "
                    "decouples policy from network location entirely, so a "
                    "workload's protection travels with it automatically when "
                    "it migrates, eliminating the manual VLAN-rule rewrite "
                    "and the exposure window that comes with it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Create a larger number of smaller VLANs so each workload "
                    "has less distance to migrate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Smaller VLANs still tie policy to IP "
                    "addressing and subnet membership; workloads still need "
                    "manual rule updates whenever they move between them, so "
                    "the underlying problem is unchanged."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Disable workload migration entirely so IP-to-VLAN "
                    "mappings never change"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling migration removes the orchestration "
                    "platform's core capacity-management capability and is a "
                    "disproportionate response compared to adopting "
                    "policy that follows workload identity."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Assign every workload the same VLAN so no migration ever "
                    "crosses a segmentation boundary"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Placing every workload on one VLAN eliminates "
                    "segmentation entirely, meaning a single compromised "
                    "workload could reach every other workload directly — the "
                    "opposite of the intended security posture."
                ),
            },
        ],
        "explanation": (
            "In highly dynamic, orchestrated environments, segmentation "
            "policy tied to static IP addresses or VLANs cannot keep up with "
            "workload mobility; binding policy to workload identity or tags "
            "instead lets protection travel automatically with the "
            "workload."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "Two data center gateways need to establish an IPSec VPN so that "
            "every packet traversing the public internet between the sites — "
            "including the original source and destination IP headers of the "
            "internal hosts — is fully encrypted and encapsulated inside a "
            "new outer IP header. Which IPSec mode BEST meets this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tunnel mode, which encrypts and encapsulates the entire "
                    "original IP packet, including its header, inside a new "
                    "outer IP packet"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tunnel mode encrypts the entire original "
                    "packet — payload and original IP header alike — and "
                    "wraps it in a new outer header for gateway-to-gateway "
                    "transport, which is exactly the site-to-site requirement "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Transport mode, which encrypts only the payload of the "
                    "original packet and leaves the original IP header exposed "
                    "for routing"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Transport mode leaves the original IP header "
                    "in the clear because it is designed for direct host-to-"
                    "host communication, not for hiding internal addressing "
                    "between two gateways as required here."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Aggressive mode, which speeds up IKE Phase 1 negotiation "
                    "by exchanging fewer messages"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Aggressive mode is an IKE negotiation "
                    "optimization about how the tunnel's keys are "
                    "established, not a data-encapsulation mode that "
                    "determines whether the original IP header is protected."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Opportunistic mode, which encrypts traffic only when both "
                    "endpoints happen to support IPSec automatically"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a standard IPSec encapsulation "
                    "mode and does not describe a mechanism for protecting the "
                    "original IP header between two site gateways."
                ),
            },
        ],
        "explanation": (
            "IPSec tunnel mode is used for gateway-to-gateway (site-to-site) "
            "VPNs because it protects the entire original packet, including "
            "its header, by wrapping it inside a new outer packet — "
            "transport mode, by contrast, only protects the payload between "
            "two communicating hosts."
        ),
    },
    {
        "id": "nd3e-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A security architect reviewing a long-lived site-to-site IPSec "
            "VPN finds that the same IKE security association (SA), and "
            "therefore the same derived session keys, has been in continuous "
            "use for over a year with no renegotiation. The architect is "
            "concerned that if a key were ever compromised, an attacker could "
            "decrypt the entire year of captured traffic. Which change BEST "
            "limits this exposure going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure a shorter SA lifetime so the tunnel "
                    "periodically renegotiates and derives fresh session keys "
                    "at regular intervals"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Setting a shorter SA lifetime forces periodic "
                    "rekeying, so even if one set of session keys were "
                    "eventually compromised, only the traffic protected by "
                    "that specific key interval would be at risk rather than "
                    "an entire year's worth."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Switch the VPN from IPSec to a plaintext GRE tunnel to "
                    "simplify key management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A plaintext GRE tunnel provides no encryption "
                    "at all, eliminating confidentiality entirely rather than "
                    "reducing the exposure window of a compromised key."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the Diffie-Hellman group size used during the "
                    "very first key exchange and leave the SA lifetime "
                    "unchanged"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stronger initial key exchange makes the "
                    "original negotiation harder to break, but it does not "
                    "limit how long a single derived key remains in use, so "
                    "the year-long exposure window described would remain "
                    "unchanged."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disable perfect forward secrecy to reduce the "
                    "computational overhead of key negotiation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling perfect forward secrecy would make "
                    "it easier, not harder, for an attacker with one "
                    "compromised long-term key to decrypt captured traffic "
                    "across the tunnel's lifetime."
                ),
            },
        ],
        "explanation": (
            "A shorter security association (SA) lifetime forces periodic "
            "rekeying, limiting how much historical traffic any single "
            "compromised key could expose — this is distinct from perfect "
            "forward secrecy, which protects past sessions if a long-term "
            "key is later compromised, but does not by itself force "
            "recurring renegotiation of an active tunnel."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A company's Zero Trust policy engine grants or denies access "
            "requests based solely on the requesting user's verified identity "
            "and successful multifactor authentication. A red team exercise "
            "shows that an employee's stolen credentials, used with a valid "
            "MFA token obtained through SIM-swapping, are granted full access "
            "from an unmanaged personal laptop that has no endpoint "
            "protection and is missing three months of OS security patches. "
            "Which Zero Trust gap does this exercise MOST clearly expose?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The policy engine's trust algorithm does not evaluate "
                    "device posture (patch level, endpoint protection status, "
                    "and management state) as an input alongside user "
                    "identity and MFA"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Zero Trust requires evaluating the device as "
                    "well as the user; here identity and MFA alone were "
                    "sufficient for access even though the connecting device "
                    "was unmanaged, unprotected, and unpatched — exactly the "
                    "missing device-posture pillar the exercise exposes."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Multifactor authentication is fundamentally ineffective "
                    "and should be removed from the Zero Trust architecture "
                    "entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MFA is a necessary Zero Trust control; the "
                    "gap here is that MFA alone was treated as sufficient, "
                    "not that MFA itself is ineffective — removing it would "
                    "make the environment less secure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The organization needs to replace its Zero Trust "
                    "architecture with a traditional perimeter-based VPN "
                    "model"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A traditional perimeter model would not "
                    "evaluate device posture either, and reverting away from "
                    "Zero Trust abandons its continuous verification benefits "
                    "rather than fixing the specific missing input."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The employee's identity should never have been "
                    "provisioned in the identity provider in the first place"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The employee is a legitimate user whose "
                    "credentials and MFA were stolen; the failure is that the "
                    "policy engine did not also evaluate the device the "
                    "request came from, not that the identity should not "
                    "exist."
                ),
            },
        ],
        "explanation": (
            "A mature Zero Trust trust algorithm evaluates multiple signals "
            "together — identity, authentication strength, and device "
            "posture — before granting access; relying on identity and MFA "
            "alone leaves a gap that stolen credentials plus a compromised "
            "MFA channel can exploit from an untrusted device."
        ),
    },
    {
        "id": "nd3e-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A security team discovers employees are uploading sensitive "
            "spreadsheets to several unsanctioned, personal SaaS storage "
            "accounts that IT has no visibility into or control over, because "
            "the corporate firewall only sees generic outbound HTTPS traffic "
            "and cannot distinguish sanctioned corporate SaaS use from "
            "personal SaaS use of the same provider. Which SASE component "
            "BEST provides visibility and policy enforcement over this cloud "
            "application usage?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A cloud access security broker (CASB) that inspects and "
                    "enforces policy on traffic to sanctioned and "
                    "unsanctioned SaaS applications, distinguishing "
                    "corporate from personal account usage"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A CASB is purpose-built to sit between users "
                    "and cloud services, giving visibility into shadow IT SaaS "
                    "usage and enforcing policies such as blocking uploads to "
                    "unsanctioned or personal instances of an otherwise "
                    "approved SaaS provider."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A next-generation firewall configured only to inspect "
                    "traffic by destination IP address and port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IP- and port-based inspection alone cannot "
                    "distinguish a sanctioned corporate SaaS tenant from a "
                    "personal account on the same provider, since both use "
                    "the same destination service and HTTPS port."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A site-to-site IPSec VPN connecting the corporate network "
                    "to each SaaS provider's data center"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Site-to-site VPNs connect two networks under "
                    "an organization's control; a public multi-tenant SaaS "
                    "provider does not offer this, and it would not provide "
                    "per-account visibility or policy enforcement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A packet broker that duplicates raw traffic to multiple "
                    "passive monitoring tools"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A packet broker only distributes copies of "
                    "traffic for passive analysis; it does not decrypt, "
                    "inspect application-layer SaaS context, or enforce "
                    "policy the way a CASB does."
                ),
            },
        ],
        "explanation": (
            "The cloud access security broker (CASB) is the SASE component "
            "specifically designed to give an organization visibility into, "
            "and policy control over, sanctioned and unsanctioned SaaS "
            "application usage — a gap that generic network firewalls and "
            "VPNs cannot close."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-025",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification",
        "stem": (
            "A defense contractor handles Controlled Unclassified Information "
            "(CUI) under a federal contract. An engineer, believing CUI is "
            "not truly sensitive because it is not formally 'classified,' "
            "emails a CUI-marked design document to a personal webmail "
            "account so he can work on it from home over the weekend. Which "
            "statement BEST explains why this action violates proper "
            "handling of CUI?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "CUI is a distinct, federally defined data classification "
                    "requiring specific handling and safeguarding controls "
                    "regardless of the fact that it falls below the "
                    "classified (Secret/Top Secret) tier"
                ),
                "correct": True,
                "rationale": (
                    "Correct. CUI is a formal classification requiring "
                    "specific safeguarding under federal requirements (such "
                    "as NIST SP 800-171), independent of whether it also "
                    "carries a national-security classification level; "
                    "moving it to an unmanaged personal email account "
                    "violates those controls."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The engineer's action is acceptable because only data "
                    "labeled Secret or Top Secret has any legal handling "
                    "requirements"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reflects the exact misconception the "
                    "scenario describes; CUI carries binding federal handling "
                    "and safeguarding requirements even though it is not "
                    "classified at the Secret or Top Secret level."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The action is acceptable as long as the engineer deletes "
                    "the email from his personal account after finishing the "
                    "work"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The violation occurs the moment CUI leaves an "
                    "approved, controlled system for an unmanaged personal "
                    "account; deleting the email afterward does not undo the "
                    "unauthorized disclosure or the loss of control over "
                    "where copies may exist."
                ),
            },
            {
                "id": "d",
                "text": (
                    "CUI handling requirements apply only to physical "
                    "documents, not to electronic files sent by email"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CUI safeguarding requirements apply "
                    "regardless of format, covering electronic transmission "
                    "and storage exactly as they cover physical documents."
                ),
            },
        ],
        "explanation": (
            "Controlled Unclassified Information is a formal classification "
            "tier with its own mandated safeguarding requirements; 'not "
            "classified' does not mean 'not sensitive,' and moving CUI to an "
            "unmanaged personal account is a handling violation regardless "
            "of intent."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-026",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Data protection methods",
        "stem": (
            "A cloud architect is designing encryption for millions of "
            "objects stored in cloud object storage. Rather than encrypting "
            "every object directly with a single master key stored in the "
            "cloud provider's key management service (KMS), the design "
            "generates a unique data encryption key (DEK) for each object, "
            "encrypts each DEK using the KMS-held customer master key (CMK), "
            "and stores only the encrypted DEK alongside the object. Which "
            "statement BEST explains the security benefit of this design over "
            "encrypting every object directly with the CMK?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "This envelope encryption design limits the CMK's direct "
                    "exposure to a small number of key-wrapping operations "
                    "and lets individual objects be re-keyed or rotated "
                    "without needing to decrypt and re-encrypt the entire "
                    "object with a new master key"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Envelope encryption keeps the highly sensitive "
                    "CMK used only to wrap/unwrap small DEKs rather than "
                    "encrypting bulk object data directly, minimizing its use "
                    "and exposure, while still allowing per-object key "
                    "rotation without re-encrypting every object with a new "
                    "master key."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It removes the need to store the CMK inside the key "
                    "management service at all"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The design still requires the CMK to remain "
                    "in the KMS, since it is used to wrap and unwrap every "
                    "object's DEK; the KMS-held CMK is the root of the whole "
                    "key hierarchy, not something eliminated by this design."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It guarantees that objects cannot be decrypted even by "
                    "an attacker who obtains both the CMK and the encrypted "
                    "DEK stored alongside the object"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An attacker who obtains both the CMK and the "
                    "wrapped DEK can unwrap the DEK and then decrypt the "
                    "object; envelope encryption reduces exposure of the CMK, "
                    "it does not make objects undecryptable if both keys are "
                    "compromised together."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It eliminates the need for any access control policy on "
                    "who can call the key management service"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Access control on who may invoke the KMS to "
                    "unwrap a DEK remains essential; envelope encryption is a "
                    "key-hierarchy design, not a substitute for identity and "
                    "access management around the KMS."
                ),
            },
        ],
        "explanation": (
            "Envelope encryption — wrapping a per-object data encryption key "
            "with a KMS-held master key rather than encrypting data directly "
            "with the master key — limits the master key's exposure and "
            "enables efficient, granular key rotation, which is why it is "
            "the standard design for encrypting large volumes of cloud "
            "object storage."
        ),
    },
    {
        "id": "nd3e-027",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A contract requires that a company's proprietary research data, "
            "stored in a cloud object storage bucket, be accessible only from "
            "within its home country. The security team configures a bucket "
            "policy that evaluates the source IP address of every request "
            "and denies access if the IP does not map to that country's "
            "address ranges. Which data protection method does this policy "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Geographic (geofencing) restriction, which limits data "
                    "access based on the requester's physical or network "
                    "location"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Restricting access based on the requester's "
                    "source IP mapping to a specific country is a geographic "
                    "restriction (geofencing) control, directly matching the "
                    "contractual location-based access requirement."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Tokenization, which replaces sensitive values with a "
                    "non-sensitive substitute token"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization changes how a sensitive value is "
                    "represented in storage; it has nothing to do with "
                    "restricting who may access data based on their "
                    "location, which is what this policy does."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data masking, which obscures part of a data field for "
                    "display purposes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Masking hides portions of data shown to a "
                    "user; it does not control whether the request is allowed "
                    "to reach the data at all based on source location, which "
                    "is what the IP-based policy enforces."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Role-based permission restriction, which limits access "
                    "based on the requester's assigned job function"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The policy described evaluates only the "
                    "source IP address and country, not the requester's role "
                    "or job function, so it is a location-based control, not "
                    "a role-based permission restriction."
                ),
            },
        ],
        "explanation": (
            "Geographic restriction (geofencing) controls limit data access "
            "based on the requester's physical or network location, which is "
            "exactly what an IP-address-based, country-specific bucket "
            "policy enforces — distinct from tokenization, masking, or "
            "role-based access control."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-028",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data states",
        "stem": (
            "An employee's unencrypted USB flash drive, containing a "
            "spreadsheet of employee Social Security numbers, is lost while "
            "commuting home. No cloud sync, network transfer, or active "
            "processing was involved — the drive was simply sitting in the "
            "employee's bag. Which data state was compromised, and which "
            "control would have BEST prevented the exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data at rest was compromised; full-disk or file-level "
                    "encryption on the removable media would have rendered "
                    "the contents unreadable without the decryption key"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Data stored on a drive that is not currently "
                    "being transmitted or actively processed is data at "
                    "rest; encrypting the removable media would have made "
                    "the spreadsheet unreadable to whoever found the lost "
                    "drive."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Data in transit was compromised; TLS encryption on the "
                    "company's web applications would have prevented the "
                    "exposure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. No network transmission occurred at the time "
                    "of loss — the drive was physically lost while stored in "
                    "a bag — so TLS, which protects data moving across a "
                    "network, would not have applied to this incident."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data in use was compromised; a secure enclave on the "
                    "employee's workstation would have prevented the "
                    "exposure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The data was not being actively processed in "
                    "memory at the time of loss; it was sitting statically on "
                    "storage media, which is the definition of data at rest, "
                    "not data in use."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No data state classification applies because the loss "
                    "was physical rather than a cyberattack"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data state classification (at rest, in "
                    "transit, or in use) describes the condition of the data "
                    "itself and applies regardless of whether the loss "
                    "resulted from a cyberattack or physical loss of the "
                    "storage medium."
                ),
            },
        ],
        "explanation": (
            "Data stored on media that is not currently being transmitted or "
            "processed is data at rest; encryption of removable storage "
            "media is the standard control for protecting data at rest "
            "against exactly this kind of physical loss or theft scenario."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-029",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "Database administrators need full, unmasked access to a "
            "production customer database for troubleshooting, while junior "
            "analysts querying the exact same live database in real time "
            "must see sensitive fields, such as national ID numbers, obscured "
            "automatically based on their role — without maintaining a "
            "separate, permanently altered copy of the data. Which technique "
            "BEST meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Dynamic data masking, which alters how sensitive field "
                    "values are displayed in query results in real time based "
                    "on the querying user's role, without changing the "
                    "underlying stored data"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Dynamic data masking applies masking rules at "
                    "query time based on the requester's role, so DBAs "
                    "querying with full privileges see real values while "
                    "junior analysts see obscured values from the exact same "
                    "live database — no separate copy is required."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Static data masking, which permanently overwrites "
                    "sensitive values in a separate, non-production copy of "
                    "the database"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking is applied to a separate copy "
                    "of the data used for non-production purposes such as "
                    "testing; it does not provide role-based masking on the "
                    "same live production database, which is what this "
                    "scenario requires."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Vault-based tokenization, which replaces sensitive "
                    "values with a randomly generated token stored in a "
                    "separate token vault"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization permanently replaces the stored "
                    "value with a token for every reader, rather than "
                    "displaying different views of the same underlying value "
                    "depending on the querying user's role."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Full-disk encryption on the database server's underlying "
                    "storage volumes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Full-disk encryption protects data at rest "
                    "against someone bypassing the database and reading raw "
                    "disk blocks; it has no effect on what an authenticated "
                    "database user sees in query results."
                ),
            },
        ],
        "explanation": (
            "Dynamic data masking is distinct from static masking because it "
            "is applied on the fly at query time based on the requesting "
            "user's role against the live production data, rather than "
            "permanently altering a separate copy of the database."
        ),
    },
    {
        "id": "nd3e-030",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A retailer wants to tokenize card numbers before they reach a "
            "decades-old mainframe order-processing application. The "
            "mainframe's field validation logic rejects any 16-digit value "
            "that does not pass a Luhn checksum, and rejects any value that "
            "is not exactly 16 digits long. A naive tokenization scheme that "
            "generates random 16-digit strings causes most transactions to "
            "fail mainframe validation. Which tokenization approach BEST "
            "resolves this without modifying the legacy mainframe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Format-preserving tokenization, which generates tokens "
                    "that match the original data's length and format and "
                    "pass the same validation checks, such as the Luhn "
                    "algorithm"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Format-preserving tokenization is specifically "
                    "designed to generate substitute values that satisfy the "
                    "original field's format and checksum requirements, "
                    "letting legacy validation logic like a Luhn check pass "
                    "without any changes to the mainframe application."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Standard random tokenization, continuing to generate "
                    "arbitrary 16-digit strings and instructing the mainframe "
                    "team to disable Luhn validation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling Luhn validation requires modifying "
                    "the legacy mainframe application, which the scenario "
                    "specifically rules out, and would also remove a "
                    "legitimate data-integrity check used elsewhere in the "
                    "application."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Full masking, replacing every digit of the card number "
                    "with an asterisk before sending it to the mainframe"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A fully masked value of all asterisks would "
                    "not pass a numeric, Luhn-validated 16-digit field check "
                    "and would also make the value useless for the "
                    "downstream order-processing logic that needs a "
                    "reference value."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Hashing the card number with SHA-256 before sending it "
                    "to the mainframe"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A SHA-256 hash produces a fixed-length "
                    "hexadecimal string that is neither 16 digits nor Luhn-"
                    "valid, so it would fail the mainframe's format "
                    "validation just as the naive random token did."
                ),
            },
        ],
        "explanation": (
            "Format-preserving tokenization generates substitute values that "
            "match the original data's length, character set, and even "
            "checksum properties, allowing tokenized data to pass through "
            "legacy validation logic unchanged — a key advantage over "
            "generic random tokenization, masking, or hashing."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-031",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A company backs up its file servers to two separate "
            "network-attached storage (NAS) appliances for redundancy. Both "
            "appliances sit in the same server room as the production file "
            "servers, and both are always connected to the same network. A "
            "fire in the server room destroys the production servers and "
            "both NAS appliances simultaneously. Which backup principle was "
            "violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The 3-2-1 backup rule, which requires at least three "
                    "copies of data on two different media types with at "
                    "least one copy stored offsite"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Both backup copies used the same media type and "
                    "were stored in the same physical location as production, "
                    "violating the 3-2-1 rule's requirement for an offsite "
                    "copy — which is exactly why a single localized event "
                    "(the fire) destroyed everything at once."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The principle of least privilege, because too many "
                    "administrators had access to the NAS appliances"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The incident described is a physical, "
                    "location-based loss (a fire), not an access-control or "
                    "privilege-related failure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The separation-of-duties principle, because the same "
                    "administrator managed both NAS appliances"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Who administers the appliances is unrelated "
                    "to the root cause of this loss, which was that both "
                    "copies shared the same physical location and were "
                    "destroyed by the same event."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The change management workflow, because the NAS "
                    "appliances were never formally approved through the "
                    "change advisory board"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Whether the appliances went through change "
                    "approval has no bearing on why a single fire was able "
                    "to destroy every copy of the data at once."
                ),
            },
        ],
        "explanation": (
            "The 3-2-1 backup rule exists precisely to prevent a single "
            "localized event from destroying every copy of an organization's "
            "data — keeping all backup copies in the same room as "
            "production, on the same media type, with no offsite copy, "
            "defeats the purpose of having redundant backups at all."
        ),
    },
    {
        "id": "nd3e-032",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Backups and replication",
        "stem": (
            "A ransomware operator encrypted an organization's production "
            "file servers and then pivoted to the backup infrastructure using "
            "the same compromised domain administrator credentials, deleting "
            "every recent backup before demanding payment. Which THREE "
            "backup design practices would BEST have protected the "
            "organization's backups from being reached and destroyed the "
            "same way? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Store at least one backup copy on immutable or write-"
                    "once-read-many (WORM) storage that cannot be altered or "
                    "deleted by any administrator during the retention period"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Immutable or WORM storage prevents deletion or "
                    "modification of backup data even by someone holding "
                    "valid administrative credentials, directly defeating the "
                    "attacker's ability to delete backups after compromising "
                    "an admin account."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Maintain at least one air-gapped or offline backup copy "
                    "that is disconnected from the production network"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An air-gapped or offline copy is unreachable "
                    "over the network the attacker used to pivot from the "
                    "production servers, so it survives even after domain "
                    "credentials are fully compromised."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Use separate backup administrator credentials that are "
                    "not part of the production Active Directory domain the "
                    "attacker compromised"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Isolating backup administration from the "
                    "production domain means that compromising domain admin "
                    "credentials does not automatically grant the attacker "
                    "the separate credentials needed to reach or delete the "
                    "backup repository."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Mount the backup repository as a writable network share "
                    "on every production server for fast, automated restores"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A backup repository that is continuously "
                    "mounted and writable from production servers is exactly "
                    "as reachable as the servers themselves once they are "
                    "compromised, which is what allowed the attacker to "
                    "delete the backups in this incident."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Grant the production domain administrators group full "
                    "control over the backup repository so any admin can "
                    "manage backups without requesting separate access"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is precisely the design flaw that "
                    "allowed the attacker's compromised domain admin "
                    "credentials to reach and delete the backups; backup "
                    "administration should be isolated from the production "
                    "domain, not merged with it."
                ),
            },
        ],
        "explanation": (
            "Ransomware resilience for backups depends on ensuring that "
            "compromising production credentials cannot also compromise the "
            "backups — immutability, air-gapping, and credential isolation "
            "each independently break the attack path the ransomware used to "
            "delete this organization's backups."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-033",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "High availability",
        "stem": (
            "A four-node database cluster requires a simple majority of "
            "nodes to agree before any node is allowed to serve as the "
            "active primary, in order to prevent conflicting writes. During a "
            "network partition, the cluster splits evenly into two groups of "
            "two nodes each. Neither group can reach a majority, so the "
            "entire cluster refuses to serve any writes until the partition "
            "is resolved manually. Which change BEST prevents this exact "
            "type of total outage in the future?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Add a lightweight witness (tie-breaker) node so the "
                    "cluster always has an odd total number of voting "
                    "members, ensuring a majority can always be reached during "
                    "a partition"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An odd-numbered voting membership, achieved by "
                    "adding a witness node, guarantees that a network split "
                    "can never produce two equally sized groups, so one side "
                    "can always reach majority and continue serving writes "
                    "without manual intervention."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Reduce the quorum requirement so that a single node can "
                    "act as primary during a partition"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Allowing a single node to become primary "
                    "during a partition reintroduces the exact split-brain "
                    "risk quorum voting was designed to prevent, since both "
                    "partitioned groups could independently elect a primary "
                    "and accept conflicting writes."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add a fifth full replica node holding a complete copy of "
                    "the database, but keep it on the exact same network "
                    "segment as the two existing groups"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a fifth node does create an odd count, "
                    "but placing it on the same network segment as the "
                    "existing nodes means the same partition event could "
                    "still split votes unevenly depending on how the segment "
                    "fails, unlike a witness specifically positioned to "
                    "remain reachable by exactly one side."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure all four nodes to always assume they are the "
                    "primary whenever they cannot reach the others"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This would cause every isolated node to "
                    "accept writes independently during any partition, "
                    "producing conflicting data across the cluster rather "
                    "than preventing the outage."
                ),
            },
        ],
        "explanation": (
            "Quorum-based clusters require an odd number of voting members "
            "so that a network partition can never produce two equally "
            "sized groups; a properly placed witness or tie-breaker node "
            "ensures a majority — and therefore a functioning primary — can "
            "always be determined."
        ),
    },
    {
        "id": "nd3e-034",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "A load balancer distributes traffic across three backend web "
            "servers. Its health check simply verifies that TCP port 443 is "
            "open on each server. One server's application process begins "
            "returning HTTP 500 errors on every request while the TCP port "
            "remains open and accepting connections, so the load balancer "
            "continues sending it a full share of user traffic. Which change "
            "to the health check configuration BEST addresses this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure a Layer 7 (application-layer) health check "
                    "that requests a specific URL and verifies the response "
                    "content or status code, removing a server from rotation "
                    "if it does not return a healthy response"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A Layer 7 health check evaluates whether the "
                    "application itself is functioning correctly, not just "
                    "whether the port is open, so a server returning HTTP 500 "
                    "errors would be detected as unhealthy and removed from "
                    "rotation even though its TCP port remains open."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the frequency of the existing Layer 4 TCP port "
                    "health check so it runs every second instead of every "
                    "ten seconds"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Running the same TCP-only check more "
                    "frequently does not change what it evaluates; the port "
                    "is still open and accepting connections, so the check "
                    "would continue to report the server as healthy despite "
                    "the application errors."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Remove health checking entirely and rely on round-robin "
                    "distribution to eventually route around failures"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Round-robin without any health check would "
                    "continue sending an equal share of traffic to the "
                    "failing server indefinitely, since round-robin selection "
                    "has no awareness of server health."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Add a second, identical Layer 4 TCP port health check on "
                    "a different port number"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Another Layer 4 check still only verifies "
                    "port reachability, not application response correctness, "
                    "so it would still fail to detect that the application "
                    "is returning errors on every request."
                ),
            },
        ],
        "explanation": (
            "A Layer 4 TCP health check only confirms a port is open, not "
            "that the application behind it is functioning; a Layer 7 "
            "application-layer health check that validates the actual "
            "response is required to detect and route around this class of "
            "'port open, application broken' failure."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-035",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Multi-cloud and platform diversity",
        "stem": (
            "A board of directors asks the CISO to justify the added "
            "operational cost of deliberately running workloads across two "
            "different public cloud providers instead of standardizing on "
            "one. Which THREE statements are legitimate security benefits of "
            "this multi-cloud, platform-diversity strategy? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It reduces the blast radius of a single provider's "
                    "regional outage or systemic misconfiguration, since "
                    "workloads on the other provider remain unaffected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the two providers are operationally "
                    "independent, an outage or systemic issue confined to one "
                    "provider does not automatically take down workloads "
                    "running on the other."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It avoids concentrating all of the organization's data "
                    "under a single provider's infrastructure, reducing the "
                    "impact of any one provider-side breach or compromised "
                    "administrative access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Spreading data across independent providers "
                    "means a breach of one provider's infrastructure, or "
                    "compromise of one provider's administrative access, does "
                    "not automatically expose everything the organization "
                    "runs in the cloud."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It prevents a single compromised set of cloud "
                    "administrator credentials from providing an attacker a "
                    "path to every workload the organization runs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since each provider typically has separate "
                    "identity and access management, credentials compromised "
                    "for one provider's console do not grant access to "
                    "workloads hosted with the other provider."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It always reduces the organization's total attack "
                    "surface compared to standardizing on a single provider"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Running on two providers generally increases "
                    "the total attack surface and monitoring burden, since "
                    "there are now two distinct sets of consoles, APIs, and "
                    "configurations to secure instead of one."
                ),
            },
            {
                "id": "e",
                "text": (
                    "It automatically ensures identical, consistent security "
                    "configuration across both providers without requiring "
                    "additional tooling"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Different providers have different native "
                    "security controls and configuration models, so "
                    "achieving consistent policy across them requires "
                    "deliberate cross-platform tooling and effort, not "
                    "something multi-cloud provides automatically."
                ),
            },
        ],
        "explanation": (
            "Multi-cloud/platform diversity trades increased operational and "
            "monitoring complexity for reduced blast radius, reduced "
            "single-provider data concentration risk, and reduced impact "
            "from any single set of compromised administrative credentials — "
            "it does not automatically shrink attack surface or unify "
            "configuration."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-036",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Power resilience",
        "stem": (
            "A data center has a properly sized UPS to bridge the gap until "
            "its diesel generator reaches full load, and the generator has "
            "ample fuel reserves. During a utility outage, however, the "
            "single automatic transfer switch (ATS) responsible for shifting "
            "the facility's load from utility power to generator power fails "
            "mechanically, leaving the facility with no path to backup power "
            "even though both the UPS and generator are otherwise healthy. "
            "Which improvement BEST addresses this specific failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Install a redundant automatic transfer switch so a "
                    "second, independent switch path can complete the "
                    "transfer to generator power if the primary ATS fails"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The ATS itself was the single point of failure "
                    "in this incident; a redundant ATS provides an "
                    "independent switching path so a mechanical failure in "
                    "one switch does not leave the facility with no route to "
                    "backup power at all."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the size of the generator's onboard fuel tank "
                    "to extend its runtime"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A larger fuel tank addresses how long the "
                    "generator can run once power is actually transferred to "
                    "it; it does nothing to fix the failed switch that "
                    "prevented the transfer from happening in the first "
                    "place."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add more UPS battery modules to extend the bridge time "
                    "before the generator must take over"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Extending the UPS bridge time only delays the "
                    "moment power runs out; it does not resolve the fact that "
                    "the ATS cannot complete the transfer to generator power "
                    "at all due to its mechanical failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Switch from a diesel generator to a natural-gas "
                    "generator for improved fuel reliability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the generator's fuel type does not "
                    "address the failure point described, which is the "
                    "single automatic transfer switch, not the generator's "
                    "fuel source."
                ),
            },
        ],
        "explanation": (
            "Power resilience requires eliminating single points of failure "
            "across the entire power path, not just the generator and UPS; "
            "an unredundant automatic transfer switch is just as capable of "
            "causing a total outage as an undersized generator or UPS would "
            "be."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-037",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "A company selects a disaster recovery site 400 miles from its "
            "primary data center specifically to achieve geographic "
            "dispersion from regional weather events. During a later "
            "regional fiber cut, both the primary site and the recovery site "
            "lose internet and WAN connectivity at the same time, because "
            "both sites' sole telecommunications carrier routes all of their "
            "circuits through the same regional fiber trunk. Which additional "
            "consideration would BEST have prevented this dual outage?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ensuring the recovery site uses a different "
                    "telecommunications carrier and physically diverse "
                    "circuit paths, not just physical distance from the "
                    "primary site"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Physical distance alone does not guarantee "
                    "independent network connectivity; both sites shared the "
                    "same carrier's fiber trunk, so true resilience required "
                    "carrier and circuit-path diversity in addition to "
                    "geographic dispersion."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Moving the recovery site even farther away, to 4,000 "
                    "miles instead of 400 miles"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Additional physical distance alone would not "
                    "have prevented the outage, since the actual cause was "
                    "both sites relying on the same carrier's shared fiber "
                    "trunk, not insufficient distance."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increasing the recovery time objective (RTO) so the "
                    "outage duration becomes acceptable"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Redefining the RTO changes the target "
                    "recovery time on paper but does nothing to prevent the "
                    "underlying shared-carrier single point of failure from "
                    "causing simultaneous outages at both sites."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Switching the recovery site from a warm site to a cold "
                    "site to reduce operating costs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The site tier (hot, warm, or cold) governs how "
                    "quickly equipment and data can be made operational; it "
                    "has no bearing on whether both sites share the same "
                    "telecommunications carrier and are therefore vulnerable "
                    "to the same fiber cut."
                ),
            },
        ],
        "explanation": (
            "True site resilience requires diversity in telecommunications "
            "carriers and circuit routing, not just physical distance "
            "between the primary and recovery sites — two geographically "
            "separated sites can still share a single point of failure if "
            "their connectivity ultimately depends on the same carrier's "
            "infrastructure."
        ),
    },
    {
        "id": "nd3e-038",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "A company's warm recovery site continuously replicates data "
            "with a recovery point objective (RPO) of 24 hours, which the "
            "business considers acceptable. However, the most recent "
            "disaster recovery test shows that fully restoring services at "
            "the warm site — including scaling up pre-provisioned but "
            "minimally sized servers and applying queued transaction logs — "
            "takes 18 hours, well beyond the board-approved recovery time "
            "objective (RTO) of 8 hours. Which action BEST addresses this "
            "finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Increase the pre-provisioned compute capacity and "
                    "automation at the warm site so that failover and "
                    "transaction log replay can complete within the "
                    "board-approved 8-hour RTO"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The test revealed that actual recovery "
                    "capability does not meet the approved RTO; increasing "
                    "pre-provisioned capacity and automating the failover and "
                    "log-replay steps directly targets the measured 18-hour "
                    "bottleneck so recovery can be completed within the "
                    "required 8 hours."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Change the RPO from 24 hours to 48 hours since the "
                    "current replication is working correctly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The RPO, which governs acceptable data loss, "
                    "is not the metric that failed the test; the problem "
                    "identified is that restoration takes too long relative "
                    "to the RTO, a completely separate measurement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Report the DR test as successful since data replication "
                    "achieved the target RPO"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Meeting the RPO does not mean the test was "
                    "successful; the test clearly showed the RTO commitment "
                    "was missed by ten hours, which is a material finding "
                    "that must be reported and remediated, not disregarded."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Discontinue disaster recovery testing since it revealed "
                    "an unfavorable result"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Discontinuing testing would hide the "
                    "capability gap rather than fix it, leaving the "
                    "organization unaware that it cannot meet its "
                    "board-approved recovery commitment during an actual "
                    "disaster."
                ),
            },
        ],
        "explanation": (
            "Disaster recovery testing exists to validate that measured "
            "recovery performance actually meets approved RTO and RPO "
            "targets; when a warm site's tested restoration time exceeds the "
            "approved RTO, the fix is to increase pre-provisioned capacity "
            "and automation at that site, not to redefine the metrics or "
            "stop testing."
        ),
    },
    # ------------------------------------------------------------------ #
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-039",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Resilience testing",
        "stem": (
            "A disaster recovery team wants to validate that its secondary "
            "site can correctly process real production transactions before "
            "declaring the site fully certified. The team configures the "
            "primary site to mirror a live copy of production traffic to the "
            "secondary site so both sites process the same transactions "
            "simultaneously and their outputs are compared, while the "
            "primary site continues to serve all actual users without "
            "interruption. Which type of resilience test does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A parallel test, in which the secondary site processes a "
                    "live copy of production data alongside the still-"
                    "operating primary site so results can be validated "
                    "without impacting real users"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A parallel test runs the recovery site "
                    "alongside — not instead of — the still-operating primary "
                    "site, processing a copy of real transactions to validate "
                    "correctness while avoiding any impact to actual "
                    "production users, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A tabletop exercise, in which stakeholders discuss the "
                    "DR plan around a conference table without touching any "
                    "live systems"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A tabletop exercise is a discussion-based "
                    "walkthrough with no live systems involved at all; this "
                    "scenario involves the secondary site actually processing "
                    "real, live transaction data."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A full interruption test, in which the primary site is "
                    "actually taken offline and all production traffic is "
                    "cut over to the secondary site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the primary "
                    "site continues to serve all actual users without "
                    "interruption; a full interruption test would take the "
                    "primary offline entirely, which did not happen here."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A checklist review, in which the DR plan documentation "
                    "is compared against a standard template for completeness"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A checklist review only evaluates whether "
                    "documentation exists and is complete; it involves no "
                    "live transaction processing or comparison of actual "
                    "system output, unlike the test described."
                ),
            },
        ],
        "explanation": (
            "A parallel test is the resilience-testing type that lets a "
            "recovery site prove it can correctly process real production "
            "data by running alongside the still-operating primary site, "
            "giving realistic validation without the availability risk of a "
            "full interruption test."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3e-040",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Third-party agreement types",
        "stem": (
            "A company is contracting with a managed hosting provider and "
            "wants a document that specifies measurable uptime guarantees "
            "(such as 99.9% availability), maximum support ticket response "
            "times, and financial service credits owed to the company if the "
            "provider fails to meet those targets. Which type of agreement "
            "BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A service level agreement (SLA), which defines "
                    "measurable performance targets and the remedies owed if "
                    "those targets are not met"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An SLA is specifically designed to define "
                    "quantifiable performance commitments — such as uptime "
                    "percentages and response times — along with the "
                    "penalties or credits triggered when the provider fails "
                    "to meet them, exactly matching this requirement."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A memorandum of understanding (MOU), which documents a "
                    "general intent to cooperate between two parties without "
                    "creating legally enforceable performance obligations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is typically a non-binding statement "
                    "of mutual intent and does not include enforceable, "
                    "measurable performance metrics or financial penalties, "
                    "which the company specifically requires here."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A business partnership agreement (BPA), which defines "
                    "the terms of a joint business venture between two "
                    "co-investing companies"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA governs a shared business venture "
                    "between partners with joint ownership interests; this "
                    "scenario is a customer-vendor hosting relationship, not "
                    "a joint venture."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A non-disclosure agreement (NDA), which legally obligates "
                    "both parties to protect each other's confidential "
                    "information"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects confidential information "
                    "shared between the parties; it says nothing about uptime "
                    "guarantees, response times, or financial penalties for "
                    "missed performance targets."
                ),
            },
        ],
        "explanation": (
            "A service level agreement (SLA) is the specific agreement type "
            "used to formalize measurable performance commitments, such as "
            "uptime and response-time targets, along with the remedies owed "
            "when a vendor fails to meet them."
        ),
    },
]
