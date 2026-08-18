"""
Webhook API endpoint for the AI Lead Intake and Qualification Automation.
"""

from fastapi import APIRouter

from python.models.response import LeadProcessingResponse
from python.models.webhook import LeadWebhookRequest
from python.services.lead_processing import process_lead


router = APIRouter(prefix="/webhook", tags=["webhook"])


@router.post("/lead", response_model=LeadProcessingResponse)
def receive_lead_webhook(
    payload: LeadWebhookRequest,
) -> LeadProcessingResponse:
    """Receive a lead from an external webhook such as n8n."""

    processed_lead = process_lead(payload.lead)

    return LeadProcessingResponse(
        message=f"Lead processed with {processed_lead.priority} priority.",
        status="success",
    )
