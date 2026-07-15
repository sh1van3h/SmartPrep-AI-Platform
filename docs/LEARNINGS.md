# Learnings

## Overview

SmartPrep AI Platform was developed as a learning project to understand full-stack backend development, AI integration, database management, Docker, and production deployment.

Throughout the development process, several technical concepts and real-world problems were explored.

---

# Django Development

## Learned

- Django project structure
- Applications and modules
- URL routing
- Views
- Templates
- Model creation
- Django ORM
- Authentication system
- Template inheritance
- Migrations

---

# Django MVT Architecture

Learned how Django separates application responsibilities.

Structure:

```
Model

↓

View

↓

Template
```

## Model

Responsible for:

- Database structure
- Relationships
- Data operations


## View

Responsible for:

- Handling requests
- Business logic
- Returning responses


## Template

Responsible for:

- User interface
- Displaying data

---

# Database Management

## Learned

- Relational database concepts
- PostgreSQL setup
- Foreign key relationships
- Database migrations
- Data modeling


Important concepts:

- One-to-many relationships
- Data normalization
- ORM queries

---

# Authentication

Implemented:

- User registration
- Login system
- Logout system
- Protected routes


Learned:

- Django authentication framework
- Sessions
- User authorization
- Login decorators

---

# AI Integration

Implemented AI-powered features:

- Summary generation
- Flashcard generation
- Quiz generation


Learned:

- API integration
- Sending prompts
- Processing AI responses
- Separating AI logic from application logic

---

# AI Service Architecture

A separate AI service layer was created.

Structure:

```
Django View

↓

AI Service

↓

Gemini API
```

Benefits learned:

- Cleaner code
- Easier debugging
- Better maintainability

---

# Docker

## Learned

- Containerization concepts
- Docker images
- Docker containers
- Docker Compose
- Container networking


Important lesson:

Different environments have different networking rules.

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
DB_HOST=production-host
```

---

# Deployment

Deployed the application using Render.

Learned:

- Production settings
- Gunicorn
- Environment variables
- Database configuration
- Debugging deployment issues


---

# Deployment Problems Solved

## Database Connection Issue

Problem:

```
failed to resolve host 'db'
```

Solution:

Understanding the difference between:

- Local database hostname
- Docker database hostname
- Production database hostname


---

## Django 400 Bad Request

Problem:

```
400 Bad Request
```

Solution:

Configured:

- ALLOWED_HOSTS
- CSRF_TRUSTED_ORIGINS

for production.


---

# Frontend Improvements

Initially the project used plain HTML.

Later improved using Bootstrap.

Learned:

- Template inheritance
- Base templates
- Responsive layouts
- Reusable components

---

# Git Workflow

Learned:

- Creating commits
- Writing meaningful commit messages
- Pushing changes
- Managing feature-based commits


Example workflow:

```
git add .

git commit -m "Feature update"

git push
```

---

# Overall Learning Outcome

SmartPrep AI helped understand the complete software development lifecycle:

```
Planning

↓

Development

↓

Database Design

↓

AI Integration

↓

Containerization

↓

Deployment

↓

Production Debugging
```