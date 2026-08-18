"""
Prompt construction for AI lead analysis.
"""


def build_lead_analysis_prompt(message: str) -> str:
    """Build the prompt used to analyze a lead message."""

    return f"""
Analyze the following business lead message.

Lead message:
{message}

Return ONLY a valid JSON object.

The JSON object must contain exactly these four fields:

{{
  "intent": "The lead's main intent.",
  "business_need": "The primary business problem or need.",
  "potential_value": "The potential business value.",
  "suggested_action": "The recommended next sales action."
}}

Strict output rules:
- Return JSON only.
- Do not use Markdown.
- Do not use code fences.
- Every value must be a string.
- intent must be 200 characters or fewer.
- business_need must be 200 characters or fewer.
- potential_value must be 50 characters or fewer.
- suggested_action must be 200 characters or fewer.
- Keep all answers concise and business-focused.
""".strip()