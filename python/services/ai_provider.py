"""
AI provider client for the AI Lead Intake and Qualification Automation.
"""

from python.ai_config import AI_API_KEY, AI_MODEL


class AIProvider:
    """Client responsible for communicating with the configured AI provider."""

    def __init__(self) -> None:
        self.api_key = AI_API_KEY
        self.model = AI_MODEL

    def analyze(self, message: str) -> str:
        """Analyze a lead message using the configured AI provider."""

        raise NotImplementedError(
            "AI provider connection has not been implemented yet."
        )
