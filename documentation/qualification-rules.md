# Lead Qualification Rules

## Purpose

Define the deterministic rules used to calculate a lead's qualification score and priority.

## Scoring Rules

| Condition | Points |
|---|---:|
| Industry is Technology | +40 |
| Lead source is Referral | +15 |
| Message indicates an automation need | +20 |

## Priority Rules

| Score | Priority |
|---:|---|
| 60–75 | High |
| 40–59 | Medium |
| 0–39 | Low |

## Important Design Rule

AI may interpret the lead's message and identify whether an automation need exists.

The final numeric score and priority are calculated by deterministic business rules.

AI must not independently invent the final score or priority.

## Example

A Technology lead from a Referral source with an automation-related message:

40 + 15 + 20 = 75

Priority:

High