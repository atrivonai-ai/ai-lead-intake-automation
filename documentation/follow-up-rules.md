# Follow-Up Rules

## Purpose

Define what action the automation creates after a lead has been successfully qualified.

## Follow-Up Decision

The follow-up action is based on the qualified lead information.

### High Priority

Recommended action:

`Schedule discovery call`

### Medium Priority

Recommended action:

`Send qualification follow-up`

### Low Priority

Recommended action:

`Add to nurture follow-up`

## Source of the Recommendation

The AI may provide a suggested action based on the lead's message.

The automation must also consider the final deterministic priority when creating the follow-up action.

The final workflow must not blindly execute an AI recommendation without applying the defined business rules.

## Follow-Up Record

The follow-up action must contain:

- Lead name
- Company
- Email
- Priority
- Action
- Created At
- Status

## Initial Follow-Up Status

Every newly created follow-up action starts with:

`Pending`

## Follow-Up Status Values

The system will support:

- Pending
- Completed
- Failed

## Failure Handling

If the follow-up action cannot be created:

1. The lead record must not be silently treated as fully processed.
2. The failure must be recorded.
3. The system must make the failure visible for later resolution.

## Design Principle

Lead qualification and follow-up creation are separate stages.

A lead can be successfully qualified even if the follow-up action fails.