# Project Requirements

## 1. Functional Requirements

### Lead Intake

The system must:

- Receive leads through an HTTP webhook.
- Accept the defined lead data contract.
- Preserve the original submitted information.

### Data Validation

The system must:

- Check all required fields.
- Reject missing fields.
- Reject empty values.
- Validate email format.
- Stop invalid submissions before AI processing.

### AI Analysis

The system must:

- Analyze the lead message.
- Identify lead intent.
- Identify the business need.
- Determine potential business value.
- Determine whether an automation need exists.
- Produce a suggested follow-up action.
- Return structured data according to the AI Analysis Contract.

### Qualification

The system must:

- Calculate a deterministic lead score.
- Apply the defined qualification rules.
- Assign High, Medium, or Low priority.
- Keep scoring independent from AI-generated scoring.

### Notion

The system must:

- Create a Notion record for successfully processed leads.
- Store the complete required lead information.
- Store AI analysis results.
- Store the calculated score and priority.
- Set the initial lead status to `New`.

### Follow-Up

The system must:

- Create a follow-up action for successfully qualified leads.
- Assign the action according to the final priority.
- Set the initial follow-up status to `Pending`.

### Error Handling

The system must:

- Detect validation failures.
- Detect AI failures.
- Detect invalid AI responses.
- Detect qualification failures.
- Detect Notion failures.
- Detect follow-up failures.
- Preserve relevant data when failures occur.
- Make failures visible.
- Never silently treat a failed operation as successful.

---

## 2. Non-Functional Requirements

### Reliability

The workflow should behave predictably when receiving valid and invalid data.

### Maintainability

The implementation should use clear component boundaries and documented interfaces.

### Security

Sensitive credentials must not be stored directly in source code.

### Data Integrity

Original lead information must not be silently changed during processing.

### Observability

Important processing failures must be identifiable and traceable.

### Scalability

The architecture should allow additional lead sources, scoring rules, AI analysis fields, and follow-up actions to be added without rebuilding the entire system.

---

## 3. Technology Requirements

The initial implementation will use:

- n8n
- Python
- FastAPI where a Python service is required
- AI API
- Notion API
- Git
- GitHub

Each technology must have a genuine role in the system.

---

## 4. Implementation Constraints

The project must:

- Be built as a real working automation.
- Avoid unnecessary components.
- Avoid placeholder functionality in the final implementation.
- Keep business rules deterministic.
- Use AI for interpretation rather than uncontrolled decision-making.
- Keep configuration separate from source code.
- Keep credentials outside the repository.

---

## 5. Completion Requirements

The project is complete when:

1. A real lead can enter through the webhook.
2. Valid data passes validation.
3. AI analysis executes successfully.
4. The AI response is validated.
5. The lead is scored correctly.
6. Priority is assigned correctly.
7. The lead is stored in Notion.
8. A follow-up action is created.
9. Invalid input is rejected correctly.
10. Processing failures are handled visibly.
11. The implementation is documented.
12. The project is committed to GitHub.