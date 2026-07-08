"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file G."""

QUESTIONS = [
    {
        "id": "nd4g-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A retail chain's point-of-sale (POS) software assigns transaction permissions so that any employee "
            "logged in with the 'Cashier' role can process sales. Separately, the POS software itself enforces a "
            "company-wide condition that blocks ALL cash-drawer override transactions between 11:00 p.m. and "
            "5:00 a.m., regardless of which employee or role is logged in at the register. Which access control "
            "mechanism enforces the overnight cash-drawer override block specifically?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rule-based access control",
                "correct": True,
                "rationale": (
                    "Correct. The overnight block is a fixed, administrator-defined IF-THEN condition (time window) "
                    "applied uniformly regardless of the logged-in user's role, which is the defining characteristic "
                    "of rule-based access control."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC explains why any 'Cashier' can process sales, but it does not explain the "
                    "overnight override block, which applies uniformly regardless of role rather than being tied "
                    "to a specific role assignment."
                ),
            },
            {
                "id": "c",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC lets a resource owner grant access at their discretion. The overnight block is "
                    "a fixed, centrally enforced condition with no owner discretion involved."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC compares subject clearance to object classification labels set by a central "
                    "authority. There are no classification labels or clearance levels in this scenario — just a "
                    "time-based condition applied to a transaction type."
                ),
            },
        ],
        "explanation": (
            "Rule-based access control enforces fixed, condition-driven policies (such as time-of-day windows) "
            "that apply regardless of the requester's role or identity. RBAC explains the cashier's baseline "
            "permissions, but the uniform overnight restriction is a separate rule-based control layered on top."
        ),
    },
    {
        "id": "nd4g-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A national retail chain's inventory management system originally had 12 role-based access control "
            "(RBAC) roles. Over five years, one-off requests for 'just this one extra permission' were each "
            "solved by cloning an existing role and adding the requested right. An access review now finds 340 "
            "unique, mostly overlapping role definitions, making certification and audit nearly impossible. "
            "Which access control characteristic MOST directly explains this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Role explosion, a known weakness of RBAC when fine-grained exceptions are handled by creating new roles",
                "correct": True,
                "rationale": (
                    "Correct. RBAC ties permissions to static roles; when administrators repeatedly create nearly "
                    "duplicate roles to satisfy narrow, one-off requests instead of using a more granular model, "
                    "the role count explodes, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "This is an expected, low-risk outcome of applying least privilege under any access control model",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege does not require proliferating near-duplicate roles; a model like "
                    "ABAC can grant the same fine-grained access without multiplying role definitions, so this "
                    "outcome is a design weakness, not an unavoidable byproduct of least privilege."
                ),
            },
            {
                "id": "c",
                "text": "The organization should switch to discretionary access control (DAC) to simplify administration",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC would remove centralized oversight entirely, letting individual resource owners "
                    "grant access at will — worse for auditability in a regulated retail environment, not better."
                ),
            },
            {
                "id": "d",
                "text": "The system is actually using rule-based access control instead of RBAC, which caused the growth",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly describes role definitions being cloned and expanded, not "
                    "fixed IF-THEN conditions being evaluated, so this misattributes the cause to the wrong model."
                ),
            },
        ],
        "explanation": (
            "Role explosion occurs when RBAC administrators repeatedly clone roles to satisfy narrow exceptions "
            "instead of adopting a more dynamic, attribute-driven model, resulting in an unmanageable number of "
            "overlapping roles that undermine the administrative simplicity RBAC is supposed to provide."
        ),
    },
    {
        "id": "nd4g-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A CI/CD pipeline secret-scanning tool reveals that a developer committed a live cloud provider API "
            "key to a public GitHub repository six months ago. The key was rotated in the repository's most "
            "recent commit, but the old key value was never revoked at the cloud provider. What should the "
            "security team do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Revoke the old exposed key directly with the cloud provider so it can no longer authenticate",
                "correct": True,
                "rationale": (
                    "Correct. The old key has been publicly exposed for six months and remains valid at the "
                    "provider regardless of what value now appears in the latest commit; revoking it immediately "
                    "closes the live exposure, which is the most urgent action."
                ),
            },
            {
                "id": "b",
                "text": "Purge the secret from the repository's entire git history using a history-rewriting tool",
                "correct": False,
                "rationale": (
                    "Incorrect. Rewriting history is good hygiene, but it does not invalidate the still-active key; "
                    "anyone who already cloned or scraped the public repo retains a working credential until the "
                    "key itself is revoked at the provider."
                ),
            },
            {
                "id": "c",
                "text": "Notify all engineers to enable pre-commit secret scanning going forward",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a valuable preventive control for future commits, but it does nothing to "
                    "address the currently live, already-exposed credential."
                ),
            },
            {
                "id": "d",
                "text": "Rotate the API key in the code repository a second time",
                "correct": False,
                "rationale": (
                    "Incorrect. The key was already rotated in the latest commit; changing the code again does not "
                    "revoke the old key's validity at the cloud provider, which is the actual exposure."
                ),
            },
        ],
        "explanation": (
            "Because the old key was publicly exposed for six months, it must be treated as compromised and "
            "revoked at the provider immediately. Rewriting git history and adding preventive scanning are sound "
            "follow-up steps, but neither addresses the live, still-valid exposed credential."
        ),
    },
    {
        "id": "nd4g-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "Select TWO practices that would BEST reduce the risk of a web application being exploited through "
            "vulnerabilities in its third-party open-source dependencies."
        ),
        "options": [
            {
                "id": "a",
                "text": "Maintain a software bill of materials (SBOM) and continuously scan it with software composition analysis (SCA) against known-vulnerability databases",
                "correct": True,
                "rationale": (
                    "Correct. SCA against an SBOM is specifically designed to identify known vulnerabilities in "
                    "third-party and open-source components, which is exactly the risk category described."
                ),
            },
            {
                "id": "b",
                "text": "Subscribe to vendor security advisories and apply dependency updates on a defined patch cadence rather than only reactively",
                "correct": True,
                "rationale": (
                    "Correct. Proactively tracking advisories and patching on a schedule closes known dependency "
                    "vulnerabilities before they are exploited, rather than waiting for an incident to force action."
                ),
            },
            {
                "id": "c",
                "text": "Rely solely on the application's SAST results, since static analysis fully analyzes the internals of imported third-party libraries",
                "correct": False,
                "rationale": (
                    "Incorrect. SAST is designed to analyze first-party source code; it generally does not deeply "
                    "analyze the internals of compiled or vendored third-party libraries, so relying on it alone "
                    "leaves dependency vulnerabilities undetected."
                ),
            },
            {
                "id": "d",
                "text": "Disable automatic dependency version updates entirely so the application never changes after its initial security review",
                "correct": False,
                "rationale": (
                    "Incorrect. Freezing dependencies means vulnerabilities discovered later in those pinned "
                    "versions are never remediated, increasing risk over time rather than reducing it."
                ),
            },
        ],
        "explanation": (
            "Managing third-party dependency risk requires visibility (SBOM plus SCA scanning) and an active "
            "patch cadence driven by vendor advisories. SAST does not substitute for dependency scanning, and "
            "freezing versions indefinitely only accumulates unpatched known vulnerabilities."
        ),
    },
    {
        "id": "nd4g-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A network access control (NAC) system detects an unmanaged laptop connecting to a corporate switch "
            "port. The device has never appeared in the CMDB and has no assigned owner. Which asset management "
            "practice, if properly enforced BEFORE this event, would have MOST likely prevented this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An onboarding process requiring every new device to be registered and tagged in the CMDB before it is granted network access",
                "correct": True,
                "rationale": (
                    "Correct. Requiring CMDB registration and an assigned owner as a prerequisite for network "
                    "access ensures no device can connect without first being accounted for in inventory, "
                    "directly preventing this exact gap."
                ),
            },
            {
                "id": "b",
                "text": "Conducting an annual physical inventory audit of all devices",
                "correct": False,
                "rationale": (
                    "Incorrect. An annual audit is retrospective; it might eventually discover the device but does "
                    "nothing to prevent an unregistered device from connecting to the network in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Requiring asset owners to self-report device disposal to the asset management team",
                "correct": False,
                "rationale": (
                    "Incorrect. This addresses end-of-life decommissioning, not the onboarding gap that allowed an "
                    "unregistered device to appear on the network."
                ),
            },
            {
                "id": "d",
                "text": "Classifying the sensitivity of data stored on each managed device",
                "correct": False,
                "rationale": (
                    "Incorrect. Data classification labels information sensitivity; it does not register new "
                    "hardware into inventory or gate network access at connection time."
                ),
            },
        ],
        "explanation": (
            "Preventing unmanaged devices from appearing on the network requires enforcing registration and "
            "ownership assignment as a precondition of network access — a preventive onboarding control, unlike "
            "the periodic or reactive alternatives offered as distractors."
        ),
    },
    {
        "id": "nd4g-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "Select TWO practices that are essential components of an effective IT asset management (ITAM) "
            "lifecycle program."
        ),
        "options": [
            {
                "id": "a",
                "text": "Assigning a documented owner and criticality/classification rating to every asset at the time of acquisition or provisioning",
                "correct": True,
                "rationale": (
                    "Correct. Capturing ownership and criticality at acquisition ensures every asset is accounted "
                    "for and prioritized correctly from the start of its lifecycle, rather than after a gap is "
                    "discovered."
                ),
            },
            {
                "id": "b",
                "text": "Maintaining an automated, continuously reconciled inventory (e.g., discovery scanning integrated with the CMDB) rather than relying solely on periodic manual counts",
                "correct": True,
                "rationale": (
                    "Correct. Continuous automated reconciliation catches drift between what is deployed and what "
                    "is recorded far faster than infrequent manual counts, reducing the window of unmanaged risk."
                ),
            },
            {
                "id": "c",
                "text": "Allowing any employee to connect new personal or unapproved hardware to the production network, provided IT is notified afterward",
                "correct": False,
                "rationale": (
                    "Incorrect. Notifying IT after the fact is reactive; it still allows unregistered hardware "
                    "onto the network before inventory and risk controls are applied, undermining the program."
                ),
            },
            {
                "id": "d",
                "text": "Deferring asset disposal and data sanitization decisions indefinitely until the purchasing department submits a formal request",
                "correct": False,
                "rationale": (
                    "Incorrect. A sound lifecycle program defines clear decommissioning triggers; waiting "
                    "indefinitely leaves stale devices and their data exposed with no managed disposal path."
                ),
            },
        ],
        "explanation": (
            "Effective ITAM requires proactive ownership assignment at acquisition and continuous, automated "
            "inventory reconciliation. Reactive notification-after-connection and indefinite deferral of disposal "
            "both leave gaps that undermine lifecycle visibility and control."
        ),
    },
    {
        "id": "nd4g-007",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOC's analysts currently spend significant time manually querying threat-intelligence feeds, "
            "WHOIS records, and a malware sandbox for every indicator that appears in a new alert, then pasting "
            "the results back into the ticket. Which automation capability BEST eliminates this repetitive, "
            "manual step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A SOAR enrichment playbook that automatically queries the integrated intel sources and appends the results to the alert",
                "correct": True,
                "rationale": (
                    "Correct. SOAR enrichment playbooks are purpose-built to automatically call external "
                    "intelligence, WHOIS, and sandbox APIs and attach the results to a ticket, removing the "
                    "manual, repetitive swivel-chair work described."
                ),
            },
            {
                "id": "b",
                "text": "A SIEM correlation rule that raises the alert's severity score",
                "correct": False,
                "rationale": (
                    "Incorrect. A correlation rule adjusts scoring based on already-ingested data; it does not "
                    "reach out to external threat-intel, WHOIS, or sandbox services to gather new enrichment data."
                ),
            },
            {
                "id": "c",
                "text": "An EDR policy that automatically isolates any host generating the alert",
                "correct": False,
                "rationale": (
                    "Incorrect. Host isolation is a containment action, not an enrichment/lookup capability, and "
                    "does not address the manual research burden described."
                ),
            },
            {
                "id": "d",
                "text": "A vulnerability scanner configured to run on a fixed weekly schedule",
                "correct": False,
                "rationale": (
                    "Incorrect. Scheduled vulnerability scanning identifies weaknesses in assets; it has no role "
                    "in automatically enriching alert indicators with threat intelligence."
                ),
            },
        ],
        "explanation": (
            "SOAR enrichment playbooks automate the exact repetitive, multi-source lookup work described, freeing "
            "analysts from manual data-gathering so they can focus on triage and decision-making."
        ),
    },
    {
        "id": "nd4g-008",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "Two independently built SOAR playbooks both respond to 'malware detected' alerts: Playbook A "
            "isolates the host and opens a ticket, while Playbook B isolates the host and, upon finding it "
            "already isolated, automatically escalates by shutting down the entire network segment. During a "
            "routine EDR test detection, both playbooks fire simultaneously, and a production segment is taken "
            "offline unnecessarily. Which practice would BEST have prevented this specific outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Implementing orchestration governance that checks current alert/response state before triggering a new action, preventing overlapping playbooks from causing conflicting or cascading responses",
                "correct": True,
                "rationale": (
                    "Correct. A coordinating orchestration layer that recognizes an action already in progress "
                    "(host already isolated) before allowing a second, more severe automated action to fire "
                    "directly prevents this cascading failure."
                ),
            },
            {
                "id": "b",
                "text": "Raising the EDR's detection threshold so fewer test detections occur",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing detection sensitivity might lower alert volume, but it does not fix the "
                    "underlying flaw of two playbooks independently triggering conflicting, cascading actions on "
                    "any real alert."
                ),
            },
            {
                "id": "c",
                "text": "Disabling one of the two playbooks entirely",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a blunt workaround that removes intended functionality rather than fixing "
                    "the coordination gap; a future new playbook could reintroduce the same conflict."
                ),
            },
            {
                "id": "d",
                "text": "Requiring manual analyst approval before every single automated response action",
                "correct": False,
                "rationale": (
                    "Incorrect. This would prevent the specific incident but defeats the purpose and scalability "
                    "of automation entirely, which is a worse trade-off than adding coordination logic that "
                    "preserves automated response while preventing conflicts."
                ),
            },
        ],
        "explanation": (
            "The root cause is a lack of coordination between independently triggered playbooks. Orchestration "
            "governance that checks current response state before escalating prevents cascading, conflicting "
            "actions without sacrificing the benefits of automation."
        ),
    },
    {
        "id": "nd4g-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A company's call-center agents use non-persistent virtual desktop infrastructure (VDI) sessions "
            "that are automatically destroyed and reset to a clean golden image the moment a user logs off, with "
            "no local snapshot retained. An investigation into suspected data exfiltration by an agent is opened "
            "45 minutes after that agent's shift ended and the VDI session was already destroyed. Which "
            "limitation MOST directly explains why potentially critical evidence is now unrecoverable?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Non-persistent VDI sessions discard all volatile and session-specific state upon logoff, so evidence that existed only in that ephemeral session was lost once it was destroyed",
                "correct": True,
                "rationale": (
                    "Correct. Because the VDI architecture is designed to reset to a clean image after every "
                    "logoff with no retained snapshot, any evidence unique to that session is irretrievably gone "
                    "as soon as the session ends."
                ),
            },
            {
                "id": "b",
                "text": "The responder failed to follow the order of volatility",
                "correct": False,
                "rationale": (
                    "Incorrect. The loss occurred due to the architecture's automatic destruction of the session "
                    "before the responder was even notified — there was no opportunity to apply order of "
                    "volatility procedures at all."
                ),
            },
            {
                "id": "c",
                "text": "The responder should have used a hardware write blocker on the VDI host",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical disk was seized or imaged in this scenario; a write blocker is "
                    "irrelevant to the loss of an already-destroyed ephemeral session."
                ),
            },
            {
                "id": "d",
                "text": "A chain-of-custody form was not completed in time",
                "correct": False,
                "rationale": (
                    "Incorrect. Chain-of-custody documentation tracks evidence handling after it is collected; it "
                    "has no bearing on why the underlying data was destroyed by the VDI platform's own design."
                ),
            },
        ],
        "explanation": (
            "This scenario illustrates a forensic limitation created by ephemeral infrastructure: because "
            "non-persistent VDI sessions are destroyed on logoff with no retained state, any timing delay in "
            "notification results in permanent, unrecoverable loss of session-specific evidence."
        ),
    },
    {
        "id": "nd4g-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A newly formed incident response team is assembling a field 'jump kit' for on-site forensic "
            "response to a suspected workstation compromise. Which combination of items is MOST essential to "
            "include to properly preserve evidence integrity from the moment of arrival?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Write blockers, anti-static evidence bags, chain-of-custody forms, and a forensically wiped/verified acquisition drive",
                "correct": True,
                "rationale": (
                    "Correct. These items directly support write-protected acquisition, safe physical handling, "
                    "documented custody transfer, and a clean destination for evidence — the core requirements "
                    "for preserving integrity in the field."
                ),
            },
            {
                "id": "b",
                "text": "A general-purpose laptop loaded with common productivity software and a USB drive borrowed from the help desk",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-forensic tools risk contaminating evidence: an unwiped, unverified USB drive "
                    "could already contain unrelated data or could write to the source media, undermining "
                    "integrity."
                ),
            },
            {
                "id": "c",
                "text": "A spare company laptop pre-imaged with the organization's standard corporate desktop image",
                "correct": False,
                "rationale": (
                    "Incorrect. A standard corporate image is built for productivity use, not forensic "
                    "acquisition; it lacks write-blocking and hashing tools needed to preserve evidence integrity."
                ),
            },
            {
                "id": "d",
                "text": "Only a digital camera to photograph the screen, since chain-of-custody documentation can be completed later back at the office",
                "correct": False,
                "rationale": (
                    "Incorrect. Photographs alone do not preserve digital evidence, and delaying custody "
                    "documentation risks creating an unaccounted gap that weakens the chain of custody."
                ),
            },
        ],
        "explanation": (
            "A proper forensic jump kit is built specifically to prevent contamination and support admissibility: "
            "write blockers and wiped acquisition media preserve the data, while evidence bags and custody forms "
            "preserve the handling record, unlike generic hardware or documentation shortcuts."
        ),
    },
    {
        "id": "nd4g-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "During post-incident review, an auditor discovers an unexplained four-hour gap in the "
            "chain-of-custody log for a seized hard drive, between when it was collected at the scene and when "
            "it was logged into the evidence room. Which action should the forensic team take?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Document the gap, note it as a potential integrity concern, and compare a fresh cryptographic hash of the drive against the original acquisition hash to determine whether the evidence was altered",
                "correct": True,
                "rationale": (
                    "Correct. Documenting the discrepancy preserves transparency, and hash comparison provides "
                    "objective, verifiable evidence of whether the drive's contents changed during the "
                    "unaccounted period, allowing an informed decision about the evidence's remaining value."
                ),
            },
            {
                "id": "b",
                "text": "Destroy the evidence, since a broken chain of custody means it can never be used for any purpose",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an unnecessary and drastic overreaction; hash verification may confirm "
                    "the evidence was unaltered, and even reduced evidentiary weight does not eliminate its "
                    "investigative value."
                ),
            },
            {
                "id": "c",
                "text": "Backdate the custody log to remove the appearance of a gap",
                "correct": False,
                "rationale": (
                    "Incorrect. Falsifying records is unethical and illegal, and it would further undermine the "
                    "evidence's credibility and the investigators' integrity if discovered."
                ),
            },
            {
                "id": "d",
                "text": "Continue the investigation without noting the discrepancy, since the evidence tag numbers still match",
                "correct": False,
                "rationale": (
                    "Incorrect. Matching tag numbers do not address an undocumented gap in custody; ignoring it "
                    "risks a serious admissibility challenge later when the gap is inevitably discovered."
                ),
            },
        ],
        "explanation": (
            "The correct response to a custody gap is transparency plus technical verification: document the "
            "discrepancy and use hash comparison to objectively assess whether integrity was preserved, rather "
            "than destroying evidence, falsifying records, or ignoring the issue."
        ),
    },
    {
        "id": "nd4g-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A company's evidence-handling policy requires that whenever physical evidence such as a seized "
            "laptop is transported between facilities, two authorized personnel must jointly verify and sign for "
            "the transfer at both release and receipt. During an investigation, a single courier transports a "
            "sealed evidence bag alone to an off-site forensic lab, and only the receiving examiner signs the "
            "custody log upon arrival. Which chain-of-custody principle was violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Continuous, gap-free custody documentation — there is no record of who released the evidence to the courier or verification that it remained sealed throughout transport",
                "correct": True,
                "rationale": (
                    "Correct. A defensible chain of custody requires an unbroken, documented record at every "
                    "handoff. Because no one signed for the release and the courier traveled alone and unwitnessed, "
                    "there is an unaccounted gap in custody during transport."
                ),
            },
            {
                "id": "b",
                "text": "The requirement that evidence bags be single-use only",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario indicates the tamper-evident bag was reused or resealed; "
                    "the described problem is the missing dual-signature documentation at release, not bag reuse."
                ),
            },
            {
                "id": "c",
                "text": "The requirement that only the examiner who will perform analysis may transport evidence",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a standard chain-of-custody requirement; couriers routinely transport "
                    "sealed evidence, provided the transfer is properly documented and witnessed as policy requires."
                ),
            },
            {
                "id": "d",
                "text": "The requirement that photographs be taken before resealing evidence bags",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a transport handoff, not a reopening and resealing of the "
                    "evidence bag, so this photography requirement does not apply to the described failure."
                ),
            },
        ],
        "explanation": (
            "The organization's own dual-signature policy required verification and sign-off at both ends of a "
            "transfer. Because the courier traveled alone with no release signature recorded, the chain of "
            "custody has an undocumented, unwitnessed gap during transport."
        ),
    },
    {
        "id": "nd4g-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A DLP agent blocks any file matching a confidential watermark pattern from being copied to USB "
            "removable storage. An employee bypasses this by using the 'Print to PDF' virtual printer to convert "
            "a confidential document into a new, unwatermarked PDF, which then copies to a USB drive without "
            "triggering any alert. What does this scenario BEST illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A gap in content-based DLP detection, because the exfiltration technique removed the pattern the DLP engine relied on, showing detection must also account for data transformation techniques",
                "correct": True,
                "rationale": (
                    "Correct. The DLP policy relied on matching a static watermark pattern. Converting the file "
                    "through a virtual printer produced a new file without that pattern, evading detection — "
                    "exactly the kind of transformation gap content-based DLP must be tuned to catch."
                ),
            },
            {
                "id": "b",
                "text": "A failure of the DLP agent's network-based inspection module",
                "correct": False,
                "rationale": (
                    "Incorrect. This exfiltration occurred through an endpoint USB copy operation, not a network "
                    "channel, so a network inspection module failure is not the relevant cause."
                ),
            },
            {
                "id": "c",
                "text": "A bypass of multifactor authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. No authentication step was involved in this scenario; the employee used a locally "
                    "available printing feature, not stolen or bypassed credentials."
                ),
            },
            {
                "id": "d",
                "text": "Proof that DLP is fundamentally ineffective and should be removed",
                "correct": False,
                "rationale": (
                    "Incorrect. This overgeneralized conclusion is unjustified; the correct response is to tune "
                    "detection to account for format-conversion techniques, not to abandon the control entirely."
                ),
            },
        ],
        "explanation": (
            "Static pattern/watermark matching alone is insufficient because simple format conversions can strip "
            "the detected pattern while preserving the underlying sensitive content, requiring DLP policies to "
            "also account for such transformation techniques."
        ),
    },
    {
        "id": "nd4g-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "An attacker with local administrator rights on a compromised workstation attempts to stop the EDR "
            "agent's service and delete its installation directory. The agent's kernel-mode self-protection "
            "(tamper protection) blocks both actions and immediately raises a high-severity 'defense evasion "
            "attempt' alert to the SOC. Which security benefit does this scenario BEST demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tamper protection prevents a compromised host with elevated local privileges from disabling its own security monitoring, and the attempt itself becomes a high-fidelity detection signal",
                "correct": True,
                "rationale": (
                    "Correct. Even with local administrator rights, the agent's self-protection prevented the "
                    "attacker from blinding the endpoint, and the failed attempt generated a strong, actionable "
                    "alert — exactly the intended benefit of tamper protection."
                ),
            },
            {
                "id": "b",
                "text": "It proves the workstation had fully up-to-date patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario relates to patch levels; tamper protection is a distinct "
                    "self-defense capability of the EDR agent, unrelated to OS or application patching status."
                ),
            },
            {
                "id": "c",
                "text": "It demonstrates the EDR agent relies solely on signature-based detection",
                "correct": False,
                "rationale": (
                    "Incorrect. Tamper protection is a self-protection mechanism, not a detection method; it says "
                    "nothing about whether the agent uses signatures, behavioral analytics, or both."
                ),
            },
            {
                "id": "d",
                "text": "It indicates the workstation was not a member of the domain",
                "correct": False,
                "rationale": (
                    "Incorrect. Tamper protection functions independent of domain membership, and no information "
                    "about domain status is provided or implied by this scenario."
                ),
            },
        ],
        "explanation": (
            "EDR tamper/self-protection ensures that even a locally privileged attacker cannot silently disable "
            "endpoint monitoring, and the blocked attempt itself surfaces as a high-value detection event for the "
            "SOC."
        ),
    },
    {
        "id": "nd4g-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A security team has configured DMARC with 'rua=mailto:dmarc-agg@company.com' to receive daily "
            "aggregate reports. They also want to receive individual failure reports that include a copy of "
            "specific messages that fail SPF/DKIM alignment, for deeper investigation of active spoofing "
            "attempts. Which DMARC tag should be added to the record?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ruf= (a forensic/failure reporting address)",
                "correct": True,
                "rationale": (
                    "Correct. The ruf= tag specifies where DMARC forensic (failure) reports — which can include "
                    "message-level detail about individual authentication failures — should be sent, distinct "
                    "from the rua= aggregate summary address."
                ),
            },
            {
                "id": "b",
                "text": "sp= (the subdomain policy tag)",
                "correct": False,
                "rationale": (
                    "Incorrect. sp= sets the DMARC policy applied specifically to subdomains; it has no role in "
                    "requesting forensic failure reports."
                ),
            },
            {
                "id": "c",
                "text": "pct=100 (the percentage of messages subjected to filtering)",
                "correct": False,
                "rationale": (
                    "Incorrect. pct= controls what fraction of failing messages the policy (p=) is applied to; it "
                    "does not configure where any reports are sent."
                ),
            },
            {
                "id": "d",
                "text": "adkim=s (strict DKIM alignment mode)",
                "correct": False,
                "rationale": (
                    "Incorrect. adkim= controls how strictly the DKIM domain must match the visible From domain "
                    "for alignment purposes; it has nothing to do with report delivery addresses."
                ),
            },
        ],
        "explanation": (
            "DMARC distinguishes aggregate reports (rua=), which summarize authentication results in bulk, from "
            "forensic/failure reports (ruf=), which can provide per-message detail about individual failures — "
            "the ruf= tag is required to receive the latter."
        ),
    },
    {
        "id": "nd4g-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A security audit finds that an organization's DKIM signing key is only 512 bits, which modern "
            "compute resources can factor in a practical amount of time, allowing an attacker to potentially "
            "forge valid DKIM signatures. Which remediation is BEST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rotate to a stronger key (e.g., RSA 2048-bit or higher) and republish the new DKIM public key in DNS",
                "correct": True,
                "rationale": (
                    "Correct. Replacing the weak key with a cryptographically strong one and publishing the "
                    "corresponding public key directly fixes the factorization risk while preserving DKIM's "
                    "protection."
                ),
            },
            {
                "id": "b",
                "text": "Switch from DKIM to SPF only, since SPF does not rely on cryptographic keys",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing DKIM eliminates an entire authentication mechanism and weakens DMARC "
                    "alignment options rather than fixing the actual problem, which is simply the key's length."
                ),
            },
            {
                "id": "c",
                "text": "Increase the DMARC record's 'pct' value to 100",
                "correct": False,
                "rationale": (
                    "Incorrect. The pct= tag controls what portion of failing mail the DMARC policy applies to; "
                    "it has no effect on DKIM key strength."
                ),
            },
            {
                "id": "d",
                "text": "Add more approved sending IP addresses to the SPF record",
                "correct": False,
                "rationale": (
                    "Incorrect. SPF IP authorization is unrelated to DKIM's cryptographic signing key; this "
                    "change does not address the weak-key risk at all."
                ),
            },
        ],
        "explanation": (
            "The vulnerability is specifically the DKIM key's insufficient length. The correct fix is rotating to "
            "a stronger key and republishing it — removing DKIM entirely or adjusting unrelated SPF/DMARC tags "
            "does not resolve the underlying cryptographic weakness."
        ),
    },
    {
        "id": "nd4g-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A SaaS application uses SAML just-in-time (JIT) provisioning, automatically creating accounts and "
            "assigning application roles based on a 'department' attribute in the SAML assertion. An audit finds "
            "a contractor account created via JIT provisioning has full administrative rights because the IdP's "
            "default value for unmapped departments was inadvertently set to 'IT-Admin' rather than a safe "
            "default. Which remediation MOST directly addresses the root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Change the IdP's default/fallback attribute value used in JIT provisioning to a least-privilege role so unmapped or missing attributes never resolve to elevated access",
                "correct": True,
                "rationale": (
                    "Correct. The root cause is a misconfigured fallback value that grants excessive privilege by "
                    "default; fixing that default to a minimal, least-privilege role directly closes the gap for "
                    "all future unmapped accounts."
                ),
            },
            {
                "id": "b",
                "text": "Disable SAML entirely and require manual account creation for every user",
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the operational benefit of federation and JIT provisioning "
                    "entirely rather than fixing the specific attribute-mapping misconfiguration that caused the "
                    "issue."
                ),
            },
            {
                "id": "c",
                "text": "Require the contractor to complete additional MFA enrollment",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding MFA strengthens authentication but does nothing to correct the excessive "
                    "authorization the contractor already received through the flawed default mapping."
                ),
            },
            {
                "id": "d",
                "text": "Rotate the SAML signing certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. The signing certificate's validity is unrelated to attribute-mapping logic; "
                    "rotating it would not change how unmapped department values are resolved into roles."
                ),
            },
        ],
        "explanation": (
            "The vulnerability originates in the JIT provisioning attribute-mapping default, not in "
            "authentication strength or certificate integrity. Correcting the fallback to a least-privilege value "
            "prevents any future unmapped attribute from silently granting administrative access."
        ),
    },
    {
        "id": "nd4g-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "During an authorized assessment of a web application's 'Sign in with [SSO Provider]' OAuth 2.0 "
            "authorization code flow, a tester finds that the application's callback endpoint does not validate "
            "a unique, unpredictable 'state' parameter returned from the authorization server. Which attack does "
            "this omission MOST directly enable?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An OAuth login cross-site request forgery (CSRF) attack, tricking a victim into completing an authorization flow bound to the attacker's account",
                "correct": True,
                "rationale": (
                    "Correct. The state parameter exists specifically to bind the authorization request to the "
                    "user's session and prevent forged callback requests; without it, an attacker can craft a "
                    "callback that links the victim's session to an account or context the attacker controls."
                ),
            },
            {
                "id": "b",
                "text": "SQL injection against the authorization server",
                "correct": False,
                "rationale": (
                    "Incorrect. The state parameter is a CSRF-protection mechanism unrelated to how the "
                    "authorization server processes SQL queries; this omission has no bearing on injection risk."
                ),
            },
            {
                "id": "c",
                "text": "A brute-force attack against the user's password",
                "correct": False,
                "rationale": (
                    "Incorrect. The OAuth authorization code flow at the relying party does not involve password "
                    "entry at that endpoint, and the state parameter has no relationship to password guessing."
                ),
            },
            {
                "id": "d",
                "text": "A reflected cross-site scripting (XSS) attack against the callback page",
                "correct": False,
                "rationale": (
                    "Incorrect. The state parameter's purpose is CSRF protection for the OAuth flow, not input "
                    "sanitization; its absence does not by itself create an XSS vulnerability."
                ),
            },
        ],
        "explanation": (
            "The OAuth 'state' parameter is the standard defense against CSRF in the authorization code flow. "
            "Omitting validation of it allows an attacker to forge callback requests and bind a victim's session "
            "to an attacker-controlled context."
        ),
    },
    {
        "id": "nd4g-019",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A vulnerability scan of a newly deployed production web server flags an accessible 'phpinfo.php' "
            "diagnostic file and a default web server welcome page, both left over from the initial software "
            "installation. Which hardening principle was violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Removing default/sample content and unnecessary artifacts from a system before it enters production, as part of establishing a secure baseline",
                "correct": True,
                "rationale": (
                    "Correct. Leftover default files and diagnostic pages are unnecessary attack surface that a "
                    "secure baseline process is specifically meant to strip out before deployment; their presence "
                    "shows this step was skipped."
                ),
            },
            {
                "id": "b",
                "text": "Enforcing strong password complexity policies",
                "correct": False,
                "rationale": (
                    "Incorrect. This finding involves exposed files, not authentication credentials, so password "
                    "policy is not the relevant hardening principle here."
                ),
            },
            {
                "id": "c",
                "text": "Enabling full-disk encryption on the server",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data at rest from physical access or theft; it has no "
                    "bearing on files being publicly exposed through the web server itself."
                ),
            },
            {
                "id": "d",
                "text": "Configuring host-based intrusion prevention",
                "correct": False,
                "rationale": (
                    "Incorrect. HIPS is a compensating detective/preventive control layered on top of a system; "
                    "it does not address the root gap of leftover default content never being removed."
                ),
            },
        ],
        "explanation": (
            "A secure baseline explicitly includes removing default/sample installation artifacts before "
            "production deployment. Encryption, password policy, and HIPS are all valid controls but do not "
            "address this specific attack-surface-reduction gap."
        ),
    },
    {
        "id": "nd4g-020",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "An organization builds new servers from a hardened 'golden image' baseline created 18 months ago. "
            "An audit finds that servers provisioned from this image in the past two months are all missing "
            "several patches and configuration settings that were added to the organization's hardening "
            "standard after the golden image was last updated. Which practice would BEST prevent this recurring "
            "gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Establish a recurring process to rebuild/update the golden image and validate it against the current hardening standard, so newly provisioned systems reflect the latest baseline",
                "correct": True,
                "rationale": (
                    "Correct. Because every new server inherits whatever the golden image contains, keeping the "
                    "image itself current against the latest hardening standard prevents this gap from recurring "
                    "with each new deployment."
                ),
            },
            {
                "id": "b",
                "text": "Increase the frequency of vulnerability scans on production servers",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent scanning would detect the gap sooner but does not prevent it from "
                    "being introduced in the first place, since the stale image is still the source of every new "
                    "deployment."
                ),
            },
            {
                "id": "c",
                "text": "Require manual hardening checklists to be completed by hand on every new server after provisioning",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a labor-intensive, error-prone workaround that treats the symptom on each "
                    "individual server rather than fixing the stale source image feeding every deployment."
                ),
            },
            {
                "id": "d",
                "text": "Disable the ability to provision new servers from images entirely",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an impractical overreaction that eliminates a core operational capability "
                    "instead of simply keeping the existing image current."
                ),
            },
        ],
        "explanation": (
            "Golden images must be periodically rebuilt and revalidated against the current hardening standard; "
            "otherwise every new server perpetuates whatever gaps existed when the image was last updated, no "
            "matter how frequently it is scanned afterward."
        ),
    },
    {
        "id": "nd4g-021",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During ransomware recovery, an IR team restores encrypted file servers from clean backups and "
            "returns them to production the same day the restore completes, without further investigation. Two "
            "days later, the same ransomware re-encrypts the restored servers. Which IR process failure MOST "
            "likely caused the reinfection?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Eradication was skipped or rushed — the initial access vector or attacker's persistence mechanism was never removed before systems were restored and returned to production",
                "correct": True,
                "rationale": (
                    "Correct. Restoring clean data does not remove an attacker's foothold; if the original entry "
                    "point or a backdoor/persistence mechanism remains active, the attacker can simply "
                    "re-deploy ransomware against the newly restored systems."
                ),
            },
            {
                "id": "b",
                "text": "The backups were not encrypted at rest",
                "correct": False,
                "rationale": (
                    "Incorrect. Backup encryption at rest protects backup confidentiality; it has no relationship "
                    "to whether the attacker's access into the live environment was removed."
                ),
            },
            {
                "id": "c",
                "text": "The recovery time objective (RTO) was not met",
                "correct": False,
                "rationale": (
                    "Incorrect. RTO measures how quickly recovery occurs, not whether the root cause was "
                    "eliminated; meeting or missing an RTO target does not explain a reinfection."
                ),
            },
            {
                "id": "d",
                "text": "The organization failed to update its incident response plan documentation",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an administrative gap that does not technically explain how the same "
                    "ransomware was able to re-encrypt the restored servers."
                ),
            },
        ],
        "explanation": (
            "Restoring from backup addresses recovery, not eradication. Skipping root-cause removal before "
            "returning systems to production is a classic IR failure that allows the same threat to reinfect "
            "freshly restored assets."
        ),
    },
    {
        "id": "nd4g-022",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "Three hours into an active data breach investigation, a senior executive asks a SOC analyst for a "
            "detailed technical briefing on affected systems and specific IP addresses so the executive can "
            "personally update the board via a group text message. Per a well-run incident response process, "
            "what is the BEST response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Redirect the request through the incident commander/established communication plan, providing only information appropriate to the pre-defined channels and need-to-know",
                "correct": True,
                "rationale": (
                    "Correct. The IR communication plan exists precisely to control what sensitive investigative "
                    "detail is shared, through which channel, and to whom; routing the request through it avoids "
                    "leaking details over an unsecured, ad hoc channel."
                ),
            },
            {
                "id": "b",
                "text": "Immediately comply since the requester is a senior executive with organizational authority",
                "correct": False,
                "rationale": (
                    "Incorrect. Organizational title does not override the established communication plan or "
                    "need-to-know controls, especially when the requested detail would travel over an unsecured "
                    "personal text message during an active investigation."
                ),
            },
            {
                "id": "c",
                "text": "Refuse to provide any information to anyone outside the SOC until the investigation is fully closed",
                "correct": False,
                "rationale": (
                    "Incorrect. Stakeholders legitimately need appropriate updates through proper channels during "
                    "an active incident; a blanket refusal is overly rigid and not how a functioning communication "
                    "plan operates."
                ),
            },
            {
                "id": "d",
                "text": "End the investigation early to prepare the requested report",
                "correct": False,
                "rationale": (
                    "Incorrect. Cutting an active investigation short to produce a report is a severe process "
                    "failure that disrupts response and does not reflect any recognized IR practice."
                ),
            },
        ],
        "explanation": (
            "A mature IR process routes stakeholder communications through defined channels and need-to-know "
            "controls, regardless of the requester's seniority, precisely to prevent sensitive investigative "
            "details from leaking through unsecured, informal channels."
        ),
    },
    {
        "id": "nd4g-023",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An investigator needs the exact command-line arguments used to launch a suspicious process on a "
            "Windows server, but the default Security event log (Event ID 4688) shows only the process name, "
            "not the parameters passed to it. Which change would provide this level of detail for future "
            "investigations?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable command-line auditing for process creation events via Group Policy (or deploy Sysmon with command-line logging)",
                "correct": True,
                "rationale": (
                    "Correct. Windows does not log command-line arguments in process creation events by default; "
                    "enabling that specific auditing setting (or using Sysmon, which captures it) is required to "
                    "obtain this level of detail."
                ),
            },
            {
                "id": "b",
                "text": "Increase the Security log's maximum file size",
                "correct": False,
                "rationale": (
                    "Incorrect. A larger log file only increases how much history is retained; it does not add "
                    "new data fields such as command-line arguments to existing event types."
                ),
            },
            {
                "id": "c",
                "text": "Enable Windows Defender real-time protection",
                "correct": False,
                "rationale": (
                    "Incorrect. Real-time antivirus protection is a prevention/detection control, not a logging "
                    "configuration, and does not add command-line detail to process creation events."
                ),
            },
            {
                "id": "d",
                "text": "Switch from Event Viewer to a third-party log viewing tool",
                "correct": False,
                "rationale": (
                    "Incorrect. A different viewing tool only changes how existing log data is displayed; it "
                    "cannot surface data that was never captured in the first place."
                ),
            },
        ],
        "explanation": (
            "Command-line arguments are not captured by default in Windows Event ID 4688; explicit auditing "
            "configuration (or Sysmon) must be enabled to record this detail before it can be reviewed in an "
            "investigation."
        ),
    },
    {
        "id": "nd4g-024",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "Select TWO statements that correctly describe the appropriate use of log data sources during an "
            "investigation."
        ),
        "options": [
            {
                "id": "a",
                "text": "NetFlow records show connection metadata (source/destination IP, ports, byte counts) but not the actual packet payload content",
                "correct": True,
                "rationale": (
                    "Correct. NetFlow is a summary of connection metadata; it is useful for identifying volume "
                    "and destinations of traffic but does not include the payload content itself."
                ),
            },
            {
                "id": "b",
                "text": "DNS query logs can reveal which internal host resolved a particular malicious domain name, helping identify a compromised endpoint",
                "correct": True,
                "rationale": (
                    "Correct. DNS logs record which internal client requested resolution of a given domain, "
                    "making them a key source for pinpointing which host first reached out to a malicious domain."
                ),
            },
            {
                "id": "c",
                "text": "Firewall logs alone are sufficient to reconstruct the exact SQL query text submitted to a backend database",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewalls operate at the network/connection layer and log metadata such as IPs "
                    "and ports; they do not capture application-layer content like the text of a SQL query."
                ),
            },
            {
                "id": "d",
                "text": "Windows Security event logs record full command-line arguments for every process by default, with no additional configuration required",
                "correct": False,
                "rationale": (
                    "Incorrect. As with the command-line logging gap described elsewhere, this detail is not "
                    "captured by default and requires explicit auditing configuration or a tool like Sysmon."
                ),
            },
        ],
        "explanation": (
            "NetFlow and DNS logs each provide specific, useful but limited visibility (metadata and resolution "
            "history, respectively), while firewall logs cannot substitute for application-layer/database audit "
            "logs, and Windows does not capture command-line detail without additional configuration."
        ),
    },
    {
        "id": "nd4g-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "An employee downloads what appears to be a free PDF converter utility from a non-official "
            "third-party website. After installation, the tool functions normally as a PDF converter, but a "
            "background process begins making periodic outbound connections to an unfamiliar external IP address "
            "and silently downloading additional files. Which type of malware BEST describes this software?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trojan (horse)",
                "correct": True,
                "rationale": (
                    "Correct. The malicious functionality is disguised inside software the user willingly "
                    "installed because it appeared to be a legitimate, desired utility — the defining trait of a "
                    "Trojan."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm self-propagates to other hosts without user interaction; this scenario "
                    "describes a single manually installed utility with no described spreading behavior."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb triggers its payload upon a specific condition or date being met; "
                    "this scenario describes ongoing periodic beaconing, not a condition-triggered payload."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit specifically hides its own presence by modifying the OS or intercepting "
                    "system calls; the scenario describes no concealment behavior, just a secondary malicious "
                    "function bundled with a legitimate-seeming tool."
                ),
            },
        ],
        "explanation": (
            "A Trojan disguises malicious functionality within software the victim believes to be legitimate and "
            "voluntarily installs, distinguishing it from worms (self-propagation), logic bombs "
            "(condition-triggered payloads), and rootkits (concealment of presence)."
        ),
    },
    {
        "id": "nd4g-026",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A user reports fraudulent use of their online banking credentials despite never reusing that "
            "password elsewhere and never clicking a phishing link. Forensic analysis of the user's home "
            "computer finds a hidden background process that records every keystroke, including into the "
            "browser's password field, and periodically uploads a log file to a remote server. Which "
            "classification BEST fits this malware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Keylogger (a form of spyware)",
                "correct": True,
                "rationale": (
                    "Correct. The malware's described behavior — silently capturing every keystroke, including "
                    "credentials, and exfiltrating them — is the precise defining function of a keylogger."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts files and demands payment for restoration; nothing in this "
                    "scenario describes file encryption or an extortion demand."
                ),
            },
            {
                "id": "c",
                "text": "Adware",
                "correct": False,
                "rationale": (
                    "Incorrect. Adware displays unwanted advertisements; it does not describe silently recording "
                    "and exfiltrating keystrokes and credentials as in this scenario."
                ),
            },
            {
                "id": "d",
                "text": "Botnet client used for distributed denial-of-service (DDoS) attacks",
                "correct": False,
                "rationale": (
                    "Incorrect. A DDoS bot's primary function is participating in coordinated flood attacks under "
                    "attacker command; the behavior described here — recording and exfiltrating keystrokes — is "
                    "specifically keylogging/spyware activity, not DDoS participation."
                ),
            },
        ],
        "explanation": (
            "The precise behavior of silently capturing keystrokes typed into sensitive fields and exfiltrating "
            "them to a remote server is the hallmark of a keylogger, a category of spyware, distinguishing it "
            "from ransomware, adware, and DDoS-oriented bots."
        ),
    },
    {
        "id": "nd4g-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A corporate iPhone is remotely wiped through the MDM console after being reported lost. The device "
            "is later recovered, but re-enrolling it in MDM fails because Apple's Activation Lock (tied to the "
            "previous user's personal Apple ID/Find My) requires that user's Apple ID credentials to reactivate "
            "the device. Which MDM configuration, if enforced from initial enrollment, would have MOST likely "
            "prevented this obstacle?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enforcing device supervision through Apple Business Manager so IT can clear Activation Lock without needing the end user's personal Apple ID credentials",
                "correct": True,
                "rationale": (
                    "Correct. Supervised, organization-enrolled devices allow IT to bypass or clear Activation "
                    "Lock centrally, preventing a personal Apple ID from being able to hold a corporate device "
                    "hostage after a wipe."
                ),
            },
            {
                "id": "b",
                "text": "Requiring a stronger device passcode policy",
                "correct": False,
                "rationale": (
                    "Incorrect. Passcode strength has no relationship to Activation Lock, which is tied to the "
                    "Apple ID/Find My association, not the device passcode."
                ),
            },
            {
                "id": "c",
                "text": "Enabling remote wipe capability",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote wipe was already used successfully in this scenario; it is not what "
                    "prevents the subsequent Activation Lock obstacle to re-enrollment."
                ),
            },
            {
                "id": "d",
                "text": "Configuring per-app VPN tunneling",
                "correct": False,
                "rationale": (
                    "Incorrect. Per-app VPN controls network traffic routing for specific apps; it has no "
                    "relationship to device activation or ownership locks."
                ),
            },
        ],
        "explanation": (
            "Activation Lock is tied to a personal Apple ID/Find My association, not to remote wipe or passcode "
            "settings. Enforcing supervised enrollment through Apple Business Manager from the start gives IT the "
            "ability to clear the lock without the former user's credentials."
        ),
    },
    {
        "id": "nd4g-028",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "An organization integrates its MDM platform with its cloud identity provider so that only devices "
            "reporting a 'compliant' status (encrypted, passcode enabled, not jailbroken, current OS patch "
            "level) are permitted to authenticate to corporate email and SharePoint, regardless of whether the "
            "user's credentials are correct. Which security benefit does this integration BEST provide?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It extends access decisions beyond user identity alone to include device security posture, preventing compromised credentials from being used successfully from an unmanaged or non-compliant device",
                "correct": True,
                "rationale": (
                    "Correct. By gating authentication on device compliance in addition to valid credentials, "
                    "this conditional access enforcement point blocks sign-in attempts even when an attacker "
                    "possesses correct credentials but is using an unmanaged or non-compliant device."
                ),
            },
            {
                "id": "b",
                "text": "It eliminates the need for multifactor authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Device compliance and MFA are complementary controls addressing different risks "
                    "(device posture versus authentication assurance); neither substitutes for the other."
                ),
            },
            {
                "id": "c",
                "text": "It guarantees that lost devices can never be remotely wiped",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an unrelated, false claim; compliance-gated access does not affect the "
                    "MDM's remote wipe capability in either direction."
                ),
            },
            {
                "id": "d",
                "text": "It automatically encrypts data in transit between the device and the cloud service",
                "correct": False,
                "rationale": (
                    "Incorrect. Data-in-transit encryption is handled by TLS regardless of device compliance "
                    "status; compliance checking and transport encryption are separate, unrelated controls."
                ),
            },
        ],
        "explanation": (
            "Integrating MDM compliance status with the identity provider creates a conditional access "
            "enforcement point that evaluates device posture alongside credentials, blocking valid-credential "
            "sign-ins from unmanaged or non-compliant devices — a benefit distinct from MFA, wipe capability, or "
            "transport encryption."
        ),
    },
    {
        "id": "nd4g-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "An organization enforces FIDO2 hardware security keys for all privileged administrator accounts. A "
            "help-desk audit finds that every account also has SMS-based one-time passcodes enabled as a "
            "fallback recovery method in case the hardware key is lost. A penetration tester takes over an "
            "administrator account by performing a SIM swap and using the SMS fallback, without ever touching "
            "the hardware key. What does this scenario BEST illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A strong authentication control can be undermined by a weaker fallback/recovery mechanism, since overall account security is only as strong as the weakest permitted authentication path",
                "correct": True,
                "rationale": (
                    "Correct. Regardless of how strong the FIDO2 hardware key is, leaving a weaker SMS fallback "
                    "enabled provides an alternate, easier path for an attacker to compromise the account "
                    "entirely — the account's real strength equals its weakest allowed path."
                ),
            },
            {
                "id": "b",
                "text": "FIDO2 hardware keys are vulnerable to phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. FIDO2 is specifically designed to be phishing-resistant, and the hardware key was "
                    "never used or attacked in this scenario; the compromise occurred entirely through the "
                    "separate SMS fallback path."
                ),
            },
            {
                "id": "c",
                "text": "The organization should disable MFA entirely since it was bypassed",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an overreaction that removes protection instead of addressing the actual "
                    "root cause, which is the presence of a weak fallback method alongside the strong one."
                ),
            },
            {
                "id": "d",
                "text": "SIM swapping cannot be prevented by any technical control",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a defeatist overgeneralization; removing the SMS fallback option "
                    "specifically would have prevented this exact attack path regardless of SIM-swap risk "
                    "elsewhere."
                ),
            },
        ],
        "explanation": (
            "Allowing a weak fallback authentication method alongside a strong primary factor creates an "
            "alternate, easier path to compromise, illustrating that overall account security is limited by the "
            "weakest permitted authentication method, not the strongest one deployed."
        ),
    },
    {
        "id": "nd4g-030",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "Select TWO statements that correctly describe authentication factors and attributes used in a "
            "modern adaptive/risk-based authentication system."
        ),
        "options": [
            {
                "id": "a",
                "text": "A hardware FIDO2 security key represents the 'something you have' (possession) factor",
                "correct": True,
                "rationale": (
                    "Correct. A physical security key is a tangible item the user possesses, which is the "
                    "textbook definition of the possession ('something you have') authentication factor."
                ),
            },
            {
                "id": "b",
                "text": "A user's typing cadence or gait pattern used for continuous authentication is an example of behavioral biometrics ('something you do')",
                "correct": True,
                "rationale": (
                    "Correct. Behavioral characteristics like typing rhythm or gait fall under behavioral "
                    "biometrics, commonly described as the 'something you do' authentication attribute."
                ),
            },
            {
                "id": "c",
                "text": "A device's GPS coordinates checked against the user's expected location is classified as the primary 'something you know' factor",
                "correct": False,
                "rationale": (
                    "Incorrect. GPS location is a contextual attribute ('somewhere you are') used in risk-based "
                    "authentication, not a knowledge factor; the user does not 'know' their coordinates as a "
                    "credential."
                ),
            },
            {
                "id": "d",
                "text": "Requiring a second password in addition to the first satisfies true multifactor authentication as long as two credentials are required",
                "correct": False,
                "rationale": (
                    "Incorrect. Two credentials from the same category (two knowledge factors) do not constitute "
                    "true MFA; genuine multifactor authentication requires factors from at least two different "
                    "categories."
                ),
            },
        ],
        "explanation": (
            "Possession (hardware keys) and behavioral biometrics (typing cadence, gait) are legitimate, "
            "distinct authentication factor/attribute categories. Location is a contextual attribute, not a "
            "knowledge factor, and stacking two credentials from the same category does not satisfy true MFA."
        ),
    },
    {
        "id": "nd4g-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "During the exploitation phase of an authorized penetration test, a tester identifies a SQL "
            "injection vulnerability that could be used to dump an entire customer database. Per standard "
            "penetration testing ethics and the signed rules of engagement, what should the tester do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Demonstrate impact with a small, non-sensitive proof-of-concept extraction (e.g., a single row or the database version string) sufficient to prove exploitability",
                "correct": True,
                "rationale": (
                    "Correct. Standard testing ethics call for demonstrating impact with the minimum data "
                    "necessary to prove the vulnerability is real, avoiding unnecessary handling or exposure of "
                    "large volumes of sensitive customer data."
                ),
            },
            {
                "id": "b",
                "text": "Extract the entire database to fully document the scope of exposure for the report",
                "correct": False,
                "rationale": (
                    "Incorrect. Exfiltrating the full dataset creates unnecessary risk and unnecessary handling "
                    "of sensitive data beyond what is needed to prove exploitability, and typically exceeds a "
                    "reasonable rules-of-engagement scope."
                ),
            },
            {
                "id": "c",
                "text": "Immediately stop the test and report a critical vulnerability without further validation",
                "correct": False,
                "rationale": (
                    "Incorrect. Stopping without any proof-of-concept validation leaves the finding unconfirmed, "
                    "weakening the report's evidentiary value compared to a minimal, validated demonstration."
                ),
            },
            {
                "id": "d",
                "text": "Silently patch the vulnerability during the test to prevent real attackers from exploiting it before the report is delivered",
                "correct": False,
                "rationale": (
                    "Incorrect. Remediation is the client's responsibility, not the tester's; making unauthorized "
                    "changes to production systems falls outside the tester's scope and rules of engagement."
                ),
            },
        ],
        "explanation": (
            "Ethical exploitation requires proving impact with the minimum necessary evidence — a small "
            "proof-of-concept extraction — rather than exfiltrating full datasets, skipping validation entirely, "
            "or making unauthorized changes to the target environment."
        ),
    },
    {
        "id": "nd4g-032",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "A penetration test report delivers a prioritized list of findings with CVSS-based risk ratings and "
            "remediation guidance. Sixty days later, the client asks the testing firm to re-run only the "
            "exploits for the previously reported critical findings to confirm they were fixed. Which activity "
            "does this final re-run represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Retesting/validation, confirming that the previously reported remediations were effective",
                "correct": True,
                "rationale": (
                    "Correct. Re-running exploits specifically against previously reported findings, after "
                    "remediation, to confirm they are actually fixed is the defining purpose of a retest/"
                    "validation engagement."
                ),
            },
            {
                "id": "b",
                "text": "Reconnaissance",
                "correct": False,
                "rationale": (
                    "Incorrect. Reconnaissance involves gathering information about the target before testing "
                    "begins; this activity is instead a targeted re-verification of already-known, previously "
                    "reported findings."
                ),
            },
            {
                "id": "c",
                "text": "Post-exploitation",
                "correct": False,
                "rationale": (
                    "Incorrect. Post-exploitation refers to actions taken after initial compromise within the "
                    "same engagement, such as establishing persistence or pivoting — not a separate, later "
                    "confirmation exercise conducted 60 days after the report was delivered."
                ),
            },
            {
                "id": "d",
                "text": "Rules of engagement negotiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Rules of engagement are established before testing begins to define scope and "
                    "authorization; this scenario describes a follow-up verification activity, not the initial "
                    "scoping negotiation."
                ),
            },
        ],
        "explanation": (
            "A dedicated re-run against previously reported critical findings, conducted after remediation, is a "
            "retest/validation activity distinct from reconnaissance, post-exploitation within the original "
            "engagement, or the initial rules-of-engagement negotiation."
        ),
    },
    {
        "id": "nd4g-033",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A penetration tester discovers that the built-in local Administrator account uses an IDENTICAL "
            "password across all 3,000 workstations in the environment. After compromising one workstation and "
            "extracting the local Administrator's password hash, the tester authenticates as local "
            "Administrator on hundreds of other workstations using pass-the-hash. Which control would MOST "
            "directly prevent this specific lateral movement technique?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploying a solution that randomizes and automatically rotates each computer's local Administrator password to a unique value, managed centrally",
                "correct": True,
                "rationale": (
                    "Correct. Making each workstation's local Administrator password unique and centrally "
                    "rotated (as with a local administrator password management solution) eliminates the value "
                    "of stealing one hash to authenticate anywhere else, directly stopping this lateral movement "
                    "path."
                ),
            },
            {
                "id": "b",
                "text": "Enforcing a longer minimum password length for the local Administrator account",
                "correct": False,
                "rationale": (
                    "Incorrect. Even a long, complex password remains vulnerable to pass-the-hash reuse across "
                    "every machine if the SAME password (and therefore the same hash) is shared by all "
                    "workstations."
                ),
            },
            {
                "id": "c",
                "text": "Disabling the local Administrator account on all workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. This may not be operationally feasible for local break-glass recovery scenarios "
                    "and does not address the root shared-credential problem if another shared privileged secret "
                    "still exists elsewhere."
                ),
            },
            {
                "id": "d",
                "text": "Requiring multifactor authentication for all domain administrator logins",
                "correct": False,
                "rationale": (
                    "Incorrect. This targets domain administrator authentication, not the local Administrator "
                    "pass-the-hash issue described, which occurs entirely against local accounts independent of "
                    "domain login MFA."
                ),
            },
        ],
        "explanation": (
            "Pass-the-hash lateral movement across many hosts is enabled specifically by password reuse; "
            "randomizing and centrally rotating each machine's local Administrator password removes the shared "
            "credential that made stealing one hash valuable everywhere."
        ),
    },
    {
        "id": "nd4g-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A security architecture requires that ALL SSH and RDP sessions to production servers first pass "
            "through a hardened, centrally monitored jump server (bastion host) that logs every keystroke, "
            "rather than allowing administrators to connect directly to production hosts from their "
            "workstations. What is the PRIMARY security benefit of routing all privileged access through this "
            "single chokepoint?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It creates a single, consistently monitored chokepoint for all privileged access, ensuring session recording and access control policies are uniformly enforced rather than bypassable through direct connections",
                "correct": True,
                "rationale": (
                    "Correct. By forcing every privileged session through one hardened path, the organization "
                    "guarantees consistent logging and policy enforcement instead of relying on each direct "
                    "connection being independently monitored and controlled."
                ),
            },
            {
                "id": "b",
                "text": "It eliminates the need for individual administrator accounts, since all access uses the bastion's shared identity",
                "correct": False,
                "rationale": (
                    "Incorrect. A bastion host does not remove individual accountability; administrators still "
                    "authenticate with their own identities as they pass through the chokepoint, preserving "
                    "attribution."
                ),
            },
            {
                "id": "c",
                "text": "It automatically encrypts data at rest on the production servers",
                "correct": False,
                "rationale": (
                    "Incorrect. A bastion host controls and monitors the access session path; it has no effect on "
                    "whether data stored on the destination servers is encrypted at rest."
                ),
            },
            {
                "id": "d",
                "text": "It removes the need for a PAM credential vault, since the bastion host manages all credentials directly",
                "correct": False,
                "rationale": (
                    "Incorrect. Bastion hosts and PAM vaults are typically complementary, not mutually "
                    "exclusive; a bastion controls the session path, while a vault manages and rotates the "
                    "underlying credentials — neither eliminates the need for the other."
                ),
            },
        ],
        "explanation": (
            "Routing all privileged access through a single, hardened bastion host ensures uniform session "
            "monitoring and policy enforcement, closing the gap left by administrators connecting directly and "
            "inconsistently to production systems."
        ),
    },
    {
        "id": "nd4g-035",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM generates two simultaneous 'malware detected' alerts of identical severity: one on a "
            "guest-network kiosk PC and one on the primary Active Directory domain controller. Both alerts are "
            "queued for triage in the order they arrived, causing the domain controller alert to wait 20 "
            "minutes behind the kiosk alert. Which SIEM enhancement would BEST prevent this from recurring?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integrating asset criticality/business-context data (e.g., from the CMDB) into SIEM alert scoring so alerts on high-value assets are prioritized above lower-value assets regardless of arrival order",
                "correct": True,
                "rationale": (
                    "Correct. Enriching alerts with asset criticality allows the SIEM to reorder triage priority "
                    "based on business impact rather than simple arrival time, ensuring the domain controller "
                    "alert is handled first."
                ),
            },
            {
                "id": "b",
                "text": "Increasing the SIEM's log retention period",
                "correct": False,
                "rationale": (
                    "Incorrect. Retention period affects how far back historical data can be queried; it has no "
                    "effect on how currently queued alerts are prioritized for triage."
                ),
            },
            {
                "id": "c",
                "text": "Reducing the number of correlation rules to decrease overall alert volume",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing rules could lower volume but risks losing detection coverage, and does "
                    "not itself introduce any logic to prioritize critical-asset alerts over lower-value ones."
                ),
            },
            {
                "id": "d",
                "text": "Requiring two analysts to review every alert before triage begins",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a second reviewer increases staffing overhead without addressing the "
                    "underlying issue that alerts are processed strictly by arrival order rather than by asset "
                    "importance."
                ),
            },
        ],
        "explanation": (
            "Risk-based alert triage requires enriching alerts with business context such as asset criticality "
            "so that high-value systems are prioritized ahead of lower-value ones, rather than processing purely "
            "in the order alerts arrive."
        ),
    },
    {
        "id": "nd4g-036",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC's SIEM correlation rules are built entirely around on-premises Windows Event Logs and "
            "firewall logs. An attacker compromises a user's credentials and logs into the organization's "
            "cloud-based email platform directly from an unfamiliar country, bypassing the corporate network and "
            "VPN entirely. The activity generates no SIEM alert. What is the MOST likely reason this activity "
            "went undetected?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SIEM was never configured to ingest and correlate cloud/SaaS identity provider sign-in logs, creating a visibility gap for authentication events that never traverse the on-premises network",
                "correct": True,
                "rationale": (
                    "Correct. Because the sign-in occurred entirely within the cloud platform and never touched "
                    "on-premises infrastructure, and the SIEM only ingests on-prem Windows and firewall logs, "
                    "there was no log source available to generate a correlation match or alert."
                ),
            },
            {
                "id": "b",
                "text": "The attacker used a zero-day exploit that no SIEM could ever detect",
                "correct": False,
                "rationale": (
                    "Incorrect. No exploit is described — the attacker simply logged in with valid stolen "
                    "credentials, a straightforward authentication event, not a novel technical exploit requiring "
                    "zero-day capability to detect."
                ),
            },
            {
                "id": "c",
                "text": "The SIEM's storage quota had been exceeded, causing new logs to be silently dropped",
                "correct": False,
                "rationale": (
                    "Incorrect. No such condition is described in the scenario; this is an unsupported assumption "
                    "rather than the identified cause of the missed detection."
                ),
            },
            {
                "id": "d",
                "text": "Multifactor authentication was not required for the account",
                "correct": False,
                "rationale": (
                    "Incorrect. While that may be a separate, valid concern, the question specifically asks why "
                    "the SIEM failed to alert — the root SIEM issue is the missing cloud log ingestion, a "
                    "different control layer than authentication policy."
                ),
            },
        ],
        "explanation": (
            "A SIEM can only correlate and alert on the log sources it ingests. Because cloud/SaaS identity "
            "provider sign-in logs were never connected, an entirely cloud-based authentication event created no "
            "visibility, regardless of MFA policy or exploit sophistication."
        ),
    },
    {
        "id": "nd4g-037",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability scanner flags a Linux server as vulnerable to a critical remote code execution CVE "
            "based solely on the installed package's version banner. Manual verification shows the distribution "
            "maintainers backported the security fix into that same version number without incrementing it, and "
            "the underlying vulnerable code path is already patched. What does this scenario illustrate, and "
            "what should the vulnerability management team do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This is a false positive caused by version-based detection; validate findings against the distribution vendor's patch tracking rather than relying on version strings alone, and document the finding as a false positive",
                "correct": True,
                "rationale": (
                    "Correct. Because the fix was backported without a version bump, the scanner's banner-based "
                    "check cannot distinguish patched from unpatched systems; validating against vendor advisory/"
                    "package-tracking data and documenting the false positive is the appropriate response."
                ),
            },
            {
                "id": "b",
                "text": "This is a true positive, and the server must be immediately patched again",
                "correct": False,
                "rationale": (
                    "Incorrect. The underlying vulnerable code path is already fixed; forcing a redundant patch "
                    "does not address the actual issue, which is the scanner's detection method producing a "
                    "false result."
                ),
            },
            {
                "id": "c",
                "text": "This proves credentialed scanning is inherently unreliable and should be discontinued",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an overgeneralized conclusion; the false positive stems from banner-based "
                    "version comparison, not from credentialed scanning as a methodology, which generally "
                    "improves accuracy over uncredentialed scanning."
                ),
            },
            {
                "id": "d",
                "text": "The scanner should be reconfigured to only perform uncredentialed scans going forward",
                "correct": False,
                "rationale": (
                    "Incorrect. Uncredentialed scans provide even less detail and accuracy than credentialed "
                    "scans; moving in that direction would not fix the version-banner false-positive issue and "
                    "would reduce overall detection quality."
                ),
            },
        ],
        "explanation": (
            "Version-banner-only detection cannot account for vendor backporting practices, producing false "
            "positives. The correct remediation is validating against actual patch-tracking data, not "
            "re-patching an already-fixed system or abandoning credentialed scanning."
        ),
    },
    {
        "id": "nd4g-038",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A monthly credentialed vulnerability scan of a Windows server segment reports zero critical "
            "findings for three consecutive months. During an unrelated audit, the security team discovers the "
            "scanning service account's password expired four months ago, causing every scan in that window to "
            "silently fall back to unauthenticated, external-only checks without raising any error in the scan "
            "summary. Which vulnerability management process gap MOST directly caused the false sense of "
            "security?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The lack of scan health/coverage validation — confirming successful authentication and expected result completeness for each scan run — allowed a silent degradation to go unnoticed",
                "correct": True,
                "rationale": (
                    "Correct. Without validating that each scan actually authenticated successfully and produced "
                    "expected coverage, a silent credential failure went undetected for months, creating false "
                    "assurance from incomplete, unauthenticated-only results."
                ),
            },
            {
                "id": "b",
                "text": "The scanning tool's vulnerability signature database was out of date",
                "correct": False,
                "rationale": (
                    "Incorrect. The described cause is a credential/authentication failure that degraded scan "
                    "depth, not stale vulnerability signatures; updating signatures would not have fixed the "
                    "silent authentication failure."
                ),
            },
            {
                "id": "c",
                "text": "The organization scanned too infrequently",
                "correct": False,
                "rationale": (
                    "Incorrect. Frequency was not the issue — even scanning daily during this window would have "
                    "produced the same incomplete, unauthenticated-only results because the scans were silently "
                    "failing to authenticate."
                ),
            },
            {
                "id": "d",
                "text": "CVSS scoring was miscalculated for the findings that were reported",
                "correct": False,
                "rationale": (
                    "Incorrect. The core problem is missing findings due to a coverage failure, not incorrect "
                    "scoring of findings that were actually reported."
                ),
            },
        ],
        "explanation": (
            "A silent credential failure caused scans to run in a degraded, unauthenticated mode without any "
            "error being surfaced. Validating scan health and coverage — not just reviewing reported findings — "
            "is necessary to catch this kind of silent degradation."
        ),
    },
    {
        "id": "nd4g-039",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "An external vulnerability scan finds TCP port 6379 (Redis) open and reachable from the internet on "
            "a cloud-hosted server, with no authentication password (requirepass) configured — the service's "
            "default state. Which risk is MOST directly associated with this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An unauthenticated remote attacker can connect directly to read, modify, or delete cached/session data, and in many configurations leverage Redis's scripting/replication features toward remote code execution on the host",
                "correct": True,
                "rationale": (
                    "Correct. With no authentication configured and the port exposed to the internet, anyone can "
                    "connect directly to Redis, access or destroy its data, and in many real-world "
                    "configurations abuse built-in features to escalate to code execution on the underlying host."
                ),
            },
            {
                "id": "b",
                "text": "The finding only affects availability, since Redis has no confidentiality-impacting data by design",
                "correct": False,
                "rationale": (
                    "Incorrect. Redis frequently caches session tokens, application state, or other sensitive "
                    "data; an unauthenticated attacker can read and exfiltrate this data, making confidentiality "
                    "impact very real, not merely availability."
                ),
            },
            {
                "id": "c",
                "text": "Because Redis operates over TLS by default, the exposure poses minimal risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Redis does not enable TLS by default; traffic and access are unencrypted and "
                    "unauthenticated unless explicitly configured, so this claim is false and understates the "
                    "risk."
                ),
            },
            {
                "id": "d",
                "text": "This is a false positive because Redis requires a valid client certificate for any connection by default",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no such default client-certificate requirement in Redis; out of the box, "
                    "it accepts unauthenticated connections unless requirepass or TLS client auth is explicitly "
                    "configured."
                ),
            },
        ],
        "explanation": (
            "An internet-exposed Redis instance with no authentication configured allows any remote attacker "
            "unauthenticated access to its data and, depending on configuration, a path toward remote code "
            "execution — Redis has neither authentication nor TLS enabled by default."
        ),
    },
    {
        "id": "nd4g-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A wireless security assessment of a small branch office recovers the WPA2 passphrase in under four "
            "hours despite a strong, complex 20-character passphrase being configured, because the access point "
            "has Wi-Fi Protected Setup (WPS) PIN entry enabled by default. Which finding BEST explains why the "
            "strong passphrase did not prevent this compromise?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The WPS PIN, which is split into two independently guessable halves, provides an attack path around the passphrase entirely, regardless of its strength",
                "correct": True,
                "rationale": (
                    "Correct. WPS PIN authentication has a well-known design flaw that lets an attacker brute-"
                    "force the PIN in two independently verifiable halves, recovering access (and often the "
                    "underlying passphrase) without ever attacking the passphrase itself."
                ),
            },
            {
                "id": "b",
                "text": "WPA2's 4-way handshake is inherently crackable within hours for any passphrase length",
                "correct": False,
                "rationale": (
                    "Incorrect. A sufficiently long, complex WPA2 passphrase resists practical offline dictionary/"
                    "brute-force attacks against the 4-way handshake; the rapid compromise here is explained by "
                    "the separate WPS PIN vulnerability, not a handshake weakness."
                ),
            },
            {
                "id": "c",
                "text": "The access point was using WEP encryption instead of WPA2",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states WPA2 was configured; the compromise path described "
                    "is through WPS, not a fallback to the much weaker WEP protocol."
                ),
            },
            {
                "id": "d",
                "text": "The SSID was left broadcasting, revealing the network's presence",
                "correct": False,
                "rationale": (
                    "Incorrect. Broadcasting the SSID only reveals the network's existence and name; it has no "
                    "bearing on how the passphrase itself was recovered through the WPS PIN weakness."
                ),
            },
        ],
        "explanation": (
            "WPS PIN authentication is vulnerable to a brute-force attack that recovers access independent of "
            "passphrase strength, because the 8-digit PIN can be guessed in two much smaller, separately "
            "verifiable halves — the fix is disabling WPS, not simply strengthening the passphrase."
        ),
    },
]
