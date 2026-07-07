"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file A."""

QUESTIONS = [
    {
        "id": "nd4a-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A hospital wants file server permissions to be granted automatically based on a combination of "
            "the requester's department, the sensitivity label of the file, the time of day, and whether the "
            "request originates from a managed device on the internal VLAN. Which access control model should "
            "the security architect implement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Attribute-based access control (ABAC)",
                "correct": True,
                "rationale": (
                    "Correct. ABAC evaluates multiple attributes (subject department, object sensitivity, "
                    "environmental context such as time and device posture) against policy rules in real time, "
                    "which is exactly the multi-factor, dynamic decision described here."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC grants access based solely on assigned role/department. It has no native "
                    "mechanism to also factor in time of day, device posture, or data sensitivity without "
                    "creating an unmanageable explosion of roles."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC enforces access using fixed classification/clearance labels set by a central "
                    "authority and is not designed to dynamically incorporate contextual attributes like time "
                    "of day or network location."
                ),
            },
            {
                "id": "d",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC lets the resource owner grant access at their discretion. It has no built-in "
                    "policy engine to evaluate contextual attributes, and it scales poorly for enterprise, "
                    "condition-driven decisions."
                ),
            },
        ],
        "explanation": (
            "ABAC (attribute-based access control) is the only listed model that natively supports policy "
            "decisions built from multiple simultaneous attributes: subject (department), object (sensitivity "
            "label), and environment (time, device posture/network). RBAC, MAC, and DAC each use a single "
            "primary criterion (role, classification label, or owner discretion, respectively)."
        ),
    },
    {
        "id": "nd4a-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "Select TWO statements that correctly distinguish role-based access control (RBAC) from "
            "attribute-based access control (ABAC) in an enterprise IAM deployment."
        ),
        "options": [
            {
                "id": "a",
                "text": "RBAC assigns permissions to a role and users inherit permissions by being assigned to that role.",
                "correct": True,
                "rationale": (
                    "Correct. This is the defining characteristic of RBAC: permissions are bound to roles, and "
                    "users acquire access transitively through role membership, simplifying administration."
                ),
            },
            {
                "id": "b",
                "text": "ABAC can incorporate contextual conditions such as time of day or device compliance state into the access decision.",
                "correct": True,
                "rationale": (
                    "Correct. ABAC policies evaluate subject, object, action, and environment attributes together, "
                    "so contextual conditions like time or device posture can be part of the same policy decision."
                ),
            },
            {
                "id": "c",
                "text": "RBAC natively evaluates real-time environmental conditions like geolocation before granting access.",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC's access decision is based on static role assignment; it does not natively "
                    "evaluate dynamic, real-time environmental conditions such as geolocation without extending "
                    "the model or bolting on additional controls."
                ),
            },
            {
                "id": "d",
                "text": "ABAC requires fewer total policies than RBAC in every deployment because it uses only one attribute per rule.",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC rules typically combine several attributes per policy, not one, and whether "
                    "ABAC results in fewer policies than RBAC depends on the organization's structure — it is not "
                    "guaranteed in every deployment."
                ),
            },
        ],
        "explanation": (
            "RBAC ties permissions to roles that users inherit; it is administratively simple but static. ABAC "
            "evaluates combinations of subject, resource, action, and environmental attributes dynamically, "
            "enabling context-aware decisions RBAC cannot natively make."
        ),
    },
    {
        "id": "nd4a-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "During a pre-production code review, a static analysis (SAST) tool flags a function that concatenates "
            "user-supplied input directly into a SQL query string. The development team argues the endpoint "
            "already sits behind a WAF that blocks common SQL injection signatures, so the finding should be "
            "closed as a false positive. What should the security analyst recommend instead?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Require the code be remediated using parameterized queries/prepared statements, since the WAF is a compensating control, not a fix for the underlying flaw.",
                "correct": True,
                "rationale": (
                    "Correct. A WAF provides defense-in-depth but relies on signature/pattern matching that novel "
                    "or obfuscated payloads can evade. The root cause — unsanitized input built into a query — "
                    "must be fixed at the source with parameterized queries."
                ),
            },
            {
                "id": "b",
                "text": "Accept the risk and close the finding because the WAF already blocks known SQL injection patterns.",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats a compensating control as a permanent substitute for secure coding. "
                    "WAF signatures can be bypassed with encoding or novel payloads, leaving the true "
                    "vulnerability unresolved."
                ),
            },
            {
                "id": "c",
                "text": "Move validation to a dynamic application security test (DAST) scan after deployment to confirm exploitability before acting.",
                "correct": False,
                "rationale": (
                    "Incorrect. DAST is useful for confirming exploitability in a running application, but the "
                    "flaw is already clearly identified in the source code; delaying remediation until after "
                    "deployment unnecessarily extends the exposure window."
                ),
            },
            {
                "id": "d",
                "text": "Add input length restrictions on the web form to limit the size of injected payloads.",
                "correct": False,
                "rationale": (
                    "Incorrect. Length limits do not prevent SQL injection; a malicious payload can be short. This "
                    "does not address the root cause of unsanitized input reaching the query."
                ),
            },
        ],
        "explanation": (
            "Secure coding practice requires fixing injection vulnerabilities at the source (parameterized "
            "queries/prepared statements or stored procedures with bound parameters). Perimeter controls like a "
            "WAF are compensating, defense-in-depth layers, not replacements for proper input handling."
        ),
    },
    {
        "id": "nd4a-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A development team wants to detect vulnerabilities in a running web application by sending crafted "
            "HTTP requests and observing the application's responses, without access to the source code. Which "
            "testing approach BEST fits this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dynamic application security testing (DAST)",
                "correct": True,
                "rationale": (
                    "Correct. DAST is a black-box technique that probes a running application from the outside "
                    "with crafted inputs, observing behavior/responses to identify vulnerabilities without "
                    "needing source code access."
                ),
            },
            {
                "id": "b",
                "text": "Static application security testing (SAST)",
                "correct": False,
                "rationale": (
                    "Incorrect. SAST analyzes source code, bytecode, or binaries at rest and requires access to "
                    "the codebase; it does not test a running application via external requests."
                ),
            },
            {
                "id": "c",
                "text": "Software composition analysis (SCA)",
                "correct": False,
                "rationale": (
                    "Incorrect. SCA inventories and analyzes third-party/open-source dependencies for known "
                    "vulnerable versions; it does not exercise the running application with crafted requests."
                ),
            },
            {
                "id": "d",
                "text": "Fuzz testing performed against locally compiled debug binaries",
                "correct": False,
                "rationale": (
                    "Incorrect. While fuzzing does send malformed input, this option specifically requires access "
                    "to locally compiled debug binaries, which contradicts the scenario's black-box, no-source-"
                    "access constraint that DAST satisfies directly."
                ),
            },
        ],
        "explanation": (
            "DAST tests an application in its running state from the outside (black-box), making it the correct "
            "choice when source code is unavailable and testing must rely on observing HTTP responses to "
            "crafted requests."
        ),
    },
    {
        "id": "nd4a-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "During an annual audit, the security team discovers 40 laptops in the CMDB that show no login "
            "activity, no patch compliance data, and no network traffic for over a year, yet remain marked as "
            "'active' and continue to consume software licenses. Which asset management practice would have "
            "MOST effectively prevented this issue from persisting undetected?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Periodic reconciliation of the CMDB against automated discovery scan results and license usage telemetry",
                "correct": True,
                "rationale": (
                    "Correct. Regularly reconciling inventory records against independent discovery data (network "
                    "scans, agent check-ins, license telemetry) is the control specifically designed to surface "
                    "'ghost assets' — devices recorded as active but no longer actually in use."
                ),
            },
            {
                "id": "b",
                "text": "Applying data classification labels to every asset record in the CMDB",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification labels describe data sensitivity, not asset liveness or usage "
                    "status; labeling records would not have revealed that the devices were stale."
                ),
            },
            {
                "id": "c",
                "text": "Enforcing a stricter password complexity policy on all managed endpoints",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity is an authentication control unrelated to detecting inactive "
                    "or unaccounted-for assets in inventory."
                ),
            },
            {
                "id": "d",
                "text": "Increasing the frequency of full-disk encryption key rotation on all corporate laptops",
                "correct": False,
                "rationale": (
                    "Incorrect. Key rotation cadence is a data-protection control and has no bearing on whether "
                    "stale, unused assets are identified and reconciled in the inventory system."
                ),
            },
        ],
        "explanation": (
            "Asset management maturity requires periodic reconciliation between the system of record (CMDB) and "
            "independent, automated ground truth (discovery scans, EDR check-ins, license/telemetry data) to "
            "catch ghost assets, unauthorized devices, and stale records before they become a hidden risk or "
            "wasted cost."
        ),
    },
    {
        "id": "nd4a-006",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOC wants to reduce mean time to respond to phishing reports submitted by employees. Whenever a "
            "user reports a suspicious email, the desired workflow is: automatically extract indicators, query "
            "threat intelligence feeds, search the mail gateway for other recipients, and quarantine matching "
            "messages — all without analyst intervention unless the confidence score is low. Which capability "
            "BEST accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A SOAR platform executing a predefined playbook",
                "correct": True,
                "rationale": (
                    "Correct. Security orchestration, automation, and response (SOAR) platforms are purpose-built "
                    "to chain multiple tools/APIs (threat intel lookups, mail gateway search, quarantine actions) "
                    "into a single automated playbook triggered by an event, escalating to a human only on low "
                    "confidence."
                ),
            },
            {
                "id": "b",
                "text": "A vulnerability scanner configured with an aggressive scan schedule",
                "correct": False,
                "rationale": (
                    "Incorrect. A vulnerability scanner identifies weaknesses in assets; it has no capability to "
                    "parse phishing reports, query threat intel, or quarantine email messages."
                ),
            },
            {
                "id": "c",
                "text": "A network access control (NAC) solution enforcing 802.1X authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. NAC controls device admission to the network based on authentication/posture; it "
                    "plays no role in email indicator extraction, threat intel enrichment, or mailbox remediation."
                ),
            },
            {
                "id": "d",
                "text": "A data loss prevention (DLP) agent deployed on all endpoints",
                "correct": False,
                "rationale": (
                    "Incorrect. DLP monitors and blocks sensitive data from leaving the organization; it does not "
                    "orchestrate multi-tool phishing response workflows."
                ),
            },
        ],
        "explanation": (
            "SOAR platforms combine orchestration (connecting disparate security tools), automation (executing "
            "repeatable steps without human input), and playbook-driven response — exactly the multi-step, "
            "cross-tool phishing triage workflow described, with conditional human escalation."
        ),
    },
    {
        "id": "nd4a-007",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "Which of the following is the GREATEST risk introduced specifically by automating incident response "
            "actions such as automatic host isolation and account disablement based on SIEM alert scores?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A poorly tuned correlation rule could trigger a false positive that automatically disables a critical production account or isolates a business-critical host.",
                "correct": True,
                "rationale": (
                    "Correct. Automation executes at machine speed without the judgment a human analyst would "
                    "apply; an untuned rule generating a false positive can cause immediate, wide-reaching "
                    "operational impact (an unplanned outage) before anyone can intervene."
                ),
            },
            {
                "id": "b",
                "text": "Automation always increases the mean time to detect (MTTD) because scripts run slower than manual review.",
                "correct": False,
                "rationale": (
                    "Incorrect. Automation typically decreases response time (MTTR), not increases detection "
                    "time; scripted actions execute far faster than manual analyst workflows."
                ),
            },
            {
                "id": "c",
                "text": "Playbooks eliminate the need for any human review of incidents going forward.",
                "correct": False,
                "rationale": (
                    "Incorrect. Well-designed automation still routes low-confidence or high-impact cases to "
                    "analysts; eliminating human review entirely is not an inherent property of automation, and "
                    "removing it is not the risk being described — the false-positive blast radius is."
                ),
            },
            {
                "id": "d",
                "text": "Automated playbooks cannot be logged or audited, making incidents impossible to reconstruct later.",
                "correct": False,
                "rationale": (
                    "Incorrect. SOAR platforms typically produce detailed execution logs of every automated "
                    "action, which supports auditing and post-incident review rather than preventing it."
                ),
            },
        ],
        "explanation": (
            "The core risk of security automation is that it removes human judgment from the loop, so a false "
            "positive or misconfigured rule can trigger disruptive containment actions (isolation, account "
            "disablement) instantly and at scale before anyone notices. Mitigations include staged rollouts, "
            "confidence thresholds, and human-in-the-loop approval for high-impact actions."
        ),
    },
    {
        "id": "nd4a-008",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic analyst arrives at a compromised server that is still powered on and connected to the "
            "network. Following the order of volatility, which artifact should be collected FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The contents of system RAM and active network connections",
                "correct": True,
                "rationale": (
                    "Correct. Per the order of volatility, RAM contents, running processes, and active network "
                    "connections are the most volatile data — they disappear the instant power is lost or the "
                    "state changes — so they must be captured first."
                ),
            },
            {
                "id": "b",
                "text": "A full bit-for-bit forensic image of the hard disk",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk contents are far less volatile than RAM and network state; while disk "
                    "imaging is essential, it should follow capture of volatile memory, not precede it."
                ),
            },
            {
                "id": "c",
                "text": "Archived log files stored on a separate backup server",
                "correct": False,
                "rationale": (
                    "Incorrect. Archived logs on a separate, already-persisted backup server are among the least "
                    "volatile data sources and are not at imminent risk of loss, so they are collected later."
                ),
            },
            {
                "id": "d",
                "text": "Printed physical documentation describing the server's configuration",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical paper documentation is static and not volatile at all; it has no urgency "
                    "in the order-of-volatility collection sequence."
                ),
            },
        ],
        "explanation": (
            "Order of volatility (from most to least volatile): CPU registers/cache, RAM (including running "
            "processes and network connections), swap/page files, disk data, remote logging/monitoring data, "
            "physical configuration/topology, and archival media. Volatile memory must always be captured before "
            "the system is powered down or disk imaging begins."
        ),
    },
    {
        "id": "nd4a-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "An analyst needs to acquire a forensic image of a suspect's hard drive for an internal investigation "
            "that may lead to legal action. Which action is MOST important to ensure the acquired evidence "
            "remains admissible and unaltered?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Connect the drive through a hardware write blocker before imaging and generate a cryptographic hash of the original and the image to verify integrity.",
                "correct": True,
                "rationale": (
                    "Correct. A write blocker physically/electronically prevents any write commands from "
                    "reaching the original media during acquisition, and comparing cryptographic hashes (e.g., "
                    "SHA-256) of the source and the image proves the copy is a bit-for-bit, unaltered duplicate."
                ),
            },
            {
                "id": "b",
                "text": "Boot the suspect drive directly in a workstation and copy the files needed for the investigation using the operating system's file explorer.",
                "correct": False,
                "rationale": (
                    "Incorrect. Booting the original drive or mounting it without write protection risks "
                    "modifying timestamps, metadata, and even file contents (e.g., via OS journaling), "
                    "compromising evidentiary integrity."
                ),
            },
            {
                "id": "c",
                "text": "Compress the drive contents into a password-protected archive to preserve confidentiality.",
                "correct": False,
                "rationale": (
                    "Incorrect. Compression and encryption for confidentiality do not establish or prove that the "
                    "acquisition process itself preserved the original evidence unaltered; this does not address "
                    "the integrity requirement."
                ),
            },
            {
                "id": "d",
                "text": "Have two analysts independently summarize the drive's contents in a written report.",
                "correct": False,
                "rationale": (
                    "Incorrect. Written summaries are not a substitute for a verified, hash-validated bit-for-bit "
                    "image; this does nothing to prevent alteration of the original media during acquisition."
                ),
            },
        ],
        "explanation": (
            "Forensically sound acquisition requires preventing any modification of original media (write "
            "blockers) and cryptographically proving the image matches the source (hashing). Without these "
            "controls, evidence integrity — and therefore admissibility — can be successfully challenged."
        ),
    },
    {
        "id": "nd4a-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A seized laptop is transferred from the incident responder to the forensic lab, then to outside "
            "counsel for review, and finally into long-term evidence storage. Weeks later, defense counsel "
            "challenges the integrity of the evidence. Which documentation gap would MOST likely support that "
            "challenge?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The chain-of-custody form is missing a signature and timestamp for the handoff between the forensic lab and outside counsel.",
                "correct": True,
                "rationale": (
                    "Correct. Chain of custody must document every transfer of evidence — who had it, when, and "
                    "why — without gaps. A missing signature/timestamp for one handoff creates an unaccounted-for "
                    "period during which tampering cannot be ruled out, undermining admissibility."
                ),
            },
            {
                "id": "b",
                "text": "The incident report narrative uses passive voice in several sentences.",
                "correct": False,
                "rationale": (
                    "Incorrect. Writing style/grammar in a report has no bearing on the legal integrity of "
                    "physical evidence custody and would not be grounds for challenging the evidence chain."
                ),
            },
            {
                "id": "c",
                "text": "The forensic analyst used an open-source imaging tool instead of a commercial one.",
                "correct": False,
                "rationale": (
                    "Incorrect. Tool licensing (open-source vs. commercial) does not by itself impair chain of "
                    "custody or evidence integrity, provided the tool is validated and produces a verifiable hash."
                ),
            },
            {
                "id": "d",
                "text": "The evidence bag used a tamper-evident seal with a visible barcode.",
                "correct": False,
                "rationale": (
                    "Incorrect. A tamper-evident seal with a tracked barcode is a best practice that strengthens, "
                    "rather than weakens, the custody trail — it is not a gap that would support a challenge."
                ),
            },
        ],
        "explanation": (
            "Chain of custody must record an unbroken, signed, timestamped log of every person who possessed the "
            "evidence and every transfer that occurred. Any undocumented gap in that chain creates reasonable "
            "doubt about whether the evidence could have been altered, which opposing counsel can use to "
            "challenge admissibility."
        ),
    },
    {
        "id": "nd4a-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A forensic examiner completes analysis on a disk image and later needs to prove in court that the "
            "working copy analyzed was not modified since acquisition. Which technique provides this proof?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Compare the cryptographic hash (e.g., SHA-256) of the working copy against the hash recorded at the time of acquisition.",
                "correct": True,
                "rationale": (
                    "Correct. A cryptographic hash acts as a unique fingerprint of the data. If the hash "
                    "calculated on the working copy still matches the hash recorded during acquisition, this "
                    "mathematically proves the data has not been altered."
                ),
            },
            {
                "id": "b",
                "text": "Rely on the tamper-evident seal on the original evidence bag, since it was never opened after acquisition.",
                "correct": False,
                "rationale": (
                    "Incorrect. The seal protects the physical original media, not the working copy that was "
                    "actively analyzed; it says nothing about whether the analyzed image itself remained unchanged."
                ),
            },
            {
                "id": "c",
                "text": "Present the signed chain-of-custody form documenting who possessed the evidence at each stage.",
                "correct": False,
                "rationale": (
                    "Incorrect. Chain of custody proves who handled the evidence and when, establishing "
                    "accountability, but it does not mathematically prove the bits of the working copy are "
                    "unchanged — hashing does that."
                ),
            },
            {
                "id": "d",
                "text": "Show that the analysis was performed on a forensic workstation not connected to the internet.",
                "correct": False,
                "rationale": (
                    "Incorrect. Air-gapping the workstation reduces the risk of remote tampering but is not proof "
                    "in itself that the specific working copy remains bit-for-bit identical to the original "
                    "acquisition; hash comparison is the direct evidentiary proof."
                ),
            },
        ],
        "explanation": (
            "Hashing is the definitive, mathematically verifiable method for proving data integrity across the "
            "forensic lifecycle. Chain-of-custody documentation and tamper-evident seals support the "
            "accountability trail, but only a matching hash value proves the analyzed data was never altered."
        ),
    },
    {
        "id": "nd4a-012",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "An EDR agent on a single workstation flags a suspicious PowerShell execution chain, but the analyst "
            "wants to also correlate that activity with email gateway logs, identity provider sign-in events, "
            "and firewall telemetry to determine whether the same actor moved across other systems. Which "
            "capability BEST supports this cross-domain correlation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Extended detection and response (XDR)",
                "correct": True,
                "rationale": (
                    "Correct. XDR ingests and correlates telemetry across multiple security domains — endpoint, "
                    "email, identity, network — into a unified detection view, which is precisely the cross-"
                    "domain correlation the analyst needs beyond a single endpoint agent."
                ),
            },
            {
                "id": "b",
                "text": "Endpoint detection and response (EDR) on the same workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. EDR's visibility is scoped to endpoint activity on the hosts where it is "
                    "installed; it does not natively ingest and correlate email, identity, and firewall telemetry "
                    "across the environment."
                ),
            },
            {
                "id": "c",
                "text": "Data loss prevention (DLP) policy enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. DLP focuses on detecting and blocking unauthorized movement of sensitive data; "
                    "it is not designed to correlate execution telemetry across endpoint, email, and identity "
                    "systems."
                ),
            },
            {
                "id": "d",
                "text": "A host-based intrusion prevention system (HIPS) on the affected workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. HIPS operates locally on a single host to block malicious activity in real time; "
                    "like standalone EDR, it lacks the multi-source correlation capability XDR provides."
                ),
            },
        ],
        "explanation": (
            "XDR extends beyond single-domain tools (EDR, DLP, HIPS) by aggregating and correlating telemetry "
            "from endpoint, email, identity, and network sources into unified detections, enabling analysts to "
            "trace an actor's activity across the full environment rather than one host in isolation."
        ),
    },
    {
        "id": "nd4a-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A finance employee attempts to upload a spreadsheet containing customer credit card numbers to a "
            "personal cloud storage account from a corporate laptop. The upload is automatically blocked and the "
            "security team receives an alert with the matched pattern. Which control produced this result?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An endpoint DLP agent enforcing a policy that detects and blocks PAN (primary account number) patterns leaving the device.",
                "correct": True,
                "rationale": (
                    "Correct. Endpoint DLP inspects data in use/in motion on the host, matches sensitive data "
                    "patterns such as credit card numbers (PAN), and can block the transfer while alerting the "
                    "security team — exactly the behavior described."
                ),
            },
            {
                "id": "b",
                "text": "An EDR agent detecting anomalous process behavior on the laptop.",
                "correct": False,
                "rationale": (
                    "Incorrect. EDR focuses on detecting malicious process/behavioral activity (e.g., malware, "
                    "living-off-the-land techniques), not on inspecting the content of a file for sensitive data "
                    "patterns like PANs."
                ),
            },
            {
                "id": "c",
                "text": "A network-based intrusion detection system (NIDS) signature match on the egress link.",
                "correct": False,
                "rationale": (
                    "Incorrect. NIDS is generally tuned to detect known attack signatures and traffic anomalies, "
                    "not to parse file content for structured sensitive data patterns like credit card numbers "
                    "unless specifically configured with DLP-like content inspection, which is not the standard "
                    "capability implied here."
                ),
            },
            {
                "id": "d",
                "text": "A vulnerability scanner performing an authenticated scan of the laptop.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scanners assess systems for known weaknesses and misconfigurations; "
                    "they do not monitor or block real-time data transfers based on content inspection."
                ),
            },
        ],
        "explanation": (
            "DLP solutions use content inspection (pattern matching, regex, fingerprinting) to identify sensitive "
            "data such as credit card numbers and enforce policies — block, quarantine, or alert — when that data "
            "attempts to leave the organization through unauthorized channels."
        ),
    },
    {
        "id": "nd4a-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company's DMARC record is published as 'v=DMARC1; p=none; rua=mailto:dmarc-reports@company.com'. "
            "Despite receiving daily aggregate reports showing spoofed messages failing SPF and DKIM checks, "
            "employees continue to receive spoofed emails claiming to be from the company's domain in their "
            "external partners' inboxes. What is the MOST likely reason spoofed mail is still being delivered?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The policy is set to 'p=none', which only requests monitoring/reporting and takes no enforcement action against failing messages.",
                "correct": True,
                "rationale": (
                    "Correct. A DMARC policy of 'p=none' explicitly tells receiving mail servers to take no "
                    "action on messages that fail alignment — it only enables reporting. Spoofed mail will "
                    "continue to be delivered until the policy is moved to 'quarantine' or 'reject'."
                ),
            },
            {
                "id": "b",
                "text": "SPF and DKIM records are not needed once a DMARC record is published.",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC relies on SPF and/or DKIM alignment to make its pass/fail determination; "
                    "without valid SPF and DKIM records, DMARC has no basis for evaluation. They remain required."
                ),
            },
            {
                "id": "c",
                "text": "The 'rua' tag should instead be configured as 'ruf' to enable enforcement instead of reporting.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'rua' and 'ruf' both control reporting (aggregate vs. forensic reports "
                    "respectively) — neither tag controls enforcement. Enforcement is controlled solely by the "
                    "'p=' policy tag."
                ),
            },
            {
                "id": "d",
                "text": "DMARC only applies to inbound mail the company receives, not mail claiming to be sent from its domain.",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC is specifically designed to let receiving mail servers validate whether "
                    "mail claiming to come from the publishing domain is legitimate — it protects against outbound "
                    "domain spoofing, which is the exact scenario described."
                ),
            },
        ],
        "explanation": (
            "DMARC has three policy levels: none (monitor only), quarantine (send to spam), and reject (block "
            "delivery). 'p=none' is commonly used during initial rollout to gather data safely, but it takes no "
            "enforcement action — spoofed mail keeps flowing until the policy is tightened to quarantine or reject."
        ),
    },
    {
        "id": "nd4a-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A security analyst is troubleshooting why legitimate marketing emails sent through a third-party "
            "ESP (email service provider) are being marked as spam. Select TWO true statements about SPF and "
            "DKIM that are relevant to diagnosing this issue."
        ),
        "options": [
            {
                "id": "a",
                "text": "SPF validates the envelope sender's IP address against a list of authorized sending hosts published in a DNS TXT record; if the ESP's sending IP is not included, SPF will fail.",
                "correct": True,
                "rationale": (
                    "Correct. SPF checks whether the connecting mail server's IP is authorized in the domain's "
                    "SPF record. If the third-party ESP's sending infrastructure was never added to that record, "
                    "SPF validation fails for messages sent through it."
                ),
            },
            {
                "id": "b",
                "text": "DKIM uses a private key held by the sending server to sign the message, and the receiver validates the signature using a public key published in DNS.",
                "correct": True,
                "rationale": (
                    "Correct. DKIM is a public-key cryptographic signature mechanism. If the ESP is not "
                    "configured to sign with a valid DKIM key matching the DNS-published public key, or the "
                    "message is altered in transit, DKIM validation fails."
                ),
            },
            {
                "id": "c",
                "text": "SPF verifies the message body has not been altered in transit using a digital signature.",
                "correct": False,
                "rationale": (
                    "Incorrect. That description applies to DKIM, not SPF. SPF only checks the sending IP address "
                    "against the authorized list; it does not sign or validate message content."
                ),
            },
            {
                "id": "d",
                "text": "DKIM validates the sending server's IP address against an authorized senders list in DNS.",
                "correct": False,
                "rationale": (
                    "Incorrect. That describes SPF, not DKIM. DKIM's mechanism is a cryptographic signature over "
                    "message headers/body, unrelated to IP address authorization."
                ),
            },
        ],
        "explanation": (
            "SPF authorizes sending IPs via a DNS TXT record; DKIM cryptographically signs the message using a "
            "private/public key pair validated through DNS. A common root cause for legitimate third-party mail "
            "failing checks is that the ESP's IPs were never added to the SPF record or the ESP was not "
            "configured to DKIM-sign on the customer's behalf."
        ),
    },
    {
        "id": "nd4a-016",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A SaaS application allows users to sign in with their corporate identity provider (IdP). After "
            "authenticating at the IdP, the user's browser is redirected back to the SaaS application with a "
            "signed XML document asserting the user's identity and group memberships. Which protocol is being "
            "used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SAML (Security Assertion Markup Language)",
                "correct": True,
                "rationale": (
                    "Correct. SAML uses XML-based assertions, digitally signed by the identity provider, that are "
                    "passed via the browser (typically through a redirect/POST binding) to the service provider "
                    "to convey authentication and attribute information — exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "OAuth 2.0",
                "correct": False,
                "rationale": (
                    "Incorrect. OAuth 2.0 is an authorization framework that issues access tokens (typically "
                    "JSON/JWT-based, not signed XML assertions) to grant delegated access to resources on a "
                    "user's behalf — it is not primarily an authentication assertion protocol."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos is a ticket-based authentication protocol used primarily within a single "
                    "trusted realm (e.g., Active Directory) using symmetric-key tickets, not signed XML browser "
                    "redirects to external SaaS applications."
                ),
            },
            {
                "id": "d",
                "text": "RADIUS",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS is an AAA protocol commonly used for network access (VPN, Wi-Fi, switch "
                    "authentication); it does not use browser-redirected signed XML assertions for web SSO."
                ),
            },
        ],
        "explanation": (
            "SAML is the standard for browser-based federated SSO, exchanging signed XML assertions between an "
            "identity provider and a service provider. OAuth is for delegated authorization (tokens/scopes), "
            "Kerberos is ticket-based for internal network authentication, and RADIUS is for network AAA."
        ),
    },
    {
        "id": "nd4a-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A third-party productivity app requests permission to read a user's calendar events and send "
            "meeting invites on their behalf, without ever seeing the user's corporate password. The user is "
            "redirected to the identity provider to approve specific scopes, after which the app receives a "
            "token limited to those scopes. Which mechanism is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OAuth 2.0 authorization with scoped access tokens",
                "correct": True,
                "rationale": (
                    "Correct. OAuth 2.0 is designed exactly for this: delegated, scoped authorization where a "
                    "third-party application receives a limited-privilege access token to act on a user's behalf "
                    "without ever handling the user's credentials."
                ),
            },
            {
                "id": "b",
                "text": "SAML assertion-based authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML is primarily used to assert identity/authentication for SSO login, not to "
                    "grant granular, scoped authorization to perform specific actions like reading calendar data "
                    "on a user's behalf."
                ),
            },
            {
                "id": "c",
                "text": "LDAP simple bind authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP simple bind directly validates a username/password against a directory "
                    "service; it does not provide scoped, token-based delegated authorization to third-party "
                    "applications."
                ),
            },
            {
                "id": "d",
                "text": "TACACS+ authentication and command authorization",
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ is used for device administration AAA (authenticating and authorizing "
                    "commands on network devices), not for consumer/SaaS delegated authorization scenarios like "
                    "calendar access."
                ),
            },
        ],
        "explanation": (
            "OAuth 2.0 is the delegated authorization framework: it issues scoped access tokens so a third-party "
            "application can act within defined permissions on a user's behalf without ever seeing the user's "
            "credentials. SAML addresses authentication/SSO, not scoped delegated authorization."
        ),
    },
    {
        "id": "nd4a-018",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A vulnerability scan of newly provisioned servers repeatedly finds the same set of unnecessary "
            "services enabled, default accounts left active, and inconsistent patch levels across the fleet, "
            "even though each server was manually configured following the same written procedure. Which "
            "solution would BEST prevent this recurring configuration drift?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Build and enforce a golden image/secure baseline template using configuration management tooling for all new deployments.",
                "correct": True,
                "rationale": (
                    "Correct. A golden image or automated baseline enforced through configuration management "
                    "(e.g., infrastructure as code) guarantees every server is provisioned identically and "
                    "consistently, eliminating the human error inherent in manual, procedure-based configuration."
                ),
            },
            {
                "id": "b",
                "text": "Require administrators to re-read the written hardening procedure before each deployment.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario already states each server was configured following the same "
                    "written procedure, yet drift still occurred — re-reading the same manual procedure does not "
                    "address the root cause of inconsistent, error-prone manual execution."
                ),
            },
            {
                "id": "c",
                "text": "Increase the frequency of vulnerability scans from monthly to weekly.",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent scanning improves detection speed but does not prevent the "
                    "misconfiguration from occurring in the first place — it only surfaces the same recurring "
                    "issue sooner."
                ),
            },
            {
                "id": "d",
                "text": "Disable vulnerability scanning on servers that pass their initial configuration review.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling ongoing scanning removes visibility into configuration drift entirely "
                    "and would make the problem harder to detect, not prevent."
                ),
            },
        ],
        "explanation": (
            "Manual, procedure-based hardening is error-prone and does not scale consistently. Golden images and "
            "automated configuration management enforce identical, repeatable secure baselines across the fleet, "
            "directly preventing the drift that manual processes allow."
        ),
    },
    {
        "id": "nd4a-019",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A security team wants an industry-standard, vendor-neutral checklist of specific configuration "
            "settings (e.g., disabling SMBv1, setting minimum password history, disabling guest accounts) to "
            "harden Windows Server against a recognized best-practice baseline. Which resource should they use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CIS Benchmarks",
                "correct": True,
                "rationale": (
                    "Correct. The Center for Internet Security (CIS) publishes detailed, vendor-neutral "
                    "configuration benchmarks for operating systems and applications, specifying exact settings "
                    "like disabling SMBv1 or guest accounts to establish a secure baseline."
                ),
            },
            {
                "id": "b",
                "text": "The CVSS scoring rubric",
                "correct": False,
                "rationale": (
                    "Incorrect. CVSS scores the severity of individual vulnerabilities; it is not a configuration "
                    "hardening checklist and provides no specific setting-level guidance."
                ),
            },
            {
                "id": "c",
                "text": "The MITRE ATT&CK matrix",
                "correct": False,
                "rationale": (
                    "Incorrect. ATT&CK catalogs adversary tactics and techniques for threat modeling and "
                    "detection engineering; it does not provide prescriptive OS hardening configuration settings."
                ),
            },
            {
                "id": "d",
                "text": "The organization's business impact analysis (BIA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BIA identifies critical processes and recovery objectives (RTO/RPO); it has no "
                    "content related to specific OS-level hardening configuration settings."
                ),
            },
        ],
        "explanation": (
            "CIS Benchmarks are the recognized industry standard for detailed, actionable secure configuration "
            "baselines across operating systems, cloud platforms, and applications. CVSS, ATT&CK, and BIA serve "
            "entirely different purposes (vulnerability scoring, threat modeling, and business continuity, "
            "respectively)."
        ),
    },
    {
        "id": "nd4a-020",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During an active ransomware incident, the IR team has already isolated the infected segment from "
            "the rest of the network to stop lateral spread. All affected servers remain powered on and "
            "isolated pending forensic imaging. According to the standard incident response lifecycle, what is "
            "the NEXT phase the team should perform?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Eradication — remove the malicious code, backdoors, and any persistence mechanisms from affected systems.",
                "correct": True,
                "rationale": (
                    "Correct. Containment (isolating the segment) has already been completed. The next phase in "
                    "the lifecycle is eradication: removing the malware, attacker persistence mechanisms, and "
                    "root cause from the affected systems before recovery begins."
                ),
            },
            {
                "id": "b",
                "text": "Recovery — restore the affected servers to production and reconnect them to the network.",
                "correct": False,
                "rationale": (
                    "Incorrect. Restoring systems to production before eradication is complete risks reintroducing "
                    "the same malware or leaving attacker persistence in place; recovery must follow, not precede, "
                    "eradication."
                ),
            },
            {
                "id": "c",
                "text": "Preparation — update the incident response plan and provision new tooling for future incidents.",
                "correct": False,
                "rationale": (
                    "Incorrect. Preparation is a pre-incident phase focused on readiness (plans, tools, training); "
                    "it is not the next step to take mid-incident after containment has occurred."
                ),
            },
            {
                "id": "d",
                "text": "Lessons learned — conduct a post-incident review meeting with stakeholders.",
                "correct": False,
                "rationale": (
                    "Incorrect. Lessons learned occurs after the incident is fully resolved (post-recovery); it "
                    "is premature while affected systems are still isolated awaiting cleanup."
                ),
            },
        ],
        "explanation": (
            "The standard IR lifecycle is: Preparation, Detection & Analysis, Containment, Eradication, "
            "Recovery, and Lessons Learned. After containment isolates the threat, eradication removes it "
            "(malware, backdoors, persistence) before systems are restored to production in the recovery phase."
        ),
    },
    {
        "id": "nd4a-021",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A SOC analyst confirms that a compromised workstation is actively beaconing to a known command-and-"
            "control server and attempting to authenticate to nearby file shares using stolen credentials. "
            "Select TWO actions that represent appropriate CONTAINMENT steps at this stage of the incident."
        ),
        "options": [
            {
                "id": "a",
                "text": "Disconnect or isolate the workstation from the network (e.g., via EDR network isolation) to stop further beaconing and lateral movement attempts.",
                "correct": True,
                "rationale": (
                    "Correct. Isolating the host is a textbook containment action — it stops the ongoing threat "
                    "from communicating with C2 infrastructure or spreading further while preserving the system "
                    "for forensic analysis."
                ),
            },
            {
                "id": "b",
                "text": "Disable or reset the credentials that are being used in the unauthorized authentication attempts.",
                "correct": True,
                "rationale": (
                    "Correct. Disabling the compromised/stolen credentials immediately stops the attacker from "
                    "successfully authenticating to other systems, containing the spread of the compromise while "
                    "investigation continues."
                ),
            },
            {
                "id": "c",
                "text": "Wipe and reimage the workstation from a known-good backup.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging is an eradication/recovery action, not containment, and performing it "
                    "before forensic evidence is captured would destroy volatile artifacts needed for root-cause "
                    "analysis."
                ),
            },
            {
                "id": "d",
                "text": "Conduct the post-incident lessons-learned review with all stakeholders.",
                "correct": False,
                "rationale": (
                    "Incorrect. Lessons learned occurs after the incident is fully resolved, not while the threat "
                    "is still active and containment is in progress."
                ),
            },
        ],
        "explanation": (
            "Containment focuses on stopping the immediate spread/impact without destroying evidence: isolating "
            "affected hosts and disabling compromised credentials/accounts. Reimaging (eradication/recovery) and "
            "lessons-learned reviews occur in later phases of the lifecycle."
        ),
    },
    {
        "id": "nd4a-022",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst needs to determine which internal host resolved a malicious domain name immediately "
            "before a workstation began communicating with a known-bad external IP address. Which log source "
            "will MOST directly answer this specific investigative question?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS server query logs",
                "correct": True,
                "rationale": (
                    "Correct. DNS query logs record which internal host requested resolution of which domain name "
                    "and when, directly answering the question of which host resolved the malicious domain before "
                    "the suspicious outbound connection began."
                ),
            },
            {
                "id": "b",
                "text": "Web application firewall (WAF) logs",
                "correct": False,
                "rationale": (
                    "Incorrect. WAF logs record HTTP requests/responses to and from web applications being "
                    "protected; they do not capture internal DNS resolution activity for arbitrary domain lookups."
                ),
            },
            {
                "id": "c",
                "text": "Endpoint antivirus signature-update logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus signature-update logs simply record when definition files were "
                    "downloaded and applied; they contain no information about DNS resolution or network "
                    "connections."
                ),
            },
            {
                "id": "d",
                "text": "Physical badge access logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Badge logs record physical entry/exit events at facility doors and have no "
                    "relevance to network-based DNS resolution or connections to external IP addresses."
                ),
            },
        ],
        "explanation": (
            "DNS logs are the authoritative source for mapping which internal host requested resolution of a "
            "given domain and when — critical for tracing the sequence from malicious domain lookup to the "
            "subsequent outbound connection. Firewall/NetFlow logs would corroborate the connection itself, but "
            "DNS logs answer 'who resolved what, and when' most directly."
        ),
    },
    {
        "id": "nd4a-023",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "During an investigation, an analyst wants to confirm exactly which files a specific user account "
            "opened, modified, or deleted on a shared file server over the past week, including successful and "
            "failed attempts. Which log source should the analyst prioritize?"
        ),
        "options": [
            {
                "id": "a",
                "text": "File server object access audit logs (e.g., Windows Security Event ID 4663/4656 or equivalent)",
                "correct": True,
                "rationale": (
                    "Correct. Object access auditing on the file server directly records which account performed "
                    "which action (open, modify, delete) on which specific files, including both successes and "
                    "failures — exactly what the investigation requires."
                ),
            },
            {
                "id": "b",
                "text": "Firewall connection logs showing source and destination IP addresses",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs show network-layer connection information (IPs, ports) but do not "
                    "capture file-level operations such as which specific file was opened, modified, or deleted."
                ),
            },
            {
                "id": "c",
                "text": "SIEM dashboard summarizing overall daily alert volume",
                "correct": False,
                "rationale": (
                    "Incorrect. An aggregate alert-volume dashboard provides a high-level trend view, not the "
                    "granular per-file, per-user access detail needed to answer this specific investigative "
                    "question."
                ),
            },
            {
                "id": "d",
                "text": "DHCP lease logs showing IP address assignments",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs only show which device received which IP address lease and when; they "
                    "provide no information about file-level access activity."
                ),
            },
        ],
        "explanation": (
            "To answer 'who did what to which file, and when,' the authoritative source is file/object access "
            "audit logging enabled on the file server itself. Network logs (firewall, DHCP) and aggregate SIEM "
            "dashboards lack the granular per-object detail required."
        ),
    },
    {
        "id": "nd4a-024",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "Antivirus scans on a compromised server find no malicious executable files on disk. However, "
            "process memory analysis reveals a malicious PowerShell script that was reflectively loaded into "
            "memory and executed entirely without writing any file to storage, and it disappears after a reboot. "
            "Which classification BEST describes this malware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fileless malware",
                "correct": True,
                "rationale": (
                    "Correct. Fileless malware operates entirely in memory (living-off-the-land techniques such "
                    "as malicious PowerShell/WMI), leaving no executable artifact on disk for traditional AV "
                    "signature scanning to detect, and typically does not persist across a reboot unless a "
                    "separate persistence mechanism is established."
                ),
            },
            {
                "id": "b",
                "text": "A rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit is designed to hide its presence and maintain persistent, privileged "
                    "access, typically via kernel or bootkit-level modification that does survive reboots — the "
                    "opposite of the memory-only, non-persistent behavior described here."
                ),
            },
            {
                "id": "c",
                "text": "A logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is dormant code that triggers a malicious action upon a specific "
                    "condition (date, event); it does not describe the memory-resident, no-disk-artifact execution "
                    "method observed here."
                ),
            },
            {
                "id": "d",
                "text": "A worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm is defined by its self-propagating ability to spread across networks "
                    "autonomously; the scenario describes execution method (memory-resident, no file) and does "
                    "not indicate self-replication/propagation behavior."
                ),
            },
        ],
        "explanation": (
            "Fileless malware executes directly in memory using legitimate system tools (PowerShell, WMI, "
            "scripting engines) without writing a malicious executable to disk, evading traditional signature-"
            "based antivirus and typically vanishing after a reboot unless separate persistence is added."
        ),
    },
    {
        "id": "nd4a-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A file server's contents are found encrypted, and endpoint logs across multiple hosts show a single "
            "executable spreading autonomously across the network overnight by exploiting an unpatched SMB "
            "service, with no user interaction required at any point. Which combination BEST classifies this "
            "malware's behavior and propagation method?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Ransomware with worm-like self-propagation",
                "correct": True,
                "rationale": (
                    "Correct. The impact (encrypting files) is consistent with ransomware, and the autonomous, "
                    "no-user-interaction spread across the network by exploiting a vulnerable service is the "
                    "defining characteristic of worm propagation — the two classifications describe payload and "
                    "spread mechanism, respectively."
                ),
            },
            {
                "id": "b",
                "text": "A trojan requiring the user to execute a disguised attachment",
                "correct": False,
                "rationale": (
                    "Incorrect. Trojans require the victim to be socially engineered into executing a disguised "
                    "program; the scenario explicitly states no user interaction was required, ruling out trojan "
                    "delivery."
                ),
            },
            {
                "id": "c",
                "text": "A logic bomb triggered by a specific calendar date",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no indication of a date/event-based trigger condition; the malware's "
                    "defining behavior here is autonomous network propagation via an exploited service, not a "
                    "dormant conditional trigger."
                ),
            },
            {
                "id": "d",
                "text": "Spyware collecting keystrokes for exfiltration",
                "correct": False,
                "rationale": (
                    "Incorrect. The observed impact is file encryption, not covert data collection; spyware's "
                    "goal is stealthy surveillance/exfiltration, not encrypting files for extortion."
                ),
            },
        ],
        "explanation": (
            "Classification often requires combining payload type (ransomware — encrypts data for extortion) "
            "with propagation method (worm — self-replicating, exploits a vulnerability without requiring user "
            "interaction, unlike a trojan which needs the victim to execute it)."
        ),
    },
    {
        "id": "nd4a-026",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A company allows employees to use personal smartphones for corporate email and file access, but "
            "wants to ensure that if a device is lost, only the corporate data and applications can be remotely "
            "wiped without affecting the employee's personal photos, contacts, and apps. Which MDM approach BEST "
            "meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy a containerization (application/data separation) solution that isolates corporate data in an encrypted profile, enabling a selective wipe of only that container.",
                "correct": True,
                "rationale": (
                    "Correct. Containerization creates a logically separated, encrypted corporate workspace on "
                    "the personal device. A selective/corporate wipe removes only that container's data and apps, "
                    "leaving personal content untouched — exactly the stated requirement."
                ),
            },
            {
                "id": "b",
                "text": "Enroll the device in full device supervision and perform a full factory reset if the device is lost.",
                "correct": False,
                "rationale": (
                    "Incorrect. A full factory/full wipe erases the entire device, including personal photos, "
                    "contacts, and apps — this violates the requirement to leave personal data untouched."
                ),
            },
            {
                "id": "c",
                "text": "Issue corporate-owned, business-only (COBO) devices to all employees instead of allowing personal devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. COBO changes the ownership model entirely (company-owned, no personal use) rather "
                    "than solving the stated BYOD requirement of separating corporate and personal data on the "
                    "employee's own personal device."
                ),
            },
            {
                "id": "d",
                "text": "Disable remote wipe capability entirely to avoid any risk to personal data.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling remote wipe entirely leaves corporate data permanently exposed on a "
                    "lost device with no remediation option, failing the security objective altogether."
                ),
            },
        ],
        "explanation": (
            "Containerization (application/data separation) is the standard MDM technique for BYOD environments, "
            "allowing a selective wipe of the corporate container only, preserving personal data — unlike a full "
            "wipe, which erases everything on the device."
        ),
    },
    {
        "id": "nd4a-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "An organization issues company-owned mobile devices that employees may also use for limited personal "
            "activities, such as personal email and social media, while IT retains full administrative control "
            "over the device, including the ability to install/remove any application. Which mobile deployment "
            "model does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Corporate-owned, personally enabled (COPE)",
                "correct": True,
                "rationale": (
                    "Correct. COPE describes company-owned devices that IT fully manages and controls while "
                    "permitting limited personal use — matching the scenario of full administrative control plus "
                    "allowed personal activities."
                ),
            },
            {
                "id": "b",
                "text": "Bring your own device (BYOD)",
                "correct": False,
                "rationale": (
                    "Incorrect. BYOD means the employee owns the device and IT typically has limited control, "
                    "often only over a containerized corporate workspace — not full administrative control over "
                    "the entire device as described."
                ),
            },
            {
                "id": "c",
                "text": "Choose your own device (CYOD) with no MDM enrollment",
                "correct": False,
                "rationale": (
                    "Incorrect. While CYOD lets employees select from an approved device list, this option "
                    "specifically states no MDM enrollment, which contradicts the scenario's requirement of full "
                    "IT administrative control over the device."
                ),
            },
            {
                "id": "d",
                "text": "Unmanaged personal device with a corporate VPN profile only",
                "correct": False,
                "rationale": (
                    "Incorrect. An unmanaged device with only a VPN profile provides no MDM administrative "
                    "control at all, which directly contradicts the scenario's requirement that IT retains full "
                    "control including app installation/removal."
                ),
            },
        ],
        "explanation": (
            "COPE devices are company-owned and fully managed by IT (full MDM control) while still permitting "
            "some personal use, distinguishing it from BYOD (employee-owned, limited IT control) and unmanaged "
            "deployments."
        ),
    },
    {
        "id": "nd4a-028",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "An employee reports receiving dozens of unexpected MFA push notification approval requests on their "
            "phone throughout the night, none of which they initiated. The employee did not approve any of them. "
            "What is this attack technique called, and what is the BEST immediate mitigation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This is MFA fatigue (push bombing); the immediate mitigation is to reset the compromised account's credentials and enable number-matching or require a manual code entry instead of a simple approve/deny push.",
                "correct": True,
                "rationale": (
                    "Correct. Repeated unsolicited push prompts hoping the victim eventually approves one out of "
                    "annoyance or confusion is the hallmark of MFA fatigue/push bombing. Because it indicates the "
                    "attacker already has valid credentials, the account password must be reset, and number-"
                    "matching MFA closes the gap that simple push-approval leaves open."
                ),
            },
            {
                "id": "b",
                "text": "This is a SIM-swapping attack; the mitigation is to contact the mobile carrier to reissue a new SIM card.",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping involves an attacker fraudulently porting the victim's phone number "
                    "to a device they control to intercept SMS codes — it does not match repeated push approval "
                    "prompts arriving on the victim's own working device."
                ),
            },
            {
                "id": "c",
                "text": "This is a pass-the-hash attack; the mitigation is to disable NTLM authentication across the domain.",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash involves reusing captured password hashes to authenticate without "
                    "knowing the plaintext password; it has no relationship to MFA push notifications being "
                    "repeatedly triggered."
                ),
            },
            {
                "id": "d",
                "text": "This is a replay attack; the mitigation is to shorten the validity window of session tokens.",
                "correct": False,
                "rationale": (
                    "Incorrect. A replay attack involves capturing and resending a legitimate authentication "
                    "message; the repeated unsolicited push prompts scenario is specifically MFA fatigue, not "
                    "token replay."
                ),
            },
        ],
        "explanation": (
            "MFA fatigue (push bombing) exploits simple approve/deny push notifications by bombarding the victim "
            "until they approve one by accident or frustration. Because the attacker already holds valid "
            "credentials, remediation requires a credential reset plus stronger MFA UX (number matching, phishing-"
            "resistant methods like FIDO2/WebAuthn) rather than relying on simple push approval alone."
        ),
    },
    {
        "id": "nd4a-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A bank requires customers to log in with a password and also insert a physical smart card that "
            "performs cryptographic challenge-response authentication with the bank's server. Which two "
            "authentication factor categories does this combination satisfy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Something you know (password) and something you have (smart card)",
                "correct": True,
                "rationale": (
                    "Correct. A password is knowledge-based ('something you know'), and a physical smart card "
                    "performing cryptographic authentication is possession-based ('something you have') — two "
                    "distinct factor categories, satisfying true multifactor authentication."
                ),
            },
            {
                "id": "b",
                "text": "Something you know (password) and something you are (smart card)",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Something you are' refers to inherence/biometric factors (fingerprint, iris, "
                    "facial recognition) — a smart card is a physical possession factor, not a biometric one."
                ),
            },
            {
                "id": "c",
                "text": "Something you have (password) and something you are (smart card)",
                "correct": False,
                "rationale": (
                    "Incorrect. This mislabels both factors: a password is knowledge-based, not possession-based, "
                    "and a smart card is possession-based, not biometric/inherence-based."
                ),
            },
            {
                "id": "d",
                "text": "Somewhere you are (password) and something you do (smart card)",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither factor described is location-based ('somewhere you are') or behavioral "
                    "('something you do'); the password is knowledge-based and the smart card is possession-based."
                ),
            },
        ],
        "explanation": (
            "The classic authentication factor categories are: something you know (password/PIN), something you "
            "have (token, smart card), something you are (biometric), somewhere you are (location), and "
            "something you do (behavioral). A password plus a physical smart card correctly combines knowledge "
            "and possession factors."
        ),
    },
    {
        "id": "nd4a-030",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "During an authorized penetration test, the tester has already gained an initial foothold on a "
            "workstation and now uses that access to enumerate the internal Active Directory environment, "
            "identify additional hosts, and harvest cached credentials to move to a domain controller. Which "
            "phase of the penetration testing process is being performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Lateral movement / privilege escalation during post-exploitation",
                "correct": True,
                "rationale": (
                    "Correct. Using an initial foothold to enumerate the internal environment, harvest "
                    "credentials, and pivot to additional systems (like a domain controller) is the defining "
                    "activity of the post-exploitation/lateral movement phase."
                ),
            },
            {
                "id": "b",
                "text": "Passive reconnaissance",
                "correct": False,
                "rationale": (
                    "Incorrect. Passive reconnaissance involves gathering information about the target without "
                    "directly interacting with its systems (e.g., OSINT); the scenario describes active, hands-on-"
                    "keyboard activity on already-compromised systems, well past the reconnaissance stage."
                ),
            },
            {
                "id": "c",
                "text": "Initial exploitation of the first vulnerable service",
                "correct": False,
                "rationale": (
                    "Incorrect. Initial exploitation is the act of gaining the first foothold; the scenario "
                    "states that foothold was already achieved and the tester is now operating from within the "
                    "network — this is a later phase."
                ),
            },
            {
                "id": "d",
                "text": "Reporting and remediation recommendations",
                "correct": False,
                "rationale": (
                    "Incorrect. Reporting occurs at the conclusion of testing after all technical activity is "
                    "complete; the scenario describes active technical exploitation still in progress."
                ),
            },
        ],
        "explanation": (
            "Standard penetration testing phases progress: reconnaissance, scanning/enumeration, exploitation "
            "(initial access), post-exploitation (privilege escalation, lateral movement, persistence), and "
            "reporting. Pivoting from an initial foothold to enumerate AD and harvest credentials for further "
            "access is textbook post-exploitation/lateral movement."
        ),
    },
    {
        "id": "nd4a-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "A penetration testing rules of engagement (RoE) document explicitly excludes any denial-of-service "
            "testing against production systems and requires the tester to immediately halt and notify the "
            "client if evidence of a prior, unrelated compromise is discovered. During testing, the tester finds "
            "an active backdoor left by a different, unknown threat actor. What should the tester do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Stop testing activity in that area and immediately notify the client per the rules of engagement, since this may indicate an active, unrelated compromise requiring incident response.",
                "correct": True,
                "rationale": (
                    "Correct. The RoE explicitly defines this exact scenario and requires immediate notification. "
                    "Continuing the engagement without alerting the client could allow an active threat actor's "
                    "access to persist or could contaminate evidence needed for a separate incident response "
                    "effort."
                ),
            },
            {
                "id": "b",
                "text": "Quietly remove the backdoor to protect the client, then continue the penetration test as planned.",
                "correct": False,
                "rationale": (
                    "Incorrect. Modifying or removing artifacts related to a potential unrelated incident without "
                    "authorization destroys evidence, exceeds the tester's authorized scope, and violates the "
                    "documented RoE requirement to notify the client."
                ),
            },
            {
                "id": "c",
                "text": "Document the finding in the final report and disclose it to the client only at the end-of-engagement debrief.",
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting until the final report delays notification of an active, potentially "
                    "ongoing compromise by a third party, directly violating the RoE's requirement for immediate "
                    "notification."
                ),
            },
            {
                "id": "d",
                "text": "Use the discovered backdoor to further test the depth of the existing compromise before reporting it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Leveraging an unknown, unauthorized backdoor left by another actor is outside the "
                    "tester's authorized scope and could constitute unauthorized access to a system already "
                    "controlled by a third party — a legal and ethical violation of the engagement's boundaries."
                ),
            },
        ],
        "explanation": (
            "Rules of engagement define legal and ethical boundaries for a penetration test, including required "
            "actions if unrelated compromise is found. Discovering evidence of an existing, unauthorized "
            "compromise by another actor requires immediate pause and client notification — testers must not "
            "further exploit, remove, or delay disclosure of such findings."
        ),
    },
    {
        "id": "nd4a-032",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A security review of a legacy file server finds that TCP port 23 is open and actively used by "
            "administrators to manage the device remotely. Which finding and remediation is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Port 23 is Telnet, which transmits credentials and session data in cleartext; it should be disabled and replaced with SSH (TCP 22).",
                "correct": True,
                "rationale": (
                    "Correct. TCP port 23 is the well-known Telnet port, which sends all traffic — including "
                    "authentication credentials — in cleartext. SSH provides encrypted remote administration and "
                    "is the standard secure replacement."
                ),
            },
            {
                "id": "b",
                "text": "Port 23 is SMTP relay traffic; it should be restricted to internal mail servers only.",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTP uses TCP port 25 (or 587 for submission), not port 23. This option "
                    "misidentifies the protocol/port pairing."
                ),
            },
            {
                "id": "c",
                "text": "Port 23 is RDP, which should be tunneled through a VPN before allowing remote access.",
                "correct": False,
                "rationale": (
                    "Incorrect. RDP uses TCP port 3389, not port 23. While tunneling remote administration "
                    "through a VPN is generally good practice, this option misidentifies the protocol on this "
                    "port."
                ),
            },
            {
                "id": "d",
                "text": "Port 23 is used by DNS zone transfers and should be restricted to authorized secondary name servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS zone transfers use TCP port 53, not port 23. This option misidentifies the "
                    "protocol/port pairing entirely."
                ),
            },
        ],
        "explanation": (
            "TCP port 23 is Telnet, a legacy remote administration protocol that transmits all data, including "
            "credentials, in cleartext. Best practice is to disable Telnet and use SSH (TCP 22), which encrypts "
            "the session end-to-end."
        ),
    },
    {
        "id": "nd4a-033",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A database administrator needs elevated 'sysadmin' privileges only twice a year to perform major "
            "version upgrades. The security team wants to eliminate the risk of that account holding standing "
            "administrative access year-round, while still enabling a fast, auditable elevation process when "
            "genuinely needed. Which PAM capability BEST satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Just-in-time (JIT) privileged access with time-bound approval workflows",
                "correct": True,
                "rationale": (
                    "Correct. JIT access grants elevated privileges only for a defined, temporary window after an "
                    "approval workflow, then automatically revokes them — eliminating standing privileged access "
                    "while still allowing fast, audited elevation when genuinely needed."
                ),
            },
            {
                "id": "b",
                "text": "Permanently assigning the sysadmin role to the account so upgrades never require a request process",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the exact standing-privilege problem the security team wants eliminated; "
                    "permanent elevated access year-round for an action needed twice a year maximizes the attack "
                    "surface and violates least privilege."
                ),
            },
            {
                "id": "c",
                "text": "Shared local administrator credentials distributed to the entire database team",
                "correct": False,
                "rationale": (
                    "Incorrect. Shared credentials eliminate individual accountability, prevent proper auditing "
                    "of who performed privileged actions, and are a PAM anti-pattern, not a solution."
                ),
            },
            {
                "id": "d",
                "text": "Disabling logging on the privileged account to reduce storage costs since it is rarely used",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling logging removes the auditability the security team explicitly wants "
                    "and increases risk rather than mitigating it — a rarely used privileged account should be "
                    "monitored more closely, not less."
                ),
            },
        ],
        "explanation": (
            "Just-in-time privileged access management grants temporary, approved, time-bound elevation for "
            "specific tasks and automatically revokes it afterward, directly addressing the standing-privilege "
            "risk while preserving a fast, auditable process for legitimate need."
        ),
    },
    {
        "id": "nd4a-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Auditors require proof of exactly which commands a third-party contractor executed during a "
            "privileged remote maintenance session on a production database server last month, since standard "
            "OS-level logging was insufficiently granular. Which PAM capability would have provided this level "
            "of detail?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Privileged session recording/monitoring through a PAM broker or jump host",
                "correct": True,
                "rationale": (
                    "Correct. PAM solutions can record or keystroke-log privileged sessions in full (video or "
                    "text-based command capture) when access is brokered through a jump host/vault, providing "
                    "exactly the granular, auditable evidence of every command executed."
                ),
            },
            {
                "id": "b",
                "text": "Password vaulting with automatic credential rotation after each use",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential rotation reduces the risk of credential reuse/theft but does not by "
                    "itself capture what commands were executed during the session — it addresses a different "
                    "control objective."
                ),
            },
            {
                "id": "c",
                "text": "Multifactor authentication required before the contractor's session begins",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA strengthens the login process and confirms identity at session start, but it "
                    "does not record or provide visibility into the specific commands run afterward."
                ),
            },
            {
                "id": "d",
                "text": "Role-based access control limiting the contractor to a read-only database role",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC restricts what the contractor is permitted to do, which is a preventive "
                    "control, but it does not generate a detailed record of the commands actually executed during "
                    "the session for after-the-fact audit."
                ),
            },
        ],
        "explanation": (
            "Session recording/monitoring (often via a PAM jump host or broker) captures the full detail of "
            "privileged sessions — keystrokes, commands, or video playback — providing the granular audit trail "
            "that basic OS logging, MFA, or RBAC alone cannot supply."
        ),
    },
    {
        "id": "nd4a-035",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM generates hundreds of alerts per day for 'failed login followed by successful login' events, "
            "which almost always turn out to be legitimate employees who mistyped their password once. Analysts "
            "are beginning to dismiss these alerts without investigation. Which action would BEST improve the "
            "SIEM's effectiveness without eliminating detection of genuine credential-based attacks?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tune the correlation rule to raise the failed-login threshold (e.g., 5+ failures in a short window) and add contextual conditions such as impossible travel or unfamiliar source IP before alerting.",
                "correct": True,
                "rationale": (
                    "Correct. Tuning the rule to require a more meaningful threshold and additional context (e.g., "
                    "geo-velocity, unfamiliar source, off-hours) reduces false positives from simple typos while "
                    "preserving detection of actual brute-force or credential-stuffing patterns."
                ),
            },
            {
                "id": "b",
                "text": "Disable the failed-login correlation rule entirely since it produces too many false positives.",
                "correct": False,
                "rationale": (
                    "Incorrect. Completely disabling the rule eliminates all detection of credential-based "
                    "attacks, including genuine brute-force attempts, trading alert fatigue for a dangerous "
                    "detection blind spot."
                ),
            },
            {
                "id": "c",
                "text": "Increase the SIEM's log retention period from 90 days to 365 days.",
                "correct": False,
                "rationale": (
                    "Incorrect. Retention period affects how far back historical data can be searched for "
                    "investigations and compliance; it has no effect on alert volume or false-positive rate for "
                    "this correlation rule."
                ),
            },
            {
                "id": "d",
                "text": "Route all failed-login alerts to a distribution list instead of the SOC ticketing queue.",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the notification destination does not reduce the number of false-"
                    "positive alerts generated or improve analyst efficiency; it just relocates the noise rather "
                    "than tuning the underlying detection logic."
                ),
            },
        ],
        "explanation": (
            "Effective SIEM tuning reduces false positives by adding thresholds and contextual enrichment "
            "(impossible travel, unfamiliar geolocation/ASN, time-of-day anomalies) to correlation rules, rather "
            "than disabling detections outright, which would create a dangerous coverage gap."
        ),
    },
    {
        "id": "nd4a-036",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM alert fires for 'unusual data transfer volume' from a finance server to an external IP "
            "address at 2 a.m. Select TWO actions that represent appropriate NEXT steps in the triage process "
            "before escalating the alert as a confirmed incident."
        ),
        "options": [
            {
                "id": "a",
                "text": "Correlate the alert with authentication logs, DLP alerts, and firewall/proxy logs to determine which account initiated the transfer and whether the destination is known-malicious.",
                "correct": True,
                "rationale": (
                    "Correct. Enriching and correlating the alert across multiple log sources establishes context "
                    "— who, what, and where — which is necessary to determine whether this is a false positive "
                    "(e.g., a scheduled backup job) or genuine data exfiltration before escalating."
                ),
            },
            {
                "id": "b",
                "text": "Check whether the transfer aligns with a known, scheduled business process, such as an automated nightly backup or batch job to an approved destination.",
                "correct": True,
                "rationale": (
                    "Correct. Confirming whether the activity matches an authorized, scheduled process is a "
                    "standard and necessary triage step to rule out a false positive before treating the alert as "
                    "a confirmed incident."
                ),
            },
            {
                "id": "c",
                "text": "Immediately notify the media and public relations team about a potential data breach.",
                "correct": False,
                "rationale": (
                    "Incorrect. Public communication is a late-stage action taken only after an incident is "
                    "confirmed and the organization's incident response and legal/communications plan determines "
                    "disclosure is required — it is premature during initial triage."
                ),
            },
            {
                "id": "d",
                "text": "Close the alert without further review since large transfers to external IPs are common in most environments.",
                "correct": False,
                "rationale": (
                    "Incorrect. Dismissing an anomalous, off-hours, high-volume transfer alert without any "
                    "investigation risks ignoring genuine data exfiltration; proper triage requires verification, "
                    "not assumption."
                ),
            },
        ],
        "explanation": (
            "Proper SIEM alert triage involves enriching the alert with correlated data from multiple sources "
            "and checking against known, authorized business activity before deciding whether to escalate. "
            "Premature public disclosure or reflexively closing the alert are both inappropriate at the triage "
            "stage."
        ),
    },
    {
        "id": "nd4a-037",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "Two vulnerabilities are found during a scan: Vulnerability A has a CVSS base score of 9.8 but "
            "affects an isolated, air-gapped test server with no sensitive data and no network connectivity. "
            "Vulnerability B has a CVSS base score of 6.5 but affects an internet-facing production payment "
            "processing server with a known, actively exploited proof-of-concept exploit in the wild. Which "
            "vulnerability should be prioritized for remediation FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Vulnerability B, because contextual factors — exposure, exploitability in the wild, and business criticality — outweigh a higher base CVSS score in an isolated, low-value system.",
                "correct": True,
                "rationale": (
                    "Correct. CVSS base score alone does not account for the asset's exposure, exploit "
                    "availability, or business impact. A lower-scored vulnerability on an internet-facing, "
                    "actively exploited, high-value system represents far greater real-world risk than a higher-"
                    "scored one on an isolated, low-value asset."
                ),
            },
            {
                "id": "b",
                "text": "Vulnerability A, because its CVSS base score of 9.8 is objectively higher and remediation should always follow the numeric base score ranking.",
                "correct": False,
                "rationale": (
                    "Incorrect. Blindly prioritizing by base score ignores environmental and temporal context "
                    "(exposure, exploit availability, asset criticality), which is exactly why CVSS provides "
                    "environmental and temporal metrics to adjust the base score for real-world risk."
                ),
            },
            {
                "id": "c",
                "text": "Both should be remediated simultaneously with equal priority regardless of context.",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk-based vulnerability management requires prioritization based on actual "
                    "exposure and impact; treating a critical internet-facing exploited system the same as an "
                    "isolated test server wastes limited remediation resources and delays addressing the greater "
                    "risk."
                ),
            },
            {
                "id": "d",
                "text": "Neither needs immediate remediation since both scores are below the organization's typical 'emergency' threshold of 10.0.",
                "correct": False,
                "rationale": (
                    "Incorrect. A CVSS score of 10.0 is the maximum possible value, not a meaningful threshold for "
                    "deprioritizing action; an actively exploited vulnerability on a production payment system "
                    "clearly warrants urgent remediation regardless of reaching a theoretical maximum score."
                ),
            },
        ],
        "explanation": (
            "Effective vulnerability management applies risk-based prioritization: CVSS base score is only one "
            "input. Environmental context (asset exposure, criticality, data sensitivity) and temporal factors "
            "(known exploit code, active exploitation) must be weighed together — a lower base score on an "
            "actively exploited, internet-facing, critical system outranks a higher base score on an isolated, "
            "low-value asset."
        ),
    },
    {
        "id": "nd4a-038",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability report lists a CVSS v3.1 vector of 'AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H'. Which "
            "interpretation of this vector is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The vulnerability is remotely exploitable over the network, requires low attack complexity, needs no privileges or user interaction, and results in high impact to confidentiality, integrity, and availability.",
                "correct": True,
                "rationale": (
                    "Correct. AV:N = network-exploitable, AC:L = low complexity, PR:N = no privileges required, "
                    "UI:N = no user interaction, S:U = scope unchanged, and C:H/I:H/A:H indicate high impact "
                    "across confidentiality, integrity, and availability — a highly critical, easily exploitable "
                    "remote vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "The vulnerability requires physical access to the device, administrative privileges, and user interaction to exploit.",
                "correct": False,
                "rationale": (
                    "Incorrect. AV:N indicates network-based (remote) attack vector, not physical access; PR:N "
                    "means no privileges are required; UI:N means no user interaction is required — this "
                    "interpretation contradicts every one of those metric values."
                ),
            },
            {
                "id": "c",
                "text": "The vulnerability only impacts availability and has no effect on data confidentiality or integrity.",
                "correct": False,
                "rationale": (
                    "Incorrect. All three impact metrics — C:H, I:H, and A:H — are rated High, meaning "
                    "confidentiality and integrity are equally and severely impacted alongside availability, not "
                    "just availability alone."
                ),
            },
            {
                "id": "d",
                "text": "The scope changed (S:U indicates the exploited component can impact resources beyond its own security scope).",
                "correct": False,
                "rationale": (
                    "Incorrect. 'S:U' means Scope Unchanged — the impact is confined to the vulnerable component's "
                    "own security scope. 'Scope Changed' would be denoted 'S:C', the opposite of what is shown in "
                    "this vector."
                ),
            },
        ],
        "explanation": (
            "Reading a CVSS v3.1 vector requires decoding each metric: AV (attack vector: N=network, A=adjacent, "
            "L=local, P=physical), AC (complexity: L/H), PR (privileges required: N/L/H), UI (user interaction: "
            "N/R), S (scope: U/C), and C/I/A (impact: N/L/H). This vector describes a maximally severe, remotely "
            "exploitable vulnerability requiring no privileges or user interaction."
        ),
    },
    {
        "id": "nd4a-039",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A retail company's guest Wi-Fi network still uses WPA2-PSK with a single shared passphrase posted "
            "on a sign in the lobby. A security assessment recommends migrating to WPA3-Personal specifically to "
            "address which weakness inherent in WPA2-PSK?"
        ),
        "options": [
            {
                "id": "a",
                "text": "WPA2-PSK is vulnerable to offline dictionary attacks against a captured four-way handshake; WPA3 uses Simultaneous Authentication of Equals (SAE) to resist offline password-guessing attacks.",
                "correct": True,
                "rationale": (
                    "Correct. WPA2-PSK's four-way handshake can be captured and attacked offline with dictionary/"
                    "brute-force tools. WPA3-Personal replaces the PSK exchange with SAE (Simultaneous "
                    "Authentication of Equals, based on Dragonfly), which is resistant to offline dictionary "
                    "attacks even against a weak shared passphrase."
                ),
            },
            {
                "id": "b",
                "text": "WPA2-PSK does not support AES encryption, so all traffic is transmitted in cleartext.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2 does support and typically use AES-CCMP encryption; the traffic is not "
                    "cleartext. The actual weakness being addressed is the offline-attackable handshake, not a "
                    "lack of encryption."
                ),
            },
            {
                "id": "c",
                "text": "WPA2-PSK cannot support more than 32 simultaneously connected client devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2-PSK client capacity is a function of the access point hardware, not a "
                    "protocol limitation, and this is not the reason a migration to WPA3 is recommended."
                ),
            },
            {
                "id": "d",
                "text": "WPA2-PSK requires a RADIUS server for every connecting client, increasing infrastructure cost.",
                "correct": False,
                "rationale": (
                    "Incorrect. PSK (pre-shared key) mode specifically does not require a RADIUS/AAA server — "
                    "that requirement applies to WPA2-Enterprise (802.1X), not WPA2-Personal/PSK."
                ),
            },
        ],
        "explanation": (
            "WPA2-PSK's four-way handshake can be captured over the air and attacked offline with dictionary/"
            "GPU-accelerated tools, especially against weak or shared passphrases like a lobby-posted sign. "
            "WPA3-Personal's SAE handshake is designed specifically to resist offline dictionary attacks, "
            "providing forward secrecy even if the passphrase is eventually guessed or compromised."
        ),
    },
    {
        "id": "nd4a-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A wireless intrusion detection system (WIDS) alerts on an access point broadcasting the corporate "
            "SSID with a stronger signal than the legitimate APs, but it is not listed in the wireless controller's "
            "inventory of managed access points. Several employees have already connected to it. What is the "
            "MOST likely explanation and appropriate immediate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This is a rogue/evil twin access point impersonating the corporate SSID; the WIDS/WIPS should be used to contain it (e.g., deauthenticate connected clients) while the team locates and physically removes the device.",
                "correct": True,
                "rationale": (
                    "Correct. An unmanaged AP broadcasting the legitimate SSID with a stronger signal to lure "
                    "clients is the classic definition of an evil twin/rogue AP attack. WIPS containment features "
                    "can disconnect clients from the rogue AP while the physical device is located and removed."
                ),
            },
            {
                "id": "b",
                "text": "This is expected behavior from a newly provisioned legitimate access point that has not yet synced with the controller's inventory; no action is needed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Assuming this is benign without verification is dangerous — a device broadcasting "
                    "the corporate SSID with employees actively connecting, yet absent from the managed inventory, "
                    "must be treated as a potential rogue AP until proven otherwise, not dismissed."
                ),
            },
            {
                "id": "c",
                "text": "This indicates a bluesnarfing attack against nearby mobile devices and should be addressed by disabling Bluetooth on all corporate phones.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing is a Bluetooth-specific attack unrelated to Wi-Fi access points and "
                    "SSIDs; disabling Bluetooth would have no effect on a rogue Wi-Fi access point broadcasting "
                    "the corporate SSID."
                ),
            },
            {
                "id": "d",
                "text": "This indicates a successful WPS PIN brute-force attack against a legitimate AP and requires disabling WPS on the wireless controller.",
                "correct": False,
                "rationale": (
                    "Incorrect. A WPS brute-force attack targets a legitimate AP's PIN mechanism; it would not "
                    "produce an unmanaged, unrecognized access point broadcasting a stronger signal outside the "
                    "controller's inventory — that scenario specifically describes a rogue/evil twin AP."
                ),
            },
        ],
        "explanation": (
            "An unmanaged access point broadcasting the legitimate SSID (often with a stronger signal to attract "
            "clients) is a rogue/evil twin access point. WIDS/WIPS solutions can detect and actively contain such "
            "devices (e.g., targeted deauthentication of connected clients) while the security team physically "
            "locates and removes the rogue hardware."
        ),
    },
]
