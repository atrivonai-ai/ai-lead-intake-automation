"""
API response models for the AI Lead Intake and Qualification Automation.
"""

from pydantic import BaseModel, ConfigDict


class LeadProcessingResponse(BaseModel):
    """Response returned after processing a lead."""

    model_config = ConfigDict(extra="forbid")

    message: str
    status: str
