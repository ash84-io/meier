.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv install --dev

check:
	isort --recursive --check-only meier wsgi.py tests
	black -l 79 --check meier wsgi.py tests

coverage:
	python -m pytest --cov meier --cov-report term-missing --cov-report=xml

format:
	isort -rc -y meier wsgi.py tests
	black -l 79 meier wsgi.py tests

test: format
	python -m pytest

dev-build:
	docker-compose -f docker-compose-dev.yml build

dev-run:
	docker-compose -f docker-compose-dev.yml up

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
