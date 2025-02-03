.PHONY: frontend

network:
	docker network create dealsmo_nw || true

build: network
	docker compose -f local.yml up --build -d --remove-orphans
build-no-cache: network
	DOCKER_BUILDKIT=1 docker compose -f local.yml build --no-cache
up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

down-v:
	docker compose -f local.yml down -v

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs backend

makemigrations:
	docker compose -f local.yml run --rm backend python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm backend python manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm backend python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm backend python manage.py createsuperuser

db-volume:
	docker volume inspect api_estate_prod_postgres_data

mailpit-volume:
	docker volume inspect api_estate_prod_mailpit_data

dealsmo-db:
	docker compose -f local.yml exec postgres psql --username=balda --dbname=dealsmodb

frontend: 
	docker compose -f local.yml stop frontend && docker compose -f local.yml rm -f frontend && rm -rf frontend/.next frontend/node_modules && docker compose -f local.yml build --no-cache frontend && docker compose -f local.yml up -d frontend

test:
	docker compose -f local.yml run --rm backend python manage.py test

test-v:
	docker compose -f local.yml run --rm backend python manage.py test -v 2

flake8:
	docker compose -f local.yml run --rm backend sh -c "flake8"