"""
Lead scoring models for the AI Lead Intake and Qualification Automation.
"""

from typing import Literal

from pydantic import BaseModel, Field


class LeadScore(BaseModel):
    """Result produced by the deterministic lead scoring system."""

    score: int = Field(ge=0, le=75)
    priority: Literal["low", "medium", "high"]