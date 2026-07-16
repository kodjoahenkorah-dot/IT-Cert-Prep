"""CompTIA Security+ SY0-701 practice questions — topical batch: vulnerability scan
interpretation, part 2.

Scenarios focus on reading and correctly interpreting vulnerability-scan output —
CVSS v3.1/v4.0 vector strings, scan dashboards, SCAP/CIS compliance reports, scanner
disagreements, false negatives, chained/aggregate findings, and SBOM/container scan
results — and translating that interpretation into the right vulnerability-management
action, SIEM correlation/alerting decision, or hardening/baseline remediation.
"""

QUESTIONS = [
    # ---------------------------------------------------------------
    # Vulnerability management & CVSS (24) — domain 4, objective 4.3
    # ---------------------------------------------------------------
    {
        "id": "tvul-001",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan of a building-automation controller reports CVSS v3.1 vector "
            "'AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H' (base score 8.8). An analyst unfamiliar with the "
            "vector assumes this is exploitable from anywhere on the internet, the same as an AV:N "
            "finding, and opens an emergency change request to firewall the controller off from the "
            "public internet. What correction should a peer reviewer make?"
        ),
        "options": [
            {
                "id": "a",
                "text": "AV:A (Adjacent) means the attacker must already have access to the same logically adjacent network segment (e.g., the same VLAN or broadcast/collision domain) — not the open internet — so the real question is whether an attacker could plausibly reach that adjacent segment, not whether the controller faces the public internet.",
                "correct": True,
                "rationale": (
                    "Correct. Attack Vector has four values: Network (N), Adjacent (A), Local (L), and "
                    "Physical (P). Adjacent requires the attacker to be on the same broadcast domain, "
                    "Bluetooth range, or similarly bounded local segment — a materially smaller exposure "
                    "than internet-wide reachability. The emergency response should instead evaluate whether "
                    "an attacker could gain a foothold on that adjacent segment (e.g., via a compromised "
                    "guest Wi-Fi bridged to the OT VLAN)."
                ),
            },
            {
                "id": "b",
                "text": "AV:A is simply an older CVSS v2 notation that means the same thing as AV:N in CVSS v3.1.",
                "correct": False,
                "rationale": (
                    "Incorrect. AV:A is a valid, distinct CVSS v3.1 metric value with its own meaning "
                    "(adjacent network); it is not a legacy alias for Network access, and the two produce "
                    "different exploitability sub-scores."
                ),
            },
            {
                "id": "c",
                "text": "AV:A means the attacker needs physical console access to the device.",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical access is represented by AV:P, a separate metric value. AV:A "
                    "specifically describes network-adjacent access, not hands-on-keyboard physical access."
                ),
            },
            {
                "id": "d",
                "text": "AV:A means the finding cannot be exploited remotely under any circumstance and should be closed as informational.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjacent-network exploitation is still a real remote attack path for anyone "
                    "who gains a foothold on the adjacent segment; downgrading it to informational ignores a "
                    "genuine, high-impact (C:H/I:H/A:H) vulnerability."
                ),
            },
        ],
        "explanation": (
            "Attack Vector (AV) in CVSS v3.1 has four distinct values — Network, Adjacent, Local, and "
            "Physical — each describing a different required attacker position. Misreading Adjacent as "
            "equivalent to Network-wide exposure leads to either misdirected internet-facing remediation "
            "effort or, in the opposite direction, dismissing a genuine local-segment risk."
        ),
    },
    {
        "id": "tvul-002",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A container-runtime finding shows CVSS v3.1 vector 'AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H' "
            "(base score 9.9) for a kernel vulnerability that allows a process inside a container to break "
            "out and affect the underlying host. A junior analyst argues the finding is overstated because "
            "'S:C' just means the scope of the CVE description is broad. What is the correct interpretation "
            "of the Scope metric here?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Scope Changed (S:C) means a successfully exploited vulnerability in one security authority (the container) can impact resources outside that authority (the host), which is exactly what a container-escape flaw does and is why it drives the score to near-maximum.",
                "correct": True,
                "rationale": (
                    "Correct. The Scope metric captures whether the impact of exploitation is confined to the "
                    "vulnerable component's own security scope (S:U) or extends beyond it into another "
                    "security authority (S:C). A container escape is the textbook example of Scope Changed: "
                    "the compromised component (the container) impacts a resource it should not control (the "
                    "host), which materially increases the base score."
                ),
            },
            {
                "id": "b",
                "text": "Scope refers to how many CVE databases have published the vulnerability, not to any technical impact boundary.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scope is a technical CVSS metric describing whether impact crosses a security "
                    "boundary; it has nothing to do with how many databases or vendors have published the "
                    "advisory."
                ),
            },
            {
                "id": "c",
                "text": "Scope Changed only applies to web applications and should not appear on an infrastructure/kernel-level finding like this one.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scope Changed applies whenever exploitation crosses a security authority "
                    "boundary, which is common in virtualization/container escapes, sandbox breakouts, and "
                    "similar infrastructure-level flaws — not limited to web applications."
                ),
            },
            {
                "id": "d",
                "text": "Scope Changed lowers the severity compared to Scope Unchanged because it spreads impact across more systems, diluting the risk to any single one.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scope Changed increases severity relative to an otherwise identical Scope "
                    "Unchanged finding, because the ability to affect resources beyond the vulnerable "
                    "component's own boundary represents a more dangerous, broader-impact vulnerability."
                ),
            },
        ],
        "explanation": (
            "The CVSS Scope metric distinguishes vulnerabilities whose impact stays inside the vulnerable "
            "component (S:U) from those that let an attacker affect resources under a different security "
            "authority (S:C), such as a container escaping to the host. Scope Changed findings deserve "
            "elevated urgency because containment boundaries the organization relied on are the thing that "
            "actually fails."
        ),
    },
    {
        "id": "tvul-003",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A hospital's weekly scan returns:\n\n"
            "Host              CVE              CVSS   Exposure                                   Notes\n"
            "imaging-pacs-04    CVE-2026-1120    8.1    Internal clinical VLAN, no internet route   No known exploit\n"
            "portal-web-02      CVE-2026-1144    6.8    Internet-facing patient portal              Added to CISA KEV two days ago\n"
            "lab-results-09     CVE-2026-1160    9.0    Internal-only, reachable from staff Wi-Fi    Proof-of-concept published, not seen in the wild\n"
            "backup-srv-03      CVE-2026-1177    5.4    Internal, isolated backup VLAN, no user traffic   No known exploit\n\n"
            "The team can only work one emergency out-of-cycle patch tonight. Which host should be patched?"
        ),
        "options": [
            {
                "id": "a",
                "text": "portal-web-02, because it is internet-facing and its CVE was just added to the CISA Known Exploited Vulnerabilities catalog",
                "correct": True,
                "rationale": (
                    "Correct. A KEV listing confirms real-world active exploitation, and this finding is also "
                    "directly reachable from the internet. That combination of confirmed exploitation plus "
                    "internet exposure outranks every other finding here regardless of their higher base CVSS "
                    "scores."
                ),
            },
            {
                "id": "b",
                "text": "lab-results-09, because it has the highest CVSS base score of the four findings",
                "correct": False,
                "rationale": (
                    "Incorrect. This finding only has a published proof-of-concept, not confirmed active "
                    "exploitation, and it is reachable only from internal staff Wi-Fi rather than the open "
                    "internet — a smaller realistic attack surface than the KEV-listed internet-facing finding."
                ),
            },
            {
                "id": "c",
                "text": "imaging-pacs-04, because clinical imaging systems are always the highest-priority asset class in a hospital",
                "correct": False,
                "rationale": (
                    "Incorrect. Asset criticality matters, but this finding has no internet route and no known "
                    "exploit; treating asset class alone as an automatic override ignores the far more urgent "
                    "active-exploitation signal on the patient portal."
                ),
            },
            {
                "id": "d",
                "text": "backup-srv-03, because backup infrastructure compromise would be catastrophic if it ever happened",
                "correct": False,
                "rationale": (
                    "Incorrect. This finding has the lowest CVSS score, no known exploit, and sits on an "
                    "isolated VLAN with no user traffic — the lowest realistic risk of the four findings "
                    "tonight, despite backups being important in the abstract."
                ),
            },
        ],
        "explanation": (
            "Real-world prioritization weighs confirmed exploitation (CISA KEV) and exposure ahead of raw "
            "CVSS base score or generic asset-class assumptions. An actively exploited, internet-reachable "
            "finding must be remediated before higher-scoring but internally isolated, unexploited findings."
        ),
    },
    {
        "id": "tvul-004",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "Two scanners are run against the same host for the same underlying flaw. Scanner A (using the "
            "vendor-published CVSS v3.1 base score) reports CVE-2026-2201 as 'High, 7.8.' Scanner B, using a "
            "proprietary severity model that also factors in the scanner vendor's own exploit telemetry, "
            "reports the same CVE as 'Critical.' Which action should the analyst take to reconcile the "
            "discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Record both severities in the finding's documentation along with the scoring methodology behind each, and use the higher, more risk-informed rating to drive prioritization unless investigation shows the proprietary model overstated the risk.",
                "correct": True,
                "rationale": (
                    "Correct. Different tools can legitimately produce different severities because they use "
                    "different inputs (static base score vs. a model incorporating live exploit telemetry). "
                    "The correct response is transparency — document both scores and their basis — and default "
                    "toward the more conservative (higher-risk) rating unless there is a documented reason to "
                    "discount it, rather than picking one number arbitrarily."
                ),
            },
            {
                "id": "b",
                "text": "Always trust the vendor-published CVSS base score over any scanner's proprietary rating, since NVD is the sole authoritative source and all other scores should be discarded.",
                "correct": False,
                "rationale": (
                    "Incorrect. A scanner's proprietary model that incorporates live exploit telemetry can add "
                    "real, current risk signal beyond the static NVD base score; automatically discarding it "
                    "throws away potentially important information rather than reconciling it."
                ),
            },
            {
                "id": "c",
                "text": "Average the two severities into a single blended numeric score for reporting purposes.",
                "correct": False,
                "rationale": (
                    "Incorrect. The two ratings are not comparable numeric quantities on the same scale in a "
                    "way that makes averaging meaningful; blending them produces a number without a clear "
                    "interpretation and can mask the more urgent of the two signals."
                ),
            },
            {
                "id": "d",
                "text": "Uninstall Scanner B since two tools reporting different results indicates one of them is malfunctioning.",
                "correct": False,
                "rationale": (
                    "Incorrect. Differing severity models are expected behavior between tools with different "
                    "methodologies, not evidence of a malfunction; removing a scanning tool over this "
                    "discrepancy discards a legitimate data source rather than investigating the difference."
                ),
            },
        ],
        "explanation": (
            "Vulnerability scanners can legitimately disagree because they use different scoring inputs "
            "(static published base score vs. a model enriched with live exploit telemetry). Good practice is "
            "to document the methodology behind each rating and default toward the more conservative severity "
            "for prioritization, rather than blindly trusting one source or averaging incompatible numbers."
        ),
    },
    {
        "id": "tvul-005",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability management dashboard shows the count of critical findings jumped from 12 to 96 "
            "overnight. Investigation shows the spike coincides exactly with 80 new virtual machines being "
            "provisioned for a cloud migration project the previous evening. What is the MOST likely "
            "explanation and correct response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The newly provisioned VMs were built from an outdated image and were not yet enrolled in the patch management cycle before their first scan; the team should confirm the image source, patch or replace it, and add automated patch/baseline enrollment to the provisioning pipeline before the next batch goes live.",
                "correct": True,
                "rationale": (
                    "Correct. A spike that exactly tracks a bulk-provisioning event strongly indicates the new "
                    "hosts were deployed from a stale template or bypassed the normal patch/baseline "
                    "enrollment step, not that 80 genuinely new distinct critical flaws suddenly appeared. The "
                    "fix addresses both the immediate finding and the pipeline gap that will keep repeating it."
                ),
            },
            {
                "id": "b",
                "text": "The scanner is malfunctioning and duplicating findings; the scan schedule should be paused until the vendor confirms a bug fix.",
                "correct": False,
                "rationale": (
                    "Incorrect. A count increase that precisely lines up with 80 newly deployed hosts is far "
                    "more consistent with those specific hosts genuinely being unpatched than with a scanner "
                    "bug, and jumping to that conclusion without checking the new hosts' patch state skips the "
                    "obvious, easily verifiable explanation."
                ),
            },
            {
                "id": "c",
                "text": "This is normal and requires no investigation, since any large infrastructure change is expected to increase the finding count proportionally.",
                "correct": False,
                "rationale": (
                    "Incorrect. Treating a large, sudden spike as automatically 'normal' without investigating "
                    "the root cause (a stale provisioning image) misses the opportunity to fix the underlying "
                    "process gap before the next batch of hosts is deployed the same way."
                ),
            },
            {
                "id": "d",
                "text": "Exclude the new VMs from future vulnerability scans until the migration project formally closes, to keep the dashboard numbers stable.",
                "correct": False,
                "rationale": (
                    "Incorrect. Excluding genuinely vulnerable, newly deployed production hosts from scanning "
                    "to keep a dashboard metric looking stable hides real risk rather than addressing it."
                ),
            },
        ],
        "explanation": (
            "A finding-count spike that precisely correlates with a bulk deployment event almost always points "
            "to a stale provisioning image or a gap in the onboarding pipeline (patch/baseline enrollment), "
            "not a sudden wave of unrelated new vulnerabilities or a scanner defect. Correcting the pipeline "
            "prevents the same spike from recurring with the next deployment batch."
        ),
    },
    {
        "id": "tvul-006",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "During a penetration test, the tester achieves remote code execution against an internally "
            "developed HR application through a deserialization flaw in a custom API endpoint. The most "
            "recent authenticated vulnerability scan of the same host, run one week prior, reported no "
            "findings for that endpoint at all. What is the MOST likely explanation for this false negative?"
        ),
        "options": [
            {
                "id": "a",
                "text": "General-purpose vulnerability scanners rely on plugins/signatures built primarily for known CVEs in commercial and open-source software; a deserialization flaw unique to custom, in-house application logic has no corresponding CVE or plugin for the scanner to detect.",
                "correct": True,
                "rationale": (
                    "Correct. Vulnerability scanners are strongest at detecting known, catalogued vulnerabilities "
                    "(CVEs) in commercial or widely used open-source components. A logic flaw unique to a "
                    "custom-built API has no published CVE or scanner signature, so it falls into the "
                    "coverage gap that application-layer testing (SAST/DAST/manual pen testing) is specifically "
                    "designed to close."
                ),
            },
            {
                "id": "b",
                "text": "The vulnerability scan must have been run against the wrong host entirely.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no evidence of a targeting error; the far more common and likely "
                    "explanation is simply that generic scanners cannot detect custom application logic flaws "
                    "that have no associated CVE or signature."
                ),
            },
            {
                "id": "c",
                "text": "The penetration tester must have fabricated the finding, since a credentialed scan the week before found nothing.",
                "correct": False,
                "rationale": (
                    "Incorrect. Assuming the more thorough, hands-on testing result is fraudulent rather than "
                    "recognizing a known and well-documented limitation of automated scanning is the wrong "
                    "conclusion and undermines legitimate pen-test findings."
                ),
            },
            {
                "id": "d",
                "text": "Deserialization flaws cannot be exploited remotely, so the scanner correctly excluded it from its results.",
                "correct": False,
                "rationale": (
                    "Incorrect. Deserialization vulnerabilities are a well-known and frequently remotely "
                    "exploitable class of flaw (commonly leading to remote code execution); the scanner's "
                    "silence reflects a coverage gap, not a legitimate exclusion."
                ),
            },
        ],
        "explanation": (
            "Automated vulnerability scanners are built around known-CVE and configuration-signature "
            "detection and generally cannot find logic flaws unique to custom application code. Programs that "
            "rely solely on scan results for custom-developed applications should supplement them with "
            "SAST/DAST and periodic manual testing to close this coverage gap."
        ),
    },
    {
        "id": "tvul-007",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vendor advisory and active threat-intelligence reporting confirm a new, actively exploited "
            "remote code execution flaw in a widely used VPN client, but the CVE record is still marked "
            "'RESERVED' with no CVSS score published yet, and the organization's scanner has no plugin for it. "
            "What should the vulnerability management team do while waiting for an official CVSS score and "
            "scanner coverage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Treat it as a high-urgency interim risk based on the vendor advisory and threat-intel confirmation of active exploitation, manually inventory which hosts run the affected client version, and apply available compensating controls (e.g., blocking the known exploit indicators at the network boundary) without waiting for a CVSS number or scanner update.",
                "correct": True,
                "rationale": (
                    "Correct. A missing CVSS score or scanner plugin does not mean a vulnerability is not "
                    "urgent — it means the formal tracking apparatus hasn't caught up yet. Confirmed active "
                    "exploitation from vendor and threat-intel sources is itself sufficient justification for "
                    "manual inventory and interim compensating controls while the CVE record and scanner "
                    "coverage catch up."
                ),
            },
            {
                "id": "b",
                "text": "Take no action until the CVE record is finalized with an official CVSS base score, since prioritization requires a numeric score.",
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting for a formal score while active exploitation is already confirmed by "
                    "the vendor and threat intelligence leaves the organization exposed during exactly the "
                    "window when action is most needed."
                ),
            },
            {
                "id": "c",
                "text": "Wait for the scanner vendor to release a detection plugin before taking any inventory or mitigation steps, since manual processes are considered unreliable.",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual inventory and compensating controls are standard, reliable interim "
                    "practices used specifically to bridge the gap before automated scanner coverage exists; "
                    "waiting idly for tooling to catch up is not appropriate for an actively exploited flaw."
                ),
            },
            {
                "id": "d",
                "text": "Disregard the vendor advisory since no CVE has been fully published yet, and rely solely on the next scheduled scan cycle to eventually surface the issue.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vendor advisories and confirmed threat-intelligence reporting are legitimate, "
                    "actionable sources independent of CVE publication status; ignoring them until the next "
                    "scan cycle needlessly delays response to a confirmed active threat."
                ),
            },
        ],
        "explanation": (
            "Vulnerability identification is not limited to scanner output — vendor advisories, threat "
            "intelligence, and responsible-disclosure reporting are equally valid identification methods and "
            "can indicate urgency well before a CVE record is finalized or a scanner plugin exists."
        ),
    },
    {
        "id": "tvul-008",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scanner supporting CVSS v4.0 flags CVE-2026-3050 with Attack Requirements (AT) rated 'Present' "
            "and a high Vulnerable System impact but low Subsequent System impact. A colleague who has only "
            "worked with CVSS v3.1 asks what these newer metrics mean. Which explanation is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Attack Requirements (AT) captures conditions beyond attacker privileges/interaction that must exist for exploitation (e.g., a race condition or specific configuration state) — 'Present' means such conditions are needed; the Vulnerable System vs. Subsequent System split separately scores impact to the flawed component itself versus impact to other systems it can reach, replacing v3.1's single Scope metric with finer-grained detail.",
                "correct": True,
                "rationale": (
                    "Correct. CVSS v4.0 introduced Attack Requirements as a new exploitability metric "
                    "capturing deployment/execution conditions beyond privileges and user interaction, and "
                    "replaced the binary Scope metric with separate Vulnerable System (VC/VI/VA) and Subsequent "
                    "System (SC/SI/SA) impact metrics, giving more granular visibility into where the damage "
                    "actually lands."
                ),
            },
            {
                "id": "b",
                "text": "Attack Requirements is just a renamed version of Attack Complexity from CVSS v3.1 with no functional difference.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVSS v4.0 retains Attack Complexity (AC) as its own metric alongside the new "
                    "Attack Requirements (AT) metric; they are separate, non-overlapping concepts, not a "
                    "rename."
                ),
            },
            {
                "id": "c",
                "text": "Subsequent System impact refers to how the score will change in a future revision of the CVE record, not to any technical impact on other systems.",
                "correct": False,
                "rationale": (
                    "Incorrect. Subsequent System impact is a present-tense technical metric describing damage "
                    "to systems beyond the vulnerable component itself (analogous to what Scope Changed implied "
                    "in v3.1), not a forecast of future score revisions."
                ),
            },
            {
                "id": "d",
                "text": "CVSS v4.0 removed impact scoring entirely and now rates vulnerabilities purely on exploitability.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVSS v4.0 still scores impact — in fact with more granularity than v3.1, "
                    "splitting it into Vulnerable System and Subsequent System impact rather than removing it."
                ),
            },
        ],
        "explanation": (
            "CVSS v4.0 refines the exploitability and impact model used in v3.1: Attack Requirements adds a "
            "new metric for environmental/execution preconditions, and the single Scope metric is replaced by "
            "separately scored Vulnerable System and Subsequent System impact, giving analysts more precise "
            "insight into blast radius when reading modern scan output."
        ),
    },
    {
        "id": "tvul-009",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan of app-srv-19 lists the same CVE, CVE-2026-3311 (vulnerable TLS library), as five separate "
            "findings — once for each of five different listening services (HTTPS admin panel, internal API, "
            "SMTP-over-TLS, an internal metrics endpoint, and a health-check port) — because each service "
            "links its own copy of the vulnerable library. How should the team scope the remediation ticket?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open a single remediation ticket to update the shared TLS library at the host/package level (or rebuild the affected services against the patched library) so all five listeners are fixed together, rather than tracking and re-verifying five disconnected tickets for what is really one root cause.",
                "correct": True,
                "rationale": (
                    "Correct. All five findings share the same root cause — one outdated library used by "
                    "multiple services on the same host. Consolidating remediation into a single ticket that "
                    "addresses the shared dependency avoids duplicated effort, ensures nothing is missed, and "
                    "makes verification simpler (one library version to confirm across all five listeners)."
                ),
            },
            {
                "id": "b",
                "text": "Treat each of the five findings as an entirely independent vulnerability requiring separate root-cause analysis and separate patches.",
                "correct": False,
                "rationale": (
                    "Incorrect. Treating identical findings caused by the same underlying library as five "
                    "unrelated problems wastes analyst time on redundant investigation and risks inconsistent "
                    "remediation across the five services."
                ),
            },
            {
                "id": "c",
                "text": "Only remediate the HTTPS admin panel instance, since administrative interfaces are always the highest priority regardless of the other four instances.",
                "correct": False,
                "rationale": (
                    "Incorrect. Fixing only one of the five affected services while leaving the same vulnerable "
                    "library active in four other listening services leaves the host still exploitable through "
                    "those other paths."
                ),
            },
            {
                "id": "d",
                "text": "Close four of the five findings as duplicates without remediating them, keeping only one open for tracking purposes.",
                "correct": False,
                "rationale": (
                    "Incorrect. Closing findings without actually remediating the underlying vulnerable library "
                    "in each affected service leaves those services genuinely exploitable while falsely "
                    "reporting them as resolved."
                ),
            },
        ],
        "explanation": (
            "When multiple findings share one root cause (a single outdated shared library), the efficient and "
            "correct approach is to consolidate remediation at the root-cause level — fixing the library once "
            "for every service that depends on it — rather than treating each surfaced instance as an isolated "
            "problem or arbitrarily closing duplicates without fixing them."
        ),
    },
    {
        "id": "tvul-010",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "The vulnerability management team's scan target list is generated from a static CIDR range "
            "defined two years ago. A red-team exercise discovers an unauthorized wireless access point "
            "bridged into the finance VLAN, assigned an IP address outside that original CIDR range, running "
            "unpatched firmware with a critical known vulnerability. What does this reveal about the scanning "
            "program, and what is the correct fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The static, outdated scan-target definition created a blind spot for any asset outside the original range; the team should tie scan scope to a continuously updated source of truth (e.g., DHCP leases, network discovery, or asset inventory feeds) rather than a fixed CIDR list defined years ago.",
                "correct": True,
                "rationale": (
                    "Correct. A vulnerability scanning program is only as good as its target list. A static "
                    "range set years ago will not automatically capture new subnets, rogue devices, or shadow "
                    "IT; deriving scan scope from a live, continuously updated inventory source closes this "
                    "kind of blind spot going forward."
                ),
            },
            {
                "id": "b",
                "text": "This is a physical security failure only and has no implication for how the vulnerability scanning program defines its scope.",
                "correct": False,
                "rationale": (
                    "Incorrect. While unauthorized device placement does involve physical/access-control "
                    "failures, the fact that vulnerability scanning never covered this IP range at all is "
                    "specifically a scan-scope gap that needs to be addressed in the vulnerability management "
                    "program."
                ),
            },
            {
                "id": "c",
                "text": "The scanning program is working as intended; assets outside the originally defined range were never meant to be in scope and require no changes.",
                "correct": False,
                "rationale": (
                    "Incorrect. Excluding an entire class of newly appearing devices simply because they fall "
                    "outside a range defined two years ago is precisely the gap that let a critically vulnerable "
                    "rogue device go undetected; the scope definition itself needs to be fixed."
                ),
            },
            {
                "id": "d",
                "text": "Increase the scan frequency of the existing CIDR range without changing its boundaries, since more frequent scanning of the same range will eventually catch the rogue device.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning the same static range more often will never detect a device with an IP "
                    "address outside that range; the boundary/scope itself, not the frequency, is the actual "
                    "gap that needs fixing."
                ),
            },
        ],
        "explanation": (
            "Scan coverage gaps often stem from static, stale target definitions rather than technical scanner "
            "limitations. Tying scan scope to a continuously updated discovery or inventory source (rather than "
            "a fixed CIDR list) is the correct fix for detecting rogue or newly added assets like shadow-IT "
            "devices."
        ),
    },
    {
        "id": "tvul-011",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A finding for CVE-2026-3900 on an internet-facing load balancer has been tracked across three "
            "consecutive weekly scans:\n\n"
            "Week 1: Exploit Code Maturity = 'Unproven' — deprioritized behind several actively exploited findings.\n"
            "Week 2: Exploit Code Maturity = 'Proof-of-Concept' — still queued behind actively exploited findings.\n"
            "Week 3: Exploit Code Maturity = 'Functional' — threat intel also reports opportunistic scanning for this CVE across the internet.\n\n"
            "What should the team conclude from this three-week trend, and what action follows?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The exploit is maturing rapidly and real-world scanning activity has now begun; the finding should be re-prioritized upward this week — likely ahead of lower-trending findings — rather than continuing to treat it as a stable, low-urgency item based on its original Week 1 assessment.",
                "correct": True,
                "rationale": (
                    "Correct. Temporal metrics like exploit code maturity are not static — they must be "
                    "re-evaluated as conditions change. A clear week-over-week progression from unproven to "
                    "functional exploit code, combined with observed opportunistic scanning, is a strong signal "
                    "that urgency has increased and the finding's priority should be reassessed now, not left at "
                    "its original ranking."
                ),
            },
            {
                "id": "b",
                "text": "The finding's priority should remain exactly as it was ranked in Week 1, since the CVSS base score itself has not changed across the three weeks.",
                "correct": False,
                "rationale": (
                    "Incorrect. Base score is static by design, but temporal factors like exploit maturity "
                    "change over time and are meant to adjust real-world urgency; ignoring that trend defeats "
                    "the purpose of tracking temporal metrics at all."
                ),
            },
            {
                "id": "c",
                "text": "Opportunistic internet-wide scanning for a CVE is not a meaningful signal and should be disregarded until an organization-specific attack is observed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Widespread opportunistic scanning for a specific CVE is a leading indicator that "
                    "attackers are actively hunting for vulnerable, exposed targets — a meaningful and actionable "
                    "signal, not something to wait out until after a targeted attack occurs."
                ),
            },
            {
                "id": "d",
                "text": "Since the finding was correctly deprioritized in Weeks 1 and 2, no further review is needed and it can stay in its current queue position indefinitely.",
                "correct": False,
                "rationale": (
                    "Incorrect. Past deprioritization decisions were correct for the conditions at the time, but "
                    "conditions have materially changed by Week 3; failing to re-review as new data arrives "
                    "abandons the point of ongoing vulnerability tracking."
                ),
            },
        ],
        "explanation": (
            "Vulnerability prioritization is not a one-time decision. Temporal signals like exploit code "
            "maturity and observed scanning activity should be re-evaluated on each scan cycle, and a clear "
            "upward trend — especially combined with active opportunistic scanning — should trigger "
            "re-prioritization even if the original assessment correctly deprioritized the finding weeks "
            "earlier."
        ),
    },
    {
        "id": "tvul-012",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vendor publishes a public security advisory describing a critical authentication-bypass flaw "
            "in a widely used firewall OS, including proof-of-concept exploitation steps, but the assigned CVE "
            "record has not yet been ingested by the organization's vulnerability scanner (no plugin exists "
            "yet). Select the TWO actions that are appropriate immediately, before scanner coverage exists."
        ),
        "options": [
            {
                "id": "a",
                "text": "Manually cross-reference the affected firmware/software versions listed in the advisory against the organization's asset inventory to identify which firewalls are impacted.",
                "correct": True,
                "rationale": (
                    "Correct. Manual version cross-referencing against a maintained asset inventory is exactly "
                    "how identification happens for a newly disclosed flaw before automated scanner coverage "
                    "catches up — it is a standard, necessary interim identification method."
                ),
            },
            {
                "id": "b",
                "text": "Apply the vendor's recommended interim mitigation (e.g., restricting management-interface access) on any identified affected devices while a permanent firmware patch is tested and scheduled.",
                "correct": True,
                "rationale": (
                    "Correct. Vendor advisories commonly include interim mitigation guidance; applying it "
                    "immediately on identified affected devices reduces real exposure while the permanent fix "
                    "goes through normal testing and change management."
                ),
            },
            {
                "id": "c",
                "text": "Take no action of any kind until the scanner vendor releases an official detection plugin for the CVE.",
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting for scanner tooling to catch up before doing anything ignores the "
                    "actionable information already published in the vendor's own advisory and unnecessarily "
                    "extends the exposure window for a critical, publicly detailed flaw."
                ),
            },
            {
                "id": "d",
                "text": "Publicly announce the vulnerability and the organization's affected device list on social media to warn customers before internal remediation begins.",
                "correct": False,
                "rationale": (
                    "Incorrect. Publicly disclosing which of the organization's own devices are vulnerable, "
                    "before mitigation is even in place, would hand attackers a target list and is not an "
                    "appropriate vulnerability-management action."
                ),
            },
        ],
        "explanation": (
            "Identification and interim mitigation do not require waiting on scanner plugin coverage. A "
            "published vendor advisory is itself a valid identification source: manually mapping affected "
            "versions against inventory and applying vendor-recommended interim mitigations are the correct "
            "immediate steps while permanent remediation and scanner detection catch up."
        ),
    },
    {
        "id": "tvul-013",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A software composition analysis (SCA) scan of a container base image used by 40 microservices "
            "flags a critical deserialization vulnerability in a shared JSON-parsing library embedded in the "
            "base image. Individually patching each of the 40 running containers is not feasible before the "
            "next release cycle. What is the MOST effective remediation approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Patch the shared base image itself to a version with the fixed library, then rebuild and redeploy the 40 dependent service images from the corrected base — fixing the root cause once instead of patching each running container individually.",
                "correct": True,
                "rationale": (
                    "Correct. Because all 40 containers inherit the vulnerable library from the same shared "
                    "base image, the efficient and correct fix is at the base-image layer: update it once, then "
                    "rebuild and redeploy dependent images through the normal CI/CD pipeline, rather than "
                    "manually patching 40 individual running containers."
                ),
            },
            {
                "id": "b",
                "text": "Individually SSH into each of the 40 running containers and manually update the library in place.",
                "correct": False,
                "rationale": (
                    "Incorrect. Manually patching each running container in place is not scalable, does not fix "
                    "the shared base image (so future rebuilds will reintroduce the vulnerable library), and "
                    "goes against container immutability best practices."
                ),
            },
            {
                "id": "c",
                "text": "Accept the risk for all 40 containers until the next scheduled release cycle, since patching in the meantime is not feasible.",
                "correct": False,
                "rationale": (
                    "Incorrect. A base-image-level fix followed by a rebuild-and-redeploy pipeline run is "
                    "typically achievable well before a full feature release cycle and directly addresses the "
                    "critical finding rather than accepting risk unnecessarily across 40 services."
                ),
            },
            {
                "id": "d",
                "text": "Only patch the base image used by the single microservice that is internet-facing, leaving the other 39 internal services on the vulnerable base image.",
                "correct": False,
                "rationale": (
                    "Incorrect. All 40 services share the same vulnerable library from the same base image; "
                    "leaving 39 of them unpatched leaves the vulnerability active across most of the fleet, "
                    "including any that could be reached through lateral movement or internal exploitation."
                ),
            },
        ],
        "explanation": (
            "Container/SBOM-based vulnerabilities inherited from a shared base image should be remediated at "
            "the base-image layer and propagated through the normal build/redeploy pipeline — a single root-"
            "cause fix — rather than patched piecemeal on individual running instances or partially remediated "
            "across only some consumers."
        ),
    },
    {
        "id": "tvul-014",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan report lists a finding with a status field of 'Potential Vulnerability — Version Check "
            "Only' for CVE-2026-4110, meaning the scanner inferred the vulnerability purely from a reported "
            "version number without directly testing the flaw. A second finding on the same host is listed as "
            "'Confirmed Vulnerability — Exploit Verified,' meaning the scanner safely triggered proof of the "
            "flaw. How should these two status labels affect the team's workflow?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Treat the 'Confirmed' finding as validated and route it directly to remediation, while routing the 'Potential' finding through an additional manual or targeted verification step (e.g., checking actual installed build/patch level) before committing scarce remediation resources to it.",
                "correct": True,
                "rationale": (
                    "Correct. Scanner-reported confidence levels exist precisely to guide workflow: a "
                    "'Confirmed/Exploit Verified' finding has already been actively proven and can move straight "
                    "to remediation, while a version-inference-only 'Potential' finding carries meaningfully "
                    "higher false-positive risk and benefits from a quick verification step before resources are "
                    "committed."
                ),
            },
            {
                "id": "b",
                "text": "Treat both findings identically, since both were produced by the same scanner and should carry equal confidence.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scanner itself is explicitly distinguishing confidence levels between an "
                    "inferred, unverified match and an actively confirmed exploit; ignoring that distinction "
                    "wastes the scanner's own confidence signal and can misallocate remediation effort."
                ),
            },
            {
                "id": "c",
                "text": "Discard the 'Potential Vulnerability' finding entirely without any verification, since version-check-only findings are always false positives.",
                "correct": False,
                "rationale": (
                    "Incorrect. Version-inferred findings are frequently accurate, especially when banner "
                    "spoofing or backporting is not a factor; dismissing them outright without any verification "
                    "risks ignoring real vulnerabilities."
                ),
            },
            {
                "id": "d",
                "text": "Escalate only the 'Potential Vulnerability' finding to incident response, since unverified findings are inherently more suspicious.",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither status field indicates an active security incident is underway; this is "
                    "routine scan triage. An unverified finding is not more 'suspicious' in an incident-response "
                    "sense — it simply needs a verification step before being acted on."
                ),
            },
        ],
        "explanation": (
            "Scanner confidence/status fields ('Confirmed' vs. 'Potential') are a built-in guide for triage "
            "workflow: confirmed exploit-verified findings can proceed directly to remediation, while version-"
            "inference-only findings warrant a lightweight verification step to reduce wasted effort on false "
            "positives without discarding them outright."
        ),
    },
    {
        "id": "tvul-015",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability program lead builds a 2x2 prioritization matrix from combined scan and asset data: "
            "one axis is 'Exploit Likelihood' (derived from exploit maturity, exposure, and threat intel) and "
            "the other is 'Business Impact' (derived from asset criticality and data sensitivity). A finding "
            "for an internet-facing HR self-service portal (moderate business impact, storing only non-"
            "sensitive directory info) with an actively exploited CVE lands in the 'High Likelihood / Moderate "
            "Impact' quadrant, while a finding on the isolated backup-tape rotation server (low likelihood, no "
            "known exploit, air-gapped) with a theoretically severe CVE lands in 'Low Likelihood / High "
            "Impact.' Which finding should be worked FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The HR portal finding, because high exploit likelihood combined with even moderate business impact represents materially higher realistic risk than a high-impact finding with low likelihood of ever being exploited given its isolation.",
                "correct": True,
                "rationale": (
                    "Correct. In a likelihood x impact prioritization model, a high-likelihood finding "
                    "generally outranks a low-likelihood one even at a somewhat lower impact tier, because risk "
                    "is a function of both dimensions together — an attack that is actually happening (or highly "
                    "likely to happen) against a moderately important asset is more urgent than a theoretical, "
                    "unlikely attack against a highly important but effectively unreachable one."
                ),
            },
            {
                "id": "b",
                "text": "The backup-tape rotation server finding, because 'High Impact' should always be worked before 'Moderate Impact' regardless of likelihood.",
                "correct": False,
                "rationale": (
                    "Incorrect. Prioritizing on impact alone while ignoring likelihood defeats the purpose of a "
                    "two-dimensional risk matrix; a low-likelihood, effectively unreachable finding is not more "
                    "urgent than an actively exploited, internet-facing one."
                ),
            },
            {
                "id": "c",
                "text": "Both findings are equally urgent and should be worked in whichever order is administratively convenient.",
                "correct": False,
                "rationale": (
                    "Incorrect. The whole purpose of building a likelihood x impact matrix is to differentiate "
                    "urgency between quadrants; treating two clearly different quadrants as equally urgent "
                    "discards the analysis the team just built."
                ),
            },
            {
                "id": "d",
                "text": "Neither finding needs immediate attention since neither lands in the matrix's 'High Likelihood / High Impact' quadrant.",
                "correct": False,
                "rationale": (
                    "Incorrect. An actively exploited vulnerability on an internet-facing system still warrants "
                    "urgent action even outside the single highest quadrant; risk-based prioritization is a "
                    "ranking exercise across all findings, not a binary 'act only on the top corner' rule."
                ),
            },
        ],
        "explanation": (
            "A likelihood x impact prioritization matrix is meant to rank realistic risk, not to defer entirely "
            "to impact or wait for the single highest-risk quadrant. A high-likelihood finding, even at "
            "moderate impact, typically represents greater near-term real-world risk than a high-impact but "
            "low-likelihood, effectively isolated finding."
        ),
    },
    {
        "id": "tvul-016",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan flags CVE-2026-4400 (CVSS base 6.5) on a server hosting an electronic health records (EHR) "
            "database. The organization's CVSS environmental scoring sets Confidentiality Requirement (CR) and "
            "Integrity Requirement (IR) to 'High' for any system handling protected health information (PHI), "
            "producing an adjusted environmental score of 8.4 — noticeably higher than the base score. A "
            "manager questions why a 'medium' base-score finding is being treated as high priority. What is the "
            "correct explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The environmental Confidentiality/Integrity/Availability Requirement metrics let the organization state that a breach of confidentiality or integrity on this specific asset would be unusually damaging (here, due to PHI regulatory and patient-safety impact), which legitimately raises the score above the generic base value for this deployment.",
                "correct": True,
                "rationale": (
                    "Correct. CR/IR/AR are environmental metrics specifically designed to let an organization "
                    "state that a given impact type matters more for a particular asset than the generic base "
                    "score assumes. For a PHI-handling EHR database, a confidentiality or integrity breach "
                    "carries outsized regulatory and patient-safety consequences, which is exactly the scenario "
                    "these metrics exist to capture."
                ),
            },
            {
                "id": "b",
                "text": "The environmental score is inflated arbitrarily and should be disregarded in favor of the vendor's original base score of 6.5.",
                "correct": False,
                "rationale": (
                    "Incorrect. The environmental adjustment is not arbitrary — it is a deliberate, documented "
                    "application of the CR/IR/AR metrics that CVSS provides specifically for organizations to "
                    "tailor scoring to their own asset sensitivity."
                ),
            },
            {
                "id": "c",
                "text": "CR and IR represent how many compliance frameworks (e.g., HIPAA, PCI DSS) apply to the host, and are unrelated to the actual technical impact of the vulnerability.",
                "correct": False,
                "rationale": (
                    "Incorrect. CR/IR/AR are technical CVSS environmental metrics describing the organizational "
                    "importance of each impact type (confidentiality, integrity, availability) for the specific "
                    "asset, not a count of applicable compliance frameworks."
                ),
            },
            {
                "id": "d",
                "text": "The score difference indicates a data-entry error, since environmental scores can never legitimately differ from the base score by more than one point.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVSS environmental scoring can shift the score by a meaningful margin in either "
                    "direction; there is no rule limiting the adjustment to one point, and a well-justified "
                    "1.9-point increase for a high-sensitivity PHI asset is entirely legitimate."
                ),
            },
        ],
        "explanation": (
            "Environmental metrics (Confidentiality/Integrity/Availability Requirements) exist so organizations "
            "can raise or lower a generic base score to reflect how much a given impact type actually matters "
            "for a specific asset. A regulated, patient-safety-relevant PHI system legitimately produces a "
            "higher environmental score than its generic base score, and that adjusted score should drive "
            "prioritization for this asset."
        ),
    },
    {
        "id": "tvul-017",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A critical vulnerability is found in the VM template used to provision every new virtual desktop "
            "in the organization. A scan of currently running VMs shows 210 of 300 desktops already affected, "
            "with the count climbing daily as more desktops are provisioned from the still-unpatched template. "
            "What is the correct remediation sequence?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Patch the VM template first so no further vulnerable desktops are provisioned, then push the fix out to the 210 already-affected running desktops (e.g., via patch management or redeployment).",
                "correct": True,
                "rationale": (
                    "Correct. Fixing only the running desktops without first patching the source template "
                    "leaves the count climbing indefinitely as new desktops keep being provisioned vulnerable. "
                    "Patching the template stops the bleeding immediately, and remediating the already-deployed "
                    "desktops closes the remaining gap."
                ),
            },
            {
                "id": "b",
                "text": "Patch only the 210 currently affected running desktops, and leave the template as-is since it is not itself a running, exploitable system.",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving the template unpatched guarantees every future desktop provisioned from "
                    "it will also be vulnerable, meaning the finding count will keep growing even after the "
                    "current 210 are fixed."
                ),
            },
            {
                "id": "c",
                "text": "Pause all new desktop provisioning indefinitely instead of patching anything, until a full replacement platform can be evaluated.",
                "correct": False,
                "rationale": (
                    "Incorrect. Halting provisioning entirely is a disproportionate response to a fixable "
                    "template vulnerability and unnecessarily disrupts business operations when patching the "
                    "template directly resolves the root cause."
                ),
            },
            {
                "id": "d",
                "text": "Wait until all 300 desktops eventually show the finding before taking any remediation action, to remediate everything in a single batch.",
                "correct": False,
                "rationale": (
                    "Incorrect. Deliberately waiting for more desktops to become vulnerable before acting "
                    "needlessly expands the exposed population and delays an obvious, immediately actionable fix "
                    "at the template level."
                ),
            },
        ],
        "explanation": (
            "When a vulnerability originates in a shared provisioning template, the template must be patched "
            "first to stop new vulnerable instances from being created, followed by remediation of already-"
            "deployed instances — patching only the deployed instances (or waiting) leaves the root cause active "
            "and the finding count growing."
        ),
    },
    {
        "id": "tvul-018",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan reports 'Weak TLS Cipher Suites Enabled' (CVSS-equivalent 5.9) on an internet-facing API "
            "gateway, listing several deprecated cipher suites that support RC4 and weak Diffie-Hellman "
            "parameters still being offered during the TLS handshake, alongside strong modern ciphers. There is "
            "no CVE and no vendor patch referenced. What is the correct remediation and verification approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reconfigure the TLS server settings to remove the weak cipher suites and enforce a modern, minimum protocol version and cipher policy, then verify the change with a rescan or a dedicated TLS configuration scanner confirming the weak suites are no longer offered.",
                "correct": True,
                "rationale": (
                    "Correct. This is a configuration hardening finding, not a code vulnerability — remediation "
                    "is a server-side TLS configuration change (disabling weak suites, enforcing a strong "
                    "minimum protocol/cipher policy), and it should be verified afterward with a rescan or "
                    "dedicated TLS-checking tool to confirm the weak options are actually gone from the "
                    "handshake."
                ),
            },
            {
                "id": "b",
                "text": "Wait for a CVE to be assigned and a vendor patch to be released before taking any action, since the finding has no CVE identifier.",
                "correct": False,
                "rationale": (
                    "Incorrect. Weak cipher suite exposure is a configuration issue with an immediate, "
                    "well-known fix (disabling the weak ciphers); it does not require a CVE or vendor patch, and "
                    "waiting needlessly extends exposure."
                ),
            },
            {
                "id": "c",
                "text": "Ignore the finding since strong modern ciphers are also being offered alongside the weak ones, so clients will typically negotiate the strong option anyway.",
                "correct": False,
                "rationale": (
                    "Incorrect. Offering weak ciphers alongside strong ones still allows a downgrade attack or a "
                    "misconfigured/legacy client to negotiate the weaker option; leaving weak suites enabled "
                    "preserves real exploitable risk regardless of what a well-behaved client would typically "
                    "choose."
                ),
            },
            {
                "id": "d",
                "text": "Replace the entire API gateway hardware appliance, since weak cipher suite findings cannot be fixed through configuration alone.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cipher suite selection is virtually always a configuration setting on modern TLS "
                    "implementations; a full hardware replacement is a disproportionate response to what is "
                    "typically a straightforward configuration change."
                ),
            },
        ],
        "explanation": (
            "Weak cipher/protocol findings are configuration hardening issues, remediated by reconfiguring TLS "
            "settings to disable deprecated ciphers and enforce a strong minimum policy, then verified through "
            "rescanning — not something that requires a CVE, a vendor patch, or hardware replacement."
        ),
    },
    {
        "id": "tvul-019",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan reports two findings on the same internal server that were each individually deprioritized: "
            "a 'Medium' (5.3) information-disclosure flaw that reveals internal usernames, and a 'Low' (3.7) "
            "weak-password-policy finding on the same authentication service. A red-team exercise later chains "
            "the two together — harvesting usernames from the disclosure flaw, then successfully "
            "password-spraying accounts because of the weak policy — to gain initial access. What does this "
            "reveal about scoring findings individually?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Individual CVSS scores reflect each flaw's standalone severity and do not account for how an attacker might chain multiple lower-severity findings on the same asset into a higher-impact attack path, so the vulnerability management program should also review co-located, individually low-severity findings for realistic chaining risk, not just each score in isolation.",
                "correct": True,
                "rationale": (
                    "Correct. CVSS scores a single vulnerability in isolation; it does not model attack "
                    "chaining across multiple findings. A mature vulnerability management program supplements "
                    "individual scoring with periodic review (or pen testing) specifically looking for "
                    "co-located, individually low-severity findings on the same asset that could combine into a "
                    "meaningfully higher-impact attack path."
                ),
            },
            {
                "id": "b",
                "text": "The red team's result proves the scanner's severity ratings for both findings were simply wrong and should be manually overridden to 'Critical.'",
                "correct": False,
                "rationale": (
                    "Incorrect. Each finding's individual CVSS score, evaluated on its own standalone merits, is "
                    "not inherently wrong; the issue is that CVSS does not model chaining, not that the "
                    "individual severities were miscalculated."
                ),
            },
            {
                "id": "c",
                "text": "Since both findings were correctly deprioritized individually, no changes to the remediation queue or review process are needed.",
                "correct": False,
                "rationale": (
                    "Incorrect. While each score was individually reasonable, the successful attack chain shows "
                    "a real gap in the process — co-located findings should be reviewed together for chaining "
                    "risk, not left exactly as they were."
                ),
            },
            {
                "id": "d",
                "text": "This demonstrates that vulnerability scanning is fundamentally unreliable and should be replaced entirely by red-team exercises going forward.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scanning and red-team/pen testing serve complementary purposes; "
                    "this scenario shows a specific limitation of isolated CVSS scoring, not that scanning "
                    "should be discontinued altogether."
                ),
            },
        ],
        "explanation": (
            "CVSS scores vulnerabilities individually and does not model attack chaining. Findings that appear "
            "low-priority in isolation can combine into a significant attack path when co-located on the same "
            "asset, which is why mature programs supplement individual scoring with periodic chaining-aware "
            "review or pen testing rather than relying on standalone scores alone."
        ),
    },
    {
        "id": "tvul-020",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A software composition analysis (SCA)/SBOM scan reveals that a vulnerable logging library is "
            "embedded as a transitive dependency in 15 different internally developed applications, each "
            "maintained by a different team. Select the TWO actions that represent the MOST effective program-"
            "level response."
        ),
        "options": [
            {
                "id": "a",
                "text": "Centrally track the vulnerable library version as a single cross-application finding in the vulnerability management/SBOM tooling, so the security team can see at a glance which of the 15 applications have and have not yet updated to the patched version.",
                "correct": True,
                "rationale": (
                    "Correct. Tracking the shared dependency centrally, across all consuming applications, "
                    "gives the security team unified visibility into overall remediation progress rather than "
                    "15 disconnected, hard-to-correlate findings scattered across different teams' backlogs."
                ),
            },
            {
                "id": "b",
                "text": "Notify all 15 owning teams with the specific patched version to upgrade to, and set a coordinated deadline consistent with the finding's severity, rather than leaving each team to discover and prioritize it independently.",
                "correct": True,
                "rationale": (
                    "Correct. Because the same vulnerable dependency affects many teams, proactive, coordinated "
                    "notification with a clear target version and deadline ensures consistent, timely "
                    "remediation across all consumers instead of relying on each team to separately notice the "
                    "finding on its own schedule."
                ),
            },
            {
                "id": "c",
                "text": "Have the security team quietly patch and redeploy all 15 applications directly without involving the owning development teams, to save time.",
                "correct": False,
                "rationale": (
                    "Incorrect. Directly modifying and redeploying 15 applications the security team does not "
                    "own, without developer involvement or testing, risks breaking functionality and bypasses "
                    "normal change management; coordination with owning teams is the appropriate approach."
                ),
            },
            {
                "id": "d",
                "text": "Wait for each team to independently discover the vulnerable dependency during their own routine dependency audits, with no proactive outreach from the security team.",
                "correct": False,
                "rationale": (
                    "Incorrect. Passively waiting for 15 separate teams to each independently discover the same "
                    "shared vulnerability leads to inconsistent timing and likely delays; proactive, coordinated "
                    "notification is far more effective."
                ),
            },
        ],
        "explanation": (
            "Shared/transitive dependency vulnerabilities affecting many applications call for centralized "
            "tracking across all consumers and proactive, coordinated notification with a clear target version "
            "and deadline — not scattered independent discovery or the security team unilaterally modifying "
            "code it does not own."
        ),
    },
    {
        "id": "tvul-021",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "The CISO asks for a board-level summary translating this quarter's raw vulnerability scan output "
            "(thousands of individual CVE findings) into a small number of themes mapped to recognized control "
            "categories (e.g., 'Patch Management,' 'Access Control,' 'Secure Configuration') for a governance "
            "presentation. What is the BEST approach to prepare this report?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Aggregate and categorize the individual findings by underlying root-cause theme, map each theme to the corresponding control category from a recognized framework (e.g., CIS Controls or NIST CSF), and present trend and volume by category rather than listing individual CVEs.",
                "correct": True,
                "rationale": (
                    "Correct. Board-level audiences need risk themes and trends, not a raw CVE list. Aggregating "
                    "findings by root-cause theme and mapping them to recognized control categories translates "
                    "technical scan output into governance-relevant language, showing where systemic weaknesses "
                    "(and improvement trends) exist."
                ),
            },
            {
                "id": "b",
                "text": "Print the complete raw scan output, including every individual CVE and its full technical vector string, for the board to review directly.",
                "correct": False,
                "rationale": (
                    "Incorrect. A raw technical dump of thousands of CVE-level findings is not actionable or "
                    "meaningful for a governance audience; it fails to communicate risk themes or trends in a "
                    "way the board can act on."
                ),
            },
            {
                "id": "c",
                "text": "Report only the single highest CVSS score found this quarter as the entire summary, omitting all other context.",
                "correct": False,
                "rationale": (
                    "Incorrect. A single highest score tells the board nothing about overall program health, "
                    "trend direction, or systemic root causes; it is not a substitute for a categorized, "
                    "trend-aware summary."
                ),
            },
            {
                "id": "d",
                "text": "Omit the vulnerability scan data from the governance presentation entirely, since it is considered too technical for a board audience.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability posture is legitimate and important governance information; the "
                    "correct response to it being 'too technical' in raw form is to translate it appropriately, "
                    "not to omit it from oversight reporting altogether."
                ),
            },
        ],
        "explanation": (
            "Effective vulnerability management reporting translates raw scan data into risk themes mapped to "
            "recognized control categories, with trend and volume context — giving governance stakeholders "
            "actionable insight into systemic weaknesses rather than either an unusable raw data dump or an "
            "oversimplified single data point."
        ),
    },
    {
        "id": "tvul-022",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "Quarterly trend data shows the vulnerability management program's mean time to remediate (MTTR) "
            "for critical findings has grown from 12 days to 34 days over the past four quarters, even though "
            "scan frequency and finding volume have stayed roughly constant. The program lead's first instinct "
            "is to reduce scan frequency to 'give the team more time to catch up.' What is the more appropriate "
            "first step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Investigate the actual bottleneck in the remediation workflow (e.g., change-management approval delays, patch-testing backlogs, or unclear ownership) before changing anything about the scanning process itself, since scan frequency determines detection speed, not remediation speed.",
                "correct": True,
                "rationale": (
                    "Correct. MTTR measures how long it takes to fix findings after they are found — a process "
                    "and workflow metric, not a scanning-frequency metric. Reducing scan frequency would only "
                    "delay detection of new findings without addressing why existing findings are taking longer "
                    "to actually remediate; the real fix requires diagnosing the workflow bottleneck itself."
                ),
            },
            {
                "id": "b",
                "text": "Reduce scan frequency from weekly to monthly, since finding fewer new vulnerabilities per cycle will naturally lower the average remediation time.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning less often does not make existing findings get fixed any faster — it "
                    "only delays discovery of new ones, and could make the underlying (unaddressed) MTTR problem "
                    "worse by hiding it behind less frequent measurement."
                ),
            },
            {
                "id": "c",
                "text": "Lower the CVSS threshold that defines 'critical' so fewer findings are counted in this metric, improving the reported MTTR without changing actual remediation speed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Redefining thresholds to make a metric look better cosmetically hides the real "
                    "problem rather than solving it, and misrepresents the program's true remediation "
                    "performance to stakeholders."
                ),
            },
            {
                "id": "d",
                "text": "Conclude that the rising MTTR is unavoidable and stop tracking the metric going forward.",
                "correct": False,
                "rationale": (
                    "Incorrect. Discontinuing measurement of a worsening metric removes visibility into a real "
                    "and worsening operational problem rather than addressing its root cause."
                ),
            },
        ],
        "explanation": (
            "A rising MTTR trend with stable scan volume points to a remediation-workflow bottleneck (approvals, "
            "testing capacity, ownership gaps), not a scanning-cadence problem. The correct response is root-"
            "cause investigation of the remediation pipeline, not adjusting scan frequency or metric "
            "definitions to make the number look better."
        ),
    },
    {
        "id": "tvul-023",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan of a file server running Windows Server 2012 (end of extended support) shows 47 unique "
            "CVEs rated High or Critical, and that number has grown every quarter for the past year with no "
            "vendor patches forthcoming for any of them. A migration project to replace the server is budgeted "
            "but will not complete for eight months. Which interpretation of this scan trend is MOST accurate, "
            "and what follows from it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An unsupported operating system will keep accumulating unpatched CVEs indefinitely since no vendor fixes will ever arrive; rather than attempting to individually track and patch each new CVE, the team should apply broad compensating controls (network segmentation, restricted access, enhanced monitoring) for the full eight-month gap until the migration retires the host.",
                "correct": True,
                "rationale": (
                    "Correct. Once a platform reaches end-of-support, new CVEs will continue to accumulate with "
                    "no patch path — chasing each one individually is not a sustainable strategy. The correct "
                    "interpretation is that the growing count reflects a structural, unfixable-at-the-source "
                    "problem, and the correct response is broad compensating controls covering the whole "
                    "unsupported host until it is retired, rather than case-by-case CVE chasing."
                ),
            },
            {
                "id": "b",
                "text": "Each of the 47 CVEs should be individually triaged and tracked as its own separate remediation ticket with its own patch-testing plan, the same as findings on a fully supported platform.",
                "correct": False,
                "rationale": (
                    "Incorrect. Treating every CVE on an unsupported, unpatchable platform identically to "
                    "findings on a supported platform wastes significant effort chasing fixes that will never "
                    "arrive from the vendor, when a broader compensating-control strategy is more effective."
                ),
            },
            {
                "id": "c",
                "text": "The growing CVE count is a scanner artifact and should be disregarded, since an unsupported OS is expected to accumulate findings regardless of actual risk.",
                "correct": False,
                "rationale": (
                    "Incorrect. The growing findings represent genuinely new, real vulnerabilities being "
                    "discovered in the unsupported platform over time; they are not a scanner artifact and "
                    "should not be disregarded, even though the response strategy differs from a supported "
                    "platform."
                ),
            },
            {
                "id": "d",
                "text": "The migration project should be canceled since the server will be retired anyway, making any interim risk-reduction effort pointless.",
                "correct": False,
                "rationale": (
                    "Incorrect. An eight-month exposure window on a critically vulnerable file server is not "
                    "negligible; interim compensating controls remain worthwhile even though the host will "
                    "eventually be retired, and abandoning risk-reduction effort in the meantime is not "
                    "appropriate."
                ),
            },
        ],
        "explanation": (
            "An end-of-support platform will keep generating new, unpatchable CVEs indefinitely. The correct "
            "read of a growing finding count on such a host is a structural, source-level dead end, best "
            "addressed with broad compensating controls (segmentation, access restriction, monitoring) covering "
            "the entire exposure window until retirement, rather than case-by-case patch chasing or dismissing "
            "the trend."
        ),
    },
    {
        "id": "tvul-024",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A quarterly scan-coverage report shows the vulnerability scanner successfully assessed 1,180 of "
            "the 1,600 assets listed in the CMDB (73.75% coverage). The remaining 420 assets show no scan "
            "history at all for the entire quarter. What should the vulnerability management team treat this "
            "coverage gap as, and what is the appropriate response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A significant blind spot in its own right — those 420 assets could harbor unknown critical vulnerabilities — requiring investigation into why they were never scanned (decommissioned but not removed from the CMDB, network access issues, credential failures, or scanner scope gaps) before the program can claim accurate overall risk visibility.",
                "correct": True,
                "rationale": (
                    "Correct. Scan coverage itself is a critical program-health metric. A quarter of assets "
                    "never being scanned at all means the organization has no visibility into their "
                    "vulnerability status whatsoever — this must be investigated and closed (whether the cause "
                    "is stale CMDB records, connectivity, or scope gaps) before any overall risk statement can "
                    "be trusted."
                ),
            },
            {
                "id": "b",
                "text": "An acceptable result, since scanning nearly three-quarters of the inventory is generally considered sufficient for reporting purposes.",
                "correct": False,
                "rationale": (
                    "Incorrect. A 73.75% coverage rate leaving over a quarter of the inventory completely "
                    "unassessed is a material gap, not an acceptable baseline; unscanned assets could include "
                    "critically vulnerable systems that the organization has zero visibility into."
                ),
            },
            {
                "id": "c",
                "text": "Irrelevant to overall risk reporting, since the 1,180 successfully scanned assets already provide a representative sample of the environment.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanned assets are not necessarily representative of the unscanned ones (which "
                    "could be exactly the stale, unmanaged, or access-restricted systems most likely to be "
                    "vulnerable); assuming representativeness without investigation is not sound practice."
                ),
            },
            {
                "id": "d",
                "text": "A sign that the CMDB should simply be trimmed to remove the 420 assets from tracking so the coverage percentage reads as 100%.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing assets from tracking purely to make a coverage metric look better "
                    "without verifying whether those assets are actually decommissioned hides real risk rather "
                    "than resolving it."
                ),
            },
        ],
        "explanation": (
            "Scan coverage percentage is itself a key vulnerability-management KPI. A substantial unscanned "
            "population represents a genuine blind spot that must be investigated and closed — whether the "
            "cause is stale inventory records, access failures, or scope gaps — rather than accepted as "
            "adequate, assumed representative, or hidden by trimming the tracked inventory."
        ),
    },
    # ---------------------------------------------------------------
    # SIEM & monitoring (8) — domain 4, objective 4.4
    # ---------------------------------------------------------------
    {
        "id": "tvul-025",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A security team wants its SIEM to correlate IDS/IPS exploit-signature alerts against a specific "
            "database server with that same server's current vulnerability-scan status, so that an exploit "
            "attempt targeting a CVE the server is confirmed NOT vulnerable to is deprioritized, while an "
            "attempt matching a CVE the server IS confirmed vulnerable to is escalated immediately. What must "
            "be true of the SIEM's data sources for this to work?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SIEM must ingest a live, per-asset feed of confirmed unpatched CVEs from the vulnerability management platform, and the correlation rule must match the CVE referenced by the exploit signature against that specific asset's current vulnerable-CVE list before adjusting alert priority.",
                "correct": True,
                "rationale": (
                    "Correct. This kind of risk-aware correlation requires the SIEM to have current, per-asset "
                    "vulnerability data available as an enrichment source, and a rule that explicitly checks "
                    "whether the targeted asset is actually vulnerable to the specific CVE referenced by the "
                    "exploit signature — without both pieces, the SIEM cannot distinguish a real threat from a "
                    "harmless attempt against an already-patched system."
                ),
            },
            {
                "id": "b",
                "text": "The SIEM only needs firewall and NetFlow logs, since exploit signatures already indicate severity on their own without any vulnerability context.",
                "correct": False,
                "rationale": (
                    "Incorrect. Network flow data alone cannot tell the SIEM whether the specific targeted "
                    "asset is actually vulnerable to the referenced CVE; that requires ingesting vulnerability "
                    "management data as a distinct enrichment source."
                ),
            },
            {
                "id": "c",
                "text": "The SIEM should simply raise every exploit-signature alert to the highest priority regardless of target vulnerability status, to guarantee nothing is missed.",
                "correct": False,
                "rationale": (
                    "Incorrect. This defeats the stated goal of differentiating real risk from noise and would "
                    "reintroduce the exact alert-fatigue problem the team is trying to solve by building "
                    "risk-aware correlation in the first place."
                ),
            },
            {
                "id": "d",
                "text": "The SIEM should stop ingesting IDS/IPS alerts entirely and rely solely on vulnerability scan data for detection.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scan data alone cannot detect an active exploitation attempt in "
                    "progress; both the real-time exploit signature and the vulnerability status data are needed "
                    "together for this correlation to work."
                ),
            },
        ],
        "explanation": (
            "Risk-aware SIEM correlation requires combining two data sources: real-time exploit-signature "
            "telemetry and a live, per-asset feed of confirmed vulnerability status from the vulnerability "
            "management platform. Only by matching the two can the SIEM tell the difference between an exploit "
            "attempt against a genuinely exposed system and one against an already-patched one."
        ),
    },
    {
        "id": "tvul-026",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "Fifty newly deployed industrial IoT sensors begin appearing in NetFlow logs ingested by the SIEM, "
            "but none of them show up in the vulnerability management platform's asset list, and no scan has "
            "ever targeted their IP range. The SIEM has no way to tell whether alerts involving these devices "
            "represent genuine risk. What is the MOST appropriate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Add the newly discovered IoT sensor IP range to both the vulnerability scanning target list and the asset inventory feeding the SIEM, so the devices receive scan coverage and their vulnerability status can be correlated against future alerts involving them.",
                "correct": True,
                "rationale": (
                    "Correct. A device visible in network telemetry but absent from both the vulnerability "
                    "scanner's targets and the SIEM's asset context is an active blind spot; the correct fix is "
                    "onboarding it into both scanning scope and the SIEM's asset/vulnerability context so future "
                    "alerts about it can be properly risk-assessed."
                ),
            },
            {
                "id": "b",
                "text": "Suppress all SIEM alerts referencing these IP addresses until the IoT project formally closes out, to reduce noise from unclassified devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. Suppressing alerts about newly discovered, unassessed devices removes visibility "
                    "into potentially real threats rather than addressing the actual gap, which is the missing "
                    "scan and asset-inventory coverage."
                ),
            },
            {
                "id": "c",
                "text": "Ignore the NetFlow entries as noise, since IoT devices are not expected to generate meaningful security telemetry.",
                "correct": False,
                "rationale": (
                    "Incorrect. IoT devices are a well-documented, frequently targeted attack surface; treating "
                    "their network activity as inherently unimportant ignores a real and common source of risk."
                ),
            },
            {
                "id": "d",
                "text": "Remove NetFlow ingestion from the SIEM entirely, since it is surfacing devices the vulnerability program was not prepared to handle.",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow correctly did its job by surfacing an unmanaged asset; removing that "
                    "visibility would make future onboarding gaps even harder to detect, rather than fixing the "
                    "underlying inventory and scanning gap."
                ),
            },
        ],
        "explanation": (
            "When network telemetry surfaces devices absent from both the vulnerability scanner's scope and the "
            "SIEM's asset context, the correct response is to onboard them into both — closing the visibility "
            "gap — rather than suppressing the resulting alerts, dismissing the traffic as unimportant, or "
            "disabling the telemetry source that caught the gap."
        ),
    },
    {
        "id": "tvul-027",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM ingests SCAP-based configuration compliance results in addition to CVE-based vulnerability "
            "scan data. A production database server passes its CVE-based vulnerability scan with zero "
            "critical findings, but its SCAP compliance report shows it failing the benchmark check for audit "
            "logging being disabled. A junior analyst asks why the server would need any further attention "
            "since 'the vulnerability scan came back clean.' What is the correct explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CVE-based vulnerability scanning and SCAP configuration compliance checking answer different questions — one detects known software flaws, the other checks whether the system's configuration matches a secure baseline — so a host can be fully patched against known CVEs while still failing baseline configuration controls like audit logging, and both must be reviewed together.",
                "correct": True,
                "rationale": (
                    "Correct. 'No CVE findings' only means the installed software has no known unpatched "
                    "vulnerabilities; it says nothing about whether the system's configuration meets secure "
                    "baseline requirements. SCAP compliance results and vulnerability scan results are "
                    "complementary and must both be reviewed to get a full security picture."
                ),
            },
            {
                "id": "b",
                "text": "The SCAP compliance finding must be a false positive, since a host that is clean on its vulnerability scan cannot simultaneously fail a configuration check.",
                "correct": False,
                "rationale": (
                    "Incorrect. A CVE-clean vulnerability scan and a failed configuration compliance check are "
                    "not contradictory — they measure entirely different things, and both results can be "
                    "accurate simultaneously."
                ),
            },
            {
                "id": "c",
                "text": "SCAP compliance checks are strictly informational and never require remediation, unlike CVE-based vulnerability findings.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabled audit logging is a meaningful security gap (it removes the ability to "
                    "detect and investigate suspicious activity on the host) and warrants remediation just as a "
                    "CVE finding would, not dismissal as purely informational."
                ),
            },
            {
                "id": "d",
                "text": "The vulnerability scanner and the SCAP compliance tool must have scanned different hosts by mistake.",
                "correct": False,
                "rationale": (
                    "Incorrect. It is entirely normal and expected for the same host to pass one type of "
                    "assessment while failing another, since CVE scanning and configuration compliance checking "
                    "evaluate fundamentally different aspects of the system."
                ),
            },
        ],
        "explanation": (
            "Vulnerability scanning (CVE-based) and SCAP configuration compliance scanning are complementary, "
            "not redundant: one finds known software flaws, the other verifies the system's configuration "
            "against a secure baseline. A host can legitimately pass one and fail the other, and both results "
            "must be reviewed for complete visibility."
        ),
    },
    {
        "id": "tvul-028",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "During the organization's authorized weekly vulnerability scan window, the SIEM generates over 900 "
            "IDS alerts for 'port scanning' and 'directory enumeration' activity, all originating from the "
            "vulnerability scanner's own IP address, burying genuine alerts from other sources for that "
            "several-hour period. What is the MOST appropriate SIEM configuration change?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tag or allow-list the vulnerability scanner's known IP address(es) and scan schedule in the SIEM's correlation rules so its expected, authorized scanning behavior is tracked separately (or suppressed from the standard alert queue) without disabling detection of that same behavior from any unexpected, non-scanner source.",
                "correct": True,
                "rationale": (
                    "Correct. The correct tuning approach distinguishes known-good, authorized scanner traffic "
                    "from genuinely suspicious activity by source and schedule — reducing noise from the "
                    "expected scanner without blinding the SIEM to identical-looking behavior from an "
                    "unauthorized source."
                ),
            },
            {
                "id": "b",
                "text": "Disable the port-scanning and directory-enumeration detection rules entirely across the whole environment to eliminate the noise.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the detection rule entirely removes the SIEM's ability to catch "
                    "genuine reconnaissance activity from an actual attacker, not just noise from the authorized "
                    "scanner."
                ),
            },
            {
                "id": "c",
                "text": "Stop running the authorized vulnerability scans altogether, since they are generating too much SIEM noise.",
                "correct": False,
                "rationale": (
                    "Incorrect. Eliminating vulnerability scanning to reduce SIEM alert noise sacrifices a "
                    "core security control; the correct fix is tuning the SIEM to recognize the known scanner "
                    "traffic, not removing the scanning program."
                ),
            },
            {
                "id": "d",
                "text": "Increase the alert severity threshold across the entire SIEM so fewer alerts of any kind are generated during business hours.",
                "correct": False,
                "rationale": (
                    "Incorrect. A blanket severity threshold change affects all alert sources, not just the "
                    "scanner-generated noise, and risks suppressing genuinely important alerts unrelated to the "
                    "scan window."
                ),
            },
        ],
        "explanation": (
            "Authorized vulnerability scanning traffic commonly triggers IDS/IPS signatures identical to real "
            "reconnaissance. The correct tuning approach is to specifically recognize the scanner's known source "
            "and schedule (allow-listing/tagging) rather than disabling the underlying detection capability, "
            "halting scanning, or broadly raising thresholds across unrelated traffic."
        ),
    },
    {
        "id": "tvul-029",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "Vulnerability management data confirms a specific internal application server is vulnerable to a "
            "critical Java deserialization flaw with a well-documented JNDI-lookup exploitation pattern. The "
            "patch is scheduled for next week's maintenance window. Which SIEM detection configuration would "
            "MOST directly help catch an exploitation attempt against this specific host in the meantime?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Build a targeted correlation rule that inspects inbound requests and application logs for the specific JNDI-lookup exploitation pattern associated with this CVE, scoped to (or weighted toward) the confirmed-vulnerable host, with a high-priority alert on match.",
                "correct": True,
                "rationale": (
                    "Correct. A detection rule built from the vulnerability's specific, publicly documented "
                    "exploitation pattern (the JNDI lookup string) and focused on the known-vulnerable host gives "
                    "the SOC a concrete, high-fidelity way to catch an exploitation attempt during the exposure "
                    "window before the scheduled patch."
                ),
            },
            {
                "id": "b",
                "text": "Increase the SIEM's overall storage retention for this host's logs from 90 days to 365 days.",
                "correct": False,
                "rationale": (
                    "Incorrect. Extending retention supports later historical investigation but does nothing to "
                    "improve real-time detection of an exploitation attempt happening before the patch window."
                ),
            },
            {
                "id": "c",
                "text": "Temporarily disable alerting for this host to avoid generating false positives before the patch is applied next week.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling alerting on the exact host confirmed vulnerable to a critical, actively "
                    "exploitable flaw removes the SOC's ability to detect an attack during precisely the window "
                    "when detection matters most."
                ),
            },
            {
                "id": "d",
                "text": "Wait until after the patch is deployed next week before making any SIEM changes related to this vulnerability.",
                "correct": False,
                "rationale": (
                    "Incorrect. This leaves the entire pre-patch exposure window unmonitored for exploitation "
                    "attempts against a confirmed critical flaw; the detection rule should be built immediately, "
                    "not deferred until after remediation."
                ),
            },
        ],
        "explanation": (
            "When a patch is temporarily delayed, a SIEM detection rule built from the vulnerability's specific, "
            "known exploitation pattern and scoped toward the confirmed-vulnerable asset serves as a monitoring-"
            "based compensating control, giving visibility into the exposure window rather than leaving it dark "
            "or building blanket, unrelated changes."
        ),
    },
    {
        "id": "tvul-030",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM report correlating alert volume against vulnerability age shows that hosts with critical "
            "findings older than 60 days generate, on average, four times more low-severity reconnaissance and "
            "probing alerts than hosts with no open critical findings. The SOC lead wants to reduce this "
            "persistent low-level alert volume. What is the MOST effective underlying fix, as opposed to a "
            "purely SIEM-side change?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Accelerate remediation of the aging critical vulnerabilities driving the correlation, since patching the underlying exposure removes the attacker interest generating the probing traffic in the first place, rather than just tuning the alerts describing it.",
                "correct": True,
                "rationale": (
                    "Correct. The data shows a real relationship between unremediated critical findings and "
                    "increased probing activity — attackers are more persistently targeting hosts they can "
                    "detect as vulnerable. Fixing the underlying vulnerabilities (reducing MTTR for aging "
                    "critical findings) addresses the root cause of the alert volume, rather than just tuning "
                    "the SIEM to see less of the symptom."
                ),
            },
            {
                "id": "b",
                "text": "Suppress all low-severity reconnaissance and probing alerts SIEM-wide, since they are described as 'low-severity' in the correlation report.",
                "correct": False,
                "rationale": (
                    "Incorrect. Blanket suppression of reconnaissance alerts removes early-warning visibility "
                    "that is specifically more meaningful on hosts with known critical exposures, and does "
                    "nothing to address why the probing is elevated in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Reduce the SIEM's data retention period so older correlation trends like this are no longer visible in reporting.",
                "correct": False,
                "rationale": (
                    "Incorrect. Hiding the trend by shortening retention removes the very visibility that "
                    "revealed the underlying problem, rather than solving it."
                ),
            },
            {
                "id": "d",
                "text": "Move all hosts with critical findings older than 60 days off the network entirely until they are patched.",
                "correct": False,
                "rationale": (
                    "Incorrect. Wholesale removal of production hosts from the network is a disproportionate "
                    "operational disruption compared to the more direct and appropriate fix of accelerating "
                    "remediation of the aging critical findings themselves."
                ),
            },
        ],
        "explanation": (
            "A demonstrated correlation between vulnerability age and probing/reconnaissance alert volume points "
            "to a vulnerability-management root cause, not a SIEM-tuning problem. Accelerating remediation of "
            "aging critical findings reduces the underlying attacker interest driving the alerts, which is more "
            "effective than suppressing the symptom, hiding the trend, or taking hosts offline outright."
        ),
    },
    {
        "id": "tvul-031",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "NetFlow monitoring detects an unusual sustained outbound data transfer from an internal database "
            "server to an unfamiliar external IP address, and vulnerability management data confirms this same "
            "server has a critical, unpatched remote-code-execution CVE. Select the TWO actions the SOC analyst "
            "should take FIRST, before assuming this is confirmed exfiltration."
        ),
        "options": [
            {
                "id": "a",
                "text": "Correlate the NetFlow anomaly with the server's authentication logs, EDR telemetry, and the specific unpatched CVE's known exploitation indicators to determine whether the transfer is consistent with a compromise via that vulnerability or a legitimate scheduled process.",
                "correct": True,
                "rationale": (
                    "Correct. Combining the network anomaly with authentication, endpoint, and vulnerability-"
                    "specific exploitation indicators is the standard enrichment step needed to determine whether "
                    "this is genuine compromise-driven exfiltration or a benign explanation such as a scheduled "
                    "backup job, before escalating."
                ),
            },
            {
                "id": "b",
                "text": "Check whether the destination IP and transfer pattern match a known, authorized business process (e.g., a nightly backup or data-sync job to an approved partner).",
                "correct": True,
                "rationale": (
                    "Correct. Ruling out a known, authorized business process is a standard and necessary "
                    "triage step before treating an anomalous transfer as a confirmed security incident, even "
                    "when the host is separately known to have a critical unpatched vulnerability."
                ),
            },
            {
                "id": "c",
                "text": "Immediately wipe and reimage the database server without further investigation, since the combination of the transfer and the known CVE is sufficient proof of compromise.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging before investigation would destroy volatile evidence needed to confirm "
                    "whether compromise actually occurred and, if so, its scope — this is premature and "
                    "irreversible action taken before verification."
                ),
            },
            {
                "id": "d",
                "text": "Publicly disclose the potential breach to customers immediately, before internal verification is complete.",
                "correct": False,
                "rationale": (
                    "Incorrect. Public disclosure is a late-stage action that follows confirmed incident "
                    "determination and legal/communications review — it is far too early during initial triage "
                    "and correlation."
                ),
            },
        ],
        "explanation": (
            "Proper SIEM alert triage combines the anomalous signal with correlated context — endpoint, "
            "authentication, and known vulnerability exploitation indicators — and rules out legitimate business "
            "explanations before escalating to a confirmed incident. Destructive response actions and public "
            "disclosure both come later, only after verification."
        ),
    },
    {
        "id": "tvul-032",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC lead reviewing quarterly SIEM metrics notices that the analyst team's alert-closure rate has "
            "improved significantly, but a parallel review of closed tickets shows a growing number were closed "
            "as 'false positive' without any documented investigation steps, and several later turned out to "
            "correspond to confirmed vulnerability scan findings that were never actually remediated. What does "
            "this reveal, and what is the appropriate response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The improved closure-rate metric was likely achieved by under-investigating alerts rather than genuinely resolving more threats; the team should require documented verification steps (e.g., cross-checking against vulnerability management data) before closing an alert as a false positive, and treat closure rate alongside quality metrics rather than as a standalone success indicator.",
                "correct": True,
                "rationale": (
                    "Correct. A rising closure rate paired with undocumented, unverified false-positive "
                    "dispositions is a classic sign that a single metric is being optimized at the expense of "
                    "actual detection quality. The fix is requiring documented verification (including checking "
                    "against known vulnerability data) before closure, and evaluating closure rate together with "
                    "quality indicators, not in isolation."
                ),
            },
            {
                "id": "b",
                "text": "The improved closure rate is unambiguously good news and should be reported to leadership as evidence the SOC is performing better, with no further review needed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Taking the closure-rate improvement at face value, without accounting for the "
                    "undocumented false-positive closures and missed confirmed findings, would report a "
                    "misleadingly positive picture of SOC performance."
                ),
            },
            {
                "id": "c",
                "text": "The SIEM platform itself must be malfunctioning and generating incorrect alerts, and should be replaced.",
                "correct": False,
                "rationale": (
                    "Incorrect. The SIEM correctly generated alerts corresponding to real, confirmed "
                    "vulnerabilities; the failure was in the analyst triage/closure process, not in the "
                    "platform's detection capability."
                ),
            },
            {
                "id": "d",
                "text": "The vulnerability scanning program should be discontinued, since its findings are apparently unrelated to what the SIEM is alerting on.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario shows the opposite problem — the vulnerability scan findings were "
                    "relevant and should have been cross-checked during alert triage but were not; discontinuing "
                    "scanning would remove data that should be used more, not less."
                ),
            },
        ],
        "explanation": (
            "A single efficiency metric like alert-closure rate can be gamed by under-investigating and "
            "mislabeling alerts as false positives. Program leads should pair such metrics with quality controls "
            "— documented verification steps, including cross-referencing vulnerability management data — to "
            "ensure closure speed does not come at the cost of missing real, confirmed exposures."
        ),
    },
    # ---------------------------------------------------------------
    # Hardening & secure baselines (8) — domain 4, objective 4.1
    # ---------------------------------------------------------------
    {
        "id": "tvul-033",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A vulnerability scan of 60 newly provisioned Linux servers finds that all 60 have Telnet and an "
            "outdated SSH configuration allowing password authentication, even though the organization's "
            "hardening policy explicitly prohibits both. Investigation shows all 60 were cloned from the same "
            "golden image, which was last updated 18 months ago, before the policy was written. What is the "
            "MOST effective fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Update the golden image itself to reflect the current hardening policy (disable Telnet, enforce key-based SSH authentication), redeploy or reconfigure the 60 existing servers to match, and add a recurring review step so the golden image is kept in sync with policy changes going forward.",
                "correct": True,
                "rationale": (
                    "Correct. Since every affected server was cloned from the same outdated golden image, the "
                    "root cause is the image itself, not each individual server. Fixing the image, applying the "
                    "corrected configuration to already-deployed hosts, and adding a recurring review process "
                    "prevents the same class of finding from recurring on every future deployment."
                ),
            },
            {
                "id": "b",
                "text": "Manually reconfigure each of the 60 servers individually, without ever updating the golden image they were cloned from.",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving the golden image itself unpatched guarantees every future server cloned "
                    "from it will reintroduce the same Telnet/SSH misconfiguration, so the underlying source of "
                    "the problem remains unaddressed."
                ),
            },
            {
                "id": "c",
                "text": "Accept the finding as a known limitation of the current golden image and document it as a permanent exemption for all servers cloned from it.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a directly fixable configuration issue, not a case where the control "
                    "genuinely cannot be applied; granting a permanent exemption instead of fixing the image "
                    "leaves an easily preventable weakness in place indefinitely."
                ),
            },
            {
                "id": "d",
                "text": "Increase the frequency of vulnerability scans on these 60 servers so the same finding is reported more often for visibility.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning more frequently would only surface the same known, already-understood "
                    "misconfiguration more often without fixing its source in the golden image."
                ),
            },
        ],
        "explanation": (
            "When a hardening finding is traced to a shared, outdated golden image, the correct fix is at the "
            "image/template level, followed by remediation of already-deployed hosts and a recurring process to "
            "keep the image aligned with current policy — not one-off manual fixes, a blanket exemption, or "
            "more frequent scanning of the same unfixed source."
        ),
    },
    {
        "id": "tvul-034",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A CIS-CAT (SCAP-based) compliance scan reports a Linux fleet as 91% compliant against the CIS "
            "Benchmark, with the failing 9% concentrated in three control areas: audit log retention set below "
            "the required minimum, password history not enforced, and the root account not restricted to "
            "console-only login. Given limited remediation time this sprint, which failed control category "
            "should generally be prioritized FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Restricting root account login to console-only, since an unrestricted root account reachable over the network represents the most direct path to full system compromise of any of the three failing controls.",
                "correct": True,
                "rationale": (
                    "Correct. Among the three, an unrestricted root account that can be reached remotely "
                    "represents the most severe and directly exploitable weakness — a successful credential "
                    "compromise or brute-force attempt against it grants immediate full administrative control "
                    "of the system, which outweighs the audit-log retention and password-history gaps in "
                    "immediate risk."
                ),
            },
            {
                "id": "b",
                "text": "Password history enforcement, since it is listed first alphabetically among the three failing controls.",
                "correct": False,
                "rationale": (
                    "Incorrect. The order in which findings happen to be listed carries no risk information; "
                    "prioritization should be based on the actual security impact of each failing control, not "
                    "presentation order."
                ),
            },
            {
                "id": "c",
                "text": "Audit log retention, since compliance reporting always takes precedence over any technical control weakness.",
                "correct": False,
                "rationale": (
                    "Incorrect. While audit log retention supports investigations and compliance, it does not "
                    "directly prevent compromise the way restricting a powerful, remotely reachable "
                    "administrative account does; it is not automatically the top priority among these three."
                ),
            },
            {
                "id": "d",
                "text": "All three should be given exactly equal priority and worked in parallel regardless of differing potential impact.",
                "correct": False,
                "rationale": (
                    "Incorrect. With limited remediation time, treating clearly different-impact findings as "
                    "equally urgent ignores the risk-based prioritization that a compliance scan's underlying "
                    "controls are meant to support."
                ),
            },
        ],
        "explanation": (
            "Even within a configuration/baseline compliance report, failed controls still warrant risk-based "
            "prioritization rather than uniform or arbitrary treatment. A control that directly limits exposure "
            "of a powerful account (root login restriction) generally represents higher immediate risk than "
            "logging retention or password-history settings."
        ),
    },
    {
        "id": "tvul-035",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A finance department requests an exception to the organization's CIS-based hardening baseline "
            "because their legacy reporting application will not function unless SMBv1 remains enabled on the "
            "three servers it runs on. Migrating the application is planned but nine months away. Which "
            "response correctly follows secure-baseline exception governance?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Grant a documented, time-bound baseline exception scoped to only those three servers, paired with a compensating control (network segmentation isolating SMBv1 traffic to only the systems that require it) and a re-review date tied to the migration timeline.",
                "correct": True,
                "rationale": (
                    "Correct. A legitimate, narrow business constraint on a small set of systems calls for a "
                    "scoped, documented, time-bound exception with a compensating control — not a blanket "
                    "policy change or an unmanaged, permanent gap. Segmentation limits the insecure protocol's "
                    "exposure while the underlying application dependency still exists."
                ),
            },
            {
                "id": "b",
                "text": "Disable SMBv1 enforcement in the baseline policy organization-wide so the finance servers are no longer out of compliance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Weakening the baseline for the entire organization to accommodate a narrow, "
                    "three-server business constraint unnecessarily reintroduces the insecure protocol's risk "
                    "everywhere else where no such constraint exists."
                ),
            },
            {
                "id": "c",
                "text": "Deny the request outright and force the application offline immediately, without regard for the planned migration timeline or any compensating controls.",
                "correct": False,
                "rationale": (
                    "Incorrect. Abruptly taking a still-needed business application offline is a disproportionate "
                    "response when a scoped exception with a compensating control can manage the interim risk "
                    "while the planned migration proceeds."
                ),
            },
            {
                "id": "d",
                "text": "Grant a permanent, indefinite exemption with no compensating control and no scheduled re-review, since the application will eventually be migrated anyway.",
                "correct": False,
                "rationale": (
                    "Incorrect. An undocumented or indefinite exception without a compensating control or "
                    "re-review date leaves the insecure protocol exposed with no interim risk reduction and no "
                    "accountability checkpoint."
                ),
            },
        ],
        "explanation": (
            "Baseline exceptions, like vulnerability findings, should be scoped narrowly to the systems with the "
            "genuine constraint, paired with a compensating control that reduces real exposure, and tied to a "
            "documented re-review date aligned with the actual remediation plan — not resolved by weakening the "
            "baseline everywhere, an abrupt shutdown, or an unmanaged permanent gap."
        ),
    },
    {
        "id": "tvul-036",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A newly hired systems administrator manually built a production web server rather than deploying "
            "from the standard golden image, citing time pressure. Its first vulnerability/compliance scan "
            "shows 30+ baseline deviations: an active guest account, an open management port not present on any "
            "other server, and several unnecessary services running. What does this incident reveal about the "
            "provisioning process, and what is the most effective long-term fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Manual, ad hoc server builds bypass the controls baked into the standard golden image/infrastructure-as-code pipeline; the long-term fix is to enforce that all production systems are provisioned only through the automated pipeline (e.g., via access controls or approval gates that block manual builds), not just to fix this one server's findings.",
                "correct": True,
                "rationale": (
                    "Correct. The 30+ deviations are a direct symptom of bypassing the automated, policy-"
                    "enforced provisioning pipeline. Fixing only this one server's specific findings would leave "
                    "the process gap open for the next time-pressured manual build; the durable fix is "
                    "preventing manual builds from reaching production at all."
                ),
            },
            {
                "id": "b",
                "text": "Manually fix the 30+ findings on this one server and consider the matter closed, since it is now an isolated, already-known exception.",
                "correct": False,
                "rationale": (
                    "Incorrect. Fixing only this server's specific findings does nothing to prevent the same "
                    "process failure (a manual build bypassing the golden image pipeline) from happening again "
                    "with the next time-pressured deployment."
                ),
            },
            {
                "id": "c",
                "text": "Conclude that the golden image process itself is broken and should be abandoned in favor of manual builds for all future servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. This incident demonstrates the opposite: bypassing the golden image process is "
                    "what caused the extensive misconfiguration; the golden image approach is the control that "
                    "should be enforced more strictly, not discarded."
                ),
            },
            {
                "id": "d",
                "text": "Take no corrective action on the provisioning process, since this was a one-time exception caused by unusual time pressure.",
                "correct": False,
                "rationale": (
                    "Incorrect. Time pressure on deployments is a recurring operational reality, not a one-time "
                    "event; without a process control preventing manual builds, the same bypass is likely to "
                    "happen again under similar pressure."
                ),
            },
        ],
        "explanation": (
            "A heavily misconfigured host built outside the standard provisioning pipeline is a process failure, "
            "not just a one-off technical finding. The durable fix enforces that production systems can only be "
            "provisioned through the golden image/IaC pipeline, closing the gap that allowed a manual, "
            "unhardened build to reach production in the first place."
        ),
    },
    {
        "id": "tvul-037",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A federal contractor's security team is deciding which secure configuration baseline to apply to a "
            "new fleet of Windows servers supporting a Department of Defense contract, versus the baseline "
            "already used for the company's purely commercial servers. Which statement correctly distinguishes "
            "the two available baseline resources?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CIS Benchmarks are vendor-neutral, broadly applicable secure configuration baselines suitable for the commercial servers, while DISA STIGs (Security Technical Implementation Guides) are the more stringent, mandated baseline typically required for systems supporting U.S. government/DoD contracts.",
                "correct": True,
                "rationale": (
                    "Correct. CIS Benchmarks provide general-purpose, industry-consensus hardening guidance "
                    "widely used across commercial environments, while DISA STIGs are the specific, often more "
                    "stringent configuration standards mandated for systems used in U.S. Department of Defense "
                    "and related government contexts — exactly the distinction relevant to this contractor's "
                    "two server populations."
                ),
            },
            {
                "id": "b",
                "text": "CIS Benchmarks and DISA STIGs are two names for the exact same set of configuration settings, so either can be used interchangeably for both populations.",
                "correct": False,
                "rationale": (
                    "Incorrect. CIS Benchmarks and DISA STIGs are separately maintained, distinct baseline "
                    "standards with differing scope and stringency; they are not interchangeable, especially "
                    "when a specific contract mandates STIG compliance."
                ),
            },
            {
                "id": "c",
                "text": "DISA STIGs apply only to network hardware and have no baseline guidance applicable to Windows servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. DISA publishes STIGs covering a wide range of technologies, including detailed "
                    "Windows Server configuration guides, not just network hardware."
                ),
            },
            {
                "id": "d",
                "text": "CIS Benchmarks are only usable for cloud workloads and cannot be applied to on-premises Windows servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. CIS Benchmarks cover a broad range of platforms including on-premises operating "
                    "systems like Windows Server, not just cloud environments."
                ),
            },
        ],
        "explanation": (
            "CIS Benchmarks and DISA STIGs are both recognized secure configuration baselines, but they serve "
            "different contexts: CIS Benchmarks are vendor-neutral and broadly used commercially, while STIGs "
            "are the specific, typically more stringent baseline mandated for systems supporting U.S. government "
            "and defense contracts."
        ),
    },
    {
        "id": "tvul-038",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A server passed its secure-baseline compliance scan at deployment six months ago with a 98% score. "
            "A follow-up compliance scan this month shows the score has dropped to 74%, with several controls "
            "that previously passed (password policy settings, disabled guest account, restricted remote "
            "registry access) now failing, even though no formal change request was filed for any of those "
            "settings. What does this indicate, and what is the correct response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This is configuration drift — ad hoc, undocumented changes made outside change management have moved the host away from its approved baseline; the team should investigate what caused each regression, restore the approved settings, and deploy configuration-management/enforcement tooling that automatically detects and corrects drift going forward.",
                "correct": True,
                "rationale": (
                    "Correct. A previously compliant host regressing over time with no corresponding change "
                    "record is the definition of configuration drift, typically caused by undocumented manual "
                    "changes. The fix is investigating and restoring the approved settings, and adding "
                    "automated drift detection/enforcement (e.g., configuration management tooling that "
                    "continuously reasserts the desired state) to prevent recurrence."
                ),
            },
            {
                "id": "b",
                "text": "The compliance scanning tool must be misconfigured, since a server that passed at 98% should never show a lower score later without an explicit change request.",
                "correct": False,
                "rationale": (
                    "Incorrect. Regression without a documented change is a well-known real phenomenon "
                    "(configuration drift from undocumented manual administration), not primarily evidence of a "
                    "scanning tool defect."
                ),
            },
            {
                "id": "c",
                "text": "A 74% compliance score is still generally acceptable, so no investigation or remediation is needed.",
                "correct": False,
                "rationale": (
                    "Incorrect. A significant, unexplained drop from a previously much higher score — "
                    "particularly affecting security-relevant controls like password policy and remote registry "
                    "access — represents a real regression that should be investigated and corrected, not "
                    "accepted as adequate."
                ),
            },
            {
                "id": "d",
                "text": "Rebuild the server entirely from scratch every time its compliance score drops, regardless of how minor the individual regressions are.",
                "correct": False,
                "rationale": (
                    "Incorrect. A full rebuild is a disproportionate response to correctable configuration "
                    "drift when the specific regressed settings can be identified and restored directly, and "
                    "automated enforcement tooling can prevent the drift from recurring without requiring a "
                    "rebuild each time."
                ),
            },
        ],
        "explanation": (
            "A compliance score regressing over time with no corresponding change record indicates "
            "configuration drift from undocumented manual changes. The correct response restores the approved "
            "baseline settings and introduces automated configuration-management enforcement to detect and "
            "correct drift continuously, rather than dismissing the regression, blaming the tooling, or "
            "resorting to a full rebuild."
        ),
    },
    {
        "id": "tvul-039",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A cloud security posture management (CSPM) baseline scan flags a storage bucket as publicly "
            "readable, containing customer export files, in direct violation of the organization's cloud "
            "secure-baseline policy. Select the TWO actions that correctly address both the immediate exposure "
            "and the underlying process gap that allowed it."
        ),
        "options": [
            {
                "id": "a",
                "text": "Immediately correct the bucket's access policy to remove public read access and restrict it to only the specific roles/accounts that require it.",
                "correct": True,
                "rationale": (
                    "Correct. The immediate priority is closing the active exposure by correcting the "
                    "misconfigured access policy so the customer data is no longer publicly readable, which is "
                    "the direct fix for the confirmed baseline violation."
                ),
            },
            {
                "id": "b",
                "text": "Implement a policy-as-code guardrail (e.g., an automated CSPM/IaC policy check) that prevents storage resources from being provisioned or modified into a publicly readable state going forward, rather than relying solely on periodic scans to catch it after the fact.",
                "correct": True,
                "rationale": (
                    "Correct. A preventive guardrail enforced at provisioning/deployment time stops this class "
                    "of misconfiguration from recurring, closing the process gap that allowed a public bucket to "
                    "exist in the first place rather than relying only on periodic detection."
                ),
            },
            {
                "id": "c",
                "text": "Delete the CSPM scanning tool's alert history for this finding so the bucket no longer shows as a past violation in reporting.",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting the alert history destroys the audit trail documenting the exposure and "
                    "its remediation, without addressing either the immediate risk or the underlying process "
                    "gap."
                ),
            },
            {
                "id": "d",
                "text": "Leave the bucket's access policy unchanged and only document the finding as accepted risk, since cloud storage misconfigurations are considered unavoidable.",
                "correct": False,
                "rationale": (
                    "Incorrect. A publicly readable bucket containing customer data is a directly fixable "
                    "misconfiguration, not an unavoidable condition; accepting the risk without correcting the "
                    "access policy leaves customer data actively exposed."
                ),
            },
        ],
        "explanation": (
            "Cloud baseline violations require both immediate remediation (correcting the misconfigured access "
            "policy to close the exposure) and a preventive process fix (policy-as-code guardrails that block "
            "the same misconfiguration from being deployed again) — not deleting the evidence or accepting an "
            "easily fixable exposure as inevitable."
        ),
    },
    {
        "id": "tvul-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A security team wants to shorten the time between a host drifting out of its secure baseline and "
            "that drift being corrected, rather than waiting for the next scheduled monthly SCAP compliance "
            "scan to discover it. Which approach BEST accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy configuration-management/enforcement agents (e.g., continuously reasserting a desired-state policy) on managed hosts, so drifted settings are automatically detected and corrected between scheduled compliance scans rather than only at each monthly checkpoint.",
                "correct": True,
                "rationale": (
                    "Correct. Agent-based configuration management that continuously enforces a desired state "
                    "closes the visibility and correction gap between periodic compliance scans, automatically "
                    "catching and fixing drift as it happens instead of waiting up to a month for the next "
                    "scheduled scan to discover it."
                ),
            },
            {
                "id": "b",
                "text": "Reduce the SCAP compliance scan scope to only the most critical servers, so each scan completes faster and can theoretically run somewhat more often.",
                "correct": False,
                "rationale": (
                    "Incorrect. Narrowing scope trades coverage for speed and leaves excluded systems with no "
                    "detection at all; it does not meaningfully close the time gap for the systems that remain "
                    "in scope and reduces overall visibility."
                ),
            },
            {
                "id": "c",
                "text": "Switch from SCAP-based compliance scanning to CVE-based vulnerability scanning only, since vulnerability scans run more frequently.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVE-based vulnerability scanning checks for known software flaws, not baseline "
                    "configuration compliance; replacing configuration compliance checking with vulnerability "
                    "scanning would lose visibility into drift entirely rather than detecting it faster."
                ),
            },
            {
                "id": "d",
                "text": "Extend the compliance scan interval from monthly to quarterly to reduce operational overhead on the scanning infrastructure.",
                "correct": False,
                "rationale": (
                    "Incorrect. Lengthening the interval between scans widens, rather than closes, the window "
                    "during which drift can go undetected — the opposite of what the team is trying to achieve."
                ),
            },
        ],
        "explanation": (
            "Periodic SCAP compliance scanning alone leaves a detection gap between checkpoints. Continuous, "
            "agent-based configuration-management enforcement closes that gap by automatically detecting and "
            "correcting drift as it happens, rather than narrowing scan scope, substituting a different type of "
            "scan, or lengthening the interval between checks."
        ),
    },
]
