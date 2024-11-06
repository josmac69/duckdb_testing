# Makefile

# Define the docker-compose command and options
DCOMPOSE = docker compose -f docker-compose.yaml

# Start PostgreSQL container
start:
	@$(DCOMPOSE) up -d
	@echo "PostgreSQL container started."

# Stop PostgreSQL container
stop:
	@$(DCOMPOSE) down
	@echo "PostgreSQL container stopped."

# Restart PostgreSQL container
restart:
	@$(DCOMPOSE) down
	@$(DCOMPOSE) up -d
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

.PHONY: start stop restart status clean logs
