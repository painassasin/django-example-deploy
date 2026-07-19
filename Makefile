.PHONY: format check test

format:
	ruff format .
	ruff check . --fix

check:
	ruff check .
	ruff format --check .

test:
	coverage run manage.py test --shuffle
	coverage report -m
