from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import exchangeRateViewSet, exchangeRateApiview
from . import helpers
from django.http import JsonResponse

router = DefaultRouter()
router.register(r"exchange-rates", exchangeRateViewSet, basename="exchange-rate")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "get-exchange-rates/",
        exchangeRateApiview.as_view(),
        name="get-exchange-rates",
    ),
]
