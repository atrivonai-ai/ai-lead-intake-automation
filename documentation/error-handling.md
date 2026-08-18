# Error Handling

## Purpose

Define how the automation handles failures without silently losing or corrupting lead data.

## Error Categories

### 1. Validation Error

Occurs when incoming lead data does not satisfy the lead data contract.

Examples:

- Missing name
- Missing email
- Invalid email
- Missing company
- Missing industry
- Missing lead source
- Missing message

Action:

- Reject the lead.
- Return a clear validation error.
- Do not send the lead to AI analysis.
- Do not create a Notion lead record.

---

### 2. AI Analysis Error

Occurs when the AI service fails or returns unusable data.

Examples:

- API failure
- Timeout
- Invalid structured response
- Missing required AI fields

Action:

- Do not continue qualification using incomplete AI data.
- Record the failure.
- Make the failure visible for resolution.
- Do not create an incomplete Notion record.

---

### 3. Qualification Error

Occurs when the scoring or priority calculation fails.

Action:

- Do not create the final processed lead record.
- Record the failure.
- Make the failure visible for resolution.

---

### 4. Notion Error

Occurs when the system cannot create or update the Notion record.

Action:

- Record the failure.
- Preserve the processed lead information.
- Make the failure visible for retry or manual resolution.

---

### 5. Follow-Up Error

Occurs when the follow-up action cannot be created.

Action:

- Preserve the qualified lead.
- Record the follow-up failure.
- Mark the follow-up as failed.
- Make the failure visible for retry or manual resolution.

---

## General Rules

The system must:

1. Never silently discard a lead.
2. Never treat a failed operation as successful.
3. Never create records using incomplete required data.
4. Preserve the original lead information.
5. Make failures identifiable.
6. Separate processing failures from business decisions.
7. Allow failed operations to be investigated and retried where appropriate.

## Processing Principle

A lead is considered successfully processed only when all required processing stages have completed successfully.