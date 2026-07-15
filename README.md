# 📚 SmartPrep AI Platform

SmartPrep AI Platform is an AI-powered learning platform built with Django that helps students organize study material, generate AI-powered learning resources, and improve their revision process.

The project was developed from the ground up while learning Django architecture, PostgreSQL integration, Docker deployment, AI API integration, and production deployment.

---

# 🚀 Live Application

https://smartprep-ai-platform.onrender.com

---

# 🎯 Project Overview

The goal of SmartPrep AI is to create a personalized learning assistant where students can:

- Organize subjects
- Store notes
- Generate AI summaries
- Create AI-powered flashcards
- Generate quizzes from study material

---

# ✨ Features

## 🔐 Authentication System

Implemented using Django authentication.

Features:

- User registration
- Login/logout
- Password handling
- User-specific data access

---

## 📚 Subject Management

Users can:

- Create subjects
- View subjects
- Rename subjects
- Delete subjects

---

## 📝 Notes Management

Users can:

- Add notes
- Edit notes
- Delete notes
- Organize notes under subjects

---

# 🤖 AI Features

## 📄 AI Summary Generator

Converts large notes into concise summaries using Gemini AI.

Flow:

```
User Note

↓

Gemini AI

↓

Generated Summary

↓

Stored in Database
```

---

## 🃏 AI Flashcard Generator

Creates question-answer flashcards from notes.

---

## 📝 AI Quiz Generator

Creates multiple-choice quizzes from study material.

Features:

- AI-generated questions
- Multiple options
- Answer evaluation
- Score calculation

---

# 🛠 Technology Stack

## Backend

- Python
- Django
- Django ORM

## Database

- PostgreSQL

## AI

- Gemini AI API

## Frontend

- Django Templates
- Bootstrap 5

## Deployment

- Docker
- Docker Compose
- Gunicorn
- Render

---

# 🏗 Architecture

```
User

↓

Browser

↓

Django Application

↓

Views

↓

Models / PostgreSQL

↓

AI Service

↓

Gemini API
```

---

# 🐳 Docker Architecture

```
Docker Compose

        |

        |---- Django Container

        |

        |---- PostgreSQL Container
```

---

# 👨‍💻 Author

Shivansh Parmar