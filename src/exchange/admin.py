from django.contrib import admin
from .models import exchangeRate


# Register your models here.
@admin.register(exchangeRate)
class exchangeRateLogAdmin(admin.ModelAdmin):
    list_display = ["id", "base_currency", "target_currency", "rate", "fetched_at"]
    list_filter = ["base_currency", "target_currency"]
