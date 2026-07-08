from django.urls import path
from . import views

urlpatterns = [
    path("subjects/",
          views.subject_list,
            name="subject_list"),
    path("subjects/<int:id>/",
          views.subject_detail,
            name="subject_detail"),
    path("subjects/<int:id>/add-note",
          views.add_note,
            name="add_note"),
    path(
        "notes/<int:id>/",
        views.note_detail,
        name="note_detail"),
    path(
        "notes/<int:id>/edit/",
        views.edit_note,
        name="edit_note"),
    path(
        "notes/<int:id>/delete/",
        views.delete_note,
        name="delete_note"),
    path(
        "signup/",
        views.signup,
        name="signup"),

    path(
        "login/",
        views.user_login,
        name="login"),

    path(
        "logout/",
        views.user_logout,
        name="logout"),

    path(
        "notes/<int:id>/generate-summary/",
        views.generate_summary,
        name="generate_summary"),

    path(
        "notes/<int:id>/generate-flashcards/",
        views.generate_flashcards,
        name="generate_flashcards"),
    path(
        "notes/<int:id>/flashcards/",
        views.flashcards,
        name="flashcards",),
    path(
        "notes/<int:id>/summary/",
        views.summary,
        name="summary",),
    path(
        "notes/<int:id>/generate-quiz/",
        views.generate_quiz,
        name="generate-quiz",),
    path(
        "notes/<int:id>/quiz/",
        views.quiz,
        name="quiz",),
    path(
        "notes/<int:id>/quiz-result",
        views.quiz_result,
        name = "quiz_result",
    ),
    path(
    "subjects/add/",
    views.add_subject,
    name="add_subject",
),
    path(
        "subjects/<int:id>/delete",
        views.delete_subject,
        name = "delete_subject",
    ),
    
]
