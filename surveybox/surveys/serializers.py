from django.conf import settings
from rest_framework import serializers
from .models import Survey, Answer


class SurveySerializer(serializers.ModelSerializer):
    questions = serializers.JSONField()
    answers_count = serializers.SerializerMethodField()
    url_to_survey = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = ('id', 'title', 'description', 'questions', 'answers_count', 'url_to_survey',)

    def get_answers_count(self, obj):
        return obj.answer_set.count()
    
    def get_url_to_survey(self, obj):
        return f'{settings.FE_URL}/survey/{obj.id}'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'survey', 'results',)
