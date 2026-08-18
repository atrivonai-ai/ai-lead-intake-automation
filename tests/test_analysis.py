"""
Tests for the AI lead analysis service.
"""

from python.models.analysis import LeadAnalysis
from python.services import analysis


class FakeAIProvider:
    """Fake AI provider used for testing."""

    def __init__(self) -> None:
        self.received_prompt = None

    def analyze(self, message: str) -> str:
        """Return a predictable analysis result."""

        self.received_prompt = message
        return "Automation enquiry"


def test_analyze_lead_message(monkeypatch):
    """Test that the analysis service builds a prompt and returns LeadAnalysis."""

    fake_provider = FakeAIProvider()

    monkeypatch.setattr(
        analysis,
        "AIProvider",
        lambda: fake_provider,
    )

    result = analysis.analyze_lead_message(
        "We want to automate our lead management process."
    )

    assert isinstance(result, LeadAnalysis)
    assert result.intent == "Automation enquiry"
    assert "Analyze the following business lead message." in fake_provider.received_prompt
    assert "We want to automate our lead management process." in fake_provider.received_prompt
    assert result.business_need == "Not yet extracted"
    assert result.potential_value == "Not yet determined"
    assert result.suggested_action == "Not yet determined"
