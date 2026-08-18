"""
Deterministic lead scoring service.
"""

from python.models.lead import LeadInput
from python.models.score import LeadScore


def calculate_lead_score(lead: LeadInput) -> LeadScore:
    """Calculate a deterministic score and priority for a lead."""

    score = 0

    if lead.industry.lower() == "technology":
        score += 40

    if lead.lead_source.lower() == "referral":
        score += 15

    automation_keywords = [
        "automation",
        "automate",
        "automating",
        "lead management",
        "lead follow up",
        "follow-up",
        "workflow",
    ]

    message = lead.message.lower()

    if any(keyword in message for keyword in automation_keywords):
        score += 20

    if score >= 60:
        priority = "high"
    elif score >= 40:
        priority = "medium"
    else:
        priority = "low"

    return LeadScore(
        score=score,
        priority=priority,
    )