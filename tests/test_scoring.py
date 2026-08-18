"""
Tests for deterministic lead scoring.
"""

from python.models.lead import LeadInput
from python.services.scoring import calculate_lead_score


def test_high_priority_lead():
    lead = LeadInput(
        name="Sarah Johnson",
        email="sarah@example.com",
        company="BrightTech",
        industry="Technology",
        lead_source="Referral",
        message="We want to automate our lead management process.",
    )

    result = calculate_lead_score(lead)

    assert result.score == 75
    assert result.priority == "high"


def test_medium_priority_lead():
    lead = LeadInput(
        name="John Smith",
        email="john@example.com",
        company="Example Co",
        industry="Technology",
        lead_source="Website",
        message="We are interested in your services.",
    )

    result = calculate_lead_score(lead)

    assert result.score == 40
    assert result.priority == "medium"


def test_low_priority_lead():
    lead = LeadInput(
        name="Mary Jones",
        email="mary@example.com",
        company="Local Shop",
        industry="Retail",
        lead_source="Website",
        message="I would like some information.",
    )

    result = calculate_lead_score(lead)

    assert result.score == 0
    assert result.priority == "low"
