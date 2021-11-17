container_up:
	docker-compose build
	docker-compose up -d

# 初回起動時
front_build_first:
	docker-compose exec vue npm install --prefix ./frontend
	docker-compose exec vue npm run build --prefix ./frontend

front_build:
	docker-compose exec vue npm run build --prefix ./frontend

up:
	docker-compose exec flask python backend/main.py
