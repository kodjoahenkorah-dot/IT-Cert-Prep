"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file B."""

QUESTIONS = [
    {
        "id": "nd4b-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A network security engineer configures a perimeter firewall so that connection attempts are "
            "evaluated against an ordered list of 'if-then' conditions (e.g., 'if source is finance VLAN AND "
            "destination port is 3389 AND time is between 18:00-06:00, then deny'), processed strictly top-down "
            "until the first match is found. Which access control model does this configuration use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rule-based access control",
                "correct": True,
                "rationale": (
                    "Correct. Static conditional 'if-then' rules evaluated in a fixed, sequential order until "
                    "the first match is the defining characteristic of rule-based access control, as commonly "
                    "implemented in firewall and router ACLs."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC ties permissions to a user's assigned role or group membership; it does not "
                    "describe a sequentially processed list of network traffic conditions."
                ),
            },
            {
                "id": "c",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC's policy engine evaluates combinations of attributes together to reach a "
                    "decision; it is not defined by a strictly ordered, first-match-wins rule list the way "
                    "firewall/router ACL processing is."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC enforces access using fixed classification/clearance labels set by a central "
                    "authority; it does not describe conditional, time-based network traffic rules."
                ),
            },
        ],
        "explanation": (
            "Rule-based access control (as used in firewall/router ACLs) evaluates static, ordered conditional "
            "rules and stops at the first match. This differs from ABAC's simultaneous multi-attribute policy "
            "evaluation, RBAC's role-driven permissions, and MAC's centrally assigned classification labels."
        ),
    },
    {
        "id": "nd4b-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A classified government system enforces access using fixed sensitivity labels (Confidential, Secret, "
            "Top Secret) assigned by a central security authority. Even the creator/owner of a file cannot change "
            "its label or grant access to another user without the appropriate clearance, and the operating "
            "system kernel enforces this regardless of any file permission bits the owner sets. Which access "
            "control model is in use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mandatory access control (MAC)",
                "correct": True,
                "rationale": (
                    "Correct. MAC enforces access based on centrally assigned, non-discretionary classification "
                    "labels that the resource owner cannot override, with enforcement built into the kernel/OS — "
                    "exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC is the opposite of what is described: it lets the resource owner control who "
                    "gets access, whereas in this scenario the owner explicitly cannot change access or labels."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC assigns permissions through role membership; it does not describe fixed "
                    "sensitivity labels enforced centrally and non-discretionarily at the kernel level."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. While clearance could be modeled as one attribute, ABAC implies a dynamic policy "
                    "engine evaluating multiple attributes; the defining trait here is non-discretionary, "
                    "centrally controlled classification enforcement that the owner cannot override, which is "
                    "specifically MAC."
                ),
            },
        ],
        "explanation": (
            "MAC enforces non-discretionary access based on classification/clearance labels controlled by a "
            "central authority, with the OS/kernel enforcing the policy regardless of the resource owner's "
            "wishes — the hallmark difference from DAC, RBAC, and ABAC."
        ),
    },
    {
        "id": "nd4b-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "After a critical remote code execution vulnerability is disclosed in a widely used open-source "
            "logging library, a security team needs to rapidly determine which of the organization's hundreds of "
            "internally developed applications include the vulnerable library as a transitive dependency, even "
            "though no developer directly imports it by name in most projects. Which practice would have allowed "
            "the team to answer this question within minutes rather than days?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Maintaining a software bill of materials (SBOM) for every build, generated through software composition analysis (SCA)",
                "correct": True,
                "rationale": (
                    "Correct. An SBOM produced via SCA inventories every direct and transitive dependency and "
                    "version in each build, allowing an instant search for a specific vulnerable library across "
                    "the entire application portfolio."
                ),
            },
            {
                "id": "b",
                "text": "Running a static application security testing (SAST) scan on each application's proprietary source code",
                "correct": False,
                "rationale": (
                    "Incorrect. SAST analyzes code developers wrote; it does not reliably enumerate third-party "
                    "or transitive dependency versions bundled into a build the way an SBOM inventory does."
                ),
            },
            {
                "id": "c",
                "text": "Reviewing dynamic application security testing (DAST) reports from the last major release",
                "correct": False,
                "rationale": (
                    "Incorrect. DAST tests a running application's external behavior; it does not reliably "
                    "confirm the presence of a specific vulnerable library version across many applications."
                ),
            },
            {
                "id": "d",
                "text": "Increase the frequency of penetration tests scheduled for next quarter",
                "correct": False,
                "rationale": (
                    "Incorrect. Penetration tests are time-intensive, manual, and scheduled; they are not a rapid "
                    "inventory mechanism to answer 'which applications contain library X version Y' within "
                    "minutes."
                ),
            },
        ],
        "explanation": (
            "A software bill of materials, produced through software composition analysis, provides a searchable "
            "inventory of every dependency (direct and transitive) in every build, enabling rapid identification "
            "of affected applications when a new dependency vulnerability is disclosed."
        ),
    },
    {
        "id": "nd4b-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A web application's API endpoint '/api/invoices/{id}' returns invoice details based solely on the "
            "numeric ID supplied in the URL. A penetration tester changes the ID value and successfully retrieves "
            "other customers' invoices without any additional authentication or ownership check. Which class of "
            "vulnerability was exploited, and what is the correct remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insecure direct object reference / broken object-level authorization; remediate by adding server-side checks that verify the requesting user owns or is entitled to the requested object",
                "correct": True,
                "rationale": (
                    "Correct. Retrieving another user's data simply by changing an ID, with no server-side "
                    "ownership verification, is the defining pattern of an insecure direct object reference / "
                    "broken object-level authorization flaw, fixed by enforcing per-object authorization checks."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site scripting (XSS); remediate by encoding output rendered in the browser",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS involves injecting malicious script into pages viewed by other users; this "
                    "scenario involves no script injection, only unauthorized retrieval of data via an ID change."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site request forgery (CSRF); remediate by adding anti-CSRF tokens to state-changing forms",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks an authenticated user's browser into submitting unwanted requests; "
                    "the tester here directly changed a URL parameter to view data, which is an authorization "
                    "flaw, not a forged cross-site request."
                ),
            },
            {
                "id": "d",
                "text": "SQL injection; remediate with parameterized queries",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no indication of malformed SQL syntax being injected; the ID supplied "
                    "was a valid, well-formed value belonging to another customer, indicating missing "
                    "authorization logic rather than unsanitized input."
                ),
            },
        ],
        "explanation": (
            "This is a textbook insecure direct object reference (IDOR) / broken object-level authorization "
            "(BOLA) flaw: the API trusts the client-supplied ID without verifying the requester is authorized to "
            "access that specific object. The fix is server-side authorization logic per request, not input "
            "sanitization or CSRF tokens."
        ),
    },
    {
        "id": "nd4b-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A quarterly review using a cloud access security broker (CASB) reveals that several business units "
            "have been uploading corporate data to personal cloud storage accounts that were never approved, "
            "licensed, or recorded in the IT asset inventory. Which asset management practice would BEST prevent "
            "this type of unauthorized, unaccounted-for asset use going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Implement a formal procurement/acquisition process requiring all new software and SaaS services to be registered and approved before use, paired with ongoing CASB-based discovery of unsanctioned services",
                "correct": True,
                "rationale": (
                    "Correct. Governing acquisition at intake and continuously discovering unsanctioned services "
                    "in use is the combination that prevents shadow IT/unauthorized assets from persisting "
                    "unaccounted for."
                ),
            },
            {
                "id": "b",
                "text": "Increase the encryption key length used for the corporate file server",
                "correct": False,
                "rationale": (
                    "Incorrect. Key length on an already-sanctioned file server has no bearing on employees "
                    "using unapproved external cloud storage accounts outside the inventory."
                ),
            },
            {
                "id": "c",
                "text": "Require additional security awareness training focused solely on phishing recognition",
                "correct": False,
                "rationale": (
                    "Incorrect. Phishing-focused training addresses a different threat vector entirely and does "
                    "not close the governance/inventory gap that allowed unsanctioned cloud services to go "
                    "undetected."
                ),
            },
            {
                "id": "d",
                "text": "Reduce the number of licensed seats for the approved corporate file-sharing platform to cut costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing legitimate licenses does not prevent unauthorized cloud storage use and "
                    "could worsen the problem by pushing more users toward unsanctioned alternatives."
                ),
            },
        ],
        "explanation": (
            "Effective asset management requires governance at acquisition (approval/registration before use) "
            "combined with ongoing, automated discovery (e.g., CASB) to surface shadow IT and unauthorized "
            "services that never entered the formal inventory."
        ),
    },
    {
        "id": "nd4b-006",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOAR playbook uses a service account with domain administrator rights to perform automated "
            "account-disablement actions during phishing response. A logic error in a new playbook version "
            "causes it to iterate through and disable every account in the domain, including service accounts "
            "required for production systems, within seconds. Which underlying issue is the ROOT CAUSE that "
            "allowed this incident to have such a large blast radius?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The automation service account was provisioned with far more privilege (domain admin) than the specific task required, violating least privilege",
                "correct": True,
                "rationale": (
                    "Correct. A least-privilege violation is what allowed one logic bug to affect the entire "
                    "domain instead of being limited in scope; a properly scoped account could only have acted "
                    "on the accounts it was actually intended to manage."
                ),
            },
            {
                "id": "b",
                "text": "The playbook was written in a scripting language instead of a compiled language",
                "correct": False,
                "rationale": (
                    "Incorrect. The programming language used to write the playbook has no bearing on the scope "
                    "of privilege held by the account executing it."
                ),
            },
            {
                "id": "c",
                "text": "The SIEM correlation rule that triggered the playbook had too low a confidence threshold",
                "correct": False,
                "rationale": (
                    "Incorrect. A poor trigger threshold could cause the playbook to run unnecessarily, but it "
                    "does not explain why a single logic bug was able to impact the entire domain rather than a "
                    "single account — that blast radius is a privilege-scoping problem."
                ),
            },
            {
                "id": "d",
                "text": "The organization had not yet migrated the SOAR platform to a cloud-hosted deployment",
                "correct": False,
                "rationale": (
                    "Incorrect. Hosting location (on-premises vs. cloud) has no bearing on the scope of damage "
                    "caused by an over-privileged automated action."
                ),
            },
        ],
        "explanation": (
            "Automation amplifies whatever privilege the executing account holds. Scoping automation service "
            "accounts to least privilege limits the blast radius of any logic error, misconfiguration, or abuse, "
            "regardless of what triggered the playbook to run."
        ),
    },
    {
        "id": "nd4b-007",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "Select TWO statements that correctly distinguish 'automation' from 'orchestration' in the context of "
            "security operations."
        ),
        "options": [
            {
                "id": "a",
                "text": "Automation refers to executing a single, repeatable task without human intervention (e.g., automatically blocking an IP on one firewall).",
                "correct": True,
                "rationale": (
                    "Correct. Automation describes a discrete, repeatable action performed without a human "
                    "manually executing each step."
                ),
            },
            {
                "id": "b",
                "text": "Orchestration refers to coordinating and sequencing multiple automated tasks across different tools into a single end-to-end workflow (e.g., a phishing response playbook spanning email, threat intel, and endpoint tools).",
                "correct": True,
                "rationale": (
                    "Correct. Orchestration is the higher-level coordination layer that chains automated tasks "
                    "across disparate tools into one cohesive workflow."
                ),
            },
            {
                "id": "c",
                "text": "Automation and orchestration are interchangeable terms with no meaningful technical distinction in a SOAR platform.",
                "correct": False,
                "rationale": (
                    "Incorrect. They represent different layers — a single automated task versus multi-tool "
                    "workflow coordination — and are not interchangeable concepts."
                ),
            },
            {
                "id": "d",
                "text": "Orchestration can only be performed manually by a security analyst typing individual commands into each tool's console.",
                "correct": False,
                "rationale": (
                    "Incorrect. Orchestration specifically refers to automated coordination across tools, not "
                    "manual, one-at-a-time command entry."
                ),
            },
        ],
        "explanation": (
            "Automation executes individual repeatable tasks without human input; orchestration coordinates "
            "multiple automated tasks across different tools/systems into a single workflow — a layered "
            "distinction commonly tested on SY0-701."
        ),
    },
    {
        "id": "nd4b-008",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic responder arrives at a running workstation whose entire hard drive is protected with "
            "full-disk encryption. The responder knows that powering off the system will make the disk contents "
            "unreadable without a recovery key that is not otherwise available. What should the responder do "
            "FIRST to preserve access to the encrypted data for later analysis?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Perform a live memory (RAM) capture to attempt to extract the encryption key/keying material while the volume is still mounted and decrypted",
                "correct": True,
                "rationale": (
                    "Correct. While the system is running and the volume is decrypted, the encryption key or "
                    "keying material typically resides in RAM. Capturing memory live is the only opportunity to "
                    "preserve access before the volume re-locks."
                ),
            },
            {
                "id": "b",
                "text": "Immediately power down the system to preserve the state of the encrypted disk exactly as found",
                "correct": False,
                "rationale": (
                    "Incorrect. Powering down would re-lock the encrypted volume and likely make the data "
                    "permanently inaccessible without the key, destroying the only opportunity to capture it from "
                    "memory."
                ),
            },
            {
                "id": "c",
                "text": "Remove the drive and send it directly to the manufacturer for decryption assistance",
                "correct": False,
                "rationale": (
                    "Incorrect. Manufacturers generally cannot decrypt properly implemented full-disk encryption "
                    "without the key, and this wastes the critical window during which the key could be captured "
                    "from live memory."
                ),
            },
            {
                "id": "d",
                "text": "Log into the system's cloud backup portal to download an unencrypted copy of the files",
                "correct": False,
                "rationale": (
                    "Incorrect. This assumes an unencrypted cloud backup exists, which is not stated, and is not "
                    "the standard forensically sound first step; it also risks altering account access logs "
                    "relevant to the investigation."
                ),
            },
        ],
        "explanation": (
            "Order-of-volatility principles extend to full-disk encryption: keying material held only in RAM "
            "while a volume is mounted must be captured live, before any shutdown, or the encrypted data may "
            "become permanently unrecoverable."
        ),
    },
    {
        "id": "nd4b-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "Litigation is anticipated against the organization, and legal counsel issues a formal notice "
            "requiring that all emails, chat logs, and files related to a terminated executive be preserved. The "
            "company's standard data retention policy would normally auto-delete this data in 30 days. What "
            "should the security and IT teams do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Implement a legal hold that suspends the routine retention/deletion policy for the specified data, preserving it in its current state until counsel releases the hold",
                "correct": True,
                "rationale": (
                    "Correct. A legal hold overrides routine retention schedules once litigation is reasonably "
                    "anticipated, preserving all potentially relevant data until counsel determines it can be "
                    "released."
                ),
            },
            {
                "id": "b",
                "text": "Continue following the standard 30-day retention policy since it was established before the litigation notice was issued",
                "correct": False,
                "rationale": (
                    "Incorrect. Allowing routine deletion to proceed after a legal hold notice can result in "
                    "spoliation of evidence and legal sanctions; the hold must override the standard schedule."
                ),
            },
            {
                "id": "c",
                "text": "Immediately migrate the data to a separate encrypted archive and delete the original copies to save storage",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting originals — even after copying — before the hold is released risks "
                    "spoliation and can undermine the authenticity/chain of the preserved data."
                ),
            },
            {
                "id": "d",
                "text": "Forward the notice to the terminated executive so they can review and redact any personal information first",
                "correct": False,
                "rationale": (
                    "Incorrect. Giving the subject of a potential legal action control over what is preserved or "
                    "redacted could itself constitute spoliation or tampering with evidence."
                ),
            },
        ],
        "explanation": (
            "A legal hold is a formal instruction to suspend routine deletion/retention policies for data that "
            "may be relevant to anticipated or ongoing litigation, ensuring evidence is preserved intact until "
            "released by counsel."
        ),
    },
    {
        "id": "nd4b-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "While preparing evidence for trial, a paralegal notices that the serial number recorded on the "
            "evidence tag for a seized hard drive does not match the serial number visible on the physical drive "
            "photographed at the scene. What is the MOST appropriate action for the evidence custodian to take?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Document the discrepancy in detail, notify the case lead/legal counsel immediately, and investigate the handling records to determine the cause before the evidence is used further",
                "correct": True,
                "rationale": (
                    "Correct. Transparent documentation and immediate escalation of any discrepancy preserves the "
                    "integrity of the process and allows the cause to be investigated rather than concealed."
                ),
            },
            {
                "id": "b",
                "text": "Correct the tag to match the drive's actual serial number and continue using the evidence without further note, since it is clearly a simple clerical error",
                "correct": False,
                "rationale": (
                    "Incorrect. Silently altering evidence documentation after the fact — even to 'fix' an "
                    "apparent typo — creates the appearance of tampering and further undermines the defensibility "
                    "of the chain of custody."
                ),
            },
            {
                "id": "c",
                "text": "Discard the evidence tag and generate a brand-new chain-of-custody form starting from the current date",
                "correct": False,
                "rationale": (
                    "Incorrect. Discarding original documentation destroys the historical record needed to "
                    "explain the discrepancy, creating an unexplained gap far worse than the original error."
                ),
            },
            {
                "id": "d",
                "text": "Proceed with presenting the evidence in court without mentioning the discrepancy, since the drive's contents were not altered",
                "correct": False,
                "rationale": (
                    "Incorrect. Failing to disclose a known documentation/integrity issue can be far more "
                    "damaging if discovered later by opposing counsel, and may constitute withholding material "
                    "information."
                ),
            },
        ],
        "explanation": (
            "Chain-of-custody integrity depends on transparent, immediate documentation of any discrepancy, "
            "followed by investigation and disclosure — never silent correction, destruction of records, or "
            "concealment."
        ),
    },
    {
        "id": "nd4b-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "Which set of information MUST be captured on a chain-of-custody form each time evidence changes "
            "hands during an investigation, to preserve its integrity for legal proceedings?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The identity of the individual releasing and receiving the evidence, the date and time of transfer, and the purpose/reason for the transfer",
                "correct": True,
                "rationale": (
                    "Correct. A complete, unbroken record of who transferred custody to whom, when, and why is "
                    "required to prove the evidence was continuously accounted for and not tampered with."
                ),
            },
            {
                "id": "b",
                "text": "Only the final destination where the evidence will be permanently stored",
                "correct": False,
                "rationale": (
                    "Incorrect. Recording only the end destination omits the intermediate custodians and "
                    "timestamps needed to prove an unbroken chain of possession."
                ),
            },
            {
                "id": "c",
                "text": "The make and model of the evidence bag manufacturer used to package the item",
                "correct": False,
                "rationale": (
                    "Incorrect. Packaging vendor information does not establish custodial accountability; the "
                    "identity, date, and purpose of each transfer does."
                ),
            },
            {
                "id": "d",
                "text": "The personal opinion of each custodian regarding the likely guilt of the suspect",
                "correct": False,
                "rationale": (
                    "Incorrect. Subjective opinions have no place on a chain-of-custody form and would be "
                    "irrelevant, and potentially prejudicial, to include."
                ),
            },
        ],
        "explanation": (
            "A defensible chain of custody requires documenting every transfer of possession — who released it, "
            "who received it, when, and why — with no gaps, so the unbroken accountability of the evidence can "
            "be proven in legal proceedings."
        ),
    },
    {
        "id": "nd4b-012",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A DLP policy blocks HR from emailing a spreadsheet containing employee Social Security numbers to "
            "the company's own outsourced payroll processor, an approved and contractually vetted third party. "
            "HR complains that legitimate business operations are now impossible. What is the BEST way to resolve "
            "this without weakening the organization's overall data protection posture?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Create a scoped exception/allow rule in the DLP policy that permits SSN-pattern data only when the destination is the approved, contracted payroll processor's verified domain",
                "correct": True,
                "rationale": (
                    "Correct. A scoped, verified-destination exception permits the legitimate business flow while "
                    "keeping the block in place for all other destinations, preserving the overall control."
                ),
            },
            {
                "id": "b",
                "text": "Disable the SSN-pattern detection rule across the entire DLP policy so HR emails are never blocked again",
                "correct": False,
                "rationale": (
                    "Incorrect. This removes protection against SSNs leaving the organization to any destination, "
                    "dramatically increasing data loss risk far beyond the one legitimate use case."
                ),
            },
            {
                "id": "c",
                "text": "Instruct HR to convert the spreadsheet to a PDF before sending, since DLP only inspects spreadsheet file formats",
                "correct": False,
                "rationale": (
                    "Incorrect. This relies on evading the control through a file-format trick rather than fixing "
                    "the policy; a properly implemented DLP solution inspects content regardless of container "
                    "format."
                ),
            },
            {
                "id": "d",
                "text": "Grant HR staff local administrator rights on their workstations so the DLP agent can be temporarily disabled when needed",
                "correct": False,
                "rationale": (
                    "Incorrect. Granting broad administrative rights to bypass a security control on demand "
                    "creates a serious, unaudited security risk rather than a scoped, controlled solution."
                ),
            },
        ],
        "explanation": (
            "The correct remediation for a DLP false positive against a legitimate, approved business process is "
            "a narrowly scoped exception tied to the verified destination — not disabling the detection rule "
            "entirely, evading it through format tricks, or granting excessive local privileges."
        ),
    },
    {
        "id": "nd4b-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "Select TWO statements that accurately describe the difference in capability between endpoint "
            "detection and response (EDR) and extended detection and response (XDR)."
        ),
        "options": [
            {
                "id": "a",
                "text": "EDR's visibility and response actions (e.g., process termination, host isolation) are scoped to the endpoints on which its agent is installed.",
                "correct": True,
                "rationale": (
                    "Correct. EDR operates and acts at the endpoint level, limited to hosts running its agent."
                ),
            },
            {
                "id": "b",
                "text": "XDR correlates telemetry from multiple sources — such as endpoint, email, network, and identity — to detect multi-stage attacks that no single data source would reveal on its own.",
                "correct": True,
                "rationale": (
                    "Correct. XDR's defining capability is cross-domain telemetry correlation, extending beyond a "
                    "single tool's visibility."
                ),
            },
            {
                "id": "c",
                "text": "EDR agents are incapable of isolating a host from the network under any circumstance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Host isolation/quarantine is one of EDR's standard containment actions, "
                    "contradicting this statement."
                ),
            },
            {
                "id": "d",
                "text": "XDR is limited to analyzing network traffic only and cannot incorporate endpoint or identity telemetry.",
                "correct": False,
                "rationale": (
                    "Incorrect. This understates XDR, which is specifically defined by ingesting and correlating "
                    "multiple telemetry types, including endpoint and identity data, not network traffic alone."
                ),
            },
        ],
        "explanation": (
            "EDR provides deep, agent-based visibility and response scoped to individual endpoints, while XDR "
            "extends detection by correlating telemetry across endpoint, email, network, and identity domains to "
            "reveal multi-stage attacks a single tool would miss."
        ),
    },
    {
        "id": "nd4b-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A user configures their corporate mailbox to auto-forward all incoming mail to a personal Gmail "
            "account. Legitimate newsletters that previously passed SPF and DMARC at the corporate mailbox begin "
            "arriving in the user's Gmail spam folder, even though the messages were not altered in transit. "
            "What is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forwarding changes the connecting/sending IP address seen by Gmail, causing SPF to fail because the forwarding server is not an authorized sender in the original domain's SPF record, and DMARC alignment can fail if DKIM does not also validate",
                "correct": True,
                "rationale": (
                    "Correct. SPF validates the connecting server's IP; forwarding through a different server "
                    "breaks that check, and DMARC requires alignment of a passing, aligned mechanism — if DKIM "
                    "also fails to validate through the forwarding path, DMARC fails as well."
                ),
            },
            {
                "id": "b",
                "text": "DKIM signatures are invalidated by any mail forwarding, while SPF always passes regardless of the forwarding path",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the actual behavior — DKIM's cryptographic signature typically "
                    "survives unmodified forwarding, whereas SPF is IP-based and commonly breaks when forwarded "
                    "through a different server."
                ),
            },
            {
                "id": "c",
                "text": "Gmail does not support SPF or DKIM validation at all, so all forwarded mail is automatically treated as spam",
                "correct": False,
                "rationale": (
                    "Incorrect. Gmail does evaluate SPF, DKIM, and DMARC; the issue is forwarding-induced SPF/"
                    "alignment failure, not a lack of support for these mechanisms."
                ),
            },
            {
                "id": "d",
                "text": "The newsletter sender's domain does not have an MX record configured",
                "correct": False,
                "rationale": (
                    "Incorrect. A missing MX record would prevent mail delivery entirely, not cause spam-folder "
                    "placement of successfully delivered messages."
                ),
            },
        ],
        "explanation": (
            "Auto-forwarding is a classic cause of SPF failure because the forwarding server's IP is not "
            "authorized in the sender's SPF record. DKIM's signature is more resilient to forwarding since it "
            "does not depend on the connecting IP, but if it also fails to validate, DMARC alignment fails and "
            "the message may be treated as spam."
        ),
    },
    {
        "id": "nd4b-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A marketing platform sends email on behalf of 'promo.marketingtool.com' but sets the visible "
            "'From:' header to 'news@company.com'. The DKIM signature validates successfully and is signed with "
            "'d=marketingtool.com'. DMARC is configured in strict alignment mode for company.com. What is the "
            "MOST likely outcome, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DMARC will fail because strict DKIM alignment requires the DKIM signing domain (d=) to exactly match the visible From: domain (company.com), and 'marketingtool.com' does not match",
                "correct": True,
                "rationale": (
                    "Correct. Strict alignment requires an exact domain match between the authenticated (d=) "
                    "domain and the visible From: domain; a mismatch causes DMARC to fail even though the raw "
                    "DKIM signature itself validates."
                ),
            },
            {
                "id": "b",
                "text": "DMARC will pass because DKIM validated successfully, and DMARC only requires that at least one authentication mechanism succeed regardless of domain alignment",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC additionally requires alignment between the authenticated domain and the "
                    "From: header domain, not merely a successful raw DKIM or SPF check."
                ),
            },
            {
                "id": "c",
                "text": "DMARC will pass because SPF is the only mechanism DMARC evaluates when DKIM is present",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC can rely on either SPF or DKIM alignment passing; this option incorrectly "
                    "claims SPF is the sole mechanism evaluated whenever DKIM exists, which is not how DMARC "
                    "works."
                ),
            },
            {
                "id": "d",
                "text": "DMARC does not apply to messages sent through third-party marketing platforms",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC applies to any mail claiming the protected From: domain, regardless of the "
                    "underlying sending platform, which is exactly why proper alignment configuration matters for "
                    "outsourced senders."
                ),
            },
        ],
        "explanation": (
            "DMARC alignment can be configured as strict or relaxed. Strict mode requires the DKIM d= domain (or "
            "SPF-validated domain) to exactly match the visible From: domain. A third-party sender using its own "
            "signing domain will fail strict alignment even with a technically valid DKIM signature, unless "
            "relaxed alignment or proper domain configuration is used."
        ),
    },
    {
        "id": "nd4b-016",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "An organization federates authentication for over 50 SaaS applications to a single cloud identity "
            "provider (IdP) using SSO. Which risk is introduced SPECIFICALLY by this architecture that would not "
            "exist if each application maintained its own separate authentication?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A compromise of the IdP could grant an attacker federated access to all 50 connected applications through a single point of failure",
                "correct": True,
                "rationale": (
                    "Correct. Centralizing authentication concentrates risk: a single successful compromise of "
                    "the IdP can cascade into access across every federated application at once."
                ),
            },
            {
                "id": "b",
                "text": "Users will be required to memorize 50 separate, unique passwords, increasing password reuse",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the opposite outcome; SSO/federation reduces the number of "
                    "credentials a user must manage, it does not increase it."
                ),
            },
            {
                "id": "c",
                "text": "Each SaaS application must independently store and hash the user's password, increasing the attack surface for credential theft",
                "correct": False,
                "rationale": (
                    "Incorrect. Under federation, the SaaS applications specifically do NOT store the user's "
                    "password; that is a benefit of the SSO model, not a new risk it introduces."
                ),
            },
            {
                "id": "d",
                "text": "Federation eliminates the need for multifactor authentication on any connected application",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation does not eliminate the need for MFA; enforcing MFA at the IdP is a key "
                    "mitigation for the single-point-of-failure risk, not something federation removes."
                ),
            },
        ],
        "explanation": (
            "Federating authentication to a single IdP concentrates trust: compromising the IdP can cascade into "
            "unauthorized access across every connected application. Strong IdP protections (MFA, monitoring, "
            "conditional access) are essential mitigations for this concentrated risk."
        ),
    },
    {
        "id": "nd4b-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "Select TWO true statements about the relationship between OAuth 2.0 and OpenID Connect (OIDC)."
        ),
        "options": [
            {
                "id": "a",
                "text": "OAuth 2.0 is fundamentally an authorization framework (granting scoped access to resources), while OIDC is an identity/authentication layer built on top of OAuth 2.0.",
                "correct": True,
                "rationale": (
                    "Correct. OAuth 2.0 governs delegated authorization; OIDC extends it specifically to add "
                    "standardized user authentication."
                ),
            },
            {
                "id": "b",
                "text": "OIDC introduces an ID token (typically a signed JWT) that conveys the authenticated user's identity, which is not part of the base OAuth 2.0 authorization specification.",
                "correct": True,
                "rationale": (
                    "Correct. The ID token is OIDC's key addition, providing a standardized way to assert user "
                    "identity that base OAuth 2.0 does not define."
                ),
            },
            {
                "id": "c",
                "text": "OAuth 2.0 by itself was designed primarily to authenticate a user's identity to a relying party, identical in purpose to OIDC.",
                "correct": False,
                "rationale": (
                    "Incorrect. Base OAuth 2.0 is about delegated authorization (access tokens/scopes), not "
                    "asserting user identity; that authentication capability is what OIDC specifically adds."
                ),
            },
            {
                "id": "d",
                "text": "OIDC and SAML are the same protocol using different names for identical XML-based assertions.",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML uses XML assertions, while OIDC uses JSON-based ID tokens (JWTs) built on "
                    "OAuth 2.0; they are different protocols with different message formats."
                ),
            },
        ],
        "explanation": (
            "OAuth 2.0 provides delegated, scoped authorization; OIDC layers standardized authentication "
            "(identity assertions via a signed ID token) on top of OAuth 2.0. This differs fundamentally from "
            "SAML's XML-based assertion model."
        ),
    },
    {
        "id": "nd4b-018",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A newly unboxed small-office router is placed into production with its default configuration, which "
            "includes remote administration enabled from the WAN interface, UPnP enabled, and an unused FTP "
            "service running. A security review flags this as high risk before a single vulnerability scan is "
            "even run. Which hardening principle does this finding illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reducing the attack surface by disabling unnecessary services, ports, and remote-management features not required for the device's actual function",
                "correct": True,
                "rationale": (
                    "Correct. Disabling unused services and remote-management features that are not needed "
                    "directly shrinks the number of exposed entry points an attacker could exploit."
                ),
            },
            {
                "id": "b",
                "text": "Enforcing strong password complexity requirements on the router's administrative account",
                "correct": False,
                "rationale": (
                    "Incorrect. While important, this does not address the finding, which is specifically about "
                    "unnecessary enabled services/features, not password strength."
                ),
            },
            {
                "id": "c",
                "text": "Applying the latest firmware patch released by the manufacturer",
                "correct": False,
                "rationale": (
                    "Incorrect. Patching addresses known vulnerabilities in existing enabled features; it does "
                    "not address the separate issue of unnecessary services being enabled by default in the "
                    "first place."
                ),
            },
            {
                "id": "d",
                "text": "Segmenting the router onto its own dedicated VLAN",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation limits blast radius from a network architecture perspective but does "
                    "not reduce the number of unnecessary services and open management interfaces running on the "
                    "device itself."
                ),
            },
        ],
        "explanation": (
            "Hardening starts with reducing the attack surface: disabling unnecessary services, closing unused "
            "ports, and turning off unneeded remote-management features by default, independent of patching or "
            "network segmentation."
        ),
    },
    {
        "id": "nd4b-019",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A manufacturing environment with legacy, rarely updated industrial workstations wants to prevent "
            "any unauthorized or unknown executable from running, even malware variants signature-based "
            "antivirus has never seen before. Which hardening control BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Application allowlisting, which permits only explicitly approved executables to run and blocks everything else by default",
                "correct": True,
                "rationale": (
                    "Correct. Allowlisting blocks any executable not explicitly approved, including novel or "
                    "previously unseen malware, regardless of whether a signature exists for it."
                ),
            },
            {
                "id": "b",
                "text": "Signature-based antivirus with daily definition updates",
                "correct": False,
                "rationale": (
                    "Incorrect. Signature-based detection can only block known threats matching existing "
                    "signatures and would miss novel or unseen malware variants, which is exactly the gap in the "
                    "scenario."
                ),
            },
            {
                "id": "c",
                "text": "Host-based firewall rules restricting inbound network connections",
                "correct": False,
                "rationale": (
                    "Incorrect. A host firewall controls network traffic, not which local executables are "
                    "permitted to run on the system."
                ),
            },
            {
                "id": "d",
                "text": "Full-disk encryption on all workstation drives",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption protects data confidentiality at rest; it has no effect on which "
                    "programs are permitted to execute."
                ),
            },
        ],
        "explanation": (
            "Application allowlisting (a default-deny approach to executables) is uniquely suited to legacy, "
            "rarely updated systems because it blocks anything not explicitly approved, closing the gap left by "
            "signature-based antivirus against unknown/novel malware."
        ),
    },
    {
        "id": "nd4b-020",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A SOC analyst receives an automated alert suggesting a workstation may be compromised, based on a "
            "single unusual DNS query to a domain with a low reputation score. Before taking any containment "
            "action such as isolating the host, what should the analyst do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Validate and scope the alert — correlate additional evidence (endpoint telemetry, process activity, other connections) to confirm whether this is a true positive and determine the extent of any compromise",
                "correct": True,
                "rationale": (
                    "Correct. Detection and analysis, including validation and scoping, should generally precede "
                    "containment for a single low-confidence indicator, ensuring the response is proportionate "
                    "and accurately targeted."
                ),
            },
            {
                "id": "b",
                "text": "Immediately isolate the workstation from the network to guarantee no further damage can occur",
                "correct": False,
                "rationale": (
                    "Incorrect. Isolating before validating risks unnecessary business disruption from a false "
                    "positive and skips the analysis needed to properly scope the incident, given only a single "
                    "low-confidence indicator."
                ),
            },
            {
                "id": "c",
                "text": "Notify executive leadership and prepare a public statement",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a late-stage communication action taken only after an incident is "
                    "confirmed and formally declared, not a first response to a single low-confidence alert."
                ),
            },
            {
                "id": "d",
                "text": "Wipe and reimage the workstation to eliminate any possible threat",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging is an eradication/recovery action that would destroy volatile evidence "
                    "needed to determine scope and root cause, and is premature before the alert is even "
                    "validated."
                ),
            },
        ],
        "explanation": (
            "The IR lifecycle's detection and analysis phase — validating and scoping an alert — should "
            "generally precede disruptive containment actions for a single, low-confidence indicator, to avoid "
            "unnecessary business impact from a false positive while still preserving the ability to act quickly "
            "if the alert is confirmed."
        ),
    },
    {
        "id": "nd4b-021",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During a ransomware incident, the IR team is unsure whether the incident meets the threshold "
            "requiring notification of the board of directors, legal counsel, and the cyber-insurance carrier, "
            "causing delays during a stressful moment. Which pre-incident artifact, if properly developed and "
            "maintained, would have prevented this confusion?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A documented incident response communication plan defining escalation thresholds, notification triggers, and stakeholder contact responsibilities for different incident severities",
                "correct": True,
                "rationale": (
                    "Correct. A communication plan established during the preparation phase defines exactly who "
                    "must be notified, under what severity thresholds, and by whom, removing ambiguity during a "
                    "live incident."
                ),
            },
            {
                "id": "b",
                "text": "A more detailed network topology diagram of the affected segment",
                "correct": False,
                "rationale": (
                    "Incorrect. A topology diagram helps with technical containment and scoping, not with "
                    "defining who must be notified and under what conditions."
                ),
            },
            {
                "id": "c",
                "text": "An updated business continuity plan (BCP) test schedule",
                "correct": False,
                "rationale": (
                    "Incorrect. A BCP test schedule addresses when continuity exercises occur; it does not define "
                    "incident notification thresholds or escalation contacts."
                ),
            },
            {
                "id": "d",
                "text": "A vulnerability scan report from the previous quarter",
                "correct": False,
                "rationale": (
                    "Incorrect. A vulnerability report describes technical weaknesses found in an assessment; it "
                    "has no bearing on organizational communication/escalation procedures during an active "
                    "incident."
                ),
            },
        ],
        "explanation": (
            "A documented communication plan, prepared before an incident occurs, defines escalation thresholds "
            "and stakeholder responsibilities so the IR team is not left guessing who to notify and when during "
            "an active, high-pressure incident."
        ),
    },
    {
        "id": "nd4b-022",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst suspects an attacker is performing a password-spraying attack against multiple domain "
            "user accounts using a single low, evenly distributed number of attempts per account to avoid "
            "lockout thresholds. Which log source, correlated across accounts, would BEST reveal this pattern?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Domain controller authentication logs recording failed logon events aggregated across many different user accounts from the same source, over a short time window",
                "correct": True,
                "rationale": (
                    "Correct. Password spraying is identified by correlating failed authentication events across "
                    "many accounts from a common source, which domain controller authentication logs directly "
                    "capture."
                ),
            },
            {
                "id": "b",
                "text": "Local workstation application event logs showing software installation activity",
                "correct": False,
                "rationale": (
                    "Incorrect. Application installation logs have no relevance to authentication attempts "
                    "against domain accounts."
                ),
            },
            {
                "id": "c",
                "text": "Print spooler logs on the file server",
                "correct": False,
                "rationale": (
                    "Incorrect. Printing activity logs are unrelated to authentication events and would not "
                    "reveal a password-spraying pattern."
                ),
            },
            {
                "id": "d",
                "text": "Endpoint antivirus quarantine logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine logs record detected malware samples, not authentication failure "
                    "patterns across multiple accounts."
                ),
            },
        ],
        "explanation": (
            "Password spraying is designed to stay under per-account lockout thresholds, so it is only visible "
            "by correlating low-volume failed logon events across many different accounts from a common source, "
            "which domain controller authentication logs capture."
        ),
    },
    {
        "id": "nd4b-023",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "Firewall and NetFlow records confirm that a large volume of data left the network to an external IP "
            "address, but investigators need to determine the EXACT file names and content that were "
            "transmitted, not just the connection metadata (source/destination/bytes transferred). Which "
            "additional log/data source is required to answer this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Full packet capture (PCAP) collected on the relevant network segment at the time of the transfer, which records the actual payload content of the session",
                "correct": True,
                "rationale": (
                    "Correct. Only full packet capture retains the actual transmitted payload/content, which is "
                    "required to identify the exact files and data exfiltrated."
                ),
            },
            {
                "id": "b",
                "text": "NetFlow records alone, since they already contain byte counts for the session",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow records summarize connection metadata (source/destination, ports, byte/"
                    "packet counts) but do not capture the actual payload/content transmitted."
                ),
            },
            {
                "id": "c",
                "text": "DHCP lease logs showing which device held the source IP address at the time",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs help attribute an IP to a device but contain no information about the "
                    "content of the data transferred."
                ),
            },
            {
                "id": "d",
                "text": "Firewall logs showing only allow/deny actions for the connection",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs typically confirm that a connection was permitted or blocked, not "
                    "the specific payload contents exchanged during that session."
                ),
            },
        ],
        "explanation": (
            "NetFlow, DHCP, and firewall logs all provide valuable metadata, but only full packet capture "
            "retains the actual content/payload of network sessions, which is required to determine precisely "
            "what data was exfiltrated."
        ),
    },
    {
        "id": "nd4b-024",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "Investigators find that a compromised executive's laptop has a hidden program that gives a remote "
            "attacker full interactive control of the desktop — including moving the mouse, opening "
            "applications, and exfiltrating files on demand — all while displaying a legitimate-looking icon "
            "disguised as a PDF reader update. Which malware classification BEST fits this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A remote access trojan (RAT), delivered disguised as legitimate software, providing the attacker full remote interactive control of the host",
                "correct": True,
                "rationale": (
                    "Correct. Disguised delivery combined with full, real-time interactive remote control is the "
                    "defining behavior of a RAT."
                ),
            },
            {
                "id": "b",
                "text": "A keylogger, which passively records keystrokes for later retrieval",
                "correct": False,
                "rationale": (
                    "Incorrect. A keylogger's function is limited to capturing keystroke input; it does not "
                    "provide full interactive remote-control capability like moving the mouse or launching "
                    "applications on demand."
                ),
            },
            {
                "id": "c",
                "text": "Adware, which displays unwanted advertisements to generate revenue",
                "correct": False,
                "rationale": (
                    "Incorrect. Adware's purpose is to serve advertisements, not to hand an attacker full "
                    "real-time interactive control of the compromised system."
                ),
            },
            {
                "id": "d",
                "text": "A boot sector virus, which infects the master boot record to execute before the OS loads",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario indicates boot-record infection; the described behavior "
                    "is real-time interactive remote control, characteristic of a RAT, not a boot sector virus."
                ),
            },
        ],
        "explanation": (
            "A remote access trojan (RAT) is defined by disguised delivery (trojan) combined with the ability to "
            "grant an attacker full, real-time interactive control of the compromised host, distinguishing it "
            "from passive keyloggers, revenue-driven adware, or boot-record infectors."
        ),
    },
    {
        "id": "nd4b-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "Select TWO true statements that correctly distinguish a computer virus from a worm."
        ),
        "options": [
            {
                "id": "a",
                "text": "A virus requires a host file or program and typically needs some form of user action (e.g., opening an infected attachment) to execute and spread.",
                "correct": True,
                "rationale": (
                    "Correct. Viruses attach to a host file and generally rely on user action to trigger "
                    "execution and propagation."
                ),
            },
            {
                "id": "b",
                "text": "A worm is self-contained and can self-propagate across a network by exploiting a vulnerability, without requiring a host file or user interaction.",
                "correct": True,
                "rationale": (
                    "Correct. Worms are standalone programs that spread autonomously by exploiting vulnerabilities, "
                    "without needing a host file or a user to trigger execution."
                ),
            },
            {
                "id": "c",
                "text": "A virus can always self-propagate across a network without any user interaction, identical to a worm.",
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the key distinguishing feature; a virus's dependence on a host "
                    "and typically on user action is what differentiates it from a worm."
                ),
            },
            {
                "id": "d",
                "text": "A worm requires infecting an existing legitimate file in order to execute, just like a virus.",
                "correct": False,
                "rationale": (
                    "Incorrect. Worms are self-contained programs and do not need to attach to or infect an "
                    "existing host file the way a virus does."
                ),
            },
        ],
        "explanation": (
            "The classic distinction: a virus needs a host file and typically user action to spread, while a "
            "worm is self-contained and self-propagates autonomously across a network by exploiting a "
            "vulnerability, with no user interaction required."
        ),
    },
    {
        "id": "nd4b-026",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A company's MDM solution continuously checks enrolled devices for jailbreak or root status. When a "
            "device is detected as jailbroken, the MDM automatically revokes the device's certificate used for "
            "corporate Wi-Fi and VPN authentication and blocks access to corporate email. Which security "
            "principle does this configuration MOST directly enforce?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Conditional access based on device compliance/posture — corporate resource access is contingent on the device remaining in a trusted, unmodified state",
                "correct": True,
                "rationale": (
                    "Correct. Access to corporate resources is being made conditional on the device's compliance "
                    "state (not jailbroken), which is precisely the definition of posture-based conditional "
                    "access."
                ),
            },
            {
                "id": "b",
                "text": "Data loss prevention (DLP) content inspection",
                "correct": False,
                "rationale": (
                    "Incorrect. DLP inspects data content for sensitive patterns; this scenario is about device "
                    "integrity/jailbreak status, not content inspection."
                ),
            },
            {
                "id": "c",
                "text": "Full-device encryption enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes revoking access based on jailbreak detection, not "
                    "enforcing or verifying disk encryption specifically."
                ),
            },
            {
                "id": "d",
                "text": "Geofencing-based access restriction",
                "correct": False,
                "rationale": (
                    "Incorrect. Geofencing restricts access based on physical location; this scenario's trigger "
                    "is jailbreak/root status, not location."
                ),
            },
        ],
        "explanation": (
            "Conditional access ties corporate resource availability to a device's ongoing compliance/posture "
            "state. Detecting jailbreak/root status and automatically revoking access is a direct application of "
            "this principle in MDM."
        ),
    },
    {
        "id": "nd4b-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A hospital's MDM policy allows a specialized clinical application containing patient data to "
            "function only while the device's GPS location places it within the hospital campus boundary; the "
            "app automatically locks and hides patient data if the device leaves that boundary. Which MDM "
            "capability is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Geofencing",
                "correct": True,
                "rationale": (
                    "Correct. Geofencing restricts application functionality/access based on a defined physical "
                    "location boundary, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Containerization",
                "correct": False,
                "rationale": (
                    "Incorrect. Containerization separates corporate and personal data/apps into an isolated "
                    "profile; it does not by itself restrict app functionality based on physical location."
                ),
            },
            {
                "id": "c",
                "text": "Remote wipe",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote wipe erases data upon an administrator's command or a triggering condition "
                    "like repeated failed passcode attempts; it is not the mechanism that locks/hides data based "
                    "on real-time GPS boundary crossing described here."
                ),
            },
            {
                "id": "d",
                "text": "Certificate-based device authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate authentication verifies the device's identity for network/resource "
                    "access; it does not restrict application functionality based on GPS location."
                ),
            },
        ],
        "explanation": (
            "Geofencing uses location data (e.g., GPS) to enable or restrict application/data access based on "
            "whether a device is within a defined physical boundary, distinct from containerization, remote "
            "wipe, or certificate-based authentication."
        ),
    },
    {
        "id": "nd4b-028",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A financial services firm currently sends one-time passcodes to customers via SMS for account login "
            "verification. After several customers report unauthorized account access despite never revealing "
            "their OTP, investigators determine attackers fraudulently convinced the customers' mobile carriers "
            "to port their phone numbers to attacker-controlled SIM cards. Which mitigation would BEST address "
            "this specific attack vector?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace SMS-based OTP with a time-based one-time password (TOTP) authenticator app or a phishing-resistant hardware security key, neither of which depends on the carrier's SIM/phone number",
                "correct": True,
                "rationale": (
                    "Correct. Because the attack exploits the carrier's control over the phone number (SIM "
                    "swapping), moving to an authentication method not tied to the phone number/carrier removes "
                    "the exploited channel entirely."
                ),
            },
            {
                "id": "b",
                "text": "Increase the length of the SMS OTP code from 6 digits to 10 digits",
                "correct": False,
                "rationale": (
                    "Incorrect. A longer code does nothing to prevent the attacker from receiving the SMS in the "
                    "first place once the phone number itself has been fraudulently ported to their SIM."
                ),
            },
            {
                "id": "c",
                "text": "Require customers to change their account password every 30 days",
                "correct": False,
                "rationale": (
                    "Incorrect. Frequent password rotation does not address the underlying issue, which is that "
                    "the SMS delivery channel itself has been hijacked via SIM swapping."
                ),
            },
            {
                "id": "d",
                "text": "Send the OTP via both SMS and email simultaneously to increase delivery reliability",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a second delivery channel does not remove the vulnerable SMS/SIM-based "
                    "channel and does not address the root cause of the SIM-swap compromise."
                ),
            },
        ],
        "explanation": (
            "SIM swapping compromises the SMS delivery channel itself by hijacking the victim's phone number. "
            "The correct mitigation is to move to an authentication factor that does not rely on the carrier or "
            "phone number at all, such as an authenticator app or a hardware security key."
        ),
    },
    {
        "id": "nd4b-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "Several executives fall victim to a phishing kit that proxies their login session in real time: it "
            "presents a fake but fully functional login page, relays the entered password and the six-digit MFA "
            "code to the real site instantly, and captures the resulting authenticated session cookie — "
            "completely bypassing traditional push-based and OTP-based MFA. Which authentication method would "
            "MOST effectively prevent this specific attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FIDO2/WebAuthn hardware security keys, which cryptographically bind the authentication response to the legitimate site's origin and cannot be relayed by a proxying phishing page",
                "correct": True,
                "rationale": (
                    "Correct. FIDO2/WebAuthn authentication is origin-bound; a credential generated for the real "
                    "site's domain cannot be replayed by an attacker's proxy site, defeating this adversary-in-"
                    "the-middle technique."
                ),
            },
            {
                "id": "b",
                "text": "Increasing the MFA push notification timeout from 30 seconds to 5 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. A longer timeout does not prevent a real-time relay attack; it may even give the "
                    "attacker more time to complete the relayed authentication."
                ),
            },
            {
                "id": "c",
                "text": "Switching from SMS OTP to a six-digit TOTP authenticator app code",
                "correct": False,
                "rationale": (
                    "Incorrect. TOTP codes, like SMS OTPs, can still be captured and relayed in real time by an "
                    "adversary-in-the-middle proxy; this does not solve the origin-binding problem."
                ),
            },
            {
                "id": "d",
                "text": "Requiring users to memorize a longer, more complex password in addition to the existing MFA code",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity does nothing to stop a real-time relay/proxy attack that "
                    "captures whatever credentials and codes the user enters, regardless of complexity."
                ),
            },
        ],
        "explanation": (
            "Adversary-in-the-middle phishing kits can relay any shared-secret-based factor (passwords, TOTP, "
            "SMS OTP, and even simple push approvals) in real time. Only origin-bound, phishing-resistant "
            "methods like FIDO2/WebAuthn hardware keys cryptographically prevent the credential from being used "
            "on a different (phishing) origin."
        ),
    },
    {
        "id": "nd4b-030",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "Before any technical testing begins, a penetration testing firm and the client jointly finalize a "
            "signed document that defines the authorized IP address ranges and applications in scope, testing "
            "time windows, permitted techniques, emergency contacts, and explicit exclusions such as "
            "denial-of-service testing. Which phase of the engagement does this activity represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Planning/pre-engagement, including scoping and negotiation of the rules of engagement",
                "correct": True,
                "rationale": (
                    "Correct. Formally defining scope, authorized targets, timing, permitted techniques, and "
                    "exclusions is the planning/pre-engagement phase, finalized before any technical testing "
                    "begins."
                ),
            },
            {
                "id": "b",
                "text": "Active reconnaissance",
                "correct": False,
                "rationale": (
                    "Incorrect. Active reconnaissance involves direct technical interaction with target systems "
                    "(e.g., port scanning), which occurs after scope and authorization are formally established, "
                    "not during the scoping/authorization step itself."
                ),
            },
            {
                "id": "c",
                "text": "Post-exploitation",
                "correct": False,
                "rationale": (
                    "Incorrect. Post-exploitation involves actions taken after a foothold has already been "
                    "gained, far later in the engagement than initial scoping."
                ),
            },
            {
                "id": "d",
                "text": "Reporting",
                "correct": False,
                "rationale": (
                    "Incorrect. Reporting occurs at the conclusion of the engagement after testing activity is "
                    "complete, not before it begins."
                ),
            },
        ],
        "explanation": (
            "Penetration testing begins with a planning/pre-engagement phase where scope, rules of engagement, "
            "authorized targets, and exclusions are formally agreed upon and signed before any reconnaissance or "
            "technical testing activity starts."
        ),
    },
    {
        "id": "nd4b-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "A penetration tester begins an engagement by reviewing employee LinkedIn profiles, company job "
            "postings that reveal technology stacks, public WHOIS registration records, and certificate "
            "transparency logs — without sending a single packet directly to the target's systems. Which "
            "activity is being performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Passive reconnaissance",
                "correct": True,
                "rationale": (
                    "Correct. Gathering publicly available information without directly interacting with the "
                    "target's systems is the definition of passive reconnaissance."
                ),
            },
            {
                "id": "b",
                "text": "Active reconnaissance",
                "correct": False,
                "rationale": (
                    "Incorrect. Active reconnaissance requires direct interaction with the target's systems (e.g., "
                    "port scans, banner grabbing), which contradicts the scenario's explicit statement that no "
                    "packets were sent to the target directly."
                ),
            },
            {
                "id": "c",
                "text": "Vulnerability exploitation",
                "correct": False,
                "rationale": (
                    "Incorrect. Exploitation involves actively leveraging a discovered weakness to gain access; "
                    "the scenario describes only open-source information gathering, well before any exploitation "
                    "attempt."
                ),
            },
            {
                "id": "d",
                "text": "Post-engagement cleanup",
                "correct": False,
                "rationale": (
                    "Incorrect. Cleanup occurs after testing concludes to remove tools/artifacts from "
                    "compromised systems; it has no relationship to the passive information-gathering activity "
                    "described at the outset of the engagement."
                ),
            },
        ],
        "explanation": (
            "Passive reconnaissance gathers information from publicly available sources (OSINT, WHOIS, "
            "certificate transparency logs, social media) without directly touching the target's systems, "
            "distinguishing it from active reconnaissance, exploitation, and post-engagement cleanup."
        ),
    },
    {
        "id": "nd4b-032",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A vulnerability scan of network switches finds that SNMP is enabled using SNMPv1 with the community "
            "strings left at the manufacturer defaults of 'public' (read-only) and 'private' (read-write), "
            "reachable from the general corporate VLAN over UDP port 161. What is the MOST appropriate "
            "remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Migrate to SNMPv3 with unique, strong authentication credentials and encryption, and restrict SNMP access to a dedicated management VLAN or authorized management hosts only",
                "correct": True,
                "rationale": (
                    "Correct. SNMPv3 provides authentication and encryption absent in v1/v2c, and restricting "
                    "reachability to a management network limits exposure even further."
                ),
            },
            {
                "id": "b",
                "text": "Change the community strings to 'public2' and 'private2' and leave SNMPv1 in use",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv1/v2c community strings are transmitted in cleartext and offer no real "
                    "authentication strength regardless of the string chosen; renaming them does not remediate "
                    "the fundamental weakness of the protocol version."
                ),
            },
            {
                "id": "c",
                "text": "Block all UDP traffic on the corporate VLAN to eliminate the risk",
                "correct": False,
                "rationale": (
                    "Incorrect. This is overly broad and would break other legitimate UDP-based services (e.g., "
                    "DNS, DHCP, NTP) rather than specifically addressing the SNMP misconfiguration."
                ),
            },
            {
                "id": "d",
                "text": "Disable SNMP entirely and rely solely on manual console-based device checks",
                "correct": False,
                "rationale": (
                    "Incorrect. While disabling SNMP would remove the immediate risk, it eliminates a valuable, "
                    "needed monitoring capability rather than remediating it properly; migrating to a secure, "
                    "authenticated version with restricted access preserves functionality while closing the "
                    "security gap."
                ),
            },
        ],
        "explanation": (
            "SNMPv1/v2c community strings are sent in cleartext and provide weak, easily guessed authentication. "
            "The proper remediation is migrating to SNMPv3 (which adds authentication and encryption) and "
            "restricting access to authorized management hosts/networks, not merely renaming strings, blocking "
            "all UDP, or abandoning monitoring altogether."
        ),
    },
    {
        "id": "nd4b-033",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An organization maintains a single 'break-glass' emergency administrator account for its identity "
            "provider, intended for use only if the primary MFA-enabled admin accounts and the SSO system become "
            "completely unavailable during a disaster. Which set of controls is MOST appropriate for this "
            "account under PAM best practices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Store the credential in a sealed, access-logged vault requiring dual approval to retrieve, force a password rotation immediately after each use, and generate a high-priority alert to the security team any time the account is accessed",
                "correct": True,
                "rationale": (
                    "Correct. Break-glass accounts require tight vaulting, dual control, mandatory rotation after "
                    "use, and immediate alerting so any access is both difficult to obtain improperly and "
                    "instantly visible to security staff."
                ),
            },
            {
                "id": "b",
                "text": "Set the account's password to never expire and share it via a printed note kept in the IT manager's desk drawer for quick access",
                "correct": False,
                "rationale": (
                    "Incorrect. A non-expiring, informally shared, unmonitored credential undermines "
                    "accountability and increases the risk of undetected misuse — the opposite of secure "
                    "break-glass handling."
                ),
            },
            {
                "id": "c",
                "text": "Disable logging on the account since it is only used in rare emergencies and logging would add unnecessary noise",
                "correct": False,
                "rationale": (
                    "Incorrect. Emergency accounts require MORE scrutiny and alerting when used, not less, given "
                    "how rarely and sensitively they should be invoked."
                ),
            },
            {
                "id": "d",
                "text": "Grant the account standing, unmonitored domain administrator rights at all times so it is always immediately ready for use",
                "correct": False,
                "rationale": (
                    "Incorrect. Standing, unmonitored elevated privilege for a rarely used account maximizes risk "
                    "exposure; break-glass accounts should be tightly vaulted and monitored, only becoming active "
                    "on documented, approved retrieval."
                ),
            },
        ],
        "explanation": (
            "Break-glass emergency accounts require the strongest PAM controls of any privileged credential: "
            "vaulting with dual approval to retrieve, mandatory post-use rotation, and immediate alerting on any "
            "access, since their use should be exceedingly rare and always scrutinized."
        ),
    },
    {
        "id": "nd4b-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An audit discovers that a scheduled backup task on 200 servers runs under a service account that "
            "has been granted domain administrator rights, even though the backup software only requires local "
            "file read access and the ability to write to a specific backup share. Which PAM-aligned remediation "
            "BEST addresses this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reconfigure the service account with only the minimum specific permissions needed for backup operations (local read access and write access to the designated share), removing domain administrator rights",
                "correct": True,
                "rationale": (
                    "Correct. Scoping the account to exactly what the backup function needs directly applies the "
                    "principle of least privilege, eliminating the unnecessary domain-wide exposure."
                ),
            },
            {
                "id": "b",
                "text": "Enable multifactor authentication on the service account before each scheduled backup job runs",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA is designed for interactive human logins and is generally impractical/"
                    "unsupported for unattended, automated service account logons; it does not address the "
                    "excessive privilege itself."
                ),
            },
            {
                "id": "c",
                "text": "Rotate the service account's password weekly instead of quarterly",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent rotation does not reduce the scope of what the account is "
                    "authorized to do; the core issue is excessive privilege, not password age."
                ),
            },
            {
                "id": "d",
                "text": "Rename the service account to obscure its purpose from potential attackers",
                "correct": False,
                "rationale": (
                    "Incorrect. Security through obscurity does not reduce the account's actual privilege level "
                    "or the risk it poses if compromised."
                ),
            },
        ],
        "explanation": (
            "Service accounts should be provisioned with only the minimum privileges their specific function "
            "requires. Granting domain administrator rights for a task that only needs local read/share write "
            "access violates least privilege and dramatically increases the impact if the account is ever "
            "compromised."
        ),
    },
    {
        "id": "nd4b-035",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM correlation rule flags that the same user account successfully authenticated from an IP "
            "address in Tokyo and, nine minutes later, from an IP address in Toronto — a physical distance that "
            "could not be traveled in that time. Which capability generated this specific type of detection?"
        ),
        "options": [
            {
                "id": "a",
                "text": "User and entity behavior analytics (UEBA)/impossible travel detection, which baselines normal user login patterns and flags physically implausible location changes",
                "correct": True,
                "rationale": (
                    "Correct. Impossible travel detection, a form of UEBA, specifically compares login "
                    "geolocation and timing against physically plausible travel to flag anomalies like this one."
                ),
            },
            {
                "id": "b",
                "text": "Signature-based intrusion detection matching a known exploit pattern",
                "correct": False,
                "rationale": (
                    "Incorrect. This detection is based on behavioral/contextual analysis of login geography and "
                    "timing, not matching a known attack signature."
                ),
            },
            {
                "id": "c",
                "text": "Data loss prevention (DLP) content inspection",
                "correct": False,
                "rationale": (
                    "Incorrect. DLP inspects data content for sensitive information leaving the organization; it "
                    "does not evaluate authentication geolocation timing."
                ),
            },
            {
                "id": "d",
                "text": "Vulnerability scanning results correlation",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scan data identifies weaknesses in systems, not real-time "
                    "authentication geolocation anomalies."
                ),
            },
        ],
        "explanation": (
            "Impossible travel detection, powered by user and entity behavior analytics, baselines expected "
            "login geography/timing per user and flags logins that are physically implausible given the time "
            "elapsed — a behavioral detection distinct from signature matching, DLP, or vulnerability scanning."
        ),
    },
    {
        "id": "nd4b-036",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM ingests logs from a Cisco firewall, a Palo Alto firewall, a Windows domain controller, and a "
            "Linux web server, each using different field names and timestamp formats for similar events (e.g., "
            "'src_ip' vs 'source-address' vs 'ClientIP'). Before meaningful cross-source correlation rules can be "
            "built, which process must occur?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Log normalization — mapping each source's disparate fields and formats into a common schema/taxonomy so equivalent data elements can be compared and correlated",
                "correct": True,
                "rationale": (
                    "Correct. Normalization reconciles differently named/formatted fields from multiple vendors "
                    "into a consistent schema, which is a prerequisite for accurate cross-source correlation."
                ),
            },
            {
                "id": "b",
                "text": "Log retention extension — increasing how long logs are stored",
                "correct": False,
                "rationale": (
                    "Incorrect. Retention duration is unrelated to whether differently formatted fields from "
                    "different vendors can be compared to each other."
                ),
            },
            {
                "id": "c",
                "text": "Alert deduplication — suppressing repeated identical alerts",
                "correct": False,
                "rationale": (
                    "Incorrect. Deduplication reduces redundant alert volume; it does not address the underlying "
                    "problem of inconsistent field names/formats across log sources."
                ),
            },
            {
                "id": "d",
                "text": "Log encryption at rest",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting stored logs protects confidentiality but does nothing to reconcile "
                    "differing field names/formats needed for correlation."
                ),
            },
        ],
        "explanation": (
            "Log normalization maps disparate vendor field names and formats into a common schema/taxonomy, "
            "which is required before a SIEM can reliably correlate equivalent data elements (like source IP) "
            "across heterogeneous log sources."
        ),
    },
    {
        "id": "nd4b-037",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "An uncredentialed external vulnerability scan of a server reports only a handful of low-severity "
            "findings. A subsequent credentialed scan using valid local administrator credentials on the same "
            "server reveals dozens of additional high-severity findings, including missing OS patches and "
            "insecure local configurations. What is the MOST likely explanation for this discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An uncredentialed scan can only assess what is visible from the network without authenticating to the host, missing local-only issues such as missing patches and misconfigurations that a credentialed scan can enumerate directly on the system",
                "correct": True,
                "rationale": (
                    "Correct. Credentialed scans authenticate to the host and can directly inspect patch levels "
                    "and local configuration, revealing far more than an uncredentialed, network-only scan can "
                    "see."
                ),
            },
            {
                "id": "b",
                "text": "The credentialed scan used a newer scanner version with a completely different vulnerability database",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario does not indicate a difference in scanner version/database; the "
                    "described difference in results is the well-known effect of scan authentication level "
                    "(credentialed vs. uncredentialed), not database currency."
                ),
            },
            {
                "id": "c",
                "text": "Credentialed scans always report false positives that should be disregarded in favor of uncredentialed results",
                "correct": False,
                "rationale": (
                    "Incorrect. Credentialed scans are generally considered MORE accurate and thorough because "
                    "they can inspect the system internally, not less reliable."
                ),
            },
            {
                "id": "d",
                "text": "The uncredentialed scan was blocked entirely by the host firewall and produced no valid results at all",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the uncredentialed scan did return some findings (a handful "
                    "of low-severity items), so it was not entirely blocked; the gap is explained by scan depth/"
                    "authentication, not a complete block."
                ),
            },
        ],
        "explanation": (
            "Credentialed scans authenticate to the target and can directly inspect patch status and local "
            "configuration, revealing vulnerabilities invisible to a purely network-based, uncredentialed scan. "
            "This is why credentialed scanning is recommended for accurate, comprehensive vulnerability "
            "assessment."
        ),
    },
    {
        "id": "nd4b-038",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A critical zero-day vulnerability is publicly disclosed in a widely used web application framework. "
            "The vendor states a patch will not be available for at least three weeks, and the affected "
            "application cannot be taken offline. Which compensating control would BEST reduce risk during the "
            "interim period?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy a virtual patch — a targeted intrusion prevention system (IPS) or WAF signature/rule that blocks known exploitation attempts for this specific vulnerability until the vendor's official patch is released",
                "correct": True,
                "rationale": (
                    "Correct. Virtual patching provides an immediate, targeted compensating control that blocks "
                    "known exploitation patterns for the specific flaw while the organization waits for the "
                    "vendor's permanent fix."
                ),
            },
            {
                "id": "b",
                "text": "Wait for the vendor's official patch before taking any action, since only the vendor's fix can be considered valid remediation",
                "correct": False,
                "rationale": (
                    "Incorrect. Passively waiting three weeks while a publicly disclosed, actively targetable "
                    "zero-day remains completely unmitigated leaves the organization needlessly exposed when "
                    "compensating controls are available."
                ),
            },
            {
                "id": "c",
                "text": "Increase the frequency of authenticated vulnerability scans against the application to twice daily",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning more frequently only confirms the vulnerability still exists; it does "
                    "not reduce the actual risk of exploitation during the exposure window."
                ),
            },
            {
                "id": "d",
                "text": "Document the finding in the risk register and revisit it at the next scheduled quarterly review",
                "correct": False,
                "rationale": (
                    "Incorrect. Given the vulnerability is a publicly disclosed, actively exploitable zero-day on "
                    "a system that cannot be taken offline, deferring action to a routine quarterly review is an "
                    "inappropriate, overly passive response to an urgent, known risk."
                ),
            },
        ],
        "explanation": (
            "When a vendor patch is not yet available for a critical, actively exploitable vulnerability, "
            "virtual patching through an IPS/WAF rule targeting the specific exploitation pattern is the "
            "standard compensating control to reduce risk during the exposure window."
        ),
    },
    {
        "id": "nd4b-039",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "An attacker within range of a corporate wireless network repeatedly sends forged deauthentication "
            "frames, causing legitimate clients to be continually disconnected and forced to reassociate, "
            "disrupting business operations. Which wireless security feature would BEST mitigate this specific "
            "attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.11w Management Frame Protection (PMF), which cryptographically protects management frames — including deauthentication and disassociation frames — from being forged by an unauthenticated attacker",
                "correct": True,
                "rationale": (
                    "Correct. PMF specifically protects management frames from forgery, directly preventing an "
                    "attacker from injecting fraudulent deauthentication frames against associated clients."
                ),
            },
            {
                "id": "b",
                "text": "WPA3-Personal's SAE handshake, which resists offline dictionary attacks against the passphrase",
                "correct": False,
                "rationale": (
                    "Incorrect. SAE strengthens the initial key-exchange/authentication process against offline "
                    "password guessing; it does not, by itself, protect already-associated clients' management "
                    "frames from being forged, which is what PMF specifically addresses."
                ),
            },
            {
                "id": "c",
                "text": "Disabling SSID broadcast so the network name is hidden from casual scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. Hiding the SSID does not prevent an attacker who can already see wireless traffic "
                    "from sending forged deauthentication frames targeting associated clients."
                ),
            },
            {
                "id": "d",
                "text": "Lowering the access point's transmit power to reduce its coverage area",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing range may shrink the area from which an attacker can operate but does "
                    "not cryptographically prevent forged management frames from disrupting clients within that "
                    "reduced range."
                ),
            },
        ],
        "explanation": (
            "Deauthentication flood attacks exploit the fact that 802.11 management frames are traditionally "
            "unauthenticated. 802.11w Management Frame Protection cryptographically protects these frames, "
            "directly closing the gap that this attack exploits — distinct from SAE (which protects the initial "
            "key exchange), SSID hiding, or transmit power adjustments."
        ),
    },
    {
        "id": "nd4b-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A wireless security assessment of a small branch office network successfully recovers the WPA2 "
            "passphrase within a few hours using a tool that systematically brute-forces the access point's "
            "8-digit WPS PIN, despite the passphrase itself being long and complex. Which finding and "
            "remediation are MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wi-Fi Protected Setup (WPS) PIN authentication has a design weakness that allows the 8-digit PIN to be brute-forced in a feasible time frame, ultimately exposing the WPA2 passphrase; WPS should be disabled on the access point",
                "correct": True,
                "rationale": (
                    "Correct. The WPS PIN mechanism's design flaw allows the 8-digit PIN to be brute-forced in a "
                    "practical time frame, which in turn discloses the WPA2 passphrase regardless of its own "
                    "strength; disabling WPS eliminates this attack path."
                ),
            },
            {
                "id": "b",
                "text": "The WPA2 passphrase itself is inherently too short and should be lengthened further",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the passphrase is long and complex; the compromise occurred "
                    "through the separate WPS PIN mechanism, not by directly attacking the passphrase's strength."
                ),
            },
            {
                "id": "c",
                "text": "The access point is using outdated TKIP encryption instead of AES-CCMP, which should be upgraded",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario indicates the encryption cipher was the exploited "
                    "weakness; the described attack specifically targets the WPS PIN exchange mechanism, "
                    "independent of the encryption cipher in use."
                ),
            },
            {
                "id": "d",
                "text": "The access point's firmware needs to be updated to fix a buffer overflow vulnerability",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a design weakness in the WPS PIN brute-force resistance "
                    "(a protocol-level flaw, not a code-level buffer overflow), which is remediated by disabling "
                    "WPS rather than a firmware patch for memory corruption."
                ),
            },
        ],
        "explanation": (
            "WPS PIN authentication has a well-documented design flaw that allows its 8-digit PIN to be "
            "brute-forced in a practical time frame, ultimately exposing the underlying WPA2 passphrase "
            "regardless of its strength. The correct remediation is disabling WPS entirely, not lengthening the "
            "passphrase, changing the encryption cipher, or patching firmware for an unrelated flaw."
        ),
    },
]
