from django.contrib import admin
from .models import ExchangeRate


# Register your models here.
@admin.register(ExchangeRate)
class ExchangeRateLogAdmin(admin.ModelAdmin):
    list_display = ["id", "base_currency", "target_currency", "rate", "fetched_at"]
    list_filter = ["base_currency", "target_currency"]
