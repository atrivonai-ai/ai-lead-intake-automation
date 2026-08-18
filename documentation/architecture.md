# System Architecture

## Purpose

Define the technical architecture of the AI Lead Intake and Qualification Automation.

## Architecture

```text
                    External Lead Source
                           │
                           ▼
                    ┌──────────────┐
                    │  n8n Webhook │
                    └──────┬───────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Input Validation │
                  └────────┬─────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ AI Analysis │
                    └──────┬──────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ AI Response      │
                 │ Validation       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Lead Qualification│
                 │ & Scoring        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Priority         │
                 │ Assignment       │
                 └────────┬─────────┘
                          │
                    ┌─────┴─────┐
                    ▼           ▼
              ┌──────────┐  ┌──────────────┐
              │  Notion  │  │ Follow-Up    │
              │ Database │  │ Action       │
              └──────────┘  └──────────────┘