"""
Prompt construction for AI lead analysis.
"""

def build_lead_analysis_prompt(message: str) -> str:
    """Build the prompt used to analyze a business lead."""

    return f"""
Analyze the following business lead message.

Lead message:
{message}

Identify the following:

1. The lead's intent.
2. The primary business need.
3. The potential business value.
4. The most appropriate suggested action.
5. The action type the automation should execute.
6. A short natural summary that can be used in a personalized email.
7. Whether a discovery call booking is required.

Choose exactly one action_type from:

book_discovery_call
send_information
ask_clarifying_questions
sales_follow_up
nurture
no_action

Rules:

Use book_discovery_call when the lead is clearly ready for a consultation, assessment, implementation discussion, or discovery meeting.
Use send_information when the lead primarily wants information, service details, documentation, or educational material.
Use ask_clarifying_questions when the lead has a potentially relevant need but there is not enough information to recommend the next step.
Use sales_follow_up when the lead demonstrates strong commercial intent and should receive direct sales engagement.
Use nurture when the lead shows some potential interest but is not currently ready for a sales conversation.
Use no_action for irrelevant, false, test, spam, or clearly non-commercial submissions.
Set booking_required to true only when action_type is book_discovery_call or when the suggested action genuinely requires a discovery call.
Keep email_summary concise and natural.
Do not repeat the lead's message word-for-word.
Do not include the original lead message inside email_summary.
suggested_action should describe the appropriate next step in clear business language.
Do not invent information that the lead did not provide.

Return valid JSON only.

The JSON must contain exactly these fields:

{{
    "intent": "string",
    "business_need": "string",
    "potential_value": "string",
    "suggested_action": "string",
    "action_type": "book_discovery_call | send_information | ask_clarifying_questions | sales_follow_up | nurture | no_action",
    "email_summary": "string",
    "booking_required": true
}}

Keep all responses concise and business-focused.
""".strip()