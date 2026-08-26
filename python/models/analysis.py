"""
AI analysis models for the AI Lead Intake and Qualification Automation.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class LeadAnalysis(BaseModel):
    """Structured information extracted from a lead message by AI."""

    model_config = ConfigDict(extra="forbid")

    intent: str = Field(min_length=1, max_length=200)
    business_need: str = Field(min_length=1, max_length=500)
    potential_value: str = Field(min_length=1, max_length=200)
    suggested_action: str = Field(min_length=1, max_length=300)

    action_type: Literal[
        "book_discovery_call",
        "send_information",
        "ask_clarifying_questions",
        "sales_follow_up",
        "nurture",
        "no_action",
    ]

    email_summary: str = Field(min_length=1, max_length=300)

    booking_required: bool