from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SubscriptionViewSet,
    SubscriptionCancelView,
    SubscriptionListView,
    PlanApiViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
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
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


