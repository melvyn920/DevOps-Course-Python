.PHONY: help init install build run test test-api

help:
	@echo "Makefile commands:"
	@echo "  init       Install project dependencies"
	@echo "  install    Install project dependencies (same as init)"
	@echo "  build      Build the Docker image"
	@echo "  run        Run the Flask application"
	@echo "  test       Run the unit tests"
	@echo "  test-api   Test the API endpoints"

init:
	@echo "Setting up the virtual environment..."
	python3 -m venv .venv
	@echo "Activating the virtual environment..."
	. .venv/bin/activate

install: init
	@echo "Installing dependencies..."
	. .venv/bin/activate && pip install -r requirements.txt

build:
	@echo "Building the Docker image..."
	docker build -t health-calculator-service .

run:
	@echo "Running the Flask app..."
	python app.py

test:
	@echo "Running unit tests..."
	python -m unittest test.py

test-api:
	@echo "Testing API endpoints..."
	curl -X GET http://localhost:5000/health
