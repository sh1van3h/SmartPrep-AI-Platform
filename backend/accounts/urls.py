from django.urls import path
from . import views

urlpatterns = [
    path("subjects/", views.subject_list),
]