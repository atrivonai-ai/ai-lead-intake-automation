# AI Analysis Contract

## Purpose

Define exactly what the AI must analyze and return for each valid lead.

## AI Responsibilities

The AI analyzes the lead's message and identifies:

- Lead intent
- Business need
- Potential business value
- Whether the lead has an automation-related need
- Recommended follow-up action

The AI does not calculate the final lead score or priority.

## Input

The AI receives:

```json
{
  "name": "Sarah Johnson",
  "company": "BrightTech",
  "industry": "Technology",
  "lead_source": "Referral",
  "message": "We want to automate our lead management process."
}