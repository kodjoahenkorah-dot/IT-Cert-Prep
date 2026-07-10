"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch H.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 2 in
``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Threat actors (2.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A defense contractor's bid-preparation network is breached using a "
            "previously unknown exploit chain. The stolen proposal data is never "
            "leaked, sold, or referenced in any extortion demand; weeks later the "
            "contractor loses the contract to a foreign state-owned competitor whose "
            "winning bid undercuts theirs by an improbably precise margin. Threat "
            "intelligence ties the intrusion infrastructure to a group previously "
            "linked to that country's military intelligence service. Which threat "
            "actor classification BEST fits this intrusion?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Nation-state actor",
                "correct": True,
                "rationale": (
                    "Correct. A zero-day exploit chain, no monetization or public "
                    "disclosure, a strategic economic/competitive motive, and "
                    "attribution to known state intelligence infrastructure are all "
                    "hallmarks of a well-resourced nation-state operation."
                ),
            },
            {
                "id": "b",
                "text": "Organized crime group",
                "correct": False,
                "rationale": (
                    "Incorrect. Organized crime seeks direct financial gain through "
                    "extortion or resale of stolen data; here nothing was monetized "
                    "or offered for sale, and the benefit flowed to a state-owned "
                    "competitor instead."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological statement, public leak, or "
                    "protest messaging; the operation was silent and served a "
                    "competitive intelligence purpose, not activism."
                ),
            },
            {
                "id": "d",
                "text": "Unskilled attacker (script kiddie)",
                "correct": False,
                "rationale": (
                    "Incorrect. A previously unknown (zero-day) exploit chain "
                    "requires significant capability and resources far beyond what "
                    "an unskilled attacker using off-the-shelf tools could develop."
                ),
            },
        ],
        "explanation": (
            "A zero-day exploit chain, silence about the breach, a strategic "
            "economic benefit to a foreign government-linked competitor, and "
            "infrastructure attribution to state intelligence together point to a "
            "nation-state actor rather than a profit-driven, ideological, or "
            "low-skill attacker."
        ),
    },
    {
        "id": "nd2h-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A sales representative, frustrated that the approved CRM tool cannot "
            "attach large presentation files, begins using a free personal "
            "file-conversion website to compress and email customer proposal decks. "
            "The representative has no malicious intent and is unaware the site "
            "retains and indexes every uploaded document, later exposing customer "
            "contact data in a search engine. Which threat classification BEST "
            "describes the representative's role in this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Shadow IT",
                "correct": True,
                "rationale": (
                    "Correct. An employee adopting an unapproved, unvetted "
                    "third-party tool to work around a business process, without "
                    "malicious intent, is the definition of shadow IT — and it "
                    "created the exposure here."
                ),
            },
            {
                "id": "b",
                "text": "Insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. Insider threat implies malicious or knowingly "
                    "negligent intent to harm the organization; the representative "
                    "was simply trying to get work done and was unaware of the "
                    "risk, which is the hallmark of shadow IT, not malicious "
                    "insider activity."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological agenda or intent to "
                    "publicize a cause; this is an unintentional data exposure "
                    "caused by unsanctioned tool use."
                ),
            },
            {
                "id": "d",
                "text": "Organized crime group",
                "correct": False,
                "rationale": (
                    "Incorrect. No external criminal actor orchestrated this "
                    "exposure; it resulted from an employee's own unsanctioned "
                    "tool choice, not a targeted criminal operation."
                ),
            },
        ],
        "explanation": (
            "Using unapproved, unmanaged technology to accomplish a legitimate "
            "business task — without malicious intent — is shadow IT, distinct "
            "from a deliberately harmful insider threat."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-003",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "An internet-wide scanning service indexes a company's Kubernetes "
            "cluster dashboard, which was deployed without authentication enabled "
            "and is reachable on its default port from any public IP address. "
            "Attackers use the exposed dashboard to deploy cryptomining containers "
            "across the cluster. Which attack vector was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open service port",
                "correct": True,
                "rationale": (
                    "Correct. A management interface left reachable on its default "
                    "port with no authentication, discoverable by internet-wide "
                    "scanning, is the classic open-service-port attack vector."
                ),
            },
            {
                "id": "b",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media was involved; the cluster was "
                    "compromised entirely over the network through an exposed "
                    "management port."
                ),
            },
            {
                "id": "c",
                "text": "Message-based",
                "correct": False,
                "rationale": (
                    "Incorrect. No email, SMS, or messaging channel delivered the "
                    "attack; discovery and exploitation both occurred through "
                    "direct network scanning of an open port."
                ),
            },
            {
                "id": "d",
                "text": "Default credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. The dashboard had no authentication at all rather "
                    "than a default username/password that was never changed; the "
                    "root exposure is the reachable, unauthenticated open port "
                    "itself."
                ),
            },
        ],
        "explanation": (
            "An administrative service left reachable on the internet at its "
            "default port, discovered via mass scanning, is the open-service-port "
            "attack vector — distinct from default credentials, which requires an "
            "actual (unchanged) login to be present."
        ),
    },
    {
        "id": "nd2h-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A hospital continues operating a radiology control application on an "
            "operating system whose vendor ended all security updates six years "
            "ago. No patch exists for a newly disclosed remote code execution flaw "
            "in that OS because the vendor no longer issues fixes for it at any "
            "price. Which attack surface issue does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unsupported systems and applications",
                "correct": True,
                "rationale": (
                    "Correct. Software whose vendor no longer provides security "
                    "updates at all — regardless of willingness to pay — is an "
                    "unsupported system, a distinct and often unfixable attack "
                    "surface."
                ),
            },
            {
                "id": "b",
                "text": "Vulnerable software",
                "correct": False,
                "rationale": (
                    "Incorrect. \"Vulnerable software\" typically describes a "
                    "currently supported product with a fix available that simply "
                    "hasn't been applied yet; here no fix exists at all because the "
                    "vendor discontinued support."
                ),
            },
            {
                "id": "c",
                "text": "Default credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a missing vendor patch for "
                    "an end-of-life OS, not an unchanged default username or "
                    "password."
                ),
            },
            {
                "id": "d",
                "text": "Open service port",
                "correct": False,
                "rationale": (
                    "Incorrect. No exposed network port or service is described; "
                    "the issue is the underlying operating system's end-of-support "
                    "status."
                ),
            },
        ],
        "explanation": (
            "When a vendor has permanently stopped issuing security updates for a "
            "product, that product is an unsupported system/application — a "
            "different and often more severe attack surface issue than a "
            "supported product with an outstanding but available patch."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "After a newly promoted vice president posts a public \"excited to "
            "start my new role\" announcement on a professional networking site, "
            "she receives an email addressed to her by name and new title, "
            "congratulating her and asking her to \"update your executive "
            "calendar sync settings\" via an attached link that leads to a "
            "credential-harvesting page. No one else at the company receives the "
            "message. Which technique BEST describes this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spear phishing",
                "correct": True,
                "rationale": (
                    "Correct. The message is personalized using publicly gathered "
                    "details (her name, new title, timing) and sent to a single, "
                    "specifically researched target — the definition of spear "
                    "phishing."
                ),
            },
            {
                "id": "b",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling specifically targets the very highest "
                    "tier of an organization (C-suite executives); a newly "
                    "promoted vice president being individually researched fits "
                    "the broader spear-phishing pattern rather than requiring the "
                    "C-suite-specific whaling label."
                ),
            },
            {
                "id": "c",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. BEC involves a compromised or spoofed internal "
                    "executive email account used to direct financial or data "
                    "actions; here the attacker sends the phishing email from an "
                    "external, unaffiliated address to harvest credentials, not "
                    "impersonating an internal executive to trigger a transaction."
                ),
            },
            {
                "id": "d",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is conducted over a live voice call; this "
                    "entire attack was delivered by email."
                ),
            },
        ],
        "explanation": (
            "A message crafted using specific, researched details about one named "
            "individual is spear phishing; without evidence the target is being "
            "singled out specifically for her C-suite rank or that an internal "
            "executive identity was impersonated, the more general spear-phishing "
            "label is the best fit."
        ),
    },
    {
        "id": "nd2h-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "A vendor's accounts-receivable employee falls for a credential-"
            "phishing email and their real corporate mailbox is compromised. Days "
            "later, the attacker inserts a reply into an existing, legitimate "
            "invoice email thread between that vendor and one of its customers, "
            "using the vendor employee's actual mailbox, instructing the customer "
            "to send the next payment to a new bank account. Which technique BEST "
            "describes this stage of the attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Business email compromise (invoice manipulation)",
                "correct": True,
                "rationale": (
                    "Correct. Using a genuinely compromised, legitimate mailbox to "
                    "insert fraudulent payment instructions into an authentic "
                    "ongoing thread is the defining pattern of business email "
                    "compromise via invoice manipulation."
                ),
            },
            {
                "id": "b",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. No lookalike domain was registered; the attacker "
                    "used the vendor employee's actual, compromised email account, "
                    "not a spoofed similar-looking one."
                ),
            },
            {
                "id": "c",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A watering hole attack compromises a third-party "
                    "website that targets are known to visit; this attack occurs "
                    "entirely through email, with no compromised website involved."
                ),
            },
            {
                "id": "d",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. The entire attack, from the initial phishing to "
                    "the fraudulent payment instruction, is conducted by email, "
                    "not a live phone call."
                ),
            },
        ],
        "explanation": (
            "When a real, compromised mailbox is used to inject fraudulent "
            "banking instructions into a genuine invoice conversation, that is "
            "business email compromise/invoice manipulation, which is more severe "
            "than typosquatting because no lookalike domain is even needed — the "
            "communication is authentic."
        ),
    },
    {
        "id": "nd2h-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "Review the internal chat message sent to procurement staff:\n\n"
            "\"Reminder: only 3 of our discount vendor-onboarding codes remain "
            "this quarter. Over 200 of your colleagues across other departments "
            "have already redeemed theirs this week — don't miss out, claim yours "
            "at the link below before they're gone.\"\n\n"
            "Which TWO social engineering principles are being leveraged in this "
            "message? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Scarcity",
                "correct": True,
                "rationale": (
                    "Correct. Framing the codes as a limited quantity (\"only 3 "
                    "remain\") that will soon run out is a direct appeal to "
                    "scarcity to drive immediate action."
                ),
            },
            {
                "id": "b",
                "text": "Social proof (consensus)",
                "correct": True,
                "rationale": (
                    "Correct. Citing that \"over 200 of your colleagues\" have "
                    "already redeemed theirs leverages the target's tendency to "
                    "follow what peers are already doing."
                ),
            },
            {
                "id": "c",
                "text": "Authority",
                "correct": False,
                "rationale": (
                    "Incorrect. The message does not invoke a position of "
                    "organizational or institutional power (such as a manager or "
                    "executive) to compel compliance; it relies on limited supply "
                    "and peer behavior instead."
                ),
            },
            {
                "id": "d",
                "text": "Intimidation",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no threat of negative consequence or "
                    "coercive pressure; the message uses positive-framed incentive "
                    "language (a discount opportunity), not intimidation."
                ),
            },
        ],
        "explanation": (
            "\"Only 3 remain\" is a scarcity cue, and \"200 of your colleagues "
            "have already redeemed theirs\" is a social proof/consensus cue; "
            "neither authority nor intimidation is present in this message."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A legacy C-based logging utility passes a user-supplied comment "
            "field directly as the first argument to a printf-style function "
            "instead of as a data argument. A tester submits the string "
            "\"%x %x %x %x\" as the comment and the resulting log entry contains "
            "raw hexadecimal values pulled from the process's stack memory. Which "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Format string vulnerability",
                "correct": True,
                "rationale": (
                    "Correct. Passing untrusted input directly as the format "
                    "specifier to a printf-style function lets an attacker use "
                    "conversion specifiers like %x to read (or with %n, write) "
                    "arbitrary stack memory — the definition of a format string "
                    "vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No oversized input overran a fixed-size buffer "
                    "here; the flaw is that user input controls the format "
                    "specifier itself, not that a buffer boundary was exceeded."
                ),
            },
            {
                "id": "c",
                "text": "Integer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No arithmetic operation exceeded a variable's "
                    "storage capacity; the issue is untrusted data being "
                    "interpreted as format-string control characters."
                ),
            },
            {
                "id": "d",
                "text": "Time-of-check to time-of-use (TOCTOU) race condition",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no timing gap between checking and using "
                    "a resource described here; the leak occurs synchronously "
                    "from a single malformed logging call."
                ),
            },
        ],
        "explanation": (
            "User-controlled input reaching the format-string argument of a "
            "printf-style function, allowing memory disclosure via specifiers "
            "like %x, is a format string vulnerability distinct from a buffer "
            "overflow, integer overflow, or race condition."
        ),
    },
    {
        "id": "nd2h-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A signed, trusted application loads a required DLL by filename only, "
            "searching its own working directory before searching the system "
            "directories. An attacker places a malicious DLL with the exact same "
            "filename in the application's working directory; the next time a "
            "user launches the application, the attacker's code executes with the "
            "trusted application's privileges. Which vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DLL side-loading (insecure library search order)",
                "correct": True,
                "rationale": (
                    "Correct. Exploiting an application's library search order so "
                    "that it loads an attacker-planted DLL from a writable "
                    "directory before the legitimate system library is DLL "
                    "side-loading, a form of memory injection that abuses trust in "
                    "a signed host process."
                ),
            },
            {
                "id": "b",
                "text": "Process hollowing",
                "correct": False,
                "rationale": (
                    "Incorrect. Process hollowing replaces the memory of an "
                    "already-running legitimate process with malicious code; this "
                    "scenario instead exploits the application's library-loading "
                    "search order at launch time, before the process even starts."
                ),
            },
            {
                "id": "c",
                "text": "Time-of-check to time-of-use (TOCTOU) race condition",
                "correct": False,
                "rationale": (
                    "Incorrect. No check-then-use timing gap is involved; the "
                    "application simply searches a predictable, writable location "
                    "first every time it loads, with no race required."
                ),
            },
            {
                "id": "d",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. No serialized object is being reconstructed from "
                    "untrusted data; the attack targets how the OS locates and "
                    "loads a DLL by name."
                ),
            },
        ],
        "explanation": (
            "Planting a malicious DLL where a trusted application will load it "
            "ahead of the legitimate library, due to an insecure search order, is "
            "DLL side-loading — a distinct memory-injection technique from "
            "process hollowing, which hijacks a process already in memory."
        ),
    },
    {
        "id": "nd2h-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "An application's auto-update client verifies that each downloaded "
            "update package carries a valid digital signature, but it accepts any "
            "signature chaining to a certificate present in the operating "
            "system's general trusted root store, rather than requiring the "
            "vendor's specific code-signing certificate. An attacker who obtains "
            "an unrelated, legitimately issued code-signing certificate from a "
            "different trusted CA signs a malicious package, which the client "
            "installs without warning. Which vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malicious update due to missing certificate pinning",
                "correct": True,
                "rationale": (
                    "Correct. Failing to pin the update mechanism to the "
                    "vendor's specific signing certificate — instead trusting any "
                    "certificate from the general trust store — allows a "
                    "maliciously signed update from an unrelated valid CA to be "
                    "accepted as legitimate."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No memory corruption or oversized input is "
                    "involved; the flaw is a validation gap in trusting any valid "
                    "certificate rather than the specific vendor certificate."
                ),
            },
            {
                "id": "c",
                "text": "Race condition (TOCTOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no timing gap between a check and a use; "
                    "the signature check runs correctly, it is simply not "
                    "specific enough to the vendor's actual certificate."
                ),
            },
            {
                "id": "d",
                "text": "Dependency confusion",
                "correct": False,
                "rationale": (
                    "Incorrect. Dependency confusion tricks a build system into "
                    "pulling a malicious package by name from a public registry "
                    "instead of an internal one; this scenario involves a signed "
                    "update package being wrongly trusted, not a package-resolution "
                    "namespace collision."
                ),
            },
        ],
        "explanation": (
            "When an update mechanism checks only that a signature is valid — "
            "rather than that it specifically matches the vendor's pinned "
            "certificate — any attacker holding any trusted CA-issued signing "
            "certificate can push a malicious update; this is the malicious "
            "update vulnerability class."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A front-end load balancer and a back-end application server "
            "disagree on how to parse a request containing both a "
            "Content-Length header and a Transfer-Encoding: chunked header. An "
            "attacker crafts a single request that the load balancer treats as "
            "one complete request but the back-end server treats as two, causing "
            "the smuggled second \"request\" to be prepended to the next "
            "legitimate user's traffic and returned in that user's response. "
            "Which vulnerability is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "HTTP request smuggling",
                "correct": True,
                "rationale": (
                    "Correct. Exploiting inconsistent parsing of "
                    "Content-Length/Transfer-Encoding between two devices in the "
                    "request path, so that a hidden request is smuggled and "
                    "processed against another user's connection, is the "
                    "definition of HTTP request smuggling."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF forces a victim's own browser to submit an "
                    "unwanted authenticated request; it does not involve "
                    "exploiting parsing disagreements between a proxy and a "
                    "back-end server."
                ),
            },
            {
                "id": "c",
                "text": "Open redirect",
                "correct": False,
                "rationale": (
                    "Incorrect. An open redirect abuses an application's "
                    "redirect logic to send users to an attacker-chosen "
                    "destination; it has nothing to do with conflicting request "
                    "framing between a proxy and origin server."
                ),
            },
            {
                "id": "d",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks the server into making its own "
                    "unintended outbound request; here the attacker's own inbound "
                    "request is being desynchronized and smuggled to affect other "
                    "users' traffic."
                ),
            },
        ],
        "explanation": (
            "Ambiguous parsing of Content-Length versus Transfer-Encoding "
            "between a front-end and back-end device, exploited to smuggle a "
            "hidden request into another user's response, is HTTP request "
            "smuggling."
        ),
    },
    {
        "id": "nd2h-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "An API's authentication library, when verifying a submitted JSON "
            "Web Token, honors the token's own \"alg\" header field. A tester "
            "crafts a token with \"alg\": \"none\" and an empty signature, sets "
            "the payload's role claim to \"admin,\" and the API accepts the token "
            "as valid, granting administrative access with no valid signature "
            "ever presented. Which vulnerability is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Broken authentication via insecure token signature validation",
                "correct": True,
                "rationale": (
                    "Correct. Allowing the token itself to declare that no "
                    "signature algorithm is used, and honoring that declaration, "
                    "lets an attacker forge arbitrary claims with no valid "
                    "signature at all — a critical broken-authentication flaw in "
                    "how the token is verified."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF relies on a victim's browser automatically "
                    "attaching valid session cookies to a forged request; here the "
                    "attacker directly crafts and submits their own forged token "
                    "with no victim involved."
                ),
            },
            {
                "id": "c",
                "text": "Insecure direct object reference (IDOR)",
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR involves accessing another user's object via "
                    "a predictable reference while otherwise properly "
                    "authenticated; here authentication itself is being forged "
                    "outright by manipulating the signature-algorithm field."
                ),
            },
            {
                "id": "d",
                "text": "Session fixation",
                "correct": False,
                "rationale": (
                    "Incorrect. Session fixation tricks a victim into using a "
                    "session identifier the attacker already knows; no existing "
                    "session is being fixed or reused here, a brand-new forged "
                    "token is being crafted from scratch."
                ),
            },
        ],
        "explanation": (
            "Trusting a token's self-declared \"none\" algorithm and skipping "
            "signature verification entirely is a broken-authentication flaw "
            "that lets an attacker forge any claim, including elevated roles, "
            "without ever holding a valid signing key."
        ),
    },
    {
        "id": "nd2h-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A penetration test against a support-ticketing application uncovers "
            "two findings. Finding 1: submitting \"admin'--\" as the username on "
            "the login form authenticates the tester without ever supplying a "
            "valid password. Finding 2: setting the account's display name field "
            "to \"<img src=x onerror=alert(document.cookie)>\" causes that script "
            "to execute in the browser of every support agent who later opens any "
            "ticket showing that display name. Which TWO statements about these "
            "findings are accurate? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Finding 1 succeeds because attacker-supplied input alters "
                    "the structure of a backend database query"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A username like \"admin'--\" is a classic SQL "
                    "injection payload that comments out the password check, "
                    "altering the query's logical structure rather than merely "
                    "supplying a value."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Finding 2's payload persists in stored data and executes "
                    "for any user who later views it, without requiring them to "
                    "click a crafted link"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the payload is saved in the display name "
                    "and runs automatically for every agent who opens an "
                    "affected ticket, this is stored XSS — no victim interaction "
                    "with a malicious link is required."
                ),
            },
            {
                "id": "c",
                "text": "Finding 1's payload executes JavaScript in other users' browsers",
                "correct": False,
                "rationale": (
                    "Incorrect. Finding 1 manipulates a server-side SQL query to "
                    "bypass authentication; it does not inject or execute any "
                    "client-side script in another user's browser."
                ),
            },
            {
                "id": "d",
                "text": "Finding 2 requires the attacker to already hold a valid session cookie",
                "correct": False,
                "rationale": (
                    "Incorrect. Setting the display name and having the stored "
                    "payload later execute in other users' sessions requires no "
                    "session cookie belonging to those other users; the attacker "
                    "only needs to be able to save the malicious display name."
                ),
            },
        ],
        "explanation": (
            "Finding 1 is SQL injection because it manipulates the backend "
            "query's logic, while Finding 2 is stored XSS because the payload "
            "persists and runs automatically for later viewers — neither "
            "involves the other's mechanism (client-side script execution or "
            "cookie theft, respectively)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "Company-issued phones near a specific downtown intersection "
            "intermittently drop from LTE to an unencrypted, decades-old cellular "
            "protocol and exhibit unusual battery drain during the transition. "
            "Security researchers determine the devices are being forced to "
            "connect to a portable, unauthorized base station positioned nearby. "
            "Which attack MOST likely explains this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rogue cell tower / IMSI catcher (protocol downgrade)",
                "correct": True,
                "rationale": (
                    "Correct. A portable fake base station that forces nearby "
                    "phones to downgrade to an older, unencrypted cellular "
                    "protocol so their traffic can be intercepted is the classic "
                    "IMSI-catcher (rogue cell tower) attack."
                ),
            },
            {
                "id": "b",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping is a carrier-side account takeover "
                    "that ports a victim's number to an attacker's SIM; it does "
                    "not require physical proximity or cause a forced protocol "
                    "downgrade at a specific location."
                ),
            },
            {
                "id": "c",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing is unauthorized data access over a "
                    "short-range Bluetooth connection; it has no relationship to "
                    "cellular network protocol selection."
                ),
            },
            {
                "id": "d",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreaking is a deliberate, on-device "
                    "modification of OS restrictions; it does not explain phones "
                    "downgrading network protocol only near one physical "
                    "location."
                ),
            },
        ],
        "explanation": (
            "A geographically localized, forced downgrade to an insecure "
            "cellular protocol is the signature of a rogue cell tower/IMSI "
            "catcher intercepting nearby devices."
        ),
    },
    {
        "id": "nd2h-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A free \"battery saver\" app downloaded from the official app store "
            "requests and is granted a VPN configuration profile permission "
            "during setup. Analysis later shows the app routes all of the "
            "device's HTTPS traffic through a remote proxy server, which decrypts "
            "and logs plaintext content before re-encrypting and forwarding it. "
            "Which vulnerability does this MOST closely describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malicious VPN profile enabling on-device traffic interception",
                "correct": True,
                "rationale": (
                    "Correct. An app abusing a granted VPN profile permission to "
                    "route and decrypt all of a device's traffic through an "
                    "attacker-controlled proxy is a malicious VPN profile attack, "
                    "effectively an on-device man-in-the-middle position."
                ),
            },
            {
                "id": "b",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping redirects a phone number to a new "
                    "SIM at the carrier level; it has nothing to do with an "
                    "app-level VPN profile intercepting HTTPS traffic."
                ),
            },
            {
                "id": "c",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking sends unsolicited messages over a "
                    "short-range Bluetooth connection; it does not involve "
                    "traffic interception via a VPN configuration."
                ),
            },
            {
                "id": "d",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. The device's OS restrictions were never removed; "
                    "the app abused a legitimately granted VPN permission within "
                    "the normal app sandbox, not a jailbreak."
                ),
            },
        ],
        "explanation": (
            "An app that leverages a granted VPN profile permission to route and "
            "decrypt all outbound traffic through an attacker-controlled proxy "
            "is exploiting the mobile VPN-profile permission model to conduct "
            "on-device interception, distinct from carrier-level SIM attacks or "
            "OS jailbreaking."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A cloud provider's incident response team finds that a customer's "
            "compromised VM exploited a flaw in the hypervisor's paravirtualized "
            "network driver to execute code with hypervisor-level privileges, then "
            "used that access to read memory belonging to a neighboring tenant's "
            "VM running on the same physical host. Which vulnerability does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM escape",
                "correct": True,
                "rationale": (
                    "Correct. Exploiting a hypervisor component from inside a "
                    "guest to gain hypervisor-level code execution and breach "
                    "isolation between co-resident VMs is the definition of a VM "
                    "escape, regardless of which specific hypervisor component "
                    "(here, the paravirtualized network driver) was the entry "
                    "point."
                ),
            },
            {
                "id": "b",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. VM sprawl describes an operational hygiene "
                    "problem of unmanaged, forgotten VMs accumulating over time, "
                    "not an active exploit breaching isolation between two "
                    "running VMs."
                ),
            },
            {
                "id": "c",
                "text": "Resource reuse (data remnants)",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse concerns leftover data in shared "
                    "physical resources reassigned after deallocation; this "
                    "scenario describes an active exploit against a running "
                    "driver, not residual data on recycled storage."
                ),
            },
            {
                "id": "d",
                "text": "Live migration hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. This targets the process of moving a running VM "
                    "between hosts; the exploit here occurred against a network "
                    "driver on a VM that was not being migrated."
                ),
            },
        ],
        "explanation": (
            "Any exploit that lets a guest VM execute code at the hypervisor "
            "level and breach isolation from a co-resident tenant — whether via "
            "an emulated device, a paravirtualized driver, or another hypervisor "
            "component — is classified as a VM escape."
        ),
    },
    {
        "id": "nd2h-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "An internal cloud audit finds 340 running virtual machines in a "
            "private cloud environment. Of those, 95 have no assigned owner in "
            "the CMDB, have not been patched in over 14 months, and several run "
            "software versions that reached end-of-life last year. Which "
            "virtualization issue does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM sprawl",
                "correct": True,
                "rationale": (
                    "Correct. An uncontrolled accumulation of unmanaged, "
                    "unowned, unpatched VMs with no tracking in asset management "
                    "is the definition of VM sprawl."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. No isolation-breaching exploit between a guest "
                    "and the hypervisor is described here; this is a governance "
                    "and asset-management failure, not an active attack."
                ),
            },
            {
                "id": "c",
                "text": "Hyperjacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Hyperjacking involves installing a rogue "
                    "hypervisor beneath the legitimate one; nothing here "
                    "describes a malicious hypervisor, only unmanaged, "
                    "unpatched, ownerless VMs."
                ),
            },
            {
                "id": "d",
                "text": "Resource reuse (data remnants)",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse concerns leftover data on "
                    "physical storage reassigned to a new VM; this scenario "
                    "describes VMs that are still running and simply "
                    "unmanaged, not data remnants from decommissioned storage."
                ),
            },
        ],
        "explanation": (
            "Uncontrolled proliferation of forgotten, unowned, unpatched VMs "
            "that fall outside normal asset-management and patching processes is "
            "VM sprawl, an operational risk distinct from an active exploit like "
            "VM escape."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A network vulnerability scan reports zero findings on a newly "
            "imaged public-facing web server. Three months later, a source-code "
            "review discovers a critical injection flaw that has been present in "
            "the deployed code since the server's first day online, and that same "
            "flaw is confirmed to have been exploited during a breach the "
            "following week. How should the original scan result be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False negative",
                "correct": True,
                "rationale": (
                    "Correct. A real, exploitable vulnerability existed in the "
                    "code at the time of the scan but the scan failed to detect "
                    "and report it — the definition of a false negative."
                ),
            },
            {
                "id": "b",
                "text": "False positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A false positive is an incorrectly reported "
                    "vulnerability that turns out not to be real; here the "
                    "opposite occurred — a genuine vulnerability went entirely "
                    "unreported."
                ),
            },
            {
                "id": "c",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative requires that no vulnerability "
                    "actually exists; here a critical, later-exploited "
                    "vulnerability was present in the code all along, making the "
                    "silent scan result an error rather than an accurate "
                    "negative."
                ),
            },
            {
                "id": "d",
                "text": "Indicator of compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. An indicator of compromise is forensic evidence "
                    "of an actual breach; the question asks how to classify the "
                    "earlier scan's accuracy, not the later breach evidence "
                    "itself."
                ),
            },
        ],
        "explanation": (
            "A scan that reports no findings for a vulnerability that was "
            "genuinely present and later exploited is a false negative — the "
            "scanner's detection logic (likely dynamic, network-based scanning "
            "that cannot see application-layer injection flaws in source code) "
            "simply missed it."
        ),
    },
    {
        "id": "nd2h-019",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A vulnerability scanner flags a \"high\" severity outdated jQuery "
            "library file on a marketing website. A developer confirms the file "
            "is genuinely present and genuinely outdated, but web server access "
            "logs show zero requests to that specific file path over the past 90 "
            "days, and no page on the live site references or loads it — it is "
            "orphaned, dead code left over from a prior redesign. How should this "
            "finding be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False positive",
                "correct": True,
                "rationale": (
                    "Correct. Although the vulnerable file genuinely exists and "
                    "is genuinely outdated, it is never loaded or reachable by any "
                    "user or page, so it presents no actual exploitable risk — "
                    "making the \"high severity, exploitable\" finding a false "
                    "positive in practice."
                ),
            },
            {
                "id": "b",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A true positive requires the flagged issue to be "
                    "both present and actually reachable/exploitable; access logs "
                    "confirm the file is never loaded by any live page, so there "
                    "is no real exploitation path."
                ),
            },
            {
                "id": "c",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative describes a real vulnerability "
                    "the scanner failed to report; here the scanner did report "
                    "the file, it simply overstated the risk since the file is "
                    "unreachable."
                ),
            },
            {
                "id": "d",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative applies when nothing is reported "
                    "and nothing exists to find; here the scanner did generate a "
                    "finding, which then needed manual verification to determine "
                    "its real-world impact."
                ),
            },
        ],
        "explanation": (
            "A technically accurate file-presence finding that carries no "
            "real-world exploitability, because the file is unreachable dead "
            "code, is still classified as a false positive — the vulnerability "
            "the scanner is warning about does not actually exist in practice."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Network detection tooling flags a workstation whose outbound HTTPS "
            "connections each present a self-signed certificate with a different, "
            "randomly generated Subject Common Name on every connection attempt. "
            "The TLS client handshake fingerprint (JA3) matches a signature "
            "previously associated with a known malware command-and-control "
            "framework. Which indicator does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malicious traffic pattern / C2 fingerprint anomaly",
                "correct": True,
                "rationale": (
                    "Correct. Constantly rotating self-signed certificate "
                    "identities combined with a TLS handshake fingerprint "
                    "matching known malware C2 tooling is a strong network-based "
                    "indicator of malicious command-and-control traffic, "
                    "independent of any timing pattern."
                ),
            },
            {
                "id": "b",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel refers to authentication "
                    "events from geographically incompatible locations, not "
                    "outbound TLS certificate and handshake characteristics."
                ),
            },
            {
                "id": "c",
                "text": "Resource consumption anomaly",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no mention of abnormal CPU, memory, or "
                    "bandwidth usage; the indicator here is the certificate and "
                    "TLS fingerprint characteristics of the connections "
                    "themselves."
                ),
            },
            {
                "id": "d",
                "text": "Concurrent session usage",
                "correct": False,
                "rationale": (
                    "Incorrect. This indicator involves a single account being "
                    "used in multiple simultaneous sessions; the scenario "
                    "instead describes characteristics of outbound network "
                    "traffic, unrelated to session concurrency."
                ),
            },
        ],
        "explanation": (
            "Randomized, rotating certificate identities paired with a TLS "
            "fingerprint matching known malware infrastructure is a network "
            "traffic-based indicator of command-and-control activity, distinct "
            "from account-based indicators like impossible travel or concurrent "
            "sessions."
        ),
    },
    {
        "id": "nd2h-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A SIEM alert shows a service account that authentication logs "
            "confirm has never performed an interactive logon in over two years "
            "of history suddenly initiating an interactive RDP session directly "
            "to a domain controller. Which indicator does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Anomalous account behavior (atypical use of a service account)",
                "correct": True,
                "rationale": (
                    "Correct. A service account behaving in a way that is "
                    "completely inconsistent with its established, years-long "
                    "usage baseline — performing an interactive human-style logon "
                    "instead of its normal automated function — is a strong "
                    "behavioral anomaly indicator."
                ),
            },
            {
                "id": "b",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel specifically refers to two "
                    "successful logins from geographically distant locations "
                    "within an implausible timeframe; no location or timing "
                    "conflict is described here."
                ),
            },
            {
                "id": "c",
                "text": "Blocked content indicator",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no mention of content being flagged or "
                    "blocked by security tooling; the anomaly is the account's "
                    "sudden, uncharacteristic type of authentication activity."
                ),
            },
            {
                "id": "d",
                "text": "Resource consumption anomaly",
                "correct": False,
                "rationale": (
                    "Incorrect. No abnormal CPU, memory, or bandwidth usage is "
                    "described; the indicator is a behavioral deviation in how "
                    "the account is being used, not system resource usage."
                ),
            },
        ],
        "explanation": (
            "A service account departing sharply from its long-established "
            "behavioral baseline — logging in interactively for the first time "
            "ever, to a high-value target like a domain controller — is a "
            "classic anomalous account behavior indicator of compromise."
        ),
    },
    {
        "id": "nd2h-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A SOC analyst reconstructs the following endpoint timeline: "
            "winword.exe spawns powershell.exe, which then launches psexec.exe "
            "and initiates outbound connections to eleven other internal hosts "
            "within three minutes; on each of those hosts, a new local "
            "administrator account named \"svc_update\" is created moments after "
            "the connection lands. Which TWO findings are the strongest "
            "indicators that this is malicious lateral movement rather than "
            "routine IT administration? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An office document application (winword.exe) spawning a "
                    "scripting engine, which then spawns a remote-execution tool"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A document viewer/editor has no legitimate reason "
                    "to spawn PowerShell, which then launches a remote-"
                    "execution tool; this parent-child process chain is a strong "
                    "sign of an exploited document delivering a payload."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The identical new local administrator account being "
                    "created on multiple hosts within minutes of each new "
                    "connection"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rapidly and uniformly creating the same new "
                    "privileged account across many hosts in a tight time window "
                    "is a well-known persistence/lateral-movement pattern that "
                    "routine, planned administration would not produce."
                ),
            },
            {
                "id": "c",
                "text": "The activity used PowerShell, a legitimate administrative tool",
                "correct": False,
                "rationale": (
                    "Incorrect. PowerShell is used constantly for legitimate "
                    "system administration; its mere presence, without the "
                    "surrounding suspicious process chain and account creation "
                    "pattern, is not itself a distinguishing indicator."
                ),
            },
            {
                "id": "d",
                "text": "The connections occurred within a three-minute window",
                "correct": False,
                "rationale": (
                    "Incorrect. Speed alone is not the deciding factor — "
                    "automated legitimate deployment tools can also act quickly; "
                    "it is the anomalous process ancestry and identical account "
                    "creation across hosts that make this activity malicious."
                ),
            },
        ],
        "explanation": (
            "The suspicious parent-child process chain (document app spawning a "
            "shell spawning a remote-execution tool) and the uniform creation of "
            "an identical new admin account across many hosts are the strongest "
            "indicators of malicious lateral movement; the tool used and the "
            "raw speed of the activity are not, by themselves, distinguishing."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "A free browser toolbar injects unwanted banner advertisements into "
            "every webpage a user visits and silently redirects all search-bar "
            "queries to a monetized third-party search engine. Forensic review "
            "finds no keystroke logging, credential theft, or covert data "
            "exfiltration — only the ad injection and search hijacking. Which "
            "malware type BEST describes this software?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Adware",
                "correct": True,
                "rationale": (
                    "Correct. Software whose primary behavior is generating "
                    "unwanted advertising revenue — through ad injection and "
                    "search-query hijacking — without covert data theft, is "
                    "adware."
                ),
            },
            {
                "id": "b",
                "text": "Spyware",
                "correct": False,
                "rationale": (
                    "Incorrect. Spyware's defining trait is covertly monitoring "
                    "and exfiltrating a user's data or activity; the forensic "
                    "review explicitly found no keystroke logging or data theft, "
                    "only ad injection and search hijacking."
                ),
            },
            {
                "id": "c",
                "text": "Keylogger",
                "correct": False,
                "rationale": (
                    "Incorrect. A keylogger specifically records keystrokes; "
                    "this toolbar's behavior is limited to ad injection and "
                    "redirecting search queries, with no keystroke capture "
                    "found."
                ),
            },
            {
                "id": "d",
                "text": "Bot (botnet membership)",
                "correct": False,
                "rationale": (
                    "Incorrect. Bot malware checks in with a remote "
                    "command-and-control channel to receive attacker "
                    "instructions; this toolbar operates independently to inject "
                    "ads, with no described C2 channel or remote tasking."
                ),
            },
        ],
        "explanation": (
            "Software whose sole malicious behavior is unwanted advertising "
            "injection and search hijacking, without covert monitoring or data "
            "theft, is classified as adware rather than spyware."
        ),
    },
    {
        "id": "nd2h-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Security researchers find that thousands of infected smart cameras, "
            "routers, and a handful of workstations across unrelated networks "
            "periodically check in to a rotating list of command channels and, on "
            "receiving a signal, simultaneously flood an unrelated third-party "
            "target with traffic. No single attacker has interactive, real-time "
            "control of any individual device. Which malware classification BEST "
            "fits these infected devices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bot (member of a botnet)",
                "correct": True,
                "rationale": (
                    "Correct. Devices that check in to a command-and-control "
                    "channel and act on batch instructions as part of a "
                    "large, coordinated group — without an individual attacker "
                    "interactively controlling any single device — are bots "
                    "operating within a botnet."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm's defining trait is self-propagation "
                    "across a network by exploiting vulnerabilities; this "
                    "scenario centers on coordinated, centrally tasked flooding "
                    "behavior across already-infected devices, not the "
                    "propagation mechanism itself."
                ),
            },
            {
                "id": "c",
                "text": "Remote access trojan (RAT)",
                "correct": False,
                "rationale": (
                    "Incorrect. A RAT gives one attacker interactive, hands-on "
                    "remote control of a single infected machine; here devices "
                    "act on batch commands as part of a coordinated group, with "
                    "no interactive per-device control described."
                ),
            },
            {
                "id": "d",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is dormant code triggered by a "
                    "pre-set local condition on one system; this scenario "
                    "describes networked devices actively receiving external "
                    "commands from a rotating C2 infrastructure, not a "
                    "self-contained dormant trigger."
                ),
            },
        ],
        "explanation": (
            "Devices that check in with a command-and-control channel and act "
            "on batched instructions as part of a large coordinated group are "
            "bots/botnet members, distinct from a self-propagating worm or an "
            "attacker's individually operated RAT session."
        ),
    },
    {
        "id": "nd2h-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types",
        "stem": (
            "A forensic examiner finds that a malicious PowerShell payload is "
            "stored entirely as a Base64-encoded blob inside a registry Run-key "
            "value. At every user login, the OS automatically decodes and "
            "executes the payload directly in memory; no corresponding "
            "executable or script file has ever existed anywhere on the disk. "
            "Which malware type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fileless malware",
                "correct": True,
                "rationale": (
                    "Correct. Malware whose payload lives entirely in the "
                    "registry (or memory) and is decoded and executed without "
                    "ever being written to disk as a file is fileless malware."
                ),
            },
            {
                "id": "b",
                "text": "Bootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A bootkit persists by infecting the Master Boot "
                    "Record or firmware to load before the OS itself; this "
                    "payload instead runs after login via a standard registry "
                    "auto-run key, not the boot process."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb triggers on a specific pre-set "
                    "condition (such as a date); this payload instead executes "
                    "on every single login, not a one-time or condition-based "
                    "trigger."
                ),
            },
            {
                "id": "d",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan's defining trait is disguising itself "
                    "as legitimate software to trick a user into installing it; "
                    "this scenario centers on where and how the payload persists "
                    "and executes (registry, memory-only), not on deceptive "
                    "packaging."
                ),
            },
        ],
        "explanation": (
            "Persistence via an encoded registry value that is decoded and run "
            "purely in memory, with no file ever written to disk, is the "
            "defining trait of fileless malware, distinct from disk/boot-"
            "persistent bootkits or condition-triggered logic bombs."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "A web application assigns each authenticated user a sequential, "
            "incrementing numeric session identifier. A tester logs in, notes "
            "their own session ID, increments it by one, and submits it as a "
            "cookie value — successfully assuming another user's currently "
            "active session without ever capturing that user's traffic. Which "
            "attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Session hijacking via predictable session identifiers",
                "correct": True,
                "rationale": (
                    "Correct. Guessing or deriving another user's valid session "
                    "identifier because identifiers are generated predictably "
                    "(sequential numbers) and then using it to assume that "
                    "session is session hijacking through predictable/weak "
                    "session ID generation."
                ),
            },
            {
                "id": "b",
                "text": "ARP poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning manipulates Layer 2 address "
                    "mappings to intercept traffic; no packet capture or "
                    "network-layer manipulation occurred here, only prediction "
                    "of an application-layer identifier."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks a victim's own browser into "
                    "submitting a forged request using the victim's legitimate "
                    "session; here the attacker directly assumes the victim's "
                    "session by guessing its identifier, not by forging a "
                    "request through the victim's browser."
                ),
            },
            {
                "id": "d",
                "text": "On-path (man-in-the-middle) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No traffic interception occurred; the tester "
                    "never captured the victim's session ID, they derived it "
                    "purely by predicting the next value in a sequential "
                    "pattern."
                ),
            },
        ],
        "explanation": (
            "When session identifiers are generated in a predictable, "
            "sequential pattern, an attacker can derive a valid session for "
            "another user without any traffic interception — a session-"
            "hijacking attack rooted in weak session ID generation."
        ),
    },
    {
        "id": "nd2h-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "A penetration tester runs a tool on an internal segment that "
            "listens for and responds to broadcast name-resolution requests "
            "(LLMNR/NBT-NS) sent by workstations when normal DNS lookups fail. "
            "The tool's forged responses cause several workstations to attempt "
            "NTLM authentication directly to the tester's laptop, which captures "
            "and relays the credentials. Which attack technique is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "LLMNR/NBT-NS poisoning",
                "correct": True,
                "rationale": (
                    "Correct. Responding to legacy fallback name-resolution "
                    "broadcasts (LLMNR/NBT-NS) with a forged answer, so that "
                    "victims send their NTLM authentication attempt straight to "
                    "the attacker, is the defining pattern of LLMNR/NBT-NS "
                    "poisoning."
                ),
            },
            {
                "id": "b",
                "text": "DNS cache poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS cache poisoning corrupts a DNS resolver's "
                    "cached records; here no DNS server is targeted at all — "
                    "the attack exploits the legacy local broadcast "
                    "fallback protocols used only when standard DNS fails."
                ),
            },
            {
                "id": "c",
                "text": "BGP hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. BGP hijacking manipulates internet-scale "
                    "routing announcements between autonomous systems; this "
                    "attack is confined to a single local network segment "
                    "exploiting a name-resolution fallback protocol."
                ),
            },
            {
                "id": "d",
                "text": "STP manipulation",
                "correct": False,
                "rationale": (
                    "Incorrect. Spanning Tree Protocol manipulation abuses "
                    "bridge election to redirect switching topology; no BPDU "
                    "frames or switching topology changes are described in this "
                    "scenario."
                ),
            },
        ],
        "explanation": (
            "Forging responses to LLMNR/NBT-NS fallback name-resolution "
            "broadcasts to capture or relay NTLM authentication attempts is "
            "LLMNR/NBT-NS poisoning, a common on-path credential-harvesting "
            "technique distinct from DNS-server, BGP, or Layer-2 switching "
            "attacks."
        ),
    },
    {
        "id": "nd2h-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A public-facing web server becomes unresponsive to new users. "
            "Server logs show hundreds of connections held open by clients that "
            "each sent only a partial HTTP request header and then paused, "
            "periodically trickling in one additional byte just often enough to "
            "keep the connection from timing out. Overall inbound bandwidth "
            "remains negligible throughout the incident. Which attack MOST "
            "likely explains this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Application-layer denial-of-service (slow HTTP attack)",
                "correct": True,
                "rationale": (
                    "Correct. Deliberately sending incomplete HTTP requests very "
                    "slowly to exhaust the server's limited pool of open "
                    "connections, without generating meaningful bandwidth, is a "
                    "slow HTTP (application-layer) denial-of-service attack."
                ),
            },
            {
                "id": "b",
                "text": "SYN flood",
                "correct": False,
                "rationale": (
                    "Incorrect. A SYN flood exhausts resources with a high "
                    "volume of TCP SYN packets that never complete the "
                    "handshake, typically producing significant bandwidth and "
                    "packet volume; here connections do complete the TCP "
                    "handshake and bandwidth stays negligible."
                ),
            },
            {
                "id": "c",
                "text": "Amplified reflection DDoS (e.g., DNS/NTP amplification)",
                "correct": False,
                "rationale": (
                    "Incorrect. Amplification attacks abuse third-party servers "
                    "to generate a large volume of inbound traffic from spoofed "
                    "requests; this scenario shows negligible bandwidth from "
                    "direct client connections, not a volumetric reflected flood."
                ),
            },
            {
                "id": "d",
                "text": "ARP poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning is a Layer 2 on-path technique for "
                    "intercepting traffic on a local segment; it has no "
                    "relationship to a web server's connection pool being "
                    "exhausted by slow, incomplete HTTP requests."
                ),
            },
        ],
        "explanation": (
            "Exhausting a server's connection pool with deliberately slow, "
            "incomplete requests and minimal bandwidth is a slow HTTP "
            "application-layer DoS attack, distinct from the high-volume "
            "network-layer SYN flood or amplification attacks."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A contractor without a valid badge approaches a secure entrance and "
            "asks a badge-holding employee to let them in. The employee, "
            "recognizing the contractor from prior visits, deliberately holds the "
            "door open and waves them through without checking whether the "
            "contractor's badge is currently active. Which physical security "
            "term BEST describes this incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Piggybacking",
                "correct": True,
                "rationale": (
                    "Correct. Piggybacking occurs when an authorized person "
                    "knowingly and willingly allows an unauthorized individual "
                    "to enter with them — as opposed to the unauthorized person "
                    "sneaking in without the badge-holder's knowledge."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating specifically describes an "
                    "unauthorized person following an authorized person through "
                    "a door without that person's knowledge or consent; here the "
                    "employee knowingly and deliberately let the contractor in, "
                    "which is piggybacking, not tailgating."
                ),
            },
            {
                "id": "c",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving involves searching discarded "
                    "trash for sensitive information; no discarded materials are "
                    "involved in this door-access scenario."
                ),
            },
            {
                "id": "d",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing is covertly observing someone "
                    "entering credentials or sensitive information; this "
                    "scenario involves physical access through a door, not "
                    "observation of input."
                ),
            },
        ],
        "explanation": (
            "The key distinction is consent and awareness: piggybacking is "
            "knowing, willing complicity by the badge holder, while tailgating "
            "is unauthorized entry the badge holder is unaware of."
        ),
    },
    {
        "id": "nd2h-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "During routine maintenance, a technician discovers a thin, "
            "battery-powered overlay fitted precisely over the card slot of a "
            "retail store's point-of-sale terminal. The overlay silently records "
            "the magnetic-stripe data of every payment card swiped through it "
            "and is nearly indistinguishable from the terminal's factory card "
            "reader. Which physical attack does this device represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Card skimming",
                "correct": True,
                "rationale": (
                    "Correct. A concealed overlay device attached to a card "
                    "reader that captures magnetic-stripe data from every card "
                    "swiped is a card skimmer — a classic payment card skimming "
                    "attack."
                ),
            },
            {
                "id": "b",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing is direct visual observation of "
                    "someone entering data; this attack instead uses a physical "
                    "hardware device to electronically capture card data, with "
                    "no observation involved."
                ),
            },
            {
                "id": "c",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving involves retrieving discarded "
                    "physical documents or media; no discarded materials are "
                    "involved in a covert card-reader overlay device."
                ),
            },
            {
                "id": "d",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating is unauthorized physical entry by "
                    "following an authorized person through a door; it has "
                    "nothing to do with capturing payment card data from a "
                    "compromised terminal."
                ),
            },
        ],
        "explanation": (
            "A concealed device physically attached to a card reader that "
            "captures magnetic-stripe data from every swipe is card skimming, a "
            "physical attack distinct from observation-based (shoulder "
            "surfing) or access-based (tailgating) techniques."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "Authentication logs show a single external IP address attempting "
            "the exact same password, \"Winter2026!\", against 3,000 different "
            "employee usernames over several days, submitting only one or two "
            "attempts per account per day to stay under the account lockout "
            "threshold. Which attack technique does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Password spraying",
                "correct": True,
                "rationale": (
                    "Correct. Trying one (or a small number of) common "
                    "passwords across a large number of different accounts, "
                    "deliberately staying below the lockout threshold per "
                    "account, is the defining pattern of password spraying."
                ),
            },
            {
                "id": "b",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing uses previously breached, "
                    "unique username/password pairs obtained from other sites; "
                    "here every attempt uses the identical single password "
                    "against many different usernames, not distinct known-valid "
                    "pairs."
                ),
            },
            {
                "id": "c",
                "text": "Brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A brute-force attack rapidly tries many "
                    "different passwords against one specific account; here the "
                    "opposite pattern occurs — one password is tried sparingly "
                    "across many different accounts."
                ),
            },
            {
                "id": "d",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A rainbow table attack cracks captured password "
                    "hashes offline using precomputed lookup tables; this "
                    "scenario describes live login attempts against "
                    "authentication logs, not offline hash cracking."
                ),
            },
        ],
        "explanation": (
            "Using one common password against many different accounts, at a "
            "low per-account rate specifically to evade lockout thresholds, is "
            "password spraying — distinct from credential stuffing (unique "
            "known pairs) and brute force (many passwords against one account)."
        ),
    },
    {
        "id": "nd2h-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A laptop's capacitive fingerprint reader is configured without "
            "pulse or conductivity liveness detection. A colleague lifts a "
            "latent fingerprint left on a glass surface, molds it in gelatin, "
            "and successfully unlocks the laptop by pressing the mold against "
            "the sensor. Which concept does this attack MOST directly exploit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A biometric presentation attack exploiting missing liveness detection",
                "correct": True,
                "rationale": (
                    "Correct. Presenting a fabricated replica of a biometric "
                    "characteristic — here, a molded fingerprint — to defeat a "
                    "sensor that lacks liveness/anti-spoofing checks is a "
                    "biometric presentation attack, and it is the missing "
                    "liveness detection that makes it succeed."
                ),
            },
            {
                "id": "b",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing involves reusing breached "
                    "username/password pairs against login forms; no passwords "
                    "or credential pairs are involved in spoofing a biometric "
                    "sensor with a fabricated fingerprint."
                ),
            },
            {
                "id": "c",
                "text": "MFA fatigue (push bombing)",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA fatigue involves overwhelming a user with "
                    "repeated push notifications until they approve one out of "
                    "annoyance; this scenario involves directly spoofing a "
                    "biometric sensor with a physical fake, with no push "
                    "notifications involved."
                ),
            },
            {
                "id": "d",
                "text": "Session replay attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Session replay reuses a previously captured "
                    "valid session token; this attack instead directly deceives "
                    "the physical sensor into granting a brand-new "
                    "authentication event with a fake fingerprint."
                ),
            },
        ],
        "explanation": (
            "Fabricating a physical replica of a biometric characteristic to "
            "fool a sensor that lacks liveness/anti-spoofing detection is a "
            "biometric presentation attack — a factor-specific weakness "
            "distinct from credential-based or session-based attacks."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A database stores password hashes using a modern, slow hashing "
            "algorithm combined with a salt — but a code review reveals the "
            "application uses the exact same hardcoded salt value for every "
            "single user account rather than generating a unique, random salt "
            "per user. An attacker who precomputes a rainbow table for that one "
            "known salt value can instantly crack every account's hash "
            "simultaneously. Which weakness is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Static/shared salt reuse defeating the purpose of salting",
                "correct": True,
                "rationale": (
                    "Correct. Salting only defeats precomputed rainbow tables "
                    "when each user's salt is unique and random; a single salt "
                    "shared across every account lets an attacker precompute one "
                    "table that cracks all accounts at once, effectively "
                    "nullifying the salt's protection."
                ),
            },
            {
                "id": "b",
                "text": "Unsalted hash storage",
                "correct": False,
                "rationale": (
                    "Incorrect. A salt is genuinely present and applied to "
                    "every hash; the flaw is that the same salt value is reused "
                    "for all users rather than being generated uniquely per "
                    "account, not that salting was omitted entirely."
                ),
            },
            {
                "id": "c",
                "text": "Padding oracle vulnerability",
                "correct": False,
                "rationale": (
                    "Incorrect. A padding oracle exploits distinguishable error "
                    "responses during decryption to recover plaintext "
                    "incrementally; this scenario involves offline hash "
                    "cracking via a reused salt, not a decryption error side "
                    "channel."
                ),
            },
            {
                "id": "d",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A downgrade attack forces a weaker protocol or "
                    "cipher to be negotiated; this scenario involves a "
                    "structural flaw in how salts are generated and applied, not "
                    "a forced protocol/algorithm negotiation."
                ),
            },
        ],
        "explanation": (
            "Salting only defeats precomputed attacks when each salt is unique "
            "per user; reusing one static salt across every account lets an "
            "attacker build a single rainbow table that compromises the entire "
            "user base at once, distinct from having no salt at all."
        ),
    },
    {
        "id": "nd2h-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A legacy application encrypts multiple different outbound messages "
            "using the RC4 stream cipher with the same static key and no "
            "per-message nonce or IV. An analyst intercepts two ciphertexts sent "
            "close together, XORs them against each other, and — without ever "
            "recovering the key itself — derives the XOR of the two original "
            "plaintexts, ultimately reconstructing readable fragments of both "
            "messages. Which cryptographic weakness is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Stream cipher keystream reuse (two-time pad attack)",
                "correct": True,
                "rationale": (
                    "Correct. Reusing the identical key (and thus the identical "
                    "keystream) to encrypt more than one message with a stream "
                    "cipher allows an attacker to XOR the ciphertexts together "
                    "and recover the XOR of the plaintexts — the classic "
                    "two-time pad weakness."
                ),
            },
            {
                "id": "b",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack exploits the mathematics of "
                    "hash collisions to find two inputs producing the same "
                    "digest; this scenario involves reused stream-cipher "
                    "keystream material, not hash collisions."
                ),
            },
            {
                "id": "c",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Rainbow tables crack password hashes using "
                    "precomputed lookup tables; this scenario involves live "
                    "traffic encrypted with a reused stream-cipher key, not "
                    "hashed password storage."
                ),
            },
            {
                "id": "d",
                "text": "Padding oracle attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A padding oracle attack exploits distinguishable "
                    "error messages from a block-cipher decryption process; this "
                    "scenario involves a stream cipher and requires no oracle or "
                    "error-message feedback at all, only the two intercepted "
                    "ciphertexts themselves."
                ),
            },
        ],
        "explanation": (
            "Reusing the same key/keystream to encrypt multiple messages with a "
            "stream cipher lets an attacker XOR intercepted ciphertexts to "
            "recover plaintext relationships without ever needing the key — the "
            "well-known two-time pad weakness."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "A firewall log confirms a workstation connected to a known-"
            "malicious IP address at 14:32:07, but the firewall only records "
            "source/destination IP addresses and ports — no username. "
            "Investigators need to determine exactly which employee was logged "
            "into that workstation at that precise moment. Which log source "
            "should they consult next?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The workstation's authentication/security event log",
                "correct": True,
                "rationale": (
                    "Correct. Endpoint authentication logs record logon and "
                    "logoff events tied to specific usernames and timestamps, "
                    "letting investigators correlate the malicious connection's "
                    "exact time with the user who was logged in at that moment."
                ),
            },
            {
                "id": "b",
                "text": "DNS query logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs record which domain names were "
                    "resolved and by which source IP; they do not identify "
                    "which specific user was logged into a shared workstation "
                    "at a given time."
                ),
            },
            {
                "id": "c",
                "text": "DHCP lease logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs map an IP address to a device's MAC "
                    "address and lease time, not to the identity of the human "
                    "user logged into that device."
                ),
            },
            {
                "id": "d",
                "text": "NetFlow/flow-record logs",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow records traffic volume and connection "
                    "metadata between IP addresses and ports; like the firewall "
                    "log, it carries no username attribution."
                ),
            },
        ],
        "explanation": (
            "To attribute network activity on a shared endpoint to a specific "
            "individual, investigators need the endpoint's own authentication/"
            "security event log, which records logon sessions by username and "
            "timestamp — information that firewall, DNS, DHCP, and NetFlow logs "
            "do not provide."
        ),
    },
    {
        "id": "nd2h-036",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "Incident responders confirmed which endpoint was compromised based "
            "on a single antivirus detection alert. They now need a detailed "
            "list of every file created or modified and every registry key "
            "touched during the malware's execution window, in order to build "
            "indicators of compromise for the rest of the fleet. Which log "
            "source will provide this level of detail?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Endpoint detection and response (EDR) telemetry",
                "correct": True,
                "rationale": (
                    "Correct. EDR tooling continuously records granular "
                    "process, file, and registry activity, providing the "
                    "detailed file-system and registry-level telemetry needed "
                    "to build a complete set of indicators of compromise — "
                    "detail a single antivirus alert does not include."
                ),
            },
            {
                "id": "b",
                "text": "Firewall logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs record network connection "
                    "attempts by IP and port; they contain no information about "
                    "file creation or registry modification on the host."
                ),
            },
            {
                "id": "c",
                "text": "DNS query logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs show which domain names were resolved; "
                    "they provide no visibility into local file-system or "
                    "registry activity on the compromised host."
                ),
            },
            {
                "id": "d",
                "text": "Vulnerability scan reports",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scan reports describe known "
                    "weaknesses present on a host at scan time; they are not a "
                    "source of real-time forensic file and registry activity "
                    "during an incident."
                ),
            },
        ],
        "explanation": (
            "Detailed, granular visibility into file and registry changes made "
            "during malware execution comes from EDR telemetry, not from "
            "network-focused logs (firewall, DNS) or point-in-time vulnerability "
            "scan data."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A security assessment of a fleet of network printers finds SNMP v1 "
            "enabled with the default \"public\" community string, an exposed "
            "legacy FTP-based print-job submission interface, and a web "
            "management console still using default admin/admin credentials — "
            "all reachable from the general office VLAN. Which action would MOST "
            "comprehensively reduce this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Apply a standard hardening baseline to the printers: "
                    "disable unused services, change default credentials, and "
                    "restrict management access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A hardening baseline that disables unnecessary "
                    "services (SNMP v1, legacy FTP), changes default "
                    "credentials, and restricts who can reach the management "
                    "interface addresses every weakness identified, rather than "
                    "fixing just one symptom."
                ),
            },
            {
                "id": "b",
                "text": "Change only the SNMP community string to a stronger value",
                "correct": False,
                "rationale": (
                    "Incorrect. This addresses only one of the three "
                    "identified weaknesses; the exposed FTP interface and "
                    "default web console credentials would remain fully "
                    "exploitable."
                ),
            },
            {
                "id": "c",
                "text": "Install endpoint antivirus software on each printer",
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus software does not address exposed "
                    "insecure services or default credentials; embedded printer "
                    "firmware generally does not support traditional antivirus "
                    "agents in the first place."
                ),
            },
            {
                "id": "d",
                "text": "Move the printers to the general guest Wi-Fi VLAN",
                "correct": False,
                "rationale": (
                    "Incorrect. This does not fix any of the underlying "
                    "insecure services or default credentials, and placing "
                    "business-critical print infrastructure on a guest network "
                    "would likely break required internal connectivity while "
                    "leaving the core vulnerabilities unaddressed."
                ),
            },
        ],
        "explanation": (
            "A complete hardening baseline — disabling unused/legacy services, "
            "eliminating default credentials, and restricting management "
            "access — addresses the full set of exposures, whereas fixing only "
            "one setting or adding an unrelated control leaves the others "
            "exploitable."
        ),
    },
    {
        "id": "nd2h-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hardening",
        "stem": (
            "An audit of a Windows server fleet finds that the legacy "
            "PowerShell version 2 engine remains installed and enabled "
            "alongside the modern, fully logged PowerShell 5.1 engine. "
            "Attackers are observed specifically invoking "
            "\"powershell -version 2\" to bypass script-block logging and AMSI "
            "scanning that only the modern engine enforces. Which action BEST "
            "addresses the root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remove/disable the legacy PowerShell v2 engine fleet-wide",
                "correct": True,
                "rationale": (
                    "Correct. Since PowerShell v2 has no modern logging or AMSI "
                    "integration and serves no purpose once v5.1 is deployed, "
                    "removing the legacy engine eliminates the attacker's "
                    "downgrade path entirely — true attack surface reduction "
                    "rather than just watching for the abuse."
                ),
            },
            {
                "id": "b",
                "text": "Increase the logging verbosity of PowerShell 5.1 only",
                "correct": False,
                "rationale": (
                    "Incorrect. Increasing logging on the modern engine does "
                    "nothing to stop attackers from invoking the legacy v2 "
                    "engine, which bypasses that logging entirely; the "
                    "vulnerable component itself remains present and usable."
                ),
            },
            {
                "id": "c",
                "text": "Block all PowerShell execution across the fleet",
                "correct": False,
                "rationale": (
                    "Incorrect. Completely blocking PowerShell would break "
                    "legitimate administrative automation across the fleet; the "
                    "targeted fix is removing only the unnecessary, unlogged "
                    "legacy engine, not eliminating a core administrative tool "
                    "entirely."
                ),
            },
            {
                "id": "d",
                "text": "Reimage only the servers where the downgrade was already observed",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging affected hosts does not remove the "
                    "legacy engine from the rest of the fleet, leaving every "
                    "other unaudited server still vulnerable to the same "
                    "downgrade technique."
                ),
            },
        ],
        "explanation": (
            "The root cause is the continued presence of an unnecessary legacy "
            "component that undermines modern security controls; removing that "
            "component fleet-wide is true hardening/attack-surface reduction, "
            "unlike partial logging increases, blanket tool bans, or "
            "reimaging only already-affected hosts."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2h-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "After an incident in which a rogue laptop was connected to an open "
            "wall jack in an unused conference room and pivoted into the "
            "internal network undetected for several days, a security team wants "
            "to ensure that any device plugged into a wired port must be "
            "authenticated and placed on the correct VLAN automatically, or be "
            "denied network access entirely. Which mitigation BEST addresses "
            "this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.1X port-based network access control (NAC)",
                "correct": True,
                "rationale": (
                    "Correct. 802.1X requires a device (or its user) to "
                    "authenticate before the switch port grants network access, "
                    "and can dynamically assign the correct VLAN or deny access "
                    "entirely — directly closing the gap that let the rogue "
                    "laptop connect unchallenged."
                ),
            },
            {
                "id": "b",
                "text": "Application allowlisting",
                "correct": False,
                "rationale": (
                    "Incorrect. Application allowlisting controls which "
                    "software can execute on an endpoint; it does nothing to "
                    "authenticate a device attempting to connect to a wired "
                    "network port."
                ),
            },
            {
                "id": "c",
                "text": "Network segmentation alone, without port authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation limits where traffic can go once a "
                    "device is on the network, but without port-level "
                    "authentication a rogue device can still plug in and reach "
                    "whatever segment that jack is wired to."
                ),
            },
            {
                "id": "d",
                "text": "Multifactor authentication for user accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA strengthens login security for user "
                    "accounts; it does not control or authenticate which "
                    "physical devices are permitted to connect to a wired "
                    "switch port in the first place."
                ),
            },
        ],
        "explanation": (
            "Requiring devices to authenticate before a switch port grants "
            "access — and automatically assigning the correct VLAN or denying "
            "access — is exactly what 802.1X port-based NAC provides, directly "
            "closing the gap exploited by the rogue laptop."
        ),
    },
    {
        "id": "nd2h-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A ransomware outbreak is actively spreading between workstations "
            "over SMB file shares. Which TWO actions should the incident "
            "response team take FIRST to contain the outbreak? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Isolate the affected hosts and segment from the rest of "
                    "the network immediately"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Immediately isolating infected hosts and cutting "
                    "off their network segment stops the malware from reaching "
                    "additional shares and workstations while the rest of the "
                    "response proceeds."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Block or disable SMBv1 and restrict unnecessary east-west "
                    "SMB traffic between workstations"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cutting off the SMB pathway the ransomware is "
                    "using to spread laterally between peer workstations "
                    "directly halts its propagation mechanism."
                ),
            },
            {
                "id": "c",
                "text": "Immediately pay the ransom to obtain a decryption key",
                "correct": False,
                "rationale": (
                    "Incorrect. Paying a ransom is not a containment technique, "
                    "does not stop active spread, offers no guarantee of a "
                    "working decryption key, and is generally discouraged as it "
                    "funds further criminal activity."
                ),
            },
            {
                "id": "d",
                "text": "Wait for the next scheduled monthly patch cycle to apply fixes",
                "correct": False,
                "rationale": (
                    "Incorrect. An active, spreading outbreak requires "
                    "immediate containment action; waiting for a routine "
                    "scheduled patch cycle would allow the ransomware to keep "
                    "spreading unchecked in the meantime."
                ),
            },
        ],
        "explanation": (
            "Immediate isolation of infected hosts and cutting the lateral SMB "
            "propagation path are the correct first containment actions for an "
            "active ransomware outbreak; paying a ransom and waiting for a "
            "routine patch cycle are not appropriate immediate containment "
            "steps."
        ),
    },
]
