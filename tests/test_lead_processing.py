"""
Tests for the lead processing service.
"""

from python.models.analysis import LeadAnalysis
from python.models.lead import LeadInput
from python.services import lead_processing


def test_process_lead(monkeypatch):
    """Test that lead processing combines scoring, AI analysis, and Notion storage."""

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

    class FakeNotionService:
        def create_lead(self, **kwargs):
            assert kwargs["name"] == "Sarah Johnson"
            assert kwargs["email"] == "sarah@example.com"
            assert kwargs["company"] == "BrightTech"
            assert kwargs["score"] == 75
            assert kwargs["priority"] == "high"
            assert kwargs["status"] == "New"
            assert kwargs["suggested_action"] == "Schedule discovery call"
            assert kwargs["ai_intent"] == "Automation enquiry"
            assert kwargs["business_need"] == "Lead management automation"

            return {
                "id": "test-notion-page-id",
                "object": "page",
            }

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

    monkeypatch.setattr(
        lead_processing,
        "NotionService",
        FakeNotionService,
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
    assert result.notion_page_id == "test-notion-page-id"