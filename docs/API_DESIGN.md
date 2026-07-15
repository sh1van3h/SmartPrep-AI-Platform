# API Design

## Overview

SmartPrep AI currently uses Django views and templates instead of a separate REST API.

The application follows Django's URL routing system.

---

# Authentication Routes

## Signup

```
/signup/
```

Purpose:

Creates a new user account.


---

## Login

```
/login/
```

Purpose:

Authenticates users and creates sessions.


---

## Logout

```
/logout/
```

Purpose:

Ends user sessions.

---

# Subject Routes

## Subject List

```
/subjects/
```

Purpose:

Displays user's subjects.


---

## Add Subject

```
/subjects/add/
```

Purpose:

Creates a new subject.


---

## Subject Detail

```
/subjects/<id>/
```

Purpose:

Displays subject information and related notes.


---

## Delete Subject

```
/subjects/<id>/delete/
```

Purpose:

Removes a subject.

---

# Note Routes

## Add Note

```
/subjects/<id>/add-note/
```

Purpose:

Creates a note under a subject.


---

## Note Detail

```
/notes/<id>/
```

Purpose:

Displays note content and AI features.


---

## Edit Note

```
/notes/<id>/edit/
```

Purpose:

Updates note information.


---

## Delete Note

```
/notes/<id>/delete/
```

Purpose:

Deletes a note.


---

# AI Routes

## Generate Summary

```
/notes/<id>/generate-summary/
```

Process:

```
Note Content

↓

AI Service

↓

Gemini API

↓

Save Summary
```

---

## Generate Flashcards

```
/notes/<id>/generate-flashcards/
```

Process:

```
Note Content

↓

Gemini API

↓

Flashcard Objects

↓

Database
```

---

## Generate Quiz

```
/notes/<id>/generate-quiz/
```

Process:

```
Note Content

↓

Gemini API

↓

Quiz Questions

↓

Database
```

---

# Quiz Routes

## Start Quiz

```
/notes/<id>/quiz/
```

Purpose:

Allows users to answer generated questions.


---

## Quiz Result

```
/notes/<id>/quiz-result/
```

Purpose:

Displays final score.

---

# Future API Improvements

Possible future development:

- Django REST Framework API
- JWT authentication
- Mobile application support
- External client access