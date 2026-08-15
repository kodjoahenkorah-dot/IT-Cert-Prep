"""Shared pytest fixtures.

Loads every exam's bank once and exposes helpers so the individual test
modules stay focused on behaviour rather than setup.
"""

import pytest

from exam.bank import load_bank
from exam.catalog import EXAMS


@pytest.fixture(scope="session")
def profiles():
    """All registered exam profiles, keyed by exam key."""
    return dict(EXAMS)


@pytest.fixture(scope="session")
def banks(profiles):
    """Every exam's question bank, strictly validated on load.

    ``strict=True`` makes ``load_bank`` raise if any question fails schema
    validation, so simply building this fixture is itself an integration test.
    """
    return {key: load_bank(p.questions_package, strict=True) for key, p in profiles.items()}


# Convenient parametrization: (exam_key, profile) for every exam.
def pytest_generate_tests(metafunc):
    if "exam_key" in metafunc.fixturenames:
        metafunc.parametrize("exam_key", list(EXAMS.keys()))
