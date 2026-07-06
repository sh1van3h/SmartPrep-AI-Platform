from django.shortcuts import render 
from .models import Subject , Note
from django.shortcuts import get_object_or_404
# Create your views here.

def subject_list(request):
    subjects = Subject.objects.all()

    return render(
        request,
        "accounts/subject_list.html",
        {"subjects": subjects}
    )

def subject_detail(request, id):
    subject = get_object_or_404(Subject, id=id)
    notes = Note.objects.filter(subject=subject)
    return render(
        request,
        "accounts/subject_detail.html",
        {
            "subject" : subject,
            "notes" : notes,
        }
    )