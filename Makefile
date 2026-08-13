.PHONY: install dev test lint build serve api

install:
	pip install -e .

dev:
	pip install -e ".[api]"

lint:
	ruff check quantserve

build-web:
	cd web && npm install && npm run build

api:
	uvicorn quantserve.api.app:get_app --factory --reload

cli:
	quantserve doctor
