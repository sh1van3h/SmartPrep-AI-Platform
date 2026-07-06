from django.shortcuts import render , get_object_or_404
from .models import Subject , Note
from django.shortcuts import redirect
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

def add_note(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Note.objects.create(title=title,content=content,
                            subject=subject)
        return redirect("subject_detail" , id=subject.id)
    
    return render(
        request,
        "accounts/add-note.html",
        {
            "subject" : subject
        }
    )

def note_detail(request, id):

    note = get_object_or_404(
        Note,
        id=id
    )

    return render(
        request,
        "accounts/note_detail.html",
        {
            "note": note
        }
    )

def edit_note(request, id):

    note = get_object_or_404(
        Note,
        id=id
    )

    if request.method == "POST":

        note.title = request.POST["title"]

        note.content = request.POST["content"]

        note.save()

        return redirect(
            "note_detail",
            id=note.id
        )

    return render(
        request,
        "accounts/edit_note.html",
        {
            "note": note
        }
    )