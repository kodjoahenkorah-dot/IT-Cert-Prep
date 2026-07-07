"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch B.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 2 in
``_topic_labels.json``. Brand-new scenarios distinct from d2a.py.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Threat actors (2.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "Forensic investigators recover an internal invoice, addressed to a "
            "rival company's marketing director, that references \"Phase 2 payment "
            "for competitor intelligence gathering\" inside the home directory of "
            "the account used to spear-phish a product manager and exfiltrate an "
            "unreleased product roadmap. The intrusion used only commodity "
            "phishing kits purchased from an underground forum, and the attacker "
            "disappeared from the network within 48 hours of completing the theft. "
            "Which threat actor MOST likely carried out this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hacker for hire (mercenary)",
                "correct": True,
                "rationale": (
                    "Correct. Evidence of being paid by a specific client (the "
                    "invoice) for a narrow, defined objective, and quickly "
                    "departing once the paid work is done, is the signature of a "
                    "hacker-for-hire, who may use inexpensive commodity tools "
                    "since completing the job matters more than sophistication."
                ),
            },
            {
                "id": "b",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. Nation-states pursue broad strategic intelligence "
                    "goals over long timeframes using custom tooling; a single "
                    "paid deliverable using off-the-shelf phishing kits and a "
                    "rapid exit points to a for-hire operator, not state "
                    "sponsorship."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological motive or public "
                    "messaging; the invoice reveals a purely commercial, paid "
                    "transaction for competitive intelligence."
                ),
            },
            {
                "id": "d",
                "text": "Insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. The attack originated externally via "
                    "spear-phishing against a product manager rather than being "
                    "carried out by a trusted internal employee with existing "
                    "legitimate access."
                ),
            },
        ],
        "explanation": (
            "A paid, client-directed, narrowly-scoped operation completed quickly "
            "with commodity tools is the hallmark of a hacker-for-hire (mercenary) "
            "threat actor, distinguishing it from a nation-state's patience/custom "
            "tooling, a hacktivist's ideological messaging, or an insider's "
            "pre-existing legitimate access."
        ),
    },
    {
        "id": "nd2b-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A sales team lead, frustrated with the multi-week approval process "
            "for the corporate file-sharing platform, begins uploading customer "
            "contracts and pricing sheets to a personal cloud storage account so "
            "the team can collaborate faster ahead of a deadline. No data is sold, "
            "altered, or shared outside the team, and the lead openly mentions the "
            "workaround in a team meeting. Which term BEST classifies this "
            "activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Shadow IT",
                "correct": True,
                "rationale": (
                    "Correct. Using unsanctioned but not maliciously intended "
                    "technology to bypass slow official processes, done openly "
                    "rather than covertly, is the definition of shadow IT."
                ),
            },
            {
                "id": "b",
                "text": "Insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. Insider threat implies malicious intent or "
                    "negligent harm hidden from the organization; here the lead "
                    "is transparent about the workaround and has no intent to "
                    "harm the company."
                ),
            },
            {
                "id": "c",
                "text": "Data exfiltration by a competitor",
                "correct": False,
                "rationale": (
                    "Incorrect. There's no evidence a competitor or any external "
                    "party directed or received this data; it is an internal "
                    "convenience workaround."
                ),
            },
            {
                "id": "d",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No email account was compromised or spoofed; "
                    "this scenario involves cloud storage usage, not "
                    "email-based fraud."
                ),
            },
        ],
        "explanation": (
            "Unsanctioned but transparent, non-malicious use of unauthorized "
            "technology to work around official processes is shadow IT — distinct "
            "from insider threat (which implies harmful intent), external data "
            "theft, or BEC."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-003",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A photo-sharing feature on an internal HR portal allows employees to "
            "upload profile pictures. A researcher uploads a JPEG file containing "
            "an embedded script within its EXIF metadata; when the server's "
            "thumbnail-generation library parses the file, the embedded script "
            "executes on the server and opens a reverse shell. Which threat vector "
            "was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Image-based",
                "correct": True,
                "rationale": (
                    "Correct. The malicious payload was embedded within an image "
                    "file's metadata and triggered by the server's own "
                    "image-processing routine — the defining trait of an "
                    "image-based attack vector."
                ),
            },
            {
                "id": "b",
                "text": "Message-based",
                "correct": False,
                "rationale": (
                    "Incorrect. No email, SMS, or chat message delivered or "
                    "triggered the payload; the vector was a file upload "
                    "processed by server-side image-handling code."
                ),
            },
            {
                "id": "c",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media (USB, external drive) was "
                    "involved; the file was uploaded through a web-based portal."
                ),
            },
            {
                "id": "d",
                "text": "Supply chain",
                "correct": False,
                "rationale": (
                    "Incorrect. No trusted vendor's software or update pipeline "
                    "was compromised; this is a direct exploitation of the "
                    "portal's own image-processing feature."
                ),
            },
        ],
        "explanation": (
            "A malicious payload hidden inside an image file's metadata and "
            "triggered by the server's own image-parsing logic is the image-based "
            "threat vector."
        ),
    },
    {
        "id": "nd2b-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A vulnerability assessment finds thousands of internet-facing "
            "security cameras belonging to the organization's retail locations "
            "still using the vendor's factory-set \"admin/admin\" login, published "
            "in the publicly available installation manual. An attacker used this "
            "information to take control of the camera feeds without exploiting "
            "any software flaw. Which threat vector was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Default credentials",
                "correct": True,
                "rationale": (
                    "Correct. Gaining access using unchanged, publicly "
                    "documented factory credentials, with no software "
                    "vulnerability exploited, is the definition of the "
                    "default-credentials threat vector."
                ),
            },
            {
                "id": "b",
                "text": "Supply chain",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing was tampered with before delivery by "
                    "the vendor; the devices function as designed, they were "
                    "simply never reconfigured with unique credentials after "
                    "installation."
                ),
            },
            {
                "id": "c",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media was used to deliver an "
                    "infection; access was gained purely through unchanged "
                    "login credentials over the network."
                ),
            },
            {
                "id": "d",
                "text": "Unsecure network",
                "correct": False,
                "rationale": (
                    "Incorrect. The compromise resulted from the credentials "
                    "themselves being left at factory defaults, not from a "
                    "weakness in the network transport (such as unencrypted "
                    "Wi-Fi) carrying the login."
                ),
            },
        ],
        "explanation": (
            "Devices reachable using unchanged, publicly known factory-default "
            "logins represent the default-credentials threat vector, distinct "
            "from supply-chain tampering or transport-level network weaknesses."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "Several engineers at an aerospace firm report malware infections "
            "shortly after visiting a niche online forum for aviation parts "
            "suppliers that they all frequently use. Investigation reveals the "
            "forum's third-party ad server was compromised to serve a malicious "
            "exploit kit, but only to visitors whose IP addresses resolve to the "
            "aerospace firm's corporate range; all other visitors receive normal "
            "ads. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Watering hole attack",
                "correct": True,
                "rationale": (
                    "Correct. Compromising a legitimate third-party site "
                    "frequented by a specific target group, and selectively "
                    "serving malware only to that group's IP range, is the "
                    "defining characteristic of a watering hole attack."
                ),
            },
            {
                "id": "b",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No email account or messaging was involved at "
                    "any point; the compromise occurred entirely through a "
                    "website the victims voluntarily visited."
                ),
            },
            {
                "id": "c",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. The forum is the engineers' legitimate, "
                    "correctly-spelled destination site; no lookalike or "
                    "misspelled domain was registered to lure them."
                ),
            },
            {
                "id": "d",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. No phone call or voice communication was used; "
                    "the infection was delivered through a compromised website "
                    "visit."
                ),
            },
        ],
        "explanation": (
            "Selectively compromising a trusted third-party site to target a "
            "specific victim population by IP range is a watering hole attack, "
            "not phishing, typosquatting, or vishing."
        ),
    },
    {
        "id": "nd2b-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "A financial controller receives an urgent wire-transfer request that "
            "email header analysis confirms was genuinely sent from the CFO's "
            "actual corporate mailbox, using the CFO's real authenticated SMTP "
            "session, rather than a spoofed or lookalike address. The CFO's "
            "credentials had been stolen the previous week via a separate "
            "phishing campaign. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Business email compromise (BEC)",
                "correct": True,
                "rationale": (
                    "Correct. The message originated from the CFO's genuinely "
                    "compromised, authenticated mailbox rather than a forged "
                    "sender address, which is the defining trait of BEC — the "
                    "account itself, not just its identity, was taken over."
                ),
            },
            {
                "id": "b",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling describes a phishing attack that "
                    "targets a high-profile individual as the victim; here the "
                    "CFO's account is the compromised launch point used to "
                    "target the controller, not the ultimate target being "
                    "deceived."
                ),
            },
            {
                "id": "c",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. No lookalike domain was registered or used; "
                    "the email came from the CFO's real, correctly-spelled "
                    "corporate address."
                ),
            },
            {
                "id": "d",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting involves fabricating a false "
                    "scenario or identity to build trust; here the attacker "
                    "didn't need to fabricate an identity because they were "
                    "using the CFO's actual, legitimate, compromised mailbox."
                ),
            },
        ],
        "explanation": (
            "Because the email genuinely originated from the CFO's own "
            "compromised account rather than a forged or fabricated identity, "
            "this is business email compromise, not whaling (which describes "
            "targeting an executive), typosquatting, or pretexting."
        ),
    },
    {
        "id": "nd2b-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "Review the phishing text message sent to employees:\n\n"
            "\"IT Alert: You are one of only 5 employees selected for a free "
            "security-key upgrade. Offer expires in 45 minutes — tap the link and "
            "enter your current password to claim your device before it's "
            "reassigned to someone else.\"\n\n"
            "Which TWO social engineering principles are being leveraged in this "
            "message? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Scarcity",
                "correct": True,
                "rationale": (
                    "Correct. Framing the offer as available to only 5 "
                    "employees and subject to reassignment plays on the fear "
                    "of missing out on a limited resource, which is scarcity."
                ),
            },
            {
                "id": "b",
                "text": "Urgency",
                "correct": True,
                "rationale": (
                    "Correct. The 45-minute expiration window pressures the "
                    "recipient to act immediately without pausing to verify "
                    "the request through normal channels."
                ),
            },
            {
                "id": "c",
                "text": "Authority",
                "correct": False,
                "rationale": (
                    "Incorrect. While the message claims to be from \"IT,\" it "
                    "does not invoke a position of organizational power or "
                    "command compliance the way an executive or "
                    "law-enforcement impersonation would; the primary pressure "
                    "levers here are the limited offer and countdown, not rank."
                ),
            },
            {
                "id": "d",
                "text": "Social proof (consensus)",
                "correct": False,
                "rationale": (
                    "Incorrect. The message doesn't reference other employees "
                    "having already claimed similar upgrades or endorsed the "
                    "offer; it isolates the recipient as one of a small, "
                    "exclusive group rather than pointing to peer behavior."
                ),
            },
            {
                "id": "e",
                "text": "Likability",
                "correct": False,
                "rationale": (
                    "Incorrect. The tone is transactional and impersonal, "
                    "offering a prize rather than attempting to build rapport "
                    "or friendliness with the recipient."
                ),
            },
        ],
        "explanation": (
            "The \"only 5 selected\" framing is scarcity, and the 45-minute "
            "countdown is urgency; the message lacks the authority, consensus, or "
            "likability cues that would justify those other options."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "An online retailer's cart-quantity field stores the requested "
            "quantity in a 16-bit signed integer, which has a maximum value of "
            "32,767. A tester sets the quantity to 32,768 and the application "
            "calculates a negative total price, allowing the tester to receive a "
            "credit rather than a charge. Which vulnerability is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integer overflow",
                "correct": True,
                "rationale": (
                    "Correct. A numeric value exceeding the maximum size its "
                    "data type can hold, wrapping around to a negative or "
                    "unexpected value, is the definition of an integer "
                    "overflow."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No oversized string or input overran a "
                    "fixed-size memory buffer; the flaw is purely arithmetic, "
                    "caused by a numeric value exceeding its storage type's "
                    "range."
                ),
            },
            {
                "id": "c",
                "text": "Race condition",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no timing dependency between a check "
                    "and a subsequent action; the flaw is deterministic and "
                    "occurs on a single, straightforward calculation."
                ),
            },
            {
                "id": "d",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. No serialized object was reconstructed from "
                    "untrusted data; the issue is a numeric type boundary "
                    "being exceeded during a price calculation."
                ),
            },
        ],
        "explanation": (
            "A value exceeding its data type's maximum and wrapping to an "
            "unexpected (here, negative) result is the signature of an integer "
            "overflow vulnerability."
        ),
    },
    {
        "id": "nd2b-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "An application server has no reported attack traffic, yet its "
            "available memory steadily declines over 72 hours of normal "
            "operation until the service becomes unresponsive and must be "
            "restarted. Code review reveals that a database connection object is "
            "allocated for every request but is never released back to the pool "
            "after the request completes. Which vulnerability does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memory leak (resource exhaustion)",
                "correct": True,
                "rationale": (
                    "Correct. Failing to release allocated resources after use "
                    "causes them to accumulate over time until the system runs "
                    "out of available memory — the definition of a memory leak "
                    "leading to resource exhaustion, requiring no attacker "
                    "interaction at all."
                ),
            },
            {
                "id": "b",
                "text": "Race condition",
                "correct": False,
                "rationale": (
                    "Incorrect. A race condition depends on the "
                    "interleaving/timing of concurrent operations; this issue "
                    "is a steady, predictable resource accumulation over time "
                    "from a coding defect, not a timing collision."
                ),
            },
            {
                "id": "c",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. Buffer overflows involve oversized input "
                    "overwriting adjacent memory; this scenario describes "
                    "gradual resource accumulation from unreleased handles, "
                    "not memory corruption from oversized data."
                ),
            },
            {
                "id": "d",
                "text": "Denial-of-service (DDoS) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No external attack traffic or attacker action "
                    "is described at all; the outage is self-inflicted by a "
                    "coding defect under entirely normal usage, not caused by "
                    "a deliberate distributed attack."
                ),
            },
        ],
        "explanation": (
            "A gradual decline in available resources due to allocations that "
            "are never released, eventually causing unresponsiveness under normal "
            "use, is a memory leak/resource-exhaustion vulnerability, not an "
            "active attack or timing-dependent flaw."
        ),
    },
    {
        "id": "nd2b-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A Java-based application stores session state in a serialized "
            "object placed inside a cookie. A researcher crafts a modified "
            "serialized object containing a gadget chain that, when the server "
            "deserializes the cookie on the next request, executes arbitrary "
            "commands on the host. Which vulnerability is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insecure deserialization",
                "correct": True,
                "rationale": (
                    "Correct. Reconstructing an object from attacker-"
                    "controlled serialized data without validation, allowing a "
                    "crafted gadget chain to trigger arbitrary code execution, "
                    "is the definition of insecure deserialization."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF forces an authenticated victim's browser "
                    "to submit an unwanted request; it does not involve "
                    "crafting a malicious serialized object that executes code "
                    "when reconstructed server-side."
                ),
            },
            {
                "id": "c",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No fixed-size memory buffer was overrun with "
                    "oversized input; the exploit relies on the server's "
                    "object-reconstruction logic processing a malicious object "
                    "structure, not on overflowing a buffer."
                ),
            },
            {
                "id": "d",
                "text": "XML external entity (XXE) injection",
                "correct": False,
                "rationale": (
                    "Incorrect. XXE abuses an XML parser's handling of "
                    "external entity references; this scenario describes "
                    "exploitation of a serialized object deserialization "
                    "routine, not XML parsing."
                ),
            },
        ],
        "explanation": (
            "Executing arbitrary code by supplying a maliciously crafted "
            "serialized object that the server reconstructs without validation "
            "is insecure deserialization."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A document-management web application accepts XML file uploads for "
            "metadata import. A tester uploads an XML file containing a DOCTYPE "
            "declaration that defines an external entity referencing "
            "\"file:///etc/passwd,\" and the parsed response includes the "
            "contents of that file. Which vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "XML external entity (XXE) injection",
                "correct": True,
                "rationale": (
                    "Correct. Defining and referencing an external entity "
                    "within an XML document to force the parser to read and "
                    "return an arbitrary local file is the definition of an "
                    "XXE injection."
                ),
            },
            {
                "id": "b",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks a server into making a network "
                    "request to another host on the attacker's behalf; here "
                    "the parser read a local file directly, driven by XML "
                    "entity resolution, not a server-issued network request."
                ),
            },
            {
                "id": "c",
                "text": "Directory traversal",
                "correct": False,
                "rationale": (
                    "Incorrect. Directory traversal manipulates a file path "
                    "parameter (such as \"../../\") passed directly to a "
                    "file-access function; this exploit instead abuses XML "
                    "DOCTYPE/entity parsing to reach the file, a distinctly "
                    "different mechanism."
                ),
            },
            {
                "id": "d",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. Deserialization flaws involve reconstructing "
                    "objects from serialized data structures; this attack "
                    "instead abuses standard XML external entity resolution "
                    "during parsing."
                ),
            },
        ],
        "explanation": (
            "Abusing a DOCTYPE-defined external entity to force an XML parser to "
            "disclose local file contents is XXE injection, distinct from SSRF "
            "(network requests), directory traversal (path manipulation), or "
            "deserialization."
        ),
    },
    {
        "id": "nd2b-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A web application access log shows the following request against a "
            "product search field:\n\n"
            "GET /search?q=widget' UNION SELECT username,password FROM "
            "accounts-- HTTP/1.1\n\n"
            "Shortly afterward, the response page displays a list of usernames "
            "and password hashes. Which vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SQL injection",
                "correct": True,
                "rationale": (
                    "Correct. Appending a UNION SELECT clause to an input "
                    "parameter to merge results from an unrelated database "
                    "table into the application's output is a classic SQL "
                    "injection technique."
                ),
            },
            {
                "id": "b",
                "text": "Command injection",
                "correct": False,
                "rationale": (
                    "Incorrect. Command injection passes attacker input to an "
                    "operating system shell for execution; the payload here "
                    "targets the backend database's SQL syntax, not an OS "
                    "command interpreter."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site scripting",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS injects client-side script that executes "
                    "in a victim's browser; this payload manipulates a "
                    "server-side database query and returns data directly, "
                    "with no script execution involved."
                ),
            },
            {
                "id": "d",
                "text": "LDAP injection",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP injection manipulates directory-service "
                    "queries using LDAP filter syntax; the payload here uses "
                    "SQL-specific syntax (UNION SELECT) against a relational "
                    "database, not an LDAP query."
                ),
            },
        ],
        "explanation": (
            "A UNION SELECT payload appended to a search parameter that returns "
            "unrelated database table contents is the signature of SQL "
            "injection."
        ),
    },
    {
        "id": "nd2b-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A file-download feature accepts a filename parameter. A tester "
            "submits the request \"GET /download?file=../../../../etc/shadow\" "
            "and the server returns the contents of the system's shadow "
            "password file instead of a document from the intended download "
            "directory. Which vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Directory traversal (path traversal)",
                "correct": True,
                "rationale": (
                    "Correct. Using relative path sequences (\"../\") within a "
                    "file-path parameter to escape the intended directory and "
                    "access arbitrary files elsewhere on the filesystem is the "
                    "definition of directory traversal."
                ),
            },
            {
                "id": "b",
                "text": "Local file inclusion via insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. No serialized object was submitted or "
                    "reconstructed; the exploit is a raw file-path parameter "
                    "manipulated with relative path sequences, not a "
                    "deserialization flaw."
                ),
            },
            {
                "id": "c",
                "text": "Server-side request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF causes a server to issue a network "
                    "request to another host; this exploit retrieves a local "
                    "file directly via filesystem path manipulation, involving "
                    "no outbound network request."
                ),
            },
            {
                "id": "d",
                "text": "Insecure direct object reference",
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR involves manipulating a reference (such "
                    "as an ID) to access another user's application-level "
                    "object; here the manipulation targets raw filesystem path "
                    "traversal sequences to escape the intended directory "
                    "entirely, reaching arbitrary system files rather than "
                    "another user's record."
                ),
            },
        ],
        "explanation": (
            "Manipulating a file path with \"../\" sequences to escape the "
            "intended directory and read arbitrary files, such as the shadow "
            "file, is directory/path traversal."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A security researcher sitting in a hotel lobby uses a laptop with a "
            "Bluetooth adapter to connect to a nearby smartphone's OBEX "
            "file-transfer service, which is not properly access-controlled, and "
            "silently downloads the device's contact list and calendar entries "
            "without the phone user ever accepting a pairing request. Which "
            "attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bluesnarfing",
                "correct": True,
                "rationale": (
                    "Correct. Unauthorized access to and extraction of data "
                    "(contacts, calendar) from a device over Bluetooth, "
                    "without the owner's knowledge or a completed pairing, is "
                    "the definition of bluesnarfing."
                ),
            },
            {
                "id": "b",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking is sending unsolicited messages or "
                    "data to a nearby device; it does not involve extracting "
                    "data from the victim's device, which is what occurred "
                    "here."
                ),
            },
            {
                "id": "c",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping involves porting a victim's "
                    "phone number to an attacker-controlled SIM through the "
                    "carrier; this attack occurred entirely over a local "
                    "Bluetooth connection with no carrier involvement."
                ),
            },
            {
                "id": "d",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreaking removes OS-level restrictions on "
                    "a device the attacker or user controls directly; this "
                    "scenario describes remote extraction of data from "
                    "someone else's device over Bluetooth, not modification "
                    "of the device's own OS."
                ),
            },
        ],
        "explanation": (
            "Silently extracting data such as contacts and calendar entries "
            "from a nearby device over an improperly secured Bluetooth service "
            "is bluesnarfing, distinct from bluejacking (sending unsolicited "
            "data) or carrier-based SIM swapping."
        ),
    },
    {
        "id": "nd2b-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A flashlight application downloaded from the official app store "
            "functions normally but was granted, and actively uses, permissions "
            "to read SMS messages, contacts, and precise location — none of "
            "which are required for controlling a camera flash. Forensic "
            "analysis later shows the app forwarded intercepted SMS one-time "
            "passcodes to an external server. Which mobile vulnerability MOST "
            "directly enabled this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Excessive/overly permissive application permissions",
                "correct": True,
                "rationale": (
                    "Correct. Granting an app access far beyond what its "
                    "stated function requires, and the app actively "
                    "exploiting that unnecessary access to intercept "
                    "sensitive SMS content, is the defining mobile "
                    "vulnerability here."
                ),
            },
            {
                "id": "b",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no indication the device's OS-level "
                    "restrictions were removed; the app operated within the "
                    "normal permission model, simply having been granted more "
                    "access than it needed."
                ),
            },
            {
                "id": "c",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping involves porting the victim's "
                    "number to an attacker's SIM via the carrier; here the "
                    "legitimate device retained its number, and interception "
                    "occurred locally through the app's own excessive "
                    "permissions."
                ),
            },
            {
                "id": "d",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. No Bluetooth connection or proximity-based "
                    "data extraction is involved; the app obtained data "
                    "directly through permissions granted during normal "
                    "installation."
                ),
            },
        ],
        "explanation": (
            "An app functioning without OS restrictions removed, but granted "
            "and abusing permissions well beyond its actual purpose, illustrates "
            "the mobile vulnerability of excessive/overly permissive app "
            "permissions."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "An internal audit of a private cloud environment discovers 60 "
            "virtual machines that no team claims ownership of, several still "
            "running end-of-life operating systems with default administrator "
            "passwords, none of which appear in the current asset inventory or "
            "patch management system. Which vulnerability does this environment "
            "MOST clearly exhibit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM sprawl",
                "correct": True,
                "rationale": (
                    "Correct. An unmanaged, undocumented proliferation of "
                    "forgotten virtual machines lacking ownership, patching, "
                    "and inventory tracking is the definition of VM sprawl."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. VM escape is an active exploit breaching "
                    "hypervisor isolation between running VMs; this scenario "
                    "describes an inventory and governance failure over time, "
                    "not an isolation-breaking attack."
                ),
            },
            {
                "id": "c",
                "text": "Resource reuse (data remnants)",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse concerns residual data left in "
                    "storage reassigned to a new VM after deallocation; this "
                    "scenario describes forgotten, still-running VMs, not "
                    "leftover data from decommissioned storage."
                ),
            },
            {
                "id": "d",
                "text": "Hyperjacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Hyperjacking involves installing a rogue "
                    "hypervisor beneath the legitimate one; there is no "
                    "evidence of a compromised or rogue hypervisor here, only "
                    "unmanaged VM proliferation."
                ),
            },
        ],
        "explanation": (
            "A large number of unowned, unpatched, untracked VMs accumulating "
            "over time without governance is VM sprawl, distinct from an active "
            "hypervisor exploit, storage data remanence, or a rogue hypervisor."
        ),
    },
    {
        "id": "nd2b-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "Forensic analysis of a physical host reveals a malicious Type 1 "
            "hypervisor was installed beneath the organization's existing, still-"
            "functioning production hypervisor, giving the attacker full control "
            "over every guest VM's memory and CPU state while remaining "
            "completely invisible to monitoring tools running inside the guest "
            "operating systems. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hyperjacking (rogue/malicious hypervisor)",
                "correct": True,
                "rationale": (
                    "Correct. Installing an unauthorized hypervisor beneath "
                    "the legitimate one to gain covert, complete control over "
                    "all guest VMs, undetectable from within the guests, is "
                    "the definition of hyperjacking."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. VM escape describes an attacker breaking out "
                    "from within a single guest VM to reach the host or other "
                    "VMs; here the attacker instead inserted an entirely new, "
                    "lower-level hypervisor beneath the existing one, a "
                    "distinct and more severe attack."
                ),
            },
            {
                "id": "c",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. VM sprawl is an unmanaged accumulation of "
                    "forgotten VMs over time due to poor governance; it does "
                    "not involve installing a covert rogue hypervisor to "
                    "actively control running VMs."
                ),
            },
            {
                "id": "d",
                "text": "Resource reuse (data remnants)",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse concerns leftover data in "
                    "storage reassigned between VMs; it has no relation to a "
                    "rogue hypervisor being installed beneath a legitimate "
                    "one."
                ),
            },
        ],
        "explanation": (
            "Installing a covert hypervisor beneath the legitimate one to gain "
            "total, undetectable control over all guest VMs is hyperjacking, "
            "distinguished from VM escape (breakout from a single guest) and VM "
            "sprawl (governance failure)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A vulnerability scan flags a critical unauthenticated remote code "
            "execution flaw in an internal application server. The security team "
            "notes that a web application firewall in front of the server "
            "currently blocks the known exploit pattern, so no compromise has "
            "occurred. How should the underlying scan finding itself be "
            "classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "True positive",
                "correct": True,
                "rationale": (
                    "Correct. The vulnerability genuinely exists in the "
                    "underlying software regardless of whether a compensating "
                    "control like a WAF currently blocks exploitation; the "
                    "scan accurately identified a real flaw, making this a "
                    "true positive even though risk is currently mitigated."
                ),
            },
            {
                "id": "b",
                "text": "False positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A false positive means the flagged condition "
                    "doesn't actually exist; here the vulnerability is real "
                    "and confirmed present in the software itself, it is "
                    "simply not currently being exploited due to an external "
                    "mitigating control."
                ),
            },
            {
                "id": "c",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative would mean a real "
                    "vulnerability went undetected and unreported; here the "
                    "scanner correctly detected and reported the "
                    "vulnerability."
                ),
            },
            {
                "id": "d",
                "text": "Indicator of compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. An IoC is forensic evidence that an actual "
                    "breach occurred; this question concerns classifying an "
                    "unexploited scan finding, not evidence of a completed "
                    "compromise."
                ),
            },
        ],
        "explanation": (
            "A scan finding is classified based on whether the underlying "
            "vulnerability actually exists, not on whether a compensating "
            "control is currently preventing exploitation — making this a true "
            "positive despite the WAF's mitigation."
        ),
    },
    {
        "id": "nd2b-019",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A network scan of a Windows file server without any login "
            "credentials reports zero vulnerabilities. Later that same day, an "
            "authenticated (credentialed) scan of the identical host using local "
            "administrator credentials reports 14 missing critical patches, "
            "several rated as remotely exploitable. Which statement BEST "
            "explains this discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The unauthenticated scan lacked the local visibility "
                    "needed to detect the missing patches, producing a false "
                    "negative"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Unauthenticated/network-only scans have limited "
                    "visibility into installed software and patch levels; the "
                    "unauthenticated scan's failure to detect real, present "
                    "vulnerabilities is a false negative for that scan type."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The credentialed scan produced 14 false positives because "
                    "local scans are inherently less reliable than network-"
                    "based scans"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards — credentialed scans "
                    "generally provide deeper, more accurate visibility than "
                    "unauthenticated network scans, not less reliable results."
                ),
            },
            {
                "id": "c",
                "text": "The server was fully patched between the two scans that day",
                "correct": False,
                "rationale": (
                    "Incorrect. Both scans ran the same day; patch timing "
                    "does not plausibly explain a same-day discrepancy of "
                    "this scale between the two scan results."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The unauthenticated scanner could not reach the host at "
                    "all due to a firewall rule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The unauthenticated scanner did reach the "
                    "host and returned a result of zero vulnerabilities, not "
                    "a connectivity failure or an empty/error result."
                ),
            },
        ],
        "explanation": (
            "Unauthenticated/network-only scans have limited visibility and can "
            "produce false negatives for vulnerabilities, such as missing "
            "patches, that only credentialed, authenticated scans can detect via "
            "local system access."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A SOC analyst reviewing proxy logs notices that a single "
            "workstation makes an outbound HTTPS connection to the same "
            "external IP address every 60 seconds, 24 hours a day including "
            "overnight when no user is logged in, and each connection transfers "
            "almost exactly 200 bytes regardless of time of day. Which indicator "
            "does this MOST closely represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Command-and-control (C2) beaconing",
                "correct": True,
                "rationale": (
                    "Correct. Highly regular, fixed-interval outbound "
                    "connections with consistent, small payload sizes "
                    "occurring even when no user is present is the classic "
                    "behavioral signature of malware beaconing to a C2 server "
                    "for instructions."
                ),
            },
            {
                "id": "b",
                "text": "Data exfiltration",
                "correct": False,
                "rationale": (
                    "Incorrect. Exfiltration is typically characterized by "
                    "unusually large outbound transfer volumes; this traffic "
                    "pattern involves small, consistent packet sizes at "
                    "regular intervals, which is check-in behavior rather "
                    "than bulk data theft."
                ),
            },
            {
                "id": "c",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel refers to successful "
                    "authentications from geographically distant locations in "
                    "an implausible timeframe; this scenario describes "
                    "outbound network connection patterns from a single host, "
                    "not authentication events."
                ),
            },
            {
                "id": "d",
                "text": "On-path (man-in-the-middle) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An on-path attack involves an adversary "
                    "intercepting traffic between two legitimate parties; "
                    "this scenario shows a host initiating its own regular "
                    "outbound connections, not traffic being intercepted "
                    "between two other parties."
                ),
            },
        ],
        "explanation": (
            "Fixed-interval, consistently small outbound connections occurring "
            "around the clock — even without a logged-in user — is the "
            "signature of C2 beaconing, not exfiltration, impossible travel, or "
            "interception."
        ),
    },
    {
        "id": "nd2b-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A domain controller's security log shows a standard user account "
            "being added to the Domain Admins group at 3:14 a.m. The account "
            "performing the addition is a service account that, according to "
            "its documented purpose, only ever runs an unattended nightly backup "
            "job and has never previously modified group memberships. Which "
            "indicator does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unusual/unauthorized privilege escalation",
                "correct": True,
                "rationale": (
                    "Correct. A service account acting far outside its "
                    "documented, narrow function to grant elevated group "
                    "membership at an unusual hour is a strong indicator that "
                    "the account has been compromised and used for privilege "
                    "escalation."
                ),
            },
            {
                "id": "b",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel concerns geographically "
                    "implausible successful logins; this scenario concerns an "
                    "account performing an action (group membership change) "
                    "outside its normal scope, not a login-location anomaly."
                ),
            },
            {
                "id": "c",
                "text": "Resource consumption anomaly",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource consumption anomalies involve "
                    "abnormal CPU, memory, or bandwidth usage; this indicator "
                    "is about an account performing an unauthorized "
                    "administrative action, not a performance metric."
                ),
            },
            {
                "id": "d",
                "text": "Concurrent session anomaly",
                "correct": False,
                "rationale": (
                    "Incorrect. A concurrent session anomaly refers to the "
                    "same account being logged in from multiple "
                    "locations/sessions simultaneously; this scenario "
                    "describes an out-of-scope privilege change, not "
                    "simultaneous sessions."
                ),
            },
        ],
        "explanation": (
            "An account acting far outside its documented, narrow purpose to "
            "escalate another account's privileges is a strong indicator of "
            "account compromise and privilege escalation, distinct from "
            "impossible travel, resource anomalies, or concurrent-session "
            "indicators."
        ),
    },
    {
        "id": "nd2b-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A departing employee's laptop is reviewed after their two-weeks' "
            "notice. Logs show a 25 GB outbound transfer to a personal cloud-"
            "storage domain at 11:58 p.m. on the employee's last Friday in the "
            "office, and the DNS query for that transfer was resolved using a "
            "public DNS-over-HTTPS (DoH) resolver the host had never used in the "
            "prior six months of logs, bypassing the organization's monitored "
            "internal DNS server entirely. Which TWO facts are the strongest "
            "indicators of intentional data exfiltration? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The unusually large (25 GB) outbound transfer to a "
                    "personal cloud-storage destination"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A large volume of data leaving to a personal, "
                    "non-corporate cloud destination is a strong indicator of "
                    "data exfiltration, especially from a departing employee."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The use of a previously never-seen DoH resolver that "
                    "bypassed normal, monitored internal DNS logging"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Switching to an unfamiliar external DNS-over-"
                    "HTTPS resolver specifically evades the organization's "
                    "DNS-based monitoring and logging, indicating a "
                    "deliberate attempt to conceal the destination and evade "
                    "detection."
                ),
            },
            {
                "id": "c",
                "text": "The transfer occurred late at night on a Friday",
                "correct": False,
                "rationale": (
                    "Incorrect. Time of day/week alone is a weak, easily "
                    "explained indicator (an employee could simply be "
                    "working late); it is not by itself a reliable sign of "
                    "malicious intent."
                ),
            },
            {
                "id": "d",
                "text": "The connection used HTTPS encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. The vast majority of legitimate business and "
                    "personal traffic today is encrypted with HTTPS; "
                    "encryption alone is completely routine and not "
                    "indicative of exfiltration."
                ),
            },
        ],
        "explanation": (
            "The unusual transfer volume to personal cloud storage and the "
            "deliberate switch to an unmonitored DNS resolver are the strongest, "
            "most specific indicators of intentional exfiltration; the time of "
            "day and the mere use of HTTPS are both too common in legitimate "
            "activity to be meaningful on their own."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Endpoint forensics on a compromised workstation reveal a hidden "
            "background process that captures every keystroke typed by the user "
            "into a local encrypted log file, which is then emailed to an "
            "external address once every 24 hours. The process does not attempt "
            "to spread to other hosts or destroy any data. Which malware type is "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Keylogger (spyware)",
                "correct": True,
                "rationale": (
                    "Correct. Covertly capturing and exfiltrating a user's "
                    "keystrokes for surveillance/data-theft purposes, with no "
                    "self-propagation or destructive payload, is the "
                    "definition of a keylogger/spyware."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. Worms self-propagate across a network by "
                    "exploiting vulnerabilities; this malware does not spread "
                    "to other hosts at all, it only exfiltrates data from the "
                    "single infected host."
                ),
            },
            {
                "id": "c",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts files and demands "
                    "payment for their release; this malware does not "
                    "encrypt or hold any files hostage, it silently captures "
                    "keystrokes."
                ),
            },
            {
                "id": "d",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is dormant code that triggers a "
                    "destructive action on a specific condition; this malware "
                    "is continuously active, quietly collecting and "
                    "exfiltrating keystrokes rather than waiting to trigger a "
                    "one-time destructive event."
                ),
            },
        ],
        "explanation": (
            "Continuous, covert keystroke capture and exfiltration for "
            "surveillance purposes, without self-propagation or destruction, is "
            "a keylogger/spyware."
        ),
    },
    {
        "id": "nd2b-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Employees at a law firm report that thousands of case files across "
            "multiple network shares now have a new \".encrypted\" extension and "
            "no longer open. Every affected folder contains a new text file "
            "demanding payment in cryptocurrency within 72 hours in exchange for "
            "a decryption key, with a countdown timer that doubles the demanded "
            "amount if the deadline passes. Which malware type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Ransomware",
                "correct": True,
                "rationale": (
                    "Correct. Encrypting victim files and demanding "
                    "cryptocurrency payment for a decryption key, with an "
                    "escalating deadline, is the defining behavior of "
                    "ransomware."
                ),
            },
            {
                "id": "b",
                "text": "Cryptojacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Cryptojacking secretly uses a victim's "
                    "computing resources to mine cryptocurrency for the "
                    "attacker; it does not encrypt the victim's files or "
                    "demand a ransom payment."
                ),
            },
            {
                "id": "c",
                "text": "Wiper malware",
                "correct": False,
                "rationale": (
                    "Incorrect. Wiper malware is designed to permanently "
                    "destroy data with no intent or mechanism for recovery, "
                    "even if payment is made; here a ransom note explicitly "
                    "offers a path to decryption, which is inconsistent with "
                    "pure wiper intent."
                ),
            },
            {
                "id": "d",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb triggers a one-time destructive "
                    "action based on a specific condition; this scenario "
                    "describes an active, ongoing extortion scheme with a "
                    "ransom note and payment mechanism, not a dormant "
                    "triggered payload."
                ),
            },
        ],
        "explanation": (
            "Mass file encryption paired with a cryptocurrency ransom demand and "
            "payment deadline is the signature of ransomware, distinct from "
            "cryptojacking (resource theft), wiper malware (pure destruction "
            "with no recovery path offered), or a logic bomb (one-time "
            "triggered action)."
        ),
    },
    {
        "id": "nd2b-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types",
        "stem": (
            "A forensic analyst runs Task Manager and standard antivirus tools "
            "on a suspicious server and sees nothing unusual, but a bootable "
            "forensic tool run from external media reveals a hidden process and "
            "several hidden files that were invisible to the running operating "
            "system. Analysis shows a kernel-mode driver hooking system calls to "
            "filter out any reference to the malicious process and files from "
            "tools running within the compromised OS. Which malware type is "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rootkit",
                "correct": True,
                "rationale": (
                    "Correct. A kernel-level component that hooks system "
                    "calls to hide processes and files from tools running "
                    "within the compromised OS, only revealed when the OS "
                    "itself is bypassed, is the definition of a rootkit."
                ),
            },
            {
                "id": "b",
                "text": "Bootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A bootkit specifically infects the boot "
                    "process (such as the MBR or UEFI firmware) to load "
                    "before the OS and survive reinstallation; this scenario "
                    "describes a kernel-mode driver hiding activity within an "
                    "already-running OS, not boot-sector infection."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is dormant, condition-triggered "
                    "destructive code; this malware is actively and "
                    "continuously concealing a running process and files, not "
                    "waiting to trigger a destructive event."
                ),
            },
            {
                "id": "d",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan's defining trait is disguising "
                    "itself as legitimate software to trick a user into "
                    "installing it; this scenario centers on kernel-level "
                    "concealment techniques after infection, not the initial "
                    "deceptive delivery method."
                ),
            },
        ],
        "explanation": (
            "Kernel-level system-call hooking that hides a process and files "
            "from every tool running within the compromised OS, revealed only "
            "by bypassing the OS entirely, is the definition of a rootkit, "
            "distinct from a bootkit's boot-sector persistence."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A recursive DNS resolver used by an organization begins returning "
            "an attacker-controlled IP address for \"bank.example.com\" to "
            "every internal host that queries it, even though the bank's "
            "authoritative DNS records were never modified. Packet captures "
            "show the resolver received a flood of forged DNS responses with "
            "guessed transaction IDs immediately after each legitimate query, "
            "arriving just before the real authoritative answer. Which attack "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS cache poisoning",
                "correct": True,
                "rationale": (
                    "Correct. Injecting a forged response with a matching "
                    "(guessed) transaction ID before the legitimate "
                    "authoritative answer arrives, causing the resolver to "
                    "cache and serve the attacker's IP for subsequent "
                    "queries, is the definition of DNS cache poisoning."
                ),
            },
            {
                "id": "b",
                "text": "ARP poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning operates at Layer 2 within a "
                    "local segment by forging MAC-to-IP bindings; this attack "
                    "targets DNS resolution at the application layer by "
                    "forging DNS responses, not ARP replies."
                ),
            },
            {
                "id": "c",
                "text": "Domain hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Domain hijacking involves an attacker "
                    "gaining unauthorized control of the domain's actual "
                    "registration or authoritative DNS records; here the "
                    "authoritative records were never modified, only the "
                    "resolver's cache was corrupted with forged responses."
                ),
            },
            {
                "id": "d",
                "text": "On-path (man-in-the-middle) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An on-path attack requires the attacker to "
                    "be positioned inline intercepting traffic between two "
                    "parties; this attack instead races forged responses to "
                    "arrive at the resolver before the legitimate one, "
                    "without the attacker needing to sit inline on the "
                    "traffic path."
                ),
            },
        ],
        "explanation": (
            "Forging DNS responses with matching transaction IDs to beat the "
            "legitimate authoritative answer and corrupt a resolver's cache is "
            "DNS cache poisoning, distinct from ARP poisoning (Layer 2), domain "
            "hijacking (registrar/authoritative record takeover), or a true "
            "on-path interception."
        ),
    },
    {
        "id": "nd2b-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "Employees' laptops in the parking garage automatically connect to "
            "a Wi-Fi network broadcasting the exact same SSID as the corporate "
            "wireless network, but with a much stronger signal than any "
            "legitimate access point in that area. Shortly afterward, several "
            "employees' captured login credentials appear on an underground "
            "forum. Which attack MOST likely occurred?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Evil twin attack",
                "correct": True,
                "rationale": (
                    "Correct. A rogue access point broadcasting an identical "
                    "SSID to the legitimate corporate network, with a "
                    "stronger signal to entice automatic connections, is the "
                    "definition of an evil twin attack used to capture "
                    "credentials."
                ),
            },
            {
                "id": "b",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking involves sending unsolicited data "
                    "over Bluetooth to nearby devices; this scenario "
                    "describes a rogue Wi-Fi access point, an entirely "
                    "different wireless technology and mechanism."
                ),
            },
            {
                "id": "c",
                "text": "ARP poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning manipulates MAC-to-IP bindings "
                    "on an already-joined local network segment; this attack "
                    "instead lures victims into joining an entirely separate, "
                    "attacker-controlled wireless network in the first place."
                ),
            },
            {
                "id": "d",
                "text": "DNS cache poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS poisoning corrupts name resolution "
                    "records; this scenario describes victims connecting to "
                    "a fraudulent wireless access point that captures "
                    "credentials directly, not corrupted DNS responses."
                ),
            },
        ],
        "explanation": (
            "A rogue access point mimicking the legitimate SSID with a "
            "stronger signal to lure automatic connections and harvest "
            "credentials is an evil twin attack, distinct from Bluetooth-based, "
            "ARP-based, or DNS-based attacks."
        ),
    },
    {
        "id": "nd2b-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "A web server becomes unresponsive to new connections. Firewall "
            "logs show an enormous spike in TCP SYN packets arriving from "
            "thousands of distinct source IP addresses, none of which ever "
            "send the final ACK to complete the three-way handshake, and the "
            "server's connection table shows thousands of entries stuck in the "
            "SYN_RECEIVED state. Many of the source IPs correspond to address "
            "blocks that are not currently routed on the internet. Which TWO "
            "findings BEST confirm this is a SYN flood attack rather than a "
            "legitimate traffic surge? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A large number of connections stuck in SYN_RECEIVED with "
                    "no completing ACK ever received"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Half-open connections that never complete the "
                    "handshake, exhausting the connection table, is the core "
                    "mechanism and defining evidence of a SYN flood."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Many source IP addresses correspond to unrouted/"
                    "unallocated address blocks, indicating spoofed sources"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Traffic appearing to originate from IP space "
                    "that isn't actually routable on the internet strongly "
                    "indicates the source addresses were forged (spoofed), "
                    "which is a hallmark of SYN flood attacks, since real "
                    "users at those addresses could never receive a "
                    "response."
                ),
            },
            {
                "id": "c",
                "text": "The traffic volume is high",
                "correct": False,
                "rationale": (
                    "Incorrect. High volume alone can also occur during a "
                    "legitimate flash-crowd traffic surge (such as a product "
                    "launch); volume by itself doesn't distinguish an attack "
                    "from a legitimate spike without the half-open connection "
                    "and spoofing evidence."
                ),
            },
            {
                "id": "d",
                "text": "The traffic uses the TCP protocol",
                "correct": False,
                "rationale": (
                    "Incorrect. The vast majority of legitimate web traffic "
                    "also uses TCP; the protocol alone is a completely "
                    "generic fact that provides no evidence of malicious "
                    "intent."
                ),
            },
        ],
        "explanation": (
            "Thousands of half-open connections that never complete the "
            "handshake, combined with source addresses drawn from unroutable "
            "ranges (indicating spoofing), are the specific evidence confirming "
            "a SYN flood — raw volume and protocol type alone do not "
            "distinguish an attack from legitimate demand."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A bank customer enters their PIN at a lobby kiosk. Investigators "
            "later determine that a person standing several feet away, "
            "pretending to read a brochure, used a small handheld mirror angled "
            "toward the keypad to observe and memorize the PIN, with no device, "
            "card, or badge involved at any point. Which attack does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Shoulder surfing",
                "correct": True,
                "rationale": (
                    "Correct. Covertly observing a target entering sensitive "
                    "information, such as a PIN, using direct or indirect "
                    "(mirror-assisted) line of sight, is the definition of "
                    "shoulder surfing."
                ),
            },
            {
                "id": "b",
                "text": "Skimming",
                "correct": False,
                "rationale": (
                    "Incorrect. Skimming requires a physical device attached "
                    "to a card reader to capture card data electronically; no "
                    "such device was used here, only visual observation."
                ),
            },
            {
                "id": "c",
                "text": "Badge cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. Badge cloning involves electronically "
                    "capturing and duplicating an RFID/proximity credential's "
                    "signal; no access badge or electronic capture device was "
                    "involved in this PIN observation."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving involves retrieving "
                    "information from discarded materials; the PIN here was "
                    "captured through direct visual observation at the "
                    "moment of entry, not from discarded records."
                ),
            },
        ],
        "explanation": (
            "Visually observing a PIN entry — even indirectly through a "
            "mirror — with no device or credential involved, is shoulder "
            "surfing."
        ),
    },
    {
        "id": "nd2b-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Physical attacks",
        "stem": (
            "Physical security investigates an after-hours break-in at a data "
            "center annex. Findings include: a section of the perimeter fence "
            "professionally cut and re-fastened with matching hardware so it "
            "appeared undisturbed at a glance; motion-sensor logs showing that "
            "only the one sensor covering the cut section had been disconnected "
            "two days before the break-in, while every other sensor logged "
            "normally; a covert network tap spliced into the core switch's "
            "uplink cable, wired to a small hidden storage device rather than "
            "any equipment being removed; and the break-in occurring at 2 a.m. "
            "on a Saturday. Which TWO findings BEST indicate a sophisticated, "
            "planned intrusion focused on ongoing data collection rather than "
            "opportunistic theft? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The specific motion sensor covering the cut section was "
                    "disconnected two days in advance, while all others "
                    "remained active"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Disabling only the one relevant sensor well "
                    "ahead of the break-in, rather than all sensors or none, "
                    "demonstrates advance reconnaissance and planning "
                    "specific to this intrusion."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A covert network tap was installed and wired to a "
                    "hidden storage device instead of any equipment being "
                    "stolen"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Installing a passive collection device to "
                    "capture ongoing network traffic, rather than grabbing "
                    "visible assets, indicates the goal was continuous data "
                    "collection, not smash-and-grab theft — a hallmark of a "
                    "deliberate, targeted physical intrusion."
                ),
            },
            {
                "id": "c",
                "text": "The break-in occurred at 2 a.m.",
                "correct": False,
                "rationale": (
                    "Incorrect. Late-night timing alone is common to almost "
                    "any unauthorized break-in, opportunistic or planned, and "
                    "does not by itself indicate sophistication or a data-"
                    "collection motive."
                ),
            },
            {
                "id": "d",
                "text": "The fence was cut",
                "correct": False,
                "rationale": (
                    "Incorrect. A cut fence by itself only shows forced "
                    "entry; it is the careful re-fastening to avoid casual "
                    "detection, combined with the targeted sensor and network "
                    "tap, that reveals planning — cutting alone doesn't "
                    "distinguish sophisticated from opportunistic entry."
                ),
            },
        ],
        "explanation": (
            "Pre-disabling only the relevant sensor and installing a covert, "
            "ongoing data-collection tap (rather than stealing visible "
            "equipment) are the clearest signs of a planned, targeted "
            "intrusion; the time of night and the mere fact of a cut fence are "
            "common to break-ins generally and don't by themselves indicate "
            "sophistication."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A cryptography researcher demonstrates that, for a hash function "
            "producing a 64-bit digest, an attacker needs only about 2^32 "
            "randomly generated inputs on average to find any two that produce "
            "the same hash output — far fewer attempts than the 2^64 needed to "
            "find a match for one specific target digest. The researcher uses "
            "this shortcut to efficiently locate a colliding pair of "
            "certificates. Which term describes this mathematical technique?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Birthday attack",
                "correct": True,
                "rationale": (
                    "Correct. Exploiting the birthday-paradox probability "
                    "that any two random inputs (rather than one specific "
                    "match) are far more likely to collide, drastically "
                    "reducing the number of attempts needed, is precisely "
                    "what a birthday attack describes."
                ),
            },
            {
                "id": "b",
                "text": "Collision attack",
                "correct": False,
                "rationale": (
                    "Incorrect. \"Collision attack\" broadly names the goal "
                    "of finding any two inputs with the same hash; the "
                    "specific probabilistic shortcut used to reach that goal "
                    "so much faster than brute force, as described here, is "
                    "what makes it a birthday attack."
                ),
            },
            {
                "id": "c",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A rainbow table attack uses precomputed "
                    "hash-to-plaintext lookup tables to reverse a specific "
                    "hash back to a likely password; it doesn't describe the "
                    "probability-based shortcut for finding two colliding "
                    "inputs at random."
                ),
            },
            {
                "id": "d",
                "text": "Brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A brute-force attack exhaustively tries all "
                    "or most possible inputs to find one specific match; the "
                    "researcher's method specifically leverages birthday-"
                    "paradox probability to need dramatically fewer attempts "
                    "than an exhaustive brute-force search."
                ),
            },
        ],
        "explanation": (
            "Leveraging birthday-paradox probability, so that finding any two "
            "colliding inputs takes vastly fewer attempts than finding a "
            "specific match, is the defining mechanism of a birthday attack, "
            "distinguishing the technique from the general term \"collision "
            "attack,\" rainbow tables, or brute force."
        ),
    },
    {
        "id": "nd2b-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A penetration tester obtains a leaked database of unsalted NTLM "
            "password hashes. Using a large precomputed table of hash-to-"
            "plaintext mappings stored on a portable drive, the tester recovers "
            "the plaintext passwords for over 90% of the accounts within "
            "minutes; an identical exhaustive brute-force approach against the "
            "same hash set was estimated to take several years. Which attack "
            "technique did the tester use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rainbow table attack",
                "correct": True,
                "rationale": (
                    "Correct. Using a precomputed table mapping hash outputs "
                    "to their corresponding plaintext values to rapidly "
                    "reverse unsalted hashes, dramatically faster than "
                    "computing each guess in real time, is the definition of "
                    "a rainbow table attack."
                ),
            },
            {
                "id": "b",
                "text": "Brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A brute-force attack computes each password "
                    "guess in real time without precomputed data, which is "
                    "why it would take years here; the tester instead used a "
                    "precomputed lookup table to recover passwords in "
                    "minutes."
                ),
            },
            {
                "id": "c",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack exploits collision "
                    "probability to find any two matching hash outputs; the "
                    "tester's goal here was reversing specific hashes back to "
                    "their original plaintext values, not finding colliding "
                    "pairs."
                ),
            },
            {
                "id": "d",
                "text": "Dictionary attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A dictionary attack tests a curated wordlist "
                    "of likely passwords in real time against the hashes; "
                    "while related, the tester's speed advantage came "
                    "specifically from a precomputed hash-to-plaintext table "
                    "rather than testing wordlist entries on the fly."
                ),
            },
        ],
        "explanation": (
            "Rapidly reversing unsalted hashes using a precomputed hash-to-"
            "plaintext lookup table, far faster than computing guesses live, is "
            "a rainbow table attack, distinct from brute-force, birthday, or "
            "dictionary attacks."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "A confidential financial spreadsheet was deleted from a shared "
            "network drive. Multiple employees have access to the folder, and "
            "the file server administrator needs to determine exactly which "
            "specific user account performed the deletion and at what time. "
            "Which log source will MOST directly answer this question?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "File/object access audit logs (Windows Security Event "
                    "Log with object auditing enabled)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Object access auditing records exactly which "
                    "account performed a specific file operation, such as "
                    "deletion, on a given resource, directly answering the "
                    "\"who deleted this file\" investigative question."
                ),
            },
            {
                "id": "b",
                "text": "DHCP server logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs record IP address lease "
                    "assignments to devices, not which user account "
                    "performed a file operation on a shared drive."
                ),
            },
            {
                "id": "c",
                "text": "Web proxy logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Web proxy logs capture outbound web browsing "
                    "activity; they have no visibility into internal file-"
                    "server object operations like deletions."
                ),
            },
            {
                "id": "d",
                "text": "Vulnerability scan reports",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scan reports identify "
                    "weaknesses in systems and software; they do not record "
                    "real-time user file-access or deletion events."
                ),
            },
        ],
        "explanation": (
            "To determine exactly which account performed a specific file "
            "deletion, object access audit logs (with object auditing enabled) "
            "are the most direct log source, unlike DHCP, proxy, or "
            "vulnerability scan data."
        ),
    },
    {
        "id": "nd2b-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "A public-facing web server was compromised before a critical patch "
            "could be applied. Investigators have already confirmed which "
            "vulnerability existed, but now need to determine the exact byte-"
            "level exploit payload the attacker sent to trigger it, in order to "
            "build a custom detection signature. Which log source will BEST "
            "answer this question?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Full packet capture (PCAP)/IDS logs",
                "correct": True,
                "rationale": (
                    "Correct. Full packet captures preserve the complete raw "
                    "payload of network traffic, allowing investigators to "
                    "examine the exact bytes of the exploit sent to the "
                    "server, which summary logs cannot provide."
                ),
            },
            {
                "id": "b",
                "text": "Authentication logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication logs record login attempts "
                    "and outcomes; they do not capture the raw content of "
                    "exploit payloads sent against an application "
                    "vulnerability."
                ),
            },
            {
                "id": "c",
                "text": "DHCP logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs record IP address lease "
                    "information for devices joining the network, providing "
                    "no visibility into the content of an exploit payload."
                ),
            },
            {
                "id": "d",
                "text": "Antivirus quarantine logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine logs show that a known malicious "
                    "file was detected and isolated after the fact; they do "
                    "not capture the raw network-level exploit payload used "
                    "to initially compromise the server."
                ),
            },
        ],
        "explanation": (
            "To recover the exact byte-level content of an exploit payload for "
            "building a detection signature, full packet capture/IDS logs are "
            "the most direct source, since they preserve raw traffic rather "
            "than summarized events."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "An attacker who gained local administrator access to one "
            "workstation uses a credential-dumping tool to extract the NTLM "
            "password hash of a domain account cached in memory. The attacker "
            "then uses that hash directly to authenticate to a file server over "
            "SMB, without ever cracking it to recover the plaintext password. "
            "Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pass-the-hash",
                "correct": True,
                "rationale": (
                    "Correct. Authenticating to another system using a "
                    "captured password hash directly, without ever needing "
                    "to crack or know the plaintext password, is the "
                    "definition of a pass-the-hash attack."
                ),
            },
            {
                "id": "b",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting involves requesting Kerberos "
                    "TGS tickets for service accounts and cracking their "
                    "encryption offline to recover a plaintext password; here "
                    "the attacker used an NTLM hash directly via SMB with no "
                    "Kerberos ticket request or offline cracking involved."
                ),
            },
            {
                "id": "c",
                "text": "Golden ticket attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A golden ticket attack forges a Kerberos TGT "
                    "using a compromised krbtgt account hash for persistent, "
                    "universal domain access; this scenario involves a "
                    "specific captured NTLM hash used for one authentication, "
                    "not a forged domain-wide ticket."
                ),
            },
            {
                "id": "d",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A rainbow table attack reverses a hash back "
                    "to its original plaintext password using precomputed "
                    "tables; the attacker here never attempted to recover "
                    "the plaintext at all, using the hash directly to "
                    "authenticate instead."
                ),
            },
        ],
        "explanation": (
            "Directly authenticating with a captured password hash, without "
            "ever cracking it to plaintext, is a pass-the-hash attack, distinct "
            "from Kerberoasting, golden ticket attacks, or rainbow table "
            "cracking."
        ),
    },
    {
        "id": "nd2b-036",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "An attacker on an unencrypted guest Wi-Fi network captures a "
            "legitimate one-time authentication token transmitted in plaintext "
            "between a mobile app and its backend server. Within seconds, "
            "before the token's short validity window expires, the attacker "
            "resends the exact same captured token to the server and is "
            "granted access to the victim's account, without ever learning the "
            "victim's password. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replay attack",
                "correct": True,
                "rationale": (
                    "Correct. Capturing a legitimate authentication token or "
                    "credential and resending it, unmodified, before it "
                    "expires to gain unauthorized access is the definition of "
                    "a replay attack."
                ),
            },
            {
                "id": "b",
                "text": "Pass-the-hash",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses a password hash "
                    "extracted from a compromised system's memory to "
                    "authenticate; here the attacker captured a live "
                    "authentication token in transit over the network, not a "
                    "hash pulled from local memory."
                ),
            },
            {
                "id": "c",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing involves automated login "
                    "attempts using breached username/password pairs across "
                    "many accounts; this attack instead captured and resent "
                    "a single live token intercepted from actual network "
                    "traffic."
                ),
            },
            {
                "id": "d",
                "text": "On-path (man-in-the-middle) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. While the attacker was on the same network, "
                    "simply capturing and resending a token afterward is the "
                    "defining action here — an on-path attack implies "
                    "actively intercepting and potentially altering traffic "
                    "in real time between the two parties, whereas this "
                    "attack specifically reused a captured token after the "
                    "fact, making replay attack the more precise "
                    "classification."
                ),
            },
        ],
        "explanation": (
            "Capturing a valid authentication token from unencrypted traffic "
            "and resending it before it expires to impersonate the victim is a "
            "replay attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A security assessment of a retail chain's network finds that "
            "several point-of-sale printers and IoT environmental sensors are "
            "still configured with the vendor's factory-set administrator "
            "credentials, which are printed in the publicly available product "
            "manual. No software vulnerability was found on these devices. "
            "Which hardening action should be taken to remediate this specific "
            "finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Change all default credentials to unique, strong passwords",
                "correct": True,
                "rationale": (
                    "Correct. When devices are exposed specifically because "
                    "they retain publicly known factory-default credentials, "
                    "the direct and appropriate hardening step is changing "
                    "those defaults to unique, strong credentials."
                ),
            },
            {
                "id": "b",
                "text": "Apply the latest firmware patches to the devices",
                "correct": False,
                "rationale": (
                    "Incorrect. No software vulnerability was identified in "
                    "this finding; patching would not address the actual "
                    "issue, which is unchanged factory-default login "
                    "credentials."
                ),
            },
            {
                "id": "c",
                "text": "Enable full-disk encryption on the devices",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data at rest if a "
                    "device's storage is physically removed; it does nothing "
                    "to prevent unauthorized login using known default "
                    "credentials."
                ),
            },
            {
                "id": "d",
                "text": "Deploy a network intrusion prevention system",
                "correct": False,
                "rationale": (
                    "Incorrect. An IPS can help detect and block malicious "
                    "traffic patterns, but it does not directly remediate "
                    "the root cause here, which is the continued use of "
                    "default administrator credentials."
                ),
            },
        ],
        "explanation": (
            "When a finding specifically involves devices still using "
            "publicly known factory-default logins, the direct hardening "
            "remediation is changing those default credentials, not patching, "
            "encryption, or a separate detection control."
        ),
    },
    {
        "id": "nd2b-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A vendor discloses a critical buffer overflow vulnerability in a "
            "widely used application, but the official patch will not be "
            "available for another three weeks. In the meantime, the security "
            "team configures endpoint protection software to detect and block "
            "the specific exploit's memory-corruption signature at the host "
            "level, preventing exploitation attempts from succeeding even "
            "though the underlying flaw remains unpatched. Which mitigation "
            "technique does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Host-based intrusion prevention system (HIPS) / virtual patching",
                "correct": True,
                "rationale": (
                    "Correct. Detecting and blocking a specific known "
                    "exploit's behavior or signature at the endpoint, as a "
                    "stopgap before an official patch is available, is the "
                    "definition of a host-based IPS providing virtual "
                    "patching."
                ),
            },
            {
                "id": "b",
                "text": "Application allow listing",
                "correct": False,
                "rationale": (
                    "Incorrect. Allow listing restricts which executables "
                    "are permitted to run at all; it does not describe "
                    "blocking a specific exploit's memory-corruption behavior "
                    "within an already-approved, legitimately running "
                    "application."
                ),
            },
            {
                "id": "c",
                "text": "Network segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation limits which network zones can "
                    "reach a vulnerable system; this control instead "
                    "operates directly on the host itself, detecting and "
                    "blocking the exploit's behavior at the endpoint."
                ),
            },
            {
                "id": "d",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. Patch management refers to the process of "
                    "applying the vendor's official fix; the scenario "
                    "explicitly states the official patch is not yet "
                    "available, and the team instead used a host-based "
                    "compensating control in the interim."
                ),
            },
        ],
        "explanation": (
            "Blocking a specific known exploit's behavior at the endpoint "
            "level before an official patch exists is host-based IPS/virtual "
            "patching, a hardening technique distinct from allow listing, "
            "segmentation, or the eventual patch itself."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2b-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "An incident investigation reveals that a marketing coordinator's "
            "compromised account was used to access and exfiltrate the "
            "organization's entire HR payroll database, even though the "
            "coordinator's job function never required any access to HR "
            "systems; the account had been granted broad, domain-wide read "
            "access years earlier for a one-time project and was never "
            "revoked. Which mitigation technique would MOST effectively have "
            "prevented this scope of impact?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enforcing least privilege (role-based access restricted to job function)",
                "correct": True,
                "rationale": (
                    "Correct. Limiting each account's access strictly to "
                    "what its current job function requires, and revoking "
                    "access no longer needed, would have prevented a "
                    "marketing account from ever being able to reach the "
                    "unrelated HR payroll database in the first place."
                ),
            },
            {
                "id": "b",
                "text": "Network segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation restricts network-level "
                    "reachability between zones, but the coordinator's "
                    "account had valid application-level permissions to the "
                    "HR data; the root cause here is excessive access "
                    "rights, not network path availability."
                ),
            },
            {
                "id": "c",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no vulnerability described being "
                    "exploited; the account authenticated normally and used "
                    "its already-granted, excessive permissions, which "
                    "patching would not address."
                ),
            },
            {
                "id": "d",
                "text": "Full-disk encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data if physical "
                    "storage media is stolen; it does not restrict what a "
                    "valid, authenticated account is permitted to access "
                    "over the network."
                ),
            },
        ],
        "explanation": (
            "Because the damage resulted from an account retaining far more "
            "access than its job required, enforcing least privilege — and "
            "revoking access no longer needed — is the mitigation that would "
            "have most directly limited the impact."
        ),
    },
    {
        "id": "nd2b-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "An EDR alert identifies cryptomining malware actively running on "
            "a single employee workstation. The incident responder's first "
            "containment action is to immediately disconnect that specific "
            "workstation from the network (both wired and Wi-Fi) while "
            "preserving its running state for forensic analysis, without "
            "making any changes to firewall rules or VLAN assignments for the "
            "rest of the department. Which mitigation technique was applied?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Isolation",
                "correct": True,
                "rationale": (
                    "Correct. Removing a single specific compromised host "
                    "from network connectivity, without altering the broader "
                    "network's structure, is the definition of isolation as "
                    "a containment mitigation."
                ),
            },
            {
                "id": "b",
                "text": "Network segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation involves structurally dividing "
                    "the network into separate zones with controlled "
                    "boundaries; this action instead disconnected one "
                    "individual host directly, without any broader "
                    "restructuring of network zones."
                ),
            },
            {
                "id": "c",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. No vulnerability was patched in this action; "
                    "the response was purely to remove the single infected "
                    "host's network connectivity for containment."
                ),
            },
            {
                "id": "d",
                "text": "Decommissioning",
                "correct": False,
                "rationale": (
                    "Incorrect. Decommissioning is the permanent retirement "
                    "and secure disposal of an asset; here the workstation "
                    "was only temporarily disconnected for containment and "
                    "forensic preservation, not permanently retired."
                ),
            },
        ],
        "explanation": (
            "Disconnecting one specific compromised host from the network, "
            "without restructuring the broader network into zones, is "
            "isolation, distinct from segmentation (a structural division "
            "applied more broadly), patching, or permanent decommissioning."
        ),
    },
]
