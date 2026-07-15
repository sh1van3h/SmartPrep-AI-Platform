# Architecture

## Overview

SmartPrep AI Platform follows Django's Model-View-Template (MVT) architecture.

The application separates:

- User interface
- Business logic
- Database operations
- AI processing

This separation keeps the project maintainable and easier to extend.

---

# Project Evolution

The project was developed in multiple stages.

## Phase 1: Django Setup

The project started with a basic Django application structure.

Initial goals:

- Understand Django project structure
- Create applications
- Configure URLs and templates
- Build the foundation for future features

---

## Phase 2: Database Architecture

Initially Django's default SQLite database was used during development.

Later, the project migrated to PostgreSQL because:

- PostgreSQL is production ready
- Better support for relational data
- More suitable for deployment environments

---

## Phase 3: Application Architecture

The final application structure:

```
SmartPrep AI Platform

User

 |

Subjects

 |

Notes

 |

AI Features
```

---

# Request Flow

A typical request follows this flow:

```
User

↓

Browser

↓

Django URL Router

↓

View

↓

Model / AI Service

↓

Database

↓

Template Response
```

---

# Backend Components

## Views

Views handle:

- User requests
- Business logic
- Authentication checks
- Database interaction
- Response rendering


---

## Models

Models define the database structure.

Main models:

- User
- Subject
- Note
- Flashcard
- QuizQuestion

Django ORM is used to communicate with PostgreSQL.

---

## Templates

The frontend uses Django templates.

Responsibilities:

- Display data
- Handle forms
- Show AI results
- Provide user interface

Bootstrap is used for styling.

---

# AI Architecture

AI functionality was separated into its own service layer.

Structure:

```
Django View

↓

AI Service

↓

Gemini API

↓

Response Processing

↓

Database Storage
```

---

## AI Service Responsibilities

The AI service handles:

- Summary generation
- Flashcard generation
- Quiz generation

Keeping AI logic separate prevents large and complex views.

---

# Database Architecture

Database:

```
PostgreSQL
```

Relationships:

```
User

 |

Many Subjects

 |

Many Notes

 |

Flashcards / Quiz Questions
```

---

# Docker Architecture

The application uses Docker for environment consistency.

Architecture:

```
Docker Compose

        |

        |---- Django Web Container

        |

        |---- PostgreSQL Database Container
```

---

## Docker Networking

During development, different environments required different database hosts.

Local development:

```
DB_HOST=localhost
```

Docker environment:

```
DB_HOST=db
```

Reason:

Docker containers communicate using service names.

---

# Production Architecture

Deployment stack:

```
User

↓

Render

↓

Gunicorn

↓

Django Application

↓

PostgreSQL Database
```

---

# Deployment Flow

```
GitHub Repository

↓

Render Deployment

↓

Docker Build

↓

Gunicorn Server

↓

Live Application
```

---

# Future Architecture Improvements

Possible improvements:

- REST API layer
- Separate frontend application
- Background AI processing
- Task queue using Celery
- Caching system
- Analytics service