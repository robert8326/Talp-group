#!/bin/sh

python manage.py migrate
python manage.py create_superuser admin admin
python manage.py runserver