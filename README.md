# recipe-app-api
API with Django rest framework

# Project Setup

docker build .
docker-compose build

create django project:
docker-compose run app sh -c "django-admin.py startproject app ."

run tests: docker-compose run app sh -c "python manage.py test"