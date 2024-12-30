# Makefile

# Define the docker-compose command and options
DCOMPOSE = docker compose -f docker-compose.yaml

start:
	@$(DCOMPOSE) up -d $(SERVICE)

stop:
	@$(DCOMPOSE) down $(SERVICE)

# Restart PostgreSQL container
restart:
	@$(DCOMPOSE) down postgres
	@$(DCOMPOSE) up -d postgres
	@echo "PostgreSQL container restarted."

# Check status of PostgreSQL container
status:
	@$(DCOMPOSE) ps

# Remove containers and associated volumes
clean:
	@$(DCOMPOSE) down -v
	@echo "PostgreSQL container and volumes removed."

# Follow logs of PostgreSQL container
logs:
	@$(DCOMPOSE) logs -f

psql:
	docker exec -it postgres_db psql -U postgres -d postgres

bash:
	docker exec -it postgres_db bash

.PHONY: start stop restart status clean logs psql bash
