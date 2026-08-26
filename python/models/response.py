"""
API response models for the AI Lead Intake and Qualification Automation.
"""

from pydantic import BaseModel, ConfigDict

from python.models.analysis import LeadAnalysis
from python.models.lead import LeadInput


class LeadProcessingResponse(BaseModel):
    """Response returned after processing a lead."""

    model_config = ConfigDict(extra="forbid")

    message: str
    status: str
    lead: LeadInput
    score: int
    priority: str
    analysis: LeadAnalysis