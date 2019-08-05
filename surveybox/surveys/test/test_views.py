import json
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from ..models import Survey
from .factories import SurveyFactory

fake = Faker()


class TestSurveyViews(APITestCase):
    """
    Tests surveys related endpoint.
    """

    def setUp(self):
        self.url = reverse('survey-list')
        self.survey_data = model_to_dict(SurveyFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):

        payload = json.dumps(self.survey_data)

        response = self.client.post(
            self.url,
            data=payload,
            content_type='application/json',
        )

        eq_(response.status_code, status.HTTP_201_CREATED)

        survey = Survey.objects.get(pk=response.data.get('id'))
        eq_(survey.title, self.survey_data.get('title'))
        eq_(survey.description, self.survey_data.get('description'))
