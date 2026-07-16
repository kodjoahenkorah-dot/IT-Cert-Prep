"""CompTIA Security+ (SY0-701) practice question bank — targeted topic drill:
Cloud shared responsibility model.

34 scenario-driven questions (30 multiple_choice + 4 multiple_response), all
domain 3, focused on WHO is responsible (customer vs. cloud service provider)
for a given control layer — data, identity/access management, applications,
guest OS patching/configuration, middleware/runtime, hypervisor, physical
hosts, physical datacenter, and network controls — across IaaS, PaaS, and
SaaS. Recurring themes:

  * IaaS: the customer patches and hardens the guest OS; the provider owns
    hardware, hypervisor, and the physical facility.
  * PaaS: the provider manages the OS and runtime/middleware; the customer
    owns the application code and its data.
  * SaaS: the provider manages nearly the entire stack, but the customer
    STILL always owns data classification, identity/access configuration,
    and the service's security settings (e.g., a misconfigured S3 bucket or
    an over-permissioned SaaS role is a customer failure, not the
    provider's).
  * CASB visibility/enforcement over sanctioned and unsanctioned
    (shadow IT) SaaS use, and cloud misconfiguration as a customer-side
    responsibility-matrix failure regardless of service model.

study_topic values are restricted to the domain-3 labels: "Cloud
architecture", "Serverless and cloud architecture", "Third-party agreement
types", and "Data protection methods".
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # 1-8: IaaS responsibility split
    # ------------------------------------------------------------------ #
    {
        "id": "tcld-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company runs its own Linux virtual machines inside an IaaS "
            "provider's environment. A critical kernel vulnerability is disclosed "
            "and a patch is released. Under the shared responsibility model, who "
            "is responsible for applying this patch to the guest operating "
            "system?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The customer, because guest OS patching is a customer duty in IaaS",
                "correct": True,
                "rationale": (
                    "Correct. In IaaS, the provider stops at the hypervisor; "
                    "everything from the guest OS upward — including patching, "
                    "hardening, and configuration — is the customer's job."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The cloud provider, because it manages patching for every "
                    "virtual machine hosted on its infrastructure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The provider patches the hypervisor and host "
                    "firmware it controls, but never reaches into a customer's "
                    "guest OS in IaaS — that would violate tenant isolation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both parties jointly, since the VM runs on provider-owned "
                    "physical hardware"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical hardware ownership does not create joint "
                    "patching duty; the responsibility model draws a clean line at "
                    "the hypervisor, and guest OS patching sits entirely on the "
                    "customer's side of it in IaaS."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither party, because IaaS platforms patch guest kernels "
                    "automatically by default"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IaaS guest operating systems are not "
                    "auto-patched by the platform; the customer must apply "
                    "updates itself, whether manually or via its own automation."
                ),
            },
        ],
        "explanation": (
            "IaaS shifts hardware, hypervisor, and facility management to the "
            "provider, but leaves the guest OS — including kernel patching — "
            "squarely in the customer's column."
        ),
    },
    {
        "id": "tcld-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "An IaaS customer discovers that a fire suppression system failure "
            "damaged servers in one of the provider's data centers, causing an "
            "outage. Which party is responsible for the physical facility "
            "safeguards (fire suppression, physical access control) that failed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The cloud provider, because physical datacenter security is always the provider's responsibility",
                "correct": True,
                "rationale": (
                    "Correct. Regardless of service model, the physical "
                    "datacenter — including environmental and fire-suppression "
                    "controls — is always \"security of the cloud,\" owned by the "
                    "provider, since the customer has no physical access to the "
                    "facility."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The customer, because IaaS customers are responsible for "
                    "everything not explicitly labeled as software"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IaaS customers have no physical access to or "
                    "control over the provider's facility, so they cannot bear "
                    "responsibility for its physical safeguards under any "
                    "service model."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The customer's third-party auditor, since facility safety is "
                    "a compliance rather than a security function"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An auditor may verify controls exist, but "
                    "auditors do not own or operate the physical safeguards "
                    "themselves; that operational responsibility belongs to the "
                    "provider."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Whichever party's SLA has the lower uptime guarantee for "
                    "that region"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SLA uptime terms describe compensation for "
                    "downtime; they do not reassign who is responsible for "
                    "operating physical facility controls, which remains the "
                    "provider in all service models."
                ),
            },
        ],
        "explanation": (
            "Physical datacenter security — power, fire suppression, physical "
            "access — is the one layer that never shifts to the customer in any "
            "service model, because the customer has no physical presence in "
            "the facility."
        ),
    },
    {
        "id": "tcld-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A forensic review after a breach in an IaaS environment finds that "
            "the attacker escaped a customer's virtual machine and accessed "
            "other tenants' VMs by exploiting a flaw in the hypervisor itself. "
            "Who is accountable for remediating this specific flaw?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The cloud provider, because the hypervisor is provider-managed infrastructure in every service model",
                "correct": True,
                "rationale": (
                    "Correct. The hypervisor sits below the line the customer can "
                    "ever touch — it is provider-managed infrastructure in IaaS, "
                    "PaaS, and SaaS alike, so a hypervisor-level flaw is the "
                    "provider's responsibility to patch."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The affected customer, because the escape originated inside "
                    "their own virtual machine"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Where the attack originated does not change who "
                    "owns the vulnerable layer; a hypervisor flaw is exploitable "
                    "regardless of guest OS hardening, and only the provider can "
                    "patch the hypervisor itself."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Every tenant on the shared hardware equally, since they all "
                    "benefited from the same vulnerable hypervisor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tenants cannot patch infrastructure they have no "
                    "access to; accountability for the flaw itself rests with "
                    "the party that controls the hypervisor code — the provider."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The customer's cloud access security broker (CASB), since it "
                    "is responsible for all cross-tenant threats"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A CASB enforces policy on SaaS/cloud usage "
                    "visible to the customer; it has no ability to patch or "
                    "control the provider's underlying hypervisor."
                ),
            },
        ],
        "explanation": (
            "The hypervisor is infrastructure the customer never manages in any "
            "service model, so a hypervisor escape vulnerability is the cloud "
            "provider's responsibility to remediate."
        ),
    },
    {
        "id": "tcld-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "An organization runs a custom application on IaaS virtual machines "
            "it fully controls. Employees repeatedly reuse weak passwords to log "
            "into these VMs via SSH, and one is compromised via credential "
            "stuffing. Who bears responsibility for the weak identity and access "
            "controls that enabled this compromise?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The customer, because identity and access management is always a customer responsibility, even in IaaS",
                "correct": True,
                "rationale": (
                    "Correct. Identity and access management — including "
                    "credential strength, MFA enforcement, and account policy — "
                    "is a customer responsibility in every service model, "
                    "including IaaS where the customer controls the guest OS "
                    "login layer entirely."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The cloud provider, because it hosts the underlying "
                    "infrastructure the VMs run on"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hosting the infrastructure does not extend to "
                    "managing customer-created OS accounts and passwords inside "
                    "the customer's own virtual machines."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider's identity and access management (IAM) team, "
                    "since IAM is a shared service across all tenants"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The provider may offer IAM tooling, but "
                    "configuring and enforcing strong credential policy for "
                    "guest OS accounts is the customer's job to actually use "
                    "that tooling correctly."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No one, because credential stuffing exploits user behavior "
                    "outside the scope of the shared responsibility model"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Identity and access management, including "
                    "defenses against credential-based attacks like enforcing "
                    "MFA and strong password policy, is explicitly within the "
                    "customer's scope of the shared responsibility model."
                ),
            },
        ],
        "explanation": (
            "Identity and access management is one of the few responsibilities "
            "that never shifts to the provider — it belongs to the customer "
            "across IaaS, PaaS, and SaaS alike."
        ),
    },
    {
        "id": "tcld-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "In an IaaS deployment, which pairing of responsibilities correctly "
            "matches each party under the shared responsibility model?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Provider: physical hosts, hypervisor, network fabric. "
                    "Customer: guest OS, middleware, application, and data"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the textbook IaaS split: the provider "
                    "manages everything below and including the hypervisor and "
                    "the physical network, while the customer manages "
                    "everything from the guest OS upward."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Provider: physical hosts, hypervisor, guest OS. Customer: "
                    "middleware, application, and data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes PaaS, not IaaS — in IaaS the "
                    "provider does not manage the guest OS; that remains the "
                    "customer's responsibility."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Provider: physical hosts, hypervisor, guest OS, middleware, "
                    "application. Customer: data only"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes SaaS, not IaaS — IaaS leaves far "
                    "more of the stack, including the guest OS and application, "
                    "in the customer's hands."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Provider: everything including data. Customer: nothing, "
                    "since IaaS is fully outsourced"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. No cloud service model, including IaaS, ever "
                    "shifts data ownership and configuration entirely to the "
                    "provider; the customer always retains responsibility for "
                    "its own data."
                ),
            },
        ],
        "explanation": (
            "IaaS is the service model that leaves the most responsibility with "
            "the customer: the provider stops at physical hardware, hypervisor, "
            "and network fabric, while the customer owns the guest OS upward."
        ),
    },
    {
        "id": "tcld-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "An IaaS customer's virtual machine is compromised because the "
            "customer left an unnecessary RDP port open to the internet on a "
            "security group they configured themselves. The provider's network "
            "fabric and physical infrastructure were unaffected. Who is at "
            "fault for this specific exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer, because configuring security group/firewall "
                    "rules for their own instances is a customer responsibility "
                    "in IaaS"
                ),
                "correct": True,
                "rationale": (
                    "Correct. While the provider secures the underlying network "
                    "fabric, configuring instance-level network access controls "
                    "such as security groups is explicitly a customer task in "
                    "IaaS — this is a customer misconfiguration."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider, because all network-related security controls "
                    "fall under \"security of the cloud\""
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. \"Security of the cloud\" covers the underlying "
                    "network fabric and physical connectivity the provider "
                    "operates, not the security group rules a customer "
                    "configures for their own instances."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider, because it did not automatically close the "
                    "open port on the customer's behalf"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Providers do not silently override customer-"
                    "configured firewall/security group rules; doing so could "
                    "break legitimate customer configurations, so this remains "
                    "the customer's control to manage."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both equally, because the port was reachable over the "
                    "provider's public network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reachability over the provider's network does "
                    "not make the provider at fault; the provider carries the "
                    "traffic, but the customer decides which ports the traffic "
                    "is permitted to reach."
                ),
            },
        ],
        "explanation": (
            "In IaaS, instance-level security controls such as security groups "
            "and firewall rules are always a customer configuration task, even "
            "though the underlying network fabric is provider-managed."
        ),
    },
    {
        "id": "tcld-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company migrating to IaaS asks its provider who is responsible "
            "for encrypting data at rest on the virtual disks attached to its "
            "instances. Which answer correctly reflects the shared "
            "responsibility model?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer must enable and configure disk encryption for "
                    "its own volumes, even though the provider supplies the "
                    "encryption capability"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Providers typically offer encryption-at-rest "
                    "capability, but enabling it, choosing the key management "
                    "approach, and applying it to the customer's own volumes is "
                    "a customer configuration decision in IaaS."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider automatically and unconditionally encrypts "
                    "every customer's data at rest with no customer action "
                    "required"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While some providers enable default encryption, "
                    "customers cannot assume this and remain responsible for "
                    "verifying and configuring encryption settings that meet "
                    "their own compliance requirements."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data-at-rest encryption is not available in IaaS and must "
                    "be handled entirely within the application layer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IaaS providers commonly offer volume/disk-level "
                    "encryption as a built-in capability; it is a "
                    "misconception that this requires custom application-layer "
                    "encryption instead."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Encryption at rest is solely the responsibility of the "
                    "hardware vendor that manufactured the physical storage"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The physical hardware vendor has no "
                    "relationship with the customer's data configuration; "
                    "responsibility rests with the customer to enable and "
                    "configure the encryption feature the cloud provider makes "
                    "available."
                ),
            },
        ],
        "explanation": (
            "Data protection, including enabling and configuring encryption at "
            "rest, is a customer responsibility across all service models, even "
            "when the provider supplies the underlying encryption capability."
        ),
    },
    {
        "id": "tcld-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "For a standard IaaS deployment, which TWO of the following are "
            "customer responsibilities rather than provider responsibilities? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Applying security patches to the guest operating system",
                "correct": True,
                "rationale": (
                    "Correct. Guest OS patching is always a customer task in "
                    "IaaS, since the provider's management stops at the "
                    "hypervisor."
                ),
            },
            {
                "id": "b",
                "text": "Configuring identity and access management for the application",
                "correct": True,
                "rationale": (
                    "Correct. IAM configuration for the customer's own "
                    "application and accounts is a customer responsibility in "
                    "every service model, including IaaS."
                ),
            },
            {
                "id": "c",
                "text": "Maintaining the physical servers and storage arrays",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical hardware maintenance is the provider's "
                    "responsibility in IaaS, PaaS, and SaaS alike."
                ),
            },
            {
                "id": "d",
                "text": "Managing and patching the hypervisor",
                "correct": False,
                "rationale": (
                    "Incorrect. The hypervisor is provider-managed "
                    "infrastructure in every service model; the customer never "
                    "has access to patch it."
                ),
            },
        ],
        "explanation": (
            "In IaaS, the customer owns everything from the guest OS upward — "
            "including patching and IAM — while the provider retains "
            "everything at or below the hypervisor, including physical "
            "hardware and facility security."
        ),
    },
    # ------------------------------------------------------------------ #
    # 9-15: PaaS responsibility split
    # ------------------------------------------------------------------ #
    {
        "id": "tcld-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A development team deploys its web application to a PaaS offering "
            "that automatically manages the underlying operating system and "
            "language runtime. A vulnerability is later found in the runtime "
            "version the platform provisioned. Who is responsible for patching "
            "the runtime?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The cloud provider, because runtime and OS management is a defining feature of PaaS",
                "correct": True,
                "rationale": (
                    "Correct. PaaS is defined by the provider managing the OS "
                    "and runtime/middleware layer on the customer's behalf, so "
                    "patching that runtime is the provider's job — a key "
                    "distinction from IaaS."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The customer, because they authored the application code "
                    "running on top of the platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Owning the application code does not extend to "
                    "the runtime the platform provisions; that is precisely the "
                    "layer PaaS abstracts away from the customer."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The customer, because PaaS requires the same OS-level "
                    "management responsibilities as IaaS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the defining difference between "
                    "IaaS and PaaS — PaaS specifically removes OS/runtime "
                    "management from the customer, unlike IaaS."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A third-party auditor engaged under a business associate "
                    "agreement (BAA)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A BAA governs handling of protected data under "
                    "regulatory obligations; auditors do not perform runtime "
                    "patching, which is an operational task owned by the PaaS "
                    "provider."
                ),
            },
        ],
        "explanation": (
            "PaaS's defining trait is that the provider manages the OS and "
            "runtime/middleware, patching it on the customer's behalf — freeing "
            "the customer to focus on application code and data."
        ),
    },
    {
        "id": "tcld-010",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A company hosts its application on a PaaS platform. A code review "
            "reveals a SQL injection vulnerability in the application's own "
            "input handling logic. Who is responsible for fixing this flaw?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The customer, because application code security is always a customer responsibility, including in PaaS",
                "correct": True,
                "rationale": (
                    "Correct. Even though PaaS shifts OS and runtime management "
                    "to the provider, the customer still owns the application "
                    "code they write and deploy, including fixing "
                    "vulnerabilities like SQL injection in it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider, because PaaS platforms are responsible for "
                    "the full application stack"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. PaaS providers manage the OS and runtime "
                    "beneath the application, not the logic of the application "
                    "itself, which the customer writes and controls."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider, because the vulnerability exists within the "
                    "managed platform environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. \"Managed platform environment\" refers to the "
                    "OS/runtime layer the provider maintains — the application "
                    "code itself remains customer-owned and customer-secured."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither, because SQL injection is considered an inherent "
                    "and unavoidable risk of using any managed platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SQL injection is a well-understood, preventable "
                    "coding flaw addressed through secure coding practices like "
                    "parameterized queries — it is not an unavoidable platform "
                    "risk."
                ),
            },
        ],
        "explanation": (
            "In PaaS, the application layer and its code-level vulnerabilities "
            "remain the customer's responsibility, even though the provider "
            "manages the OS and runtime beneath it."
        ),
    },
    {
        "id": "tcld-011",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "Which statement BEST distinguishes the shared responsibility split "
            "in PaaS from IaaS?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "PaaS shifts OS and runtime/middleware management to the "
                    "provider, whereas IaaS leaves OS management with the "
                    "customer"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The defining architectural difference is that "
                    "PaaS providers manage the OS and runtime on the customer's "
                    "behalf, while IaaS customers retain that responsibility "
                    "themselves."
                ),
            },
            {
                "id": "b",
                "text": (
                    "PaaS gives the customer more control over the hypervisor "
                    "than IaaS does"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Neither PaaS nor IaaS customers ever manage the "
                    "hypervisor; that layer is always provider-controlled in "
                    "both models."
                ),
            },
            {
                "id": "c",
                "text": (
                    "PaaS eliminates the customer's responsibility for data "
                    "classification, unlike IaaS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data classification and protection remain "
                    "customer responsibilities in every service model, "
                    "including PaaS; this responsibility never shifts to the "
                    "provider."
                ),
            },
            {
                "id": "d",
                "text": (
                    "PaaS requires the customer to manage physical network "
                    "cabling, whereas IaaS does not"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical network infrastructure is provider-"
                    "managed in both PaaS and IaaS; customers never handle "
                    "physical cabling in either model."
                ),
            },
        ],
        "explanation": (
            "The key distinction between IaaS and PaaS is the OS/runtime "
            "layer: PaaS providers manage it, while IaaS customers retain that "
            "responsibility themselves."
        ),
    },
    {
        "id": "tcld-012",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A healthcare startup wants to deploy a custom application without "
            "managing servers, OS patching, or middleware, while retaining full "
            "control over the application's business logic and its data "
            "classification decisions. Which service model BEST fits, and who "
            "handles OS-level patching under it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PaaS; the provider handles OS and runtime patching",
                "correct": True,
                "rationale": (
                    "Correct. PaaS removes server, OS, and middleware "
                    "management from the customer while still letting the "
                    "customer control application logic and data — exactly "
                    "matching the stated requirements, with the provider "
                    "patching the OS/runtime."
                ),
            },
            {
                "id": "b",
                "text": "IaaS; the provider handles OS and runtime patching",
                "correct": False,
                "rationale": (
                    "Incorrect. In IaaS the customer, not the provider, is "
                    "responsible for OS and runtime patching — the opposite of "
                    "what the startup wants to avoid managing."
                ),
            },
            {
                "id": "c",
                "text": "SaaS; the customer handles OS and runtime patching",
                "correct": False,
                "rationale": (
                    "Incorrect. SaaS customers have no access to the OS/runtime "
                    "layer at all to patch, and SaaS would not give the startup "
                    "control over custom application business logic, which it "
                    "wants to retain."
                ),
            },
            {
                "id": "d",
                "text": "PaaS; the customer handles OS and runtime patching",
                "correct": False,
                "rationale": (
                    "Incorrect. PaaS is the right service model, but it is the "
                    "provider, not the customer, who manages OS and runtime "
                    "patching under PaaS — that is the entire point of the "
                    "model."
                ),
            },
        ],
        "explanation": (
            "PaaS is the model that removes server/OS/middleware management "
            "from the customer (provider handles patching) while preserving "
            "customer control over application logic and data."
        ),
    },
    {
        "id": "tcld-013",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A company's PaaS-hosted application suffers a breach because a "
            "developer stored an API key in plaintext inside the application's "
            "source repository. Who is responsible for this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The customer, because secure secrets handling within application code is a customer responsibility in PaaS",
                "correct": True,
                "rationale": (
                    "Correct. Even in PaaS, how the customer's application "
                    "manages secrets — such as using a secrets manager instead "
                    "of hardcoding credentials — remains a customer coding and "
                    "configuration practice, not something the platform "
                    "enforces automatically."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider, because PaaS platforms are responsible for "
                    "securing all code deployed to them"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The PaaS provider secures the runtime "
                    "environment the code executes in, not the coding "
                    "practices and secrets management decisions made within "
                    "the customer's own application."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider, because the API key was stored on "
                    "provider-managed infrastructure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Where the code executes does not shift "
                    "responsibility for how the customer wrote and stored "
                    "secrets within that code — that remains a customer "
                    "practice."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The source code repository vendor, since the plaintext key "
                    "was stored in version control"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A repository vendor hosts the code the "
                    "customer commits to it; it is not responsible for the "
                    "customer's decision to hardcode a secret into that code."
                ),
            },
        ],
        "explanation": (
            "Application-level security decisions, including secure secrets "
            "handling, remain a customer responsibility in PaaS even though "
            "the provider manages the underlying OS and runtime."
        ),
    },
    {
        "id": "tcld-014",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "In a PaaS deployment, which TWO of the following are provider "
            "responsibilities rather than customer responsibilities? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Patching the operating system underlying the platform",
                "correct": True,
                "rationale": (
                    "Correct. Patching the OS is a provider responsibility in "
                    "PaaS — this is the layer PaaS abstracts away from the "
                    "customer."
                ),
            },
            {
                "id": "b",
                "text": "Maintaining and updating the language runtime/middleware",
                "correct": True,
                "rationale": (
                    "Correct. Runtime and middleware maintenance is handled by "
                    "the provider in PaaS, freeing the customer to focus on "
                    "application code."
                ),
            },
            {
                "id": "c",
                "text": "Writing secure application code free of logic flaws",
                "correct": False,
                "rationale": (
                    "Incorrect. Application code security remains the "
                    "customer's responsibility in PaaS; the provider does not "
                    "review or secure the customer's business logic."
                ),
            },
            {
                "id": "d",
                "text": "Classifying and protecting the application's data",
                "correct": False,
                "rationale": (
                    "Incorrect. Data classification and protection are always "
                    "customer responsibilities, in PaaS just as in every other "
                    "service model."
                ),
            },
        ],
        "explanation": (
            "PaaS providers manage the OS and runtime/middleware layer, but "
            "application code, data protection, and IAM configuration remain "
            "customer duties, just as in IaaS and SaaS."
        ),
    },
    {
        "id": "tcld-015",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A team deploys business logic as serverless functions on a "
            "provider's Function-as-a-Service (FaaS) platform, a form of PaaS. "
            "The provider automatically provisions, scales, and patches the "
            "execution environment for each function invocation. Which "
            "statement about responsibility is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The provider is responsible for the underlying compute "
                    "environment and its patching; the customer remains "
                    "responsible for the function's code, its permissions, and "
                    "the data it processes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Serverless/FaaS pushes infrastructure and "
                    "runtime patching entirely to the provider, but the "
                    "customer's function code, the execution role's "
                    "permissions, and the data the function handles remain "
                    "customer responsibilities."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The customer must still patch the underlying compute "
                    "environment on a defined schedule, just as in IaaS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is precisely what serverless/FaaS "
                    "eliminates for the customer — the provider automatically "
                    "provisions and patches the execution environment, unlike "
                    "IaaS."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider assumes responsibility for the function's "
                    "code logic since it controls the execution environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Controlling the execution environment does not "
                    "extend to the function's own code logic, which the "
                    "customer writes and remains accountable for."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither party is responsible for function permissions, "
                    "since serverless platforms apply secure defaults "
                    "automatically"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Overly permissive execution roles are a common, "
                    "customer-caused serverless misconfiguration; the customer "
                    "must actively scope function permissions to "
                    "least privilege rather than relying on defaults alone."
                ),
            },
        ],
        "explanation": (
            "Serverless computing is an extreme point on the PaaS spectrum: "
            "the provider owns infrastructure and patching entirely, while the "
            "customer still owns function code, its assigned permissions, and "
            "the data it touches."
        ),
    },
    # ------------------------------------------------------------------ #
    # 16-25: SaaS responsibility split — data, IAM, and misconfiguration
    # ------------------------------------------------------------------ #
    {
        "id": "tcld-016",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company uses a SaaS email platform. An administrator "
            "accidentally grants \"anyone with the link\" sharing permissions on "
            "a folder containing sensitive HR files stored within the SaaS "
            "platform's file-sharing feature, exposing them publicly. Who is "
            "responsible for this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer, because configuring sharing permissions and "
                    "data access settings remains a customer duty even in SaaS"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SaaS providers manage nearly the entire "
                    "technology stack, but access/configuration decisions over "
                    "the customer's own data — such as sharing settings — "
                    "always remain the customer's responsibility."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider, because SaaS providers manage the entire "
                    "technology stack including data security"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. \"Managing the stack\" refers to infrastructure, "
                    "OS, runtime, and application code — it does not extend to "
                    "the access decisions a customer administrator makes about "
                    "their own stored data."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider, because the exposure occurred through a "
                    "feature built into the SaaS platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The platform providing a sharing feature does "
                    "not make the provider responsible for how the customer "
                    "chooses to configure that feature — the customer set the "
                    "permission that caused the exposure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No one, because SaaS eliminates the shared responsibility "
                    "model entirely in favor of full provider ownership"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The shared responsibility model still applies "
                    "in SaaS; it does not disappear — data classification and "
                    "access configuration remain with the customer even when "
                    "the provider manages everything else."
                ),
            },
        ],
        "explanation": (
            "Even in SaaS, where the provider manages almost the entire "
            "stack, the customer always retains responsibility for data "
            "classification and access/sharing configuration — this is the "
            "classic 'misconfigured sharing setting' failure mode."
        ),
    },
    {
        "id": "tcld-017",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A SaaS CRM vendor suffers a breach because an attacker exploited "
            "an unpatched vulnerability in the vendor's own application code, "
            "which the vendor alone develops and maintains. Which party is "
            "accountable for this specific flaw?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The SaaS provider, because in SaaS the application itself "
                    "is entirely provider-developed and provider-maintained"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In SaaS, the application code is written and "
                    "maintained by the provider, not the customer, so a flaw "
                    "in that code is the provider's accountability — a rare "
                    "case where responsibility shifts fully to the provider."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The customer, because customers are always accountable for "
                    "application-layer vulnerabilities regardless of service "
                    "model"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is true in IaaS and PaaS, where the "
                    "customer writes the application, but SaaS is the "
                    "exception — the provider, not the customer, owns and "
                    "writes the application code."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The customer's identity provider (IdP), since "
                    "authentication is the most likely attack path into SaaS "
                    "platforms"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario specifically describes an "
                    "application code vulnerability, not an authentication "
                    "compromise, so the customer's IdP has no bearing on this "
                    "particular flaw."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both parties equally, since data stored by the customer "
                    "was ultimately exposed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data exposure as an outcome does not make the "
                    "customer accountable for a flaw in code they never wrote "
                    "or had the ability to patch; the vendor alone controls "
                    "the SaaS application code."
                ),
            },
        ],
        "explanation": (
            "SaaS is the one model where the application layer itself shifts "
            "fully to the provider, so a code-level vulnerability in the "
            "vendor's own application is the provider's accountability — "
            "distinct from the customer's persistent duty over data and "
            "identity/access configuration."
        ),
    },
    {
        "id": "tcld-018",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A SaaS provider suffers a breach after an attacker compromises a "
            "customer's account using a password the employee reused from "
            "another site (no MFA was configured on the SaaS platform). Who is "
            "primarily responsible for this account compromise?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer, because configuring authentication controls "
                    "such as MFA for its own user accounts is a customer duty in "
                    "SaaS"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Even in SaaS, identity and access management — "
                    "including whether MFA is enforced for the customer's user "
                    "accounts — remains the customer's responsibility; the "
                    "provider offers the capability, but the customer must "
                    "enable and enforce it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider, because SaaS providers are responsible for "
                    "authenticating all users of their platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The provider builds and offers the "
                    "authentication mechanism (including MFA support), but "
                    "whether the customer configures and enforces it for their "
                    "own users is a customer decision."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider, because password reuse is a platform "
                    "vulnerability the provider failed to prevent"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Password reuse is a customer-side user "
                    "behavior and policy gap; the provider cannot control what "
                    "credentials an individual employee reuses across "
                    "unrelated sites."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither, because credential-stuffing attacks are considered "
                    "outside the shared responsibility model entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Identity and access management, including "
                    "defenses against credential-based attacks, is explicitly "
                    "part of the customer's scope within the shared "
                    "responsibility model, even in SaaS."
                ),
            },
        ],
        "explanation": (
            "Identity and access management — including MFA enforcement — is "
            "one of the responsibilities that never shifts to the provider, "
            "remaining with the customer across IaaS, PaaS, and SaaS."
        ),
    },
    {
        "id": "tcld-019",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "Which statement MOST accurately describes the shared "
            "responsibility model in SaaS?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The provider manages nearly the entire technology stack, "
                    "but the customer still owns data classification, identity "
                    "and access management, and configuration of the service"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SaaS shifts the most responsibility to the "
                    "provider of any service model, but data ownership, IAM "
                    "configuration, and service settings never leave the "
                    "customer's hands — this is the most tested distinction "
                    "on the exam."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider manages the entire stack, including data "
                    "classification and access control decisions, leaving the "
                    "customer with no security responsibilities"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the most common SaaS misconception — "
                    "customers frequently assume the provider owns everything, "
                    "but data and access decisions always remain customer "
                    "responsibilities."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The customer manages the OS and runtime, while the "
                    "provider only supplies physical hardware, matching the "
                    "IaaS model"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes IaaS, not SaaS — in SaaS the "
                    "customer has no access to manage the OS or runtime at "
                    "all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Responsibility in SaaS is determined entirely by which "
                    "party experiences a breach first"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Responsibility is defined in advance by the "
                    "architecture of the service model and contractual terms, "
                    "not retroactively assigned based on who is breached "
                    "first."
                ),
            },
        ],
        "explanation": (
            "SaaS is the model where the provider manages the most of the "
            "stack, yet the customer still always retains data "
            "classification, IAM, and configuration responsibilities — a "
            "distinction frequently missed in real-world misconfigurations."
        ),
    },
    {
        "id": "tcld-020",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A company discovers that a cloud object storage bucket used by its "
            "SaaS-integrated backup tool was left configured for public read "
            "access, exposing customer PII for months. The SaaS vendor states "
            "that the storage bucket in question was provisioned and configured "
            "by the customer's own IT team, not the vendor. Who is at fault?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer, because they configured the bucket "
                    "themselves and access-control configuration is always a "
                    "customer duty regardless of which vendor's tool relies on it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The vendor confirms it did not provision or "
                    "configure the bucket — the customer's own team did, and "
                    "access-control configuration of data storage is a "
                    "customer responsibility in every service model."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The SaaS vendor, because the exposed data was ultimately "
                    "used by the vendor's backup integration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The vendor's tool merely using the storage does "
                    "not make the vendor responsible for a bucket the customer "
                    "provisioned and misconfigured independently."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The cloud storage provider, because public buckets should "
                    "never be creatable under any circumstances"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Public bucket configuration is an intentional, "
                    "documented option many organizations legitimately use for "
                    "non-sensitive content; the provider offering the option "
                    "does not make it responsible for the customer's choice to "
                    "misapply it to PII."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The customer's cyber-insurance carrier, since financial "
                    "loss from the breach falls under its policy"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An insurance carrier may cover financial loss "
                    "after the fact, but it has no operational role in "
                    "configuring storage access and is not the party "
                    "accountable for the misconfiguration itself."
                ),
            },
        ],
        "explanation": (
            "Access-control configuration on customer-provisioned storage is a "
            "customer responsibility, regardless of which third-party tool or "
            "integration ultimately reads from that storage."
        ),
    },
    {
        "id": "tcld-021",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A security team wants a tool that sits between its users and "
            "multiple SaaS applications to enforce data loss prevention "
            "policy, detect risky third-party OAuth app grants, and discover "
            "unsanctioned (shadow IT) SaaS usage. Which control BEST fits?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cloud access security broker (CASB)",
                "correct": True,
                "rationale": (
                    "Correct. A CASB is purpose-built to sit between users and "
                    "cloud/SaaS services, enforcing DLP policy, monitoring "
                    "OAuth grants, and providing visibility into both "
                    "sanctioned and unsanctioned SaaS usage."
                ),
            },
            {
                "id": "b",
                "text": "Next-generation firewall (NGFW) at the network perimeter",
                "correct": False,
                "rationale": (
                    "Incorrect. An NGFW filters network-layer traffic at the "
                    "perimeter but is not designed to provide application-"
                    "level visibility into SaaS data handling or OAuth grants "
                    "the way a CASB is."
                ),
            },
            {
                "id": "c",
                "text": "Security information and event management (SIEM) platform",
                "correct": False,
                "rationale": (
                    "Incorrect. A SIEM aggregates and correlates logs for "
                    "detection and reporting; it does not sit inline to "
                    "enforce SaaS DLP policy or discover shadow IT the way a "
                    "CASB does."
                ),
            },
            {
                "id": "d",
                "text": "Web application firewall (WAF)",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF protects a specific web application from "
                    "inbound application-layer attacks; it is not designed to "
                    "monitor outbound user activity across many third-party "
                    "SaaS platforms."
                ),
            },
        ],
        "explanation": (
            "A CASB is the purpose-built control for enforcing policy and "
            "gaining visibility across sanctioned and unsanctioned SaaS usage, "
            "distinct from perimeter, SIEM, or WAF controls."
        ),
    },
    {
        "id": "tcld-022",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "An employee begins uploading sensitive company files to a "
            "personal file-sharing SaaS account that IT never approved or is "
            "aware of. Which control would MOST directly have detected this "
            "unsanctioned SaaS usage?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A CASB performing shadow IT discovery by analyzing "
                    "outbound traffic logs and cloud usage patterns"
                ),
                "correct": True,
                "rationale": (
                    "Correct. CASBs are specifically designed to discover "
                    "unsanctioned (shadow IT) cloud service usage by analyzing "
                    "outbound traffic and firewall/proxy logs for connections "
                    "to unapproved SaaS platforms."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The company's identity provider (IdP), since it manages "
                    "single sign-on for all approved SaaS applications"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An IdP only has visibility into applications "
                    "that are federated with it; by definition, an "
                    "unsanctioned personal account was never registered with "
                    "or visible to the IdP."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The approved SaaS platform's own built-in audit log, since "
                    "it records all file activity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The files were uploaded to a personal, "
                    "unapproved account entirely outside the company's "
                    "sanctioned SaaS platform, so that platform's audit log "
                    "would have no visibility into the activity."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Endpoint disk encryption on the employee's laptop"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data at rest on the "
                    "device itself; it does nothing to detect or prevent data "
                    "being uploaded to an external, unsanctioned cloud "
                    "service."
                ),
            },
        ],
        "explanation": (
            "CASBs specialize in shadow IT discovery, identifying "
            "unsanctioned cloud/SaaS usage that other identity- or platform-"
            "specific tools cannot see because the activity never touches "
            "sanctioned systems."
        ),
    },
    {
        "id": "tcld-023",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A company's SaaS project management tool allows administrators to "
            "set data retention and deletion policies for project records. "
            "Compliance requires records be purged after 90 days. Who must "
            "configure this retention policy?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The customer, because data lifecycle and retention "
                    "configuration is a customer responsibility even when the "
                    "provider hosts and stores the data"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The SaaS provider stores and hosts the data, but "
                    "deciding and configuring retention/deletion policy to meet "
                    "the customer's own compliance obligations is a customer "
                    "task in every service model."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider, because it physically stores all of the "
                    "customer's records"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physically storing the data does not make the "
                    "provider responsible for knowing or enforcing the "
                    "customer's specific regulatory retention requirements — "
                    "the customer must configure that policy."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Neither party, since data retention rules are set "
                    "automatically by industry-wide regulatory bodies"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Regulations may define requirements, but "
                    "someone must actually configure the technical control to "
                    "meet them — no automatic, regulator-driven enforcement "
                    "occurs within a SaaS platform."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The provider's data protection officer (DPO), since DPOs "
                    "are legally responsible for all customer data handling"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A provider's DPO oversees the provider's own "
                    "data protection obligations, not the customer's specific "
                    "compliance configuration decisions for their own tenant "
                    "data."
                ),
            },
        ],
        "explanation": (
            "Data governance decisions — including retention and deletion "
            "policy configuration — remain a customer responsibility in SaaS, "
            "even though the provider physically stores and hosts the data."
        ),
    },
    {
        "id": "tcld-024",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "In a SaaS deployment, which TWO of the following remain customer "
            "responsibilities despite the provider managing nearly the entire "
            "technology stack? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Classifying data and assigning appropriate sensitivity labels",
                "correct": True,
                "rationale": (
                    "Correct. Data classification is a customer responsibility "
                    "in every service model, since only the customer knows the "
                    "sensitivity and regulatory context of its own data."
                ),
            },
            {
                "id": "b",
                "text": "Configuring which users and roles can access which data within the application",
                "correct": True,
                "rationale": (
                    "Correct. Identity and access configuration for the "
                    "customer's own users remains a customer duty even in "
                    "SaaS, where the provider manages the application itself."
                ),
            },
            {
                "id": "c",
                "text": "Patching vulnerabilities in the SaaS vendor's own application source code",
                "correct": False,
                "rationale": (
                    "Incorrect. The SaaS provider writes and patches its own "
                    "application code; the customer has no access to do this "
                    "and is not responsible for it."
                ),
            },
            {
                "id": "d",
                "text": "Maintaining the physical servers that host the SaaS application",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical server maintenance is exclusively a "
                    "provider responsibility in SaaS, as in every other "
                    "service model."
                ),
            },
        ],
        "explanation": (
            "Data classification and access/IAM configuration are the two "
            "responsibilities that never leave the customer's hands, even in "
            "SaaS where the provider manages the application, runtime, OS, "
            "and physical infrastructure."
        ),
    },
    {
        "id": "tcld-025",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A SaaS vendor suffers a distributed denial-of-service (DDoS) "
            "attack against its multi-tenant infrastructure, causing an outage "
            "for all customers, including one company whose own configuration "
            "was flawless. Who is responsible for maintaining availability "
            "against this network-layer DDoS attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The SaaS provider, because protecting the shared "
                    "multi-tenant infrastructure from network-layer attacks is "
                    "a provider responsibility"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In SaaS, the provider owns and must defend the "
                    "underlying infrastructure — including DDoS protection for "
                    "the shared platform — since customers have no ability to "
                    "influence network-layer defenses of infrastructure they "
                    "don't control."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The affected customer, because availability of the "
                    "application is always a customer responsibility"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The customer has no access to the SaaS "
                    "provider's shared infrastructure to defend it; "
                    "infrastructure-level availability against attacks like "
                    "DDoS is a provider responsibility in SaaS."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Every customer collectively, since they all share the same "
                    "multi-tenant platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Customers sharing a platform does not give them "
                    "any control over or responsibility for that platform's "
                    "network-layer defenses, which are managed solely by the "
                    "provider."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The customer's internet service provider (ISP), since the "
                    "attack traffic transited their network en route"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The customer's own ISP has no relationship "
                    "with or control over the SaaS vendor's infrastructure "
                    "that was actually targeted and needs to be defended."
                ),
            },
        ],
        "explanation": (
            "Network and infrastructure-layer availability, including DDoS "
            "protection for shared multi-tenant SaaS infrastructure, is a "
            "provider responsibility since the customer has no access to "
            "that layer."
        ),
    },
    # ------------------------------------------------------------------ #
    # 26-30: Cross-model comparison, responsibility matrix reasoning
    # ------------------------------------------------------------------ #
    {
        "id": "tcld-026",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "As an organization moves the same workload from IaaS to PaaS to "
            "SaaS, which statement correctly describes how the shared "
            "responsibility model shifts?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The provider assumes progressively more infrastructure and "
                    "platform responsibility moving from IaaS to SaaS, but data "
                    "classification and identity/access management remain "
                    "customer responsibilities throughout"
                ),
                "correct": True,
                "rationale": (
                    "Correct. As service models move up the stack, the "
                    "provider takes on more of the OS/runtime/application "
                    "burden, but data governance and IAM configuration remain "
                    "constant customer duties across all three models."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The customer assumes progressively more responsibility "
                    "moving from IaaS to SaaS, since SaaS platforms expose more "
                    "configuration options"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards — moving from IaaS to SaaS "
                    "shifts more responsibility to the provider, not the "
                    "customer, even though certain customer duties like IAM "
                    "persist."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data classification responsibility shifts to the provider "
                    "once an organization adopts SaaS, since the provider "
                    "physically stores the data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data classification never shifts to the "
                    "provider in any service model; only the customer "
                    "understands the sensitivity and regulatory context of its "
                    "own data."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Identity and access management responsibility shifts "
                    "entirely to the provider in SaaS, since the provider "
                    "controls user login to the platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The provider builds the authentication "
                    "mechanism, but configuring and enforcing IAM policy for "
                    "the customer's own users remains a customer "
                    "responsibility even in SaaS."
                ),
            },
        ],
        "explanation": (
            "Moving from IaaS to PaaS to SaaS progressively shifts "
            "infrastructure and platform management to the provider, but data "
            "classification and IAM configuration remain constant customer "
            "responsibilities across all three models."
        ),
    },
    {
        "id": "tcld-027",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A procurement team is reviewing a responsibility matrix document "
            "provided by a prospective cloud vendor before signing a contract. "
            "What is the PRIMARY purpose of this document?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "To explicitly define which security and operational "
                    "controls the provider owns versus which the customer must "
                    "implement, reducing ambiguity and coverage gaps"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A responsibility matrix exists precisely to "
                    "remove ambiguity about who owns each control, so both "
                    "parties understand their obligations and no critical "
                    "control is assumed to be someone else's job and left "
                    "unaddressed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "To transfer all legal liability for a breach to the "
                    "provider regardless of which party misconfigured a control"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A responsibility matrix clarifies operational "
                    "ownership of controls; it does not transfer all legal "
                    "liability to the provider — customer-owned "
                    "misconfigurations remain the customer's accountability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "To replace the need for the customer to configure any "
                    "security controls of its own"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The matrix documents which controls the "
                    "customer must configure — it does not eliminate the "
                    "customer's own configuration duties."
                ),
            },
            {
                "id": "d",
                "text": (
                    "To satisfy a marketing requirement with no operational or "
                    "security relevance to either party"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The responsibility matrix has direct "
                    "operational and security relevance — it is used to plan "
                    "control coverage and avoid gaps, not as a marketing "
                    "artifact."
                ),
            },
        ],
        "explanation": (
            "A shared responsibility matrix's core purpose is eliminating "
            "ambiguity over control ownership between provider and customer, "
            "preventing gaps where each party assumes the other is handling a "
            "given control."
        ),
    },
    {
        "id": "tcld-028",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A breach investigation reveals that neither the customer nor the "
            "cloud provider had configured logging and monitoring for a "
            "critical administrative API, because each side assumed the other "
            "was handling it. What underlying failure MOST directly caused "
            "this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The organization failed to clearly define and document "
                    "responsibility ownership for this control in a shared "
                    "responsibility/RACI matrix before deployment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is a textbook responsibility-matrix gap — "
                    "without explicit documentation of who owns a given "
                    "control, both parties can reasonably assume the other is "
                    "handling it, leaving the control unaddressed entirely."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The cloud provider's hypervisor was misconfigured, "
                    "allowing the administrative API to bypass logging"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes an ownership/assumption "
                    "gap over who configures logging, not a hypervisor-level "
                    "technical flaw."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The customer's guest OS kernel was outdated and unable to "
                    "support modern logging agents"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states logging was never "
                    "configured due to mutual assumption, not that an "
                    "outdated kernel was technically incapable of supporting "
                    "logging."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The provider's physical datacenter lacked adequate power "
                    "redundancy for logging infrastructure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical power redundancy is unrelated to "
                    "whether logging was configured for an administrative "
                    "API; the failure described is one of ownership "
                    "assumption, not physical infrastructure."
                ),
            },
        ],
        "explanation": (
            "Gaps where both provider and customer assume the other owns a "
            "control are exactly what a documented shared responsibility "
            "matrix is meant to prevent — every control needs a single, "
            "explicitly assigned owner."
        ),
    },
    {
        "id": "tcld-029",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "An organization wants a contractually binding document that "
            "specifies the cloud provider's guaranteed uptime percentage and "
            "the credits owed if that uptime is not met, in support of "
            "responsibility for infrastructure-layer availability. Which "
            "document should it establish with the provider?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A service level agreement (SLA)",
                "correct": True,
                "rationale": (
                    "Correct. An SLA is the standard contractual document "
                    "specifying measurable service commitments, such as "
                    "uptime percentage and remedies (credits) if the provider "
                    "fails to meet them."
                ),
            },
            {
                "id": "b",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU expresses a non-binding mutual intent "
                    "to work together; it lacks the enforceable, measurable "
                    "commitments and remedies an SLA provides."
                ),
            },
            {
                "id": "c",
                "text": "A non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects confidential information "
                    "shared between parties; it says nothing about uptime "
                    "commitments or service credits."
                ),
            },
            {
                "id": "d",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A business partnership agreement defines "
                    "ownership stakes and financial structure in a joint "
                    "venture; it is not the vehicle for defining uptime "
                    "guarantees with a cloud vendor."
                ),
            },
        ],
        "explanation": (
            "An SLA is the specific contractual instrument used to define and "
            "enforce measurable provider commitments like uptime, directly "
            "supporting the provider's side of infrastructure-layer "
            "responsibility."
        ),
    },
    {
        "id": "tcld-030",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Third-party agreement types",
        "stem": (
            "A cloud provider's contract states it will encrypt data in "
            "transit and at rest at the infrastructure layer, but disclaims "
            "any responsibility for encryption keys the customer generates and "
            "manages for its own application-layer encryption. Which principle "
            "does this contract language reflect?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The shared responsibility model still applies within a "
                    "specific security domain (encryption) — the provider "
                    "secures its own infrastructure-layer encryption while the "
                    "customer manages controls it configures itself, like its "
                    "own key material"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Even within a single security domain like "
                    "encryption, the responsibility split still applies: the "
                    "provider secures what it controls (infrastructure "
                    "encryption), while the customer is accountable for "
                    "controls it configures and owns, such as its own "
                    "application-layer keys."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider is attempting to void its entire shared "
                    "responsibility obligation through contract language"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The provider still commits to infrastructure-"
                    "layer encryption; it is only disclaiming responsibility "
                    "for keys the customer itself generates and manages, not "
                    "voiding the model entirely."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Encryption key management is always a provider "
                    "responsibility, so this contract clause is invalid"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Key management for customer-generated, "
                    "application-layer keys is a customer responsibility; "
                    "assuming it is always the provider's job is a "
                    "misunderstanding of the model, not a sign the clause is "
                    "invalid."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This language only applies to SaaS deployments and is "
                    "irrelevant to IaaS or PaaS contracts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This kind of encryption-scope language "
                    "commonly appears across IaaS, PaaS, and SaaS contracts "
                    "alike wherever customers manage their own keys; it is not "
                    "limited to one service model."
                ),
            },
        ],
        "explanation": (
            "The shared responsibility model applies at a granular level even "
            "within a single domain like encryption — the provider secures "
            "infrastructure it controls, while the customer remains "
            "accountable for controls, like self-managed keys, that it "
            "configures itself."
        ),
    },
    # ------------------------------------------------------------------ #
    # 31-34: Additional cross-model / CASB / misconfiguration scenarios
    # ------------------------------------------------------------------ #
    {
        "id": "tcld-031",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "Which of the following is the BEST example of a customer "
            "responsibility that persists identically across IaaS, PaaS, and "
            "SaaS deployments?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Classifying data sensitivity and configuring who is authorized to access it",
                "correct": True,
                "rationale": (
                    "Correct. Data classification and access/identity "
                    "configuration are the two responsibilities that remain "
                    "with the customer unchanged across all three service "
                    "models, regardless of how much infrastructure the "
                    "provider manages."
                ),
            },
            {
                "id": "b",
                "text": "Patching the guest operating system",
                "correct": False,
                "rationale": (
                    "Incorrect. OS patching is a customer duty in IaaS, but "
                    "shifts to the provider in PaaS and SaaS — it does not "
                    "persist identically across all three models."
                ),
            },
            {
                "id": "c",
                "text": "Maintaining the application's source code",
                "correct": False,
                "rationale": (
                    "Incorrect. Application code is customer-owned in IaaS "
                    "and PaaS, but is provider-owned in SaaS — this "
                    "responsibility does not stay constant across all three "
                    "models."
                ),
            },
            {
                "id": "d",
                "text": "Managing the hypervisor",
                "correct": False,
                "rationale": (
                    "Incorrect. The hypervisor is always a provider "
                    "responsibility, never a customer one, in any service "
                    "model — this is the opposite of a customer "
                    "responsibility."
                ),
            },
        ],
        "explanation": (
            "Data classification and identity/access configuration are the "
            "constants of the shared responsibility model — every other "
            "layer's ownership shifts depending on IaaS, PaaS, or SaaS."
        ),
    },
    {
        "id": "tcld-032",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A retailer uses a SaaS payment processing platform. During an "
            "audit, it is discovered that the retailer's own staff granted a "
            "third-party marketing app broad OAuth access (read/write) to "
            "customer payment records through the SaaS platform's app "
            "marketplace, and that app was later compromised. Who is "
            "primarily accountable for this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The retailer, because approving and scoping third-party "
                    "OAuth application access is a customer identity/access "
                    "decision, even within a SaaS platform"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Granting OAuth scopes to a third-party app is an "
                    "access-control decision made by the customer's own "
                    "staff; reviewing and limiting such grants is squarely a "
                    "customer IAM responsibility, even inside a SaaS "
                    "marketplace."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The SaaS payment platform, because it hosts the "
                    "marketplace where the third-party app was listed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hosting a marketplace of optional integrations "
                    "does not make the platform responsible for a customer's "
                    "decision to grant a specific third-party app "
                    "overly broad access."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The third-party marketing app's cloud hosting provider, "
                    "since that is where the compromise technically occurred"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While the compromise happened within that "
                    "vendor's environment, the exposure of the retailer's "
                    "payment records traces back to the retailer's own "
                    "decision to grant excessive access in the first place."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No one, because OAuth grants made through an approved "
                    "marketplace are considered pre-vetted and risk-free"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Marketplace listing does not equal a risk "
                    "assessment of what data scopes a specific app should "
                    "receive; that review and scoping decision remains the "
                    "customer's job."
                ),
            },
        ],
        "explanation": (
            "Reviewing and limiting the scope of third-party OAuth grants is "
            "a customer identity/access-management decision — a frequently "
            "overlooked but classic example of customer responsibility "
            "persisting inside a SaaS platform."
        ),
    },
    {
        "id": "tcld-033",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "Which TWO of the following scenarios describe a genuine cloud "
            "PROVIDER failure, rather than a customer misconfiguration? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A flaw in the provider's hypervisor allows cross-tenant VM "
                    "memory access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The hypervisor is provider-managed infrastructure "
                    "in every service model, so a flaw in it is a genuine "
                    "provider failure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider's physical data center loses power due to a "
                    "failed backup generator it operates"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Physical facility infrastructure, including "
                    "backup power, is exclusively a provider responsibility in "
                    "every service model."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A customer administrator leaves an S3-style storage bucket "
                    "publicly readable"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a classic customer misconfiguration — "
                    "access control configuration on customer data is always a "
                    "customer responsibility, not a provider failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A customer fails to enable MFA on privileged SaaS accounts, "
                    "leading to account takeover"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IAM configuration, including enabling MFA, is a "
                    "customer responsibility across all service models — this "
                    "is a customer failure, not a provider one."
                ),
            },
        ],
        "explanation": (
            "Genuine provider failures are limited to layers the provider "
            "exclusively controls — hypervisor and physical infrastructure — "
            "while bucket permissions and IAM/MFA configuration are "
            "customer-side failures regardless of service model."
        ),
    },
    {
        "id": "tcld-034",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A CISO is briefing the board after a cloud data exposure incident "
            "and states, \"Because we used a reputable SaaS vendor with strong "
            "certifications, we assumed data security was entirely the "
            "vendor's responsibility, so we never reviewed our own sharing and "
            "access settings.\" Which concept BEST explains why this assumption "
            "led to the incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A misunderstanding of the shared responsibility model: "
                    "vendor reputation and certifications cover the provider's "
                    "side of the model, but never eliminate the customer's "
                    "persistent duty over data and access configuration"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the single most common real-world root "
                    "cause of cloud data breaches — organizations conflate a "
                    "vendor's strong certifications and reputation with a "
                    "belief that the vendor also owns the customer's own data "
                    "and access configuration decisions, which it never does."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A failed penetration test that should have caught the "
                    "exposure before go-live"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The stated root cause is an assumption about "
                    "who owns data/access configuration, not a missed finding "
                    "in a specific penetration test."
                ),
            },
            {
                "id": "c",
                "text": (
                    "An expired TLS certificate on the vendor's public-facing "
                    "login portal"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a data/sharing "
                    "configuration assumption, not a certificate lifecycle "
                    "failure, which is an unrelated technical issue."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Insufficient bandwidth between the customer's network and "
                    "the SaaS provider's data center"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bandwidth capacity has no relationship to "
                    "whether sharing and access settings were reviewed and "
                    "correctly configured; this is unrelated to the described "
                    "root cause."
                ),
            },
        ],
        "explanation": (
            "Vendor reputation and compliance certifications address the "
            "provider's side of the shared responsibility model, but never "
            "relieve the customer of its own persistent duty to configure "
            "data classification, sharing, and access settings correctly."
        ),
    },
]
