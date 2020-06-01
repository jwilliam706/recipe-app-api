# Recipe App API

API with Django rest framework

## Project Setup

docker build .

docker-compose build

### Commands

**create django project:** docker-compose run app sh -c "django-admin.py startproject <project_name> ."

**create django app:** docker-compose run app sh -c "django-admin.py startapp <app_name>"

**run tests:** docker-compose run app sh -c "python manage.py test"

**run app locally:** docker-compose up
