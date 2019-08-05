from django.contrib import admin
from .models import Survey, Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey']
