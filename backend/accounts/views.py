from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject
# Create your views here.

def subject_list(request):
    subjects = Subject.objects.all()
    output = ""
    for subject in subjects:
        output += subject.name + "<br>"
    return HttpResponse(output)
