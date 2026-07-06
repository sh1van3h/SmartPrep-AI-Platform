from django.shortcuts import render , get_object_or_404
from .models import Subject , Note
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

@login_required
def subject_list(request):
    subjects = Subject.objects.filter(
    user=request.user)

    return render(
        request,
        "accounts/subject_list.html",
        {"subjects": subjects}
    )

@login_required
def subject_detail(request, id):
    subject = get_object_or_404(Subject, id=id, user=request.user)
    notes = Note.objects.filter(subject=subject)
    return render(
        request,
        "accounts/subject_detail.html",
        {
            "subject" : subject,
            "notes" : notes,
        }
    )

@login_required
def add_note(request, id):
    subject = get_object_or_404(Subject,
                                id=id,
                                subject__user=request.user)
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

@login_required
def note_detail(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    return render(
        request,
        "accounts/note_detail.html",
        {
            "note": note
        }
    )

@login_required
def edit_note(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
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

@login_required
def delete_note(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    if request.method == "POST":

        subject_id = note.subject.id

        note.delete()

        return redirect(
            "subject_detail",
            id=subject_id
        )

    return render(
        request,
        "accounts/delete_note.html",
        {
            "note": note
        }
    )

def signup(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = UserCreationForm()

    return render(
        request,
        "accounts/signup.html",
        {
            "form": form
        }
    )


def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("subject_list")

    return render(
        request,
        "accounts/login.html"
    )


def user_logout(request):

    logout(request)

    return redirect("login")