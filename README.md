# surveybox-be

[![Build Status](https://dev.azure.com/KananRahimov/SurveyBox/_apis/build/status/KenanBek.surveybox-be?branchName=master)](https://dev.azure.com/KananRahimov/SurveyBox/_build/latest?definitionId=2&branchName=master)

Back-end for SurveyBox.

# Prerequisites

- Docker
- Azure CLI
- Kubectl
- Python

# Local Development

Start the dev server for local development:

```bash
docker-compose up
```

Run a command inside the docker container to create a `superuser`:

```bash
docker-compose exec web python manage.py createsuperuser
```

# Run Tests

```
# activate environment
virtualenv venv -p python3.7
source ./venv/bin/activate

# run postgres database locally
docker run --name postgres -p 5432:5432 postgres

# run tests
python manage.py test
```
