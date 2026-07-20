.PHONY: format check test create_superuser

format:
	ruff format .
	ruff check . --fix

check:
	ruff check .
	ruff format --check .
	typos .

test:
	coverage run manage.py test --shuffle
	coverage report -m

create_superuser:
	docker compose exec backend python manage.py createsuperuser