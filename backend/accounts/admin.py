from django.contrib import admin
from .models import Subject,Note,QuizQuestion
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title","subject","updated_at")

admin.site.register(Subject)
admin.site.register(QuizQuestion)
