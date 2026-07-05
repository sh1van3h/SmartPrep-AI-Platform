SmartPrep AI Platform - Engineering Decisions

Decision #1 – Backend Framework
Decision

Use Django with Django REST Framework (DRF) instead of FastAPI.

Reason
Built-in authentication
Built-in admin panel
Excellent ORM
Mature ecosystem
Faster development for a complete web application
Why not FastAPI?

FastAPI is excellent for API-first applications and microservices, but SmartPrep AI requires authentication, admin features, file uploads, and a complete backend framework. FastAPI will be used in TradeWise AI, where it fits naturally.

Decision #2 – Database
Decision

Use PostgreSQL instead of SQLite.

Reason
Production-ready relational database
Better performance
Supports concurrent users
Widely used in industry
Excellent integration with Django
Why not SQLite?

SQLite is perfect for small projects and learning, but it stores everything in a single file and isn't ideal for applications expected to grow.

Decision #3 – AI Content Generation
Decision

AI-generated content will be generated only when the user requests it.

Examples:

Generate Summary
Generate Flashcards
Generate Quiz
Generate Interview Questions
Generate Cheat Sheet
Reason
Reduces AI API usage
Faster note uploads
Gives users full control
Lower operational cost
Why not generate everything automatically?

Most users may only need one feature. Automatically generating all AI outputs wastes API calls, time, and money.

Decision #4 – AI Content Storage
Decision

Store all AI-generated content in the database.

Examples:

Summary
Flashcards
Quiz
Interview Questions
Cheat Sheets
Reason
Instant retrieval
No repeated AI requests
Lower API cost
Better user experience
Handling Note Updates
Decision

When a note is updated:

Existing AI content is not deleted.
It is marked as Outdated.
The user chooses when to regenerate the AI content.
Reason
Avoid unnecessary AI calls
User stays in control
Better performance
Easier to maintain

Future Improvements (Not Version 1)

These ideas are intentionally postponed to avoid over-engineering.

AI content versioning
Automatic change detection
Partial AI regeneration
Background AI processing
ML-based study recommendations
Semantic search using embeddings
Real-time notifications