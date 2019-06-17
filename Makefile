.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv install --dev

check:
	isort --recursive --check-only meier tests meier.py
	black -l 79 --check meier tests meier.py
	pylint meier meier.py

format:
	isort -rc -y meier tests meier.py
	black -l 79 meier tests meier.py

test: format
	python -m meier -vv

coverage:
	python -m meier --cov meier --cov-report term --cov-report xml

htmlcov:
	python -m meier --cov meier --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

requirements:
	pipenv lock -r > requirements.txt
	pipenv lock -dr > requirements-dev.tx