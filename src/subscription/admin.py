from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Plan, Subscription
from exchange.models import ExchangeRate


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "duration_days"]
    search_fields = ["name"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "plan", "start_date", "end_date", "status"]
    list_filter = ["status", "plan"]
    search_fields = ["user__username"]
