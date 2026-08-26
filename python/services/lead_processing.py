"""
Lead processing service for the AI Lead Intake and Qualification Automation.
"""

from python.models.analysis import LeadAnalysis
from python.models.lead import LeadInput
from python.models.score import LeadScore
from python.services.analysis import analyze_lead_message
from python.services.scoring import calculate_lead_score


class ProcessedLead(LeadInput):
    """Lead data combined with scoring and AI analysis results."""

    score: int
    priority: str
    analysis: LeadAnalysis


def process_lead(lead: LeadInput) -> ProcessedLead:
    """Validate, analyze, and score a lead."""

    score: LeadScore = calculate_lead_score(lead)
    analysis: LeadAnalysis = analyze_lead_message(lead.message)

    return ProcessedLead(
        **lead.model_dump(),
        score=score.score,
        priority=score.priority,
        analysis=analysis,
    )