"""
Lead processing service for the AI Lead Intake and Qualification Automation.
"""

from python.models.analysis import LeadAnalysis
from python.models.lead import LeadInput
from python.models.score import LeadScore
from python.services.analysis import analyze_lead_message
from python.services.notion import NotionService
from python.services.scoring import calculate_lead_score


class ProcessedLead(LeadInput):
    """Lead data combined with scoring and AI analysis results."""

    score: int
    priority: str
    analysis: LeadAnalysis
    notion_page_id: str


def process_lead(lead: LeadInput) -> ProcessedLead:
    """Validate, analyze, score, and store a lead in Notion."""

    score: LeadScore = calculate_lead_score(lead)
    analysis: LeadAnalysis = analyze_lead_message(lead.message)

    notion_service = NotionService()

    notion_record = notion_service.create_lead(
        name=lead.name,
        email=lead.email,
        company=lead.company,
        industry=lead.industry,
        lead_source=lead.lead_source,
        message=lead.message,
        score=score.score,
        priority=score.priority.capitalize(),
        status="New",
        suggested_action=analysis.suggested_action,
        ai_intent=analysis.intent,
        business_need=analysis.business_need,
    )

    return ProcessedLead(
        **lead.model_dump(),
        score=score.score,
        priority=score.priority,
        analysis=analysis,
        notion_page_id=notion_record["id"],
    )