"""
Prompt construction for AI lead analysis.
"""


def build_lead_analysis_prompt(message: str) -> str:
    """Build the prompt used to analyze a lead message."""

    return f"""
Analyze the following business lead message.

Lead message:
{message}

Identify:

1. The lead's intent.
2. The primary business need.
3. The potential business value.
4. The most appropriate suggested action.

Return concise, business-focused information.
""".strip()
