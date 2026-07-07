"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch C.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 2 in
``_topic_labels.json``. Brand-new scenarios distinct from d2a.py and d2b.py.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Threat actors (2.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A hospital network is hit with ransomware. The intrusion chat log "
            "recovered by responders shows the attacker's group operating a "
            "structured 'affiliate' program: a separate developer group licenses "
            "the ransomware payload for a cut of each ransom, while the operators "
            "who actually breached the hospital handle negotiation through a "
            "professional dark-web payment portal complete with a 'customer "
            "support' chat and a countdown timer. Which threat actor "
            "classification BEST fits the operators who breached the hospital?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Organized crime (ransomware-as-a-service affiliate)",
                "correct": True,
                "rationale": (
                    "Correct. A profit-driven operation using a licensed criminal "
                    "toolset, professional extortion infrastructure, and a revenue-"
                    "sharing business model is the hallmark of organized crime "
                    "operating within a ransomware-as-a-service ecosystem."
                ),
            },
            {
                "id": "b",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no strategic intelligence-gathering motive "
                    "here, only structured financial extortion through a criminal "
                    "affiliate/licensing arrangement, which points to organized "
                    "crime rather than state sponsorship."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological cause or public messaging "
                    "involved; the entire operation is structured purely around "
                    "monetizing the intrusion through ransom payment."
                ),
            },
            {
                "id": "d",
                "text": "Insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an external breach carried out by a "
                    "criminal affiliate group; there is no indication a trusted "
                    "employee with existing legitimate access was involved."
                ),
            },
        ],
        "explanation": (
            "A licensed criminal toolset, a revenue-sharing affiliate structure, "
            "and professional extortion infrastructure are the signature of "
            "organized crime operating a ransomware-as-a-service affiliation, "
            "distinct from nation-state espionage, hacktivism, or insider abuse."
        ),
    },
    {
        "id": "nd2c-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A junior analyst reviewing an intrusion into a small nonprofit's "
            "donor database finds that the attacker used a downloaded, unmodified "
            "exploit script pulled directly from a public proof-of-concept "
            "repository, left the tool's default debug output enabled — flooding "
            "the target's logs with the tool's own banner text — and posted a "
            "screenshot of the compromised admin panel to a public forum bragging "
            "about the 'hack' within an hour of gaining access. Which threat "
            "actor MOST likely carried out this intrusion?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unskilled attacker (script kiddie)",
                "correct": True,
                "rationale": (
                    "Correct. Reliance on an unmodified public tool, sloppy "
                    "tradecraft that left obvious log artifacts, and public "
                    "bragging for attention rather than profit or ideology are "
                    "classic markers of a low-skill, attention-seeking attacker."
                ),
            },
            {
                "id": "b",
                "text": "Hacker for hire (mercenary)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no evidence of a paying client or a "
                    "discreet, narrowly scoped deliverable; publicly bragging "
                    "about the intrusion is inconsistent with a professional, "
                    "paid operation that would typically want to avoid exposure."
                ),
            },
            {
                "id": "c",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. Nation-states use custom, carefully tested "
                    "tooling and avoid leaving obvious debug artifacts or "
                    "publicly bragging about access, both of which occurred here."
                ),
            },
            {
                "id": "d",
                "text": "Organized crime",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no attempt to monetize the access "
                    "through ransom, data sale, or fraud; the only observed "
                    "outcome is public bragging, not financial exploitation."
                ),
            },
        ],
        "explanation": (
            "Unmodified public tooling, sloppy operational security, and public "
            "bragging for attention rather than profit are the fingerprints of an "
            "unskilled attacker, distinguishing it from a paid mercenary, a "
            "disciplined nation-state, or profit-driven organized crime."
        ),
    },
    {
        "id": "nd2c-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Threat actors",
        "stem": (
            "A network engineer at a defense contractor begins quietly exporting "
            "schematics to a personal email account after receiving an anonymous "
            "message threatening to release compromising personal photos unless "
            "specific files are provided on a recurring schedule. Investigators "
            "determine the anonymous contact is linked to a foreign intelligence "
            "service, but the engineer personally selects, retrieves, and "
            "exfiltrates each file using their own valid access. Which threat "
            "actor classification BEST describes the engineer's role in this "
            "incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insider threat (coerced)",
                "correct": True,
                "rationale": (
                    "Correct. A trusted employee misusing their own legitimate "
                    "access to select and exfiltrate data is, by definition, "
                    "insider-threat activity — the fact that the behavior was "
                    "coerced by an external party describes the motive, not the "
                    "classification of the person actually carrying out the theft."
                ),
            },
            {
                "id": "b",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the party directing and coercing "
                    "the engineer from the outside, not the engineer's own role; "
                    "the question asks how to classify the person actually using "
                    "legitimate insider access to commit the theft."
                ),
            },
            {
                "id": "c",
                "text": "Hacker for hire",
                "correct": False,
                "rationale": (
                    "Incorrect. A hacker for hire is voluntarily paid to perform "
                    "an intrusion; the engineer is acting under blackmail, not "
                    "payment, and needed no hacking skill since they already had "
                    "legitimate access to the files."
                ),
            },
            {
                "id": "d",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological cause driving the "
                    "engineer's actions; the motive is coercion under threat, "
                    "serving a foreign intelligence service's agenda, not a "
                    "personal cause."
                ),
            },
        ],
        "explanation": (
            "Because the engineer used their own legitimate access to select and "
            "exfiltrate the data, the correct classification for their role is "
            "insider threat, even though a nation-state actor is the external "
            "party coercing and ultimately benefiting from that insider access."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "An employee receives a text message appearing to come from the "
            "company's IT department containing a link to 'verify' their VPN "
            "credentials ahead of a planned system migration. The employee taps "
            "the link on their phone and enters their username and password into "
            "a convincing but fraudulent portal. Which threat vector was used to "
            "deliver this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Message-based",
                "correct": True,
                "rationale": (
                    "Correct. The malicious link was delivered directly through "
                    "an SMS text message; delivery channel is what defines the "
                    "message-based threat vector, regardless of the specific "
                    "messaging platform used."
                ),
            },
            {
                "id": "b",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical device such as a USB drive was "
                    "involved; the payload was delivered entirely through a text "
                    "message link."
                ),
            },
            {
                "id": "c",
                "text": "Default credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. The employee's own real, previously chosen "
                    "credentials were phished; no factory-default login was "
                    "involved anywhere in this scenario."
                ),
            },
            {
                "id": "d",
                "text": "Supply chain",
                "correct": False,
                "rationale": (
                    "Incorrect. No vendor's software or update pipeline was "
                    "compromised; the attack was a direct message sent to the "
                    "employee, not something delivered through a trusted vendor "
                    "channel."
                ),
            },
        ],
        "explanation": (
            "A malicious link delivered directly via SMS text is the message-"
            "based threat vector, distinct from removable media, default-"
            "credential exposure, or a compromised supply chain."
        ),
    },
    {
        "id": "nd2c-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "At a security conference, an attendee connects a laptop to the "
            "venue's free public Wi-Fi to check email during a break. Because "
            "the network uses no encryption and broadcasts all traffic in "
            "cleartext, another attendee running a packet sniffer captures the "
            "attendee's webmail session cookie and later accesses the account "
            "without ever needing a password. Which threat vector enabled this "
            "attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unsecure network",
                "correct": True,
                "rationale": (
                    "Correct. An open, unencrypted wireless network that exposes "
                    "all traffic in cleartext to anyone nearby is the definition "
                    "of the unsecure-network threat vector, which is exactly what "
                    "allowed the session cookie to be captured."
                ),
            },
            {
                "id": "b",
                "text": "Vulnerable software",
                "correct": False,
                "rationale": (
                    "Incorrect. No software flaw in the webmail client or "
                    "operating system was exploited; the exposure came purely "
                    "from the absence of encryption on the network transport "
                    "itself."
                ),
            },
            {
                "id": "c",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media was used at any point; the "
                    "compromise happened entirely over the open wireless network."
                ),
            },
            {
                "id": "d",
                "text": "Message-based",
                "correct": False,
                "rationale": (
                    "Incorrect. No email, SMS, or chat message delivered or "
                    "triggered anything; the cookie was captured passively from "
                    "unencrypted network traffic."
                ),
            },
        ],
        "explanation": (
            "An open, unencrypted network that exposes session data to any "
            "nearby listener is the unsecure-network threat vector, distinct "
            "from a software flaw, physical media, or a delivered message."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "A warehouse's shipping coordinator receives a phone call from "
            "someone claiming to be a regional logistics dispatcher, stating "
            "that today's shipment of laptops needs to be redirected to a new "
            "consolidation address 'per updated carrier routing.' The "
            "coordinator updates the shipping label rather than escalating the "
            "change, and the pallet of laptops is picked up by a truck that is "
            "never seen again. Which social engineering attack does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Diversion theft",
                "correct": True,
                "rationale": (
                    "Correct. Tricking a party into misdirecting a legitimate "
                    "physical shipment to an attacker-controlled destination is "
                    "the specific definition of diversion theft."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Although the deception was delivered by phone, "
                    "vishing is the general term for voice-based phishing aimed "
                    "at extracting information or credentials; this specific "
                    "pattern of redirecting a physical shipment has a more "
                    "precise, dedicated classification in diversion theft."
                ),
            },
            {
                "id": "c",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. A fabricated scenario was indeed used, but the "
                    "specific named technique for tricking a target into "
                    "misdirecting a physical delivery is diversion theft, a more "
                    "precise classification than the general term pretexting."
                ),
            },
            {
                "id": "d",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. The entire attack was conducted by phone call; "
                    "no email account or message was involved at any point."
                ),
            },
        ],
        "explanation": (
            "Redirecting a legitimate physical shipment to an attacker-"
            "controlled location through a fabricated phone request is diversion "
            "theft, a more specific classification than the general terms "
            "vishing or pretexting."
        ),
    },
    {
        "id": "nd2c-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "At a trade show, a booth visitor engages a network engineer in a "
            "lengthy, friendly conversation about 'industry challenges,' "
            "gradually asking specific, technical follow-up questions about the "
            "company's firewall vendor, patch cadence, and remote-access setup. "
            "The engineer never realizes he is being questioned and happily "
            "shares the details, believing it to be normal small talk. No "
            "document, badge, or system was ever accessed. Which social "
            "engineering technique does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Elicitation",
                "correct": True,
                "rationale": (
                    "Correct. Subtly extracting sensitive information through "
                    "what feels like normal, casual conversation, without the "
                    "target ever realizing they are being questioned, is the "
                    "definition of elicitation."
                ),
            },
            {
                "id": "b",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting relies on a fabricated identity or "
                    "invented scenario to justify a request; the visitor never "
                    "adopted a false identity or cover story here, relying "
                    "purely on conversational skill to draw out information."
                ),
            },
            {
                "id": "c",
                "text": "Impersonation",
                "correct": False,
                "rationale": (
                    "Incorrect. The visitor never claimed to be a specific "
                    "person, vendor, or role to gain trust; the technique relied "
                    "entirely on a genuine-seeming conversation, not a false "
                    "identity."
                ),
            },
            {
                "id": "d",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. No visual observation of a screen, keypad, or "
                    "document was involved; all information was obtained "
                    "verbally through conversation."
                ),
            },
        ],
        "explanation": (
            "Gradually drawing sensitive technical details out of a target "
            "through seemingly casual, friendly conversation — without the "
            "target ever suspecting they are being questioned — is elicitation, "
            "distinct from pretexting's fabricated identity/scenario."
        ),
    },
    {
        "id": "nd2c-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "Review the internal chat message sent to several employees from an "
            "account posing as a well-liked, longtime coworker:\n\n"
            "\"Hey! Quick favor — IT already had me and half the team update "
            "our password through this new portal this morning, took like 30 "
            "seconds: [link]. Wanted to give you a heads up before they email "
            "everyone officially!\"\n\n"
            "Which TWO social engineering principles are being leveraged in "
            "this message? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Social proof (consensus)",
                "correct": True,
                "rationale": (
                    "Correct. Claiming that 'half the team' already completed "
                    "the action leverages the target's tendency to follow what "
                    "peers appear to have already done."
                ),
            },
            {
                "id": "b",
                "text": "Likability",
                "correct": True,
                "rationale": (
                    "Correct. The warm, casual tone and the message posing as a "
                    "well-liked, familiar coworker doing a friendly favor "
                    "leverages rapport and likability rather than pressure or "
                    "rank."
                ),
            },
            {
                "id": "c",
                "text": "Scarcity",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no claim that the offer or portal "
                    "access is limited in availability or about to expire; "
                    "nothing in the message suggests a scarce resource."
                ),
            },
            {
                "id": "d",
                "text": "Authority",
                "correct": False,
                "rationale": (
                    "Incorrect. A peer coworker is not presented as holding "
                    "organizational power or rank; the persuasion here relies on "
                    "friendliness and apparent peer consensus, not command "
                    "authority."
                ),
            },
            {
                "id": "e",
                "text": "Urgency",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no deadline or countdown pressuring "
                    "immediate action; the casual 'wanted to give you a heads "
                    "up' framing is deliberately low-pressure, not urgent."
                ),
            },
        ],
        "explanation": (
            "Claiming peers already completed the action is social proof, and "
            "impersonating a well-liked coworker with a friendly tone is "
            "likability; the message lacks the scarcity, authority, or urgency "
            "cues that would justify those other options."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A crash analysis of a custom PDF-rendering application shows that a "
            "memory object is freed when a document tab is closed, but a "
            "background rendering thread still holds a reference to that same "
            "memory region. A specially crafted PDF triggers the tab closure at "
            "a precise moment, and the background thread then writes attacker-"
            "influenced data into the already-freed memory, resulting in "
            "arbitrary code execution. Which vulnerability class does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use-after-free",
                "correct": True,
                "rationale": (
                    "Correct. Continuing to reference and write to a memory "
                    "region after it has already been deallocated, allowing an "
                    "attacker to influence what gets written there, is the "
                    "definition of a use-after-free vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No oversized input overran a fixed-size buffer "
                    "boundary; the flaw instead involves a dangling reference to "
                    "memory that was already freed and later reused."
                ),
            },
            {
                "id": "c",
                "text": "Time-of-check to time-of-use (TOCTOU) race condition",
                "correct": False,
                "rationale": (
                    "Incorrect. TOCTOU specifically involves a security check "
                    "(such as a permission or existence check) becoming stale "
                    "before the resource is used; this flaw instead involves a "
                    "low-level memory-management defect where freed memory is "
                    "dereferenced again, a related but distinct memory-safety "
                    "issue."
                ),
            },
            {
                "id": "d",
                "text": "Integer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No arithmetic value exceeded its storage type's "
                    "boundary; the flaw is about referencing deallocated memory, "
                    "not a numeric wraparound."
                ),
            },
        ],
        "explanation": (
            "Writing attacker-influenced data into memory after it has already "
            "been freed, via a dangling reference held by another thread, is a "
            "use-after-free vulnerability, distinct from buffer overflows, "
            "TOCTOU races, or integer overflows."
        ),
    },
    {
        "id": "nd2c-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A source code review of an internal inventory application finds a "
            "database connection string, including a plaintext administrator "
            "username and password, hardcoded directly into a source file "
            "stored in the company's shared, broadly-readable code repository. "
            "Any developer with repository read access — including several "
            "contractors whose engagement ended months ago — can retrieve full "
            "administrative access to the production database. Which "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hardcoded/embedded credentials",
                "correct": True,
                "rationale": (
                    "Correct. Storing plaintext administrative credentials "
                    "directly in source code, where anyone with repository "
                    "access — including former contractors — can retrieve them, "
                    "is the definition of a hardcoded-credentials vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. No serialized object is being reconstructed "
                    "from untrusted data; the issue is a plaintext credential "
                    "embedded directly in a source file."
                ),
            },
            {
                "id": "c",
                "text": "Insecure direct object reference (IDOR)",
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR involves manipulating an object reference "
                    "within a running application to access another user's "
                    "data; this issue instead concerns credentials embedded "
                    "directly in source code, a distinct root cause."
                ),
            },
            {
                "id": "d",
                "text": "SQL injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No injected query syntax is involved; the "
                    "database is reached using legitimate, though improperly "
                    "stored, administrator credentials."
                ),
            },
        ],
        "explanation": (
            "Plaintext administrative credentials embedded directly in a "
            "broadly readable source file, retrievable by anyone with "
            "repository access, is a hardcoded/embedded-credentials "
            "vulnerability."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A tester crafts a search-page link containing a script payload in "
            "the query string and emails it to a target, disguised as a 'view "
            "your order' link. When the victim clicks the link, the search "
            "results page echoes the query parameter directly into the page "
            "without encoding, executing the script in the victim's browser and "
            "sending their session cookie to the attacker's server. The payload "
            "is never saved anywhere on the server. Which vulnerability was "
            "exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reflected cross-site scripting (XSS)",
                "correct": True,
                "rationale": (
                    "Correct. The script exists only within the crafted URL "
                    "itself and executes when that specific link is clicked, "
                    "with nothing persisted on the server — the defining trait "
                    "of reflected XSS."
                ),
            },
            {
                "id": "b",
                "text": "Stored cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. Stored XSS persists the payload server-side so "
                    "it affects any future visitor; here the payload exists "
                    "only in the one-time crafted link and requires that "
                    "specific victim to click it, with nothing saved server-"
                    "side."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF forces a victim's browser to submit an "
                    "unwanted state-changing request using their existing "
                    "session; here the attack instead injects and executes a "
                    "script that then steals the session cookie, a distinct "
                    "client-side scripting exploit."
                ),
            },
            {
                "id": "d",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF causes the server itself to issue an "
                    "unintended request; here the payload executes in the "
                    "victim's own browser via a script reflected back in the "
                    "page, not a server-issued request."
                ),
            },
        ],
        "explanation": (
            "A script payload carried entirely within a crafted URL, executed "
            "only when that specific link is clicked and never persisted "
            "server-side, is reflected XSS, distinct from stored XSS, CSRF, or "
            "SSRF."
        ),
    },
    {
        "id": "nd2c-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A network diagnostics page on an internal appliance lets "
            "administrators type a hostname to ping. A tester submits "
            "\"8.8.8.8; cat /etc/passwd\" as the hostname, and the resulting "
            "page displays both the ping output and the full contents of the "
            "system's password file. Which vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Command injection",
                "correct": True,
                "rationale": (
                    "Correct. Using a shell metacharacter to chain and execute "
                    "an additional operating system command onto a legitimate "
                    "one is the definition of command injection."
                ),
            },
            {
                "id": "b",
                "text": "SQL injection",
                "correct": False,
                "rationale": (
                    "Incorrect. The payload terminates and chains an OS shell "
                    "command using a semicolon rather than manipulating SQL "
                    "query syntax against a database."
                ),
            },
            {
                "id": "c",
                "text": "Directory traversal",
                "correct": False,
                "rationale": (
                    "Incorrect. No relative path sequence such as \"../\" was "
                    "used to escape a restricted directory; instead, a shell "
                    "metacharacter was used to chain a second OS command onto "
                    "the legitimate one."
                ),
            },
            {
                "id": "d",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. The appliance did not make an unintended "
                    "network request to another host; the input directly "
                    "reached and was executed by the underlying operating "
                    "system shell."
                ),
            },
        ],
        "explanation": (
            "Appending a shell metacharacter and a second command to a field "
            "that is passed directly to the operating system shell is command "
            "injection, distinct from SQL injection, directory traversal, or "
            "SSRF."
        ),
    },
    {
        "id": "nd2c-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A tester hosts a malicious webpage containing a hidden, auto-"
            "submitting HTML form that targets a banking application's "
            "/transfer-funds endpoint. When a logged-in victim visits the "
            "malicious page in the same browser, the hidden form silently "
            "submits, and the browser automatically includes the victim's valid "
            "session cookie, initiating a transfer to the attacker's account "
            "with no visible interaction from the victim and no JavaScript ever "
            "executing within the banking application's own origin. Which TWO "
            "facts confirm this is a cross-site request forgery (CSRF) attack "
            "rather than XSS or SSRF? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The victim's own browser automatically attached their "
                    "valid session cookie to a request they never intended to "
                    "send"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Relying on the browser's automatic inclusion of "
                    "stored credentials/cookies with a forged, unintended "
                    "request is the defining mechanism of CSRF."
                ),
            },
            {
                "id": "b",
                "text": (
                    "No script ever executed within the banking application's "
                    "own origin/domain"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The absence of any script execution in the "
                    "target application's trusted context rules out XSS, which "
                    "requires the attacker's script to run within the "
                    "vulnerable site's own origin."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The attacker's page made a direct server-to-server "
                    "request to the bank on the attacker's behalf"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes SSRF, where the target server "
                    "itself issues an outbound request; here it was the "
                    "victim's own browser, not a server, that submitted the "
                    "forged request."
                ),
            },
            {
                "id": "d",
                "text": "The transfer amount exceeded the account's normal daily limit",
                "correct": False,
                "rationale": (
                    "Incorrect. The transaction amount has no bearing on which "
                    "web application vulnerability class was exploited."
                ),
            },
            {
                "id": "e",
                "text": (
                    "The malicious page's form field referenced a relative "
                    "file path containing \"../\" sequences"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes directory traversal, which "
                    "manipulates file-path parameters to escape a restricted "
                    "directory; no file-path manipulation is involved in this "
                    "forged funds-transfer request."
                ),
            },
        ],
        "explanation": (
            "The victim's browser automatically attaching stored session "
            "credentials to a forged request, with no script execution ever "
            "occurring in the target's own origin, are the two facts that "
            "distinguish CSRF from XSS (which requires in-origin script "
            "execution) and SSRF (which requires the server to issue its own "
            "outbound request)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "An employee at an outdoor kiosk scans a QR code advertising 'free "
            "event Wi-Fi setup' and, following the on-screen prompts, installs a "
            "configuration profile on their corporate-managed iPhone. The "
            "profile silently redirects all of the device's web traffic through "
            "an attacker-controlled proxy and installs a rogue root "
            "certificate, allowing the attacker to decrypt the device's HTTPS "
            "traffic. Which mobile vulnerability MOST directly enabled this "
            "attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malicious configuration profile installation",
                "correct": True,
                "rationale": (
                    "Correct. Tricking a user into installing a configuration "
                    "profile that redirects traffic and adds a rogue trusted "
                    "root certificate abuses a legitimate device-management "
                    "feature for malicious interception."
                ),
            },
            {
                "id": "b",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. No OS-level restrictions were removed; the "
                    "device remained in its normal, managed state, but the user "
                    "was tricked into installing a profile using a legitimate, "
                    "built-in configuration capability."
                ),
            },
            {
                "id": "c",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. No carrier-level number port occurred; the "
                    "compromise happened entirely through the device accepting "
                    "a malicious configuration profile."
                ),
            },
            {
                "id": "d",
                "text": "Excessive application permissions",
                "correct": False,
                "rationale": (
                    "Incorrect. No app permission is involved here; the "
                    "traffic interception was enabled by a device-level "
                    "configuration/certificate installation, not an app's "
                    "requested permissions."
                ),
            },
        ],
        "explanation": (
            "Installing a malicious configuration profile that redirects "
            "traffic and adds a rogue trusted certificate is a mobile "
            "vulnerability distinct from jailbreaking, SIM swapping, or "
            "excessive app permissions."
        ),
    },
    {
        "id": "nd2c-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "Commuters on a train report their phones repeatedly displaying "
            "unsolicited pop-up messages and contact-card invitations with "
            "crude advertising content whenever they enable Bluetooth "
            "discovery mode near a particular seat. No data is taken from any "
            "device, and no pairing is ever completed — the messages simply "
            "appear and can be dismissed. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bluejacking",
                "correct": True,
                "rationale": (
                    "Correct. Sending unsolicited messages or content to "
                    "nearby Bluetooth-discoverable devices, without extracting "
                    "any data or completing a pairing, is the definition of "
                    "bluejacking."
                ),
            },
            {
                "id": "b",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing involves unauthorized extraction "
                    "of data such as contacts or files from the victim's "
                    "device; here no data is taken, only unsolicited messages "
                    "are pushed to the device."
                ),
            },
            {
                "id": "c",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. No carrier or phone-number takeover is "
                    "involved; this is a short-range Bluetooth messaging "
                    "nuisance, unrelated to cellular service."
                ),
            },
            {
                "id": "d",
                "text": "Evil twin attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No rogue Wi-Fi access point mimicking a "
                    "legitimate SSID is involved; the vector here is Bluetooth "
                    "proximity messaging, not Wi-Fi."
                ),
            },
        ],
        "explanation": (
            "Pushing unsolicited messages to nearby devices without extracting "
            "any data or completing a pairing is bluejacking, distinct from "
            "bluesnarfing (data theft), SIM swapping, or an evil twin access "
            "point."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A cloud provider's incident response team determines that a "
            "customer's VM exploited a flaw in the virtual GPU passthrough "
            "driver to execute arbitrary code directly on the physical "
            "hypervisor, subsequently gaining read/write access to a co-located "
            "tenant's VM memory on the same host. The flaw existed specifically "
            "in how the hypervisor mediated device access. Which vulnerability "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM escape",
                "correct": True,
                "rationale": (
                    "Correct. Breaking out of a guest VM's isolation boundary "
                    "by exploiting a flaw in the hypervisor's device mediation, "
                    "then reaching another tenant's memory, is the definition of "
                    "VM escape."
                ),
            },
            {
                "id": "b",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. Sprawl is an unmanaged accumulation of "
                    "forgotten VMs over time; this is an active exploit of a "
                    "device-mediation flaw to break out of VM isolation."
                ),
            },
            {
                "id": "c",
                "text": "Resource reuse (data remnants)",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse involves residual data left in "
                    "storage or memory reassigned after deallocation; this is "
                    "an active isolation-breaking exploit against a running "
                    "VM's device driver, not leftover data."
                ),
            },
            {
                "id": "d",
                "text": "Hyperjacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Hyperjacking involves installing an entirely "
                    "separate, rogue hypervisor beneath the legitimate one; "
                    "here the attacker instead broke out of an existing guest "
                    "VM through the legitimate hypervisor's own device-"
                    "passthrough driver."
                ),
            },
        ],
        "explanation": (
            "Exploiting a hypervisor device-mediation flaw to break out of a "
            "guest VM and reach another tenant's memory is VM escape, distinct "
            "from sprawl, resource reuse, or installing a rogue hypervisor."
        ),
    },
    {
        "id": "nd2c-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A cloud customer terminates a VM that briefly held a private TLS "
            "key in memory. Minutes later, a new VM is provisioned on the same "
            "physical host and allocated some of the same RAM pages, which were "
            "not zeroed by the hypervisor before reassignment. Using a memory-"
            "scraping technique, the new tenant's process recovers fragments of "
            "the previous VM's private key directly from the freed RAM. Which "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource reuse (data remnants)",
                "correct": True,
                "rationale": (
                    "Correct. Reassigning physical memory to a new tenant "
                    "without sanitizing it first leaves recoverable remnants of "
                    "the prior tenant's data — a resource-reuse/data-remanence "
                    "issue in shared virtualized memory."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. No isolation boundary was actively breached "
                    "between two running VMs; the second VM simply received "
                    "unsanitized RAM pages previously used by another, now-"
                    "terminated VM."
                ),
            },
            {
                "id": "c",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. Sprawl describes unmanaged, forgotten VMs "
                    "accumulating over time, not a single instance of "
                    "unsanitized memory reassignment between a terminated and a "
                    "new VM."
                ),
            },
            {
                "id": "d",
                "text": "Hyperjacking",
                "correct": False,
                "rationale": (
                    "Incorrect. No rogue hypervisor was installed; the flaw "
                    "here is the legitimate hypervisor's failure to zero RAM "
                    "before reassignment."
                ),
            },
        ],
        "explanation": (
            "Recovering a prior tenant's data from unsanitized RAM reassigned "
            "to a new VM is a resource reuse (data remanence) vulnerability, "
            "distinct from VM escape, sprawl, or hyperjacking."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A vulnerability scan of a newly hardened jump server reports no "
            "findings. A separate manual penetration test performed the same "
            "week, using both automated tools and manual exploitation attempts, "
            "also confirms no exploitable weaknesses exist on the host. How "
            "should the original scan result be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "True negative",
                "correct": True,
                "rationale": (
                    "Correct. The scan reported no vulnerabilities, and "
                    "independent manual testing confirmed that none actually "
                    "exist, making this an accurate negative result."
                ),
            },
            {
                "id": "b",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative requires a real vulnerability "
                    "that went undetected; here independent manual testing "
                    "confirmed none actually exists, so the scan's clean result "
                    "is accurate."
                ),
            },
            {
                "id": "c",
                "text": "False positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A false positive requires the scan to have "
                    "reported a vulnerability that isn't real; this scan "
                    "reported nothing at all."
                ),
            },
            {
                "id": "d",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A true positive requires a reported and "
                    "confirmed vulnerability; no vulnerability was reported "
                    "here."
                ),
            },
        ],
        "explanation": (
            "When a scan reports no vulnerabilities and independent testing "
            "confirms none exist, the result is a true negative, the accurate "
            "counterpart to a false negative, false positive, or true "
            "positive."
        ),
    },
    {
        "id": "nd2c-019",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "An automated vulnerability scanner reports zero issues on an e-"
            "commerce checkout flow. During a subsequent manual assessment, a "
            "tester discovers that submitting a negative quantity in the cart "
            "causes the application to credit the customer's stored balance "
            "instead of charging it — a flaw the scanner's signature-based "
            "checks were never designed to recognize because it involves the "
            "application's business logic rather than a known CVE or malformed-"
            "input pattern. How should the original scanner's silence on this "
            "issue be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False negative",
                "correct": True,
                "rationale": (
                    "Correct. A real, exploitable flaw existed but the "
                    "automated tool failed to detect and report it — a false "
                    "negative, here caused by a fundamental limitation of "
                    "signature-based tools against business-logic flaws."
                ),
            },
            {
                "id": "b",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative requires that no vulnerability "
                    "actually exists; here a real, exploitable flaw was later "
                    "confirmed by manual testing."
                ),
            },
            {
                "id": "c",
                "text": "False positive",
                "correct": False,
                "rationale": (
                    "Incorrect. False positive applies to something "
                    "incorrectly reported as a finding; the scanner reported "
                    "nothing at all on this checkout flow."
                ),
            },
            {
                "id": "d",
                "text": "Indicator of compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. An IoC is forensic evidence of an actual "
                    "completed breach; this question concerns classifying a "
                    "scan's undetected finding, not evidence that exploitation "
                    "occurred."
                ),
            },
        ],
        "explanation": (
            "A real, exploitable business-logic flaw that an automated "
            "scanner's signature-based checks were never designed to detect is "
            "a false negative, illustrating a key limitation of automated "
            "scanning versus manual assessment."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "An SSO dashboard shows a marketing director's account holding two "
            "simultaneously active sessions: one actively editing a "
            "presentation from the New York office's corporate IP address, and "
            "a second, separate active session at that same moment issuing API "
            "calls against the HR system from an IP address in a country the "
            "director has never traveled to. Both sessions remain open at "
            "once. Which indicator does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Concurrent session anomaly",
                "correct": True,
                "rationale": (
                    "Correct. The same account holding two simultaneously "
                    "active sessions from divergent locations, both open at "
                    "once, is the concurrent-session indicator."
                ),
            },
            {
                "id": "b",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel refers to two sequential "
                    "successful logins from locations that couldn't both be "
                    "reached in the elapsed time; here both sessions are open "
                    "and active at the very same moment, not sequential logins."
                ),
            },
            {
                "id": "c",
                "text": "Privilege escalation",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no indication the account's own "
                    "permissions were changed or elevated; the concern is two "
                    "simultaneous sessions from divergent locations, not a "
                    "change in assigned privileges."
                ),
            },
            {
                "id": "d",
                "text": "Resource consumption anomaly",
                "correct": False,
                "rationale": (
                    "Incorrect. This indicator concerns abnormal CPU, memory, "
                    "or bandwidth usage, not simultaneous active sessions from "
                    "different locations."
                ),
            },
        ],
        "explanation": (
            "Two genuinely simultaneous, active sessions on the same account "
            "from geographically divergent locations is a concurrent-session "
            "anomaly, distinct from the sequential-login pattern of impossible "
            "travel."
        ),
    },
    {
        "id": "nd2c-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Authentication logs show a single external IP address attempting "
            "to log in to 400 different employee accounts over six hours, using "
            "the exact same password, \"Winter2024!\", against every account "
            "exactly once, with no account locked out because each one only "
            "received a single failed attempt. Which attack does this "
            "indicator MOST likely represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Password spraying",
                "correct": True,
                "rationale": (
                    "Correct. A single common password tried against many "
                    "accounts, one attempt each, specifically to stay under "
                    "per-account lockout thresholds, is the signature of "
                    "password spraying."
                ),
            },
            {
                "id": "b",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing tests previously breached, "
                    "unique username/password pairs harvested from other "
                    "sites, not the same single guessed password reused across "
                    "every account."
                ),
            },
            {
                "id": "c",
                "text": "Brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Brute force concentrates many attempts "
                    "against a single account, trying many passwords; here it "
                    "is the opposite — one password tried once against many "
                    "different accounts."
                ),
            },
            {
                "id": "d",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting harvests and offline-cracks "
                    "Kerberos service tickets; it does not generate a pattern "
                    "of live web/domain authentication attempts across many "
                    "accounts like this."
                ),
            },
        ],
        "explanation": (
            "A single password tried exactly once against hundreds of "
            "different accounts, deliberately staying under per-account "
            "lockout thresholds, is password spraying, distinct from "
            "credential stuffing, brute force, or Kerberoasting."
        ),
    },
    {
        "id": "nd2c-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Endpoint monitoring flags a finance department workstation with "
            "CPU utilization pinned at 100% around the clock, including "
            "overnight and weekends when no user is logged in. A newly created "
            "scheduled task launches an unsigned binary named \"svchost32.exe\" "
            "(note the added digits) at every boot, which then opens a "
            "persistent outbound connection to a known cryptocurrency mining "
            "pool address. Which TWO findings BEST confirm this is cryptojacking "
            "malware rather than a legitimate but resource-intensive "
            "application? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Sustained 100% CPU usage occurring even when no user is "
                    "logged in"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Legitimate resource-intensive applications are "
                    "typically tied to active user sessions or scheduled "
                    "business jobs; unexplained round-the-clock maximum CPU "
                    "usage with no user present is a strong cryptomining "
                    "indicator."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The persistent outbound connection to a known "
                    "cryptocurrency mining pool address"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is direct evidence of the specific "
                    "malicious purpose — connecting to infrastructure used to "
                    "submit mining work and receive payouts."
                ),
            },
            {
                "id": "c",
                "text": "The binary was launched via a scheduled task",
                "correct": False,
                "rationale": (
                    "Incorrect. Scheduled tasks are an entirely routine and "
                    "common mechanism used by countless legitimate "
                    "applications for persistence; alone, this is not a "
                    "distinguishing indicator of malicious intent."
                ),
            },
            {
                "id": "d",
                "text": "The workstation belongs to the finance department",
                "correct": False,
                "rationale": (
                    "Incorrect. Which department a workstation belongs to has "
                    "no bearing on whether the process running on it is "
                    "malicious."
                ),
            },
            {
                "id": "e",
                "text": "The binary's filename closely mimics a legitimate Windows process name",
                "correct": False,
                "rationale": (
                    "Incorrect. While suspicious, a mimicked filename alone is "
                    "circumstantial and far weaker evidence than direct proof "
                    "of the malware's behavior and network destination; on its "
                    "own it does not confirm cryptojacking as clearly as the "
                    "round-the-clock CPU usage and mining-pool connection do."
                ),
            },
        ],
        "explanation": (
            "Round-the-clock maximum CPU usage with no user present, combined "
            "with a persistent connection to a known mining pool, are the "
            "specific indicators confirming cryptojacking; the scheduling "
            "mechanism and the department the host belongs to are both too "
            "generic to be meaningful on their own."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "An employee downloads what they believe is a legitimate PDF-"
            "editing utility from a third-party download site. The installer "
            "displays a normal-looking setup wizard and the PDF editor works "
            "exactly as advertised, but it also silently installs a hidden "
            "background service that opens a remote-access backdoor to an "
            "external server. The malware does not attempt to spread to any "
            "other host on the network. Which malware type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trojan",
                "correct": True,
                "rationale": (
                    "Correct. Disguising malicious functionality inside "
                    "software that also performs its advertised, legitimate "
                    "purpose, tricking the user into installing it themselves, "
                    "is the definition of a trojan."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. Worms self-propagate across a network without "
                    "needing to disguise themselves as legitimate software; "
                    "this malware spread through a voluntary download of a "
                    "disguised utility and shows no network-spreading "
                    "behavior."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb lies dormant until a specific "
                    "triggering condition; this backdoor is actively "
                    "established and usable immediately upon installation, not "
                    "waiting on a condition."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit's defining trait is concealing an "
                    "existing compromise at the OS/kernel level; this scenario "
                    "centers on the deceptive delivery method — a disguised, "
                    "seemingly legitimate installer — not on concealment "
                    "techniques after infection."
                ),
            },
        ],
        "explanation": (
            "Legitimate-looking, fully functional software that also secretly "
            "installs a backdoor, relying on the user to voluntarily install "
            "it, is a trojan, distinct from a self-propagating worm, a "
            "condition-triggered logic bomb, or a concealment-focused rootkit."
        ),
    },
    {
        "id": "nd2c-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Multiple employees report that after opening a shared quarterly-"
            "report spreadsheet and clicking 'Enable Content' to allow macros, "
            "their own personal spreadsheet files created afterward also become "
            "infected and begin corrupting formulas — but only on their local "
            "machine; the infection never crosses to any other host or network "
            "share on its own. Which malware type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Virus",
                "correct": True,
                "rationale": (
                    "Correct. Requiring a host file and explicit user action "
                    "— opening the file and enabling macros — to execute, and "
                    "then infecting other local files without self-propagating "
                    "across the network, matches the classic definition of a "
                    "virus."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. Worms self-propagate across networks/hosts "
                    "without requiring a user to open an infected file each "
                    "time; this infection instead requires the user to "
                    "actively open and enable macros in each file, and stays "
                    "local to the machine."
                ),
            },
            {
                "id": "c",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan disguises itself as an entirely "
                    "different, desirable piece of software to trick "
                    "installation; here the file is a normal, expected "
                    "spreadsheet that becomes a carrier once macros are "
                    "enabled, matching virus behavior, not deceptive-software "
                    "delivery."
                ),
            },
            {
                "id": "d",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. No files are encrypted and no ransom is "
                    "demanded; the malware corrupts formulas and spreads to "
                    "other local files, not holding data hostage for payment."
                ),
            },
        ],
        "explanation": (
            "A host-file-dependent infection that requires explicit user "
            "action (opening the file, enabling macros) and spreads only to "
            "other local files, not across the network, is a virus, distinct "
            "from a self-propagating worm, a deceptively packaged trojan, or "
            "ransomware."
        ),
    },
    {
        "id": "nd2c-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "IT notices a spike in the company's cloud compute bill and, upon "
            "investigation, finds a background process running on several web "
            "servers that is not part of any deployed application, silently "
            "consuming 90% of available CPU cycles around the clock and "
            "periodically submitting completed work units to an external "
            "mining pool in exchange for cryptocurrency credited to a wallet "
            "address unrelated to the company. No files are encrypted, and no "
            "data appears to have been exfiltrated. Which malware type is "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cryptojacking (cryptomining malware)",
                "correct": True,
                "rationale": (
                    "Correct. Silently stealing computing resources to mine "
                    "cryptocurrency for an attacker-controlled wallet, without "
                    "encrypting files or exfiltrating data, is the definition "
                    "of cryptojacking."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. No files are encrypted and no ransom demand "
                    "exists; the malware is instead stealing computing "
                    "resources to mine cryptocurrency for the attacker."
                ),
            },
            {
                "id": "c",
                "text": "Botnet (DDoS zombie)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no indication the servers are being "
                    "used to send attack traffic against a third party; the "
                    "resource theft here is directed at generating "
                    "cryptocurrency, not launching coordinated attacks."
                ),
            },
            {
                "id": "d",
                "text": "Memory leak (resource exhaustion)",
                "correct": False,
                "rationale": (
                    "Incorrect. A memory leak is an unintentional coding "
                    "defect that gradually consumes memory with no external "
                    "benefit to an attacker; here CPU is deliberately consumed "
                    "by an external process that yields cryptocurrency "
                    "payouts to a specific wallet, indicating malicious intent, "
                    "not a bug."
                ),
            },
        ],
        "explanation": (
            "A hidden process consuming CPU cycles to submit work to a mining "
            "pool for an attacker's wallet, with no encryption or "
            "exfiltration, is cryptojacking, distinct from ransomware, a DDoS "
            "botnet, or an unintentional memory leak."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A network analyst notices a switch's CAM (content-addressable "
            "memory) table has been filled with tens of thousands of bogus, "
            "rapidly changing source MAC addresses arriving from a single port "
            "within seconds. Shortly after, the switch begins broadcasting "
            "unicast traffic for legitimate hosts out of every port instead of "
            "only the correct destination port, and a laptop connected to an "
            "unrelated port begins capturing traffic that was never addressed "
            "to it. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MAC flooding",
                "correct": True,
                "rationale": (
                    "Correct. Overwhelming a switch's CAM table with bogus "
                    "addresses, forcing it into hub-like broadcast behavior for "
                    "all traffic, is the definition of MAC flooding."
                ),
            },
            {
                "id": "b",
                "text": "ARP poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning forges MAC-to-IP bindings to "
                    "redirect traffic to a specific attacker host; this attack "
                    "instead overwhelms the switch's address table itself, "
                    "forcing it into broadcast/hub-like behavior for all "
                    "traffic."
                ),
            },
            {
                "id": "c",
                "text": "DHCP spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP spoofing hands out malicious lease "
                    "configurations to new clients requesting an address; it "
                    "does not involve overflowing a switch's MAC address "
                    "table with bogus entries."
                ),
            },
            {
                "id": "d",
                "text": "Evil twin attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin is a rogue wireless access point "
                    "mimicking a legitimate SSID; this attack occurred on a "
                    "wired switch's CAM table, an entirely different "
                    "mechanism."
                ),
            },
        ],
        "explanation": (
            "Overflowing a switch's CAM table with bogus MAC addresses to "
            "force it into hub-like broadcast behavior, enabling passive "
            "sniffing from any port, is MAC flooding, distinct from ARP "
            "poisoning, DHCP spoofing, or an evil twin."
        ),
    },
    {
        "id": "nd2c-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "New laptops joining a branch office's wired network begin "
            "receiving IP configuration pointing to a DNS server and default "
            "gateway that do not match any device on the organization's "
            "approved infrastructure list. Investigation traces the source to "
            "an unauthorized device plugged into an open conference-room jack "
            "that responds to DHCP requests faster than the legitimate "
            "corporate DHCP server. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP spoofing (rogue DHCP server)",
                "correct": True,
                "rationale": (
                    "Correct. An unauthorized device racing to answer DHCP "
                    "requests with malicious gateway and DNS configuration "
                    "before the legitimate server responds is the definition "
                    "of DHCP spoofing."
                ),
            },
            {
                "id": "b",
                "text": "DNS cache poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS poisoning corrupts a resolver's cached "
                    "records after normal IP configuration; here the "
                    "malicious DNS server address itself is being handed out "
                    "directly during IP lease assignment, before any DNS "
                    "query is even made."
                ),
            },
            {
                "id": "c",
                "text": "ARP poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning forges MAC-to-IP bindings on "
                    "hosts already configured on the network; this attack "
                    "instead supplies the initial network configuration "
                    "itself via a race against the legitimate DHCP server."
                ),
            },
            {
                "id": "d",
                "text": "MAC flooding",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding overwhelms a switch's address "
                    "table to force broadcast behavior; this attack instead "
                    "races to answer DHCP requests with malicious "
                    "configuration, an entirely different technique."
                ),
            },
        ],
        "explanation": (
            "An unauthorized device racing the legitimate DHCP server to hand "
            "out malicious gateway/DNS configuration to new clients is DHCP "
            "spoofing, distinct from DNS poisoning, ARP poisoning, or MAC "
            "flooding."
        ),
    },
    {
        "id": "nd2c-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "Users report intermittent browser certificate warnings when "
            "accessing the company's internal HR portal. A network engineer "
            "captures traffic and finds that the TLS certificate currently "
            "being presented to internal clients has a different serial number "
            "and issuer than the certificate actually installed on the HR "
            "server, and that the number of network hops (TTL decrement) to the "
            "HR server's IP address has unexpectedly increased by one compared "
            "to the documented baseline topology. Which TWO findings BEST "
            "support the conclusion that an on-path (man-in-the-middle) attack "
            "is occurring? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The presented TLS certificate does not match the one "
                    "actually installed on the legitimate server"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A substituted certificate is direct evidence "
                    "that traffic is being intercepted and re-terminated by an "
                    "intermediary rather than reaching the real server "
                    "directly."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The measured hop count to the server increased beyond "
                    "the documented baseline"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An unexplained extra hop is consistent with "
                    "traffic now being routed through an additional attacker-"
                    "controlled device sitting inline between the client and "
                    "server."
                ),
            },
            {
                "id": "c",
                "text": "The HR portal uses TLS encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Using TLS is completely routine for any "
                    "internal web portal and is not itself evidence of "
                    "interception; it is the mismatched certificate that "
                    "matters, not the mere presence of encryption."
                ),
            },
            {
                "id": "d",
                "text": "The warnings occurred on multiple different users' browsers",
                "correct": False,
                "rationale": (
                    "Incorrect. By itself, multiple users seeing warnings "
                    "could also result from a simple expired or misconfigured "
                    "legitimate certificate; without the certificate mismatch "
                    "and hop-count evidence, this fact alone doesn't confirm "
                    "interception."
                ),
            },
            {
                "id": "e",
                "text": "The HR portal is hosted on an internal, private IP address",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal hosting is completely routine for an "
                    "HR portal and provides no evidence one way or another "
                    "about whether traffic is being intercepted in transit."
                ),
            },
        ],
        "explanation": (
            "A substituted TLS certificate combined with an unexplained extra "
            "network hop are the specific findings confirming an inline on-"
            "path interception; the mere use of TLS and the number of affected "
            "users are both too generic to confirm an attack on their own."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A competitor gains detailed knowledge of a company's unreleased "
            "product pricing after an investigation reveals that draft pricing "
            "sheets marked \"Confidential — Internal Only\" were thrown into an "
            "unlocked recycling bin behind the office, unshredded, where they "
            "were retrieved by someone sorting through the bin after hours. No "
            "computer system, badge, or network was ever accessed. Which "
            "physical attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dumpster diving",
                "correct": True,
                "rationale": (
                    "Correct. Retrieving sensitive information from improperly "
                    "discarded physical documents is the definition of "
                    "dumpster diving."
                ),
            },
            {
                "id": "b",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves directly observing "
                    "someone entering information or viewing a screen in real "
                    "time; this attack involved retrieving discarded physical "
                    "documents, not live observation."
                ),
            },
            {
                "id": "c",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating involves physically following an "
                    "authorized person through a secured door; no facility "
                    "access or door was involved here, only retrieval of "
                    "discarded trash."
                ),
            },
            {
                "id": "d",
                "text": "Badge cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. Badge cloning involves capturing and "
                    "duplicating an RFID/proximity credential; no electronic "
                    "credential was involved in this paper-document retrieval."
                ),
            },
        ],
        "explanation": (
            "Recovering confidential information from improperly discarded "
            "paper documents in an unsecured bin is dumpster diving, distinct "
            "from shoulder surfing, tailgating, or badge cloning."
        ),
    },
    {
        "id": "nd2c-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A data center's cooling system unexpectedly shuts down, causing "
            "ambient temperature to rise rapidly and triggering automatic "
            "shutdown of several server racks to prevent thermal damage. "
            "Facilities investigation finds that an unauthorized individual "
            "accessed the mechanical room using a stolen maintenance badge and "
            "manually disabled the HVAC controller, then left without touching "
            "any server or network equipment directly. Which physical attack "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Environmental attack",
                "correct": True,
                "rationale": (
                    "Correct. Deliberately sabotaging building systems such as "
                    "HVAC/cooling to disrupt operations is an environmental "
                    "physical attack."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. The individual used a stolen badge to gain "
                    "entry rather than following an authorized person through "
                    "a door without any credential of their own."
                ),
            },
            {
                "id": "c",
                "text": "Badge cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. A stolen physical badge was used directly; no "
                    "wireless capture-and-duplication of a credential signal "
                    "is described."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. No discarded materials were involved; the "
                    "attack directly sabotaged operational building "
                    "infrastructure."
                ),
            },
        ],
        "explanation": (
            "Deliberately disabling a facility's HVAC/cooling system to "
            "disrupt operations is an environmental attack, distinct from "
            "tailgating, badge cloning, or dumpster diving."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A mobile banking app allows a 4-digit numeric PIN with no limit on "
            "the number of attempts and no lockout or delay between tries. An "
            "attacker writes a script that automates entry of every possible "
            "PIN combination from 0000 to 9999 against a stolen, unlocked "
            "device, successfully unlocking it after trying roughly 3,000 "
            "combinations in under two minutes. Which attack technique was "
            "used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Brute-force attack",
                "correct": True,
                "rationale": (
                    "Correct. Systematically and exhaustively trying all "
                    "possible values of a small keyspace until the correct one "
                    "is found, with no throttling to stop it, is the "
                    "definition of a brute-force attack."
                ),
            },
            {
                "id": "b",
                "text": "Dictionary attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A dictionary attack tests a curated list of "
                    "likely, real-world values such as common passwords or "
                    "words; this attack instead exhaustively tried every "
                    "possible numeric combination in the entire keyspace, not "
                    "a curated list."
                ),
            },
            {
                "id": "c",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Rainbow tables reverse a captured password "
                    "hash using precomputed lookups; here the attacker is "
                    "directly attempting live PIN entries against the "
                    "unlocked device's lock screen, not reversing a stored "
                    "hash."
                ),
            },
            {
                "id": "d",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing tests breached username/"
                    "password pairs from other services against a login; this "
                    "attack instead exhaustively guesses every possible PIN "
                    "value on a single device with no prior credential list."
                ),
            },
        ],
        "explanation": (
            "Exhaustively trying every possible value in a small keyspace, "
            "with no throttling in place, is a brute-force attack, distinct "
            "from a curated dictionary attack, a rainbow table lookup, or "
            "credential stuffing."
        ),
    },
    {
        "id": "nd2c-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A researcher studying a smart card's cryptographic chip measures "
            "the precise amount of time the chip takes to complete each "
            "decryption operation across thousands of trials with slightly "
            "different ciphertext inputs. By statistically analyzing the tiny "
            "variations in processing time, the researcher infers individual "
            "bits of the private key without ever directly capturing the key "
            "material or breaking the underlying algorithm mathematically. "
            "Which attack technique does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Side-channel (timing) attack",
                "correct": True,
                "rationale": (
                    "Correct. Inferring secret key material by observing a "
                    "physical characteristic of the cryptographic operation "
                    "itself, such as timing variations, rather than attacking "
                    "the algorithm's mathematics directly, is the definition of "
                    "a side-channel attack."
                ),
            },
            {
                "id": "b",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A downgrade attack forces use of a weaker "
                    "protocol or cipher version; this attack instead passively "
                    "observes timing behavior of the existing, unmodified "
                    "cryptographic operation."
                ),
            },
            {
                "id": "c",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack exploits collision "
                    "probability to find two matching hash outputs; this "
                    "attack instead extracts key bits from processing-time "
                    "variations during decryption, an unrelated technique."
                ),
            },
            {
                "id": "d",
                "text": "Collision attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A collision attack finds two different inputs "
                    "producing an identical hash digest; this attack instead "
                    "recovers private key material through physical timing "
                    "measurements, not hash collisions."
                ),
            },
        ],
        "explanation": (
            "Recovering key material by statistically analyzing physical "
            "timing variations during cryptographic operations, rather than "
            "attacking the algorithm's math directly, is a side-channel "
            "(timing) attack, distinct from downgrade, birthday, or collision "
            "attacks."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "An analyst confirms that a malicious script executed on an "
            "endpoint and now needs to determine exactly which parent process "
            "launched it, in order to identify the initial infection point "
            "(such as a browser, an email client, or a scheduled task). Which "
            "log source will MOST directly answer this investigative question?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "EDR/Sysmon process creation (parent-child process) logs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Process creation telemetry records the parent-"
                    "child relationship between processes, directly showing "
                    "which application launched the malicious script."
                ),
            },
            {
                "id": "b",
                "text": "DNS query logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs show domain name resolution "
                    "attempts, not the parent-child relationship between "
                    "processes on a single endpoint."
                ),
            },
            {
                "id": "c",
                "text": "Firewall allow logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs show network connections "
                    "permitted between hosts and ports; they contain no "
                    "information about which local process spawned another on "
                    "an endpoint."
                ),
            },
            {
                "id": "d",
                "text": "Vulnerability scan reports",
                "correct": False,
                "rationale": (
                    "Incorrect. Scan reports identify weaknesses in installed "
                    "software; they do not capture real-time process execution "
                    "or parent-child relationships."
                ),
            },
        ],
        "explanation": (
            "To determine which parent process launched a malicious script, "
            "EDR/Sysmon process creation logs are the most direct source, "
            "ahead of DNS, firewall, or vulnerability scan data."
        ),
    },
    {
        "id": "nd2c-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "Investigators have already confirmed which host was compromised "
            "and which external IP address it communicated with. They now need "
            "to determine how much data, in total, was transferred to that "
            "external IP address over the course of the intrusion, without "
            "needing to inspect the actual content of the traffic. Which log "
            "source will MOST efficiently answer this question?"
        ),
        "options": [
            {
                "id": "a",
                "text": "NetFlow/flow logs",
                "correct": True,
                "rationale": (
                    "Correct. Flow logs record connection metadata, including "
                    "bytes transferred between hosts, without requiring full "
                    "packet content, making them the efficient source for "
                    "measuring data volume."
                ),
            },
            {
                "id": "b",
                "text": "Full packet capture (PCAP)",
                "correct": False,
                "rationale": (
                    "Incorrect. PCAP does contain enough information to "
                    "calculate volume but also captures full payload content, "
                    "requiring far more storage and processing than necessary "
                    "when only total volume, not content, needs to be "
                    "determined."
                ),
            },
            {
                "id": "c",
                "text": "DHCP logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs record IP address lease "
                    "assignments, not data volumes transferred during a "
                    "specific connection."
                ),
            },
            {
                "id": "d",
                "text": "Antivirus quarantine logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine logs report detected and blocked "
                    "files, not the volume of network traffic transferred to "
                    "an external IP."
                ),
            },
        ],
        "explanation": (
            "To efficiently measure total data volume transferred without "
            "needing payload content, NetFlow/flow logs are the most direct "
            "and efficient source, ahead of full packet capture, DHCP, or "
            "antivirus logs."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A retailer's login page logs show 50,000 login attempts within an "
            "hour, each using a different, unique username/password pair. Two "
            "thousand of the attempts succeed and immediately trigger a spike "
            "in fraudulent gift-card purchases. Investigation confirms every "
            "successful username/password pair matches an entry in a large "
            "breach dataset leaked from an unrelated streaming service two "
            "years earlier. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Credential stuffing",
                "correct": True,
                "rationale": (
                    "Correct. Testing large volumes of unique, previously "
                    "breached username/password pairs from another service "
                    "against a login page, relying on password reuse, is the "
                    "definition of credential stuffing."
                ),
            },
            {
                "id": "b",
                "text": "Password spraying",
                "correct": False,
                "rationale": (
                    "Incorrect. Password spraying uses a single common "
                    "password tried once against many different accounts; "
                    "here each attempt used a unique, previously breached "
                    "username/password pair, not one shared guessed password."
                ),
            },
            {
                "id": "c",
                "text": "Brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Brute force exhaustively tries many possible "
                    "password guesses against typically one target account; "
                    "this attack instead used many known, previously breached, "
                    "unique credential pairs across many accounts, not "
                    "exhaustive guessing."
                ),
            },
            {
                "id": "d",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting targets Kerberos service "
                    "tickets for offline cracking; this incident is a web "
                    "login attack using breached credentials, with no ticket-"
                    "granting service involved."
                ),
            },
        ],
        "explanation": (
            "Testing a large batch of unique, previously breached credential "
            "pairs against a login page, succeeding wherever users reused "
            "their passwords, is credential stuffing, distinct from password "
            "spraying, brute force, or Kerberoasting."
        ),
    },
    {
        "id": "nd2c-036",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "An attacker on the same coffee-shop Wi-Fi captures an "
            "authenticated user's session cookie in transit over an "
            "unencrypted connection to a forum website. For the next several "
            "hours, while the legitimate user continues browsing normally on "
            "their own device, the attacker also loads the same session cookie "
            "into their own browser and freely reads and posts as the victim, "
            "with the victim's original session remaining active and "
            "unaffected throughout. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Session hijacking",
                "correct": True,
                "rationale": (
                    "Correct. Using a captured, still-valid session token to "
                    "ride along on an active session for an extended period, "
                    "in parallel with the legitimate user, is the defining "
                    "trait of session hijacking, distinct from a single one-"
                    "time replay."
                ),
            },
            {
                "id": "b",
                "text": "Replay attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A classic replay attack retransmits a single "
                    "captured authentication event once to gain a new, single "
                    "access instance; here the attacker instead continuously "
                    "reuses the live session cookie in parallel with the still-"
                    "active legitimate session over an extended period, which "
                    "is the more precise session-hijacking classification."
                ),
            },
            {
                "id": "c",
                "text": "Pass-the-hash",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses a captured password hash "
                    "to authenticate to Windows/SMB-based services; this "
                    "attack instead reused a captured web session cookie, not "
                    "a password hash."
                ),
            },
            {
                "id": "d",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing tests breached username/"
                    "password pairs against login forms; no password was ever "
                    "obtained or tested here, only an already-authenticated "
                    "session cookie was captured and reused."
                ),
            },
        ],
        "explanation": (
            "Continuously reusing a captured, still-valid session cookie in "
            "parallel with the legitimate user's own active session, over an "
            "extended period, is session hijacking — a distinct, ongoing "
            "pattern of abuse rather than a single retransmitted event (replay), "
            "a reused password hash (pass-the-hash), or tested breached "
            "credentials (credential stuffing)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A vulnerability assessment finds that 200 workstations are "
            "missing a vendor-released security patch for a critical, actively "
            "exploited vulnerability that has been publicly available for six "
            "weeks. No compensating control, such as a host-based IPS "
            "signature, is currently deployed for this specific flaw. Which "
            "hardening action should be prioritized to remediate this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Patch management (apply the available vendor patch)",
                "correct": True,
                "rationale": (
                    "Correct. Since an official patch already exists and no "
                    "compensating control is currently in place, applying it "
                    "directly is the appropriate and available remediation."
                ),
            },
            {
                "id": "b",
                "text": "Network segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation can reduce exposure but does not "
                    "remove the underlying vulnerability, which already has a "
                    "readily available vendor fix that should be applied "
                    "directly."
                ),
            },
            {
                "id": "c",
                "text": "Host-based IPS / virtual patching",
                "correct": False,
                "rationale": (
                    "Incorrect. Virtual patching is a stopgap used "
                    "specifically when an official patch is not yet "
                    "available; here a vendor patch already exists and should "
                    "be applied rather than relying on a workaround."
                ),
            },
            {
                "id": "d",
                "text": "Application allow listing",
                "correct": False,
                "rationale": (
                    "Incorrect. Allow listing controls which executables may "
                    "run; it does not address a vulnerability within an "
                    "already-approved, legitimately running application or OS "
                    "component."
                ),
            },
        ],
        "explanation": (
            "When an official vendor patch already exists and no compensating "
            "control is in place, applying that patch is the prioritized "
            "hardening action, ahead of segmentation, virtual patching, or "
            "allow listing."
        ),
    },
    {
        "id": "nd2c-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A security assessment of a file server finds that SMBv1 remains "
            "enabled alongside the newer, more secure SMBv3 protocol, even "
            "though every client on the network fully supports SMBv3 and no "
            "legacy device requires the older protocol. SMBv1 contains known, "
            "unpatched design weaknesses that have been exploited in prior "
            "widescale worm outbreaks. Which hardening action should be taken?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable the unnecessary legacy SMBv1 protocol",
                "correct": True,
                "rationale": (
                    "Correct. Since no client requires the outdated, "
                    "inherently weak protocol, disabling it eliminates the "
                    "exposure entirely and reduces the server's attack "
                    "surface."
                ),
            },
            {
                "id": "b",
                "text": "Apply the latest firmware to the file server",
                "correct": False,
                "rationale": (
                    "Incorrect. SMBv1's weaknesses are inherent design flaws "
                    "in the protocol itself, not a specific patchable firmware "
                    "bug; since no client needs the legacy protocol at all, "
                    "disabling it directly addresses the exposure rather than "
                    "patching."
                ),
            },
            {
                "id": "c",
                "text": "Enable full-disk encryption on the file server",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data at rest if "
                    "physical media is stolen; it does nothing to reduce the "
                    "network-facing exposure created by an unnecessary, "
                    "insecure legacy protocol remaining enabled."
                ),
            },
            {
                "id": "d",
                "text": "Deploy network segmentation around the file server",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation could reduce exposure, but since "
                    "no client requires the legacy protocol at all, directly "
                    "disabling the unnecessary, insecure service is the more "
                    "complete and direct remediation."
                ),
            },
        ],
        "explanation": (
            "When an insecure legacy protocol is enabled but no client "
            "actually requires it, disabling that protocol directly is the "
            "appropriate hardening action, more complete than firmware "
            "patching, disk encryption, or segmentation alone."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2c-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "An organization discovers an unpatchable legacy print server "
            "running an operating system that reached end-of-life five years "
            "ago. A business review confirms the print server's only "
            "remaining function was replaced by a cloud print service eighteen "
            "months ago, and no department currently relies on it. Which "
            "mitigation technique is MOST appropriate for this specific "
            "system?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Decommissioning",
                "correct": True,
                "rationale": (
                    "Correct. When a vulnerable, unsupported system no longer "
                    "serves any active business function, permanently "
                    "retiring and securely disposing of it eliminates the risk "
                    "entirely, rather than continuing to manage exposure."
                ),
            },
            {
                "id": "b",
                "text": "Network segmentation/isolation",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation is the appropriate compensating "
                    "control for a vulnerable system that must remain in "
                    "service for a legitimate business need; since this "
                    "server serves no remaining function at all, removing it "
                    "entirely is more appropriate than continuing to isolate "
                    "and maintain it."
                ),
            },
            {
                "id": "c",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. The system is explicitly unpatchable due to "
                    "its end-of-life status; patching is not a viable option "
                    "here."
                ),
            },
            {
                "id": "d",
                "text": "Application allow listing",
                "correct": False,
                "rationale": (
                    "Incorrect. Allow listing controls which executables may "
                    "run on an active, in-use system; it does not address a "
                    "system that has no remaining legitimate business function "
                    "and should instead be retired."
                ),
            },
        ],
        "explanation": (
            "When a vulnerable, unsupported system no longer serves any "
            "active business function, decommissioning it is the most "
            "appropriate mitigation, eliminating the risk entirely rather than "
            "continuing to manage or isolate it."
        ),
    },
    {
        "id": "nd2c-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A sales employee's laptop, configured with full-disk encryption "
            "enforced by policy, is stolen from a parked car. The device was "
            "locked and powered off at the time of theft. The security team "
            "classifies this as a lost-asset incident requiring no mandatory "
            "customer breach notification, in contrast to a similar theft the "
            "previous year involving an unencrypted laptop that did trigger "
            "notification requirements. Which mitigation technique made the "
            "critical difference in this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Encryption (full-disk encryption)",
                "correct": True,
                "rationale": (
                    "Correct. Rendering data on the device unreadable without "
                    "the encryption key ensures that physical theft of a "
                    "powered-off, locked device does not result in actual data "
                    "disclosure, which is why notification requirements were "
                    "not triggered."
                ),
            },
            {
                "id": "b",
                "text": "Network segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation restricts network-level "
                    "reachability between systems; it has no bearing on data "
                    "confidentiality of a physically stolen, offline device."
                ),
            },
            {
                "id": "c",
                "text": "Least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege restricts what an "
                    "authenticated account can access on running systems; it "
                    "does nothing to protect data stored on a stolen device's "
                    "disk itself."
                ),
            },
            {
                "id": "d",
                "text": "Isolation",
                "correct": False,
                "rationale": (
                    "Incorrect. Isolation refers to removing a compromised "
                    "host's network connectivity; it is not the control that "
                    "determines whether data on a stolen, powered-off device "
                    "remains protected."
                ),
            },
        ],
        "explanation": (
            "Full-disk encryption is the mitigation that determines whether "
            "data on a physically stolen, powered-off device remains "
            "protected, distinct from segmentation, least privilege, or "
            "isolation, none of which apply to an offline device's stored "
            "data."
        ),
    },
]
