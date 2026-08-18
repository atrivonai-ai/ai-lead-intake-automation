# Lead Data Contract

## Purpose

Define the exact data structure that the lead intake system accepts.

## Required Fields

| Field | Type | Required |
|---|---|---|
| name | string | Yes |
| email | string | Yes |
| company | string | Yes |
| industry | string | Yes |
| lead_source | string | Yes |
| message | string | Yes |

## Example Lead

```json
{
  "name": "Sarah Johnson",
  "email": "sarah@example.com",
  "company": "BrightTech",
  "industry": "Technology",
  "lead_source": "Referral",
  "message": "We want to automate our lead management process."
}