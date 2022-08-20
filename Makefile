.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv install --dev

check:
	black -l 79 --check meier wsgi.py tests

coverage:
	python -m pytest --cov meier --cov-report term-missing --cov-report=xml

format:
	black -l 79 meier wsgi.py tests

test: format
	pytest

dev:
	docker build --tag meier:dev . && docker run -p 2368:2368 --env-file .env meier:dev

build:
	@read -p "Enter Docker User: " DOCKER_USER; \
	read -p "Enter Docker Tag: " DOCKER_TAG; \
	docker build -t $$DOCKER_USER/meier:$$DOCKER_TAG . && docker build -t $$DOCKER_USER/meier:latest .

push:
	@read -p "Enter Docker User: " DOCKER_USER; \
	read -p "Enter Docker Tag: " DOCKER_TAG; \
	docker push $$DOCKER_USER/meier:$$DOCKER_TAG && docker push $$DOCKER_USER/meier:latest

requirements:
	pipenv requirements > requirements.txt
	pipenv requirements --dev > requirements-dev.txt
