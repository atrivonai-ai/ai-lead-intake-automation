# AI Lead Intake & Qualification Automation

An AI-powered lead intake and qualification system that automatically receives new leads, analyzes their intent and quality, assigns a qualification score, and routes them into the appropriate follow-up process.

The system combines **FastAPI, Python, n8n, Google Gemini, Gmail, Google Drive, Google Calendar, and Notion** to automate the lead journey from initial inquiry to business action.

---

## 🚀 Project Overview

Businesses often receive leads through forms, websites, or other channels but still rely on manual processes to:

- Review incoming leads
- Determine lead quality
- Decide who needs immediate attention
- Send follow-up information
- Schedule qualified prospects
- Update lead records

This project automates that workflow.

A new lead enters the system, is analyzed by AI, scored based on qualification criteria, and automatically routed to the appropriate next step.

---

## 🎯 Business Problem

Manual lead qualification can result in:

- Slow response times
- Inconsistent lead scoring
- Missed opportunities
- Repetitive administrative work
- Leads receiving the wrong follow-up
- Poor visibility into the sales pipeline

The goal of this automation is to reduce manual intervention while ensuring every lead receives an appropriate response.

---

## 💡 Solution

The system creates an automated lead-processing pipeline:

```text
Lead Submission
      ↓
     n8n
      ↓
FastAPI Lead Processing API
      ↓
Google Gemini AI Analysis
      ↓
Lead Qualification & Scoring
      ↓
   ┌───────────────┐
   │               │
Qualified       Low Lead
   │               │
   ↓               ↓
Booking         Brochure
   │               │
   ↓               ↓
Google Calendar  Email
                   ↓
              Google Drive
   │               │
   └───────┬───────┘
           ↓
      Lead Database
         / Notion
