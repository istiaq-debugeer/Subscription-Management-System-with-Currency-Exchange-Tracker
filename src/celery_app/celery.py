import os
import django
from celery import Celery
from celery.schedules import crontab, schedule

# ✅ Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subscription_management.settings")  # change if needed
django.setup()


app = Celery(
    "subscription_management",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

app.config_from_object("django.conf:settings", namespace="CELERY")



app.conf.beat_schedule = {
    "fetch-exchange-rate": {
        "task": "exchange.tasks.fetch_and_store_exchange_rate",
        # Run every 30 seconds
        "schedule": schedule(30.0),
        "args": ("USD", "EUR"),
    },
}
app.autodiscover_tasks(['exchange'])
app.conf.timezone = "UTC"
app.conf.enable_utc = True
