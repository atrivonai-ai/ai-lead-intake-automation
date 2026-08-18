# Notion Data Structure

## Purpose

Define the exact structure of the lead record that will be stored in Notion after successful processing.

## Lead Record

Each processed lead will contain the following information:

| Field | Type | Source |
|---|---|---|
| Name | Title | Lead submission |
| Email | Email | Lead submission |
| Company | Text | Lead submission |
| Industry | Select | Lead submission |
| Lead Source | Select | Lead submission |
| Message | Text | Lead submission |
| Score | Number | Qualification rules |
| Priority | Select | Qualification rules |
| AI Intent | Text | AI analysis |
| Business Need | Text | AI analysis |
| Potential Value | Select | AI analysis |
| Automation Need | Checkbox | AI analysis |
| Suggested Action | Text | AI analysis |
| Status | Select | Automation |
| Created At | Date | Automation |

## Status

The initial status for a successfully processed lead is:

`New`

## Priority Values

The priority field will contain:

- High
- Medium
- Low

## Potential Value Values

The potential value field will contain:

- High
- Medium
- Low

## Data Integrity

The automation must preserve the original lead information.

AI-generated information must remain separate from the original submitted information.

The score and priority must be generated from the defined qualification rules.

## Record Creation

A Notion record should only be created after:

1. The incoming lead passes validation.
2. AI analysis succeeds.
3. The AI response passes validation.
4. The qualification score is calculated successfully.
5. The priority is assigned successfully.

If any required processing stage fails, the system must follow its error-handling process instead of creating an incomplete lead record.