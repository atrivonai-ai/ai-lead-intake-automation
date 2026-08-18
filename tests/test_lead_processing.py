"""
Tests for the lead processing service.
"""

from python.models.analysis import LeadAnalysis
from python.models.lead import LeadInput
from python.services import lead_processing


def test_process_lead(monkeypatch):
    """Test that lead processing combines scoring and AI analysis."""

    def fake_score(lead):
        return type(
            "FakeScore",
            (),
            {
                "score": 75,
                "priority": "high",
            },
        )()

    def fake_analysis(message):
        return LeadAnalysis(
            intent="Automation enquiry",
            business_need="Lead management automation",
            potential_value="High",
            suggested_action="Schedule discovery call",
        )

    monkeypatch.setattr(
        lead_processing,
        "calculate_lead_score",
        fake_score,
    )

    monkeypatch.setattr(
        lead_processing,
        "analyze_lead_message",
        fake_analysis,
    )

    lead = LeadInput(
        name="Sarah Johnson",
        email="sarah@example.com",
        company="BrightTech",
        industry="Technology",
        lead_source="Referral",
        message="We want to automate our lead management process.",
    )

    result = lead_processing.process_lead(lead)

    assert result.name == "Sarah Johnson"
    assert result.score == 75
    assert result.priority == "high"
    assert result.analysis.intent == "Automation enquiry"
    assert result.analysis.business_need == "Lead management automation"
    assert result.analysis.potential_value == "High"
    assert result.analysis.suggested_action == "Schedule discovery call"
