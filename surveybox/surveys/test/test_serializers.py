from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import SurveyFactory
from ..serializers import SurveySerializer


class TestSurveySerializer(TestCase):

    def setUp(self):
        self.user_data = model_to_dict(SurveyFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = SurveySerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = SurveySerializer(data=self.user_data)
        ok_(serializer.is_valid())
