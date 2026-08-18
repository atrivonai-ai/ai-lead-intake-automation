"""
Lead API endpoints for the AI Lead Intake and Qualification Automation.
"""

from fastapi import APIRouter, HTTPException

from python.models.lead import LeadInput
from python.models.response import LeadProcessingResponse
from python.services.ai_provider import AIProviderConfigurationError
from python.services.lead_processing import process_lead


router = APIRouter(prefix="/leads", tags=["leads"])


@router.post("/process", response_model=LeadProcessingResponse)
def process_lead_endpoint(lead: LeadInput) -> LeadProcessingResponse:
    """Receive and process a new lead."""

    try:
        processed_lead = process_lead(lead)
    except AIProviderConfigurationError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc

    return LeadProcessingResponse(
        message=f"Lead processed with {processed_lead.priority} priority.",
        status="success",
    )