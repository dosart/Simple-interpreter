install: ## Install dependencies
	@poetry install

format: ## Install dependencies
	poetry run black .

test:  ## Run tests
	@poetry run pytest

lint: ## Run linter
	@poetry run flake8 interpreter
	@poetry run flake8 tests

selfcheck: ## Checks the validity of the pyproject.toml file
	@poetry check

check: ## selfcheck + test + lint
	@make selfcheck
	@make test
	@make lint
	poetry run black --check

build: ## Check and builds a package
	@make check
	@poetry build

.PHONY: install format test lint selfcheck check build cc-coverage help
