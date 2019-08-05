import factory


class SurveyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'surveys.Survey'

    id = factory.Faker('uuid4')
    title = factory.Sequence(lambda n: f'test survey {n}')
    description = factory.Sequence(lambda n: f'test survey description {n}')
    questions = {
		'title': 'A single-field form',
		'type': 'string'
	}
