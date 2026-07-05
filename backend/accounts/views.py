from django.shortcuts import render 
from .models import Subject
# Create your views here.

def subject_list(request):
    subjects = Subject.objects.all()

    return render(
        request,
        "accounts/subject_list.html",
        {"subjects": subjects}
    )
