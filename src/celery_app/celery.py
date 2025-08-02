# app/celery.py
from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "subscription_management",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

celery.conf.timezone = 'UTC'
celery.conf.enable_utc = True


# Schedule the exchange rate fetch task every hour
celery.conf.beat_schedule = {
    'fetch-exchange-rate-every-hour': {
        'task': 'exchange.tasks.fetch_and_store_exchange_rate',
        'schedule': crontab(minute=0, hour='*'),  # every hour
        'args': ('USD', 'EUR'),  # Change as needed
    },
}

celery.autodiscover_tasks(["exchange", "subscription"])