# Database Design

## Overview

SmartPrep AI Platform uses PostgreSQL as the production database.

The database follows a relational structure because the application contains clear relationships between users, subjects, notes, and AI-generated content.

---

# Database Technology

## PostgreSQL

PostgreSQL was selected because:

- Production ready
- Reliable relational database
- Strong support for relationships
- Better scalability compared to SQLite

---

# Entity Relationship Structure

```
User

 |

Many Subjects

 |

Many Notes

 |

Flashcards

 |

Quiz Questions
```

---

# User Model

SmartPrep uses Django's built-in authentication system.

Stores:

- Username
- Password
- Email
- Authentication information


Relationship:

```
User

 |

Many Subjects
```

---

# Subject Model

The Subject model stores learning categories.

Example:

```
Python

Machine Learning

Database
```

Fields:

```
id
name
user
```

Relationship:

```
User

 |

Subjects
```

---

# Note Model

The Note model stores study material.

Example:

```
Title:
Python Variables

Content:
Variables store values in memory.
```

Fields:

```
id
title
content
subject
ai_summary
summary_is_outdated
```

Relationship:

```
Subject

 |

Many Notes
```

---

# Flashcard Model

Stores AI-generated flashcards.

Example:

```
Question:
What is Django?

Answer:
A Python web framework.
```

Fields:

```
id
question
answer
note
```

Relationship:

```
Note

 |

Many Flashcards
```

---

# QuizQuestion Model

Stores AI-generated quiz questions.

Fields:

```
id
question
option_a
option_b
option_c
option_d
correct_option
note
```

Relationship:

```
Note

 |

Many Quiz Questions
```

---

# Database Design Decisions

## User Data Isolation

Each user can only access their own:

- Subjects
- Notes
- AI-generated content

This is enforced using Django query filtering.

---

## Foreign Key Relationships

Foreign keys are used to maintain:

- Data consistency
- Proper relationships
- Easy querying

---

# Migration Process

Database changes were managed using Django migrations.

Commands used:

```
python manage.py makemigrations

python manage.py migrate
```

---

# Future Database Improvements

Possible improvements:

- User profile table
- Learning progress table
- Activity tracking
- Notes search indexing
- Analytics tables