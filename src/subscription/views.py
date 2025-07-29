from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Plan, Subscription
from .serializers import PlanSerializer, SubscriptionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return self.queryset.filter(user=user)
        return Subscription.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer.data


class SubscriptionCancelView(APIView):
    def post(self, request, *args, **kwargs):
        subscription_id = kwargs.get("subscription_id")
        try:
            subscription = Subscription.objects.get(
                id=subscription_id, user=request.user
            )
            subscription.status = "cancelled"
            subscription.save()
            return Response(
                {"status": "Subscription cancelled successfully."}, status=200
            )
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=404)
