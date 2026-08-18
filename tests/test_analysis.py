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
        """Return a predictable structured analysis result."""

        self.received_prompt = message

        return """
{
  "intent": "Automate lead management",
  "business_need": "Improve lead tracking and qualification",
  "potential_value": "Higher sales efficiency",
  "suggested_action": "Schedule a discovery call"
}
""".strip()


def test_analyze_lead_message(monkeypatch):
    """Test that the analysis service returns structured LeadAnalysis data."""

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

    assert result.intent == "Automate lead management"
    assert result.business_need == "Improve lead tracking and qualification"
    assert result.potential_value == "Higher sales efficiency"
    assert result.suggested_action == "Schedule a discovery call"

    assert "Analyze the following business lead message." in fake_provider.received_prompt
    assert "We want to automate our lead management process." in fake_provider.received_prompt