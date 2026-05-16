COMPOSE_BASE = docker compose -f docker-compose.yml
COMPOSE_PROD = $(COMPOSE_BASE) -f docker-compose.prod.yml

.PHONY: dev dev-down dev-refresh dev-recreate dev-reset-db prod prod-down logs ps clean

dev:
	docker compose up --build

dev-down:
	docker compose down

dev-refresh:
	docker compose down --remove-orphans
	docker compose up -d --build --force-recreate --remove-orphans

dev-recreate:
	docker compose up -d --build --force-recreate --remove-orphans

prod:
	$(COMPOSE_PROD) up -d --build

prod-down:
	$(COMPOSE_PROD) down

logs:
	docker compose logs -f

ps:
	docker compose ps

clean:
	docker compose down --volumes --remove-orphans