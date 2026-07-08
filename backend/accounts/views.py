from django.shortcuts import render , get_object_or_404
from .models import Subject , Note , Flashcard , QuizQuestion
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from . import ai_service
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

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            subject.name = name
            subject.save()
        return redirect(
            "subject_detail",
            id=subject.id
        )

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
                                user=request.user)
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

    old_content = note.content

    if request.method == "POST":

        note.title = request.POST["title"]

        new_content = request.POST["content"]

        note.content = new_content

        if old_content != new_content:
            note.summary_is_outdated = True

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

@login_required
def generate_summary(request, id):
    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    if note.ai_summary and not note.summary_is_outdated:
        return redirect("note_detail", id=note.id)

    try:
        summary = ai_service.generate_summary(note.content)

        note.ai_summary = summary
        note.summary_is_outdated = False
        note.save()

    except Exception as e:
        print(e)  # We'll replace this with proper logging later.

    return redirect("note_detail", id=note.id)

@login_required
def generate_flashcards(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    note.flashcards.all().delete()

    flashcards = ai_service.generate_flashcards(
        note.content
    )

    for flashcard in flashcards:

        Flashcard.objects.create(
            note=note,
            question=flashcard["question"],
            answer=flashcard["answer"]
        )

    return redirect(
        "flashcards",
        id=note.id,
    )

@login_required
def flashcards(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    return render(
        request,
        "accounts/flashcards.html",
        {
            "note": note
        }
    )

@login_required
def summary(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    return render(
        request,
        "accounts/summary.html",
        {
            "note": note
        }
    )

@login_required
def quiz(request, id):
    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    if "current_question" not in request.session:
        request.session["score"] = 0
        request.session["current_question"] = 0

    questions = note.quiz_question.all()
    current_question = request.session["current_question"]
    if current_question >= len(questions):


        request.session["final_score"] = request.session["score"]
        request.session["total_questions"] = len(questions)
        request.session.pop("score",None)
        request.session.pop("current_question",None)
        return redirect(
            "quiz_result",
            id=note.id
        )
    question = questions[current_question]

    if request.method == "POST":
        answer = request.POST.get("answer")
        if answer == question.correct_option:
            request.session["score"] += 1
        request.session["current_question"] += 1
        return redirect(
            "quiz",
            id=note.id
        )

    return render(
        request,
        "accounts/quiz.html",
        {
            "note": note,
            "question":question
        }
    )

@login_required
def generate_quiz(request, id):
    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    note.quiz_question.all().delete()

    quizquestions = [
        {
            "question": "What is Python?",
            "option_a": "Programming Language",
            "option_b": "Database",
            "option_c": "Browser",
            "option_d": "Operating System",
            "correct_option": "A"
        },
        {
            "question": "What is Django?",
            "option_a": "Framework",
            "option_b": "Database",
            "option_c": "Operating System",
            "option_d": "Programming Language",
            "correct_option": "A"
        }
    ]

    for quizquestion in quizquestions:

        QuizQuestion.objects.create(
            note=note,
            question=quizquestion["question"],
            option_a=quizquestion["option_a"],
            option_b=quizquestion["option_b"],
            option_c=quizquestion["option_c"],
            option_d=quizquestion["option_d"],
            correct_option=quizquestion["correct_option"]
        )

    return redirect(
        "quiz",
        id=note.id,
    )

@login_required
def quiz_result(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        subject__user=request.user
    )

    score = request.session.get("final_score", 0)
    total = request.session.get("total_questions", 0)
    request.session.pop("final_score", None)
    request.session.pop("total_questions", None)

    return render(
        request,
        "accounts/quiz_result.html",
        {
            "note": note,
            "score": score,
            "total": total
        }
        
    )

@login_required
def add_subject(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()

    if name :
        Subject.objects.create(
            name=name,
            user=request.user
        )

    return redirect("subject_list")

@login_required
def delete_subject(request,id):
    subject = get_object_or_404(
        Subject,
        id=id,
        user=request.user
    )
    subject.delete()
    return redirect("subject_list")