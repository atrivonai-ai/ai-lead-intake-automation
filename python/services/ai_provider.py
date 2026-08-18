"""
Gemini AI provider for lead analysis.
"""

from google import genai

from python.ai_config import AI_API_KEY, AI_MODEL


class AIProviderConfigurationError(RuntimeError):
    """Raised when the AI provider is not configured correctly."""


class AIProvider:
    """Client responsible for communicating with Google Gemini."""

    def __init__(self) -> None:
        if not AI_API_KEY:
            raise AIProviderConfigurationError(
                "AI provider API key is not configured."
            )

        self.client = genai.Client(api_key=AI_API_KEY)
        self.model = AI_MODEL

    def analyze(self, prompt: str) -> str:
        """Send a prompt to Gemini and return the generated text."""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return response.text