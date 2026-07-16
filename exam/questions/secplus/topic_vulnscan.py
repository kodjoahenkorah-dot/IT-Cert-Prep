"""CompTIA Security+ SY0-701 practice questions — topical batch: vulnerability scan
interpretation.

Scenarios center on reading small vulnerability-scan result tables (CVE, CVSS base
score, exploit/threat-intel status, exposure) and making the correct real-world risk
call: what to patch first, when a finding is a false positive vs. a true positive,
when a compensating control or virtual patch is appropriate, exception vs. exemption,
credentialed vs. uncredentialed scanning, and verification/rescanning after remediation.
"""

QUESTIONS = [
    # ---------------------------------------------------------------
    # Vulnerability management & CVSS (30) — domain 4, objective 4.3
    # ---------------------------------------------------------------
    {
        "id": "tvln-001",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A quarterly authenticated vulnerability scan returns the following findings:\n\n"
            "CVE              CVSS Base   Exploit / Threat Intel                              Exposure\n"
            "CVE-2024-30442    9.8        No known public exploit code                         Internal ERP database, isolated VLAN, no internet route\n"
            "CVE-2024-30478    7.2        Actively exploited in the wild; listed in CISA KEV   Internet-facing VPN gateway\n"
            "CVE-2024-30501    6.4        Proof-of-concept exploit published, not seen in the wild   Internal file server\n"
            "CVE-2024-30519    5.3        No known exploit code                                Internet-facing marketing website\n\n"
            "With only enough change-window capacity to patch one system before the weekend, which CVE should the team remediate FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CVE-2024-30478 on the internet-facing VPN gateway",
                "correct": True,
                "rationale": (
                    "Correct. It is internet-facing, remotely reachable by any attacker, and confirmed as "
                    "actively exploited (CISA KEV). Real-world exploitation plus direct internet exposure "
                    "outweighs a higher base score on an isolated internal system with no known exploit."
                ),
            },
            {
                "id": "b",
                "text": "CVE-2024-30442 on the internal ERP database, since it has the highest CVSS base score",
                "correct": False,
                "rationale": (
                    "Incorrect. CVSS base score alone ignores exploitability and exposure. This host is on an "
                    "isolated VLAN with no internet route and no known exploit code, so the realistic likelihood "
                    "of exploitation this week is far lower than the actively-exploited VPN finding."
                ),
            },
            {
                "id": "c",
                "text": "CVE-2024-30501 on the internal file server, since a proof-of-concept exploit already exists",
                "correct": False,
                "rationale": (
                    "Incorrect. A published PoC raises risk versus no exploit code at all, but it has not been "
                    "observed in the wild and the asset is internal, not internet-facing — lower real risk than "
                    "an internet-facing system already under active attack."
                ),
            },
            {
                "id": "d",
                "text": "CVE-2024-30519 on the internet-facing marketing website, since it is internet-facing",
                "correct": False,
                "rationale": (
                    "Incorrect. Internet exposure alone is not sufficient; this finding has the lowest severity "
                    "and no known exploit code, making it far less urgent than a KEV-listed, actively exploited "
                    "finding on another internet-facing system."
                ),
            },
        ],
        "explanation": (
            "Real-world prioritization is exposure x exploitability, not CVSS base score alone. An "
            "internet-facing, actively exploited (CISA KEV) finding must be remediated before a higher-scoring "
            "but isolated, unexploited finding, because the probability of imminent compromise is what drives "
            "actual risk."
        ),
    },
    {
        "id": "tvln-002",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability manager is building this week's remediation queue from scan output:\n\n"
            "Host                CVE              CVSS Base   Notes\n"
            "web-edge-03          CVE-2025-1187    8.6         Internet-facing reverse proxy; vendor patch available; no known exploit in the wild\n"
            "print-svc-11         CVE-2025-1204    9.1         Print server on an internal-only VLAN with no route to the internet or to sensitive segments\n"
            "vpn-gw-02            CVE-2025-1240    7.8         Internet-facing SSL VPN concentrator; exploit code weaponized and added to CISA KEV yesterday\n"
            "jump-host-14         CVE-2025-1255    8.9         Internal jump box reachable only from the security team's management subnet\n\n"
            "Which host should receive emergency, out-of-cycle patching rather than waiting for the normal weekly maintenance window?"
        ),
        "options": [
            {
                "id": "a",
                "text": "vpn-gw-02 — internet-facing with a weaponized exploit newly added to CISA KEV",
                "correct": True,
                "rationale": (
                    "Correct. A weaponized exploit that just entered CISA's Known Exploited Vulnerabilities "
                    "catalog on an internet-facing VPN concentrator represents imminent, active attacker "
                    "capability against a directly reachable system — this warrants breaking the normal cadence."
                ),
            },
            {
                "id": "b",
                "text": "print-svc-11 — it has the highest CVSS base score of the four findings",
                "correct": False,
                "rationale": (
                    "Incorrect. The highest base score belongs to a host with no internet route and no known "
                    "exploitation activity; base score alone, without considering exposure or exploit maturity, "
                    "does not justify jumping the queue ahead of an actively weaponized internet-facing finding."
                ),
            },
            {
                "id": "c",
                "text": "web-edge-03 — because it is internet-facing and a patch is already available",
                "correct": False,
                "rationale": (
                    "Incorrect. Being internet-facing with an available patch matters, but there is no evidence "
                    "of active exploitation here; it belongs in the normal weekly cycle rather than displacing "
                    "the KEV-listed emergency."
                ),
            },
            {
                "id": "d",
                "text": "jump-host-14 — because jump hosts are always considered crown-jewel assets",
                "correct": False,
                "rationale": (
                    "Incorrect. This jump host is only reachable from the restricted security management "
                    "subnet, significantly limiting real exposure; it does not outrank an actively exploited, "
                    "internet-facing KEV finding."
                ),
            },
        ],
        "explanation": (
            "Newly weaponized exploits added to the CISA KEV catalog against internet-facing infrastructure "
            "represent the highest real-world urgency and typically justify emergency, out-of-cycle patching, "
            "even when other findings carry a higher raw CVSS base score."
        ),
    },
    {
        "id": "tvln-003",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan report lists CVE-2025-2201 with a CVSS v3.1 base score of 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) "
            "on a public-facing API gateway. The organization's environmental scoring, which factors in that this API "
            "gateway sits behind a mutual-TLS requirement and an authenticated API key gate that the base score does "
            "not account for, produces an adjusted environmental score of 6.1. Which statement BEST explains why the "
            "environmental score differs from the base score?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The base score reflects the vulnerability's intrinsic characteristics in a generic environment, while the environmental score adjusts that base value to reflect compensating controls and configuration specific to this organization's deployment.",
                "correct": True,
                "rationale": (
                    "Correct. CVSS base metrics are static and vendor-published, describing worst-case severity "
                    "independent of deployment context. The environmental metric group lets an organization "
                    "adjust the score to reflect real controls in place, such as mTLS and API-key gating, that "
                    "reduce actual exploitability here."
                ),
            },
            {
                "id": "b",
                "text": "The environmental score is simply an error and the base score of 9.8 should always be used for prioritization instead.",
                "correct": False,
                "rationale": (
                    "Incorrect. The environmental score is a legitimate, intentional part of the CVSS "
                    "specification, not an error; using only the generic base score would ignore real "
                    "compensating controls specific to this deployment."
                ),
            },
            {
                "id": "c",
                "text": "The environmental score reflects how much exploit code maturity has increased since the CVE was published.",
                "correct": False,
                "rationale": (
                    "Incorrect. Exploit code maturity is part of the temporal (or CVSS 4.0 threat) metric group, "
                    "not the environmental group, which instead reflects security requirements and modified base "
                    "metrics from an organization's specific deployment."
                ),
            },
            {
                "id": "d",
                "text": "CVSS scores are recalculated automatically by the vendor once a patch becomes available, which explains the lower number.",
                "correct": False,
                "rationale": (
                    "Incorrect. Patch availability does not by itself change either the base or environmental "
                    "score; the environmental adjustment here comes from the organization's own compensating "
                    "controls (mTLS, API key gate), not from vendor patch status."
                ),
            },
        ],
        "explanation": (
            "CVSS base scores are static and context-free; environmental scores let an organization tailor the "
            "score using its actual deployment (compensating controls, criticality, exposure). A high base score "
            "can legitimately produce a lower environmental score when strong compensating controls reduce real "
            "exploitability, which should inform — but not automatically override — prioritization decisions."
        ),
    },
    {
        "id": "tvln-004",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "Two findings from this week's scan both affect the same unpatched load-balancer firmware:\n\n"
            "CVE-2025-4410: CVSS base 7.5. Temporal metrics show Exploit Code Maturity = 'Proof-of-Concept', "
            "Remediation Level = 'Official Fix', Report Confidence = 'Confirmed'.\n"
            "CVE-2025-4433: CVSS base 7.1. Temporal metrics show Exploit Code Maturity = 'Functional', "
            "Remediation Level = 'Unavailable', Report Confidence = 'Confirmed'.\n\n"
            "Both affect internet-facing load balancers with equivalent exposure. Which finding should be treated "
            "as the higher priority, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CVE-2025-4433, because its 'Functional' exploit code maturity combined with 'Unavailable' remediation makes it both easier to exploit right now and harder to immediately fix.",
                "correct": True,
                "rationale": (
                    "Correct. Temporal metrics adjust urgency based on real-world exploit maturity and fix "
                    "availability. Functional exploit code is more dangerous than proof-of-concept code, and the "
                    "lack of an official fix means the team must also stand up interim mitigations rather than "
                    "simply scheduling a patch."
                ),
            },
            {
                "id": "b",
                "text": "CVE-2025-4410, because it has the higher CVSS base score of the two.",
                "correct": False,
                "rationale": (
                    "Incorrect. The base score difference (7.5 vs 7.1) is marginal, and CVE-2025-4410 already "
                    "has an official fix and only proof-of-concept exploit code — it is objectively less urgent "
                    "right now than a functionally exploitable, unpatched flaw."
                ),
            },
            {
                "id": "c",
                "text": "Both are equally urgent and should simply be patched in CVE numerical order.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVE numbers carry no risk information; treating findings as equally urgent "
                    "ignores the meaningful difference in exploit maturity and fix availability that the "
                    "temporal metrics reveal."
                ),
            },
            {
                "id": "d",
                "text": "Neither is urgent because both remain below the 8.0 CVSS threshold commonly used to define 'critical'.",
                "correct": False,
                "rationale": (
                    "Incorrect. Rigid adherence to a numeric severity band while ignoring exploit maturity and "
                    "remediation availability is exactly the mistake temporal scoring is meant to correct; a "
                    "functionally exploited, unpatched flaw on internet-facing infrastructure is urgent regardless "
                    "of falling just under a 'critical' cutoff."
                ),
            },
        ],
        "explanation": (
            "Temporal metrics (exploit code maturity, remediation level, report confidence) refine the base "
            "score to reflect current real-world conditions. A lower base score with functional exploit code and "
            "no available fix can be more urgent than a higher base score that already has an official patch and "
            "only proof-of-concept exploitation."
        ),
    },
    {
        "id": "tvln-005",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability scan flags CVE-2025-5502 (CVSS 9.1, remote code execution) on a legacy build server. "
            "The vendor has announced end-of-life for the affected software with no patch forthcoming. The build "
            "server is scheduled for internet exposure next month to support a new CI/CD integration. Which action "
            "MOST directly reduces real risk in the interim, before decommissioning or replacement can occur?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Restrict network access to the build server to only the specific internal CI/CD hosts that require it, and delay the planned internet exposure until a patched or replacement platform is in place.",
                "correct": True,
                "rationale": (
                    "Correct. Since no vendor patch exists, a compensating control that reduces exposure — "
                    "network segmentation limiting reachability to only what is strictly necessary, and delaying "
                    "the internet exposure — directly reduces the realistic attack surface until remediation is "
                    "possible."
                ),
            },
            {
                "id": "b",
                "text": "Proceed with the planned internet exposure on schedule, since the CI/CD integration is a business priority.",
                "correct": False,
                "rationale": (
                    "Incorrect. Exposing an unpatchable, remotely exploitable server to the internet directly "
                    "increases the attack surface for a critical, unfixable vulnerability — this is the opposite "
                    "of risk reduction."
                ),
            },
            {
                "id": "c",
                "text": "Lower the finding's severity in the vulnerability management tool to 'informational' since no patch is available and nothing else can be done.",
                "correct": False,
                "rationale": (
                    "Incorrect. Downgrading severity to make a risk disappear from reporting does not reduce "
                    "actual risk and misrepresents the organization's true exposure; a patch being unavailable "
                    "calls for compensating controls, not re-labeling."
                ),
            },
            {
                "id": "d",
                "text": "Wait for the vendor to eventually issue a patch before taking any other action.",
                "correct": False,
                "rationale": (
                    "Incorrect. The vendor has already announced end-of-life with no patch forthcoming, so "
                    "waiting indefinitely leaves the critical, remotely exploitable flaw fully exposed with no "
                    "mitigation in place."
                ),
            },
        ],
        "explanation": (
            "When no vendor patch exists, vulnerability management shifts to compensating controls: restricting "
            "network reachability, delaying planned exposure increases, and pursuing replacement/decommissioning "
            "— not ignoring the finding, downgrading it cosmetically, or proceeding with plans that increase "
            "exposure."
        ),
    },
    {
        "id": "tvln-006",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A business unit requests that a critical finding on a legacy point-of-sale application be closed "
            "without patching because the vendor says a fix will break the register hardware. Select the TWO "
            "statements that correctly distinguish a risk EXCEPTION from a risk EXEMPTION in this context."
        ),
        "options": [
            {
                "id": "a",
                "text": "An exception is a temporary, time-bound deviation from policy, typically paired with a compensating control and a defined expiration or re-review date.",
                "correct": True,
                "rationale": (
                    "Correct. An exception acknowledges the vulnerability cannot be remediated right now, "
                    "applies interim compensating controls (e.g., network isolation of the register segment), "
                    "and is explicitly time-bound with a scheduled re-review — it is not a permanent closure."
                ),
            },
            {
                "id": "b",
                "text": "An exemption is a longer-term or permanent waiver, formally approved by a risk owner, acknowledging the control genuinely cannot be applied to this asset class.",
                "correct": True,
                "rationale": (
                    "Correct. An exemption is used when a policy requirement structurally cannot apply (e.g., a "
                    "point-of-sale device that cannot be patched without breaking certified hardware) and is "
                    "granted with formal, documented risk-owner sign-off rather than an expectation of eventual "
                    "remediation."
                ),
            },
            {
                "id": "c",
                "text": "Both an exception and an exemption permanently remove the finding from the vulnerability scan report so it never needs to be reviewed again.",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither should silently suppress future visibility; exceptions are re-reviewed "
                    "at expiration, and even exemptions should remain tracked and periodically reassessed as risk "
                    "conditions change, not permanently hidden from reporting."
                ),
            },
            {
                "id": "d",
                "text": "An exception requires no compensating control and no approval, since it is only a documentation formality.",
                "correct": False,
                "rationale": (
                    "Incorrect. A properly governed exception requires documented risk acceptance, an approving "
                    "authority, and typically a compensating control — it is a formal risk-management decision, "
                    "not a rubber-stamp formality."
                ),
            },
        ],
        "explanation": (
            "Exceptions are temporary, reviewed periodically, and usually paired with compensating controls. "
            "Exemptions are longer-term or permanent waivers granted when a control structurally cannot apply, "
            "still require risk-owner approval, and should remain tracked rather than silently closed out."
        ),
    },
    {
        "id": "tvln-007",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "An uncredentialed external scan of a company's public IP range reports the web server as 'healthy' "
            "with no findings above medium severity. A credentialed internal scan of the same host, run the same "
            "week, reports a critical local privilege-escalation CVE in an outdated system library. Which "
            "statement BEST explains this discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Uncredentialed scans can only observe what is visible from outside the host (open ports, banners, responses), while credentialed scans authenticate to the host and can inspect installed package/library versions directly, revealing vulnerabilities invisible from the network alone.",
                "correct": True,
                "rationale": (
                    "Correct. Uncredentialed scanning is inherently limited to externally observable behavior. "
                    "Credentialed scanning logs into the host and enumerates actual installed software versions, "
                    "which is the only reliable way to detect local-privilege-escalation flaws in system "
                    "libraries that don't manifest in network responses."
                ),
            },
            {
                "id": "b",
                "text": "The credentialed scan result must be a false positive, since the uncredentialed scan already confirmed the server is healthy.",
                "correct": False,
                "rationale": (
                    "Incorrect. An uncredentialed scan finding nothing does not validate the host's true patch "
                    "state; it only reflects what is visible externally. Assuming the more thorough, "
                    "authenticated result is wrong reverses the correct interpretation."
                ),
            },
            {
                "id": "c",
                "text": "Credentialed scans always produce inflated severity scores compared to uncredentialed scans and should be discounted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Credentialed scans are generally considered more accurate, not inflated, because "
                    "they can verify actual installed versions rather than guessing from network banners; "
                    "discounting them removes the more reliable data source."
                ),
            },
            {
                "id": "d",
                "text": "The two scans must have targeted different hosts by mistake, since results should always match.",
                "correct": False,
                "rationale": (
                    "Incorrect. It is expected and normal for credentialed and uncredentialed scans of the same "
                    "host to produce different results because they use fundamentally different visibility; this "
                    "does not indicate a targeting error."
                ),
            },
        ],
        "explanation": (
            "Credentialed scans authenticate to the target and inspect installed software/patch levels directly, "
            "giving far deeper and more accurate visibility than uncredentialed scans, which can only infer "
            "conditions from externally observable network responses. This is why credentialed scanning is "
            "preferred for internal assets whenever feasible."
        ),
    },
    {
        "id": "tvln-008",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scanner flags CVE-2025-6120 (Apache HTTP Server, CVSS 8.2) on a production web server based on the "
            "'Server: Apache/2.4.41' banner returned in HTTP response headers. The Linux distribution vendor "
            "confirmed that its maintained package backports the security fix into version 2.4.41 without "
            "incrementing the displayed version string, and 'apt list --installed' on the host shows the patched "
            "package build number. What should the analyst do with this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mark the finding as a false positive, and document the vendor's backport confirmation and the verified installed package build number as evidence.",
                "correct": True,
                "rationale": (
                    "Correct. Version-string banner grabbing cannot detect vendor backporting, where a fix is "
                    "applied without changing the displayed version. Verified evidence (vendor advisory plus the "
                    "actual installed package build) confirms the host is patched, so the finding should be "
                    "closed as a documented false positive, not simply ignored."
                ),
            },
            {
                "id": "b",
                "text": "Patch the server immediately by upgrading to the latest upstream Apache release, overriding the distribution's maintained package.",
                "correct": False,
                "rationale": (
                    "Incorrect. The host is already confirmed patched via the vendor's backported package; "
                    "forcing an upstream override would abandon the distribution's supported, tested package "
                    "management and could introduce compatibility or support issues for no security benefit."
                ),
            },
            {
                "id": "c",
                "text": "Accept the risk without further documentation, since the finding is probably not a real issue.",
                "correct": False,
                "rationale": (
                    "Incorrect. Dismissing a critical-looking finding without documenting the verification "
                    "evidence leaves no audit trail and could later be mistaken for an unaddressed real "
                    "vulnerability; false positives must be documented, not just waved off."
                ),
            },
            {
                "id": "d",
                "text": "Suppress future alerts for this CVE across the entire fleet without verifying other hosts individually.",
                "correct": False,
                "rationale": (
                    "Incorrect. Backport status must be verified per host/package build; blanket suppression "
                    "across the fleet risks masking genuinely unpatched hosts running a different or outdated "
                    "package version."
                ),
            },
        ],
        "explanation": (
            "False positive handling requires verification (checking actual installed package state, not just "
            "banner version strings) and documentation of the evidence used to close the finding — not blind "
            "dismissal, blanket suppression, or unnecessary re-patching of an already-fixed host."
        ),
    },
    {
        "id": "tvln-009",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan reports CVE-2025-6300, a critical SQL injection finding, as remediated on host db-prod-07 "
            "after the patch management system logged a successful update job. Which action should the "
            "vulnerability management team take BEFORE closing the ticket as fully resolved?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run an authenticated rescan of db-prod-07 (or an exploit-based verification test) to confirm the specific CVE no longer detects as present.",
                "correct": True,
                "rationale": (
                    "Correct. A successful patch deployment job only confirms the installer executed — it does "
                    "not guarantee the vulnerable service was restarted or that the fix actually took effect. "
                    "Verification via rescan or exploit testing is required before a remediation ticket can be "
                    "considered truly closed."
                ),
            },
            {
                "id": "b",
                "text": "Close the ticket immediately, since the patch management system already reported success.",
                "correct": False,
                "rationale": (
                    "Incorrect. Deployment success in the patch tool is not equivalent to confirmed remediation; "
                    "closing without verification risks leaving a critical, exploitable flaw active while it is "
                    "reported as fixed."
                ),
            },
            {
                "id": "c",
                "text": "Escalate directly to the incident response team, since a critical CVE was found.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a routine remediation-verification step within vulnerability management, "
                    "not an active security incident; escalating to IR is unnecessary unless verification later "
                    "reveals the vulnerability is still exploitable or was actively exploited before the patch."
                ),
            },
            {
                "id": "d",
                "text": "Lower the CVSS score of the finding to reflect that a patch job was attempted.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVSS reflects the vulnerability's characteristics, not the status of a patch "
                    "deployment attempt; altering the score does not verify whether the vulnerability was "
                    "actually closed."
                ),
            },
        ],
        "explanation": (
            "Remediation is not confirmed by a 'successful' patch job alone. Vulnerability management best "
            "practice requires a verification step — an authenticated rescan or targeted exploit test — before "
            "marking a finding as closed, since partial application or a pending restart can leave the "
            "vulnerability exploitable despite a reported deployment success."
        ),
    },
    {
        "id": "tvln-010",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A manufacturing plant runs a programmable logic controller (PLC) with a confirmed critical "
            "remote-code-execution vulnerability (CVSS 9.6). The PLC vendor states no firmware update is planned "
            "for this hardware generation, and the PLC cannot be taken offline without halting the production "
            "line. Which mitigation strategy is MOST appropriate given these constraints?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Place the PLC on an isolated OT VLAN with strict ACLs limiting communication to only the specific engineering workstation and historian server it must talk to, monitored by an industrial IDS.",
                "correct": True,
                "rationale": (
                    "Correct. When a patch is unavailable and the asset cannot be taken offline, segmentation "
                    "that minimizes reachability to only essential communication paths — combined with dedicated "
                    "monitoring — is the standard compensating control for unpatchable OT/ICS devices."
                ),
            },
            {
                "id": "b",
                "text": "Leave the PLC on the general corporate network as-is, since production cannot be interrupted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving a critically vulnerable, unpatchable device broadly reachable on the "
                    "corporate network maximizes exposure and ignores the need for a compensating control; "
                    "production continuity and security are not mutually exclusive here."
                ),
            },
            {
                "id": "c",
                "text": "Wait for the vendor to eventually release a firmware update before taking any other action.",
                "correct": False,
                "rationale": (
                    "Incorrect. The vendor has explicitly stated no update is planned for this hardware "
                    "generation, so waiting indefinitely leaves the vulnerability fully exposed with no interim "
                    "protection."
                ),
            },
            {
                "id": "d",
                "text": "Reduce the finding's recorded severity to match the plant's uptime requirements so it no longer appears as critical in reporting.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting the reported severity to match operational convenience misrepresents "
                    "actual risk and does nothing to reduce the real exposure of an unpatched, critically "
                    "vulnerable PLC."
                ),
            },
        ],
        "explanation": (
            "For unpatchable OT/ICS assets that cannot be taken offline, segmentation and access restriction "
            "(isolating the device to only its required communication paths, with dedicated monitoring) is the "
            "standard compensating control, balancing operational continuity with risk reduction until "
            "replacement is feasible."
        ),
    },
    {
        "id": "tvln-011",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan of the corporate network reports the same critical CVE-2025-7010 twice for the same physical "
            "server: once under its management IP and once under its iSCSI storage-network IP, each treated as a "
            "separate open finding in the vulnerability management dashboard, inflating the open-finding count. "
            "What is the BEST way to handle this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Correlate and deduplicate the two findings to a single underlying asset (e.g., by hostname/hardware UUID) in the CMDB/scanner asset inventory, while still ensuring the single patch resolves both reported interfaces.",
                "correct": True,
                "rationale": (
                    "Correct. Multi-homed hosts frequently appear as multiple 'assets' when scanned across "
                    "different NICs/VLANs. Proper asset correlation (deduplication by hostname or hardware "
                    "identifier) keeps reporting accurate while confirming that remediating the host resolves "
                    "the underlying vulnerability on every interface."
                ),
            },
            {
                "id": "b",
                "text": "Ignore one of the two findings entirely without investigating why it appeared twice.",
                "correct": False,
                "rationale": (
                    "Incorrect. Simply ignoring a finding without confirming it is a duplicate of the same "
                    "underlying host risks silently dropping a legitimate finding on a genuinely different asset."
                ),
            },
            {
                "id": "c",
                "text": "Patch only the management-IP interface, since storage-network findings are never a security concern.",
                "correct": False,
                "rationale": (
                    "Incorrect. The vulnerability lives in the host/service itself, not the interface; both "
                    "reported IPs belong to the same vulnerable server and remediation must resolve the "
                    "underlying flaw regardless of which network interface it was scanned from."
                ),
            },
            {
                "id": "d",
                "text": "Increase the scan frequency on this host so the duplicate finding is reported more often for visibility.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning more frequently does not fix asset correlation; it would simply "
                    "generate the same duplicate finding more often without addressing the root cause of "
                    "inflated reporting."
                ),
            },
        ],
        "explanation": (
            "Multi-homed assets can appear as separate entries when scanned via different IP addresses. Accurate "
            "vulnerability management requires asset correlation/deduplication so that remediation efforts and "
            "open-finding metrics reflect the true number of distinct vulnerable systems, not inflated interface "
            "counts."
        ),
    },
    {
        "id": "tvln-012",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "The vulnerability management team is finalizing SLAs for remediation timelines. Which SLA structure "
            "MOST correctly reflects standard vulnerability management practice, combining severity with "
            "exploitability signals such as CISA KEV listing?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CISA KEV-listed or actively exploited findings get the shortest fixed window (e.g., 24-72 hours) regardless of base CVSS; remaining findings are then tiered by severity band (critical, high, medium, low) with progressively longer windows.",
                "correct": True,
                "rationale": (
                    "Correct. Active exploitation is the single strongest predictor of imminent compromise, so "
                    "KEV-listed/actively exploited findings should always receive the most aggressive remediation "
                    "window, with remaining findings tiered by CVSS severity band for everything not already "
                    "under active attack."
                ),
            },
            {
                "id": "b",
                "text": "All findings, regardless of severity or exploitation status, are given the same 90-day remediation window to simplify tracking.",
                "correct": False,
                "rationale": (
                    "Incorrect. A single uniform window for all findings ignores risk entirely, leaving actively "
                    "exploited critical vulnerabilities exposed for as long as low-severity, unexploited ones — "
                    "this is not risk-based prioritization."
                ),
            },
            {
                "id": "c",
                "text": "SLA windows should be based solely on how long the finding has existed in the scan report, oldest first, regardless of severity or exploitation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Finding age alone is not a risk indicator; a newly discovered, actively exploited "
                    "critical finding must be prioritized ahead of an old, low-severity, unexploited one."
                ),
            },
            {
                "id": "d",
                "text": "Only findings on internet-facing systems ever get an SLA; internal findings are excluded from remediation tracking entirely.",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal systems can still be critical assets or become exploitable through "
                    "lateral movement after an initial breach; excluding them from tracking entirely ignores "
                    "legitimate internal risk."
                ),
            },
        ],
        "explanation": (
            "Mature vulnerability management programs set the tightest SLA for actively exploited/KEV-listed "
            "findings regardless of raw CVSS score, then tier remaining findings by severity band. This reflects "
            "the principle that exploitability and exposure — not base severity alone — should drive urgency."
        ),
    },
    {
        "id": "tvln-013",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan flags a finding titled 'Default credentials in use' on a newly deployed network-attached "
            "storage (NAS) appliance, with a CVSS-equivalent severity of critical. There is no CVE associated "
            "with this finding, and no vendor patch is referenced. What is the correct remediation approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Log in and change the default administrative credentials to a unique, strong password (or disable the default account and provision a named account), since this is a misconfiguration, not a code-level vulnerability requiring a patch.",
                "correct": True,
                "rationale": (
                    "Correct. Default-credential findings are configuration weaknesses, not vulnerabilities with "
                    "an associated CVE or vendor fix. Remediation is immediate reconfiguration — changing or "
                    "disabling the default account — rather than waiting for a patch that will never be released "
                    "for this class of finding."
                ),
            },
            {
                "id": "b",
                "text": "Wait for the vendor to release a CVE and an official patch before taking action, since the finding has no CVE identifier.",
                "correct": False,
                "rationale": (
                    "Incorrect. Not every finding is a code vulnerability; a misconfiguration like default "
                    "credentials has no associated CVE because it is fixed through configuration change, not "
                    "software patching, and should be corrected immediately."
                ),
            },
            {
                "id": "c",
                "text": "Treat this as a false positive since it has no CVE number and close the ticket without further action.",
                "correct": False,
                "rationale": (
                    "Incorrect. The absence of a CVE does not make this a false positive — default credentials "
                    "on a NAS appliance are a genuine, high-severity misconfiguration that provides an easy path "
                    "to full administrative compromise."
                ),
            },
            {
                "id": "d",
                "text": "Apply a virtual patch via the IPS to block network access to the NAS management interface, since this is functionally equivalent to fixing the underlying issue.",
                "correct": False,
                "rationale": (
                    "Incorrect. Virtual patching is a reasonable interim control while a real fix is pending, "
                    "but here a genuine fix (changing the credentials) is immediately available and takes minutes "
                    "— there is no reason to rely on a compensating control instead of fixing the root cause."
                ),
            },
        ],
        "explanation": (
            "Not every scan finding is a code-level vulnerability requiring a vendor patch. Misconfiguration "
            "findings such as default credentials are remediated directly through configuration changes and "
            "should be fixed immediately, since a real fix is trivially available."
        ),
    },
    {
        "id": "tvln-014",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan of a subscription-based SaaS CRM platform's public API endpoint reports CVE-2025-8801, a "
            "critical authentication-bypass flaw, in software the SaaS vendor owns and operates. The organization "
            "does not control the underlying servers or code. What is the MOST appropriate action for the "
            "organization's vulnerability management team?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open a ticket with the SaaS vendor referencing the CVE, request their remediation timeline, monitor the vendor's status page/security bulletins, and consider temporarily restricting or monitoring the organization's own use of the affected API pending vendor confirmation of a fix.",
                "correct": True,
                "rationale": (
                    "Correct. For vulnerabilities in third-party-owned infrastructure the organization cannot "
                    "directly patch, the correct process is vendor engagement, tracking their remediation timeline, "
                    "and applying whatever compensating controls the organization can control on its own side "
                    "(e.g., its own API usage/monitoring) while the vendor fixes the platform."
                ),
            },
            {
                "id": "b",
                "text": "Attempt to directly patch the SaaS vendor's servers using the organization's own security team.",
                "correct": False,
                "rationale": (
                    "Incorrect. The organization does not own or control the SaaS vendor's infrastructure or "
                    "code; attempting to directly modify systems it does not control is not possible and would "
                    "likely violate the vendor's terms of service."
                ),
            },
            {
                "id": "c",
                "text": "Close the finding immediately since third-party vendor vulnerabilities are outside the organization's responsibility and do not need to be tracked.",
                "correct": False,
                "rationale": (
                    "Incorrect. Third-party risk still affects the organization's data and operations; closing "
                    "the finding without vendor follow-up abandons due diligence and third-party risk management "
                    "responsibilities."
                ),
            },
            {
                "id": "d",
                "text": "Immediately terminate the SaaS contract without first engaging the vendor about their remediation plan.",
                "correct": False,
                "rationale": (
                    "Incorrect. Terminating the relationship is a disproportionate first response; the "
                    "appropriate first step is vendor engagement and monitoring, escalating to contractual "
                    "remedies only if the vendor fails to respond appropriately."
                ),
            },
        ],
        "explanation": (
            "Vulnerabilities in third-party-owned SaaS infrastructure fall under vendor/third-party risk "
            "management: the organization tracks the CVE, engages the vendor for a remediation timeline, applies "
            "any compensating controls within its own control, and monitors vendor communications — it cannot "
            "patch infrastructure it does not own."
        ),
    },
    {
        "id": "tvln-015",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A critical CVE was remediated on a production database cluster over the weekend via an emergency "
            "patch. Select the TWO actions the vulnerability management team should complete before formally "
            "closing the remediation ticket."
        ),
        "options": [
            {
                "id": "a",
                "text": "Run an authenticated rescan of the patched hosts to confirm the specific CVE no longer detects as present.",
                "correct": True,
                "rationale": (
                    "Correct. Verification through rescanning is the standard confirmation step proving the "
                    "vulnerability is actually closed, rather than relying solely on the patch job's reported "
                    "success status."
                ),
            },
            {
                "id": "b",
                "text": "Document the remediation timeline, patch version applied, and verification results for audit and reporting purposes.",
                "correct": True,
                "rationale": (
                    "Correct. Complete documentation of what was patched, when, and how it was verified supports "
                    "audit trails, compliance reporting, and future incident investigation, and is a required part "
                    "of properly closing a remediation ticket."
                ),
            },
            {
                "id": "c",
                "text": "Permanently delete the original scan finding and all related alert history so the dashboard shows a clean record.",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting historical finding data destroys the audit trail needed to prove "
                    "remediation occurred and when; findings should be marked resolved/verified, not erased from "
                    "history."
                ),
            },
            {
                "id": "d",
                "text": "Disable future vulnerability scanning on the patched hosts, since they are now considered permanently secure.",
                "correct": False,
                "rationale": (
                    "Incorrect. No host is permanently secure after a single patch; continuous scanning must "
                    "continue to catch new vulnerabilities, configuration drift, or regressions over time."
                ),
            },
        ],
        "explanation": (
            "Proper closure of a remediation ticket requires verification (rescan/exploit test confirming the "
            "CVE is gone) and documentation (timeline, patch details, evidence) to support audits and future "
            "investigations — not deletion of history or discontinuation of ongoing scanning."
        ),
    },
    {
        "id": "tvln-016",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "During remediation planning, an analyst compares two CVSS v3.1 vector strings for findings on "
            "identically exposed internet-facing hosts:\n\n"
            "CVE-2025-9010: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (base score 9.8)\n"
            "CVE-2025-9044: AV:N/AC:H/PR:H/UI:R/S:U/C:L/I:L/A:N (base score 3.1)\n\n"
            "Which statement correctly interprets why CVE-2025-9010 is scored dramatically higher?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CVE-2025-9010 requires no privileges (PR:N) and no user interaction (UI:N) with low attack complexity (AC:L), while CVE-2025-9044 requires high privileges, user interaction, and high attack complexity — making 2025-9010 far easier for an attacker to exploit remotely.",
                "correct": True,
                "rationale": (
                    "Correct. The exploitability sub-metrics (attack complexity, privileges required, user "
                    "interaction) directly drive score severity. CVE-2025-9010's combination of no privileges "
                    "needed, no user interaction, and low complexity makes it trivially exploitable by any remote "
                    "attacker, unlike CVE-2025-9044, which needs an already-privileged, actively cooperating "
                    "victim under difficult conditions."
                ),
            },
            {
                "id": "b",
                "text": "CVE-2025-9010 is scored higher purely because it was published more recently than CVE-2025-9044.",
                "correct": False,
                "rationale": (
                    "Incorrect. Publication date has no bearing on CVSS base score; the score is derived "
                    "entirely from the exploitability and impact sub-metrics encoded in the vector string."
                ),
            },
            {
                "id": "c",
                "text": "The scope metric (S:U vs S:U) differs between the two, which alone accounts for the score gap.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both vector strings show the same scope value (S:U, unchanged); the score "
                    "difference comes from the differing exploitability metrics (AC, PR, UI) and impact metrics "
                    "(C/I/A), not scope."
                ),
            },
            {
                "id": "d",
                "text": "CVE-2025-9044 must be a local-only vulnerability since it scores lower, while CVE-2025-9010 is remote.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both vector strings show Attack Vector = Network (AV:N); CVE-2025-9044 is still "
                    "remotely reachable, it is simply far harder to exploit due to high complexity, required "
                    "privileges, and required user interaction — not because it is local."
                ),
            },
        ],
        "explanation": (
            "CVSS base score severity is driven by how easily and impactfully a flaw can be exploited: low "
            "attack complexity, no privileges required, and no user interaction dramatically increase "
            "exploitability and therefore score, independent of publication timing or superficial similarities "
            "like matching scope values."
        ),
    },
    {
        "id": "tvln-017",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A penetration test report notes that a critical CVE flagged by the last vulnerability scan (CVSS "
            "9.4, remote code execution in a legacy SOAP service) could not actually be exploited during testing "
            "because the SOAP endpoint requires a client certificate that is issued only to two hardened "
            "internal management workstations, and the service is unreachable from any other network segment. "
            "What should the vulnerability management team do with this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Keep the finding open at its true CVSS base severity for tracking purposes, but document the mutual-TLS restriction and network isolation as a compensating control that substantially lowers real-world (environmental) risk, and deprioritize it relative to exploitable internet-facing findings.",
                "correct": True,
                "rationale": (
                    "Correct. The vulnerability genuinely exists (it is not a false positive), so it should "
                    "remain tracked, but the documented compensating controls (mTLS restricted to two hardened "
                    "hosts, network isolation) meaningfully reduce real exploitability and justify a lower "
                    "remediation priority relative to genuinely exploitable, more exposed findings."
                ),
            },
            {
                "id": "b",
                "text": "Close the finding entirely as a false positive, since the penetration test could not exploit it.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a false positive — the vulnerable code is genuinely present. Failing "
                    "to exploit it in one test with current compensating controls does not mean the underlying "
                    "flaw doesn't exist or could never be exploited if those controls changed or were bypassed."
                ),
            },
            {
                "id": "c",
                "text": "Treat it as the top remediation priority across the entire organization, since its base CVSS score of 9.4 is the highest in the environment.",
                "correct": False,
                "rationale": (
                    "Incorrect. Base score alone ignores the substantial compensating controls already "
                    "documented (certificate-restricted access, network isolation) that meaningfully reduce real "
                    "exploitability compared to unmitigated, exploitable findings elsewhere."
                ),
            },
            {
                "id": "d",
                "text": "Remove the finding from the asset's vulnerability history entirely once the penetration test is complete.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing tracking history destroys the audit trail; the finding should remain "
                    "documented and tracked with its compensating control noted, not erased."
                ),
            },
        ],
        "explanation": (
            "A vulnerability that genuinely exists but is substantially mitigated by compensating controls "
            "should stay tracked at its true severity with the mitigating context documented, and be "
            "deprioritized relative to findings that are actually exploitable given current exposure — it is "
            "neither a false positive to dismiss nor an unconditional top priority based on base score alone."
        ),
    },
    {
        "id": "tvln-018",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan shows CVE-2025-9910 present on 340 workstations. Threat intelligence confirms the CVE was "
            "added to the CISA Known Exploited Vulnerabilities (KEV) catalog this morning, and it is now being "
            "used in an active, widespread ransomware campaign targeting organizations that have not yet patched. "
            "A vendor patch has been available for six weeks. What is the MOST important immediate implication of "
            "the CISA KEV listing for this organization's remediation plan?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The finding should be escalated to the shortest available emergency remediation window and treated as the top priority across the fleet, since KEV listing confirms real-world, active exploitation is already occurring — not merely theoretical risk.",
                "correct": True,
                "rationale": (
                    "Correct. CISA KEV listing specifically means the vulnerability has confirmed evidence of "
                    "active exploitation in the wild, which is the strongest possible signal that immediate, "
                    "emergency-priority remediation is warranted, especially with 340 vulnerable endpoints and an "
                    "active ransomware campaign already targeting it."
                ),
            },
            {
                "id": "b",
                "text": "The KEV listing is informational only and does not change the remediation timeline already set based on the original CVSS score six weeks ago.",
                "correct": False,
                "rationale": (
                    "Incorrect. KEV listing is a material change in threat intelligence — moving from 'patch "
                    "available' to 'confirmed active exploitation' — and should trigger re-prioritization to the "
                    "most urgent tier, not be treated as unchanged business as usual."
                ),
            },
            {
                "id": "c",
                "text": "Since a patch has been available for six weeks already, the organization is not at meaningfully greater risk today than it was yesterday.",
                "correct": False,
                "rationale": (
                    "Incorrect. Patch availability does not equal patch deployment; with 340 still-vulnerable "
                    "workstations and an active ransomware campaign confirmed today, the organization's real-time "
                    "risk has materially increased, warranting emergency action."
                ),
            },
            {
                "id": "d",
                "text": "KEV listings only apply to U.S. federal agencies under binding operational directives, so private-sector organizations can disregard them for prioritization purposes.",
                "correct": False,
                "rationale": (
                    "Incorrect. While CISA's KEV-driven binding operational directives legally apply to federal "
                    "agencies, the KEV catalog is widely used across the private sector as a best-practice signal "
                    "of confirmed active exploitation and should directly inform any organization's prioritization."
                ),
            },
        ],
        "explanation": (
            "Addition to the CISA KEV catalog confirms real-world active exploitation, which is a stronger "
            "urgency signal than CVSS base score alone. Combined with active ransomware targeting and a large "
            "vulnerable population, this should trigger emergency-tier, fleet-wide remediation regardless of how "
            "long a patch has already been available."
        ),
    },
    {
        "id": "tvln-019",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scanner reports CVE-2025-1050 (critical, remote code execution) on host analytics-dev-22. "
            "Investigation reveals this host was decommissioned eight months ago, is powered off in the "
            "virtualization platform, and no longer has an active network interface, but the CMDB and scan "
            "target list were never updated to remove it. What is the correct next step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remove the decommissioned host from the CMDB and the scanner's target inventory, and add a process check to ensure decommissioning workflows automatically deregister assets from scanning and asset records.",
                "correct": True,
                "rationale": (
                    "Correct. This is a stale asset record, not an active vulnerability requiring remediation; "
                    "the correct fix is proper asset lifecycle management — removing the decommissioned host from "
                    "tracking and closing the gap in the decommissioning process that let it persist."
                ),
            },
            {
                "id": "b",
                "text": "Power the host back on so it can be patched and then verified as remediated before being powered off again.",
                "correct": False,
                "rationale": (
                    "Incorrect. Powering on a decommissioned system solely to patch a host that is no longer in "
                    "use wastes effort and unnecessarily reintroduces it to the network; the asset should simply "
                    "be removed from tracking since it is no longer in service."
                ),
            },
            {
                "id": "c",
                "text": "Treat this as the highest-priority critical finding in the environment because of its 'critical' severity label, and escalate to emergency patching.",
                "correct": False,
                "rationale": (
                    "Incorrect. A powered-off, decommissioned host with no active network interface poses no "
                    "real exploitable risk; treating a stale inventory record as an emergency misdirects "
                    "remediation resources away from genuinely active, exploitable findings."
                ),
            },
            {
                "id": "d",
                "text": "Leave the finding open indefinitely in the dashboard since the host still technically exists in the virtualization platform.",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving a stale finding open indefinitely pollutes reporting metrics and "
                    "obscures the true state of the environment; the CMDB and scan inventory should be corrected, "
                    "not left inaccurate."
                ),
            },
        ],
        "explanation": (
            "Not every scan finding represents active risk. Stale inventory records for decommissioned, "
            "powered-off assets should be corrected through proper asset lifecycle management, closing the gap "
            "in decommissioning process rather than treating the CMDB error as an urgent vulnerability."
        ),
    },
    {
        "id": "tvln-020",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "The CISO asks the vulnerability management team to weight remediation priority not just by CVSS "
            "score and exploit status, but by asset criticality. Two internet-facing findings have identical "
            "CVSS base scores (7.8) and identical exploit status (proof-of-concept only, not seen in the wild): "
            "one is on a marketing landing-page server with only public content, and the other is on the "
            "e-commerce payment processing gateway that handles cardholder data. Which finding should be "
            "prioritized higher, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The payment processing gateway, because asset criticality (handling regulated cardholder data critical to business operations) should weight prioritization even when CVSS score and exploit status are otherwise identical.",
                "correct": True,
                "rationale": (
                    "Correct. Effective risk-based prioritization considers business/data impact, not just "
                    "technical severity. When two findings are technically identical, the one affecting a "
                    "crown-jewel asset handling regulated cardholder data represents materially higher real-world "
                    "risk and should be remediated first."
                ),
            },
            {
                "id": "b",
                "text": "The marketing landing page, because it is customer-facing and reputational damage from any compromise is always the top concern.",
                "correct": False,
                "rationale": (
                    "Incorrect. While reputational impact matters, a compromise of the payment gateway handling "
                    "cardholder data carries materially greater regulatory, financial, and business impact than a "
                    "public marketing page with no sensitive data."
                ),
            },
            {
                "id": "c",
                "text": "Neither should be prioritized over the other, since identical CVSS scores and exploit status mean identical risk regardless of the asset involved.",
                "correct": False,
                "rationale": (
                    "Incorrect. Treating CVSS and exploit status as the sole risk factors ignores asset "
                    "criticality and data sensitivity entirely, which is exactly the additional context the CISO "
                    "asked the team to weigh."
                ),
            },
            {
                "id": "d",
                "text": "They should be remediated in alphabetical order by hostname, since that is the simplest tie-breaker.",
                "correct": False,
                "rationale": (
                    "Incorrect. Hostname alphabetization carries no risk information and ignores the explicit "
                    "criticality/data-sensitivity distinction between the two assets that should drive the "
                    "prioritization decision."
                ),
            },
        ],
        "explanation": (
            "Mature risk-based vulnerability management incorporates asset criticality and data classification "
            "alongside CVSS score and exploit status. When technical severity is a tie, the finding on the more "
            "business-critical, regulated-data-handling asset should be remediated first."
        ),
    },
    {
        "id": "tvln-021",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A newly deployed vulnerability scanner is configured to run credentialed scans against Windows "
            "servers using a domain service account. On the first scan cycle, half the servers return "
            "'authentication failed' and are scanned only via unauthenticated network checks, producing "
            "significantly fewer findings for those hosts than for the successfully authenticated half. What "
            "should the analyst conclude and do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The lower finding counts on the failed-authentication hosts likely reflect reduced scan visibility, not fewer actual vulnerabilities; the service account's permissions/connectivity to those hosts should be fixed and the scan rerun before drawing any conclusions about their true risk posture.",
                "correct": True,
                "rationale": (
                    "Correct. A drop in findings correlated with authentication failure is a visibility problem, "
                    "not evidence of a cleaner host. The scanning service account issue must be resolved and the "
                    "credentialed scan rerun to get an accurate, comparable picture of those servers' true "
                    "vulnerability posture."
                ),
            },
            {
                "id": "b",
                "text": "The servers with fewer findings are genuinely more secure than the others and require no further scanning investigation.",
                "correct": False,
                "rationale": (
                    "Incorrect. This mistakes reduced scan depth (due to failed authentication) for genuinely "
                    "better security; without credentialed access, those hosts' internal patch levels are largely "
                    "unknown, not confirmed clean."
                ),
            },
            {
                "id": "c",
                "text": "Accept the results as final and report the environment as having an uneven but accurate risk distribution across the two halves of the fleet.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reporting mismatched-depth scan results as an accurate risk comparison would "
                    "mislead stakeholders, since the apparent difference is a scanning artifact, not a real "
                    "security difference."
                ),
            },
            {
                "id": "d",
                "text": "Switch all future scans to uncredentialed-only mode across the entire fleet for consistency.",
                "correct": False,
                "rationered": False,
                "rationale": (
                    "Incorrect. Standardizing on the less-thorough method to achieve superficial consistency "
                    "sacrifices the deeper visibility credentialed scanning provides on the servers that already "
                    "authenticate successfully — the actual fix is repairing authentication on the failing half."
                ),
            },
        ],
        "explanation": (
            "Credentialed scanning failures produce artificially low finding counts because the scanner cannot "
            "inspect installed software versions on those hosts. The correct response is to troubleshoot and fix "
            "the authentication issue and rerun the scan, not to interpret the gap as genuinely better security "
            "or to downgrade scanning depth fleet-wide."
        ),
    },
    {
        "id": "tvln-022",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan finding for CVE-2025-2277 (CVSS 8.4, internet-facing) has remained open for 45 days, past "
            "the organization's 30-day SLA for high-severity findings, because the application owner says patch "
            "testing keeps surfacing regressions in a critical business workflow. The security team needs an "
            "interim answer that satisfies both audit requirements and real risk reduction while testing "
            "continues. What is the BEST course of action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Grant a documented, time-bound exception with an approved compensating control (e.g., a virtual patch/WAF rule blocking the specific exploit pattern, or added monitoring) while patch testing continues, with a defined re-review date.",
                "correct": True,
                "rationale": (
                    "Correct. When remediation is legitimately delayed by a real operational constraint, the "
                    "correct governance response is a formal, time-bound exception paired with a compensating "
                    "control that reduces real exposure in the interim — satisfying both audit and risk-reduction "
                    "needs — rather than silently missing the SLA or ignoring the constraint."
                ),
            },
            {
                "id": "b",
                "text": "Force the patch into production immediately despite known regressions, since the SLA has already been missed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Forcing a patch known to cause regressions in a critical business workflow could "
                    "cause an availability incident; SLA pressure does not override the need for responsible "
                    "change management and testing."
                ),
            },
            {
                "id": "c",
                "text": "Leave the finding open past the SLA with no additional documentation or compensating control, since testing is still in progress.",
                "correct": False,
                "rationale": (
                    "Incorrect. An undocumented, ungoverned SLA breach with no interim risk reduction leaves the "
                    "organization both audit-exposed and materially at risk from the unpatched, internet-facing "
                    "finding in the meantime."
                ),
            },
            {
                "id": "d",
                "text": "Permanently exempt this class of finding from future SLA tracking to avoid repeated SLA breach reporting.",
                "correct": False,
                "rationale": (
                    "Incorrect. A permanent exemption is disproportionate to a temporary testing delay; this "
                    "situation calls for a time-bound exception with re-review, not a permanent waiver from "
                    "tracking."
                ),
            },
        ],
        "explanation": (
            "When a legitimate operational constraint delays remediation past SLA, the correct response is a "
            "documented, time-bound exception paired with a compensating control (such as a virtual patch or "
            "enhanced monitoring) — reducing real risk while testing continues, and preserving an accurate audit "
            "trail rather than silently missing deadlines or forcing an unsafe change."
        ),
    },
    {
        "id": "tvln-023",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan report shows the following for a single internal application server:\n\n"
            "CVE               CVSS Base   Category\n"
            "CVE-2025-3301      9.6         Critical\n"
            "CVE-2025-3315      8.8         High\n"
            "CVE-2025-3322      8.1         High\n"
            "CVE-2025-3340      6.9         Medium\n\n"
            "The team can only patch one CVE this maintenance window due to a required service restart and "
            "change-freeze constraints. Threat intelligence shows no known exploitation for any of the four, and "
            "exposure/network reachability is identical for all four (same host, same segment). Under these "
            "conditions, which factor should MOST appropriately break the tie?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Patch CVE-2025-3301 first, since with exploitability and exposure equal across all four findings, the raw CVSS base severity (critical, 9.6) is the correct remaining differentiator for potential impact.",
                "correct": True,
                "rationale": (
                    "Correct. When exploit status and exposure are genuinely identical across findings, CVSS "
                    "base score becomes a valid tie-breaker because it reflects the worst-case severity/impact if "
                    "the flaw were exploited — the highest-scoring finding should be remediated first under these "
                    "equal conditions."
                ),
            },
            {
                "id": "b",
                "text": "Patch CVE-2025-3340 first, since medium findings are typically overlooked and deserve priority for that reason alone.",
                "correct": False,
                "rationale": (
                    "Incorrect. Being 'often overlooked' is not a legitimate risk-based prioritization factor; "
                    "with all other conditions equal, the objectively lower-severity finding should not be "
                    "patched ahead of a critical one."
                ),
            },
            {
                "id": "c",
                "text": "Patch whichever CVE was published earliest, since older vulnerabilities are inherently riskier.",
                "correct": False,
                "rationale": (
                    "Incorrect. Publication date alone does not indicate risk; an older CVE is not inherently "
                    "more dangerous than a newer one when exploitability and exposure are identical — severity "
                    "should drive the decision instead."
                ),
            },
            {
                "id": "d",
                "text": "Patch whichever CVE has the shortest CVE identifier number, since it is likely simpler to remediate.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVE identifier length has no relationship to remediation complexity or risk; "
                    "this is not a legitimate prioritization criterion in any circumstance."
                ),
            },
        ],
        "explanation": (
            "CVSS base score should not be the sole prioritization driver when exploitability and exposure "
            "differ across findings — but when those factors are genuinely equal, base severity legitimately "
            "becomes the correct tie-breaker, since it reflects worst-case impact if the vulnerability is "
            "exploited."
        ),
    },
    {
        "id": "tvln-024",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "An analyst reviewing a scan notices CVE-2025-4450 flagged as 'critical, unauthenticated remote code "
            "execution' on an internal HR application server. Manual testing by the app team shows the specific "
            "vulnerable function is guarded by an authentication check that the scanner's plugin failed to "
            "detect due to a non-standard login redirect flow, meaning exploitation actually requires valid "
            "credentials. What is the correct next step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Document the verified testing results showing authentication is actually required, adjust the finding's recorded severity/priority to reflect the true (authenticated, not unauthenticated) exploitation path, and report the scanner plugin issue to the vendor or tune the scan policy.",
                "correct": True,
                "rationale": (
                    "Correct. This is a partial false positive: the underlying flaw is real, but the scanner "
                    "mischaracterized its exploitability due to a detection limitation. The correct response is "
                    "to document verified findings, adjust severity/priority to reflect true risk, and address the "
                    "scanner tuning/plugin gap so future scans are more accurate."
                ),
            },
            {
                "id": "b",
                "text": "Close the finding entirely as a complete false positive, since exploitation requires authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. The underlying vulnerability itself is real and still exploitable by any "
                    "authenticated user (which could include a compromised low-privilege account); fully closing "
                    "the finding would ignore a genuine, still-relevant risk."
                ),
            },
            {
                "id": "c",
                "text": "Leave the finding's severity unchanged as 'critical, unauthenticated' in the dashboard, since scanner output should never be second-guessed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Verified manual testing showing the scanner mischaracterized the exploitation "
                    "path is exactly the kind of evidence that should update recorded severity; blindly trusting "
                    "unverified scanner output over confirmed testing produces inaccurate risk reporting."
                ),
            },
            {
                "id": "d",
                "text": "Escalate immediately to the incident response team, since a critical unauthenticated RCE finding always triggers incident response regardless of verification results.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is routine vulnerability triage and verification, not an active security "
                    "incident; escalating to IR is unwarranted once testing shows the actual exploitation path "
                    "requires authentication and no compromise has occurred."
                ),
            },
        ],
        "explanation": (
            "Verification can reveal a scanner mischaracterized (rather than fabricated) a finding — the "
            "underlying flaw is real but the risk profile differs from what was reported. The correct handling "
            "is to document evidence, adjust severity/priority to reflect verified reality, and address the "
            "detection gap, rather than fully dismissing or blindly trusting the original scan output."
        ),
    },
    {
        "id": "tvln-025",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability management program lead wants to reduce analyst time wasted chasing findings that "
            "turn out to be non-issues on this environment's specific configuration. Over the last quarter, the "
            "same plugin has generated 40 findings that were all manually verified and closed as false positives "
            "for the same underlying reason. What is the MOST effective long-term solution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Work with the scanner vendor or scan policy configuration to tune or adjust the specific plugin/check so it correctly accounts for the environment-specific condition causing the repeated false positives, rather than manually re-verifying each new instance.",
                "correct": True,
                "rationale": (
                    "Correct. Repeated false positives from the same root cause indicate a detection logic gap. "
                    "Tuning the scan policy or plugin configuration (or working with the vendor to fix the check) "
                    "eliminates the recurring noise at the source, which is far more efficient than manually "
                    "re-verifying each new occurrence indefinitely."
                ),
            },
            {
                "id": "b",
                "text": "Instruct analysts to stop investigating findings from that plugin entirely going forward, since it has proven unreliable.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling investigation of an entire plugin risks missing genuine true positives "
                    "it might also detect; the correct fix is tuning the specific check, not abandoning "
                    "verification of that detection category altogether."
                ),
            },
            {
                "id": "c",
                "text": "Continue manually verifying and closing each new instance individually, since documentation alone is sufficient without addressing the recurring cause.",
                "correct": False,
                "rationale": (
                    "Incorrect. Continuing to manually re-verify the same known false-positive condition every "
                    "time is precisely the wasted analyst time the program lead wants to eliminate; tuning "
                    "addresses the root cause instead of repeating the same manual work indefinitely."
                ),
            },
            {
                "id": "d",
                "text": "Increase the scan frequency for that specific plugin so the false positive is reported more often for better tracking.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning more frequently would only generate the same known false positive more "
                    "often, increasing analyst workload rather than reducing it."
                ),
            },
        ],
        "explanation": (
            "When a specific check repeatedly produces the same verified false positive due to an "
            "environment-specific condition, the efficient long-term fix is tuning the scan policy/plugin "
            "configuration to account for that condition — closing the detection gap at its source rather than "
            "repeatedly performing the same manual verification."
        ),
    },
    {
        "id": "tvln-026",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A critical CVE affecting a custom-built internal application cannot be patched because the "
            "development team that owns the code was disbanded and no one currently maintains it, and there is "
            "no vendor to contact. The application is scheduled for full replacement in nine months. Which "
            "approach BEST balances risk reduction against the reality that remediation is not currently "
            "feasible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy a virtual patch (WAF/IPS rule blocking the specific exploit pattern) and restrict network access to only the minimum required users/systems, formally documented as a time-bound exception tied to the replacement timeline with periodic risk re-review.",
                "correct": True,
                "rationale": (
                    "Correct. When source-level remediation is genuinely infeasible, the correct approach "
                    "combines virtual patching and access restriction as compensating controls, formalized as a "
                    "documented, time-bound exception aligned to the known replacement date, with ongoing periodic "
                    "review rather than an indefinite, undocumented gap."
                ),
            },
            {
                "id": "b",
                "text": "Take no action until the replacement project completes in nine months, since remediation is not currently feasible.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Not currently feasible to patch the code' does not mean nothing can be done; "
                    "compensating controls (virtual patching, access restriction) can meaningfully reduce risk "
                    "during the nine-month gap and should not be skipped."
                ),
            },
            {
                "id": "c",
                "text": "Decommission the application immediately rather than waiting for the planned replacement.",
                "correct": False,
                "rationale": (
                    "Incorrect. Immediate decommissioning without warning could disrupt whatever business "
                    "function the application still serves; a planned nine-month replacement suggests a "
                    "controlled transition is already underway, and interim compensating controls are the "
                    "appropriate bridge, not an unplanned abrupt shutdown."
                ),
            },
            {
                "id": "d",
                "text": "Reassign the finding's severity to 'low' in the dashboard since there is currently no team available to fix it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Team availability to remediate has no bearing on the vulnerability's actual "
                    "severity; misrepresenting severity to match staffing reality hides true risk from "
                    "stakeholders and decision-makers."
                ),
            },
        ],
        "explanation": (
            "When a vulnerability cannot be remediated at the source due to a genuine organizational constraint, "
            "compensating controls (virtual patching, access restriction) paired with a formally documented, "
            "time-bound exception tied to a real remediation plan (the replacement timeline) is the correct "
            "balance of risk reduction and operational reality."
        ),
    },
    {
        "id": "tvln-027",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A monthly external scan and a monthly internal credentialed scan of the same server both report "
            "CVE-2025-5501 as present, but the two scans assign different severities: the external scan rates it "
            "'high' (7.4) because the vulnerable service is reachable on the public interface, while the internal "
            "scan rates the same CVE 'critical' (9.1) reflecting the vendor's published base score for the flaw "
            "itself. Which severity should the vulnerability management team use to drive remediation priority?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use the vendor's published base CVSS score (9.1) to understand worst-case impact, but weight the actual remediation priority using the real exposure context (public reachability) confirmed by the external scan — treating this as a high-priority, externally reachable critical flaw.",
                "correct": True,
                "rationale": (
                    "Correct. The base score reflects the vulnerability's intrinsic worst-case severity, while "
                    "the external scan's exposure context confirms it is reachable by any internet-based "
                    "attacker. Combining both — a critical flaw that is also externally exposed — should drive "
                    "urgent prioritization rather than picking one number in isolation."
                ),
            },
            {
                "id": "b",
                "text": "Use only the internal scan's score and ignore the external scan's exposure context entirely, since internal scans are always more authoritative.",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal credentialed scans are more thorough for detecting the presence of a "
                    "vulnerability, but exposure context from the external scan (public reachability) is "
                    "essential real-world risk information that should not be discarded."
                ),
            },
            {
                "id": "c",
                "text": "Use only the external scan's lower severity number and disregard the vendor's base CVSS score entirely.",
                "correct": False,
                "rationale": (
                    "Incorrect. Discarding the vendor's base severity ignores the vulnerability's true worst-case "
                    "impact; both context (exposure) and intrinsic severity (base score) should inform the "
                    "combined prioritization decision."
                ),
            },
            {
                "id": "d",
                "text": "Average the two severities mathematically (7.4 and 9.1) to produce a single blended score for prioritization.",
                "correct": False,
                "rationale": (
                    "Incorrect. Mechanically averaging two scores that measure different things (intrinsic "
                    "severity vs. exposure-adjusted context) produces a meaningless number; the correct approach "
                    "is to consider both factors together qualitatively, not blend them arithmetically."
                ),
            },
        ],
        "explanation": (
            "Different scan perspectives (internal vs. external) surface complementary information: base "
            "severity reflects intrinsic worst-case impact, while exposure context from external scanning shows "
            "real-world reachability. A critical vulnerability confirmed to be externally reachable should be "
            "treated as urgent, combining both signals rather than relying on either number alone or averaging "
            "them mathematically."
        ),
    },
    {
        "id": "tvln-028",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan flags CVE-2025-6610 (CVSS 7.9) on a legacy internal file-sharing protocol still enabled on "
            "several file servers. There is a vendor patch available, but applying it requires disabling the "
            "insecure protocol entirely, which will break access for a small number of unsupported client "
            "devices still in use by one department. Which approach represents the BEST balance between security "
            "and business continuity while a longer-term device upgrade is planned?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable the insecure protocol on all file servers except a tightly scoped, segmented subnet serving only the unsupported department's legacy devices, and set a firm deadline tied to the device upgrade project to fully disable it everywhere.",
                "correct": True,
                "rationale": (
                    "Correct. This minimizes the attack surface immediately across most of the environment while "
                    "using segmentation as a compensating control for the narrow legitimate business exception, "
                    "paired with a firm deadline — balancing security and continuity rather than an all-or-nothing "
                    "choice."
                ),
            },
            {
                "id": "b",
                "text": "Leave the insecure protocol enabled fleet-wide indefinitely to avoid disrupting the one department's legacy devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving the vulnerable protocol enabled across the entire environment to "
                    "accommodate a small subset of devices unnecessarily preserves the vulnerability everywhere "
                    "else where no such constraint exists."
                ),
            },
            {
                "id": "c",
                "text": "Apply the patch and disable the protocol fleet-wide immediately without any transition plan for the affected department's devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores legitimate business continuity impact and risks an unplanned outage "
                    "for the affected department's operations; a scoped, temporary compensating measure with a "
                    "deadline better balances both concerns."
                ),
            },
            {
                "id": "d",
                "text": "Downgrade the finding's severity in the dashboard to reflect the business constraint instead of applying the patch or any compensating control.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting reported severity to match a business constraint misrepresents actual "
                    "risk and does not reduce the exposure of the insecure protocol anywhere in the environment."
                ),
            },
        ],
        "explanation": (
            "When remediation would break a legitimate, narrow business need, the correct approach is scoped "
            "segmentation as a compensating control limited to only the affected legacy devices, paired with "
            "remediating everywhere else immediately and a firm deadline for closing the remaining gap — not an "
            "all-or-nothing choice or a cosmetic severity change."
        ),
    },
    {
        "id": "tvln-029",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A retail organization's scan shows CVE-2025-7701, a critical vulnerability, on a point-of-sale "
            "terminal that processes cardholder data and is in scope for PCI DSS. The internal remediation SLA "
            "for critical findings is 30 days, but PCI DSS requires critical vulnerabilities affecting the "
            "cardholder data environment to be remediated within a shorter window defined by the standard. Which "
            "timeline should govern this specific finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The stricter PCI DSS requirement, since regulatory/compliance mandates for in-scope cardholder data environment assets take precedence over the organization's general internal SLA when the two conflict.",
                "correct": True,
                "rationale": (
                    "Correct. When a compliance framework's requirement for in-scope systems is more stringent "
                    "than an organization's internal policy, the compliance requirement governs for that asset — "
                    "internal SLAs represent a baseline, not a ceiling, for regulated environments."
                ),
            },
            {
                "id": "b",
                "text": "The internal 30-day SLA, because internal policy always takes precedence over external compliance frameworks.",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal policy cannot override a binding compliance obligation for in-scope "
                    "systems; where PCI DSS mandates a stricter timeline for the cardholder data environment, "
                    "that stricter requirement governs."
                ),
            },
            {
                "id": "c",
                "text": "Whichever timeline the terminal's vendor recommends in its own documentation, regardless of internal SLA or PCI DSS requirements.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vendor recommendations are not a substitute for binding regulatory requirements; "
                    "PCI DSS timelines for the cardholder data environment apply regardless of what the vendor's "
                    "own documentation suggests."
                ),
            },
            {
                "id": "d",
                "text": "There is no need to follow either timeline as long as the finding is eventually remediated before the next audit cycle.",
                "correct": False,
                "rationale": (
                    "Incorrect. PCI DSS specifies remediation timelines by severity that must be met on an "
                    "ongoing basis, not merely 'before the next audit'; treating the audit cycle as the only "
                    "deadline misunderstands the continuous compliance obligation."
                ),
            },
        ],
        "explanation": (
            "For assets in scope for a regulatory or contractual framework like PCI DSS, the framework's "
            "remediation timeline requirements govern when they are stricter than internal policy — internal "
            "SLAs set a general baseline but cannot relax a binding compliance obligation for in-scope systems."
        ),
    },
    {
        "id": "tvln-030",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability management maturity assessment finds that the organization currently only scans and "
            "remediates based on point-in-time snapshots each quarter, with no visibility into vulnerabilities "
            "introduced between scan cycles. Which enhancement would MOST directly close this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy continuous/agent-based vulnerability monitoring that reports new findings as they appear, supplementing the periodic full scans rather than relying solely on quarterly point-in-time snapshots.",
                "correct": True,
                "rationale": (
                    "Correct. Continuous monitoring (via agents or frequent lightweight scanning) closes the "
                    "visibility gap between periodic full scans by surfacing newly introduced vulnerabilities "
                    "(e.g., from new software installs or configuration changes) as they occur, rather than "
                    "waiting up to a quarter to detect them."
                ),
            },
            {
                "id": "b",
                "text": "Reduce the scan scope to only internet-facing assets so each quarterly scan completes faster.",
                "correct": False,
                "rationale": (
                    "Incorrect. Narrowing scope reduces coverage rather than closing the time-gap problem; it "
                    "would leave internal assets even less visible between cycles and does not address the "
                    "underlying point-in-time limitation."
                ),
            },
            {
                "id": "c",
                "text": "Switch entirely to uncredentialed scanning to speed up each quarterly cycle.",
                "correct": False,
                "rationale": (
                    "Incorrect. Uncredentialed scanning reduces detection depth and would not address the "
                    "fundamental issue of only scanning once per quarter; it trades accuracy for speed without "
                    "closing the visibility gap between cycles."
                ),
            },
            {
                "id": "d",
                "text": "Increase the CVSS severity threshold required before a finding is reported, so fewer findings need review each quarter.",
                "correct": False,
                "rationale": (
                    "Incorrect. Raising the reporting threshold hides lower-severity findings rather than "
                    "improving detection timeliness, and does nothing to close the gap between quarterly scan "
                    "cycles."
                ),
            },
        ],
        "explanation": (
            "Point-in-time quarterly scanning creates blind windows where newly introduced vulnerabilities go "
            "undetected for weeks or months. Continuous or agent-based monitoring between full scan cycles is "
            "the direct fix, providing ongoing visibility rather than narrowing scope, reducing scan depth, or "
            "hiding lower-severity findings."
        ),
    },
    # ---------------------------------------------------------------
    # Mitigation techniques (6) — domain 4, objective 4.1
    # ---------------------------------------------------------------
    {
        "id": "tvln-031",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan finds a critical vulnerability in an internet-facing legacy content management system (CMS) "
            "for which the vendor has stopped issuing patches. Replacing the CMS is planned but will take four "
            "months. Which combination of interim mitigation techniques BEST reduces exploitation risk while "
            "minimizing disruption to the still-needed public website?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy a WAF rule set (virtual patch) tuned to block the specific exploit pattern for this CVE, and place the CMS behind a reverse proxy that restricts administrative endpoints to an allow-listed set of internal IP addresses.",
                "correct": True,
                "rationale": (
                    "Correct. Virtual patching via a WAF blocks the specific known exploit pattern without "
                    "requiring code changes to the unsupported CMS, and restricting administrative endpoint "
                    "access via allow-listing shrinks the attack surface — both preserve public site availability "
                    "while meaningfully reducing exploitation risk during the replacement project."
                ),
            },
            {
                "id": "b",
                "text": "Take the CMS offline entirely until the replacement project completes in four months.",
                "correct": False,
                "rationale": (
                    "Incorrect. Taking the still-needed public website offline for four months is a "
                    "disproportionate response that ignores available compensating controls that could reduce "
                    "risk while preserving the business function."
                ),
            },
            {
                "id": "c",
                "text": "Disable all logging on the CMS to reduce the chance that an attacker discovers the vulnerability through log-based reconnaissance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling logging removes the security team's ability to detect exploitation "
                    "attempts and does nothing to prevent the vulnerability from being exploited; it makes the "
                    "situation worse, not better."
                ),
            },
            {
                "id": "d",
                "text": "Increase the CMS's session timeout duration so legitimate administrators are logged out less frequently.",
                "correct": False,
                "rationale": (
                    "Incorrect. Extending session timeouts is unrelated to the vulnerability itself and would "
                    "not reduce exploitation risk; if anything, longer-lived sessions slightly increase exposure "
                    "if a session is hijacked."
                ),
            },
        ],
        "explanation": (
            "When a patch is unavailable, virtual patching (WAF/IPS rules targeting the specific exploit "
            "pattern) combined with access restriction (allow-listing sensitive endpoints) are standard "
            "compensating controls that reduce real exploitation risk while preserving required business "
            "functionality during a planned replacement."
        ),
    },
    {
        "id": "tvln-032",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "EDR telemetry confirms a workstation is actively being exploited via a known CVE for which a patch "
            "exists but has not yet been deployed organization-wide. The exploitation attempt was blocked by the "
            "EDR agent's behavioral detection, but the underlying vulnerability remains unpatched on this and "
            "other workstations. What is the MOST appropriate immediate mitigation for the affected workstation, "
            "distinct from the broader patch rollout already in progress?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Isolate the affected workstation from the network using the EDR's containment/isolation capability while the incident is investigated, independent of the fleet-wide patch rollout timeline.",
                "correct": True,
                "rationale": (
                    "Correct. A workstation with a confirmed active exploitation attempt needs immediate "
                    "isolation to prevent any further attacker activity or lateral movement, regardless of when "
                    "the broader patch rollout completes — this is a targeted, immediate mitigation for the "
                    "specific affected host."
                ),
            },
            {
                "id": "b",
                "text": "Wait for the scheduled fleet-wide patch rollout to reach this workstation in its normal sequence, since the exploitation attempt was already blocked.",
                "correct": False,
                "rationale": (
                    "Incorrect. A blocked exploitation attempt still indicates active attacker interest in this "
                    "specific host; waiting for a routine, unprioritized patch cycle ignores the immediate need "
                    "for containment and investigation of a host that was directly targeted."
                ),
            },
            {
                "id": "c",
                "text": "Uninstall the EDR agent from the workstation since it successfully did its job and is no longer needed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing the EDR agent would eliminate ongoing visibility and protection on a "
                    "workstation that has already been targeted once and remains unpatched — this increases risk "
                    "rather than reducing it."
                ),
            },
            {
                "id": "d",
                "text": "Reset the workstation's local firewall rules to their factory defaults to simplify troubleshooting.",
                "correct": False,
                "rationale": (
                    "Incorrect. Resetting firewall rules to factory defaults is unrelated to containing an active "
                    "exploitation attempt and could actually weaken the host's defenses during an active "
                    "investigation."
                ),
            },
        ],
        "explanation": (
            "A confirmed, targeted exploitation attempt against a specific host calls for immediate, targeted "
            "containment (network isolation) independent of the broader remediation timeline — the affected host "
            "should not simply wait in the normal patch rollout queue once it has already been directly "
            "targeted."
        ),
    },
    {
        "id": "tvln-033",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A critical CVE affects a vendor-supported industrial control system (ICS) human-machine interface "
            "(HMI). The vendor confirms a patch will not be available for at least six months due to a lengthy "
            "certification process required for this hardware. Select the TWO compensating controls that would "
            "MOST appropriately reduce risk in the interim without disrupting plant operations."
        ),
        "options": [
            {
                "id": "a",
                "text": "Segment the HMI onto an isolated OT VLAN with strict ACLs permitting only the specific engineering and monitoring systems it must communicate with.",
                "correct": True,
                "rationale": (
                    "Correct. Network segmentation limiting reachability to only essential systems directly "
                    "reduces the attack surface of an unpatchable device without requiring any change to the "
                    "HMI itself, preserving normal plant operation."
                ),
            },
            {
                "id": "b",
                "text": "Deploy an industrial-aware IDS/IPS to monitor for and block known exploit traffic patterns targeting the specific CVE as a virtual patch.",
                "correct": True,
                "rationale": (
                    "Correct. A virtual patch using protocol-aware OT monitoring can detect and block the "
                    "specific known exploit traffic without modifying the HMI's certified firmware, providing "
                    "protection while the vendor's lengthy certification process completes."
                ),
            },
            {
                "id": "c",
                "text": "Connect the HMI directly to the internet so remote engineers can monitor it more easily during the six-month wait.",
                "correct": False,
                "rationale": (
                    "Incorrect. Directly exposing a known-vulnerable, unpatchable ICS device to the internet "
                    "dramatically increases attack surface and is the opposite of an appropriate compensating "
                    "control."
                ),
            },
            {
                "id": "d",
                "text": "Shut down the HMI and halt the affected production line for the full six months until the vendor patch is certified and released.",
                "correct": False,
                "rationale": (
                    "Incorrect. Halting production for six months is a disproportionate response when "
                    "segmentation and monitoring-based compensating controls can meaningfully reduce risk while "
                    "preserving plant operations."
                ),
            },
        ],
        "explanation": (
            "For unpatchable OT/ICS assets, the standard compensating controls are network segmentation "
            "(restricting reachability to only essential systems) and virtual patching via protocol-aware "
            "IDS/IPS monitoring — both reduce risk without requiring firmware changes or halting operations, "
            "unlike internet exposure or a full production shutdown."
        ),
    },
    {
        "id": "tvln-034",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability assessment finds a critical flaw in a 15-year-old internal application that only "
            "three employees still use, running on hardware nearing end-of-life, with no vendor support and no "
            "development team able to patch the code. Business analysis confirms the application's remaining "
            "functionality has been replaced by a newer platform for all but a legacy reporting task that can be "
            "completed manually. Which mitigation technique is MOST appropriate here?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Decommission the application and hardware entirely, migrating the remaining legacy reporting task to a manual process or the newer platform.",
                "correct": True,
                "rationale": (
                    "Correct. When a vulnerable asset has no patch path, no ongoing support, and minimal "
                    "remaining business value that can be absorbed elsewhere, decommissioning eliminates the risk "
                    "entirely rather than investing effort in compensating controls for an asset that no longer "
                    "needs to exist."
                ),
            },
            {
                "id": "b",
                "text": "Deploy a virtual patch and segment the application indefinitely, since decommissioning would be too disruptive for the three remaining users.",
                "correct": False,
                "rationale": (
                    "Incorrect. Given that the application's remaining function can be absorbed by an existing "
                    "newer platform or a manual process, indefinitely maintaining compensating controls for a "
                    "barely-used, unsupportable legacy system wastes ongoing effort compared to simply retiring it."
                ),
            },
            {
                "id": "c",
                "text": "Leave the application running unmitigated, since only three employees use it and the exposure is considered minimal.",
                "correct": False,
                "rationale": (
                    "Incorrect. User count does not equate to risk; an unpatched, unsupported, critically "
                    "vulnerable system remains a viable entry point for an attacker regardless of how few "
                    "legitimate users it has."
                ),
            },
            {
                "id": "d",
                "text": "Purchase extended vendor support to obtain a patch, even though the vendor has confirmed none is available.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states no vendor support or patch path exists at all; there is no "
                    "extended support contract that can produce a patch that does not exist."
                ),
            },
        ],
        "explanation": (
            "Decommissioning is itself a mitigation technique, and often the most efficient one when a "
            "vulnerable, unsupportable asset provides minimal remaining business value that can be absorbed by "
            "an existing platform or process — it eliminates the risk permanently rather than maintaining "
            "compensating controls indefinitely."
        ),
    },
    {
        "id": "tvln-035",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan identifies a critical vulnerability in the management interface of a network switch, "
            "exploitable only by hosts that can reach TCP port 443 on the switch's management VLAN. The switch "
            "vendor's patch requires a maintenance window not scheduled for another three weeks. In the "
            "meantime, which mitigation reduces risk MOST directly and with the least operational impact?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Apply a host-based/network ACL restricting access to the switch's management interface (TCP 443) to only the specific jump hosts network administrators use, rather than the entire management VLAN.",
                "correct": True,
                "rationale": (
                    "Correct. Since exploitation requires network reachability to the specific management port, "
                    "tightly restricting which hosts can reach it directly shrinks the realistic attack surface "
                    "with minimal operational impact, without requiring the firmware update itself."
                ),
            },
            {
                "id": "b",
                "text": "Disable the switch's management interface entirely for three weeks, preventing all administrative access until the patch window arrives.",
                "correct": False,
                "rationale": (
                    "Incorrect. Fully disabling management access for three weeks would prevent legitimate "
                    "administrators from performing necessary configuration or troubleshooting; a scoped ACL "
                    "achieves the security benefit without this operational cost."
                ),
            },
            {
                "id": "c",
                "text": "Increase the frequency of vulnerability scans against the switch to detect exploitation attempts sooner.",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent scanning improves detection but does not reduce the actual "
                    "exploitable attack surface of the management interface; it is a monitoring enhancement, not "
                    "a mitigation of the vulnerability itself."
                ),
            },
            {
                "id": "d",
                "text": "Change the switch's SNMP community string to a more complex value.",
                "correct": False,
                "rationale": (
                    "Incorrect. The vulnerability is in the management interface on TCP 443, unrelated to SNMP; "
                    "changing an unrelated credential does not address the actual exposed vulnerability."
                ),
            },
        ],
        "explanation": (
            "Restricting network reachability to only the specific administrative hosts that need it (a scoped "
            "ACL) is a targeted compensating control that directly reduces the attack surface of a vulnerable "
            "management interface while preserving legitimate administrative access — a better balance than a "
            "full outage or an unrelated monitoring/credential change."
        ),
    },
    {
        "id": "tvln-036",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A scan flags a critical vulnerability in a macro-enabled Office document workflow used by the "
            "finance team, exploited via malicious macros in email attachments. IT confirms most business "
            "processes relying on macros have been rebuilt using a supported, macro-free reporting tool, but a "
            "small number of legacy finance macros are still in daily use and cannot be immediately replaced. "
            "Which mitigation technique BEST addresses this risk while preserving the still-needed legacy "
            "macros?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Implement application allow listing so only the small set of digitally signed, approved legacy macro files can execute, while blocking all other unsigned or unapproved macros organization-wide.",
                "correct": True,
                "rationale": (
                    "Correct. Application allow listing lets the organization explicitly permit only the known, "
                    "trusted legacy macros the finance team still needs, while blocking the malicious or "
                    "unapproved macros that create the actual exploitation risk — directly addressing the threat "
                    "without breaking the required legacy workflow."
                ),
            },
            {
                "id": "b",
                "text": "Disable macros organization-wide with no exceptions, immediately breaking the finance team's remaining legacy workflows.",
                "correct": False,
                "rationale": (
                    "Incorrect. A blanket disable-all approach ignores the still-needed legitimate macros and "
                    "would disrupt finance operations; a scoped allow-listing approach achieves the security "
                    "goal without an unnecessary business disruption."
                ),
            },
            {
                "id": "c",
                "text": "Leave macros fully enabled for all users, but ask the finance team to be more careful about which email attachments they open.",
                "correct": False,
                "rationale": (
                    "Incorrect. Relying solely on user awareness/caution without any technical control leaves "
                    "the organization broadly exposed to malicious macros; awareness training is a good "
                    "supplement but not a sufficient standalone mitigation for a known exploitation vector."
                ),
            },
            {
                "id": "d",
                "text": "Increase the mailbox storage quota for the finance team so legitimate macro-enabled attachments are not rejected for being too large.",
                "correct": False,
                "rationale": (
                    "Incorrect. Mailbox storage quotas are unrelated to the malicious-macro exploitation "
                    "vector and do nothing to reduce the risk described in the scenario."
                ),
            },
        ],
        "explanation": (
            "Application allow listing is the standard mitigation technique for scoping legitimate but risky "
            "functionality (like macros) down to only explicitly approved, trusted content — blocking malicious "
            "or unapproved macros while preserving business-critical legacy workflows that cannot yet be "
            "retired."
        ),
    },
    # ---------------------------------------------------------------
    # SIEM & monitoring (4) — domain 4, objective 4.4
    # ---------------------------------------------------------------
    {
        "id": "tvln-037",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A critical CVE affecting the organization's VPN concentrator has a vendor patch available, but the "
            "change-management board will not approve emergency deployment for another five days due to a "
            "required regression test. Which SIEM configuration change would MOST directly help detect active "
            "exploitation attempts against this specific vulnerability during the five-day gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Create a targeted correlation rule/detection using the published indicators of compromise and exploit signature for this specific CVE, ingesting VPN concentrator logs, and configure it to generate a high-priority alert.",
                "correct": True,
                "rationale": (
                    "Correct. While the patch is pending, a targeted detection rule built from the CVE's known "
                    "exploit indicators and applied to the relevant log source (the VPN concentrator itself) "
                    "gives the SOC the best chance of catching an active exploitation attempt during the exposure "
                    "window, functioning as a monitoring-based compensating control."
                ),
            },
            {
                "id": "b",
                "text": "Increase the SIEM's overall log retention period from 90 days to 180 days.",
                "correct": False,
                "rationale": (
                    "Incorrect. Extending retention affects how far back historical investigation can go; it "
                    "does nothing to improve real-time detection of exploitation attempts happening during the "
                    "current five-day exposure window."
                ),
            },
            {
                "id": "c",
                "text": "Disable alerting on the VPN concentrator's logs temporarily to reduce analyst alert fatigue until the patch is deployed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling alerting during the exact window when the device is known to be "
                    "vulnerable and awaiting a patch removes the SOC's ability to detect an active attack, which "
                    "is the opposite of what is needed."
                ),
            },
            {
                "id": "d",
                "text": "Wait for the patch to be deployed in five days before making any SIEM changes related to this vulnerability.",
                "correct": False,
                "rationale": (
                    "Incorrect. This leaves the five-day exposure window completely unmonitored for exploitation "
                    "attempts against a known critical vulnerability; a targeted detection rule should be stood "
                    "up immediately, not deferred until after the patch."
                ),
            },
        ],
        "explanation": (
            "When a patch is delayed for a legitimate change-management reason, a targeted SIEM detection rule "
            "built from the CVE's known exploit indicators, applied to the relevant log source, serves as a "
            "monitoring-based compensating control — giving the SOC visibility into exploitation attempts during "
            "the exposure window rather than leaving it dark."
        ),
    },
    {
        "id": "tvln-038",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM dashboard shows a spike in alerts referencing CVE-2025-8100 exploit signatures from the IPS "
            "over the past hour, all targeting a single internal application server that vulnerability "
            "management data confirms is unpatched for that exact CVE. Correlating with the IPS action field "
            "shows the traffic was blocked. What should the SOC analyst do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Validate that the IPS truly blocked every attempt (not merely alerted) by reviewing the affected server's own logs for any signs of successful exploitation, then escalate the confirmed blocked-attack pattern to vulnerability management to accelerate patch prioritization for that host.",
                "correct": True,
                "rationale": (
                    "Correct. An IPS 'blocked' action field should be independently verified against the "
                    "target's own logs before assuming full containment, since IPS signatures can sometimes miss "
                    "variant payloads; confirming no successful exploitation occurred, then using this real "
                    "attack activity to justify accelerating remediation, is the correct combined SIEM-to-VM "
                    "workflow."
                ),
            },
            {
                "id": "b",
                "text": "Close the alerts immediately without further review, since the IPS action field already shows the traffic was blocked.",
                "correct": False,
                "rationale": (
                    "Incorrect. Trusting the IPS action field alone without correlating against the target "
                    "host's own logs risks missing a successful exploitation that evaded the specific blocked "
                    "signature variant; repeated, targeted attack attempts against a known-unpatched host warrant "
                    "verification, not automatic dismissal."
                ),
            },
            {
                "id": "c",
                "text": "Disable the IPS signature generating these alerts to reduce dashboard noise, since the traffic is already being blocked.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the very signature that is actively blocking real attack traffic "
                    "against a known-vulnerable, unpatched host removes protection precisely when it is most "
                    "needed."
                ),
            },
            {
                "id": "d",
                "text": "Immediately reimage the targeted server without further investigation, since repeated exploit attempts were observed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging is a disproportionate first step before confirming whether "
                    "exploitation actually succeeded; the priority is verification and accelerated patching, not "
                    "an unplanned rebuild based on blocked attack attempts alone."
                ),
            },
        ],
        "explanation": (
            "A spike in exploit-signature alerts against a confirmed-unpatched host requires verification "
            "beyond the IPS's own 'blocked' status — checking target-host logs for signs of successful bypass — "
            "and should feed directly into accelerating vulnerability remediation priority for that specific "
            "host, combining SIEM detection with vulnerability management action."
        ),
    },
    {
        "id": "tvln-039",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A security team wants its SIEM to automatically raise alert priority when exploitation attempts "
            "target vulnerabilities that are confirmed present and unpatched, rather than treating all exploit "
            "signature hits identically regardless of the target's actual patch status. Select the TWO actions "
            "needed to build this capability."
        ),
        "options": [
            {
                "id": "a",
                "text": "Integrate the vulnerability management platform's asset/CVE data feed into the SIEM so each asset's current unpatched-vulnerability list is available for correlation.",
                "correct": True,
                "rationale": (
                    "Correct. The SIEM needs to know, per asset, which CVEs are currently unpatched in order to "
                    "correlate incoming exploit-signature alerts against real exposure — this requires ingesting "
                    "vulnerability management data as a feed, not just network/endpoint logs."
                ),
            },
            {
                "id": "b",
                "text": "Build a correlation rule that cross-references the CVE referenced by an IPS/IDS exploit signature against that specific target asset's current unpatched-vulnerability list, boosting alert priority only on a match.",
                "correct": True,
                "rationale": (
                    "Correct. This is the actual detection logic needed: matching the exploit attempt's targeted "
                    "CVE against whether that specific asset is confirmed vulnerable, so alerts against genuinely "
                    "exposed systems are prioritized above exploit attempts against already-patched systems."
                ),
            },
            {
                "id": "c",
                "text": "Configure the SIEM to treat every exploit-signature alert as equally critical regardless of the target's patch status, to avoid missing anything.",
                "correct": False,
                "rationale": (
                    "Incorrect. Treating every alert identically is the opposite of the stated goal — the team "
                    "specifically wants to differentiate alerts against unpatched, truly vulnerable assets from "
                    "attempts against already-patched systems that pose little real risk."
                ),
            },
            {
                "id": "d",
                "text": "Remove vulnerability scan data from the SIEM entirely to reduce the volume of ingested data and improve dashboard performance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scan/asset data is exactly the input needed to build the requested "
                    "correlation capability; removing it would make the desired patch-status-aware alerting "
                    "impossible."
                ),
            },
        ],
        "explanation": (
            "Risk-aware alert prioritization requires integrating vulnerability management data into the SIEM "
            "and building correlation logic that checks whether the specific asset being targeted by an exploit "
            "attempt is actually unpatched for that CVE — elevating truly at-risk alerts above noise from "
            "attempts against already-remediated systems."
        ),
    },
    {
        "id": "tvln-040",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "After a major vulnerability scan cycle, the SOC lead wants the SIEM's alert triage queue to "
            "automatically reflect asset criticality (from the CMDB) alongside raw alert severity, so that an "
            "alert on a domain controller is never buried beneath a larger volume of alerts on low-value test "
            "systems. Which integration BEST accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Synchronize CMDB asset-criticality tags into the SIEM's asset inventory, and configure the alert triage/queue logic to weight or re-rank alerts using both the alert's technical severity and the affected asset's criticality tag.",
                "correct": True,
                "rationale": (
                    "Correct. This directly ties business context (asset criticality from the CMDB) into the "
                    "SIEM's prioritization logic, ensuring alerts on high-value systems like domain controllers "
                    "are surfaced above a higher volume of lower-value alerts, rather than relying on raw alert "
                    "count or technical severity alone."
                ),
            },
            {
                "id": "b",
                "text": "Increase the number of analysts on shift so the larger alert volume from low-value systems can be reviewed faster.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding headcount does not fix the underlying triage-ordering problem; without "
                    "criticality-aware ranking, high-value alerts can still be reviewed later than they should "
                    "be, simply processed by more people in the same flawed order."
                ),
            },
            {
                "id": "c",
                "text": "Suppress all alerts from test systems permanently so only production alerts appear in the queue.",
                "correct": False,
                "rationale": (
                    "Incorrect. Permanently suppressing an entire asset category discards potentially valid "
                    "security signal (e.g., a compromised test system used as a pivot point) rather than properly "
                    "weighting alerts by criticality while still retaining visibility."
                ),
            },
            {
                "id": "d",
                "text": "Sort the alert queue purely by timestamp so the most recent alerts always appear first.",
                "correct": False,
                "rationale": (
                    "Incorrect. Chronological sorting alone ignores both technical severity and asset "
                    "criticality entirely, which does nothing to prevent a critical domain-controller alert from "
                    "being buried under a flood of low-value system alerts."
                ),
            },
        ],
        "explanation": (
            "Effective SIEM triage combines technical alert severity with business context — asset criticality "
            "synced from the CMDB — so that alerts on high-value systems are properly weighted and surfaced "
            "above high-volume but low-value noise, rather than relying on added staffing, blanket suppression, "
            "or simple chronological ordering."
        ),
    },
]
