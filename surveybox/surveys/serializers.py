from rest_framework import serializers
from .models import Survey, Answer


class SurveySerializer(serializers.ModelSerializer):
    questions = serializers.JSONField()

    class Meta:
        model = Survey
        fields = ('id', 'title', 'description', 'questions',)


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'survey', 'results',)
