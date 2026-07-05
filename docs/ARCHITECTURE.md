# SmartPrep AI Platform - Architecture

# Overview

SmartPrep AI Platform is a backend-driven AI learning platform that helps students organize study material, generate AI-powered learning resources, and analyze learning progress.

The project follows a modular architecture where every module has a single responsibility.

---

# Architecture Diagram

                    User
                      │
               Authentication
                      │
        ┌─────────────┴─────────────┐
        │                           │
     Subjects                   AI Tutor
        │                           │
        │                    Conversations
        │
      Notes
        │
        ├──────────────┬──────────────┬──────────────┐
        │              │              │              │
    Summary      Flashcards      Quiz      Interview Questions
                                      │
                               Quiz Attempts
                                      │
                                Analytics
                                      │
                                 Dashboard

---

# High Level Workflow

1. User registers and logs into the platform.

2. User creates study subjects.

3. User uploads notes (PDF, DOCX, TXT).

4. The uploaded notes are stored securely.

5. The user can choose to generate AI content.

6. Gemini processes the uploaded notes.

7. AI-generated content is stored in the database.

8. User attempts quizzes.

9. Quiz attempts are analyzed.

10. Analytics dashboard displays learning progress.

---

# Backend Architecture

Client

↓

Django REST Framework

↓

Views

↓

Services

↓

Database / Gemini API

↓

Response

The project separates business logic from API logic.

Views will only receive requests and return responses.

Business logic will gradually move into dedicated service classes as the project grows.

---

# Application Modules

## Accounts

Responsible for

- Registration
- Login
- JWT Authentication
- User Profile

---

## Subjects

Responsible for

- Creating Subjects
- Updating Subjects
- Deleting Subjects

---

## Notes

Responsible for

- Uploading Notes
- Viewing Notes
- Updating Notes
- Deleting Notes

---

## AI

Responsible for

- Prompt Building
- Gemini Integration
- AI Response Parsing

This module should never directly manage users or notes.

Its only responsibility is AI.

---

## Flashcards

Responsible for

Generating and storing flashcards.

---

## Quizzes

Responsible for

- Quiz Generation

- Quiz Questions

- Quiz Attempts

---

## Chat

Responsible for

AI Tutor conversations.

Stores

- User Messages

- AI Responses

- Chat History

---

## Analytics

Responsible for

- Quiz Analysis

- Subject Analysis

- Dashboard Statistics

- Charts

---

# Database Philosophy

The project uses PostgreSQL as a relational database.

The database follows normalization principles.

Relationships are maintained using foreign keys.

Duplicate information should be avoided whenever possible.

---

# AI Philosophy

AI content is generated only when requested by the user.

Generated content is stored.

If notes are updated,

AI content becomes

OUTDATED

and the user decides when to regenerate it.

---

# Security

Authentication will use JWT.

Passwords will always be hashed.

Users can only access their own data.

---

# Design Principles

The project follows these principles.

1. Single Responsibility Principle

Every module should have only one responsibility.

2. Separation of Concerns

AI logic should remain separate from business logic.

3. Modularity

Every feature should be easy to maintain and extend.

4. Scalability

The architecture should support future features without major redesign.

5. Simplicity

Avoid over-engineering.

Only introduce complexity when it solves a real problem.

---

# Future Architecture Improvements

- Background AI Tasks

- ML Recommendation Engine

- Semantic Search

- Notification Service

- AI Content Versioning

These features are intentionally postponed until Version 2.

---

# Goal

The goal of SmartPrep AI Platform is not only to generate AI content.

It is to build a maintainable, scalable backend application that demonstrates modern backend development, database design, AI integration, and software engineering principles.