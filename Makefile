.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv install --dev

check:
	isort --recursive --check-only meier wsgi.py
	black -l 79 --check meier wsgi.py
	pylint meier wsgi.py

coverage:
	python -m pytest --cov meier --cov-report term --cov-report=xml

format:
	isort -rc -y meier wsgi.py
	black -l 79 meier wsgi.py

test: format
	python -m pytest

dev-build:
	docker build --tag meier:dev .

dev-run:
	docker run -p 2368:2368 -v ~/workspace/themes:/app/meier/templates/themes --env-file .env meier:dev

build:
	@read -p "Enter Docker User:" DOCKER_USER; \
	read -p "Enter Docker Tag:" DOCKER_TAG; \
	docker build --tag $$DOCKER_USER/meier:$$DOCKER_TAG .

push:
	@read -p "Enter Docker User:" DOCKER_USER; \
	read -p "Enter Docker Tag:" DOCKER_TAG; \
	docker push $$DOCKER_USER/meier:$$DOCKER_TAG

requirements:
	pipenv lock -r > requirements.txt
	pipenv lock --dev -r > requirements-dev.txt
