"""
AI analysis service for the AI Lead Intake and Qualification Automation.
"""

from python.models.analysis import LeadAnalysis
from python.services.ai_provider import AIProvider
from python.services.prompt import build_lead_analysis_prompt


def analyze_lead_message(message: str) -> LeadAnalysis:
    """
    Analyze a lead message using the configured AI provider.
    """

    prompt = build_lead_analysis_prompt(message)

    provider = AIProvider()
    raw_analysis = provider.analyze(prompt)

    return LeadAnalysis(
        intent=raw_analysis,
        business_need="Not yet extracted",
        potential_value="Not yet determined",
        suggested_action="Not yet determined",
    )
