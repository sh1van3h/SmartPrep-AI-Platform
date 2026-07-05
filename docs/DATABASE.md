# SmartPrep AI Platform - Database Design

## Entities

### User

Stores application users.

Relationship

User
│
├── Subjects
├── Notes
└── Conversations

---

### Subject

Represents a study subject.

Examples

- Python
- DBMS
- Operating Systems

Relationship

One User

↓

Many Subjects

---

### Notes

Stores uploaded study material.

Supported formats

- PDF
- DOCX
- TXT

Relationship

One Subject

↓

Many Notes

---

### Summary

Stores AI-generated summaries.

Relationship

One Note

↓

One Summary

---

### Flashcards

Stores AI-generated flashcards.

Relationship

One Note

↓

Many Flashcards

---

### Quiz

Stores generated quizzes.

Relationship

One Note

↓

Many Quizzes

---

### Quiz Attempt

Stores quiz results.

Relationship

One Quiz

↓

Many Attempts

---

### Conversation

Stores AI Tutor chat history.

Relationship

One User

↓

Many Conversations