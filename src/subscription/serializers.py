from rest_framework import serializers
from .models import Plan, Subscription


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["id", "plan", "start_date", "end_date", "status"]  # exclude user

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
