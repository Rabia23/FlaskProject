up: ## run all services
	docker-compose up

stop: ## stop all services
	docker-compose stop

app-shell: ## run a shell on the flask_app container
	docker exec -it flask_app /bin/bash

db-shell: ## run a shell on the flask_app_db container
	docker exec -it flask_app_db /bin/bash