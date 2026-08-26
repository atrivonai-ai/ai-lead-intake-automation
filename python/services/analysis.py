"""
AI analysis service for the AI Lead Intake and Qualification Automation.
"""

import json

from pydantic import ValidationError

from python.models.analysis import LeadAnalysis
from python.services.ai_provider import AIProvider
from python.services.prompt import build_lead_analysis_prompt


def _parse_ai_response(raw_response: str) -> LeadAnalysis:
    """Parse the structured JSON returned by the AI provider."""

    cleaned_response = raw_response.strip()

    if cleaned_response.startswith("```"):
        lines = cleaned_response.splitlines()

        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        cleaned_response = "\n".join(lines).strip()

    try:
        parsed_response = json.loads(cleaned_response)
    except json.JSONDecodeError as exc:
        raise ValueError(
            "AI provider returned invalid JSON."
        ) from exc

    try:
        return LeadAnalysis.model_validate(parsed_response)
    except ValidationError as exc:
        raise ValueError(
            "AI provider returned JSON that does not match "
            f"the lead analysis contract. "
            f"Validation error: {exc}. "
            f"AI response: {parsed_response}"
        ) from exc


def analyze_lead_message(message: str) -> LeadAnalysis:
    """Analyze a lead message using the configured AI provider."""

    prompt = build_lead_analysis_prompt(message)

    provider = AIProvider()
    raw_analysis = provider.analyze(prompt)

    return _parse_ai_response(raw_analysis)