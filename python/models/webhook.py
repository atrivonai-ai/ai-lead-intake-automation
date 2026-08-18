"""
Webhook request models for the AI Lead Intake and Qualification Automation.
"""

from pydantic import BaseModel, ConfigDict

from python.models.lead import LeadInput


class LeadWebhookRequest(BaseModel):
    """Incoming payload received from an n8n webhook."""

    model_config = ConfigDict(extra="forbid")

    lead: LeadInput
