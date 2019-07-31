from django.db import models
from django.contrib.postgres.fields import JSONField


class Survey(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    questions = JSONField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    results = JSONField()

    def __str__(self):
        return f'Answer for {self.survey}'
