.PHONY: help build up down logs clean logs-follow test lint

help:
	@echo "Smart Email Assistant - Available Commands"
	@echo ""
	@echo "  make build          Build Docker image"
	@echo "  make up             Start the application"
	@echo "  make down           Stop the application"
	@echo "  make logs           View application logs (one-time)"
	@echo "  make logs-follow    Follow application logs"
	@echo "  make ps             List running containers"
	@echo "  make clean          Remove containers and images"
	@echo "  make restart        Restart the application"
	@echo "  make shell          Open shell in running container"
	@echo "  make health         Check application health"
	@echo ""

build:
	@echo "Building Docker image..."
	docker compose build

up:
	@echo "Starting application..."
	docker compose up -d
	@echo "✅ Application started at http://localhost:5000"

down:
	@echo "Stopping application..."
	docker compose down

logs:
	docker compose logs

logs-follow:
	docker compose logs -f

ps:
	docker ps -a

clean:
	@echo "Cleaning up containers and images..."
	docker compose down -v
	docker system prune -f

restart:
	@echo "Restarting application..."
	docker compose restart
	@echo "✅ Application restarted"

shell:
	docker compose exec email-assistant /bin/bash

health:
	@echo "Checking application health..."
	curl -s http://localhost:5000/health | python -m json.tool || echo "Application not running"

env-setup:
	@echo "Creating .env file..."
	cp .env.example .env
	@echo "✅ .env file created. Please edit it with your API keys."

install-docker:
	@echo "Opening Docker Desktop download page..."
	open "https://www.docker.com/products/docker-desktop"

get-keys:
	@echo "Opening OpenAI API keys page..."
	open "https://platform.openai.com/api-keys"

gmail-setup:
	@echo "Opening Google Cloud Console..."
	open "https://console.cloud.google.com/"

all: build up
	@echo "✅ Setup complete!"
