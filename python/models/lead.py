"""
Lead data models for the AI Lead Intake and Qualification Automation.
"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class LeadInput(BaseModel):
    """Validated information received for a new lead."""

    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    company: str = Field(min_length=1, max_length=150)
    industry: str = Field(min_length=1, max_length=100)
    lead_source: str = Field(min_length=1, max_length=100)
    message: str = Field(min_length=1, max_length=5000)