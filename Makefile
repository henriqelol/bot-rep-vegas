PORT ?= 8000
WORKER_PROCESSES ?= 1
SIMPLE_SETTINGS ?= settings.base

run:
	@SIMPLE_SETTINGS=${SIMPLE_SETTINGS} ${NEW_RELIC_RUN} uvicorn rep_vegas:app --host 0.0.0.0 --port ${PORT} --workers ${WORKER_PROCESSES} --no-access-log

setup:
	pip install pre-commit
	@poetry install && pre-commit install --hook-type commit-msg

install:
	@poetry install

lint:
	@poetry run flake8 rep_vegas
	@poetry run isort --check rep_vegas
	@poetry run black --diff --check rep_vegas
	@poetry run mypy rep_vegas

lint-fix:
	@poetry run autoflake8 --remove-unused-variables -i -r rep_vegas alembic
	@poetry run black rep_vegas alembic
	@poetry run isort rep_vegas alembic

docker-dev-up:
	@docker-compose up -d

docker-dev-down: 
	@docker-compose down

migratedb-local:
	@SIMPLE_SETTINGS=${SIMPLE_SETTINGS} poetry run alembic upgrade head

migratedb-downgrade-local:
	@SIMPLE_SETTINGS=${SIMPLE_SETTINGS} poetry run alembic downgrade -1

alembic-status-local:
	@SIMPLE_SETTINGS=${SIMPLE_SETTINGS} poetry run alembic current

revision-local: ## make revision-local M="revision description here"
	@SIMPLE_SETTINGS=${SIMPLE_SETTINGS} poetry run alembic revision --autogenerate --rev-id "`poetry run python alembic/rev_gen.py`" -m "${M}"
