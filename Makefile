up_container:
	docker-compose build
	docker-compose up -d

build_front:
	docker-compose exec vue npm install --prefix ./frontend
	docker-compose exec vue npm run build --prefix ./frontend

up_server:
	docker-compose exec flask python backend/main.py

down_container:
	docker-compose down