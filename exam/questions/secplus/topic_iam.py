"""CompTIA Security+ SY0-701 practice questions — topical batch: Identity and Access
Management (IAM) flows and identity.

Scenarios cover federated SSO (SAML assertions, OAuth 2.0 delegated authorization, OIDC
identity tokens, LDAP/LDAPS, Kerberos KDC/TGT, RADIUS vs. TACACS+), multifactor
authentication (factor categories, same-category traps, passwordless/FIDO2/WebAuthn/
passkeys, attestation, MFA fatigue, adaptive authentication), privileged access management
(password vaulting, just-in-time access, ephemeral credentials, privilege creep, separation
of duties, break-glass accounts, session recording, orphaned accounts/JML), and access
control models (MAC, DAC, RBAC, ABAC, rule-based access control, implicit deny).
"""

QUESTIONS = [
    # ---------------------------------------------------------------
    # Federation & SSO (SAML/OAuth) — domain 4, objective 4.6
    # ---------------------------------------------------------------
    {
        "id": "tiam-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A mobile app needs to know the authenticated user's identity (name, email) after login, not just "
            "obtain permission to call an API on the user's behalf. The identity provider returns a signed JWT "
            "containing the user's identity claims in addition to an OAuth access token. Which component provides "
            "this identity information?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The OpenID Connect (OIDC) ID token",
                "correct": True,
                "rationale": (
                    "Correct. OIDC extends OAuth 2.0 by adding an ID token, a signed JWT that carries the user's "
                    "identity/authentication claims. This is distinct from the access token, which authorizes API "
                    "calls rather than asserting who the user is."
                ),
            },
            {
                "id": "b",
                "text": "The OAuth 2.0 access token",
                "correct": False,
                "rationale": (
                    "Incorrect. The access token authorizes calls to a resource server within defined scopes; it "
                    "is not designed to carry verified identity claims about the authentication event."
                ),
            },
            {
                "id": "c",
                "text": "A SAML assertion",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML is a separate, XML-based protocol. The scenario describes a JSON Web Token "
                    "issued as part of an OAuth-based flow, not a SAML exchange."
                ),
            },
            {
                "id": "d",
                "text": "A Kerberos service ticket",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos tickets are issued within a trusted realm by a KDC for internal "
                    "network authentication; they are not used to deliver identity claims to a mobile app via a "
                    "signed JWT."
                ),
            },
        ],
        "explanation": (
            "OIDC layers authentication on top of OAuth's authorization framework. The ID token (a signed JWT) "
            "conveys who the user is, while the access token separately grants scoped permission to call APIs. "
            "Confusing the two — or reaching for SAML or Kerberos, which use entirely different token formats and "
            "trust models — is the classic trap in this scenario."
        ),
    },
    {
        "id": "tiam-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "In a SAML federation between a university's identity provider (IdP) and a cloud learning management "
            "system (LMS), the LMS receives and validates the signed assertion, then grants a session. Which role "
            "does the LMS play in this exchange?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Service provider (SP), also called the relying party",
                "correct": True,
                "rationale": (
                    "Correct. The SP/relying party is the entity that consumes and trusts the signed assertion "
                    "issued by the IdP to grant access — exactly the LMS's role here."
                ),
            },
            {
                "id": "b",
                "text": "Identity provider (IdP)",
                "correct": False,
                "rationale": (
                    "Incorrect. The IdP authenticates the user and issues the assertion; that role belongs to the "
                    "university's identity system, not the LMS receiving the assertion."
                ),
            },
            {
                "id": "c",
                "text": "Registration authority (RA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An RA is a PKI concept responsible for verifying identity before certificate "
                    "issuance; it has no role in a SAML SSO exchange."
                ),
            },
            {
                "id": "d",
                "text": "Key Distribution Center (KDC)",
                "correct": False,
                "rationale": (
                    "Incorrect. A KDC is a Kerberos component that issues tickets within a trusted realm; it is "
                    "unrelated to SAML's IdP/SP browser-federation model."
                ),
            },
        ],
        "explanation": (
            "SAML defines two core roles: the identity provider (authenticates the user and signs the assertion) "
            "and the service provider/relying party (validates the assertion and grants access). The LMS, which "
            "trusts and consumes the assertion, is the service provider."
        ),
    },
    {
        "id": "tiam-003",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A user logs into a Windows domain workstation. The workstation contacts the Key Distribution Center "
            "(KDC), and after successful authentication, receives a ticket-granting ticket (TGT) that will later "
            "be presented to request service tickets for specific resources without re-entering credentials. "
            "Which protocol is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Kerberos",
                "correct": True,
                "rationale": (
                    "Correct. Kerberos issues a TGT from the KDC's authentication service after initial login, "
                    "which the client then presents to the ticket-granting service to obtain service tickets for "
                    "individual resources — exactly this workflow."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS is a UDP-based challenge/response AAA protocol typically used for network "
                    "access (VPN, Wi-Fi); it has no concept of a KDC or a ticket-granting ticket."
                ),
            },
            {
                "id": "c",
                "text": "SAML",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML uses browser-redirected, signed XML assertions between an IdP and SP; it "
                    "does not involve a KDC or ticket-granting tickets."
                ),
            },
            {
                "id": "d",
                "text": "LDAP simple bind",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP simple bind directly validates a username/password against a directory in a "
                    "single request; it does not issue tickets or involve a KDC."
                ),
            },
        ],
        "explanation": (
            "Kerberos authentication begins when the client authenticates to the KDC's authentication service "
            "(AS) and receives a TGT. The TGT is then presented to the ticket-granting service (TGS) to obtain "
            "service tickets for specific resources, avoiding repeated credential entry within the realm."
        ),
    },
    {
        "id": "tiam-004",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A network security team wants to authenticate administrators logging into network switches and "
            "routers, and additionally wants to authorize each individual command (e.g., allow 'show' commands "
            "but require additional approval for 'configure terminal') on a per-user basis, with the entire "
            "authentication packet encrypted. Which protocol should be used for device administration in this "
            "scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TACACS+",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ separates authentication, authorization, and accounting, supports granular "
                    "per-command authorization, and encrypts the entire packet body — the standard choice for "
                    "device administration AAA."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS combines authentication and authorization into a single response, encrypts "
                    "only the password attribute by default, and lacks native per-command authorization — better "
                    "suited to network access than device administration."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos issues tickets for service-to-service authentication within a realm; it "
                    "provides no mechanism for authorizing individual CLI commands on network devices."
                ),
            },
            {
                "id": "d",
                "text": "LDAPS",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAPS secures directory lookups and binds; it does not provide command-level "
                    "authorization for network device administration."
                ),
            },
        ],
        "explanation": (
            "TACACS+ is purpose-built for device administration: it fully encrypts packets and supports granular, "
            "per-command authorization decisions. RADIUS is the common alternative for network access (Wi-Fi, "
            "VPN) but is weaker for this specific per-command, device-admin use case."
        ),
    },
    {
        "id": "tiam-005",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A packet capture on the internal network reveals that user bind credentials for the directory "
            "service are transmitted as cleartext over TCP port 389 whenever an application performs an LDAP "
            "simple bind. Which change would MOST directly remediate this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Migrate the bind operation to LDAPS (LDAP over SSL/TLS) or enforce StartTLS to encrypt the credential exchange",
                "correct": True,
                "rationale": (
                    "Correct. LDAPS (or StartTLS) wraps the LDAP session in TLS, encrypting the bind credentials "
                    "in transit and directly eliminating the cleartext exposure observed in the capture."
                ),
            },
            {
                "id": "b",
                "text": "Switch the application's authentication mechanism to RADIUS instead of LDAP",
                "correct": False,
                "rationale": (
                    "Incorrect. Swapping to RADIUS doesn't fix the directory's LDAP bind exposure, and RADIUS "
                    "itself only encrypts the password attribute by default, leaving other data in cleartext."
                ),
            },
            {
                "id": "c",
                "text": "Increase the minimum password length policy enforced by the directory",
                "correct": False,
                "rationale": (
                    "Incorrect. A longer password policy does not prevent the credential from being transmitted "
                    "in cleartext; it does nothing to address the transport-layer exposure identified."
                ),
            },
            {
                "id": "d",
                "text": "Change the LDAP bind DN to use a lower-privileged service account",
                "correct": False,
                "rationale": (
                    "Incorrect. A lower-privileged account reduces the impact if the credential is captured, but "
                    "the credential would still traverse the network in cleartext — the root exposure remains."
                ),
            },
        ],
        "explanation": (
            "Standard LDAP simple binds send credentials in cleartext unless the session is protected by TLS. "
            "LDAPS (port 636) or StartTLS on port 389 encrypts the bind exchange, which is the direct fix for "
            "credentials observed in cleartext on the wire."
        ),
    },
    {
        "id": "tiam-006",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A native mobile application needs to obtain an OAuth 2.0 access token to call a company API on "
            "behalf of the signed-in user. Because the app cannot securely store a client secret, which OAuth "
            "grant type/flow should be used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Authorization code flow with PKCE (Proof Key for Code Exchange)",
                "correct": True,
                "rationale": (
                    "Correct. PKCE protects the authorization code flow for public clients that cannot hold a "
                    "client secret, such as native mobile apps, by binding the code exchange to a dynamically "
                    "generated verifier — the current recommended practice for this scenario."
                ),
            },
            {
                "id": "b",
                "text": "Implicit grant flow",
                "correct": False,
                "rationale": (
                    "Incorrect. The implicit grant returns the access token directly in a URL fragment with no "
                    "code exchange step, exposing it to interception; it is deprecated for public clients in "
                    "favor of PKCE-protected authorization code flow."
                ),
            },
            {
                "id": "c",
                "text": "Client credentials grant",
                "correct": False,
                "rationale": (
                    "Incorrect. The client credentials grant is for machine-to-machine access with no user "
                    "context — it does not represent a signed-in user's delegated permission, which this scenario "
                    "requires."
                ),
            },
            {
                "id": "d",
                "text": "Resource owner password credentials grant",
                "correct": False,
                "rationale": (
                    "Incorrect. This legacy grant requires the app to directly collect the user's username and "
                    "password, defeating OAuth's purpose of never exposing credentials to the client, and is "
                    "discouraged for exactly this reason."
                ),
            },
        ],
        "explanation": (
            "For public clients (mobile/SPA apps) unable to protect a client secret, the authorization code flow "
            "with PKCE is the current best practice, replacing the deprecated implicit grant. Client credentials "
            "and resource owner password grants do not fit a user-delegated mobile app scenario."
        ),
    },
    {
        "id": "tiam-007",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "An enterprise's legacy on-premises portal needs to enable single sign-on into a partner's cloud "
            "application. The partner requires a digitally signed XML document containing the user's identity "
            "and role attributes, delivered via browser redirect/POST, and does not support parsing JSON web "
            "tokens. Which federation protocol satisfies the partner's requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SAML",
                "correct": True,
                "rationale": (
                    "Correct. SAML delivers signed XML assertions via browser redirect/POST bindings, directly "
                    "matching the partner's explicit requirement for XML rather than JSON."
                ),
            },
            {
                "id": "b",
                "text": "OAuth 2.0",
                "correct": False,
                "rationale": (
                    "Incorrect. OAuth issues tokens for delegated authorization, commonly formatted as JSON/JWT, "
                    "not signed XML assertions, so it doesn't meet an XML-only requirement."
                ),
            },
            {
                "id": "c",
                "text": "OpenID Connect (OIDC)",
                "correct": False,
                "rationale": (
                    "Incorrect. OIDC ID tokens are JSON Web Tokens (JSON-based), not XML; a partner limited to "
                    "parsing XML assertions would not be satisfied by an OIDC ID token."
                ),
            },
            {
                "id": "d",
                "text": "Kerberos",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos is not a browser-redirect web federation protocol and does not produce "
                    "signed XML assertions for cross-organization SSO with external partners."
                ),
            },
        ],
        "explanation": (
            "SAML remains the standard when a partner explicitly requires signed XML assertions delivered via "
            "browser bindings — a common integration constraint with legacy or XML-only relying parties. OAuth "
            "and OIDC use JSON/JWT formats instead."
        ),
    },
    {
        "id": "tiam-008",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A startup building a mobile-first application wants to add 'Sign in with Google' functionality. "
            "They need a lightweight, JSON/REST-friendly protocol that layers authentication on top of an "
            "authorization framework already widely supported by mobile SDKs. Which protocol should they "
            "implement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OpenID Connect (OIDC)",
                "correct": True,
                "rationale": (
                    "Correct. OIDC is purpose-built as a thin authentication layer on top of OAuth 2.0, using "
                    "JSON/JWT ID tokens and REST-friendly flows well suited to mobile SDKs — exactly the "
                    "'sign in with' use case described."
                ),
            },
            {
                "id": "b",
                "text": "SAML",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML relies on heavier XML processing and browser POST bindings that are "
                    "cumbersome for native mobile SDKs compared to OIDC's lightweight JSON/REST model."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos requires a trusted realm and KDC infrastructure; it is not used for "
                    "consumer-facing 'sign in with' authentication against a third-party identity provider."
                ),
            },
            {
                "id": "d",
                "text": "TACACS+",
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ is a device-administration AAA protocol for network equipment, entirely "
                    "unrelated to consumer mobile app sign-in."
                ),
            },
        ],
        "explanation": (
            "OIDC was specifically designed to bring lightweight, JSON-based authentication to OAuth-supported "
            "ecosystems (mobile, SPAs, consumer sign-in), making it the natural fit over SAML's heavier XML model "
            "or protocols unrelated to web/mobile federation like Kerberos and TACACS+."
        ),
    },
    {
        "id": "tiam-009",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "An OAuth 2.0 client's access token expires after 15 minutes. Rather than forcing the user to log in "
            "again, the client silently sends a separate long-lived credential to the authorization server's "
            "token endpoint to obtain a new access token without user interaction. Which credential is being "
            "used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Refresh token",
                "correct": True,
                "rationale": (
                    "Correct. Refresh tokens are long-lived credentials issued alongside the access token "
                    "specifically so the client can silently obtain new access tokens after expiration without "
                    "user re-authentication."
                ),
            },
            {
                "id": "b",
                "text": "Access token",
                "correct": False,
                "rationale": (
                    "Incorrect. The access token is the short-lived credential that already expired; it cannot "
                    "be used to renew itself."
                ),
            },
            {
                "id": "c",
                "text": "Authorization code",
                "correct": False,
                "rationale": (
                    "Incorrect. The authorization code is a single-use, short-lived value exchanged once during "
                    "the initial authorization flow; it is not reused later to silently refresh tokens."
                ),
            },
            {
                "id": "d",
                "text": "Client secret",
                "correct": False,
                "rationale": (
                    "Incorrect. The client secret authenticates the confidential client application itself to "
                    "the authorization server; it is not a per-user credential used for silent token renewal."
                ),
            },
        ],
        "explanation": (
            "OAuth 2.0 pairs short-lived access tokens with long-lived refresh tokens so clients can silently "
            "obtain new access without repeated user interaction. Authorization codes and client secrets serve "
            "different, earlier steps in the flow."
        ),
    },
    {
        "id": "tiam-010",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A security engineer compares two AAA protocols and notes that Protocol A encrypts only the password "
            "field within its Access-Request packets, leaving other attributes (such as username) sent in "
            "cleartext by default, while Protocol B encrypts the entire body of every packet exchanged. Which "
            "pairing correctly identifies Protocol A and Protocol B?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Protocol A is RADIUS; Protocol B is TACACS+",
                "correct": True,
                "rationale": (
                    "Correct. RADIUS encrypts only the password attribute using a shared-secret hash, leaving "
                    "most of the packet (including the username) in cleartext, whereas TACACS+ encrypts the "
                    "entire packet body."
                ),
            },
            {
                "id": "b",
                "text": "Protocol A is TACACS+; Protocol B is RADIUS",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the actual behavior — TACACS+ is the protocol that encrypts the "
                    "full packet body, not the one limited to password-only encryption."
                ),
            },
            {
                "id": "c",
                "text": "Protocol A is Kerberos; Protocol B is LDAP",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos does not describe partial, password-only encryption of AAA packets, and "
                    "unencrypted LDAP does not encrypt entire packet bodies at all — neither matches the "
                    "description."
                ),
            },
            {
                "id": "d",
                "text": "Protocol A is SAML; Protocol B is OAuth",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML and OAuth are web federation/authorization protocols, not AAA protocols "
                    "evaluated on packet-level encryption scope like RADIUS and TACACS+."
                ),
            },
        ],
        "explanation": (
            "A key exam distinction: RADIUS encrypts only the password attribute in its packets (UDP-based), "
            "while TACACS+ encrypts the entire packet body (TCP-based) — one of the main reasons TACACS+ is "
            "preferred for sensitive device-administration AAA."
        ),
    },
    {
        "id": "tiam-011",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "Select TWO statements that correctly distinguish SAML from OAuth 2.0/OpenID Connect (OIDC) in "
            "enterprise identity architectures."
        ),
        "options": [
            {
                "id": "a",
                "text": "SAML was designed primarily for browser-based enterprise SSO using XML assertions, while OAuth was designed primarily for delegated API authorization.",
                "correct": True,
                "rationale": (
                    "Correct. SAML's core use case is federated browser SSO with signed XML assertions, while "
                    "OAuth's core use case is issuing scoped tokens for delegated access to APIs."
                ),
            },
            {
                "id": "b",
                "text": "OIDC adds an identity/authentication layer (the ID token) on top of OAuth 2.0's authorization framework.",
                "correct": True,
                "rationale": (
                    "Correct. OIDC is explicitly built as an authentication extension to OAuth 2.0, introducing "
                    "the signed ID token to convey verified identity claims."
                ),
            },
            {
                "id": "c",
                "text": "SAML cannot be used for single sign-on; it is only used for authorizing API calls between microservices.",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML's primary and most common use case is browser-based SSO, not microservice "
                    "API authorization — this statement inverts SAML's actual purpose."
                ),
            },
            {
                "id": "d",
                "text": "OAuth 2.0 access tokens are always formatted as signed XML assertions identical to SAML.",
                "correct": False,
                "rationale": (
                    "Incorrect. OAuth access tokens are commonly opaque strings or JWTs (JSON-based), not XML "
                    "assertions; conflating the two token formats is incorrect."
                ),
            },
        ],
        "explanation": (
            "SAML and OAuth/OIDC solve related but distinct problems: SAML for federated browser SSO via signed "
            "XML, and OAuth (with OIDC layered for authentication) for scoped, JSON/JWT-based delegated "
            "authorization and identity in modern app and mobile ecosystems."
        ),
    },
    # ---------------------------------------------------------------
    # Multifactor authentication — domain 4, objective 4.6
    # ---------------------------------------------------------------
    {
        "id": "tiam-012",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A bank requires customers to enter their account password and then answer a secret security "
            "question (e.g., mother's maiden name) before logging in online. Which statement BEST evaluates "
            "whether this satisfies true multifactor authentication (MFA)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This is NOT true MFA; both the password and the security question answer are 'something you know' factors from the same category.",
                "correct": True,
                "rationale": (
                    "Correct. True MFA requires factors from different categories. A password and a memorized "
                    "security question answer are both knowledge-based, so this is two-step verification within a "
                    "single factor category, not genuine MFA."
                ),
            },
            {
                "id": "b",
                "text": "This IS true MFA because two separate pieces of information are required.",
                "correct": False,
                "rationale": (
                    "Incorrect. Requiring two pieces of information is not sufficient if both come from the same "
                    "factor category; MFA specifically requires factors from distinct categories."
                ),
            },
            {
                "id": "c",
                "text": "This IS true MFA because the security question adds a 'something you have' factor.",
                "correct": False,
                "rationale": (
                    "Incorrect. A memorized answer to a question is knowledge-based, not possession-based; "
                    "nothing physical is required to answer it."
                ),
            },
            {
                "id": "d",
                "text": "This IS true MFA because it adds a 'something you are' biometric factor.",
                "correct": False,
                "rationale": (
                    "Incorrect. Answering a security question involves no biometric measurement; it remains "
                    "purely knowledge-based, like the password."
                ),
            },
        ],
        "explanation": (
            "MFA requires combining factors from different categories (knowledge, possession, inherence, "
            "location). A password plus a security question are both 'something you know,' so this setup is "
            "single-factor, two-step verification — not true MFA — despite requiring two separate answers."
        ),
    },
    {
        "id": "tiam-013",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A CISO wants to eliminate credential phishing risk for administrator logins by deploying a factor "
            "that cryptographically binds the authentication response to the specific origin (domain) being "
            "logged into, so a fake lookalike login page cannot successfully relay the response. Which "
            "technology BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FIDO2/WebAuthn hardware security keys or platform passkeys",
                "correct": True,
                "rationale": (
                    "Correct. FIDO2/WebAuthn performs origin-bound public-key challenge-response, so an "
                    "authentication attempt against a phishing domain fails because the signed response will not "
                    "match the legitimate origin — this is what makes it phishing-resistant."
                ),
            },
            {
                "id": "b",
                "text": "A time-based one-time password (TOTP) generated by an authenticator app",
                "correct": False,
                "rationale": (
                    "Incorrect. A TOTP code is just a numeric string that a user can be tricked into typing into "
                    "a phishing site in real time; TOTP is not cryptographically bound to the requesting origin."
                ),
            },
            {
                "id": "c",
                "text": "An SMS-delivered one-time passcode",
                "correct": False,
                "rationale": (
                    "Incorrect. Like TOTP, an SMS code can be relayed or phished in real time and is also "
                    "vulnerable to SIM-swapping; it provides no origin binding at all."
                ),
            },
            {
                "id": "d",
                "text": "A push notification approval without number matching",
                "correct": False,
                "rationale": (
                    "Incorrect. A simple push approval can be defeated via MFA fatigue/push-bombing attacks and "
                    "lacks cryptographic origin binding to prevent phishing relay."
                ),
            },
        ],
        "explanation": (
            "FIDO2/WebAuthn is considered phishing-resistant because the authenticator's cryptographic response "
            "is bound to the specific origin during the handshake, unlike TOTP, SMS, or simple push approvals, "
            "which can all be relayed or socially engineered by an attacker-in-the-middle."
        ),
    },
    {
        "id": "tiam-014",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "Employees sign into their laptops and cloud apps using only a fingerprint scan on their device, "
            "which unlocks a private key stored in the device's secure hardware enclave to complete a public-key "
            "challenge-response with no password ever entered or stored server-side. Which authentication "
            "approach is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Passwordless authentication using a FIDO2 passkey",
                "correct": True,
                "rationale": (
                    "Correct. This matches passkeys/passwordless authentication exactly — a locally verified "
                    "biometric unlocks a hardware-protected private key that completes a public-key challenge, "
                    "eliminating passwords entirely."
                ),
            },
            {
                "id": "b",
                "text": "Single sign-on (SSO) using a shared session cookie",
                "correct": False,
                "rationale": (
                    "Incorrect. SSO reduces repeated logins across applications via a shared session/token, but "
                    "does not describe biometric unlock of a locally stored private key, nor does it inherently "
                    "eliminate passwords."
                ),
            },
            {
                "id": "c",
                "text": "Knowledge-based authentication (KBA) using security questions",
                "correct": False,
                "rationale": (
                    "Incorrect. KBA relies on memorized secret answers (something you know) — the opposite of the "
                    "hardware-bound biometric key exchange described here."
                ),
            },
            {
                "id": "d",
                "text": "RADIUS challenge-response authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS challenge-response is a network AAA mechanism unrelated to local biometric "
                    "unlock of a device-bound private key."
                ),
            },
        ],
        "explanation": (
            "Passkeys implement FIDO2/WebAuthn passwordless authentication: a locally verified biometric (or PIN) "
            "unlocks a private key inside secure hardware, which completes a public-key challenge with no "
            "password ever transmitted or stored on the server."
        ),
    },
    {
        "id": "tiam-015",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "During FIDO2 security key registration, the relying party's server requests and validates a signed "
            "statement from the authenticator proving it is a genuine hardware token from an approved "
            "manufacturer, rather than software emulating one. Which concept is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Attestation",
                "correct": True,
                "rationale": (
                    "Correct. Attestation is the process by which a FIDO2 authenticator cryptographically proves "
                    "its authenticity/provenance to the relying party during registration, distinguishing genuine "
                    "hardware from emulated or software authenticators."
                ),
            },
            {
                "id": "b",
                "text": "Enrollment",
                "correct": False,
                "rationale": (
                    "Incorrect. Enrollment broadly refers to registering a factor or credential; it does not "
                    "specifically describe the cryptographic proof-of-authenticity step being validated here."
                ),
            },
            {
                "id": "c",
                "text": "Federation",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation refers to trust relationships across separate identity domains, not to "
                    "proving a single authenticator's hardware authenticity during registration."
                ),
            },
            {
                "id": "d",
                "text": "Provisioning",
                "correct": False,
                "rationale": (
                    "Incorrect. Provisioning refers to creating or granting a user's account and access rights, "
                    "not to validating an authenticator's manufacturer authenticity."
                ),
            },
        ],
        "explanation": (
            "Attestation lets a relying party verify that a FIDO2 authenticator is genuine, certified hardware "
            "(not an emulator or unapproved device) at registration time, adding trust assurance beyond simply "
            "enrolling a new credential."
        ),
    },
    {
        "id": "tiam-016",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "An attacker who has already obtained a user's password repeatedly triggers push-based MFA approval "
            "requests to the user's phone late at night, hoping the user will eventually tap 'Approve' just to "
            "stop the notifications. Which mitigation MOST directly addresses this specific attack technique?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable number matching, requiring the user to enter a displayed code from the login screen into the authenticator app before the push is approved",
                "correct": True,
                "rationale": (
                    "Correct. Number matching forces active engagement with the actual login attempt's details "
                    "rather than a single blind tap, directly defeating mass-push fatigue attacks."
                ),
            },
            {
                "id": "b",
                "text": "Increase the complexity requirements of the user's password",
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker already has a valid password; strengthening future password "
                    "complexity does nothing to stop already-compromised credentials from triggering push floods."
                ),
            },
            {
                "id": "c",
                "text": "Switch from push notifications to SMS-delivered one-time codes",
                "correct": False,
                "rationale": (
                    "Incorrect. SMS OTP does not solve the fatigue problem and introduces its own weaknesses "
                    "(SIM swapping, interception); it lacks the active verification number matching provides."
                ),
            },
            {
                "id": "d",
                "text": "Extend the session timeout duration for authenticated users",
                "correct": False,
                "rationale": (
                    "Incorrect. Session timeout duration is unrelated to how the initial MFA approval is granted; "
                    "it does not prevent exploitation of push fatigue during login."
                ),
            },
        ],
        "explanation": (
            "MFA fatigue (push bombing) exploits simple tap-to-approve push notifications. Number matching "
            "requires the user to actively read and enter a code shown on the login screen, which directly "
            "defeats blind-tap approval attacks."
        ),
    },
    {
        "id": "tiam-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A financial services firm relies on SMS-delivered one-time passcodes as its second factor. "
            "Attackers successfully perform SIM-swapping attacks against several executives, porting their phone "
            "numbers to attacker-controlled devices and intercepting the OTPs. Which change would MOST "
            "effectively address this specific weakness going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace SMS OTP with FIDO2 hardware security keys or platform passkeys for the affected accounts",
                "correct": True,
                "rationale": (
                    "Correct. FIDO2/WebAuthn factors are bound to physical hardware/device-secured keys and are "
                    "not dependent on the mobile carrier's number-porting process, eliminating the SIM-swap "
                    "attack vector entirely."
                ),
            },
            {
                "id": "b",
                "text": "Increase the length of the SMS OTP code from 6 to 10 digits",
                "correct": False,
                "rationale": (
                    "Incorrect. Code length does nothing to prevent the SIM swap itself; the attacker still "
                    "receives whatever code is sent to the now-hijacked number."
                ),
            },
            {
                "id": "c",
                "text": "Require the OTP to be resent twice before granting access",
                "correct": False,
                "rationale": (
                    "Incorrect. Resending the code through the same vulnerable channel (SMS to a hijacked number) "
                    "does not address the root cause; the attacker still intercepts it."
                ),
            },
            {
                "id": "d",
                "text": "Shorten the validity window of the SMS OTP from 5 minutes to 3 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. A shorter validity window marginally reduces replay risk but does not stop "
                    "delivery to an attacker who has already hijacked the phone number via SIM swap."
                ),
            },
        ],
        "explanation": (
            "SMS OTP's dependence on the mobile carrier's number makes it vulnerable to SIM swapping. FIDO2/"
            "WebAuthn hardware or platform authenticators remove this dependency entirely, since the credential "
            "lives in device-bound secure hardware rather than being delivered over the cellular network."
        ),
    },
    {
        "id": "tiam-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A conditional access policy grants access only when a login attempt's GPS/network-derived location "
            "falls within an approved geofenced region, in addition to a valid password. Which authentication "
            "factor category does the location check represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Somewhere you are (location-based factor)",
                "correct": True,
                "rationale": (
                    "Correct. Verifying the geographic location of a request is the defining example of the "
                    "'somewhere you are' factor category, distinct from knowledge, possession, or inherence "
                    "factors."
                ),
            },
            {
                "id": "b",
                "text": "Something you have",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Something you have' refers to possession of a physical or virtual token/device, "
                    "not the geographic location of the request itself."
                ),
            },
            {
                "id": "c",
                "text": "Something you are",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Something you are' refers to inherent biometric traits (fingerprint, face); "
                    "location is not a biological characteristic of the user."
                ),
            },
            {
                "id": "d",
                "text": "Something you do",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Something you do' refers to behavioral biometrics such as typing cadence or "
                    "gait; it does not describe a static geographic location check."
                ),
            },
        ],
        "explanation": (
            "'Somewhere you are' is a distinct authentication factor category based on the requester's verified "
            "geographic location, separate from knowledge (know), possession (have), inherence (are), and "
            "behavior (do) factors."
        ),
    },
    {
        "id": "tiam-019",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A continuous authentication system monitors a user's unique typing rhythm, mouse movement patterns, "
            "and touchscreen swipe dynamics throughout a session, silently re-verifying identity without "
            "requiring the user to stop and scan a fingerprint or face. Which factor category does this "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Something you do (behavioral biometrics)",
                "correct": True,
                "rationale": (
                    "Correct. Behavioral biometrics — typing cadence, gesture/swipe dynamics, mouse movement — "
                    "fall under 'something you do,' distinct from static physiological biometrics like "
                    "fingerprints."
                ),
            },
            {
                "id": "b",
                "text": "Something you are (physiological biometrics)",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Something you are' covers static physical characteristics (fingerprint, iris, "
                    "face); the scenario explicitly describes dynamic behavioral patterns, not a physiological "
                    "scan."
                ),
            },
            {
                "id": "c",
                "text": "Something you have",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical token or device possession is described; the system analyzes "
                    "behavior patterns, not verification of an item's possession."
                ),
            },
            {
                "id": "d",
                "text": "Something you know",
                "correct": False,
                "rationale": (
                    "Incorrect. No memorized secret is involved; typing rhythm and movement patterns are "
                    "behavioral, not knowledge-based."
                ),
            },
        ],
        "explanation": (
            "'Something you do' captures dynamic behavioral biometrics (typing cadence, gait, gesture patterns), "
            "which is distinct from 'something you are,' the category for static physiological biometrics such "
            "as fingerprints or facial geometry."
        ),
    },
    {
        "id": "tiam-020",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "Several users report that their authenticator app's six-digit codes are consistently rejected by "
            "the login server, even though the app and server share the correctly provisioned secret. "
            "Investigation reveals the mobile device's system clock is several minutes out of sync with real "
            "time. Which type of one-time password algorithm is MOST likely in use, and what does this explain?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Time-based one-time password (TOTP); TOTP codes are derived from the shared secret combined with the current time, so clock drift between client and server causes valid-looking codes to be rejected.",
                "correct": True,
                "rationale": (
                    "Correct. TOTP derives its code from the shared secret and the current time step; if the "
                    "device clock drifts significantly, the generated code no longer matches what the server "
                    "expects, causing rejections — exactly the symptom described."
                ),
            },
            {
                "id": "b",
                "text": "HMAC-based one-time password (HOTP); HOTP codes are derived from a synchronized counter, so this failure indicates the counters are out of sync rather than time drift.",
                "correct": False,
                "rationale": (
                    "Incorrect. HOTP failures stem from counter desynchronization (e.g., generating codes without "
                    "submitting them), not from clock/time drift — the scenario explicitly describes a time "
                    "synchronization issue, which is TOTP's defining vulnerability, not HOTP's."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos pre-authentication timestamp; ticket requests are being rejected due to time skew with the KDC.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes an authenticator app generating six-digit MFA codes for a "
                    "login server, not a Kerberos ticket exchange with a domain KDC."
                ),
            },
            {
                "id": "d",
                "text": "SAML assertion validity window; the assertion's NotBefore/NotOnOrAfter timestamps are being rejected due to clock skew between IdP and SP.",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML assertion timing applies to XML federation assertions between IdP and SP, "
                    "not to six-digit codes generated by a mobile authenticator app."
                ),
            },
        ],
        "explanation": (
            "TOTP ties code generation to the current time, so device clock drift is a well-known cause of "
            "otherwise-valid codes being rejected. HOTP instead relies on a synchronized counter and would fail "
            "differently (from counter desync, not time drift)."
        ),
    },
    {
        "id": "tiam-021",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A user successfully authenticates with a password and a registered mobile push approval from their "
            "usual laptop and home network. Later that day, a login attempt using the same valid password occurs "
            "from a new device and an unfamiliar country. The system automatically requires an additional "
            "verification step before granting access, even though the correct password was supplied. Which "
            "concept does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk-based (adaptive) authentication that triggers step-up verification based on contextual anomalies",
                "correct": True,
                "rationale": (
                    "Correct. Risk-based/adaptive authentication continuously evaluates contextual signals "
                    "(device, location, network) and dynamically requires additional verification when the risk "
                    "score increases, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Federation between the identity provider and the application",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation describes trust relationships enabling SSO across organizational "
                    "boundaries; it does not describe dynamically adjusting authentication requirements based on "
                    "contextual risk."
                ),
            },
            {
                "id": "c",
                "text": "Just-in-time (JIT) provisioning of user accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. JIT provisioning refers to automatically creating a user account/access at first "
                    "federated login, not to triggering additional verification for a risky login attempt."
                ),
            },
            {
                "id": "d",
                "text": "Kerberos mutual authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos mutual authentication ensures client and server verify each other's "
                    "identity using tickets; it does not describe adaptive, risk-based step-up challenges tied to "
                    "contextual anomalies."
                ),
            },
        ],
        "explanation": (
            "Risk-based (adaptive) authentication evaluates contextual signals like device, network, and "
            "location, dynamically escalating (step-up) authentication requirements for anomalous attempts even "
            "when the base credential is correct."
        ),
    },
    {
        "id": "tiam-022",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": "Select TWO true statements about FIDO2/WebAuthn authentication.",
        "options": [
            {
                "id": "a",
                "text": "FIDO2 uses asymmetric (public-key) cryptography, so the relying party stores only a public key and never a shared secret that could be stolen in a server-side breach.",
                "correct": True,
                "rationale": (
                    "Correct. FIDO2's public-key design means the relying party only ever stores a public key; "
                    "there is no shared secret on the server that an attacker could steal and replay."
                ),
            },
            {
                "id": "b",
                "text": "FIDO2 authentication responses are cryptographically bound to the requesting origin, which prevents replay against a phishing site impersonating the legitimate domain.",
                "correct": True,
                "rationale": (
                    "Correct. Origin binding is exactly what makes FIDO2/WebAuthn phishing-resistant — a signed "
                    "response generated for a fake domain will not validate against the real one."
                ),
            },
            {
                "id": "c",
                "text": "FIDO2 requires the user's private key to be transmitted to the relying party's server during every authentication so it can be verified.",
                "correct": False,
                "rationale": (
                    "Incorrect. The private key never leaves the authenticator/secure enclave; only a signed "
                    "assertion is sent, which is the entire point of the public-key design."
                ),
            },
            {
                "id": "d",
                "text": "FIDO2 is a knowledge-based factor, meaning it can be satisfied purely by the user memorizing and entering a static value.",
                "correct": False,
                "rationale": (
                    "Incorrect. FIDO2 is a possession-based factor (often combined with inherence via biometric "
                    "unlock) requiring the physical authenticator, not a memorized static value."
                ),
            },
        ],
        "explanation": (
            "FIDO2/WebAuthn's phishing resistance and breach resilience come from asymmetric cryptography (only "
            "a public key is stored server-side) combined with origin-bound challenge-response, with the private "
            "key never leaving the secure hardware."
        ),
    },
    # ---------------------------------------------------------------
    # Privileged access management — domain 4, objective 4.6
    # ---------------------------------------------------------------
    {
        "id": "tiam-023",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A PAM solution stores all shared local administrator and service account passwords in an encrypted "
            "vault. When an administrator needs elevated access, they check out the credential through the "
            "vault's web portal; the vault automatically rotates the password immediately after the session ends, "
            "so the checked-out value cannot be reused. Which capability is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Password/credential vaulting with automatic rotation",
                "correct": True,
                "rationale": (
                    "Correct. This is the defining PAM capability — centrally storing privileged credentials in "
                    "an encrypted vault, brokering time-limited checkout, and automatically rotating the secret "
                    "after use so it cannot be reused."
                ),
            },
            {
                "id": "b",
                "text": "Single sign-on (SSO)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSO lets a user authenticate once to access multiple applications with their own "
                    "identity; it does not describe vaulting and rotating shared privileged credentials."
                ),
            },
            {
                "id": "c",
                "text": "Federation",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation establishes cross-domain trust for authentication between "
                    "organizations; it has no relationship to centrally storing and rotating local admin/service "
                    "account passwords."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC is a policy decision model for evaluating attributes to grant access; it "
                    "does not itself vault or rotate credentials."
                ),
            },
        ],
        "explanation": (
            "Password vaulting with automatic rotation is a core PAM feature: shared privileged credentials are "
            "centrally stored, checked out under approval, and rotated after each use so that even a credential "
            "seen during a session cannot be reused later."
        ),
    },
    {
        "id": "tiam-024",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Rather than granting engineers permanent, standing administrator rights on production servers, a "
            "PAM platform allows an engineer to request elevated access for a specific, time-boxed maintenance "
            "window; the elevated permission is automatically granted at the start of the window and "
            "automatically revoked at the end, with no lingering standing privilege. Which concept does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Just-in-time (JIT) access",
                "correct": True,
                "rationale": (
                    "Correct. JIT access provisions elevated privileges only for the duration they are actually "
                    "needed and automatically revokes them afterward, eliminating standing privileged access."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC assigns permissions based on static role membership; by itself it does not "
                    "describe automatic time-boxed grant-and-revoke behavior tied to a specific request window."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC enforces access using fixed classification labels set by a central authority; "
                    "it does not describe temporary, self-service, time-limited privilege elevation."
                ),
            },
            {
                "id": "d",
                "text": "Federation",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation concerns cross-domain trust for authentication, not time-boxed "
                    "provisioning/revocation of elevated permissions within a single environment."
                ),
            },
        ],
        "explanation": (
            "Just-in-time access is a core PAM control that replaces standing privileges with temporary, "
            "time-boxed elevation granted only when needed and automatically revoked afterward, minimizing the "
            "attack surface of always-on administrative rights."
        ),
    },
    {
        "id": "tiam-025",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A CI/CD pipeline needs to deploy resources to a cloud environment. Instead of embedding a long-lived "
            "static API key in the pipeline configuration, the pipeline authenticates to the cloud provider's "
            "identity service and receives a short-lived access token, valid for only 15 minutes, that is "
            "automatically discarded after the deployment job completes. Which practice does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use of ephemeral credentials",
                "correct": True,
                "rationale": (
                    "Correct. Ephemeral credentials are short-lived, dynamically issued secrets that minimize "
                    "the exposure window compared to static, long-lived API keys — exactly matching the "
                    "pipeline's 15-minute token behavior."
                ),
            },
            {
                "id": "b",
                "text": "Password vaulting of a shared static secret",
                "correct": False,
                "rationale": (
                    "Incorrect. Vaulting a static secret still relies on a long-lived credential being stored and "
                    "checked out; the scenario explicitly describes a short-lived, automatically expiring token "
                    "instead of a stored static secret."
                ),
            },
            {
                "id": "c",
                "text": "Federated single sign-on for the pipeline's human operators",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a machine-to-machine automated pipeline obtaining a token, "
                    "not a human operator authenticating via federated SSO."
                ),
            },
            {
                "id": "d",
                "text": "Privilege creep mitigation through periodic access review",
                "correct": False,
                "rationale": (
                    "Incorrect. Periodic access review is a governance process for human accounts over time; it "
                    "doesn't describe the mechanism of issuing short-lived tokens to an automated pipeline."
                ),
            },
        ],
        "explanation": (
            "Ephemeral credentials — short-lived, dynamically issued tokens instead of static long-lived keys — "
            "are a PAM best practice for automation and machine identities, sharply reducing the window during "
            "which a leaked credential remains useful."
        ),
    },
    {
        "id": "tiam-026",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An employee who has moved through four different departments over six years still retains active "
            "access permissions granted for every prior role, none of which were ever revoked when they "
            "transferred. Which practice would have MOST effectively prevented this accumulation of unnecessary "
            "access?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Periodic user access reviews/recertification that revoke permissions no longer aligned with the employee's current role, enforcing least privilege",
                "correct": True,
                "rationale": (
                    "Correct. Regular access recertification compares each user's current entitlements against "
                    "their actual current role and revokes anything no longer justified, directly preventing "
                    "privilege creep."
                ),
            },
            {
                "id": "b",
                "text": "Requiring a longer, more complex password for the employee's account",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity has no bearing on excess entitlements accumulated across "
                    "role changes; it does not remove access that should have been revoked."
                ),
            },
            {
                "id": "c",
                "text": "Enabling full-disk encryption on the employee's assigned laptop",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data at rest on the device; it does nothing to detect or "
                    "revoke unnecessary directory/application permissions."
                ),
            },
            {
                "id": "d",
                "text": "Migrating the employee's email to a cloud-hosted platform",
                "correct": False,
                "rationale": (
                    "Incorrect. An email platform migration is unrelated to reviewing and revoking accumulated "
                    "access permissions from prior roles."
                ),
            },
        ],
        "explanation": (
            "Privilege creep — the silent accumulation of unneeded access across role changes — is prevented "
            "through periodic access recertification that actively compares and prunes entitlements against the "
            "user's current job function, restoring least privilege."
        ),
    },
    {
        "id": "tiam-027",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "In the accounts payable department, the same employee is currently able to both create a new "
            "vendor record and approve payments to that vendor without any second reviewer. Internal audit flags "
            "this as a significant fraud risk. Which control should be implemented to address this specific "
            "finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Separation of duties (SoD), requiring that vendor creation and payment approval be performed by two different individuals",
                "correct": True,
                "rationale": (
                    "Correct. SoD splits critical, conflicting responsibilities between different people "
                    "specifically to prevent a single individual from being able to commit and conceal fraud "
                    "unilaterally."
                ),
            },
            {
                "id": "b",
                "text": "Least privilege applied only to the employee's read access on unrelated HR systems",
                "correct": False,
                "rationale": (
                    "Incorrect. This addresses access to a completely unrelated system and does nothing about the "
                    "conflicting vendor-creation/payment-approval capability within accounts payable."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory access control (MAC) using classification labels for the vendor database",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC enforces static clearance-based labels; it does not address the workflow-"
                    "level conflict of one person performing two incompatible duties."
                ),
            },
            {
                "id": "d",
                "text": "Increasing the frequency of vulnerability scans on the accounts payable application server",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scanning identifies technical weaknesses in software; it has no "
                    "bearing on a business-process control gap like conflicting duties."
                ),
            },
        ],
        "explanation": (
            "Separation of duties directly addresses fraud risk created when one person holds two conflicting "
            "capabilities (create and approve). It is a business-process control distinct from least privilege, "
            "MAC, or vulnerability scanning."
        ),
    },
    {
        "id": "tiam-028",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Six months after an employee's last day, IT discovers their VPN and file-share accounts are still "
            "active and were used to log in twice after their termination date. Which process failure MOST "
            "directly caused this, and what should be implemented to prevent recurrence?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A failure in the offboarding/deprovisioning process; integrate the HR system with identity management so account disablement is automatically triggered by the employee's termination event (joiner-mover-leaver, or JML, automation)",
                "correct": True,
                "rationale": (
                    "Correct. This is a textbook orphaned account caused by a manual, disconnected offboarding "
                    "process; tying deprovisioning to the authoritative HR termination event ensures access is "
                    "revoked immediately and consistently."
                ),
            },
            {
                "id": "b",
                "text": "A failure in the password complexity policy; require longer passwords for VPN accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity is unrelated to the account remaining active after "
                    "termination; a strong password on a still-enabled orphaned account provides no protection."
                ),
            },
            {
                "id": "c",
                "text": "A failure in encryption key management; rotate the VPN's TLS certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate rotation on the VPN service doesn't disable an individual terminated "
                    "user's still-active account credentials."
                ),
            },
            {
                "id": "d",
                "text": "A failure in vulnerability scanning; add the VPN concentrator to the monthly scan scope",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scanning finds technical flaws in the VPN appliance itself, not "
                    "stale/orphaned user accounts left active after termination."
                ),
            },
        ],
        "explanation": (
            "Orphaned accounts result from manual, disconnected offboarding. Automating deprovisioning as part "
            "of the joiner-mover-leaver (JML) lifecycle, triggered directly by the authoritative HR termination "
            "event, closes this gap consistently across all systems."
        ),
    },
    {
        "id": "tiam-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An organization maintains a highly restricted 'break-glass' local administrator account for use "
            "only when the primary identity provider is unavailable during an outage. Which practice is MOST "
            "important for securing this account?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Store its credential in a sealed/vaulted process with mandatory approval, and generate high-priority alerts with mandatory post-use review any time it is checked out or used",
                "correct": True,
                "rationale": (
                    "Correct. Break-glass accounts bypass normal federated controls by design, so they require "
                    "compensating controls — strict vaulting and immediate alerting plus mandatory review of "
                    "every use — to ensure the emergency bypass is not silently abused."
                ),
            },
            {
                "id": "b",
                "text": "Disable the account entirely so it cannot be misused",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the account defeats its entire purpose, which is to provide emergency "
                    "access precisely when normal federated authentication is unavailable."
                ),
            },
            {
                "id": "c",
                "text": "Share its credential among all IT staff via a common team chat channel for convenience during outages",
                "correct": False,
                "rationale": (
                    "Incorrect. Broadly sharing a highly privileged emergency credential via an unaudited channel "
                    "massively increases the risk of misuse or compromise — the opposite of proper break-glass "
                    "handling."
                ),
            },
            {
                "id": "d",
                "text": "Configure the account to require the same federated MFA as normal admin accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. A break-glass account exists specifically for scenarios where the federated "
                    "identity provider (and its MFA flow) is down; requiring the same federated MFA would make it "
                    "unusable during the very outage it's meant to survive."
                ),
            },
        ],
        "explanation": (
            "Break-glass accounts intentionally bypass normal federated authentication for emergency use, so "
            "they need compensating controls — sealed vault storage, mandatory approval, and immediate alerting "
            "plus post-use review — rather than being disabled or tied to the very system they're meant to "
            "survive an outage of."
        ),
    },
    {
        "id": "tiam-030",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "During a compliance audit, an assessor asks how the organization can reconstruct exactly which "
            "commands a third-party contractor executed during a privileged remote session on a production "
            "database server three months ago. Which PAM capability directly provides this evidence?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Privileged session recording/monitoring, which logs and can play back keystrokes and screen activity during privileged sessions",
                "correct": True,
                "rationale": (
                    "Correct. Session recording captures a full, reviewable record of everything performed "
                    "during a privileged session, giving auditors exact after-the-fact visibility into contractor "
                    "actions."
                ),
            },
            {
                "id": "b",
                "text": "Multifactor authentication enforced at session start",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA verifies who initiated the session but provides no record of what commands "
                    "were executed once the session was underway."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control limiting which servers the contractor could reach",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC controls which resources are reachable in the first place; it does not "
                    "capture a detailed record of the specific commands run during an authorized session."
                ),
            },
            {
                "id": "d",
                "text": "Network segmentation isolating the database server on its own VLAN",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation limits network reachability/blast radius; it does not log or record "
                    "the content of an authorized privileged session."
                ),
            },
        ],
        "explanation": (
            "Privileged session recording is the PAM control that captures a full, replayable record of "
            "privileged activity, enabling exact reconstruction of what a user or contractor did during a "
            "session — which MFA, RBAC, and segmentation do not provide."
        ),
    },
    {
        "id": "tiam-031",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A security assessment finds that 80% of the organization's domain administrator accounts are "
            "permanently enabled with full privileges around the clock, even though most admins only need "
            "elevated rights a few hours per week for scheduled maintenance. Which change would MOST reduce the "
            "attack surface associated with these accounts?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace standing (always-on) administrative privileges with just-in-time elevation that is granted only for scheduled maintenance windows and automatically expires",
                "correct": True,
                "rationale": (
                    "Correct. Eliminating always-on privileged access in favor of time-boxed, on-demand JIT "
                    "elevation drastically shrinks the window during which a compromised admin credential could "
                    "be abused."
                ),
            },
            {
                "id": "b",
                "text": "Require all domain administrators to use 20-character passwords instead of 14-character passwords",
                "correct": False,
                "rationale": (
                    "Incorrect. Longer passwords marginally raise brute-force difficulty but do nothing to "
                    "reduce the fact that full privileges remain active and exploitable around the clock."
                ),
            },
            {
                "id": "c",
                "text": "Move the domain controllers to a different physical data center",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical relocation of servers has no effect on the standing-privilege exposure "
                    "of the administrator accounts themselves."
                ),
            },
            {
                "id": "d",
                "text": "Increase the domain administrators' account lockout threshold from 5 to 10 failed attempts",
                "correct": False,
                "rationale": (
                    "Incorrect. Loosening the lockout threshold would, if anything, make brute-force attacks "
                    "easier, and it does not address the core issue of unnecessary always-on privilege."
                ),
            },
        ],
        "explanation": (
            "Standing (always-on) privileged access maximizes the time window an attacker can exploit a "
            "compromised admin credential. JIT elevation confines privilege to only the time it's genuinely "
            "needed, directly shrinking that attack surface."
        ),
    },
    {
        "id": "tiam-032",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A security architect explains to leadership why a dedicated PAM vaulting solution is required "
            "instead of simply having administrators store shared credentials in a consumer-grade password "
            "manager. Which capability distinguishes an enterprise PAM vault from a typical consumer password "
            "manager in this context?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Automatic credential rotation after each checkout, brokered/proxied privileged sessions, and detailed audit logging of who accessed which credential and when",
                "correct": True,
                "rationale": (
                    "Correct. Enterprise PAM platforms add automatic rotation, session brokering, approval "
                    "workflows, and granular audit trails — capabilities consumer password managers are not "
                    "built to provide for shared privileged accounts."
                ),
            },
            {
                "id": "b",
                "text": "The ability to store more than one password per entry",
                "correct": False,
                "rationale": (
                    "Incorrect. Consumer password managers already routinely store many credentials; storage "
                    "volume is not the meaningful differentiator being tested here."
                ),
            },
            {
                "id": "c",
                "text": "The use of AES encryption to protect stored secrets",
                "correct": False,
                "rationale": (
                    "Incorrect. Many consumer password managers also use strong encryption at rest; encryption "
                    "algorithm choice alone doesn't capture what makes PAM enterprise-grade for shared privileged "
                    "accounts."
                ),
            },
            {
                "id": "d",
                "text": "Browser autofill integration for login forms",
                "correct": False,
                "rationale": (
                    "Incorrect. Browser autofill is a convenience feature common to consumer password managers; "
                    "it is not a differentiator that addresses enterprise privileged-account governance needs."
                ),
            },
        ],
        "explanation": (
            "Enterprise PAM vaults go beyond simple encrypted storage: they add automatic rotation, brokered/"
            "proxied sessions (so the raw credential may never be revealed), approval workflows, and detailed "
            "audit trails purpose-built for governing shared privileged accounts."
        ),
    },
    {
        "id": "tiam-033",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Select TWO true statements about the principles of least privilege and separation of duties (SoD) "
            "as applied in a PAM program."
        ),
        "options": [
            {
                "id": "a",
                "text": "Least privilege means granting a user or process only the minimum access necessary to perform its required function, and no more.",
                "correct": True,
                "rationale": (
                    "Correct. This is the precise definition of least privilege — access is scoped to only what "
                    "is required for the function being performed."
                ),
            },
            {
                "id": "b",
                "text": "Separation of duties reduces fraud/error risk by requiring that no single individual can both execute and approve a sensitive transaction alone.",
                "correct": True,
                "rationale": (
                    "Correct. SoD splits conflicting responsibilities across multiple individuals specifically "
                    "to prevent one person from unilaterally committing and concealing fraud or error."
                ),
            },
            {
                "id": "c",
                "text": "Least privilege and separation of duties are the same control and are always implemented using identical technical mechanisms.",
                "correct": False,
                "rationale": (
                    "Incorrect. They are distinct principles — least privilege limits the scope of a single "
                    "actor's access, while SoD splits a sensitive process across multiple actors; they are "
                    "complementary but not identical."
                ),
            },
            {
                "id": "d",
                "text": "Applying least privilege to an administrator account eliminates the need for any session monitoring or logging of that account's activity.",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege reduces the scope of what an account can do, but it does not "
                    "replace the need for monitoring/logging, which is still required to detect misuse within "
                    "the account's authorized scope."
                ),
            },
        ],
        "explanation": (
            "Least privilege and separation of duties are complementary but distinct PAM principles: least "
            "privilege scopes an individual actor's access down to the minimum needed, while SoD distributes a "
            "sensitive process across multiple actors so no one person can complete it alone."
        ),
    },
    # ---------------------------------------------------------------
    # Access control models — domain 4, objective 4.6
    # ---------------------------------------------------------------
    {
        "id": "tiam-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A defense contractor's document management system enforces access strictly according to "
            "classification labels (Unclassified, Secret, Top Secret) assigned by a central security office. "
            "Users cannot change these labels or grant access to others, regardless of their role or ownership "
            "of a file. Which access control model is in use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mandatory access control (MAC)",
                "correct": True,
                "rationale": (
                    "Correct. MAC enforces access using fixed, centrally assigned classification/clearance "
                    "labels that ordinary users cannot alter or override — exactly matching the rigid, centrally "
                    "controlled labeling described."
                ),
            },
            {
                "id": "b",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC lets the resource owner decide who else may access a file at their "
                    "discretion; the scenario explicitly states users cannot grant access to others, ruling out "
                    "DAC."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC ties permissions to a user's assigned role, not to a centrally assigned data "
                    "classification label independent of role."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. While ABAC can incorporate classification as one attribute among many, the "
                    "scenario describes a single rigid label-based scheme controlled centrally — the defining "
                    "characteristic of MAC specifically, not a broader multi-attribute ABAC policy engine."
                ),
            },
        ],
        "explanation": (
            "MAC is defined by centrally assigned, non-negotiable classification/clearance labels that users "
            "cannot alter — the hallmark of government/defense document handling systems, unlike DAC (owner "
            "discretion), RBAC (role-based), or ABAC (multi-attribute policy)."
        ),
    },
    {
        "id": "tiam-035",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "On a shared department file server, whoever creates a folder is automatically its owner and can "
            "independently decide, at any time, which specific coworkers are allowed to read or edit its "
            "contents — no central administrator approval is required. Which access control model does this "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Discretionary access control (DAC)",
                "correct": True,
                "rationale": (
                    "Correct. DAC is defined by resource owners having the discretion to grant or restrict "
                    "access to their own resources without requiring central authority approval, exactly as "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC access decisions are made by a central authority using fixed classification "
                    "labels; individual folder creators would have no discretion to independently grant access "
                    "under MAC."
                ),
            },
            {
                "id": "c",
                "text": "Rule-based access control",
                "correct": False,
                "rationale": (
                    "Incorrect. Rule-based access control applies predefined, system-wide rules (e.g., "
                    "time-of-day, IP restrictions) uniformly, rather than allowing each individual owner "
                    "discretion over their own resources."
                ),
            },
            {
                "id": "d",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC grants access according to a user's assigned role, not according to the "
                    "individual discretion of whoever happens to own a specific folder."
                ),
            },
        ],
        "explanation": (
            "DAC's defining trait is owner discretion: whoever owns a resource can grant or revoke others' "
            "access without central approval, in contrast to MAC's centrally fixed labels, RBAC's role "
            "assignments, or rule-based access control's uniform system-wide rules."
        ),
    },
    {
        "id": "tiam-036",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A hospital's EHR system automatically grants nurses access to medication administration records and "
            "grants billing staff access to insurance claim records, based solely on each employee's assigned "
            "job title in the HR system. When an employee transfers from nursing to billing, their access set "
            "changes to match the new title. Which access control model is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Role-based access control (RBAC)",
                "correct": True,
                "rationale": (
                    "Correct. Access is determined solely by the user's assigned role/job title, and permissions "
                    "change automatically as the role changes — the defining behavior of RBAC."
                ),
            },
            {
                "id": "b",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes access driven by a single factor (job title/role) rather "
                    "than an evaluation of multiple combined subject/resource/environment attributes, which "
                    "would be ABAC."
                ),
            },
            {
                "id": "c",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC would require individual resource owners to grant access at their "
                    "discretion; here, access is systematically tied to role assignment in HR, not to owner "
                    "discretion."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC is based on classification/clearance labels set by a central security "
                    "authority, not on job-title-based role assignment that changes automatically with a "
                    "transfer."
                ),
            },
        ],
        "explanation": (
            "RBAC ties permissions directly to a user's assigned role, automatically updating access as the role "
            "changes — distinct from ABAC's multi-attribute evaluation, DAC's owner discretion, or MAC's "
            "centrally fixed classification labels."
        ),
    },
    {
        "id": "tiam-037",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A cloud storage policy engine grants download access to a document only when ALL of the following "
            "are simultaneously true: the requesting user's department attribute matches the document's owning "
            "department, the document's sensitivity tag is not 'restricted' unless the user holds a "
            "'compliance-reviewer' attribute, and the request originates during business hours from a "
            "corporate-managed device. Which access control model is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Attribute-based access control (ABAC)",
                "correct": True,
                "rationale": (
                    "Correct. This policy dynamically evaluates and combines multiple simultaneous attributes — "
                    "subject department, resource sensitivity tag, a special subject attribute, time, and device "
                    "— which is the defining capability of ABAC."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC decisions are based on static role assignment alone; it cannot natively "
                    "combine resource sensitivity tags, time-of-day, and device attributes into a single "
                    "evaluated policy without an unmanageable number of roles."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC uses fixed classification labels set centrally; it doesn't dynamically "
                    "evaluate combinations of department match, time, and device posture as described."
                ),
            },
            {
                "id": "d",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC relies on the resource owner's individual discretion to grant access, not on "
                    "a policy engine automatically evaluating multiple combined attributes."
                ),
            },
        ],
        "explanation": (
            "ABAC is uniquely suited to policies that combine multiple simultaneous conditions across subject, "
            "resource, and environment attributes — exactly the multi-condition rule described, which RBAC, MAC, "
            "and DAC cannot natively express."
        ),
    },
    {
        "id": "tiam-038",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A border router applies a fixed, ordered set of access control list (ACL) entries to every packet: "
            "block all inbound traffic from a specific country's IP ranges, permit TCP/443 from any source, and "
            "deny everything else by default — applied identically regardless of which user or role is "
            "associated with the traffic. Which access control model does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rule-based access control",
                "correct": True,
                "rationale": (
                    "Correct. Rule-based access control applies a predefined, ordered set of if-then rules "
                    "uniformly to all traffic/requests, independent of any individual user's role or identity — "
                    "exactly matching a router ACL evaluated in sequence."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC decisions hinge on a subject's assigned role; the router ACL described has "
                    "no concept of user roles at all — it evaluates packet attributes against static rules."
                ),
            },
            {
                "id": "c",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC requires a resource owner to grant access at their discretion; a router "
                    "applying a fixed, pre-configured ACL involves no per-request owner discretion."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. While ACL rules do reference packet attributes, ABAC implies a dynamic policy "
                    "engine evaluating combined subject/resource/environment attributes with fine-grained "
                    "conditions, not a simple static, sequentially evaluated permit/deny rule list."
                ),
            },
        ],
        "explanation": (
            "Rule-based access control applies a static, ordered set of system-wide rules uniformly to all "
            "requests, with no concept of individual user roles or ownership — the classic model behind router/"
            "firewall ACLs, distinguishing it from RBAC, DAC, and ABAC."
        ),
    },
    {
        "id": "tiam-039",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "An organization using RBAC finds that many employees hold five or six roles accumulated over "
            "multiple transfers, and access reviews reveal most employees actually only need one current role's "
            "permissions. Which RBAC administrative practice would BEST correct this without abandoning the RBAC "
            "model?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Conduct periodic role recertification, removing role assignments that no longer match the employee's current job function",
                "correct": True,
                "rationale": (
                    "Correct. RBAC still requires ongoing governance; periodic recertification identifies and "
                    "removes stale role assignments accumulated through transfers, restoring alignment with "
                    "least privilege while keeping the RBAC model intact."
                ),
            },
            {
                "id": "b",
                "text": "Switch entirely to mandatory access control (MAC) using classification labels instead",
                "correct": False,
                "rationale": (
                    "Incorrect. Replacing RBAC with MAC is an unnecessary architectural overhaul that doesn't "
                    "fit this scenario; MAC solves a different problem (centralized clearance-based labeling), "
                    "not accumulated stale role assignments."
                ),
            },
            {
                "id": "c",
                "text": "Grant every employee the 'domain administrator' role as a temporary fix until the review is finished",
                "correct": False,
                "rationale": (
                    "Incorrect. This would drastically worsen the privilege creep problem by granting excessive "
                    "access to everyone, directly violating least privilege."
                ),
            },
            {
                "id": "d",
                "text": "Disable RBAC auditing to reduce noise from the large number of role assignments",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling auditing removes visibility needed to even detect and correct the "
                    "excessive accumulated role assignments; it does not fix the underlying access problem."
                ),
            },
        ],
        "explanation": (
            "RBAC deployments still require ongoing governance to remain effective. Periodic role "
            "recertification prunes stale role assignments accumulated across transfers, correcting privilege "
            "creep while preserving the RBAC model rather than abandoning it."
        ),
    },
    {
        "id": "tiam-040",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A defense contractor grants an analyst read access to a Top Secret database because their "
            "clearance level qualifies them, but a supervisor further restricts their view to only the specific "
            "project files relevant to their current assignment, even though their clearance would technically "
            "permit broader access. Which principle does the supervisor's additional restriction illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Need-to-know, which further limits access within an already-authorized clearance level to only the information required for a specific task",
                "correct": True,
                "rationale": (
                    "Correct. Need-to-know adds a task-specific restriction layered on top of clearance-based "
                    "authorization, ensuring that even a cleared individual only sees the subset of information "
                    "actually required for their current work — exactly what the supervisor enforced."
                ),
            },
            {
                "id": "b",
                "text": "Separation of duties, which prevents a single person from completing an entire sensitive process alone",
                "correct": False,
                "rationale": (
                    "Incorrect. SoD addresses splitting conflicting responsibilities among multiple people; the "
                    "scenario describes narrowing one analyst's visibility to relevant files, not dividing a "
                    "process between people."
                ),
            },
            {
                "id": "c",
                "text": "Federation, which establishes trust between the contractor's identity provider and the database's service provider",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation concerns cross-domain authentication trust relationships, not "
                    "narrowing an already-authenticated user's visibility within a single system based on task "
                    "relevance."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC) alone, since clearance level was the only factor considered",
                "correct": False,
                "rationale": (
                    "Incorrect. Clearance level (MAC) determined the outer boundary of eligibility, but the "
                    "scenario centers on an additional restriction beyond that clearance — the need-to-know "
                    "narrowing — not on MAC by itself."
                ),
            },
        ],
        "explanation": (
            "Need-to-know is a distinct principle layered on top of clearance-based MAC authorization: even a "
            "user with sufficient clearance is further limited to only the specific information required for "
            "their current task, minimizing unnecessary exposure of sensitive data."
        ),
    },
    {
        "id": "tiam-041",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A firewall administrator configures several explicit 'permit' rules for known business traffic. No "
            "rule exists for a newly observed, unrecognized protocol attempting to traverse the firewall, yet "
            "that traffic is blocked automatically. Which underlying access control principle explains this "
            "behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Implicit deny (default deny), where any traffic or request not explicitly permitted by a rule is automatically denied",
                "correct": True,
                "rationale": (
                    "Correct. Implicit/default deny is the security posture in which anything not explicitly "
                    "allowed is blocked by default, which is exactly why traffic with no matching permit rule "
                    "was automatically rejected."
                ),
            },
            {
                "id": "b",
                "text": "Separation of duties",
                "correct": False,
                "rationale": (
                    "Incorrect. SoD concerns dividing responsibilities among multiple people to prevent "
                    "unilateral fraud/error; it has no relationship to how unmatched firewall traffic is handled "
                    "by default."
                ),
            },
            {
                "id": "c",
                "text": "Federation",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation establishes cross-organization identity trust; it is unrelated to a "
                    "firewall's default handling of traffic lacking a matching rule."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. While ABAC policies can include deny conditions, the specific behavior described "
                    "— blocking anything not explicitly permitted — is the implicit/default-deny principle "
                    "itself, not a defining characteristic unique to ABAC."
                ),
            },
        ],
        "explanation": (
            "Implicit (default) deny is the foundational access control posture underlying most secure ACL and "
            "firewall configurations: only explicitly permitted traffic is allowed, and everything else is "
            "blocked automatically, regardless of the specific policy model layered on top."
        ),
    },
    {
        "id": "tiam-042",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "An ERP system's permission structure is deliberately designed so that the 'Create Purchase Order' "
            "permission and the 'Approve Purchase Order' permission can never be assigned to the same user role "
            "simultaneously, enforced by the system itself at the role-definition level. Which access control "
            "concept is built into this system design?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Separation of duties (SoD) enforced through mutually exclusive role/permission constraints",
                "correct": True,
                "rationale": (
                    "Correct. Technically enforcing that conflicting permissions (create and approve) can never "
                    "coexist in a single role is SoD implemented directly in the access control system's role "
                    "design, preventing the conflict from ever being configurable."
                ),
            },
            {
                "id": "b",
                "text": "Least privilege applied only to read-only reporting roles",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario is about preventing two specific conflicting permissions from "
                    "combining, not about minimizing an individual's overall access scope for reporting "
                    "functions."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory access control label inheritance",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC label inheritance concerns propagating classification labels to derived "
                    "objects; it has nothing to do with preventing two specific permissions from being combined "
                    "in one role."
                ),
            },
            {
                "id": "d",
                "text": "Federation trust between the ERP system and an external partner",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes an internal role-permission constraint within a single "
                    "ERP system, not a cross-organization federation trust relationship."
                ),
            },
        ],
        "explanation": (
            "SoD can be technically enforced within an access control system by defining mutually exclusive "
            "role/permission combinations, preventing conflicting capabilities (create and approve) from ever "
            "being assignable to the same role."
        ),
    },
    {
        "id": "tiam-043",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A file server administrator right-clicks a specific spreadsheet and adds three individual named "
            "users, each with distinct read/write/no-access permissions, directly on that file's security "
            "properties — with no role or group involved. Which mechanism, closely associated with the DAC "
            "model, is being used here?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A discretionary access control list (ACL) applied directly to the object by its owner/administrator",
                "correct": True,
                "rationale": (
                    "Correct. An ACL that lists specific named users and their individual permissions directly "
                    "on an object, configured at the owner's/administrator's discretion, is the classic "
                    "implementation mechanism of the DAC model."
                ),
            },
            {
                "id": "b",
                "text": "A security group tied to a role definition",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states 'no role or group involved' — permissions are "
                    "assigned to individually named users directly, which is not role/group-based access."
                ),
            },
            {
                "id": "c",
                "text": "A mandatory classification label attached to the file",
                "correct": False,
                "rationale": (
                    "Incorrect. No centrally assigned clearance/classification label is described; individual "
                    "named-user permissions set at the owner's discretion is not how MAC labels function."
                ),
            },
            {
                "id": "d",
                "text": "An attribute-based policy rule evaluating environmental conditions",
                "correct": False,
                "rationale": (
                    "Incorrect. No environmental conditions (time, location, device) are being evaluated; this "
                    "is a static, per-user permission list set directly on the object, not a dynamic ABAC "
                    "policy."
                ),
            },
        ],
        "explanation": (
            "Per-object access control lists (ACLs) listing individually named users and their permissions, set "
            "at the discretion of the resource's owner/administrator, are the classic technical implementation "
            "of the DAC model — distinct from role/group assignment, MAC labels, or ABAC policy rules."
        ),
    },
    {
        "id": "tiam-044",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "Select TWO true statements comparing mandatory access control (MAC) and discretionary access "
            "control (DAC)."
        ),
        "options": [
            {
                "id": "a",
                "text": "In MAC, access decisions are enforced using classification/clearance labels controlled by a central authority, and individual users cannot override them.",
                "correct": True,
                "rationale": (
                    "Correct. This is the defining characteristic of MAC: a central authority sets and enforces "
                    "classification/clearance labels that individual users have no ability to override."
                ),
            },
            {
                "id": "b",
                "text": "In DAC, the owner of a resource has the discretion to grant or revoke other users' access to that specific resource.",
                "correct": True,
                "rationale": (
                    "Correct. DAC is defined by owner discretion — the resource owner decides who else may "
                    "access it, without requiring central authority approval."
                ),
            },
            {
                "id": "c",
                "text": "MAC allows each file's creator to independently decide who else may access it, similar to DAC.",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes DAC's owner-discretion model, not MAC, which is precisely defined "
                    "by removing that discretion in favor of centrally controlled labels."
                ),
            },
            {
                "id": "d",
                "text": "DAC is generally considered more rigid and difficult to scale in dynamic environments than MAC because it requires a central authority to approve every access change.",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the characteristics — MAC is the more rigid, centrally controlled "
                    "model, while DAC is comparatively flexible (owner-discretion), though it can create "
                    "inconsistent enforcement across many independent owners."
                ),
            },
        ],
        "explanation": (
            "MAC and DAC sit at opposite ends of the control spectrum: MAC enforces centrally controlled, "
            "non-negotiable classification labels, while DAC delegates access decisions to each resource's "
            "individual owner — a distinction frequently tested by reversing which model is 'rigid' versus "
            "'flexible.'"
        ),
    },
]
