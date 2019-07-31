from django.contrib import admin
from .models import Survey, Answer


admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
