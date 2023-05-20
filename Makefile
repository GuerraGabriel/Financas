.PHONY: help
.DEFAULT_GOAL := help
SHELL=/bin/bash

help: ## Mostra lista de comandos
	@echo -e "\033[35mListando todos comandos encontrandos em Makefile.\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'

init: ## Inicializa os serviços
	-@docker network create financas > /dev/null
	@docker-compose up -d
	@output=$$(docker exec db pg_isready); \
	while [[ "$$output" != *"accepting connections"* ]]; do \
		echo "Aguardando pg_isready"; \
		output=$$(docker exec db pg_isready); \
		sleep 0.5; \
	done
	@docker exec -i -u postgres db psql -c "CREATE DATABASE financas;"> /dev/null; echo "Banco de dados criado"
	@ls $(CURDIR)/apps/db/boot/*.sql  | sort | xargs cat | docker exec -i db psql -U postgres -d financas > /dev/null; echo "Schemas e usuários criados"


migrate: ## Usa Flyway para realizar migrations no banco de dados
	@docker run --pull always --rm -v $(CURDIR)/apps/db/migrations:/flyway/sql \
		-e FLYWAY_EDITION=community \
		--network financas \
			flyway/flyway:9.17-alpine \
			-url=jdbc:postgresql://db:5432/financas \
			-schemas=flyway \
			-user=postgres \
			-password=admin \
			-connectRetries=3 \
			migrate

clear-compose: ## Desliga todos os serviços, apaga todos volumes, redes e containers orfãos relacionados ao serviço
	@docker-compose down -v --remove-orphans
	@docker volume rm -f finanas_contas_db
	@docker network rm financas

api: ##Inicia o container da API para debug e desenvolvimento
	@docker-compose up -d api
	@docker exec -it api

python-dev:
	python3.11 -m venv apps/api/venv
	. 	/apps/api/venv/bin/activate
	pip install -r requirements.txt
