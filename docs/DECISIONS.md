# Technical Decisions

## Overview

This document explains the major technical decisions made during the development of SmartPrep AI Platform and the reasons behind them.

---

# Choosing Django

## Decision

The backend was developed using Django.

## Reasons

Django was selected because:

- It provides a complete web framework
- Built-in authentication system
- Powerful ORM
- Secure default settings
- Fast development process
- Large community support

Django's MVT architecture helped keep the application organized.

---

# Choosing PostgreSQL

## Decision

The project migrated from SQLite to PostgreSQL.

## Reasons

SQLite was useful during initial development, but PostgreSQL was chosen for production because:

- Better handling of relational data
- Production-ready database system
- Improved scalability
- Better support for complex applications

---

# Choosing Django ORM

## Decision

The project uses Django ORM instead of writing raw SQL queries.

## Reasons

Benefits:

- Faster development
- Database abstraction
- Safer queries
- Easier model relationships

Example:

Instead of writing SQL:

```sql
SELECT * FROM notes;
```

Django allows:

```python
Note.objects.all()
```

---

# Choosing Gemini AI

## Decision

Gemini AI was integrated for AI-powered learning features.

## Reasons

The AI service is used for:

- Generating summaries
- Creating flashcards
- Generating quizzes

The AI logic was separated into a service layer to keep the application flexible.

---

# AI Service Layer

## Decision

AI functionality was separated from Django views.

Structure:

```
views.py

↓

ai_service.py

↓

Gemini API
```

## Reasons

Benefits:

- Cleaner views
- Easier debugging
- Easier AI provider replacement
- Better code organization

---

# Choosing Docker

## Decision

Docker was introduced for development and deployment.

## Reasons

Docker provides:

- Consistent environments
- Easier setup
- Container isolation
- Simplified deployment

The final setup contains:

```
Django Container

+

PostgreSQL Container
```

---

# Choosing Bootstrap

## Decision

Bootstrap was used for frontend styling.

## Reasons

Initially the project used plain HTML.

Bootstrap was introduced because:

- Faster UI development
- Responsive components
- Cleaner design
- Less custom CSS required

---

# Choosing Render

## Decision

Render was selected for deployment.

## Reasons

Render provides:

- Simple deployment workflow
- GitHub integration
- Managed databases
- Easy hosting for Django applications

---

# Environment Variable Management

## Decision

Sensitive configuration was moved to environment variables.

Examples:

```
DATABASE_PASSWORD
DATABASE_HOST
GEMINI_API_KEY
DEBUG
```

## Reasons

Benefits:

- Better security
- Different settings for local and production environments
- Avoid exposing secrets in GitHub

---

# Database Host Decision

Different environments required different database hosts.

Local:

```
DB_HOST=localhost
```

Docker:

```
DB_HOST=db
```

Production:

```
DB_HOST=<production database hostname>
```

Reason:

Each environment has a different networking setup.

---

# Future Technical Decisions

Possible future improvements:

- REST API using Django REST Framework
- Background tasks using Celery
- Redis caching
- Automated testing
- CI/CD pipeline