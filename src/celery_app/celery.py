# app/celery.py
from celery import Celery
from celery.schedules import crontab


celery = Celery(
    "notification_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    # include=[
    #     "app.tasks.email",
    #     "app.tasks.instant_notification",
    #     "app.tasks.periodic_notification",
    # ]
)

celery.conf.timezone = 'UTC'
celery.conf.enable_utc = True

celery.conf.task_routes = {
    "app.tasks.instant_notification.send_instant_notification": {
        "queue": "instant_notification"
    },
}

celery.conf.beat_schedule = {
    'run-every-day': {
        'task': 'app.tasks.periodic_notification.periodic_notification_task',
        'schedule': crontab(hour=2, minute=0),  # 2:00 AM UTC == 8:00 AM BST
        # 'schedule': 120.0,
        # 'schedule': 300.0,
    },
}

celery.autodiscover_tasks(["app.tasks"])