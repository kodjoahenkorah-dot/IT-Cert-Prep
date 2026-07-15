"""Exam Traps & Hands-On Practice — curated, hands-on practice categories.

Each category selects a slice of the Security+ bank (by question-id prefix
and/or study_topic and/or question type), rendered with instant feedback and,
where useful, a visual aid (monospace log/ACL rendering, a network-zone
diagram, or an SLE/ALE/ARO calculator).
"""

from __future__ import annotations

import random

# visual keys the template knows how to render
VIS_ZONES = "zones"     # network security-zone diagram
VIS_RISK = "risk"       # SLE/ALE/ARO calculator widget
VIS_PORTS = "ports"     # common ports quick-reference

CATEGORIES = [
    {
        "key": "linux",
        "name": "Linux command & log questions",
        "blurb": "auth.log / secure, SSH failed logins, grep, tail, chmod, chown, sudo, ps, ss/netstat, systemctl, SELinux.",
        "id_prefixes": ["tlnx"],
        "study_topics": [],
        "pbq_only": False,
        "mono": True,
        "visual": None,
    },
    {
        "key": "logs",
        "name": "Log reading & packet analysis",
        "blurb": "Read firewall / IDS / endpoint / web logs and packet clues; find the source IP, port, action, attack type, infected host.",
        "id_prefixes": ["tlog"],
        "study_topics": ["Log data sources", "SIEM & monitoring"],
        "pbq_only": False,
        "mono": True,
        "visual": None,
    },
    {
        "key": "firewall_pbq",
        "name": "Firewall rule PBQs",
        "blurb": "Build and order ACL rules — source, destination, port, protocol, allow/deny, implicit deny, rule order.",
        "id_prefixes": [],
        "study_topics": ["Firewalls", "Port and protocol security", "Attack surface reduction"],
        "pbq_only": True,
        "mono": True,
        "visual": None,
    },
    {
        "key": "ports",
        "name": "Port & protocol drills",
        "blurb": "22 SSH, 21 FTP, 23 Telnet, 25 SMTP, 53 DNS, 80/443, 389/636 LDAP(S), 445 SMB, 3389 RDP, 161/162 SNMP, 514 syslog — secure vs insecure.",
        "id_prefixes": [],
        "study_topics": ["Port and protocol security"],
        "pbq_only": False,
        "mono": False,
        "visual": VIS_PORTS,
    },
    {
        "key": "iam",
        "name": "IAM & identity scenarios",
        "blurb": "SSO, SAML, OAuth, OIDC, LDAP, Kerberos, RADIUS, TACACS+, MFA factors, FIDO2, PAM, JIT access, ephemeral credentials.",
        "id_prefixes": [],
        "study_topics": ["Access control models", "Federation & SSO (SAML/OAuth)",
                          "Multifactor authentication", "Privileged access management",
                          "Authentication factors and protocols"],
        "pbq_only": False,
        "mono": False,
        "visual": None,
    },
    {
        "key": "cloud",
        "name": "Cloud shared responsibility",
        "blurb": "Who manages what across IaaS / PaaS / SaaS — data, identity, apps, OS patching, hosts, network.",
        "id_prefixes": [],
        "study_topics": ["Cloud architecture", "Serverless and cloud architecture",
                          "Multi-cloud and platform diversity", "Architecture trade-offs"],
        "pbq_only": False,
        "mono": False,
        "visual": None,
    },
    {
        "key": "risk",
        "name": "Risk formula calculations",
        "blurb": "SLE = AV × EF, ALE = SLE × ARO, cost-benefit — with a built-in calculator to practice the math.",
        "id_prefixes": [],
        "study_topics": ["Quantitative risk analysis (SLE/ALE/ARO)"],
        "pbq_only": False,
        "mono": False,
        "visual": VIS_RISK,
    },
    {
        "key": "ir",
        "name": "Incident response ordering",
        "blurb": "Sequence real response actions — preparation, detection, containment, eradication, recovery, lessons learned.",
        "id_prefixes": [],
        "study_topics": ["Incident response process", "Digital forensics",
                         "Digital forensics and chain-of-custody process"],
        "pbq_only": False,
        "mono": False,
        "visual": None,
    },
    {
        "key": "dataroles",
        "name": "Data role matching",
        "blurb": "Owner, controller, processor, custodian, steward, data subject — match responsibilities to roles.",
        "id_prefixes": [],
        "study_topics": ["Data roles (controller/processor/custodian)", "Data classification levels"],
        "pbq_only": False,
        "mono": False,
        "visual": None,
    },
    {
        "key": "appliances",
        "name": "WAF / TLS / IDS / IPS / firewall comparison",
        "blurb": "The commonly-confused controls — which one protects a web app, encrypts in transit, detects vs blocks, controls ports.",
        "id_prefixes": ["tfw"],
        "study_topics": ["Firewalls", "Network appliances",
                         "Secure communication (VPN/TLS/IPSec)"],
        "pbq_only": False,
        "mono": True,
        "visual": VIS_ZONES,
    },
]

_BY_KEY = {c["key"]: c for c in CATEGORIES}


def get_category(key: str):
    return _BY_KEY.get(key)


def _matches(cat, q) -> bool:
    if any(q["id"].startswith(p) for p in cat["id_prefixes"]):
        pass  # id-prefix match always qualifies
    elif cat["study_topics"] and q.get("study_topic") in set(cat["study_topics"]):
        pass
    else:
        return False
    if cat["pbq_only"] and not q["type"].startswith("pbq"):
        return False
    return True


def category_pool(cat, bank) -> list[dict]:
    return [q for q in bank if _matches(cat, q)]


def build_traps_session(cat, bank, num_questions=15, seed=None) -> list[dict]:
    rng = random.Random(seed)
    pool = category_pool(cat, bank)
    rng.shuffle(pool)
    return pool[: min(num_questions, len(pool))]


def category_counts(bank) -> dict[str, int]:
    return {c["key"]: len(category_pool(c, bank)) for c in CATEGORIES}
