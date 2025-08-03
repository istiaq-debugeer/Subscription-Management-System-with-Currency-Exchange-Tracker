

# Subscription-Management-System-with-Currency-Exchange-Tracker

A Django-based system for managing user subscriptions and tracking currency exchange rates, with REST API, Celery background tasks, and Docker support.

## Features
- User subscription management (plans, status, cancellation)
- Currency exchange rate tracking and storage
- RESTful API (Django REST Framework)
- Periodic background fetching of exchange rates (Celery + Redis)
- PostgreSQL database
- Dockerized for easy deployment

## Requirements
- Docker & Docker Compose

## Quick Start

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd Subscription-Management-System-with-Currency-Exchange-Tracker
   ```

2. **Set environment variables (optional):**
   Create a .env file or export variables for database credentials if you want to override defaults.

3. **Build and start all services:**
   ```sh
   docker compose up --build
   ```

4. **Apply migrations and create superuser:**
   In a new terminal:
   ```sh
   docker-compose exec web python src/manage.py migrate
   docker-compose exec web python src/manage.py createsuperuser
   ```


5. **Access the app:**
   - Django app: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

6. **Get your access token:**
   - After creating a superuser, you can obtain a JWT access token by making a POST request to `/api/token/` with your username and password:
     
   - The response will include an `access` token. Use this token in your API requests as a Bearer token:
     ```http
     Authorization: Bearer <access_token>
     ```

## API Endpoints

- `/api/subscriptions/` - Manage subscriptions
- `/api/plan/` - Manage plans
- `/api/exchange-rates/` - List exchange rates
- `/api/get-exchange-rates/` - Fetch latest rates from external API

## Celery Tasks
- Periodically fetches and stores exchange rates every hour
- Uses Redis as broker and backend

## Project Structure
- src - Django project and apps
- Dockerfile - Build instructions
- docker-compose.yaml - Multi-service orchestration

## Customization
- Update the exchange API key in `exchange/helpers.py` and `exchange/tasks.py`
- Change periodic task schedule in celery.py

## Running Celery Locally

To run Celery worker and beat locally (outside Docker), use:

```sh
# Start Celery worker
celery -A src.celery_app.celery worker --loglevel=info

# In another terminal, start Celery beat
celery -A src.celery_app.celery beat --loglevel=info
```

Make sure Redis and PostgreSQL are running and your environment variables are set.

