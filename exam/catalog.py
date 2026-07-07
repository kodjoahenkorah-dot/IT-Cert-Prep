"""Catalog of supported practice exams.

Each :class:`ExamProfile` bundles everything that is specific to one exam:
its display name, domain names + official weightings, where its offline
question bank lives, the pass threshold, the timer length, and the system
prompt used for optional AI question generation.

Adding a new exam is just adding another ExamProfile here plus a question
subpackage under ``exam/questions/``.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ExamProfile:
    key: str                       # url-safe id, e.g. "secplus"
    name: str                      # "CompTIA Security+ (SY0-701)"
    short_name: str                # "Security+"
    questions_package: str         # importable package of QUESTIONS modules
    domains: dict                  # {1: {"name":..., "weight":0.12}, ...}
    pass_percent: float = 83.0
    default_num_questions: int = 90
    default_pbqs: int = 5
    time_limit_min: int = 90
    ai_system_prompt: str = ""     # used only when AI mode is enabled
    blurb: str = ""                # one-line description for the home page


# --------------------------------------------------------------------------- #
# Security+ SY0-701                                                            #
# --------------------------------------------------------------------------- #
SECPLUS = ExamProfile(
    key="secplus",
    name="CompTIA Security+ (SY0-701)",
    short_name="Security+",
    questions_package="exam.questions.secplus",
    domains={
        1: {"name": "General Security Concepts", "weight": 0.12},
        2: {"name": "Threats, Vulnerabilities, and Mitigations", "weight": 0.22},
        3: {"name": "Security Architecture", "weight": 0.18},
        4: {"name": "Security Operations", "weight": 0.28},
        5: {"name": "Security Program Management and Oversight", "weight": 0.20},
    },
    pass_percent=83.0,
    default_num_questions=90,
    default_pbqs=5,
    time_limit_min=90,
    blurb="Cybersecurity fundamentals: threats, crypto, architecture, operations, and governance.",
    ai_system_prompt=(
        "You are an item writer for the CompTIA Security+ SY0-701 certification exam. "
        "Write questions indistinguishable from real SY0-701 items, calibrated to be AS "
        "HARD OR HARDER than the live exam: scenario-based, with plausible distractors that "
        "test real misconceptions and 'best answer' wording where more than one option is "
        "defensible but only one is best. The five domains are: 1 General Security Concepts; "
        "2 Threats, Vulnerabilities, and Mitigations; 3 Security Architecture; 4 Security "
        "Operations; 5 Security Program Management and Oversight."
    ),
)


# --------------------------------------------------------------------------- #
# A+ Core 1 (220-1201)                                                         #
# --------------------------------------------------------------------------- #
APLUS_CORE1 = ExamProfile(
    key="aplus_core1",
    name="CompTIA A+ Core 1 (220-1201)",
    short_name="A+ Core 1",
    questions_package="exam.questions.aplus_core1",
    domains={
        1: {"name": "Mobile Devices", "weight": 0.13},
        2: {"name": "Networking", "weight": 0.23},
        3: {"name": "Hardware", "weight": 0.25},
        4: {"name": "Virtualization and Cloud Computing", "weight": 0.11},
        5: {"name": "Hardware and Network Troubleshooting", "weight": 0.28},
    },
    # A+ is scored 100-900 with a 675 pass mark (~75%).
    pass_percent=75.0,
    default_num_questions=90,
    default_pbqs=5,
    time_limit_min=90,
    blurb="PC technician fundamentals: mobile, networking, hardware, virtualization, and troubleshooting.",
    ai_system_prompt=(
        "You are an item writer for the CompTIA A+ Core 1 (220-1201) certification exam. "
        "Write questions indistinguishable from real 220-1201 items, calibrated to be AS "
        "HARD OR HARDER than the live exam: scenario-based, with plausible distractors that "
        "test real misconceptions and 'best answer' wording. The five domains are: 1 Mobile "
        "Devices; 2 Networking; 3 Hardware; 4 Virtualization and Cloud Computing; 5 Hardware "
        "and Network Troubleshooting."
    ),
)


# --------------------------------------------------------------------------- #
# A+ Core 2 (220-1202)                                                         #
# --------------------------------------------------------------------------- #
APLUS_CORE2 = ExamProfile(
    key="aplus_core2",
    name="CompTIA A+ Core 2 (220-1202)",
    short_name="A+ Core 2",
    questions_package="exam.questions.aplus_core2",
    domains={
        1: {"name": "Operating Systems", "weight": 0.28},
        2: {"name": "Security", "weight": 0.28},
        3: {"name": "Software Troubleshooting", "weight": 0.23},
        4: {"name": "Operational Procedures", "weight": 0.21},
    },
    # A+ is scored 100-900 with a 700 pass mark (~78%).
    pass_percent=78.0,
    default_num_questions=90,
    default_pbqs=5,
    time_limit_min=90,
    blurb="PC support, part 2: operating systems, security, software troubleshooting, and operational procedures.",
    ai_system_prompt=(
        "You are an item writer for the CompTIA A+ Core 2 (220-1202) certification exam. "
        "Write questions indistinguishable from real 220-1202 items, calibrated to be AS "
        "HARD OR HARDER than the live exam: scenario-based, with plausible distractors that "
        "test real misconceptions and 'best answer' wording. The four domains are: 1 "
        "Operating Systems; 2 Security; 3 Software Troubleshooting; 4 Operational Procedures."
    ),
)


# --------------------------------------------------------------------------- #
# Cisco CCNA (200-301)                                                         #
# --------------------------------------------------------------------------- #
CCNA = ExamProfile(
    key="ccna_200_301",
    name="Cisco CCNA (200-301)",
    short_name="CCNA",
    questions_package="exam.questions.ccna_200_301",
    domains={
        1: {"name": "Network Fundamentals", "weight": 0.20},
        2: {"name": "Network Access", "weight": 0.20},
        3: {"name": "IP Connectivity", "weight": 0.25},
        4: {"name": "IP Services", "weight": 0.10},
        5: {"name": "Security Fundamentals", "weight": 0.15},
        6: {"name": "Automation and Programmability", "weight": 0.10},
    },
    # CCNA does not publish a fixed passing score; ~825/1000 is the commonly
    # cited bar. We use 82% as the pass line for self-assessment.
    pass_percent=82.0,
    default_num_questions=100,
    default_pbqs=6,
    time_limit_min=120,
    blurb="Cisco networking: fundamentals, switching/wireless access, routing, IP services, security, and automation.",
    ai_system_prompt=(
        "You are an item writer for the Cisco CCNA 200-301 certification exam. "
        "Write questions indistinguishable from real 200-301 items, calibrated to be AS "
        "HARD OR HARDER than the live exam: scenario-based, with plausible distractors that "
        "test real misconceptions, configuration/output interpretation, and 'best answer' "
        "wording. The six domains are: 1 Network Fundamentals; 2 Network Access; 3 IP "
        "Connectivity; 4 IP Services; 5 Security Fundamentals; 6 Automation and "
        "Programmability."
    ),
)


EXAMS: dict[str, ExamProfile] = {
    SECPLUS.key: SECPLUS,
    APLUS_CORE1.key: APLUS_CORE1,
    APLUS_CORE2.key: APLUS_CORE2,
    CCNA.key: CCNA,
}

DEFAULT_EXAM = SECPLUS.key


def get_exam(key: str | None) -> ExamProfile:
    """Return the requested exam profile, falling back to the default."""
    return EXAMS.get(key or DEFAULT_EXAM, EXAMS[DEFAULT_EXAM])
