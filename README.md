**# 🤖 AI Lead Intake & Qualification Automation**

> **A practical AI automation system that turns incoming leads into structured, routed, and actionable business workflows.**

---

## 🚀 Project Overview

This project automates the journey from **lead intake to qualification, record keeping, and follow up**.

The system uses **Python and FastAPI** for lead processing and **n8n** for workflow orchestration, connecting Google Calendar, Google Drive, Gmail, Notion, and GitHub.

### Core Value

**Less manual work → faster processing → consistent lead handling → automated follow up**

---

# 💼 Business Problem

Manual lead handling often requires teams to repeatedly review leads, check information, retrieve documents, update records, and send follow ups.

| Manual Task | Operational Impact |
|---|---|
| Review incoming leads | Slow response times |
| Check information | Repetitive administration |
| Retrieve documents | Manual effort |
| Update records | Inconsistent record keeping |
| Send follow ups | Missed opportunities |

The automation converts these repetitive activities into a **repeatable business workflow**.

---

# ⚙️ Solution Architecture

The workflow separates **lead processing** from **workflow orchestration**.

```text
                    INCOMING LEAD
                         │
                         ▼
                      Webhook
                         │
                         ▼
                   HTTP Request
                         │
                         ▼
                  FastAPI / Python
                         │
                         ▼
                        If
                    ┌────┴────┐
                    │         │
                  TRUE      FALSE
                    │         │
                    ▼         ▼
              Edit Fields  Edit Fields1
                    │         │
                    ▼         ▼
             Google Calendar Google Drive
                    │         │
                    ▼         ├────────→ Notion
                  Merge       │
                 ┌──┴──┐      └────────→ Send an Email1
                 │     │
                 ▼     ▼
              Notion Edit Fields2
                       │
                       ▼
                  Send an Email

Workflow preserved: Both branches ultimately create a record in Notion, while each branch retains its own follow up process.

**🔄 Workflow Logic**

01 · Webhook

The Webhook receives the incoming lead processing request and starts the automation.

02 · HTTP Request

The HTTP Request sends the lead information to the FastAPI service, separating processing logic from n8n orchestration.

03 · If Node

The If node evaluates the processed lead and routes it to either the True or False path.

🟢 TRUE PATH · Calendar Workflow
If
 ↓
Edit Fields
 ↓
Google Calendar
 ↓
Merge
 ├────────→ Notion
 │
 └────────→ Edit Fields2
                ↓
           Send an Email

**Node Function**

Edit-Fields	Prepares data for the calendar stage
Google Calendar-Retrieves relevant calendar events
Merge-Receives the calendar result and continues to two downstream actions
Notion-Creates the lead database record
Edit Fields2-Prepares final email information
Send an Email-Sends the True path follow up

🔴 FALSE PATH · Information Retrieval Workflow

If
 ↓
Edit Fields1
 ↓
Google Drive
 ├────────→ Notion
 │
 └────────→ Send an Email1
Node	Function
Edit Fields1	Prepares data for Google Drive
Google Drive	Retrieves the relevant file
Notion	Creates the lead database record
Send an Email1	Sends the False path communication

🗂️ Centralized Record Keeping

A key design feature is the shared Notion destination.

TRUE PATH
Merge
  ↓
Notion
  ↑
  │
FALSE PATH
Google Drive
  ↓
Notion

Both outcomes are recorded in the same Notion database, providing consistent lead tracking while preserving different follow up workflows.

📧 Automated Communication
Path	Email Flow
🟢 True	Merge → Edit Fields2 → Send an Email
🔴 False	Google Drive → Send an Email1

## Automation Workflow



This workflow receives the lead, validates the information, analyzes the lead, determines the appropriate action, and routes the lead through the relevant automation.

<img width="797" height="323" alt="main n8n workflow" src="https://github.com/user-attachments/assets/5037d4ee-3638-408e-b12f-9622696f6f12" />

### Workflow Demo

The video demonstrates the complete automation from lead submission through AI analysis, routing, email delivery, scheduling, and lead record creation.

https://drive.google.com/file/d/1SLpliX-NLUBn6lyU7_VwAtfsODpb4IfT/view?usp=sharing


## Meeting Scheduling

When a lead requires a meeting, the workflow provides the lead with the option to schedule a discovery call.

<img width="737" height="277" alt="booking link email" src="https://github.com/user-attachments/assets/939f02d4-426e-4670-87da-698380f45cba" />


## Brochure Delivery

When a lead requests information, the workflow automatically sends a professional email with the relevant brochure.

<img width="734" height="358" alt="Email with brochure attached" src="https://github.com/user-attachments/assets/cd1a0138-297a-4d37-bd83-b6cff975ac5a" />


## Lead Record in Notion

The qualified lead is automatically added to Notion with the relevant lead information and qualification details.

<img width="877" height="230" alt="Notion_lead_database_1" src="https://github.com/user-attachments/assets/f652a1ca-0612-4cee-a438-f289eb94bbb8" />

<img width="944" height="268" alt="Notion_lead_database_2" src="https://github.com/user-attachments/assets/9dc5baab-9fc9-453b-a327-788b38fb52f5" />

**🧩 Technology Stack**

Technology	Purpose
Python-Lead processing logic
FastAPI-API layer
n8n-Workflow orchestration
Google Calendar-Calendar event retrieval
Google Drive-File retrieval
Gmail-Automated email delivery
Notion-Centralized lead records
GitHub-Version control and portfolio presentation

🧠 Automation Patterns Demonstrated

Pattern	Demonstrated Capability
🔌 API Integration	n8n connected to FastAPI through HTTP
🔀 Conditional Routing	If node determines workflow path
📅 Calendar Integration	Calendar data retrieval
📁 File Retrieval	Google Drive document retrieval
⚡ Parallel Actions	Branch outputs support multiple actions
🗃️ Centralized Records	Both outcomes create Notion records
✉️ Automated Communication	Separate email flows for each outcome
📈 Business Value

This automation transforms manual lead handling into a structured, repeatable process.

Before	                   After
Manual lead review	       Automated processing
Manual routing	           Conditional routing
Manual calendar checks	   Automated Calendar integration
Manual document retrieval	 Automated Drive retrieval
Manual record updates	     Automated Notion records
Manual follow ups	         Automated email communication
Disconnected systems	     One connected workflow

**Impact**

Faster lead processing · Reduced administration · Consistent handling · Centralized records · Automated follow up · Multi system integration

🛠️ Skills Demonstrated

AI assisted lead processing · Python · FastAPI · REST APIs · n8n · Workflow orchestration · Conditional routing · Google Calendar · Google Drive · Gmail · Notion · Data transformation · Business process automation · Multi system integration

🔮 Future Improvements

Error handling-Handle integration failures
Retry logic	Retry-failed operations
Execution logging-Improve workflow visibility
Lead status tracking-Track lead progression
Automated testing-Improve reliability
Monitoring & reporting-Measure workflow performance
Conversion analytics-Measure lead outcomes

🎯 Project Outcome

The completed automation demonstrates:

Lead Intake
   ↓
Webhook
   ↓
API Processing
   ↓
Conditional Routing
   ↓
┌──────────────────┬──────────────────┐
│ TRUE             │ FALSE            │
│ Calendar         │ Google Drive     │
│ ↓                │ ↓                │
│ Merge            │ Notion           │
│ ↓                │ ↓                │
│ Notion           │ Email            │
│ ↓                │                  │
│ Email            │                  │
└──────────────────┴──────────────────┘


The project demonstrates the ability to translate a business process into an automated, multi system workflow connecting API processing, business logic, external services, database operations, and communication.

⭐ Key Takeaway

The value is not simply connecting tools. It is designing a workflow where each system performs a specific business function and the entire process operates as one repeatable automation.
