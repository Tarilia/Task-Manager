dev:
	poetry run python3 manage.py runserver

PORT ?= 10000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

lint:
	poetry run flake8

install:
	poetry install

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

shell:
	python3 manage.py shell

messages:
	django-admin makemessages -l ru

compile:
	django-admin compilemessages

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run --source="task_manager" manage.py test task_manager
	poetry run coverage xml

test-report:
	poetry run coverage report
