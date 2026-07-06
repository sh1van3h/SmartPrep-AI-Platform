from django.urls import path
from . import views

urlpatterns = [
    path("subjects/", views.subject_list, name="subject_list"),
    path("subjects/<int:id>/", views.subject_detail, name="subject_detail"),
    path("subjects/<int:id>/add-note", views.add_note, name="add_note"),
]