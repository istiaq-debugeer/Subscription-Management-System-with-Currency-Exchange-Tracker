from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import exchange_rates_api
from . import helpers
from django.http import JsonResponse

# router = DefaultRouter()
# router.register(r'exchange-rates', ExchangeRateViewSet, basename='exchange-rate')


urlpatterns = [
    # path('', include(router.urls)),
    path('get-exchange-rates/', exchange_rates_api, name='get-exchange-rates'),
]
