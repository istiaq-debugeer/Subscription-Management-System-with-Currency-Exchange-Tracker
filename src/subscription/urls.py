from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SubscriptionViewSet,
    SubscriptionCancelView,
    SubscriptionListView,
    PlanApiViewSet,
)

router = DefaultRouter()
router.register(r"subscriptions", SubscriptionViewSet, basename="subscription")
router.register(r"plan", PlanApiViewSet, basename="plan")
urlpatterns = [
    path("", include(router.urls)),
    path(
        "subscriptions/<int:subscription_id>/cancel/",
        SubscriptionCancelView.as_view(),
        name="subscription-cancel",
    ),
    path("get_list/", SubscriptionListView, name="subscription-list"),
]
