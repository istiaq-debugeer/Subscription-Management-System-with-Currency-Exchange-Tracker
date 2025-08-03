from celery import shared_task
from django.utils import timezone
from .models import exchangeRate
# from celery_app.celery import celery


# @celery.task
@shared_task
def fetch_and_store_exchange_rate(base: str, target: str):
    import requests

    url = f"https://v6.exchangerate-api.com/v6/2c4750bcb38a08424d1f44ef/latest/{base}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        rate = data.get("conversion_rates", {}).get(target)
        print(rate)
        if rate:
            exchangeRate.objects.create(
                base_currency=base,
                target_currency=target,
                rate=rate,
                fetched_at=timezone.now(),
            )
            return {"base": base, "target": target, "rate": rate}
        else:
            return {"error": f"Target currency '{target}' not found in exchange data"}
    else:
        return {"error": f"Failed to fetch data. Status: {response.status_code}"}
